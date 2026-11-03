# PEDAGOGY — Why AI-Generated Code Still Needs a Human Who Understands the System

Single-topic `ai-explainer` reel (~2:05 target), Film 1 of a new
general-AI-topic series (distinct from the topic-explainer and weekly-report
series this fellow already runs). Audience: developers who use AI coding
assistants. Thesis: a fix can look correct — it addresses the visible
symptom — while being wrong at the system level, because it doesn't account
for what actually happens when it fails.

## Act structure
- B00 TITLE — silent title card (title + @HumanitariansAI), added 2026-08-17 ✓
- B01 HOOK — a fix that looks right and still crashes production, shown not narrated ✓
- B02 FRAMEWORK — the 3-question rubric (Trace / Consequence / Why), shown in full before any example ✓
- B03 WORKED-EXAMPLE — all three rubric questions walked through a code fix, both versions legible simultaneously ✓
- B04 FALSIFIABILITY — a low-stakes date-formatter case that breaks an absolutist "never trust AI code" reading ✓
- B05 CTA — a literal 3-step checklist, not "ask your AI tool" ✓
- B06 CLOSE — callback to the hook, restates the thesis ✓
- B07 SIGN-OFF — channel/fellow credit, added 2026-08-17 ✓

(Renumbered 2026-08-17 — see "Revision after watching v2" below. All B0N references above and elsewhere in this file predate the renumbering and describe the same content, now shifted by one.)

## Self-score against the PROOF.md rubric (0–2 each, /12)

| Criterion | Score | Note |
|---|---|---|
| Explicit framework | 2 | Rubric shown as a graphic (B01) before any example appears |
| Reusable rubric | 2 | Trace / Consequence / Why applies to any AI-suggested fix, not just B02's case |
| Worked example | 2 | B02 walks the reasoning step (trace → consequence → why) live, not just the conclusion |
| Falsifiability / edge case | 2 | B03 names the case (low-stakes utility) that would break a blanket-distrust framing |
| Active task | 2 | B04's 3-step task is concrete and repeatable, not a vague pointer |
| Friction | 1 | The tension (quick trust vs. full scrutiny) is stated and resolved by the rubric, but the video doesn't make the viewer sit with an ambiguous case before resolving it — see Friction note below |

**Total: 11/12** (pending fellow review — this is a self-check, not a sign-off).

## Production gate self-check (from BEAT-SHEET.md, carried forward)

- [x] Rubric graphic appears before the worked example — not narrated after
- [x] Before/after code diff planned as legible simultaneously (pending actual `scenes.py` build — see BUILD-LOG.md)
- [x] Falsifiability case shown, not just claimed in voiceover
- [x] CTA is the literal 3-step text, not a paraphrase
- [ ] No claim made without a visible on-screen artifact backing it — **cannot confirm until `scenes.py` exists**; this is a paper gate only until previz

## Evidence discipline (source: FACTCHECK.md)
| Claim | Verdict |
|---|---|
| Worked example (B02) | PASS (illustrative, explicitly not attributed to a real incident) |
| All other claims | PASS (editorial framework, not empirical) |

## Compliance

**RESOLVED 2026-08-17:** B06 sign-off card added ("in for Sai Pranavi
J."), matching the pattern in this fellow's other two videos and the
fellowship's requirement that videos demonstrably come from the volunteer.

## Friction protected
- Kept: the falsifiability case (B03) even though it slightly undercuts the
  hook's urgency — cutting it would have made the rubric read as "distrust
  everything," which the premise explicitly rejects.
- Deliberately excluded: attributing the worked example to a real codebase,
  even though real matching source material was found and would have made
  the claim stronger — see `FACTCHECK.md`'s no-fabrication note. Kept
  generic by fellow decision, not because no real source existed.

## Gate P sign-off (v1)

Narration reviewed and approved by the fellow, 2026-08-17, before any audio generation.

VERDICT: PASS

## Revision after watching v1 (2026-08-17)

The fellow watched the rendered v1 master (56.46s) and found it **too vague**:
B01 (framework) and B04 (CTA) just labeled the three items without explaining
them, and B02 (worked example) stated the rubric answers tersely instead of
walking the actual reasoning. Revised narration for B01/B02/B04 in
`beat_sheet.json` — each of the 3 rubric questions and each of the 3 CTA
steps now gets a real explanatory sentence (e.g. B02 now explains *why*
quote-escaping fails — backslashes/null bytes/encoding — and *why*
parameter binding removes the failure mode, not just labels it). B01 now
opens with the fellow's requested line: "Before you trust it, ask yourself
all three questions." Estimated runtime grew from ~2:05 to ~2:55 as a direct
result — accepted by the fellow ("its okay if its longer add it").

## Gate P sign-off (v2)

Revised narration (B01/B02/B04) reviewed and approved by the fellow,
2026-08-17, before regenerating audio.

VERDICT: PASS

## Revision after watching v2 (2026-08-17)

The fellow watched the v2 master (119.03s) and requested: (1) a silent
opening title card before the hook — the video previously dove straight into
the crash log with no title/branding intro; (2) the Trace question's "not
just read the diff" phrasing was unclear — "diff" jargon wasn't landing even
for the fellow. Reworded to "not just read what's different," per explicit
instruction to keep the concept and swap in "different" rather than drop the
clause. A new `B00_TitleCard` beat was added and all 7 existing beats
renumbered up by one (see Act structure above and `BUILD-LOG.md`).

## Gate P sign-off (v3)

Title-card addition and Trace-line rewording reviewed and approved by the
fellow, 2026-08-17, before regenerating audio/render.

VERDICT: PASS

## v4 — Program feedback: 4K, executive-summary beat, self-assessment (2026-08-26)

Applied three pieces of program feedback: (1) confirmed 4K (3840x2160) —
this reel was already 4K since v3, re-verified after rebuilding on the
updated toolkit; (2) added a new **B01 EXECUTIVE SUMMARY** beat right after
the B00 title card — "Hi, I'm Sai Pranavi J.. This video is about
why a fix that looks right isn't always a fix that's actually right — and
the three questions to ask before you trust one." All prior content beats
shifted down by one (old B01-B07 -> B02-B08). Act structure above predates
this shift; add B01 EXEC-SUMMARY between TITLE and HOOK when reading it. (3)
self-assessed against `PROOF.md` below (newly copied into this folder from
the facial-recognition project, which already carried it — it's a generic
protocol doc, not video-specific).

## Self-Assessment against PROOF.md (v4)

**PROOF.md's teaching rubric (0-2 each, /12)** — re-scored against the
actual v4 video, not carried forward from the v1 self-check above:

| Criterion | Score | Note |
|---|---|---|
| Explicit framework | 2 | Rubric (Trace/Consequence/Why) shown as a graphic in B03 before the B04 worked example |
| Reusable rubric | 2 | The three questions apply to any AI-suggested fix, not just B04's SQL case |
| Worked example | 2 | B04 walks trace -> consequence -> why live against the code diff, with real explanatory depth (not just the conclusion) |
| Falsifiability / edge case | 2 | B05 names the low-stakes date-formatter case that breaks a blanket-distrust reading |
| Active task | 2 | B06's 3-step task is concrete (ask/trace/write-one-sentence), not "ask your AI tool" |
| Friction | 1 | Same gap as the v1 self-check: the tension between quick-trust and full-scrutiny is stated and resolved, but the viewer never sits with a genuinely ambiguous case before the resolution arrives |

**Total: 11/12.**

**PROOF.md's binary Production Gate**, checked against real extracted frames
(`_qc/contact_sheet.png`, GATE V run on the true clean 4K master, not the
watermarked `-slate.mp4`):
- [x] Evidence legible at the moment of assertion — B04's before/after code
  diff, B06's checklist, and B05's date-formatter function are all readable
  at 4K in the contact sheet, not faded/clipped/overlapping.
- [x] Sources on screen, not just voiced — the worked example is explicitly
  labeled "illustrative example — a generic before/after pattern" on screen
  (matching FACTCHECK.md's no-fabrication note), not presented as a sourced
  real incident without saying so.
- [x] No claim made without a visible on-screen artifact — every beat's
  narration has a corresponding graphic (rubric, diff, checklist, etc.).

**GATE V (automated) note:** the toolkit's `final_frame_check.py` was
updated in this same session's toolkit pull — it now samples far more
densely (269 frames across the reel vs. the old 18 at 50%/85%-per-beat) and
treats MAJOR findings as blocking by default. Ran it three ways to get a
real signal: (1) against the reel positional arg, which defaulted to the
watermarked `-slate.mp4` and reproduced the long-documented false-positive
edge-bleed (18 BLOCKER) — not a real defect, same as every prior build in
this project; (2) against the true master directly (`--mp4 <slug>.mp4`):
**0 BLOCKER, 74 MAJOR** — nearly all `underfill`/`low-contrast` on frames
sampled *during* build-in animations (content hasn't fully landed yet) or on
the deliberately minimal title/exec-summary/brand cards, not on any
steady-state content frame; (3) visually confirmed via the contact sheet
that every flagged beat is legible by eye — dark-panel text reads clearly,
card layouts are intentional minimalist compositions, consistent with this
fellow's other two videos' own accepted cosmetic-only QC history. Per this
project's standing rule (never trust the automated report alone, verify
real frames), 0 BLOCKER stands as the ship bar; the MAJOR count reflects a
stricter/denser tool, not a new visual regression.

**VERDICT: PASS** (self-assessment; not a substitute for a human reviewer's PROOF.md pass).
