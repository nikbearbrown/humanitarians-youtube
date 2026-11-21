# STATUS — Ep. 18, *counting-craters*

**DELIVERED.** Both masters built, verified by reading frames, and sitting in
the reel folder. Per house rule, **nothing is published.**

---

## Deliverables

| file | spec | size |
|---|---|---|
| `claude-for-astronomy_OmMali_20_11_2026.mp4` | **3840×2160**, 24 fps, 3834 frames, 159.75 s | 17.9 MB |
| `short/claude-for-astronomy_OmMali_20_11_2026.mp4` | **2160×3840**, 24 fps, 3834 frames, 159.75 s | 20.0 MB |

Runtime **2:39.8**, under the 3:00 ceiling. The master duration equals the
summed narration exactly — the audio really is the master clock.

The date is the **Friday of the build week**: built Saturday 2026-11-21, so
the tag is `20_11_2026`. Both cuts carry the same filename; the 9:16 lives in
`short/`.

The 9:16 is a real portrait build, not a crop: `scenes.py` restacks at
2160×3840 and the Remotion beats use their `*916` compositions.

`counting-craters.mp4` and `short/counting-craters-9x16.mp4` are the
pipeline's own outputs and will be overwritten by any recompile. The dated
files are copies and are the deliverables.

---

## Pipeline

| stage | result |
|---|---|
| Topic | `ideas.md` Astronomy #18, "Dating planets by their craters" |
| Facts | 11 claims traced in FACTCHECK; 7 corrections logged in SOURCES |
| Plates | 6 generated, **9 assertions** pass or nothing is written |
| GATE P | **signed** (Om Mali, 11/20/2026, on the human's written instruction) |
| Audio | Kokoro `af_bella`, 14 beats, 159.75 s measured |
| Pacing | solved to RT 1.550 / HOLD 0.148–0.719; **no `RT_PORTRAIT` needed** |
| GATE F | paperwork present |
| GATE A | **10/10 clean** |
| GATE W | **10/10 clean** |
| GATE B | **20/20 clean**, `--curve-strict`, both aspects |
| Remotion | 4 + 4 beats, props audited against all three zod schemas, 0 unknown |
| compile | **14/14 slots** both cuts, no slates |
| GATE V | 0 BLOCKER both cuts; 1 MAJOR (16:9) and 2 MAJOR (9:16), both measured and characterised in VISUAL-QC |
| Frames | read at native 4K in both aspects; 2 real defects found and fixed |
| **Spend** | **$0.00** |

---

## The episode

**Title:** *The Clock Needs a Rock.* · **Ep. 18** · playlist *AI in Astronomy
& Space Science* · register Pragmatist · audience STUDENTS.

The series spine is *when to use AI and when not to*. This is the first
episode in the run that answers **both ways at once**:

- **Counting craters is AI's job.** 384,343 Martian craters were catalogued by
  hand; the sub-kilometre population runs to tens of millions. Expert analysts
  disagree with each other by up to ±45%. DeepMoon recovers 92% of known
  craters and 42% of what it found was new.
- **Dating them is not.** Crater density becomes an age only through a
  chronology curve, and every anchor on that curve is a radiometrically dated
  rock somebody flew home. No detector has ever moved it.

The load-bearing beat is B08: push the published ±45% through the published
chronology function and it costs **16% of the answer on 3.5 Ga ground and 90%
on 1.0 Ga ground**. Precision matters most exactly where the curve had no
calibration point at all — until Chang'e-5 landed in the 1–3 Ga gap in 2020
and returned a rock dated to 2.030 ± 0.004 Ga, against a counted window 175×
wider.

---

## Four honest notes

1. **`surface.png` and `spread.png` are synthetic.** They make "denser =
   older" and "analysts disagree" visible. The only quantitative claim either
   makes is the 5.72× count ratio, which is asserted against the real
   chronology function (C6). The ±45% is cited from Robbins et al., never read
   off the simulation.
2. **The anchor positions in `anchors.png` are illustrative.** The sourced,
   load-bearing content is the *shape* — old cluster, empty middle, young
   cluster — and `gen_craters.py` asserts that no plotted anchor falls inside
   1–3 Ga.
3. **The counter-evidence weakens the headline, and it ships as a beat.** The
   Chang'e-5 recalibration moved the Neukum curve by at most 0.24 Gyr. Crater
   counting was never wildly wrong; it was loose. B10 says exactly that, and
   the rock's answer landed *inside* the counted window (C8).
4. **The 92% does not stand alone.** DeepMoon's raw network recall is 57%; it
   is on screen in the same beat, beneath the headline.

---

## Not done, deliberately

- **Not published.** No publishing machinery exists here and none was sought.
- **`ideas.md` not edited.** Eps. 16 and 17 are still marked `idea` in that
  backlog; this build did not touch the file, matching prior episodes.
- **The collection README not regenerated.** It is a generated inventory and
  is already stale for Eps. 03–17.
