# Claude for Business

This directory is the **Claude for Business** collection in the Humanitarians YouTube production repository. Each child project is a beat-sheet-driven video workspace; rendered media may be gitignored or stored alongside its production files.

## Collection snapshot

- Video projects with `beat_sheet.json`: **1**
- Authored beats represented: **20**
- Masters present locally: **0**
- Review cuts present locally: **0**
- Audio-stage projects: **0**
- Beat-sheet-only projects: **1**
- Invalid/unreadable beat sheets: **0**

## How to read the inventory

- **State** is inferred from files currently present; it is not a publishing claim.
- **Runtime** uses measured beat durations when present and estimated durations otherwise.
- **QC**, **Facts**, and **Status** report whether `_qc/REPORT.md`, `FACTCHECK.md`, and `STATUS.md` exist.
- A local master is not permission to publish. YouTube uploads must use the channel ledger and publishing review gates.

## Video and beat-sheet inventory

| Project | Title | Series / genre | Persona / audience | Voice | Beats | Runtime | State | QC | Facts | Status |
|---|---|---|---|---|---:|---:|---|:---:|:---:|:---:|
| `claude-liam-hawthorne-effect` | Claude, Observed | Claude for Management | Claude | am_onyx | 20 | 5:05 | beat sheet authored | no | yes | yes |

## Repository conventions

- The beat sheet is the production source of truth for narration, timing, shot routing, persona, and playlist metadata.
- Preserve source projects and audience variants; do not overwrite a sibling cut.
- Keep credentials, OAuth tokens, upload ledgers, and large generated media out of Git.
- Publishing is an external state change: preview the exact upload set, privacy, channel, and playlist before committing quota.

_This inventory is generated from the current filesystem and should be refreshed after substantial batch changes._


<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# Claude For Business

This folder organizes **1 video project** built around beat sheets. Each project README explains the subject, supplies research and fact-check prompts, and documents the free local rebuild workflow.

## Rebuild toolkit

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Brutalist is audio-first and local: the beat sheet drives narration, measured audio becomes the clock, generated visual beats compile immediately, and unavailable media remains as labeled slates until a human fills the pantry. The human conducts, watches, fact-checks, refines, and decides whether anything is published.

## Projects in this folder

- [Hawthorne Effect](./claude-liam-hawthorne-effect/)

<!-- END BRUTALIST REBUILD GUIDE -->
