# Three working-paper overviews — draft candidate

Prepared October 15, 2026. This extends the reader-oriented structure established by PR #26 without changing the two pilot pages.

## Authority and source fidelity

Research-Lab PR #22 merged at `6d0baeb7fefdd9d8d34176ce5a6b457e3fe4c843`. Its three independent Working Paper v1.0 releases are dated October 2026 and authored by Honggao Cao:

- *Inequality in the Context of a Mechanical Model of Society: Nature, Nurture, and the Separation of Mechanism from Correction*.
- *The Value and Evolution of Governance*.
- *A Second Life: Opportunity, Choice, and Luck Along the Roads Not Taken*.

[Source metadata](discoverability/three-paper-sources.json) records titles, subtitles, complete abstract paragraphs, versions, author, dates, authoritative URLs, release commit, and approved Word/PDF hashes. All six files were downloaded from Research-Lab main and matched the approved release hashes and byte counts. Publication READMEs confirmed status and edition. The manuscripts were read for the motivating questions, explanatory introductions, and limits; this is not a renewed substantive review.

Abstracts are copied verbatim from the approved Word paragraphs, with HTML escaping only. Governance retains its three abstract paragraphs. The manuscripts' use of “essay” is retained within the abstracts; Working Paper v1.0 is the authoritative repository publication status. Suggested citations include the approved full titles and month/year without inventing a day, affiliation, DOI, journal, or peer-review status.

Research-Lab remains authoritative for all publication assets and histories. New overview buttons use verified raw PDF destinations; Word copies are reached through each research record. The only related-reading section is on A Second Life, linking two works explicitly discussed and cited in the manuscript. The other two pages do not add speculative connections.

## Navigation decision

Option A is used: three concise entries in Additional Papers, each with a motivating question, one-sentence description, direct PDF title link, overview link, and research-record link. The four featured cards, six Research Questions categories, and Essays & Reflections remain unchanged. The list grows from five to eight entries, without three additional cards or duplicate topical summaries.

Option B would make a separate complete directory easier to scan as the portfolio grows, but would introduce another route, an additional navigation step, and another inventory to maintain. For three additions, the existing list remains usable and provides the smaller meaningful improvement. Reconsider a directory if later releases make this list difficult to navigate; it is not part of this draft.

The original 13 approved editions, Evidence-Centered AI Evaluation, applied work, and all existing homepage articles and links are retained. With these three additions, the homepage provides 16 approved editions plus the separate Evidence-Centered AI Evaluation paper. The XML sitemap retains its original 14 entries and adds three, for 17 canonical pages.

## Research direction

A short Current Direction section on About follows Research Approach. Its text is:

> I regard Phase I of my research as provisionally complete: a period focused primarily on analytical frameworks, perspectives, and conceptual understanding. In Phase II, I intend to place greater emphasis on practically meaningful problems, beginning with an investigation of machine-learning explainability. This is a shift in emphasis within independent inquiries, not a resolution of all earlier questions. Earlier ideas remain available to inform the work, but need not determine its conclusions.

This wording comes from the author's instructions, not an inferred publication claim. It neither reopens closed projects nor claims completed explainability results. These research-emphasis phases are distinct from the website discoverability implementation phases in issue #20.

## Discovery boundary and verification

The conventions in [PAPER-PILOT.md](PAPER-PILOT.md) remain in force: citation title, author and verified year only; no `citation_pdf_url` for externally hosted PDFs and no manuscript copies on this website. External hosting does not satisfy the documented Google Scholar same-directory requirement. Technical accessibility does not establish indexing, ranking, or Scholar inclusion.

Candidate checks:

- Eight existing discoverability regression tests pass.
- Candidate audit: 17 sitemap entries, 190 local links, 39 network destinations, zero findings.
- All six authoritative Word/PDF downloads match approved hashes and sizes; all three publication records are accessible.
- Exact abstract paragraphs, citation title/author/year, canonical URLs, version/status, and PDF/record destinations checked against source metadata.
- Existing homepage articles, prior hrefs and IDs, both pilot pages, and shared CSS preserved.
- Headless Chromium checks passed for all five changed/new HTML pages at 1440px, 390px and 320px (15 combinations): no horizontal overflow, one H1, sequential headings, named primary navigation, keyboard-reachable links with visible focus, working skip links, and sticky headers. Rendered screenshots were inspected for readable titles, abstracts, buttons and layout.
- These are browser and accessibility-basics checks, not a full screen-reader or cross-browser certification. No live deployment or new indexing result is claimed.

Reproduce the route and network audit from the repository root:

```sh
python -m unittest discover -s scripts -p test_discoverability.py
python scripts/check_discoverability.py --network --external-only --output ../three-paper-candidate.json
```

This is an undeployed draft. After approval and deployment, run `--live --network` without `--external-only`, require 17 sitemap entries, and verify the three live abstracts and publication destinations. Search Console processing and indexing require separate live evidence.
