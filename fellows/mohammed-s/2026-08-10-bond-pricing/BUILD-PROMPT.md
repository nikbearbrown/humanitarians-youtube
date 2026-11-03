# BUILD-PROMPT — hussain-bond-pricing-duration
# "Bond Pricing and Duration — Price-Yield Curve with Claude" | Kokoro am_onyx

## Standalone rebuild instructions

```bash
cd Brut/brutalist.art
REEL=../../Videos/humanitarians-youtube/claude-for-finance/hussain-bond-pricing-duration

# 1. Gate P must be signed (PEDAGOGY.md "VERDICT: PASS") — already done.
# 2. Audio (Kokoro am_onyx, free)
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"

# 3. Render Remotion scenes (foreground, concurrency=1)
python3 runtime/scripts/remotion_scenes.py "$REEL"

# 4. Render Manim + compile the 4K review + master cut (./art run defaults to --height 2160)
./art run "$REEL"

# 5. Derive the 9:16 cut (fits under the 3:00 cap — full reformat, no beats dropped)
./art shorts "$REEL"
# then, once short/scenes.py (portrait Manim) exists:
python3 runtime/scripts/remotion_scenes.py "$REEL/short"
./art run "$REEL/short" --height 3840        # 4K portrait (2160x3840)
```

## Key decisions
- Voice: Kokoro `am_onyx` ("Onyx") — the only house voices are Onyx/Bella;
  this build is personal (Hussain), not a NikBearBrown/HumanitariansAI
  channel episode, so the footer chip reads "Hussain", not @NikBearBrown.
- Intro line is literal, per request: "Hi, I am Hussain, and this video is
  about bond pricing and duration…" (B00 narration).
- All bond math independently recomputed and corrected against the sibling
  `claude-for-finance/bond-pricing-duration` project, which had two errors
  (Price(2%) and the Macaulay/Modified duration mislabel) — see FACTCHECK.md.
- 16:9 master carries the required cli-explainer spine: INTRO → PROBLEM →
  CLI/CODE/OUTPUT → CLI/CODE/OUTPUT (revision) → SUMMARY → NEXT STEPS → OUTRO.
- 9:16 is a full reformat of the same 11 beats (total ≈176s, under the 3:00
  Shorts cap) — nothing cut, no outro rewrite needed.
- 4K both ways: 16:9 → 3840×2160 (`./art run` default height 2160); 9:16 →
  2160×3840 (`./art run <reel>/short --height 3840`).

## Human checklist before treating this as finished
- [ ] Watch the compiled 16:9 master end to end.
- [ ] Watch the compiled 9:16 cut end to end (check title-safe margins, text
      legibility on a phone-sized preview).
- [ ] Confirm the spoken numbers match the on-screen numbers at B04 and B07.
- [ ] This toolkit never publishes — uploading is a separate, human decision.
