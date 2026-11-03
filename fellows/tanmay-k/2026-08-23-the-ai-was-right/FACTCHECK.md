# FACTCHECK — The AI Was Right. That Was the Problem.

Week 19 · Humanitarians AI · Tanmay Kulkarni · audited 2026-08-24

Every factual, numerical, dated and product claim in the shipped cut, spoken **or on
screen**. Card text is audited alongside narration (PLAYBOOK §1) — a fact-check that only
scans `narration_text` misses claims sitting in a visual prop, and this film had two.

Verdicts: **SUPPORTED** · **QUALIFY** (true but needs the stated framing) · **UNSUPPORTED** ·
**ILLUSTRATIVE** (labelled as such on screen).

Nothing here is inherited from the source folder. Its `PEDAGOGY.md` cited `../RECEIPTS.md`
for its claim table; that file does not exist anywhere in the repo, so every claim was
re-sourced from scratch. Detail in `SOURCE-ANALYSIS.md` §3.

---

## Spoken claims

| Beat | Claim | Verdict | Source |
|---|---|---|---|
| B02 | "sync licensing" is the term for getting a song into film/TV | SUPPORTED | Standard industry usage; consistent across all sources reviewed |
| B03 | Songview is a free public database | SUPPORTED | songview.com, read directly |
| B03 | "thirty-eight million songs" | SUPPORTED | songview.com states 38M+ works |
| B03 | Songview is run by ASCAP and BMI | SUPPORTED | songview.com; ASCAP/BMI joint announcement, 2017 |
| B03 | It holds who wrote and who owns a song | SUPPORTED | songview.com — writers, publishers, ownership shares |
| B03 | It does **not** hold which show/scene a song appeared in | SUPPORTED | songview.com; no placement field described. Confirmed empirically — none of the ten experiment claims was resolvable there |
| B03 | Placement data lives "where the public types it in" | SUPPORTED | Tunefind entries are community-submitted and community-voted; verified in-browser 2026-08-23 |
| B04 | Ten supervisor/show/song claims were requested with no search | SUPPORTED | `experiment/01-COLD-BRIEF.md`, frozen before verification |
| B04 | "Eight out of ten held up" | SUPPORTED | `experiment/02-VERIFICATION.md` — 8 supported, 1 unverified, 1 wrong |
| B04 | The two failures were the two lowest-confidence claims | SUPPORTED | Confidence recorded at generation time, before checking |
| B05 | Breaking Bad's finale ends on "Baby Blue" | SUPPORTED | Wikipedia "Felina"; Rolling Stone |
| B05 | Thomas Golubić was Breaking Bad's music supervisor | SUPPORTED | Rolling Stone; Wikipedia |
| B05 | The episode is "Felina" | SUPPORTED | Wikipedia |
| B05–B06 | Golubić did **not** choose the song; Vince Gilligan did | SUPPORTED | Rolling Stone — Gilligan's idea; Golibić proposed alternate "blue" songs, all rejected |
| B07 | "ten claims, one model, one try — a demonstration, not a study" | SUPPORTED | Self-describing; n=10, single run, single model, no repeats |
| B08 | Tunefind published a warning in April 2025 | SUPPORTED | tunefind.com blog, dated 8 April 2025, read in full |
| B08 | People impersonated Tunefind, promising placements for money | SUPPORTED | Same post, verbatim |
| B08 | Those emails were convincing because they referenced real shows | SUPPORTED | Same post: "may even include fake licensing agreements or references to real shows" |
| B09 | "Music Supervisor Verified" means the supervisor confirmed it | SUPPORTED | Verified in-browser, logged out, 2026-08-23 — distinct badge with its own asset |
| B09 | "Questions" means the entry is disputed | SUPPORTED | Same check — "Questions (2)" section with an "Ask a Question" control |

## On-screen claims (card and prop text)

| Beat | On screen | Verdict | Note |
|---|---|---|---|
| B01, B07 | `modelLabel: Opus 5` | SUPPORTED | The experiment ran on Claude Opus 5. The component's default read `Fable 5`; corrected, or it would have implied a model we did not use |
| B03 | "Songview · ASCAP + BMI · 38M+ works" | SUPPORTED | As above |
| B03 | "Placement sites · typed in by the public" | SUPPORTED | As above |
| B03 | "Release metadata / Usually right, rarely disputed" (middle band) | **QUALIFY** | Reasonable and uncontroversial, but not separately sourced. It is scene-setting between two sourced bands, not a load-bearing claim |
| B04 | Eight named show/song rows | SUPPORTED | Each individually verified — `experiment/02-VERIFICATION.md` |
| B04 | "Supervisor A" / "Supervisor B" rows | **ILLUSTRATIVE, anonymised** | Deliberate. The two failed claims name real people; publishing a false claim beside a real name is unnecessary when the pattern is the teaching point |
| B04 | "n = 10 · one model · one run · not a rate" | SUPPORTED | On screen throughout the beat |
| B05 | "Golubić placed Baby Blue in the Breaking Bad finale." | **QUALIFY — intentionally** | Presented as the *claim under test*, in quotation marks, and immediately shown to be misleading. That is the beat's subject |
| B06 | "I thought it was an odd little love song." | SUPPORTED | Verbatim, Thomas Golubić, Rolling Stone — attributed in-beat |
| B08 | "…may even include fake licensing agreements or references to real shows." | SUPPORTED | Verbatim, Tunefind, 8 April 2025 — attributed in-beat |
| B09 | Three label states with meanings | SUPPORTED | Verified in-browser; card carries "Tunefind, checked 23 Aug 2026" |

## Claims deliberately **not** made

Recorded because each was in an earlier draft or the source material, and each failed a check:

| Claim | Why it was cut |
|---|---|
| "No legitimate sync company ever charges artists" | Widely repeated in trade blogs. The **GMS Code of Conduct**, read directly, contains no such rule, and there is **no FTC alert** specific to music placement. Sound advice, not an enforceable standard. Replaced with the honest and stronger framing: *nobody is checking this for you* |
| "80% accurate" | Never stated. n=10 does not support a percentage; the film says "eight out of ten" |
| Any claim that the AI "lied" or hallucinated | B07 states the opposite: every fact checked out |
| Anything inherited from the source's `RECEIPTS.md` | The file does not exist |

## Dated and version-sensitive claims

- **Tunefind badge states** — verified 2026-08-23. A product UI can change; the on-screen
  card is dated for that reason.
- **Songview scale (38M+)** — will grow. Stated as "thirty-eight million," which stays
  defensible as a floor.
- **"Back in April 2025"** — B08 originally said "Last April," which on a 2026 upload would
  read as April 2026 and contradict the card beside it. Changed to the absolute date so the
  spoken and printed dates agree.

## Outstanding

**[EDIT, optional] B04's sources are not on screen.** The results table and the `n = 10`
caveat are visible, so the production gate passes, but the sources that settled the eight
(Rolling Stone, Variety, TheWrap, Songview) appear nowhere in frame. A viewer can verify the
claim's shape, not its content. Cheapest fix is a description link to
`experiment/02-VERIFICATION.md`. Carried since review 1 and accepted.

## Method

Claims were extracted from `narration_text` **and** from every `shot.remotion.props` string,
then checked against primary sources where one exists. Where a primary could not be
retrieved by tooling, it was opened by hand in a browser and the result recorded — that is
how the Tunefind claims were settled, after `WebFetch` returned 403 on all three pages.

Full evidence: `RESEARCH.md` (claim table with confidence levels) and `experiment/` (the
frozen cold brief and its verification).
