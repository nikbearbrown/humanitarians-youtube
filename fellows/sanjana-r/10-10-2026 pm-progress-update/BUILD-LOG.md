# BUILD-LOG — "The Last Mile" (film 7)

- **Skill:** ai-explainer (claude-explainer), brand `claude-hai` → @HumanitariansAI.
- **Type:** PROGRESS RECORD, week of Oct 4–10 2026, first-person Sanjana Rao.
- **Voice:** Kokoro `af_bella` (female). User authorized a female voice in chat
  ("any female voice") → persistent-fellow-selected approval block written
  (subject_sha256 d3486a7…). Free/local, $0.
- **Pipeline (Windows, direct-call, per the toolkit's Windows notes):**
  1. `build_sheet.py` → `beat_sheet.json` (10 beats).
  2. `generate_audio_kokoro.py` → 10 mp3 (durations are the master clock).
  3. Manim scenes rendered at `-r 3840,2160 --fps 24`; copied to `manim/T0x.mp4`.
     Paced just under each beat's measured audio (1.02–1.12× conform, no trim).
  4. `remotion_scenes.py` → `media/T00,T01,T04,T08.mp4` (4K composer + hesitant writer).
  5. `compile.py --height 2160` → conform + mux + captions.
  6. `add_transitions.py` → cross-dissolve-through-cream → 16:9 master.
  7. `shorts.py`/dedicated short sheet → 9:16 master.
- **Correction applied (DOUBLE-CHECK LAW):** T04 narration said "Friday's queue"; Oct 10
  2026 is a Saturday and the 14 figure is the week's review entries, so changed to
  "this week's queue / 14 reviews." Rebuilt sheet + regenerated audio accordingly.
- **New graphics** vs films 3–6: film-strip throughput counter, export-style progress
  checklist, literal 16:9/9:16 screen panes (the portrait defect shown, not described),
  a footer-strike for the stray-footer failure. Claude fidelity palette, one terracotta
  accent per beat.
- **Outro:** custom Manim @HumanitariansAI card (house ClaudeTitleOutro is
  @NikBearBrown-locked). SKIN LINT warns, does not block.
- **Never pushed to GitHub** (per user instruction + project convention). Delivered to
  `Humanitarians AI Brutalist files/the-last-mile/`.
