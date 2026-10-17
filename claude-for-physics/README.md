# Claude for Physics

This directory is the **Claude for Physics** collection in the Humanitarians YouTube production repository. Each child project is a beat-sheet-driven video workspace; rendered media may be gitignored or stored alongside its production files.

## Collection snapshot

- Video projects with `beat_sheet.json`: **12**
- Authored beats represented: **110**
- Masters present locally: **0**
- Review cuts present locally: **0**
- Audio-stage projects: **0**
- Beat-sheet-only projects: **6**
- Invalid/unreadable beat sheets: **0**

## How to read the inventory

- **State** is inferred from files currently present; it is not a publishing claim.
- **Runtime** uses measured beat durations when present and estimated durations otherwise.
- **QC**, **Facts**, and **Status** report whether `_qc/REPORT.md`, `FACTCHECK.md`, and `STATUS.md` exist.
- A local master is not permission to publish. YouTube uploads must use the channel ledger and publishing review gates.

## Video and beat-sheet inventory

| Project | Title | Series / genre | Persona / audience | Voice | Beats | Runtime | State | QC | Facts | Status |
|---|---|---|---|---|---:|---:|---|:---:|:---:|:---:|
| `hai-who-was-albert-einstein` | Who was Albert Einstein? | — | HAI | af_kore | 11 | 3:59 | beat sheet authored | no | yes | no |
| `hai-who-was-max-planck` | Who was Max Planck? | — | HAI | af_kore | 13 | 2:47 | beat sheet authored | no | yes | yes |
| `medhavy-who-was-albert-einstein` | Who was Albert Einstein? | — | MEDHAVY | af_kore | 11 | 3:32 | beat sheet authored | no | yes | no |
| `medhavy-who-was-max-planck` | Who was Max Planck? | — | MEDHAVY | af_kore | 13 | 2:36 | beat sheet authored | no | yes | yes |
| `who-was-albert-einstein` | Who was Albert Einstein? | — | NikBearBrown | af_kore | 13 | 2:32 | beat sheet authored | no | no | no |
| `who-was-max-planck` | Who was Max Planck? | — | NikBearBrown | af_kore | 13 | 2:32 | beat sheet authored | no | no | no |
| `medhavy-ball-and-feather` | Which Falls Faster? | Physics Vol. 1 §3.5 | MEDHAVY | am_michael | 6 | 2:03 | published (YouTube Short) | no | no | no |
| `medhavy-car-turning` | Is A Turning Car Still Accelerating? | Physics Vol. 1 §4.2 | MEDHAVY | am_michael | 6 | 1:35 | published (YouTube Short) | no | no | no |
| `medhavy-rain-relative-motion` | Why Does Rain Hit You From The Front? | Physics Vol. 1 §4.5 | MEDHAVY | am_michael | 6 | 1:24 | published (YouTube Short) | no | no | no |
| `medhavy-horse-cart-paradox` | How Does Anything Ever Move? | Physics Vol. 1 §5.5 | MEDHAVY | am_michael | 6 | 1:54 | published (YouTube Short) | no | no | no |
| `medhavy-inertia-puck` | What Really Stops A Sliding Puck? | Physics Vol. 1 §5.2 | MEDHAVY | am_michael | 6 | 1:16 | published (YouTube Short) | no | no | no |
| `medhavy-weight-vs-mass` | Did She Lose Five-Sixths Of Her Mass? | Physics Vol. 1 §5.4 | MEDHAVY | am_michael | 6 | 1:49 | published (YouTube Short) | no | no | no |

## Repository conventions

- The beat sheet is the production source of truth for narration, timing, shot routing, persona, and playlist metadata.
- Preserve source projects and audience variants; do not overwrite a sibling cut.
- Keep credentials, OAuth tokens, upload ledgers, and large generated media out of Git.
- Publishing is an external state change: preview the exact upload set, privacy, channel, and playlist before committing quota.

_This inventory is generated from the current filesystem and should be refreshed after substantial batch changes._

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# Claude For Physics

This folder organizes **12 video projects** built around beat sheets. Each project README explains the subject, supplies research and fact-check prompts, and documents the free local rebuild workflow.

## Rebuild toolkit

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Brutalist is audio-first and local: the beat sheet drives narration, measured audio becomes the clock, generated visual beats compile immediately, and unavailable media remains as labeled slates until a human fills the pantry. The human conducts, watches, fact-checks, refines, and decides whether anything is published.

## Projects in this folder

- [Who Was Albert Einstein](./hai-who-was-albert-einstein/)
- [Who Was Max Planck](./hai-who-was-max-planck/)
- [Who Was Albert Einstein](./medhavy-who-was-albert-einstein/)
- [Who Was Max Planck](./medhavy-who-was-max-planck/)
- [Who Was Albert Einstein](./who-was-albert-einstein/)
- [Who Was Max Planck](./who-was-max-planck/)
- [Which Falls Faster?](./medhavy-ball-and-feather/)
- [Is A Turning Car Still Accelerating?](./medhavy-car-turning/)
- [Why Does Rain Hit You From The Front?](./medhavy-rain-relative-motion/)
- [How Does Anything Ever Move?](./medhavy-horse-cart-paradox/)
- [What Really Stops A Sliding Puck?](./medhavy-inertia-puck/)
- [Did She Lose Five-Sixths Of Her Mass?](./medhavy-weight-vs-mass/)

<!-- END BRUTALIST REBUILD GUIDE -->
