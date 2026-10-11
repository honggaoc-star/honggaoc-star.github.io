"""Audit local or deployed site metadata, sitemap, routes, and publication links.
Python 3 standard library only. Exit 1 means findings; network errors are failures.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urljoin, urlsplit, unquote
from urllib.request import Request, urlopen
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET

BASE = 'https://honggaoc-star.github.io/'
ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.ids, self.canonicals, self.descriptions = [], [], [], []
        self.robots, self.refresh, self.title = '', '', ''
        self.in_title = False
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'title': self.in_title = True
        if tag in ('a', 'link') and 'href' in a: self.links.append(a['href'])
        if tag in ('img', 'script') and 'src' in a: self.links.append(a['src'])
        if tag == 'link' and 'canonical' in a.get('rel', '').split(): self.canonicals.append(a.get('href', ''))
        if tag == 'meta':
            name = a.get('name', '').lower()
            if name == 'description': self.descriptions.append(a.get('content', ''))
            if name in ('robots', 'googlebot'): self.robots += ' '+a.get('content', '').lower()
            if a.get('http-equiv', '').lower() == 'refresh': self.refresh = a.get('content', '')
    def handle_endtag(self, tag):
        if tag == 'title': self.in_title = False
    def handle_data(self, data):
        if self.in_title: self.title += data

def route(path):
    rel = path.relative_to(ROOT).as_posix()
    return rel[:-10] if rel.endswith('index.html') else rel

def local_path(url):
    u = urlsplit(url)
    if u.scheme != 'https' or u.netloc != urlsplit(BASE).netloc: return None
    p = ROOT / unquote(u.path.lstrip('/'))
    if p.is_dir(): p /= 'index.html'
    if not p.resolve().is_relative_to(ROOT.resolve()): return None
    return p if p.is_file() else None

def fetch(url):
    try:
        with urlopen(Request(url, headers={'User-Agent': 'ResearchWebsiteAudit/1.0'}), timeout=40) as r:
            body = r.read()
            return {'url': url, 'final_url': r.url, 'status': r.status,
                    'x_robots_tag': r.headers.get('X-Robots-Tag', ''),
                    'content_type': r.headers.get('Content-Type', ''), 'body': body}
    except Exception as e:
        return {'url': url, 'error': str(e), 'body': b''}

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--live', action='store_true', help='Read deployed metadata/robots/sitemap, not local replacements')
    ap.add_argument('--network', action='store_true', help='Also fetch linked publication PDFs and records')
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    pages = sorted(p for p in ROOT.rglob('*.html') if '.git' not in p.parts and not p.name.startswith('google'))
    urls = [BASE+route(p) for p in pages]
    urls += [BASE+'robots.txt', BASE+'sitemap.xml']
    fetched = {}
    if args.live:
        with ThreadPoolExecutor(max_workers=6) as pool:
            fetched = {r['url']: r for r in pool.map(fetch, urls)}
    failures, inventory, parsed = [], [], {}
    def read(url, path):
        if not args.live: return path.read_text(encoding='utf-8')
        r = fetched[url]
        if r.get('status') != 200: failures.append(url+': HTTP failure '+r.get('error', str(r.get('status'))))
        return r['body'].decode('utf-8', errors='replace')
    robots = RobotFileParser(); robots.parse(read(BASE+'robots.txt', ROOT/'robots.txt').splitlines())
    if BASE+'sitemap.xml' not in (robots.site_maps() or []): failures.append('robots.txt lacks the site sitemap declaration')
    for p in pages:
        url = BASE+route(p); page = Page(read(url, p)); parsed[url] = page
        checks = []
        if not page.refresh:
            if len(page.canonicals) != 1 or page.canonicals[0] != url: checks.append('missing/non-self canonical')
            if len(page.descriptions) != 1 or not page.descriptions[0].strip(): checks.append('missing/duplicate description')
            if not page.title.strip(): checks.append('missing title')
        if len(page.ids) != len(set(page.ids)): checks.append('duplicate IDs')
        failures.extend(url+': '+c for c in checks)
        inventory.append({'url': url, 'path': p.relative_to(ROOT).as_posix(), 'title': page.title,
                          'canonical': page.canonicals, 'description': page.descriptions,
                          'meta_refresh': page.refresh, 'robots_meta': page.robots.strip(),
                          'robots_allowed': robots.can_fetch('Googlebot', url),
                          'http': {k:v for k,v in fetched.get(url, {}).items() if k != 'body'}, 'findings': checks})
    try: sitemap = [e.text for e in ET.fromstring(read(BASE+'sitemap.xml', ROOT/'sitemap.xml')).findall('{*}url/{*}loc')]
    except ET.ParseError as e: sitemap = []; failures.append('Invalid sitemap XML: '+str(e))
    if not sitemap: failures.append('Empty sitemap')
    if len(sitemap) != len(set(sitemap)): failures.append('Duplicate sitemap URLs')
    for url in sitemap:
        p = local_path(url)
        if urlsplit(url).fragment or urlsplit(url).query or p is None or url not in parsed:
            failures.append(str(url)+': sitemap URL is not a canonical HTML route owned by this repository'); continue
        pg = parsed[url]; header = fetched.get(url, {}).get('x_robots_tag', '').lower()
        if pg.refresh or pg.canonicals != [url] or any(x in pg.robots+' '+header for x in ('noindex', 'none')) or not robots.can_fetch('Googlebot', url): failures.append(url+': sitemap route is redirected/noncanonical/blocked')
        if args.live and fetched[url].get('final_url') != url: failures.append(url+': sitemap HTTP redirect')
    local_links, publication_urls, redirects = [], set(), []
    for url, pg in parsed.items():
        targets = list(pg.links)
        if pg.refresh:
            match = re.search(r'url\s*=\s*(.+)', pg.refresh, re.I)
            if match:
                target = urljoin(url, match[1].strip(' \"\'')); targets.append(target); redirects.append({'source':url,'target':target})
        for href in targets:
            target = urljoin(url, href); u = urlsplit(target)
            if u.scheme not in ('http','https'): continue
            path = local_path(target)
            if u.netloc == urlsplit(BASE).netloc and path:
                if u.fragment and path.suffix == '.html':
                    target_page = parsed.get(BASE+route(path))
                    if target_page and unquote(u.fragment) not in target_page.ids: failures.append(url+': missing fragment '+target)
                local_links.append(target)
            elif u.netloc == urlsplit(BASE).netloc and not any(u.path.startswith('/'+n+'/') for n in ('practical-ai-sense','practical-ai-evaluation','practical-life-sense')):
                failures.append(url+': missing local route '+target)
            if u.netloc == 'github.com' and any('/'+n+'/' in u.path for n in ('Research-Lab','AI-Risk-Management')) and (u.path.endswith('.pdf') or u.path.endswith('/README.md')): publication_urls.add(target)
    network = []
    if args.network:
        targets = publication_urls | {r['target'].split('#')[0] for r in redirects}
        targets |= {u.split('#')[0] for u in local_links} | set(sitemap)
        with ThreadPoolExecutor(max_workers=6) as pool:
            for r in pool.map(fetch, sorted(targets)):
                r.pop('body'); network.append(r)
                if r.get('status') != 200: failures.append(r['url']+': linked HTTP failure '+r.get('error', str(r.get('status'))))
    report = {'checked_at_utc':datetime.now(timezone.utc).isoformat(), 'mode':'deployed' if args.live else 'local candidate',
              'inventory':inventory, 'sitemap':sitemap, 'local_links_checked':len(local_links), 'meta_redirects':redirects,
              'network_checks':network, 'findings':failures, 'passed':not failures,
              'limit':'Checks technical accessibility and declared directives, not Google indexing, ranking, or Scholar inclusion.'}
    args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'mode':report['mode'],'pages':len(pages),'sitemap_urls':len(sitemap),'local_links':len(local_links),'network_checks':len(network),'findings':failures}, indent=2))
    return bool(failures)

if __name__ == '__main__': raise SystemExit(main())
