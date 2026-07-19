# BUILD-LOG — session-karaoke-audiogram

## HUMAN FEEDBACK — 2026-07-13

Read youtube/session-karaoke-audiogram/BUILD-PROMPT.md and execute it. Standing rules #1–#4 in EXAMPLES-CAMPAIGN.md apply. Voice the narration via the Suno path (./art suno — session notes + directed lyrics; the human generates and drops the vocal-only stem in pantry/). Byron excerpts come from youtube/she-walks-in-beauty/pantry/. Stop at every gate for human review; never publish without approval.

---

## Session start — 2026-07-13

Building video 19b: "Session, Karaoke & Audiogram".
Voice path: Suno (dogfood — session notes + directed lyrics → human generates → pantry stem → ./art suno-slice).
Palette: teardown. Chapter: 6. Estimated duration: ~178s ≈ 2:58.

Beat inventory:
  - REMOTION (BrutalistTerminalOpen): B00
  - GRAPHIC (Manim): B01, B04, B07, B09, B10
  - NikBearBrownCodeBlock: B02, B03, B06
  - NikBearBrownTerminalAsk: B05, B08, B11
  - BrutalistCommentCTA: B99

Standing rules: #3 (remotion_scenes.py foreground only) and #4 (props matched to zod schema) enforced throughout.
Byron excerpts: she-walks-in-beauty/pantry/SheWalksinBeautybyLordByron1814NateSpoken-mastered.wav

## STEP 1 — PEDAGOGY gate (GATE P)

PEDAGOGY.md written. Audit: 7-beat arc (hook→argument→reveal→how→restraint→close→CTA),
cold open on sound not title, gap formula, utility-framing checked per beat, vocabulary law
confirmed, length 178s ≈ 2:58 (under 4:00 target). VERDICT: PASS.

## STEP 2 — beat_sheet.json authored

13 beats: B00 (BrutalistTerminalOpen), B01/B04/B07/B09/B10 (Manim GRAPHIC),
B02/B03/B06 (NikBearBrownCodeBlock), B05/B08/B11 (NikBearBrownTerminalAsk), B99 (BrutalistCommentCTA).
Chapter 6. Total estimated 178s. `delivery` field on every beat for directed Suno output.

## STEP 3 — ./art suno (text generation only — no credits)

Command: ./art suno youtube/session-karaoke-audiogram
Output:
  session-karaoke-audiogram.suno.style.txt  574 chars  → STYLE box
  session-karaoke-audiogram.suno.1.txt     3740 chars · 13 beats (B00–B99) → 1 LYRICS file

GATE P: ✅ PASS — PEDAGOGY.md present with VERDICT: PASS before ./art suno ran.

## STEP 4 — scenes.py authored (2026-07-13)

Manim GRAPHIC beats written: B01_TheSpokenWordEra, B04_TheWordClock,
B07_AudiogramLayers, B09_TheOverlayHero (hero, dark canvas), B10_TheChoice (hero split).
All 5 scenes match beat_sheet specs (colors, layout, timing). SYNTAX OK.
File: youtube/session-karaoke-audiogram/scenes.py

Remotion component schemas verified (rule #4):
  BrutalistTerminalOpen  → command, checklist, topic ✓
  NikBearBrownCodeBlock  → filename, segment, topic, code, language ✓
  NikBearBrownTerminalAsk → command, topic, segment, runningText, output ✓
  BrutalistCommentCTA    → filename, code, variant, topic ✓
All beat_sheet props match exact zod schema keys.

Byron audio confirmed: she-walks-in-beauty/pantry/SheWalksinBeautybyLordByron1814NateSpoken-mastered.wav

## ⛔ GATE — Human review required

Review PEDAGOGY.md, beat_sheet.json, and the two Suno files before generating audio.
Human action needed:
  1. Review PEDAGOGY.md (arc, narration, beat count) and beat_sheet.json — both already PASS.
  2. Paste suno.style.txt into Suno STYLE box, paste suno.1.txt into LYRICS box.
  3. Generate with Bear's voice. Download VOCAL-ONLY stem (no music bed).
  4. Save as: brutalist-art/youtube/session-karaoke-audiogram/pantry/session-karaoke-audiogram-vocals-1.wav
  5. Signal ready → Claude runs: ./art suno-slice + Manim renders + Remotion renders + ./art run
