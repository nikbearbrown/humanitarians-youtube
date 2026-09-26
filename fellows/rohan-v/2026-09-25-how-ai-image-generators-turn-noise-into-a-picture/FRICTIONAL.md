# FRICTIONAL — How AI Image Generators Turn Noise Into a Picture

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-09-25 — Image diffusion explainer (week 6, STEM)

> Written during the build, with Claude, from this session's record. The
> decisions and corrections are mine.

**Working on.** How an image generator like Midjourney turns random noise into a
picture — for Lyrical Literacy fellows who use Midjourney but have never been
told what it does. Paired with this week's progress video.

**Tried, and expected.**
- Asked for one STEM video on audio, AI or both, planned carefully, with strong
  motion graphics, on the current Brutalist framework — pulling its latest
  changes first.
- The first proposal was how music generators turn sound into tokens. I expected
  we had already made something close to it, and asked for a check.

**Where it resisted, and what I did next.**
- The check found no tokens video, but two of its beats repeated the MP3 and
  Nyquist videos. I dropped it and asked for more options, twice; chose image
  diffusion from fifteen.
- The framework had changed: equations must be properly typeset, and anything we
  can compute must be run, not pictured. So a small diffusion model was trained
  from scratch on my laptop (numpy, CPU, 31 minutes) and every picture in the
  video is its output.
- There was no torch, and C: had under 9 GB free, so nothing big was installed.
  The math renderer's one dependency, matplotlib, was missing entirely; it went
  into the toolkit folder on D:, not C:.
- The note generated from seed 7 was faint. Instead of picking a nicer seed by
  eye, 40 seeds were scored against the real training set by a written rule, and
  seed 38 was chosen (`scan_seeds.py`, all 40 results kept).
- Importing the training script from the later scripts silently emptied its log.
  It was restored from the run's captured output; the script was not edited,
  because its hash is part of the record.
- A caption said "your grid of four". My own Midjourney captures from week 3
  showed one row of four, not a grid, so it was corrected before the final render.
- The equation's two "shares" are multipliers that don't add to 100%. They are
  shown as × 0.78 / × 0.62, not percentages, so the video doesn't teach a false sum.
- The first 9:16 cuts failed the framework's type check: on a phone, body text has
  to be about 4% of the screen height, and most portrait labels were half that.
  Every portrait layout was rebuilt with less text, larger, and short strings
  written for the vertical cut only.

**What Claude contributed — accepted, changed, rejected.**
- Claude merged the Brutalist update, wrote and trained the toy model, the seed
  scan and the exporter, built five new scenes with native portrait layouts, and
  drafted the docs.
- Rejected: the tokens topic (too close to earlier videos) and the first list of
  three topics (I wanted more options).
- Accepted: the diffusion topic, the toy-model approach, quoting Midjourney's own
  Seeds page instead of guessing at its internals.

**Understand now / still don't.**
- Now: an image generator starts from static and removes a little noise many
  times; the prompt steers each step, and the seed only decides the starting
  static. That is why locking a seed makes a prompt test fair.
- Still don't know: how Midjourney's own model differs from this — it isn't
  published.

**Evidence:** [`MEASUREMENTS.txt`](./MEASUREMENTS.txt) · [`train_toy_diffusion.py`](./train_toy_diffusion.py) ·
[`scan_seeds.py`](./scan_seeds.py) · [`FACTCHECK.md`](./FACTCHECK.md) · [`qc-sheet-16x9.png`](./qc-sheet-16x9.png)
