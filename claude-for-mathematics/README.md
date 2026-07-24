# Claude for Mathematics

This directory is the **Claude for Mathematics** collection in the Humanitarians YouTube production repository. Each child project is a beat-sheet-driven video workspace; rendered media may be gitignored or stored alongside its production files.

## Collection snapshot

- Video projects with `beat_sheet.json`: **22**
- Authored beats represented: **254**
- Masters present locally: **0**
- Review cuts present locally: **0**
- Audio-stage projects: **0**
- Beat-sheet-only projects: **21**
- Invalid/unreadable beat sheets: **0**

## How to read the inventory

- **State** is inferred from files currently present; it is not a publishing claim.
- **Runtime** uses measured beat durations when present and estimated durations otherwise.
- **QC**, **Facts**, and **Status** report whether `_qc/REPORT.md`, `FACTCHECK.md`, and `STATUS.md` exist.
- A local master is not permission to publish. YouTube uploads must use the channel ledger and publishing review gates.

## Video and beat-sheet inventory

| Project | Title | Series / genre | Persona / audience | Voice | Beats | Runtime | State | QC | Facts | Status |
|---|---|---|---|---|---:|---:|---|:---:|:---:|:---:|
| `arrows-impossibility` | Arrow's Impossibility — Same Ballots, Different Winners | — | — | af_kore | 11 | 1:57 | beat sheet authored | no | yes | no |
| `compound-interest-simulator` | Compound Interest — The Exponential Cliff | — | — | af_kore | 11 | 1:57 | beat sheet authored | no | yes | no |
| `konigsberg-bridge-solver` | Königsberg Bridges — Euler's Theorem | — | — | af_kore | 11 | 1:57 | beat sheet authored | no | yes | no |
| `law-of-large-numbers` | Law of Large Numbers — Convergence | — | — | af_kore | 11 | 1:57 | beat sheet authored | no | yes | no |
| `medhavy-vox-probability-density` | Why a Probability Density Can Be Greater Than One | — | MEDHAVY | af_kore | 14 | 3:03 | beat sheet authored | no | no | no |
| `metric-conversion-auditor` | Unit Mismatch — Mars Climate Orbiter ($325M) | — | — | af_kore | 11 | 1:57 | beat sheet authored | no | yes | no |
| `nbb-arrows-impossibility` | Arrow's Impossibility — Same Ballots, Different Winners | — | NikBearBrown | af_kore | 14 | 2:36 | beat sheet authored | no | yes | no |
| `nbb-compound-interest-simulator` | Compound Interest — The Exponential Cliff | — | NikBearBrown | af_kore | 14 | 2:35 | beat sheet authored | no | yes | no |
| `nbb-konigsberg-bridge-solver` | Königsberg Bridges — Euler's Theorem | — | NikBearBrown | af_kore | 14 | 2:37 | beat sheet authored | no | yes | no |
| `nbb-law-of-large-numbers` | Law of Large Numbers — Convergence | — | NikBearBrown | af_kore | 14 | 2:34 | beat sheet authored | no | yes | no |
| `nbb-metric-conversion-auditor` | Unit Mismatch — Mars Climate Orbiter ($325M) | — | NikBearBrown | af_kore | 14 | 2:37 | beat sheet authored | no | yes | no |
| `nbb-number-base-converter` | Number Base Converter — 738 in Base 10, 2, 16 | — | NikBearBrown | af_kore | 14 | 2:39 | beat sheet authored | no | yes | no |
| `nbb-prime-factorization-timer` | Prime Factorization — The RSA Asymmetry | — | NikBearBrown | af_kore | 14 | 2:40 | beat sheet authored | no | yes | no |
| `nbb-sampling-bias-demonstrator` | Sampling Bias — The 1936 Literary Digest Disaster | — | NikBearBrown | af_kore | 14 | 2:36 | beat sheet authored | no | yes | no |
| `number-base-converter` | Number Base Converter — 738 in Base 10, 2, 16 | — | — | af_kore | 11 | 1:57 | beat sheet authored | no | yes | no |
| `prime-factorization-timer` | Prime Factorization — The RSA Asymmetry | — | — | af_kore | 11 | 1:57 | beat sheet authored | no | yes | no |
| `review-naked-statistics-stripping` | Naked Statistics: Stripping the Dread from the Data — Book Review | — | HAI Fellows | af_kore | 10 | 1:25 | beat sheet authored | yes | no | no |
| `riff-manim-math-to-manim` | The Brutalist Manim Shelf — Math-To-Manim | — | — | af_kore | 0 | — | scaffold | no | no | no |
| `sampling-bias-demonstrator` | Sampling Bias — The 1936 Literary Digest Disaster | — | — | af_kore | 11 | 1:57 | beat sheet authored | no | yes | no |
| `the-art-of-statistics-how-to-learn` | The Art of Statistics: How to Learn from Data — Book Review | — | HAI Fellows | af_kore | 10 | 1:40 | beat sheet authored | yes | no | no |
| `the-math-of-being-afraid-together` | The Math of Being Afraid Together: Co-op Horror Design | — | HAI Fellows | af_kore | 10 | 1:22 | beat sheet authored | yes | no | no |
| `why-120-bpm-works-the-hidden-mathematics` | The Sesame Street Conspiracy | — | HAI Fellows | af_kore | 10 | 1:18 | beat sheet authored | yes | no | no |

## Repository conventions

- The beat sheet is the production source of truth for narration, timing, shot routing, persona, and playlist metadata.
- Preserve source projects and audience variants; do not overwrite a sibling cut.
- Keep credentials, OAuth tokens, upload ledgers, and large generated media out of Git.
- Publishing is an external state change: preview the exact upload set, privacy, channel, and playlist before committing quota.

_This inventory is generated from the current filesystem and should be refreshed after substantial batch changes._

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# Claude For Mathematics

This folder organizes **22 video projects** built around beat sheets. Each project README explains the subject, supplies research and fact-check prompts, and documents the free local rebuild workflow.

## Rebuild toolkit

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Brutalist is audio-first and local: the beat sheet drives narration, measured audio becomes the clock, generated visual beats compile immediately, and unavailable media remains as labeled slates until a human fills the pantry. The human conducts, watches, fact-checks, refines, and decides whether anything is published.

## Projects in this folder

- [Arrows Impossibility](./arrows-impossibility/)
- [Compound Interest Simulator](./compound-interest-simulator/)
- [Konigsberg Bridge Solver](./konigsberg-bridge-solver/)
- [Law Of Large Numbers](./law-of-large-numbers/)
- [Vox Probability Density](./medhavy-vox-probability-density/)
- [Metric Conversion Auditor](./metric-conversion-auditor/)
- [Arrows Impossibility](./nbb-arrows-impossibility/)
- [Compound Interest Simulator](./nbb-compound-interest-simulator/)
- [Konigsberg Bridge Solver](./nbb-konigsberg-bridge-solver/)
- [Law Of Large Numbers](./nbb-law-of-large-numbers/)
- [Metric Conversion Auditor](./nbb-metric-conversion-auditor/)
- [Number Base Converter](./nbb-number-base-converter/)
- [Prime Factorization Timer](./nbb-prime-factorization-timer/)
- [Sampling Bias Demonstrator](./nbb-sampling-bias-demonstrator/)
- [Number Base Converter](./number-base-converter/)
- [Prime Factorization Timer](./prime-factorization-timer/)
- [Review Naked Statistics Stripping](./review-naked-statistics-stripping/)
- [Riff Manim Math To Manim](./riff-manim-math-to-manim/)
- [Sampling Bias Demonstrator](./sampling-bias-demonstrator/)
- [The Art Of Statistics How To Learn](./the-art-of-statistics-how-to-learn/)
- [The Math Of Being Afraid Together](./the-math-of-being-afraid-together/)
- [Why 120 Bpm Works The Hidden Mathematics](./why-120-bpm-works-the-hidden-mathematics/)

<!-- END BRUTALIST REBUILD GUIDE -->
