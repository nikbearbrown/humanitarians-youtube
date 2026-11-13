# VISUAL-PLAN — "Three Tiers, One Plan" (week-11)

AI-explainer (`claude-hai`), 1920×1080, 30fps. Audio-first; pure `useP()`. **PROOF: framework-first** (B01
the three tiers before any count). Two-skin. Grounded only in `sources/`.

## Palette contract

| Where | Palette |
|---|---|
| UI beats B00/B07/B08/B09 | **claude** (cream, warm ink, terracotta) |
| Body beats B01–B06 | **humanitarians** (CREAM, INK, TEAL, CRIMSON, SLATE, GOLD, SAGE) |

**TEAL = required / gates / primary; GOLD = recommended / the key example; SLATE = curious / scale;
SAGE = done / committed; CRIMSON = draft / falsifiability caveats.** (Tier colors are consistent across all beats.)

## Components (B01–B06 net-new; `Week11Tiers.tsx`)

| Beat | Pattern | Accent | What's shown (real, sourced) |
|---|---|---|---|
| B00 | `ClaudeComposerAsk` | terracotta | the ask; 3 result lines (tiers / 1,283 / questions + plan) |
| B01 | `ThreeTiers` | TEAL+GOLD+SLATE | **the three tiers — before any count** (gloss + behavior each) |
| B02 | `TiersAtScale` | TEAL/GOLD/SLATE | 1,283 total; 298/575/410 tier cards + 3 checks (0 cycles, 302 chapter, appendices out) |
| B03 | `WhyThreeTiers` | TEAL vs GOLD | one target (Ch4), two prereqs at different tiers; the Ch2 → 109 stat |
| B04 | `QuestionsAttach` | TEAL/GOLD/SLATE | the chain goal → prereqs → sections → questions + coverage stats |
| B05 | `TierRoadmap` | TEAL/GOLD/SLATE | the real roadmap: goal banner + tiered steps (linked + why) + bounded note |
| B06 | `TierHonestBoundary` | SAGE done / CRIMSON draft | committed+acyclic vs still-a-draft + stamp |
| B07 | `ClaudeVerdictArtifact` | terracotta | 5 lines: tiers / scale / why / questions / draft |
| B08 | `ClaudeComposerAsk` | terracotta | "Your turn." — three tiers not two → attach → approve column |
| B09 | `ClaudeTitleOutro` | terracotta | title + handle + sign-off |

## Per-beat show design
- **B01:** three tier cards (REQUIRED · TEAL; RECOMMENDED · GOLD; CURIOUS · SLATE), each with its gloss + behavior, then a rule band "Required gates · recommended helps · curious invites."
- **B02:** a big total (1,283) + three tier-colored stat cards (298/575/410) + 3 SAGE-checked lines.
- **B03:** a target card (Ch4 Genetics) with two prereq rows beneath — Ch1 REQUIRED (teal) vs Ch2 RECOMMENDED (gold), each with its reason — then a GOLD stat band "109 topics now have Chapter 2 as a prerequisite."
- **B04:** a 4-chip chain (a goal → its prerequisites → the sections → the questions) with arrows, then three stat cards (1,544/1,584 · ~8 · 193) + a note on the 5 unmatched.
- **B05:** a goal banner (TEAL) + a count line (8 required · 8 recommended · 3 curious) + 3 tiered step cards (tier chip colored by tier, "Read: Ch X · Section", a why), footer "bounded to ~15 readings · runs offline on the real book."
- **B06:** two columns — **COMMITTED + ACYCLIC** (SAGE ✓) vs **STILL A DRAFT** (CRIMSON ✗: llm_proposed/derived, needs_review; questions borrowed, 5 unmatched) + crimson stamp "COMMITTED & ACYCLIC — NOT YET VERIFIED · NEEDS FACULTY."

## PROOF production gate (binding at QC)
1. Legible at assertion (1,283/298/575/410, the Ch4 two-tier example, the demo roadmap, held ≥2s). 2. Framework-first (B01 before counts). 3. Side-by-side (B03 required vs recommended; B06 done vs draft). 4. Caveats shown (B06). 5. Sources on screen (every figure traces to `sources/`). 6. Tier colors consistent (TEAL/GOLD/SLATE) across all body beats.

## Render + assembly (binding)
- **Render:** `TMPDIR/TEMP/TMP=d:/_remotion_tmp`, `ART_REMOTION_SCALE=2`, concurrency 2 (low RAM); top up transient Chrome timeouts with `--only BXX` at concurrency 1; last resort `npx remotion render ... --timeout=120000`.
- **Assembly:** BOTH video and audio via the concat **FILTER** (beats span sessions → stream-copy truncates; demuxer re-encode balloons). Verify the **video stream** duration + volumedetect ≈ −20 dB.

## QC (under PYTHONUTF8=1)
Sample settled frames → rubric + two-skin + production gate + no-source-no-verdict + audio present + **video
full length**. Confirm B01 tiers before counts; B02 1,283 + 298/575/410 + checks; B03 Ch1 required vs Ch2
recommended + 109; B04 the chain + coverage; B05 the tiered roadmap; B06 done vs draft + stamp; tier colors
consistent; nothing frames a draft as approved or claims a learning gain. Log to `_qc/REPORT.md`.
