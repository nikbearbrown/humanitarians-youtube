# Frictional log — What Does a P-Value Actually Mean?

*Drafted with Claude from the build logs; reviewed by me.*

## 2026-10-15 — research, script, both cuts and final masters

- **Drive:** https://drive.google.com/drive/folders/1Qv08qMadpEt0HqUofMmGLkYbmBDq5knF?usp=drive_link
- **Folder:** [README.md](README.md) · [SOURCES.md](SOURCES.md) · [BUILD-LOG.md](BUILD-LOG.md)

**What I was working on.** A 60-second-format explainer, my first outside Claude's
own behaviour: a p-value is how likely data this extreme would be if there were no
real effect. It is not the chance you're right, not the size or importance of an
effect, and p under 0.05 alone isn't proof. Primary source: the ASA Statement on
p-Values (Wasserstein & Lazar, 2016).

**What I tried, and what I expected.**
- I checked the shared repository first. No video explains p-values; the one title
  with "hypothesis" in it is about hypothesis-driven case interviews.
- I asked for the narration and on-screen text to be shown to me once before any
  building, so corrections would happen in the script, not in renders.

**Where it resisted, and what I did next.**
- **Wording direction.** The draft said a p-value is "how surprising your data
  would be if nothing were going on". Read literally, a bigger p-value then means
  more surprising data, which is backwards. I replaced it with the ASA's framing:
  how likely data this extreme is if there's no real effect.
- **One-sided vs two-sided.** The coin example's 11/1024 (about 1%) is a one-sided
  p-value; two-sided is about 2%. Logged in `SOURCES.md`.
- **Length.** My edits brought the script to 194 words; Claude trimmed lines I
  hadn't edited to bring it to 179, and the audio runs at Kokoro speed 1.08.
  The video is 63.7 s, not 60.
- **Math in the checks.** The type check (GATE T) read the two strokes of "≈" as
  undersized text. I sized the symbol instead of changing the checker.
- **Things the gates missed.** Checking portrait frames by eye found "ILLUSTRATIVE"
  overlapping the coin row and a box touching the line under it. Fixed and
  re-rendered, along with an underfilled diagram beat (B03) that visual QC flagged.

**What Claude contributed, and what I did with it.**
- Claude found the ASA's own release and a published quote of the definition (the
  journal page was blocked), confirmed the citation, computed every example number
  in code, and drafted the script and both cuts.
- I approved the script with edits: the greeting, the definition line, "If the null
  is true…", "p under zero point zero five", "its uncertainty", and the summary.
- I rewrote B06 on review to "A huge study can give a tiny effect a tiny p. A small
  study can give a big effect a large p.", which Claude retimed and re-rendered.
- I approved re-rendering the two portrait beats outside that change.

**What I understand now.**
- The common misreading of a p-value is a reversed conditional: the probability of
  the hypothesis given the data instead of the probability of the data given no
  real effect.
- Example numbers should be computed, with their assumptions stated.
- Automated checks catch a lot, but they read pixels, not meaning; I still have to
  look at the frames.

**Sign-off.** Pedagogy gate: reviewed and approved by me, with five known
weaknesses accepted. Both 4K masters passed GATE T and GATE V.
