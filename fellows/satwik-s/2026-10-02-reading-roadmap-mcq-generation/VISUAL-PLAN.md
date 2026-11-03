# VISUAL-PLAN — "A Question for Every Step" (week-10, MCQ Bank + Demo)

AI-explainer (`claude-hai`), 1920×1080, 30fps. Audio-first; pure `useP()`. **PROOF: framework-first** (B01 the
rule before any count). Two-skin. Grounded only in `sources/`.

## Palette contract

| Where | Palette |
|---|---|
| UI beats B00/B07/B08/B09 | **claude** (cream, warm ink, terracotta) |
| Body beats B01–B06 | **humanitarians** (CREAM, INK, TEAL, CRIMSON, SLATE, GOLD, SAGE) |

**TEAL = correct / covered / primary; GOLD = the key example / receipts emphasis; SAGE = pass / validated;
CRIMSON = the draft / falsifiability caveats; SLATE = the bank / scale.**

## Components (B01–B06 net-new; `McqBankDemo.tsx`)

| Beat | Pattern | Accent | What's shown (real, sourced) |
|---|---|---|---|
| B00 | `ClaudeComposerAsk` | terracotta | the ask; 3 result lines (rule / 315 / demo + drafts) |
| B01 | `BankThreeMoves` | TEAL+GOLD+CRIMSON | **the rule in 3 moves — before any count** |
| B02 | `BankAtScale` | SLATE | 315 / 219 / 96 stat cards + 3 validation checks (coverage, 4 options, answer matches) |
| B03 | `QuestionAnatomy` | **GOLD** | a real MCQ card: question + 4 options (Water correct ✓ teal) + reason + difficulty + section ref |
| B04 | `NodeVsConnection` | TEAL / GOLD | topic question vs connection question; the real mutations→oncogenes example + answer |
| B05 | `DemoFlow` | SLATE/TEAL/GOLD | 3 mini-screens: pick a goal · your roadmap (steps + chapter/section + why) · quick check → where you are |
| B06 | `BankHonestBoundary` | SAGE done / CRIMSON draft | complete+validated (sage ✓) vs not-verified (crimson ✗: drafts, empty-body caveat) + stamp |
| B07 | `ClaudeVerdictArtifact` | terracotta | 5 lines: covered / receipts / validated / demo / drafts |
| B08 | `ClaudeComposerAsk` | terracotta | "Your turn." — cover every node+link → receipts → approve column |
| B09 | `ClaudeTitleOutro` | terracotta | title + handle + sign-off |

## Per-beat show design

- **B01:** three move-cards (COVER EVERYTHING · GOLD; CARRY THE RECEIPTS · TEAL; SHIP AS A DRAFT · CRIMSON) + rule band.
- **B02:** three SLATE stat cards (315 questions / 219 topic / 96 connection) + a subtitle, then 3 SAGE-checked validation lines.
- **B03:** a single MCQ card (GOLD-edged) — section ref (small), the question, 4 option rows (Water filled TEAL with ✓, others outlined), a reason line, a difficulty chip; bottom note "answer · reason · difficulty · exact section — one reviewable row."
- **B04:** two cards — **TOPIC QUESTION** (neutral/SLATE: "do you know this topic?" + example) vs **CONNECTION QUESTION** (GOLD: "how does one topic support the next?" + the mutations→oncogenes example + its answer in a teal strip); point "the connection tests the link, not just the facts."
- **B05:** three stacked/side-by-side mini-screens numbered 1-2-3 — "Pick a goal" (SLATE, a search box + topic rows), "Your roadmap" (TEAL goal banner + 2-3 numbered steps each "Read: Ch X · Section" + a why), "Quick check → where you are" (GOLD: a mini question + pass/skip, then done/start-here/upcoming chips); footer "runs offline, driven by the real book."
- **B06:** two columns — **DONE** (SAGE ✓: complete + validated; usable by the engine) vs **STILL A DRAFT** (CRIMSON ✗: every question a draft; empty-body sections anchored to title+facts) + crimson stamp "COMPLETE & VALIDATED — NOT YET VERIFIED · NEEDS FACULTY."

## PROOF production gate (binding at QC)

1. Legible at assertion (315/219/96, the real question + answer, demo screens, held ≥2s). 2. Framework-first (B01 before counts). 3. Side-by-side (B04 topic vs connection; B06 done vs draft). 4. Caveats shown (B06). 5. Sources on screen (every figure traces to `sources/`).

## Render + assembly (binding)

- **Render:** `TMPDIR/TEMP/TMP=d:/_remotion_tmp`, `ART_REMOTION_SCALE=2`, concurrency 2 (low RAM); top up transient Chrome timeouts at concurrency 1. If a beat repeatedly hits the 25s connect timeout, render it direct: `npx remotion render src/index.ts <CompId> media/BXX.mp4 --props=p.json --scale=2 --crf=16 --timeout=120000`.
- **Assembly:** BOTH video and audio via the concat **FILTER** (beats span sessions → stream-copy truncates; demuxer re-encode balloons). Verify the **video stream** duration (not just format) + volumedetect ≈ −20 dB.

## QC (under PYTHONUTF8=1)

Sample settled frames → rubric + two-skin + production gate + no-source-no-verdict + audio present + **video
full length**: confirm B01 rule before counts; B02 315/219/96 + checks; B03 the real question with Water✓; B04
topic vs connection; B05 the 3 demo screens; B06 done vs draft + stamp; `✓ ✕ · →` clean; nothing frames a
draft as approved or claims a learning gain. Log to `_qc/REPORT.md`.
