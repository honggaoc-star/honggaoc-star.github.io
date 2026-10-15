# Discoverability technical baseline

Phase 1 of [issue #20](https://github.com/honggaoc-star/honggaoc-star.github.io/issues/20), checked October 11, 2026. This is a technical accessibility audit, not evidence of Google indexing, ranking, or Google Scholar inclusion. Phase 2 paper landing pages remain a separate task.

## Before and candidate results

| Check | Deployed baseline | Local candidate |
|---|---|---|
| Content/redirect HTML routes | 15 accessible | Same 15 routes retained |
| Sitemap | 5 URLs, including 3 separate project sites | 12 canonical URLs owned by this repository |
| Canonical metadata | Missing on 10 non-redirect support pages | Added only where missing |
| Description metadata | Missing on 7 support pages | Added only where missing, from existing page content |
| Internal link/fragment checks | 118 | 128 (including new canonical tags) |
| Live URL checks | 39 passed | 43 passed |
| Audit findings | 20 metadata/sitemap findings | None |

Full before/after URL inventories, returned HTTP status and final URL, HTTP robots directives, HTML metadata, meta-refresh destinations, and findings are in [before-deployed.json](discoverability/before-deployed.json) and [after-local.json](discoverability/after-local.json).

The candidate report validates local HTML, robots, and sitemap, then checks the existing deployed targets for HTTP accessibility. It does **not** claim that candidate metadata is deployed. Re-run live mode after an approved merge and successful Pages deployment.

## Sitemap policy and preservation

Include the root, About, the three project exhibit pages under `projects/`, and the existing background, writing, method, and four status support pages. These are real content pages with self-canonical URLs and no observed noindex or crawling prohibition. Inclusion is not a claim that Google will index them.

Exclude the three meta-refresh compatibility pages (`projects/index.html`, `background/past-research.html`, `writing/life-views.html`), the Google verification file, fragment URLs, and independent project sites under `practical-ai-sense/`, `practical-ai-evaluation/`, and `practical-life-sense/`. Those project sites share the host but have separate repositories; their existing links remain untouched. Index aliases remain functional, while the sitemap prefers the directory URL for `index.html` pages.

All visible HTML bodies, existing titles and descriptions, homepage publication links, CSS, robots rules, verification file, licenses, and redirect behavior remain unchanged. No publication assets or paper landing pages are added. The 13 current PDFs and their paper-level records are accessible; the additional Research-Lab project record remains linked. No publication-status discrepancy was identified in this bounded check. Older support-page project descriptions are preserved historical context, not rewritten to describe current publication status.

## Repeatable checks

Python 3.9 or later; standard library only. From the repository root:

```sh
python -m unittest discover -s scripts -p test_discoverability.py
python scripts/check_discoverability.py --output /tmp/site-local.json
python scripts/check_discoverability.py --network --output /tmp/site-candidate-network.json
python scripts/check_discoverability.py --live --network --output /tmp/site-deployed.json
```

On Windows, use a writable output path such as `../site-local.json` instead of `/tmp/site-local.json`. Exit code 0 means the checks passed; 1 means findings or failed HTTP requests. Baseline live mode is expected to fail until this PR is deployed. Network failures are reported as failures, not interpreted as proof of indexing problems. `--network` fetches local navigation/canonical targets, sitemap URLs, redirect destinations, and GitHub publication PDF/README links; it is not a crawler for every external social/profile link. HTTP redirects are reflected in `final_url`; meta-refresh destinations are listed separately. The Google verification file is deliberately excluded from content-page metadata checks.

After approved deployment, require a passing live report, verify its 12 sitemap URLs, and retain the report separately from these dated snapshots. The checker evaluates declared technical directives and route existence; it does not replace Search Console inspection or implement every search engine's robots behavior.

## Manual Search Console steps (not performed)

1. Sign in with the owner's account and select the exact `https://honggaoc-star.github.io/` URL-prefix property. Confirm ownership in Search Console. The existing verification HTML file alone is not proof that ownership is currently verified; retain it unchanged. Follow Google's [ownership verification guidance](https://support.google.com/webmasters/answer/9008080).
2. After deployment and a passing live audit, open Sitemaps and submit `https://honggaoc-star.github.io/sitemap.xml`. Record the submission date, fetch/processing status, and discovered-URL count. Google describes submission as a hint, not a guarantee of crawling or indexing: [sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap).
3. Use [URL Inspection](https://support.google.com/webmasters/answer/9012289) for the root, About, and representative support pages. Record the indexed-page result separately from the live test, including fetch/crawl access, user-declared canonical, Google-selected canonical, and any exclusion reason. Request indexing only where appropriate and authorized.
4. Review indexing reports later and record actual platform evidence. Do not infer failure from search-tool errors or claim ranking/Scholar inclusion from an HTTP 200 result. ORCID, ResearchGate, Scholar profiles, and account-level changes remain separate manual tracks.

## Current overview coverage — October 15, 2026 candidate

The [remaining working-paper overviews](REMAINING-WORKING-PAPER-OVERVIEWS.md) complete all seven Research-Lab working-paper pages. Together with Analytical Framework, the directory links eight overview pages. The candidate sitemap has 21 canonical URLs; earlier counts above describe dated checkpoints. Source fidelity, hashes, navigation choices, and candidate validation are documented in the completion note. External PDF hosting and the omission of `citation_pdf_url` remain unchanged. Live deployment and indexing require separate evidence.
