# Video gate — Short (9:16), measured on the compiled file

File: `color-never-hears-the-music-short.mp4`. Measured by `short/proof_short.py` (pixels from the compiled mp4, the builder's text log of every frame, the Whisper word clock). Voice: Kokoro `am_onyx`.

- PASS  1 resolution and first frame: 2160x3840 @ 30/1 fps, 2266 frames, h264/yuv420p; frame 0 sky colour (186, 184, 178) (opening grey (185, 184, 178), distance 1); not black: mean 211
- PASS  2 ink zones: 151 frames sampled every 0.5 s: ink x 59..899 (safe 60..900), y 230..1438 (safe 230..1440); right-rail pixels 0
- PASS  3 type size: 2266 frames, 11861 text draws (alpha > 0.3): smallest 34 px logical (floor 34); sizes in use [34, 36, 40, 52, 56, 84]
- PASS  4 figures on screen when spoken: S03 spoken '97' (ninety seven) @ 21.0s ok; S03 spoken 'Bach' @ 19.1s ok; S03 spoken 'Brahms' @ 20.8s ok; S05 spoken 'Bach's' example @ 45.8s ok; S05 spoken 'Brahms's' example @ 50.2s ok; S04 'closely' (0.99 counter has landed) @ 41.6s ok; S04 source 0.89-0.99 while the ratings are spoken @ 35.9s ok; S08 title spoken @ 71.7s ok
- PASS  5 sources in the safe area: 8/8 lines show a source line (34 px, y 1335..1440) at mid-line: [('S01', True), ('S02', True), ('S03', True), ('S04', True), ('S05', True), ('S06', True), ('S07', True), ('S08', True)]
- PASS  6 no hard cuts: 2266 frames; largest frame-to-frame mean change 2.78 grey levels (threshold 3.0: a full-scene cut is 20+, a sky colour wash between frames is under 1); three largest at [74.97, 75.0, 74.93] s = [2.78, 2.62, 2.61]
- PASS  7 no static stretch over 3 s: longest run with fewer than 10 pixels changing between frames 0.97 s (ends 29.7 s); change between frames 2.5 s apart: min 0.56%, median 3.71%
- PASS  8 loop-friendly last frame: last frame differs from frame 0 in 3.40% of pixels, all inside the landscape box: True (clouds only); bbox x 30..449, y 203..619 at 540x960
- PASS  9 audio: aac,48000,1; -14.5 LUFS (target -14); true peak -1.9 dBTP (limit -1.5); silences >= 0.7 s: none
- PASS  10 no foreign text or handle: 72 distinct strings drawn; words not in SHORT-SCRIPT.md: none; handles: none
- PASS  11 duration: video 75.533 s, audio 75.533 s (difference 0 ms); target about 75.5 s; Shorts limit 180 s

**GATE: 11/11**
