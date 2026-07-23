# BUILD-LOG — Kokoro: Free Voices (With Names)

## HUMAN FEEDBACK — 2026-07-13

Read youtube/kokoro-free-voices/BUILD-PROMPT.md and execute it. Standing rules #1–#4 in EXAMPLES-CAMPAIGN.md apply. The beat sheet and PEDAGOGY gate are already authored — do not re-author. Phase A installs kokoro-onnx + downloads the model files and FACTCHECKs the cast against --list-voices. Only B00 spends money. Stop at the gate with the review cut; the human may recast any beat by changing its voice field.

## BUILD LOG — 2026-07-13

### Phase A — engine setup

- `pip install kokoro-onnx` → kokoro-onnx 0.4.7 installed
- Model files downloaded to `runtime/models/kokoro/`: kokoro-v1.0.onnx (310 MB), voices-v1.0.bin (27 MB)
- `--list-voices` returns 54 total; English subset (af_/am_/bf_/bm_) = 28 voices exactly
- All 8 cast voices confirmed present: af_bella, af_sarah, am_adam, am_michael, bf_emma, bm_george, am_puck, am_santa
- All grades verified against hexgrad/Kokoro-82M VOICES.md (A-/C+/F+/C+/B-/C/C+/D-) — no corrections needed
- FACTCHECK.md written

### Phase B — audio

- B00 (ElevenLabs): 16.38s — NikBearBrown clone, ~$0.02
- B01–B99 (Kokoro): 10 beats × $0.00 = $0.00 total
- All 11 mp3s generated; timings.json written; beat_sheet.json updated with actual durations
- Total actual duration: ~142.7s

### Phase C — build

- scenes.py authored: 8 GRAPHIC beats (B01–B03, B05–B09) with name-card visual signature
- Gate A: all 8 scenes PASS (3 initial failures fixed by staging non-text shapes across distinct play() calls)
- Manim render: all 8 GRAPHIC beats rendered successfully
- Remotion (rule #3, foreground): B00 BrutalistTerminalOpen, B04 NikBearBrownTerminalAsk, B99 BrutalistCommentCTA — all OK
- Compile: 11/11 slots filled — B00:VIDEO B01–B03:MANIM B04:VIDEO B05–B09:MANIM B99:VIDEO
- qc-sheet.png verified (rule #2): every name card shows correct name+grade, B04 shows casting field, B09 dark hero confirmed, no placeholders
- Review cut: `kokoro-free-voices-review.mp4` (142.7s)

### Audio listen notes (for human review)

B03 Adam (F+) reads "F plus" — likely sounds rough by design (it's an F-grade voice).
B08 Santa (D-) is 5.85s — very short clip, may sound choppy. Caption says "you get what you pay for."
B01 Bella reads "No A P I. No meter. No bill." — space-separated letters should read as individual letters.
B04 Michael reads "voice: A M underscore Michael" — underscore may not read cleanly.

→ GATE: awaiting human sign-off. Recast by changing `"voice"` field in beat_sheet.json + re-run `generate_audio_kokoro.py --only <bid>`.

## HUMAN FEEDBACK — 2026-07-13

perfect final cut and post to the "brutalist" playlist make the 9:16 version

## BUILD LOG — 9:16 SHORT PORTRAIT FIX — 2026-07-13

Visual inspection of first short compile revealed all 8 GRAPHIC beats broken:
root cause — `config.frame_width = 9; config.frame_height = 16` inside construct()
has NO effect (camera initializes before construct() runs); actual coordinate space
is x ∈ [-2.25, 2.25], y ∈ [-4.0, 4.0] (frame_height=8 default, 1080/1920 aspect).

Rewrote short/scenes.py:
- Removed all config.frame_width/height overrides
- Name cards: UP*2.5 (was UP*4.5 — off screen)
- B03 grade scale: 2 rows × 3 chips @ width=0.72 (was 1 row × 6 @ 1.5 = 9.7 wide)
- B05 roster: 4 tiles/row @ 0.88 wide + scale_to_fit_width(0.54) on names to prevent
  inner VGroup overflow (long names like af_jessica at font_size=9 overflow 0.88 tile)
- B06 arrow annotation: next_to(arrow, RIGHT, buff=0.14) at font_size=12 (was clipping)
- B07: FREE/NO CLONING stacked vertically via divider line (was side-by-side, clipping)
- B09: title at UP*3.0 (was UP*5.5), cols at ORIGIN (was UP*1.5)
- B02 engine boxes: width=3.6 (was 5.5)

Gate A: not applicable to these Scene subclasses (static_scene_check expects BearsDoodlesVideo).
All 8 beats re-rendered; QC sheet verified — no clipping, all content within frame.
Short review cut: kokoro-free-voices-short-review.mp4 (147.2s, 12/12 filled)

## HUMAN FEEDBACK — 2026-07-13

those can be final cut and posted to YouTube 16:9 and 9:16
