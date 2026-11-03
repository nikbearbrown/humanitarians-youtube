# Frictional log — Explainer: Mixture of Experts

## 2026-10-23 — claude-hai explainer, 16:9 + 9:16

- **Drive:** https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G

Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`,(11/12, gate PASS), `_qc/REPORT.md`, `mixture-of-experts.mp4`,`short/mixture-of-experts-short.mp4`. 

**What I was working on.** An explainer on Mixture of Experts (MoE), framework-first:
many experts + a router that runs only a few per token, so the model is huge in *total*
parameters but small in *active* parameters — capacity pulled apart from cost. Kept
qualitative (no param counts, FLOPs, or model names).

**What I tried, and what I expected.**
* By now the pipeline is mature — the card generator has every kind I need, the
  sequential audio → render order is habit, the interpreter is pinned. I expected a
  clean, uneventful build.


**What Claude contributed, and what I did with it.**
* Mine: the topic, the framework (total vs active),
* Claude's: flagged the disk risk and refused to blind-render at 2.6 GB; cleared only
  regenerable scratch (never finals or other projects); built the whole reel (beat sheet,
  cards, Kokoro audio, Remotion bookends, 4K compiles, QC, PROOF) under `/usr/bin/python3`
  (the one interpreter here that still has Pillow).

**What I understand now, and what I still do not.**
* Understood: the limiting resource has shifted from the toolkit to the machine's free
  disk. A 4K reel needs real headroom, and the first safe thing to reclaim is the
  regenerable `clips/` caches — not the finals, not other people's projects.
* Not resolved: the drive is genuinely full (other projects, plus `.git` holding 605 MB
  of committed reel videos because the root `.gitignore` never matched our `<slug>.mp4`
  names). This needs a real cleanup, not just clearing my scratch.
