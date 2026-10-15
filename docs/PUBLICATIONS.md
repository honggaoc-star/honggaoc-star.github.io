# Publication navigation

Draft candidate prepared October 15, 2026, from website main `3d921d30a86fe1e339a360de6defdff7c30389c6` (PR #27).

## Reader routes and authority

- Homepage: six Research Questions categories, four featured works, three representative Additional Papers, and the unchanged Essays & Reflections area.
- [Publications](../publications/index.html): the complete current reader-facing inventory, with concise entries and no abstracts or duplicated manuscript files.
- Existing paper overviews: motivating questions, explanations, approved abstracts, citations, and publication links.
- Authoritative repositories: recommended manuscript editions, Word copies, history, and research records.

The directory is the maintained public inventory. The repository README links to it instead of repeating the full publication list. The internal Portfolio Register continues to document project homes, status boundaries and historical context. The complete record is not a claim that these independent works form one research series.

## Coverage and sources

The directory covers 17 current publications:

| Directory section | Coverage | Edition/status handling |
|---|---|---|
| Working papers | Seven Research-Lab working papers | Four v1.1 and three v1.0 editions, all dated 2026 |
| AI research publications | Four AI-Risk-Management publications and the independent Evidence-Centered AI Evaluation paper | Analytical Framework v1.3 and Plausible Mechanisms v1.2 are research manuscripts; AI Provenance v1.1 is a paper; Return-Weighted Risk v1.2 and Evidence-Centered AI Evaluation v1.1 are working papers |
| Essays | Four published Research-Lab essays | Each v1.1, 2026 |
| Longer manuscripts | How We Get Where We Are | Completed manuscript v1.1, 2026 |

The section labels follow existing publication types and project homes. Working papers maintained by AI-Risk-Management or Practical AI Evaluation are shown in AI research with their working-paper status explicitly retained; they are not repeated in another section.

Sources checked directly:

- [Research-Lab publication inventory](https://github.com/honggaoc-star/Research-Lab/blob/main/README.md) and [Working Papers](https://github.com/honggaoc-star/Research-Lab/blob/main/Working-Papers/README.md).
- [AI-Risk-Management research and publication guide](https://github.com/honggaoc-star/AI-Risk-Management/blob/main/README.md).
- All 16 individual publication READMEs linked by the directory, together with the existing approved homepage and overview metadata for full titles/subtitles.
- [Evidence-Centered AI Evaluation](https://honggaoc-star.github.io/practical-ai-evaluation/working-paper.html), whose web edition identifies Working Paper v1.1, July 2026. Its [source record](https://github.com/honggaoc-star/practical-ai-evaluation/blob/main/working-paper.html) is linked separately. No separate Word/PDF edition is linked from that web publication, so none is inferred here.

All 16 existing PDF destinations and research records remain authoritative. Word access remains through each record; the linked current Word files were also fetched during validation. GitHub PDF links may open an HTML file viewer. The separate HTML evaluation paper is labeled Read paper. All five existing overview routes remain available from the directory. No DOI, exact publication day, peer-review status, citation tag or indexing claim is added.

Earlier scholarly publications remain accessible through the existing Earlier Research link. Superseded editions and internal development drafts are not promoted into current entries; their established records remain accessible.

## Homepage selection — PR #28 checkpoint

Additional Papers is reduced from eight to three, retaining existing wording:

- **Why Important Questions Are Often Difficult** introduces inquiry and understanding, balancing the AI-focused featured works.
- **Inequality in the Context of a Mechanical Model of Society** represents social outcomes and the distinction between correction and remaining possibilities.
- **A Second Life** provides an accessible entry into opportunity, choices and human experience.

This selection represents different reader questions rather than simply the newest releases. Governance, Prediction–Attribution, Apparent Complexity, Plausible Mechanisms and Evidence-Centered AI Evaluation remain in the complete directory. Existing topical and applied-work links to these works are retained where present. View all publications appears directly below Additional Papers; Browse publications and the primary Publications navigation also open the directory. The homepage `#publications` anchor remains Selected Publications.

## Design and compatibility

Reuse the existing content width, typography, entry list, colors and focus/skip-link conventions. Four section links support scanning; anchor offsets on this page prevent the sticky header from hiding section headings. Every repeated reading/record/overview link has a work-specific accessible name. There are no filters, search widgets, new cards, client-side JavaScript or shared stylesheet changes.

Publications points to `/publications/` in current primary menus and overview footers. Support-page menus gain only that link; their existing labels and destinations are retained. Three immediate redirect compatibility pages retain their original contents and targets. Existing overview content, abstracts, citation metadata and canonicals are unchanged. No research-program transition statement is introduced.

## Candidate validation

- Complete inventory: 17 unique entries, correct current versions/statuses, all five overview links.
- 50 reading, current Word and source/research-record destinations returned HTTP 200; PDF and DOCX signatures checked where applicable.
- Eight existing discoverability regression tests pass.
- Candidate discoverability audit: 18 canonical sitemap entries, 222 local links, 39 network checks, zero findings. All original 17 sitemap entries retained.
- Existing overview content and metadata, About content, all four featured cards, six Research Questions categories, other homepage sections and all existing homepage IDs preserved.
- Chromium checks at 1440px, 390px and 320px across all 18 canonical routes (54 combinations): no horizontal overflow and Publications available in each primary menu. Homepage/directory keyboard traversal, visible focus, skip links, heading hierarchy, work-specific link names and sticky-header section offsets passed. Rendered desktop/mobile screenshots inspected.
- Twenty relative documentation links resolve. These are accessibility-basics checks, not full screen-reader or cross-browser certification.

Run from the repository root:

```sh
python -m unittest discover -s scripts -p test_discoverability.py
python scripts/check_discoverability.py --network --external-only --output ../publications-candidate.json
```

These checks validate the local draft and existing external destinations. After approval, merge and successful Pages deployment, run `--live --network`, require 18 canonical sitemap entries, and verify the live directory and homepage. No live deployment, Search Console processing or indexing result is claimed for this draft.

## Maintenance

For a new release, verify the controlling record before changing the directory entry. Retain one current entry per work, point historical editions to their records, and add an overview link only when that page exists. The homepage may remain selective; adding a directory entry does not require a new homepage entry or a category redesign. Update this coverage note and the sitemap only when their respective scope changes.

## Current overview coverage — October 15, 2026 candidate

The [remaining working-paper overviews](REMAINING-WORKING-PAPER-OVERVIEWS.md) complete all seven Research-Lab working-paper pages. Together with Analytical Framework, the directory links eight overview pages. The candidate sitemap has 21 canonical URLs; earlier counts above describe dated checkpoints. Source fidelity, hashes, navigation choices, and candidate validation are documented in the completion note. External PDF hosting and the omission of `citation_pdf_url` remain unchanged. Live deployment and indexing require separate evidence.

## Broad Reader Entry — current draft

Prepared from PR #29 merge `c42adbfa0ba17eeaaaad21ee0c70bc2684738014`. Earlier selection and validation sections above describe historical checkpoints.

Featured, in order: Why Important Questions Are Often Difficult; AI Evolution as an Advancing Approximation Frontier; Inequality in the Context of a Mechanical Model of Society; A Second Life. Additional Papers, in order: Prediction–Attribution Conjugacy in Adaptive Decision Problems; An Analytical Framework for Error and Hallucination in Deployed Generative AI Systems; The Value and Evolution of Governance.

This arrangement makes inquiry, AI development, social outcomes, and human experience visible in the prominent cards. The additional entries complement them with prediction and attribution, AI evaluation, and institutions. It is a set of reader entry points, not a ranking or a single research series. AI Provenance and Return-Weighted Risk remain in the complete directory and existing research-question links.

The heading remains Selected Publications, with this approved introduction:

> These publications offer starting points across different questions in my research. Each has its own scope, methods, and conclusions; the Publications directory lists all current works.

Existing homepage wording is reused, including the previously published Prediction–Attribution and Governance entries. Prediction–Attribution gains its established overview link. Analytical Framework is labeled Research Manuscript v1.3, consistent with its authoritative status. No manuscripts, abstracts, overview pages, About text, styles, canonical URLs, or sitemap entries change.

### Broad Reader Entry candidate validation

- Exactly four featured cards and three Additional Papers in the approved order, with no duplicate work and the exact approved section introduction.
- All seven PDF/overview/research-record link sets agree with the established overview pages. Previously approved questions and descriptions are reused.
- The homepage outside Selected Publications is unchanged; all IDs are preserved. The directory, eight overview pages, About, stylesheet, and 21-URL sitemap are unchanged.
- Eight regression tests pass. Candidate audit: 21 canonical URLs, 262 internal-link checks, 42 external network checks, zero findings.
- Chromium checks at 1440px, 390px and 320px pass horizontal-overflow, heading-hierarchy, keyboard traversal, visible-focus and skip-link checks. Rendered screenshots inspected for the four-card/three-entry relationship and mobile readability.
- This is local candidate validation, not public deployment or indexing evidence. No Search Console requests were made. After an approved merge, rerun the live audit and inspect the deployed homepage.
