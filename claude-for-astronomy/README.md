# Claude for Astronomy

This directory is the **Claude for Astronomy** collection in the Humanitarians YouTube production
repository. Each child project is a beat-sheet-driven video workspace; rendered media may be
gitignored or stored alongside its production files.

## Collection snapshot

- Video projects with `beat_sheet.json`: **1**
- Authored beats represented: **18**
- Masters present locally: **0**
- Review cuts present locally: **0**
- Audio-stage projects: **1**
- Beat-sheet-only projects: **0**
- Invalid/unreadable beat sheets: **0**

## How to read the inventory

- **State** is inferred from files currently present; it is not a publishing claim.
- **Runtime** uses measured beat durations when present and estimated durations otherwise.
- **QC**, **Facts**, and **Status** report whether `_qc/REPORT.md`, `FACTCHECK.md`, and
  `STATUS.md` exist.
- A local master is not permission to publish. YouTube uploads must use the channel ledger and
  publishing review gates.

## Video and beat-sheet inventory

| Project | Title | Series / genre | Persona / audience | Voice | Beats | Runtime | State | QC | Facts | Status |
|---|---|---|---|---|---:|---:|---|:---:|:---:|:---:|
| `ai-vs-the-data-deluge` | AI vs. the Data Deluge | AI in Astronomy & Space Science, Ep. 01 | General audience | af_heart | 18 | ~1:47 narration (full render longer) | audio present | no | yes | yes |

## Series notes

This is the first entry in a planned weekly series on AI applications in astronomy and space
science, chosen specifically because it had no overlap with this repository's existing
collections (cancer biology, nanomedicine, quantum mechanics, physics, mathematics,
computer-science/edge-AI, and others). 14 further topic ideas are scoped but not yet built:
exoplanet hunting (deep-dive), gravitational wave detection, galaxy classification, fast radio
bursts, Mars rover autonomy, cosmological simulation, asteroid tracking, deep-space image
denoising, real-time supernova classification, generative spacecraft design, solar storm
prediction, SETI signal detection, stellar spectra classification, and satellite collision
avoidance.

## Repository conventions

- The beat sheet is the production source of truth for narration, timing, shot routing,
  persona, and playlist metadata.
- Preserve source projects and audience variants; do not overwrite a sibling cut.
- Keep credentials, OAuth tokens, upload ledgers, and large generated media out of Git.
- Publishing is an external state change: preview the exact upload set, privacy, channel, and
  playlist before committing quota.

_This inventory is generated from the current filesystem and should be refreshed after
substantial batch changes._

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# Claude For Astronomy

This folder organizes **1 video project** built around beat sheets. Each project README explains
the subject, supplies research and fact-check prompts, and documents the free local rebuild
workflow.

## Rebuild toolkit

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Brutalist is audio-first and local: the beat sheet drives narration, measured audio becomes the
clock, generated visual beats compile immediately, and unavailable media remains as labeled
slates until a human fills the pantry. The human conducts, watches, fact-checks, refines, and
decides whether anything is published.

## Projects in this folder

- [AI vs. the Data Deluge](./ai-vs-the-data-deluge/)

<!-- END BRUTALIST REBUILD GUIDE -->
