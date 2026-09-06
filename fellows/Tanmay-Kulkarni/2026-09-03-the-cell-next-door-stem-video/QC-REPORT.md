# QC REPORT — The Cell Next Door

Week 21 topic video · Humanitarians AI · Tanmay Kulkarni · 2026-09-03

---

## Deliverables

| File | Aspect | Resolution | Duration | Loudness | Verified |
|---|---|---|---|---|---|
| `2026-09-03-the-cell-next-door.mp4` | 16:9 | **3840 × 2160** | 508.9s (8:28.9) | −14.8 LUFS / −1.2 dBFS | `ffprobe` + `ebur128` |
| `2026-09-03-the-cell-next-door-short.mp4` | 9:16 | **2160 × 3840** | 141.8s (2:21.8) | −14.9 LUFS / −1.3 dBFS | `ffprobe` + `ebur128` |

Both are **clean masters** — no slate, no review burn-ins. Masters are in the shared Google
Drive; this folder holds text and code only.

## Loudness — a defect caught at assembly, not during the build

Both cuts compiled at **−24.5 LUFS**, roughly 10 dB below Week 20's masters and well below
YouTube's normalisation target. `compile.py` does not normalise and nothing downstream checks,
so every gate in the pipeline passed on a deliverable that would have played back quiet.

Found by reading Week 20's `DELIVERY.md`, which records loudness per cut — not by any check in
this week's own toolchain. `BEATS.md` defect 13 names this exact hazard; it simply was not in
the sequence.

Fixed with two-pass EBU R128 to −14 LUFS / −1.5 dBTP, **video stream-copied**, so the picture
is byte-identical and no beat was re-rendered. The table above is the post-normalisation
measurement, taken after the fix rather than predicted from it.

## Resolution

Every beat renders at exactly 3840 × 2160 and is asserted at render time, not sampled
afterwards — `render_beats.py` fails the run if any frame comes back at another size. This
matters more than it sounds: BEATS.md's most-cited cause of "uneven letter spacing" is a 1080p
beat upscaled into a 4K master, where antialiasing bridges letter gaps unevenly depending on
which letters border them. It reads as a typography bug that no typography fix will touch.

The Short's slates are **native 2160 × 3840**, not centre cuts. `shorts.py` offers to centre-cut
16:9 stills into 9:16; for a text slate that discards 72% of the width and chops words without
failing loudly. Verified by ink-width measurement rather than by eye: all seven portrait slates
read 86–87% ink width, where a letterboxed render would land near 27%.

## Motion

9 of 18 beats animated; `hold` carries 44%, inside the ~40% guidance after nine conversions.
Every animated beat is asserted to land within 0.1% of its measured audio, checked at render
rather than left to the compiler's ±5% retime ladder.

## Gates

| | |
|---|---|
| Build | `build_beat_sheet.py --check` — 10 gate classes, clean |
| Gate proof | `test_gates.py` — **10/10 gates verified to actually fire** |
| Read-aloud | `gate_p_lint.py` — 67 flags → 10 accepted |
| Gate P | signed 2026-09-03, listen-through completed on the compiled cut |
| Evidence | `experiment/tmb_orr_audit.py` — stdlib only, reproduces every number |

## Captions

`.srt` and `.vtt` produced at build time from `beat_sheet.json`, 176 cues, none unwrappable,
none over 6 s. Kept with the masters in the Drive per this collection's convention.

The caption generator derives its output slug from `beat_sheet.json` metadata rather than a
literal — BEATS.md defect 21 records a copy of this script that shipped correct captions under
the *previous* film's filename, silently.
