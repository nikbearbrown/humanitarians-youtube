# Frictional log — Explainer: What Is MCP



## 2026-08-24 — the CLI explainer, in two aspect ratios

- **Video:** [MCP](https://www.youtube.com/watch?v=a1tiMgiQDfg) 
- **Drive:** https://drive.google.com/drive/folders/1BS4mqXHacyxOIfFH9vQwKDVt2q36ZS23?usp=sharing 
- **Report:** [REPORT.md](REPORT.md)
- **Paired sprint:** [Sprint 1 — request logbook](../08282026-mycroft-logbook/)



**What I was working on.** A `cli-explainer` on what the Model Context Protocol
is  one standard interface an AI application can call tools through  cut at
both 16:9 and 9:16, using the house components with one terracotta accent per
beat, opening on the verbatim line *"Hi, I am Simba, and this video is about
MCP  …"*.

**What I tried, and what I expected.**
- I assumed the compiler's `--height` flag meant "render at 2160" whatever the
  orientation.
- I assumed the beat sheets' `metadata.aspect` field was what the compiler read
  to decide aspect ratio.
- Both assumptions were wrong, and neither failed loudly.

**Where it resisted, and what I did next.**
- **The 9:16 cut compiled at 1216×2160 instead of 2160×3840.** `--height` means
  *long edge*, not "always 2160", so a 4K portrait render needs `--height 3840`
  stated explicitly. Caught by measuring the finished file's dimensions rather
  than trusting that the flag did what its name suggested. Re-measured after the
  fix.
- **A real bug, not a cosmetic one: the beat sheets used `metadata.aspect`, but
  the compiler reads `metadata.aspect_ratio`.** Left alone this would have framed
  the 9:16 cut as 16:9 with no error at all  a wrong file, not a failed build.
  Fixed in both the master sheets and the working copies.


**What Claude contributed, and what I did with it.**
- Mine: the research  working out how MCP actually works  and the diagrams.
- Claude's: the beat sheet built from those, then production of both cuts, then
  QC by pulling **actual frames from the compiled files**  not component stills
   across the intro, a middle illustration beat, the code and output beats, and
  the outro, at both aspect ratios, checking nothing clipped and the safe area
  held.
- Claude checked the verbatim intro line against the rendered frame rather than
  against the script, which is how the stale-persona audio was caught; audio and
  video were regenerated to match.
- Caught without being asked to look: the `metadata.aspect` /
  `metadata.aspect_ratio` mismatch  a bug that fails silently.

**What I understand now, and what I still do not.**

- Understood: a mismatched metadata key produces a wrong-but-plausible file
  instead of an error, so QC has to measure the artifact, not read the config.
- Understood, and it is the same lesson my project work keeps teaching: the
  failures worth fearing are the ones that produce a plausible result and no
  error message.
- Not resolved: whether the tracker's single YouTube link is the 16:9 cut, the
  9:16 cut, or a combined upload. The tracker lists one link for two cuts.
- Not resolved: the exact build date inside the 24–28 Aug window.