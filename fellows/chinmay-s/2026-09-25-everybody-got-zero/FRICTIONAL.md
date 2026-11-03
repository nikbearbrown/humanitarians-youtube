# Frictional log — The Test Where Everybody Got Zero

## 2026-09-25 — 4:01, 22 beats, Bella / Humanitarians AI

Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`, `build_beat_sheet.py`. Master MP4 held outside Git per repository policy. (YouTube: TBD.)

**What I was working on.** A kid-friendly retelling of the eval-harness teardown.

**What I tried, and what I expected.** I expected this to be a visual job — same
narration, friendlier pictures.

**Where it resisted, and what I did next.**
* It is not. The narration said "KS statistic," "exact match," "base rate." A child
  watching the friendliest animation still loses the thread in the audio. It needed a
  rewrite, not a reskin, so it became a separate cut rather than a patch.
* The `Grader` character rendered nothing. It returns an SVG `<g>`, so it only draws
  inside an `<svg>`; I had placed it as a bare child of a `div`. Robo appeared, the
  teacher did not, and the QC sheet caught it.
* Found the metaphors by asking what the bug physically resembles: a full stop that
  sticks like chewing gum, a machine with teeth that eats the accent off Brasília.

**What Claude contributed, and what I did with it.** Mine: the decision that a kid cut
needs new narration, not new pictures. Claude's: the metaphors, two characters, the
`<svg>` stage fix.

**What I understand now, and what I still do not.**
* Understood: "explain it for kids" is an audio problem first. The visuals are the easy
  half.
* Not resolved: I have not watched a child watch it. Whether the gum metaphor lands is
  still a guess.
