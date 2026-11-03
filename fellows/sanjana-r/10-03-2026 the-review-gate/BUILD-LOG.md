# BUILD-LOG — The Review Gate

**What:** ai-explainer (claude-explainer) PROGRESS RECORD for @HumanitariansAI,
first-person Sanjana Rao, af_bella (female, Kokoro, free). Film 5 in the series
(follows ai-project-management-tools). Built 2026-10-08.

**Decisions**
- **Format = progress record, not concept explainer.** Data = Sanjana's own review
  tracker, window Sep 16–30 2026. Framework retrofitted honestly: THE REVIEW GATE,
  whose three checks ARE the recurring rejection reasons in her own Comments column.
- **New visual language** (user asked for different graphics vs prior films): gate
  check-stations, stat tiles, lollipop project ranking, segmented approval bar,
  GitHub compliance arc, and a submit→fail→email→fix→pass loop. Distinct from film 3
  (waffle/donut/funnel/gauge) and film 4 (the Ticket Test rows).
- **Voice gate:** af_bella approval block written with the user's explicit in-chat
  authorization (2026-10-08). subject_sha256 matches the engine+voice digest.
- **Custom HAI outro** (T09 / S03): the house ClaudeTitleOutro is hardcoded to
  @NikBearBrown (OUTRO-LOCK), so a bespoke Manim card carries @HumanitariansAI.
- **Transitions:** cross-dissolve-through-cream via add_transitions.py (0.35s) — user
  explicitly asked for transitions.

**Pipeline (Windows, per brutalist-art-windows-pipeline):** build_sheet.py →
generate_audio_kokoro.py (master clock) → manim 4K + remotion_scenes.py → compile.py
(PYTHONUTF8=1, no --review) → ffmpeg wav→m4a → add_transitions.py → QC. Short built
the same way with its own sheet/scenes, rendered 2160×3840.

**Retimes:** af_bella narrates faster than word-count estimates; T02_Gate Manim
trimmed from ~30s to ~24s to land under its 25.6s audio (avoid tail trim). Others
authored within ±1× of their measured audio.

**Not pushed to GitHub** (per request). Output under "Humanitarians AI Brutalist files".
