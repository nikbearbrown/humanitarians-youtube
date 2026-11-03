# Video gate: work-video Short (9:16), measured on the compiled file

File: `the-sum-behind-the-number-short.mp4`. Measured by `short/proof_short.py` (pixels from the compiled mp4, the builder's text log of every frame, the Whisper word clock). Voice: Kokoro `am_onyx`.

- PASS  1 resolution and first frame: 2160x3840 @ 30/1 fps, 2364 frames, h264/yuv420p; frame 0 page colour (249, 246, 243) (cream (250, 249, 245)), mean 242 (not black), the opening number is drawn: True
- PASS  2 ink zones: 158 frames sampled every 0.5 s: ink x 59..899 (safe 60..900), y 230..1439 (safe 230..1440); right-rail pixels 0
- PASS  3 type size: 2364 frames, 24838 text draws (alpha > 0.3): smallest 34 px logical (floor 34); sizes in use [34, 36, 38, 40, 44, 46, 48, 52, 56, 60, 68, 70, 104, 105, 106, 107, 108, 110, 111, 114, 117, 119, 121, 124, 126, 130, 131, 136, 137, 140, 142, 144, 148, 150, 152, 154, 160, 161, 167, 169, 174, 177, 181, 186, 187, 194, 201, 203, 207, 211, 214, 219, 220, 226, 231, 233, 236, 239, 241, 245, 249, 252, 253, 255, 256, 257, 258, 259, 260]
- PASS  4 figures on screen when spoken: S01 '78' (the number) @ 4.5s ok; S03 'market' -15% @ 29.9s ok; S03 '35' @ 32.0s ok; S03 '40' @ 34.1s ok; S03 '30' @ 36.0s ok; S04 '15' @ 45.6s ok; S04 '35' (running total 50) @ 46.1s ok; S04 '90' @ 48.2s ok; S05 '90' @ 51.0s ok; S05 '50' @ 54.0s ok; S06 '36' @ 60.7s ok; S06 '27' @ 61.1s ok; S06 '15' @ 62.0s ok; S06 '78' @ 62.7s ok; S07 '24' @ 68.2s ok; S08 title spoken @ 75.5s ok; the exact title on the closing card: True
- PASS  5 sources in the safe area: 8/8 lines show their source line (34 px, y 1335..1440) at mid-line: [('S01', True), ('S02', True), ('S03', True), ('S04', True), ('S05', True), ('S06', True), ('S07', True), ('S08', True)]
- PASS  6 no hard cuts: 2364 frames; largest frame-to-frame mean change 2.47 grey levels (threshold 3.0: a full-scene cut is 20+); three largest at [8.83, 8.8, 8.87] s = [2.47, 2.44, 2.43]
- PASS  7 no static stretch over 3 s: longest run with fewer than 10 pixels changing between frames 1.53 s (ends 39.6 s); change between frames 2.5 s apart: min 0.315%, median 1.658%
- PASS  8 loop-friendly last frame: last frame differs from frame 0 in 0.362% of pixels (a closing 1.0 s ease returns the number, the chips and the empty stack to the opening state); bbox x 37..253, y 403..459 at 540x960
- PASS  9 audio: aac,48000,1; -14.7 LUFS (target -14); true peak -2.0 dBTP (limit -1.5); silences >= 0.7 s inside the track: [0.73]; end tail none
- PASS  10 no foreign text or handle: 71 distinct strings on screen >= 6 frames (449 including typing partials); words not in SHORT-SCRIPT.md: none; handles: none
- PASS  11 duration: video 78.800 s, audio 78.800 s (difference 0 ms); narration track 78.796 s; Shorts limit 180 s

**GATE: 11/11**
