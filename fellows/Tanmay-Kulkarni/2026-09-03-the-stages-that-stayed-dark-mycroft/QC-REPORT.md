# QC REPORT — The Stages That Stayed Dark

Week 21 work video · Humanitarians AI · Tanmay Kulkarni · 2026-09-03

---

## Deliverables

| File | Aspect | Resolution | Duration | Loudness | Verified |
|---|---|---|---|---|---|
| `2026-09-03-the-stages-that-stayed-dark.mp4` | 16:9 | **3840 × 2160** | 265.6s (4:25.5) | −14.8 LUFS / −1.4 dBFS | `ffprobe` + `ebur128` |
| `2026-09-03-the-stages-that-stayed-dark-short.mp4` | 9:16 | **2160 × 3840** | 157.3s (2:37.2) | −14.8 LUFS / −1.3 dBFS | `ffprobe` + `ebur128` |

Both are **clean masters** — no slate, no review burn-ins. Masters are in the shared Google
Drive; this folder holds text and code only.

## Loudness

Both cuts compiled at **−24.6 LUFS** and were normalised at assembly with two-pass EBU R128 to
−14 LUFS / −1.5 dBTP, video stream-copied. Same miss as the topic video, same fix, found the
same way — by reading a prior week's delivery record rather than by any check in this week's
pipeline. Measured after the fix; the table is the reading, not the target.

## Resolution

Every 16:9 beat is asserted at 3840 × 2160 at render time. The Short's ten slates are **native
2160 × 3840** and measure 87% ink width apiece — positive evidence the portrait reshape worked,
rather than absence of a complaint.

The portrait layout is not a reflow. Five pipeline stages do not fit across a 4.5-unit frame at
legible size, so portrait stacks the pipeline **vertically** — which reads as a descent, and
how far down a claim gets before it stops is this film's subject.

## Motion

2 of 15 beats animated, both within 0.1% of their measured audio. `hold` carries 86%, above the
~40% guidance, and that is a deliberate call rather than an omission: eleven of the thirteen
held beats state a fact, and holding on a fact is correct. Motion was added only where it
carries an argument —

- **B09** the shadow receding 3 → 2 → 1 across three claims. A recession is a change over time
  and cannot be a still by definition.
- **B07** one lamp differing between two pipelines. Animated, the extra lit stage is an event;
  held, it is a spot-the-difference.

## Gates

| | |
|---|---|
| Build | `build_beat_sheet.py --check` — clean, including a new `unshown-number` gate |
| Read-aloud | `gate_p_lint.py` — 17 flags → 12 accepted |
| Gate P | signed 2026-09-03, no revisions requested |
| Evidence | `verify_claims.py` — **13/13**, twelve of thirteen executable |

The `unshown-number` gate — a beat may not speak a figure its slate does not show — was written
*because* the PROOF review found B08 speaking "twenty-seven of the twenty-eight" over a frame
containing neither number. The narration gained that figure during Gate P; the slate had been
built a day earlier against a qualitative version. Nothing connected the two, so the gate is
that connection. It was then proven by reverting the slate and confirming it fires.

## The evidence, and why the script is not in this folder

`verify_claims.py` produces all thirteen claims rather than asserting them, including the
centrepiece: a deliberately broken pipeline whose output is byte-identical to the correct one
and which is caught only by an assertion about what was never called.

It is **not** included here because it imports the Zurich/Clara reference implementation, which
lives with the case study rather than in this repository. A script that cannot run is worse
than no script. `VERIFY-RESULTS.txt` is the saved output of the run that produced the numbers
in the film — evidence of record, honestly labelled as such.

One thing recorded there rather than quietly fixed: the first version of that harness held its
own module references, so the tests' patches never reached the broken code and it reported
**0 failures** — a false all-clear on a film about tests failing open.

## Captions

`.srt` and `.vtt` produced at build time from `beat_sheet.json`, 88 cues, none unwrappable, none
over 6 s. Kept with the masters in the Drive.
