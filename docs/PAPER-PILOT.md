# Paper discovery pilot

Phase 2 of [issue #20](https://github.com/honggaoc-star/honggaoc-star.github.io/issues/20), prepared October 11, 2026. Separate from Phase 1, which merged at `7acd2cd3f3d4fd3c5f6bc6ce56f72b3d3a218d15` and passed the deployed 12-page audit.

## Sources and authority

Two static, crawler-readable pages present the approved title, full abstract, author, manuscript month/year, current version, status, citation, and links:

- `papers/why-important-questions-are-often-difficult.html`: public working paper v1.1; abstract and title/subtitle from page 1 of the approved PDF.
- `papers/analytical-framework-error-hallucination.html`: research manuscript v1.3; abstract and title from page 1 of the approved PDF. The older abstract labeled historical in its repository README is deliberately not used or changed.

[Source metadata](discoverability/pilot-sources.json) records the exact abstract, authoritative record, download URL, and approved PDF hash for each. The title pages show September 2026, without a day. Accordingly, visible dates retain September 2026 and `citation_publication_date` uses only the verified year, `2026`; it does not invent a publication day or use the website deployment date. The working-paper/manuscript status does not imply journal publication, peer review, arXiv acceptance, or empirical validation.

The motivating question on each page is retained from the existing homepage. Suggested citations use the approved title, author, year, version, and manuscript status. Related links follow established project relationships. Repository records remain authoritative for Word copies, versions, history, rights, and status; these pages are discovery surfaces, not duplicate manuscript homes.

## PDF response and scholarly metadata boundary

GitHub `/blob/` destinations are HTML file viewers. The two new download links use `raw.githubusercontent.com`: both returned HTTP 200, `%PDF-` signatures, and SHA-256 hashes matching the approved release. GitHub serves them with `application/octet-stream`, so the buttons say Download PDF. The existing homepage PDF-viewer links remain unchanged.

The pilot adds `citation_title`, `citation_author`, and `citation_publication_date`. It deliberately omits `citation_pdf_url`: [Google Scholar's inclusion guidance](https://scholar.google.com/intl/en/scholar/inclusion.html) requires that value to reference a PDF in the same directory as the HTML abstract. External repository hosting does not meet that condition. The author chose to retain that hosting and omit the tag; no PDFs are duplicated. These pages must not be described as fully Scholar-compatible or as guaranteeing PDF/abstract association or indexing.

Structured data was considered separately and deferred. No DOI, journal, affiliation, acceptance date, or unsupported status is added. Search Console submission, ORCID, ResearchGate, and Scholar accounts remain outside this implementation.

## Navigation and sitemap

The homepage keeps its existing title-to-PDF and repository links. Each pilot gets an additional Abstract and citation link in Selected Publications and a Paper overview link in its existing topical card. The 12 existing sitemap entries are retained, with two new page URLs added. No route, fragment, stylesheet, publication file, or historical record is removed or changed.

The audit now checks completeness: every non-redirect, self-canonical HTML page allowed by robots and without noindex must appear in the sitemap. It also checks direct GitHub PDF signatures. The regression suite includes a missing-canonical-page test.

```sh
python -m unittest discover -s scripts -p test_discoverability.py
python scripts/check_discoverability.py --network --external-only --output ../pilot-candidate.json
```

`--external-only` tests external destinations while validating local new routes, so draft pages are not incorrectly tested as if already deployed. After approved deployment, run `--live --network` without that flag and require all 14 sitemap entries and all routes to pass. Never interpret the candidate check as a deployment or indexing result.
