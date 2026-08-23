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
Jeedigunta"), matching the pattern in this fellow's other two videos and the
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
