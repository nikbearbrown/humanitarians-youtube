# Claude for Astronomy

This directory is the **Claude for Astronomy** collection in the Humanitarians YouTube production
repository. Each child project is a beat-sheet-driven video workspace; rendered media may be
gitignored or stored alongside its production files.

## Collection snapshot

- Video projects with `beat_sheet.json`: **2**
- Authored beats represented: **39** (19 + 20)
- Masters present locally: **2** (`ai-vs-the-data-deluge`, rendered 2026-08-01; `exoplanet-hunting`,
  rendered 2026-08-01)
- Review cuts present locally: **0**
- Audio-stage projects: **0**
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
| `ai-vs-the-data-deluge` | AI vs. the Data Deluge | AI in Astronomy & Space Science, Ep. 01 | General audience | af_heart | 19 | 117.5s (~1:58), 4K master rendered | complete — master rendered | no | yes | yes |
| `exoplanet-hunting` | Exoplanet Hunting: Teaching AI to Show Its Work | AI in Astronomy & Space Science, Ep. 02 | General audience | af_heart | 20 | 150.0s (~2:30), 4K master rendered | complete — master rendered | no | yes | yes |

## Series notes

This is a planned weekly series on AI applications in astronomy and space science, chosen
specifically because it had no overlap with this repository's existing collections (cancer
biology, nanomedicine, quantum mechanics, physics, mathematics, computer-science/edge-AI, and
others). Ep. 01 covered AstroNet's two-view CNN and the Kepler-90i discovery. Ep. 02,
`exoplanet-hunting`, is a deliberate follow-up rather than a repeat: it names the three
false-positive signal types Ep. 01 never covered (eclipsing binary, stellar variability,
instrumental artifact) and centers on NASA's ExoMiner — an explainable, separate-diagnostic-branch
classifier — and its 301-planet Kepler batch validation plus 2026 TESS extension (ExoMiner++).
Ep. 02 has been voiced (Kokoro `af_heart`) and rendered to a 4K master, with a presenter
self-introduction beat (B02) added 2026-08-01 for series consistency with Ep. 01's own intro card
(see `exoplanet-hunting/STATUS.md`).

13 further topic ideas are scoped but not yet built: gravitational wave detection, galaxy
classification, fast radio bursts, Mars rover autonomy, cosmological simulation, asteroid
tracking, deep-space image denoising, real-time supernova classification, generative spacecraft
design, solar storm prediction, SETI signal detection, stellar spectra classification, and
satellite collision avoidance.

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

This folder organizes **2 video projects** built around beat sheets. Each project README explains
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
- [Exoplanet Hunting: Teaching AI to Show Its Work](./exoplanet-hunting/)

<!-- END BRUTALIST REBUILD GUIDE -->
