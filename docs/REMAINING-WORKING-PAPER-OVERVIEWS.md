# Remaining Research-Lab working-paper overviews

Draft candidate prepared October 15, 2026, from website main `93f27199a615fadc4ebf7605587205193669a175` (PR #28). This completes reader-oriented overview coverage for the seven independent Research-Lab working papers. The existing Analytical Framework page makes eight overviews in total.

## Approved sources

Research-Lab main was verified at `6d0baeb7fefdd9d8d34176ce5a6b457e3fe4c843`. Each paper's current publication README identifies v1.1 as the recommended public working-paper release. Honggao Cao is the author. AI Evolution and Prediction–Attribution are dated October 2026; The World Might Not Be as Complex as We Thought is dated September 2026 and retains its approved subtitle.

[Source metadata](discoverability/remaining-working-paper-sources.json) records exact titles, subtitle, author, month/year, status, versions, abstract paragraphs, authoritative URLs, byte counts, source commit, and six artifact hashes. All six current Word/PDF downloads matched the manifest inside the approved publication ZIP, whose SHA-256 is `796c425889cce2efc8115021bbff4f5a074b028f42d1c50a2f601c3f6cf70b70`.

The Word paragraphs and PDF text agree after normalizing PDF line wrapping and whitespace. Title-page renders were inspected. The website copies the approved Word abstract paragraphs with HTML escaping only: four paragraphs for AI Evolution, one for Prediction–Attribution, and one for Apparent Complexity. No wording, punctuation, or paragraph boundaries are rewritten. Publication records and manuscript title pages agree; no material source discrepancy was found.

| Paper | Word SHA-256 | PDF SHA-256 |
|---|---|---|
| AI Evolution as an Advancing Approximation Frontier | `4da33410139c8f303bc2e8b7589e85761526034bd161348743d676ece6936a73` | `63ed41bfc34bde8be295d705b3d356bcedb370ad0be10109578904dd7a5fd3f8` |
| Prediction–Attribution Conjugacy in Adaptive Decision Problems | `ea216f37420543999ba6acd0d20d8d6e3584a16a064151e8979384fef36cbf8e` | `fbfdfe56674f3967c683ce454f3437ec0b9a685a43a7b17882f6175059d2ae45` |
| The World Might Not Be as Complex as We Thought | `b07df14bf42924f9ae2110db22a41f424b9d1e8ed36fa24557dbe56d2afa0384` | `b2f024e4e9feffb30ba80894dbc3bfac399eed7b986f73c7888bb36a6a50fecd` |

## Reader entry and navigation

- AI Evolution distinguishes possible sources of a remaining development limitation and the difficulty of diagnosing it while development continues. It leaves capability ceilings and architectural succession open.
- Prediction–Attribution explains why a useful forecast can leave an action unresolved, when competing accounts can be distinguished, and why successful intervention can weaken a predictive signal.
- Apparent Complexity distinguishes a change in observation conditions, connecting available information, and relating accounts at different scales. Better explanation need not resolve the practical difficulty.

Each page follows the existing HTML structure and shared stylesheet: question, concise introduction, complete abstract, publication metadata, PDF download, research record, and bounded suggested citation. Only AI Evolution adds related reading: the Prediction–Attribution framework it explicitly uses. That link goes to the current overview, without changing the manuscript's historical reference to v1.0. No speculative related-reading list is added to the other pages.

The Publications directory retains all 17 works, all four groups, all existing reading/record destinations, and five existing overview links. Three links are added. The homepage adds only one overview link in the existing AI Evolution featured card. Existing research-card links remain as they are to avoid crowding; the other two new overviews are accessible through the complete directory. Six research categories, four featured selections, three Additional Papers, existing anchors, and all other homepage content remain intact.

## Scholarly metadata boundary

The conventions in [PAPER-PILOT.md](PAPER-PILOT.md), [THREE-PAPER-OVERVIEWS.md](THREE-PAPER-OVERVIEWS.md), and [DISCOVERABILITY.md](DISCOVERABILITY.md) remain in force. Citation metadata includes approved title, author, and verified year; visible dates retain month/year. Suggested citations identify Working paper v1.1 without a DOI, journal, peer-review status, affiliation, or invented publication day.

PDF buttons use verified raw Research-Lab URLs; the research records provide Word copies and history. Manuscripts remain in Research-Lab. No `citation_pdf_url` is added because external PDF hosting does not meet the documented Google Scholar same-directory requirement. These pages do not establish Google or Google Scholar indexing. No Search Console requests are performed.

## Candidate verification

- All six downloaded artifacts matched approved hashes and byte counts; all three publication records were accessible.
- Exact abstract paragraphs and metadata verified against the approved sources.
- The five existing overview files, About page, and shared CSS are unchanged. Removing the one added homepage link and the three added directory links reproduces their baseline content exactly.
- All eight overviews are linked from the 17-entry directory. All 18 existing sitemap URLs remain; exactly three new self-canonical pages produce 21 URLs.
- Eight existing discoverability regression tests pass. Local candidate audit: 24 HTML routes including three compatibility redirects, 21 canonical sitemap URLs, 260 internal-link checks, 42 external network checks, zero findings.

- Headless Chromium passed 63 route/width combinations across 21 canonical routes at 1440px, 390px and 320px: no horizontal overflow and consistent primary navigation. The three new pages, homepage, and directory additionally passed heading hierarchy, keyboard traversal, visible focus, and skip-link checks; directory section anchors clear the sticky header. Desktop/mobile renders were inspected for readable titles, abstracts, links, and buttons.
- All 33 relative links in the changed documentation resolve. These checks cover accessibility basics, not full screen-reader or cross-browser certification.

Reproduce the checks from the website repository root:

```sh
python -m unittest discover -s scripts -p test_discoverability.py
python scripts/check_discoverability.py --network --external-only --output ../remaining-working-paper-candidate.json
```

These results describe an undeployed candidate. After review, approved merge, and successful Pages deployment, run `--live --network`, require 21 canonical URLs, and compare the live abstracts, metadata, and publication links with the recorded sources. Deployment and actual indexing remain separate checks.
