# Deck-Lecture — session handoff (updated 2026-06-30, late)

Turning the **Chapter 7 — Fairness Metrics** deck into a narrated Remotion lecture.

## TL;DR
Pipeline works end-to-end; previews in Remotion Studio. The "staring at static text
for 30s" problem is solved: every slide now has a moving visual after a ~3.5s hold.
**Before the next render, two things still need doing:** (a) regenerate the 5
corrected-name audios; (b) hand-clean the auto-bullet wording on the slides that
matter. Nothing was auto-rendered (Bear renders from Remotion when it's worth it).

## Visual model — THREE tiers (per slide; priority doodle > bullets > live)
All tiers use the **deck's typography (Lato / NU red)** — no handwriting font.
1. **live** — slide has a D3 chart (`data-chart`): stays on-screen the whole slide. (8 slides)
2. **doodle** — authored sketch draws on, one element per narration line. (8 slides: S05, S07, S09, S14, S16, S24, S29, S32 — the equation slides)
3. **bullets** — auto-condensed narration animates in as bullets, one per line, current emphasized. (23 slides — every remaining text slide)
→ Chapter 7: 8 doodle + 23 bullets + 8 live = **0 slides held static.**

## The skill (`skills/deck-lecture/`)
Scripts: `extract_slides.py` (deck→beat_sheet, detects D3→visual_mode, preserves
narration on re-run) · `script_guard.py` · `tts_audit.py` + `apply_pronunciations.py`
· `align_captions.py` · `build_doodle.py` / `preview_doodle.py` ·
`build_bullets.py` / `preview_bullets.py` · `scaffold_remotion.py`.
Remotion src: `Lecture`, `DeckBackground`, `Doodle`, `Bullets`, `Captions`, `theme`.

## Current state of this lecture
- `beat_sheet.json` — 39 beats; all have narration, tts_normalized_text, durations, visual_mode.
- `pronunciations.json` — plain respellings (Shooldekova, Mullynathan, Klineberg, Rahgavan, Koozner, Lipshits, Tile, North Point, Compass, Bayz, Aristoteelian).
- `captions.json` — present (from the earlier audio run).
- `doodles.json` — 8 equation slides authored.
- `bullets.json` — 23 auto-bullet slides (`"_auto": true` = regenerable; remove it to lock hand edits).
- `remotion/` — scaffolded with all three tiers + bullets/doodles wired; `npm install` done. `npm run studio` shows everything.

## Open items
1. **Regen 5 name audios.** mp3s for S03, S16, S23, S24, S29 are still the old broken-name takes. Needs `ELEVENLABS_API_KEY`. (commands below)
2. **Hand-clean auto-bullets.** Wording is uneven — good ("The choice is yours") and fragmenty ("Start concrete", a trailing colon on S22). Edit `bullets.json` for the slides that matter; `"_auto": true` entries are overwritten by `build_bullets.py`, hand-edited ones (remove that flag) are kept.
3. **Studio walk.** Bear to list any remaining issues seen in preview (timing, positions, crossfade, caption size).
4. **Doodle dot color** still blue `#1a73e8`; switch to NU red `#C8102E` for stricter brand match (optional).
5. **PARKED: pronunciation learning-dictionary fork** — repo-wide JSON (canonical, feeds inline aliasing) vs. synced ElevenLabs hosted dictionary. Learning loop (guess→confirm→reuse across decks) not built.
6. More doodles for the example/prose slides where a sketch beats bullets (smoke alarm S15, COMPAS, causal paths) — optional upgrade over their current bullets.

## Resume commands
Preview:
```
cd "/Users/nik/Documents/Cowork/unreal-reels/lectures/fairness-metrics-and-impossible-choices/remotion" && npm run studio
```
Fix 5 names (audio → captions → restage), from repo root:
```
cd "/Users/nik/Documents/Cowork/unreal-reels"
python3 aspects/explainer/bears-doodles/scripts/generate_audio.py "lectures/fairness-metrics-and-impossible-choices" --only S03 S16 S23 S24 S29
python3 skills/deck-lecture/scripts/align_captions.py "lectures/fairness-metrics-and-impossible-choices" --only S03 S16 S23 S24 S29
python3 skills/deck-lecture/scripts/scaffold_remotion.py "lectures/fairness-metrics-and-impossible-choices" --deck "lectures/fairness-metrics-and-impossible-choices/Chapter 7 - Fairness Metrics.dc.html"
```
Regenerate bullets after editing narration (keeps hand-locked slides):
```
cd "/Users/nik/Documents/Cowork/unreal-reels" && python3 skills/deck-lecture/scripts/build_bullets.py "lectures/fairness-metrics-and-impossible-choices"
```
Render (when worth it):
```
cd "/Users/nik/Documents/Cowork/unreal-reels/lectures/fairness-metrics-and-impossible-choices/remotion" && npm run render
```

## Suggested order next session
1. Studio walk → confirm the 3 tiers look right; note issues.
2. Hand-clean auto-bullets on the key slides.
3. Regen the 5 name audios.
4. Decide pronunciation-dictionary fork.
5. Optional: more doodles; NU-red dots.
