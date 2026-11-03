# Motion and compile check: Week 29 work video

Built by `build_motion.py` (reveal stages cross-faded on Whisper word times, slow push-in, dissolve between beats) and `compile_master.py`; measured by `proof_motion.py` on the compiled masters (output in MOTION-GATE.txt).

| | Long (16:9) | Short (9:16) |
|---|---|---|
| File | two-customers-one-run-mycroft.mp4 | short/two-customers-one-run-mycroft-short.mp4 |
| Size / fps / length | 3840x2160, 30 fps, 241.6 s | 2160x3840, 30 fps, 96.6 s |
| Loudness / true peak | -14.6 LUFS, -1.9 dBFS | -14.7 LUFS, -1.9 dBFS |
| Gate | 8 of 8 | 10 of 10 |

Short gate details: ink between 12.3% and 74.5% of the height, nothing in the right-hand strip; smallest type 32 px at 1080 wide; no hard cut (largest frame change 0.96 grey levels); longest static stretch 2.90 s; first and last frames match (it ends on its own opening frame); no silence of 1 s or more except none (longest 0.96 s); progress rail of eleven dots carries state across the beats.
Long film: no hard cuts, longest static stretch 7.1 s (measured on pixels; the slow push-in is always running), pauses of 1 to 2.3 s between beats are the table holds.

Changes made on the way (each found by measuring, not by eye): the Short was first laid out across the full page and failed the safe area, so it was redrawn inside the safe zone; its tail pauses were cut so no silence reaches 1 s (Short audio re-synthesised, 97.2 s to 94.1 s); a loop stage was added; the title and intro beats got extra reveal stages to end a 4.9 s static stretch.

Update 2026-11-01: the Short's opening beat was changed to start with the claim (re-signed in chat), audio, captions, picture and gates for the Short were redone; measured results above are the final ones (Short 10 of 10).
