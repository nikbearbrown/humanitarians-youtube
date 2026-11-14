# FRICTIONAL — What We Ask For.

Where the toolkit pushed back during this build.

1. **Voice allow-list.** `af_kore` was requested; `generate_audio_kokoro.py` only accepts
   `am_onyx` / `af_bella`. Built with `af_bella` (the voice of every prior @Yatra episode).
2. **Skill tier.** `deep-explainer` is ADVANCED (Bear sign-off); built on `ai-explainer` instead.
3. **Part cards too short.** First-pass act-card narration ran 1.5–2.2 s; lengthened the lines
   and regenerated only B02/B06/B11.
4. **iCloud eviction mid-render.** macOS "Optimize Mac Storage" offloaded ~15,000 toolkit files
   (node_modules, src, .venv) to iCloud placeholders while the disk sat at 92% full; Remotion failed
   with `dotenv.config is not a function`. Fixed by setting the folder to Keep Downloaded and
   pulling files back with `brctl download`. Keep the toolkit off an optimized iCloud Desktop, or
   keep it pinned.
5. **`remotion bundle` hang** for preview stills (0% CPU) — skipped stills, QC'd rendered frames.
6. **Length vs. platforms.** 4:13.7 per the brief; the 9:16 exceeds Instagram's 3-minute Reel cap.
