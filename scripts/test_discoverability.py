"""Regression tests for the local audit's failure detection; no network calls."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import check_discoverability as audit

class AuditTests(unittest.TestCase):
    def run_fixture(self, canonical=None, robots='User-agent: *\nAllow: /', extra_sitemap='', extra_html=''):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            canonical = audit.BASE if canonical is None else canonical
            (root/'index.html').write_text('<title>Test</title><meta name="description" content="Test"><link rel="canonical" href="'+canonical+'">'+extra_html)
            (root/'robots.txt').write_text(robots+'\nSitemap: '+audit.BASE+'sitemap.xml\n')
            (root/'sitemap.xml').write_text('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>'+audit.BASE+'</loc></url>'+extra_sitemap+'</urlset>')
            out=root/'result.json'
            with patch.object(audit,'ROOT',root), patch('sys.argv',['check','--output',str(out)]), contextlib.redirect_stdout(io.StringIO()):
                code=audit.main()
            return code,json.loads(out.read_text())['findings']
    def test_valid_site(self):self.assertEqual(self.run_fixture(),(False,[]))
    def test_missing_intended_page(self):
        # A non-empty sitemap that omits the valid root must fail completeness.
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'index.html').write_text('<title>Test</title><meta name="description" content="Test"><link rel="canonical" href="'+audit.BASE+'">')
            (root/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+audit.BASE+'sitemap.xml')
            (root/'sitemap.xml').write_text('<urlset><url><loc>'+audit.BASE+'missing.html</loc></url></urlset>')
            out=root/'result.json'
            with patch.object(audit,'ROOT',root), patch('sys.argv',['check','--output',str(out)]), contextlib.redirect_stdout(io.StringIO()):
                audit.main()
            self.assertTrue(any('intended canonical page missing' in x for x in json.loads(out.read_text())['findings']))
    def test_external_sitemap(self):
        code,findings=self.run_fixture(extra_sitemap='<url><loc>https://example.org/</loc></url>')
        self.assertTrue(code);self.assertTrue(any('owned by this repository' in f for f in findings))
    def test_wrong_canonical(self):self.assertTrue(self.run_fixture(canonical='https://example.org/')[0])
    def test_blocked_robots(self):self.assertTrue(self.run_fixture(robots='User-agent: *\nDisallow: /')[0])
    def test_noindex(self):self.assertTrue(self.run_fixture(extra_html='<meta name="robots" content="noindex">')[0])
    def test_broken_fragment(self):self.assertTrue(self.run_fixture(extra_html='<a href="#missing">broken</a>')[0])
    def test_redirect_not_in_sitemap(self):self.assertTrue(self.run_fixture(extra_html='<meta http-equiv="refresh" content="0; url=https://example.org/">')[0])

if __name__=='__main__':unittest.main()
