# Sai Pranavi J.

**Role:** Fellow — Project 29 (`mycroft`) engineering + weekly AI/STEM explainer series
**Project:** Financial Regulatory Intelligence System (`mycroft`) + general AI/STEM video series
**GitHub:** [@SaiPranaviJeedigunta](https://github.com/SaiPranaviJeedigunta)
**Agreement period:** 1 Aug 2026 – 31 Oct 2026 (renewal requested, see [RENEWAL.md](RENEWAL.md))

## Executive summary

Nine weeks, two Brutalist videos a week: one real engineering fix in Project 29's regulatory
intelligence pipeline, one general AI/STEM topic explainer, each in 4K 16:9 and native 4K 9:16.
Eighteen reports total, all merged to `main` on GitHub, all GATE V-verified, all with
`FACTCHECK.md`/`SOURCES.md`/`BUILD-LOG.md`. The Project 29 work follows a documented 4-layer
hardening plan; this period closed out most of Layer 1 and shipped the first Layer 2 pieces
(Ollama-based LLM re-scoring and fallback classification), landing a 9th fix — a one-character
bug that silently dropped the alert email on exactly one high-priority item — the week this report
was written. See [RENEWAL.md](RENEWAL.md) for the full evidence table and open items, including a
previously-undiscovered naming-convention gap this review surfaced (full name used instead of
first-name-last-initial across all 18 reports).

## Quick review

- [Renewal request](RENEWAL.md) — evidence table, hours, open items ([index](renewal-requests/README.md))
- [Weekly hours](HOURS.md) — 20 hours every week, self-reported
- [Research plan for the requested period](research-plan.md)

## Voice

**Bella (`af_bella`)**, confirmed 2026-07-26. The name-based heuristic in
[`fellows/README.md`](../README.md) originally suggested Kore (`af_kore`),
but that voice doesn't exist in the installed `brutalist` toolkit — it only
ships two Kokoro voices, Onyx (`am_onyx`) and Bella (`af_bella`). Bella
matches the `hai` persona and `@HumanitariansAI` channel and is now locked in
for the full report series.

## Voice

**Bella (`af_bella`)**, confirmed 2026-07-26. The name-based heuristic in
[`fellows/README.md`](../README.md) originally suggested Kore (`af_kore`),
but that voice doesn't exist in the installed `brutalist` toolkit — it only
ships two Kokoro voices, Onyx (`am_onyx`) and Bella (`af_bella`). Bella
matches the `hai` persona and `@HumanitariansAI` channel and is now locked in
for the full report series.

## Reports

| Date | Title | Type | Project |
|---|---|---|---|
| 2026-07-26 | [Recovering the Silently Dropped Filings](2026-07-26-recovering-the-silently-dropped-filings/) | Weekly work | Project 29 — Financial Regulatory Intelligence System (`mycroft`) |
| 2026-07-27 | [How Facial Recognition Actually Works (And When It Shouldn't)](2026-07-27-how-facial-recognition-actually-works/) | Weekly STEM | General AI/STEM topic explainer |
| 2026-08-17 | [Why AI-Generated Code Still Needs a Human Who Understands the System](2026-08-17-why-ai-generated-code-still-needs-a-human/) | Weekly STEM | General AI/STEM topic explainer |
| 2026-08-30 | [The Update That Almost Lied About What It Sent](2026-08-30-the-update-that-almost-lied-about-what-it-sent/) | Weekly work | Project 29 — Financial Regulatory Intelligence System (`mycroft`) |
| 2026-08-30 | [Prompt Injection: The Vulnerability Hiding in Plain Text](2026-08-30-what-prompt-injection-actually-looks-like/) | Weekly STEM | General AI/STEM topic explainer |
| 2026-08-30 | [The Check That Never Once Fired](2026-08-30-the-check-that-never-once-fired/) | Weekly work | Project 29 — Financial Regulatory Intelligence System (`mycroft`) |
| 2026-09-07 | [The Synonyms the Classifier Never Learned](2026-09-07-the-synonyms-the-classifier-never-learned/) | Weekly work | Project 29 — Financial Regulatory Intelligence System (`mycroft`) |
| 2026-09-07 | [Embeddings: How AI Tells Similar From Different (When Keyword Matching Can't)](2026-09-07-embeddings-how-ai-tells-similar-from-different/) | Weekly STEM | General AI/STEM topic explainer |
| 2026-09-14 | [The Link That Pointed Nowhere](2026-09-14-b3-the-link-that-pointed-nowhere/) | Weekly work | Project 29 — Financial Regulatory Intelligence System (`mycroft`) |
| 2026-09-14 | [RAG: Why "Looking It Up" Doesn't Guarantee It's True](2026-09-14-rag-why-looking-it-up-isnt-enough/) | Weekly STEM | General AI/STEM topic explainer |
| 2026-09-22 | [The All-Clear That Wasn't All There](2026-09-22-the-all-clear-that-wasnt-all-there/) | Weekly work | Project 29 — Financial Regulatory Intelligence System (`mycroft`) |
| 2026-09-22 | [Hallucination: Why Sounding Sure Isn't the Same as Being Right](2026-09-22-hallucination-why-sounding-sure-isnt-being-right/) | Weekly STEM | General AI/STEM topic explainer |
| 2026-09-29 | [The Keyword That Cried Wolf](2026-09-29-the-keyword-that-cried-wolf/) | Weekly work | Project 29 — Financial Regulatory Intelligence System (`mycroft`) |
| 2026-09-29 | [Tokenization: Why AI Can't Count the Letters in Its Own Words](2026-09-29-tokenization-why-ai-cant-count-its-own-letters/) | Weekly STEM | General AI/STEM topic explainer |
| 2026-10-06 | [The Classifier That Learned When Not to Guess](2026-10-06-the-classifier-that-learned-when-not-to-guess/) | Weekly work | Project 29 — Financial Regulatory Intelligence System (`mycroft`) |
| 2026-10-06 | [Lost in the Middle: Why More Context Doesn't Guarantee a Better Answer](2026-10-06-lost-in-the-middle-why-more-context-isnt-better/) | Weekly STEM | General AI/STEM topic explainer |
| 2026-10-15 | [The Alert That Waited for a Second Item](2026-10-15-the-alert-that-waited-for-a-second-item/) | Weekly work | Project 29 — Financial Regulatory Intelligence System (`mycroft`) |
| 2026-10-15 | [Chain-of-Thought: Why the Reasoning Isn't Always the Reason](2026-10-15-chain-of-thought-why-the-reasoning-isnt-always-the-reason/) | Weekly STEM | General AI/STEM topic explainer |

The first three were rebuilt 2026-08-26/28 for program-wide submission requirements: 4K (3840x2160), a title card + executive-summary opening beat, a 9:16 vertical companion (real Manim portrait relayout, not a crop), and self-assessment against each project's `PROOF.md`. Final deliverables are named per the fellowship convention (`Mycroft_SaiPranaviJeedigunta_<date>_<aspect>.mp4` for the weekly-work video, `<TopicName>_SaiPranaviJeedigunta_<date>_<aspect>.mp4` for the weekly-STEM videos) and live inside each project folder alongside the paperwork; code/paperwork for each is pushed to `github.com/nikbearbrown/humanitarians-youtube` on its own branch (see each project's `README.md` for the exact branch/commit).

The three 2026-08-30 reports (two weekly-work, one weekly-STEM) were all built natively to spec from the start (4K, both aspect ratios, exec-summary beat, naming convention) rather than rebuilt after the fact:

- **Weekly work (1st):** a real Layer 1 fix (a "Mark email sent" step re-deriving its own high-priority rule instead of reading the email step's actual output) with all on-screen numbers traced to `A7-VERIFICATION.md` and re-verified live against the database at build time — see its `README.md`/`BUILD-LOG.md`.
- **Weekly STEM:** a framework-first explainer teaching a reusable 3-question rubric (Source / Instruction-or-Data / Consequence) for whether an AI agent should act on external text, with a worked example, a falsifiability stress-test, and a scaffolded audit task — self-assessed 11/12 against `PROOF.md` — see its `README.md`/`BUILD-LOG.md`/`PEDAGOGY.md`.
- **Weekly work (2nd):** a second Layer 1 fix in the same pipeline — a source classifier rule specifically written to catch CFTC filings that, tested against every live CFTC item, matched zero of them (the rule checked for text patterns that structurally can't appear in Federal Register permalinks/titles) — fixed by reading the feed's real `dc:creator` field instead of guessing. Named `Mycroft_SaiPranaviJeedigunta_20260830b_*` (suffixed `b` since two weekly-work videos landed the same day) — see its `README.md`/`BUILD-LOG.md`.

The 2026-09-07 reports (one weekly-work, one weekly-STEM):

- **Weekly work (4th in the Layer 1 series):** a partial fix, honestly reported — 18 Google News items were falling through the source classifier to "Unknown Source" (no `dc:creator` field to fall back on this time); 10 of 18 recovered via feed-agnostic synonym keywords (`adviser`/`RIA`, `broker-dealer`/`Reg BI`), with the remaining 8 explicitly left open as a deliberate tradeoff rather than an unsolved bug — see its `README.md`/`BUILD-LOG.md`.
- **Weekly STEM:** a framework-first explainer on when to use keyword matching vs. embeddings — chosen because it explains the general pattern underneath this fellow's last several weekly-work bugs (brittle exact-match rules breaking as real-world text varies), though kept fully generic with fictional examples, not a report of any specific fix. Its meaning-space scatter diagrams (B04/B05) needed 3 rounds of layout fixes after the automated frame-QC tool failed to catch a real content-distribution defect (a small cluster of points confined to one region of a much larger panel) — resolved by direct visual inspection of extracted frames across each beat's full runtime, not by trusting the tool's reported numbers. A follow-up patch also fixed a real low-contrast palette bug (a text color measuring 1.16:1 against its panel background, WCAG minimum is 4.5:1) and a text/panel-border overlap the toolkit's own layout auditor caught. See its `BUILD-LOG.md` for the full account.

## Naming/format convention

The first 8 reports (2026-07-26 through 2026-09-07) use the original fellowship naming
(`Mycroft_SaiPranaviJeedigunta_<date>_<aspect>.mp4` / `<TopicName>_SaiPranaviJeedigunta_<date>_<aspect>.mp4`,
4K 16:9 + 1080x1920 9:16 short) and are being **kept exactly as built** — no retroactive renaming
or re-rendering.

**Starting with the 2026-09-14 reports**, submissions switch to the toolkit's own official spec
(`brutalist/docs/FELLOWS-SUBMISSION.md`, introduced 2026-09-07): `ProjectName_VolunteerName.mp4`
(no date, no aspect suffix in the filename), separate `deliverables/landscape/`/`deliverables/vertical/`
folders instead of a filename suffix, and a true 4K **2160x3840 full-length vertical companion**
(via the toolkit's `./art vertical` command — a native portrait relayout of the whole video, not a
≤180s Shorts-style cut) instead of the 1080x1920 short used above.

The two 2026-09-14 reports are the first built under this new spec:

- **Weekly work (5th in the Layer 1 series), "The Link That Pointed Nowhere":** every Google News
  item's stored link was a dead-end redirect (the `url=` regex it relied on doesn't match modern
  Google News links); the fix reverse-engineers how Google News's own page resolves the real URL,
  with an on-screen caveat that this is an undocumented/reverse-engineered mechanism, not a stable
  API. Along the way, a classification-ordering near-miss was caught before shipping — it would
  have silently undone two prior weeks' fixes. Two honest limitations kept at full weight: unverified
  against the fellow's live n8n instance, and ~400 extra requests/run by design. Named
  `GoogleNewsLinkFix_SaiPranaviJeedigunta.mp4`. GATE V: 0 BLOCKER/0 MAJOR on both masters — see its
  `README.md`/`BUILD-LOG.md`.
- **Weekly STEM, "RAG: Why 'Looking It Up' Doesn't Guarantee It's True":** a framework-first
  explainer teaching a 3-question rubric (Relevant / Current / Grounded) for whether a
  Retrieval-Augmented-Generation answer is actually grounded in what it retrieved, with a stale-document
  worked example, a falsifiability case where retrieval genuinely is the fix, and a scaffolded audit
  task. Self-assessed 11/12 against `PROOF.md`. Named `RAGGrounding_SaiPranaviJeedigunta.mp4` — see
  its `README.md`/`BUILD-LOG.md`/`PEDAGOGY.md`.

Two further weekly-work reports (2026-09-22, backdated to catch up on a missed submission week,
and 2026-09-29), both built under the same new submission spec and both under the renamed
`fellows/pranavi-j/` path (see "Fellow folder rename" below):

- **Weekly work (6th in the Layer 1 series), "The All-Clear That Wasn't All There":** the
  pipeline's "no new items" status email listed only 4 of its 5 real monitored RSS feeds
  (Investment Advisor Rules missing from both the source grid and the summary line). Fixed and
  verified by diffing every source-card label against the workflow's real feed-node names. Also
  closed a stale `FINDINGS.md` note ("apply A4/B4 to Generate Email") that turned out to already
  be fixed since the very first hardening commit. Named `AllClearEmailFix_SaiPranaviJeedigunta.mp4`.
  GATE V: 0 BLOCKER/0 MAJOR on both masters — see its `README.md`/`BUILD-LOG.md`.
- **Weekly work (7th in the Layer 1 series), "The Keyword That Cried Wolf":** built and verified a
  local-LLM (Ollama, `llama3.2:3b`) second-pass review targeting the two C1 keyword-misfire
  patterns named in `FINDINGS.md` — a Medicare rule scored 10/Critical from the word "emergency"
  inside a law's proper name, and a boilerplate Nasdaq filing scored 9/Critical from "Immediate
  Effectiveness." Verified live against both false positives plus a genuine true positive (the SEC
  insider-trading case); fail-open behavior verified separately (an Ollama outage doesn't break the
  pipeline). Ollama wasn't even installed on the dev machine before this fix — installed, model
  pulled, and tested live in-session. Named `KeywordReScoring_SaiPranaviJeedigunta.mp4`. GATE V: 0
  BLOCKER/0 MAJOR (landscape), 0 BLOCKER/2 MAJOR (vertical, both on the B08 brand card, borderline
  underfill at the 55% floor, personally confirmed legible) — see its `README.md`/`BUILD-LOG.md`.
  Both mycroft fixes behind these two videos are pushed to `github.com/SaiPranaviJeedigunta/mycroft`,
  branch `feature/regulatory-intelligence-hardening` (commit `3e32894`), documented in
  `B5-VERIFICATION.md` and `C2-VERIFICATION.md`.

Two matching weekly-STEM reports, same two backdated weeks, same new submission spec, both kept
fully generic (no real model/vendor named or benchmarked):

- **Weekly STEM, "Hallucination: Why Sounding Sure Isn't the Same as Being Right":** a
  framework-first explainer teaching a reusable 3-question rubric (Checkable? / Would It Hedge? /
  Does Confidence Track Difficulty?) for telling a model's genuine certainty apart from fluent
  phrasing that merely resembles certainty. Worked example: a fabricated citation delivered in the
  same confident tone as a real one. Falsifiability case: the same confident tone on a simple,
  genuinely true fact, stress-testing the rubric against a naive "confident tone = hallucination"
  over-trigger. Named `HallucinationConfidence_SaiPranaviJeedigunta.mp4`. GATE V: 0 BLOCKER/0 MAJOR
  on both masters — see its `README.md`/`BUILD-LOG.md`.
- **Weekly STEM, "Tokenization: Why AI Can't Count the Letters in Its Own Words":** a
  framework-first explainer on why language models read text as sub-word tokens rather than
  individual characters, and why that causes character-counting errors. Worked example: the
  well-known "how many R's in strawberry" class of failure, with the word's real token split shown
  alongside the model's miscounted tally. Falsifiability case: the same word spelled out
  letter-by-letter first, now counted correctly. Named `Tokenization_SaiPranaviJeedigunta.mp4`.
  GATE V: 0 BLOCKER/0 MAJOR on both masters — see its `README.md`/`BUILD-LOG.md`.

A real continuation of the B2 source-classification work (2026-10-06), plus a matching
weekly-STEM report, same new submission spec:

- **Weekly work (8th in the Layer 1 series), "The Classifier That Learned When Not to Guess":**
  re-ran the live source classifier against the real local DB and confirmed keyword-rule fixes
  from prior weeks had already resolved 13 of the original 21 "Unknown Source" items — leaving a
  genuine residual of 8 generic headlines no keyword list can safely catch. Added an Ollama
  (`llama3.2:3b`) fallback classification step that only acts on unresolved items and fails open on
  any error. Live-verified: 0 already-classified items touched, 1 of 8 correctly resolved, 7
  honestly left as Unknown Source rather than guessed — framed explicitly as the correct outcome,
  not a shortfall. Named `ClassifierFallbackClassification_SaiPranaviJeedigunta.mp4`. GATE V: 0
  BLOCKER/0 MAJOR on both masters — see its `README.md`/`BUILD-LOG.md`. The mycroft fix behind this
  video is pushed to `github.com/SaiPranaviJeedigunta/mycroft`, branch
  `feature/regulatory-intelligence-hardening` (commit `948fba5`), documented in the 2026-10-06
  addendum to `B2-VERIFICATION.md`.
- **Weekly STEM, "Lost in the Middle: Why More Context Doesn't Guarantee a Better Answer":** a
  framework-first explainer on the well-documented long-context effect where models are reliably
  better at using information near the start/end of a long input than information buried in the
  middle. Worked example: the same fact, same document, same question, planted in the middle
  (missed) versus the start or end (found). Kept fully qualitative — no specific real model
  benchmarked, no fabricated statistics. Named `LostInTheMiddle_SaiPranaviJeedigunta.mp4`. GATE V: 0
  BLOCKER/0 MAJOR on both masters — see its `README.md`/`BUILD-LOG.md`.

A new real bug found and fixed this week (2026-10-15), plus a matching weekly-STEM report, same
new submission spec:

- **Weekly work (9th in the Layer 1 series), "The Alert That Waited for a Second Item":** found
  (via code review, not a live incident) that the real alert-email node's `hasData` guard required
  `newItems.length > 1` — strictly more than one qualifying item — so a single new
  high-priority/critical filing, the exact case the alert path exists for, silently produced no
  email at all. Traced the failed branch to a dead end in the downstream `If` node. Fixed to
  `> 0` — verified live via a Node.js harness running the real extracted node code against 0/1/2
  item batches before and after the fix, then re-verified against the real patched file on disk.
  Honestly flagged that this wasn't caught by an observed live miss, only by re-reading the code,
  and surfaced a separate, still-open `Regulatory_QA`/`source_feed` compatibility gap found along
  the way. Named `AlertSecondItemGate_SaiPranaviJeedigunta.mp4`. GATE V: 0 BLOCKER/0 MAJOR on both
  masters — see its `README.md`/`BUILD-LOG.md`. The mycroft fix behind this video is pushed to
  `github.com/SaiPranaviJeedigunta/mycroft`, branch `feature/regulatory-intelligence-hardening`
  (commit `f9eed1e`), documented in `B6-VERIFICATION.md`.
- **Weekly STEM, "Chain-of-Thought: Why the Reasoning Isn't Always the Reason":** a
  framework-first explainer teaching a reusable 3-test check (Swap a Step / Hide a Hint / Strip It
  Out) for telling whether a model's stated reasoning actually produced its answer, or is a
  plausible-sounding story attached after the fact. Worked example: a hint embedded in a prompt
  that sways the answer while the stated reasoning never mentions it. Falsifiability case: a
  multi-step arithmetic chain where perturbing one intermediate step reliably changes the final
  answer, showing the reasoning genuinely doing causal work. Kept fully generic — no real model
  named or benchmarked. Named `ChainOfThoughtFaithfulness_SaiPranaviJeedigunta.mp4`. GATE V: 0
  BLOCKER/0 MAJOR on both masters — see its `README.md`/`BUILD-LOG.md`.

## Fellow folder rename

This folder was renamed from `fellows/sai-pranavi-j/` to `fellows/pranavi-j/` as part of an
org-wide fellows-folder normalization (first-name-last-initial convention) applied across the
whole `humanitarians-youtube` repo. All 8 prior reports carried over unchanged. A new
`FRICTIONAL.md` requirement was introduced alongside the rename (a per-work-subfolder, ungraded
process log — see the repo-wide fellows guidance for what an entry contains). Each of the 18 work
folders now has one, added 2026-10-20 as part of this renewal review — see each folder's own file.

**Separately, this same review surfaced that the folder-naming half of this convention was
followed but the no-surname half was not:** the README title, every video's spoken narration, and
every deliverable filename across all 18 reports use the full surname
("Sai Pranavi Jeedigunta" / `SaiPranaviJeedigunta.mp4`), not the first-name-last-initial form the
org's `fellows/README.md` requires everywhere. This README's title and header are now compliant;
the 18 already-rendered videos and their filenames are not, and fixing that would mean
re-recording narration and re-rendering every master — not done as part of this renewal and
flagged openly in [RENEWAL.md](RENEWAL.md) rather than fixed quietly or left undiscovered.
