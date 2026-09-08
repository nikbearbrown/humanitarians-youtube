# Can AI Discover New Quantum Materials? — 3-Minute Evidence Review Film

Complete, reproducible source for Dhrumil Shah's three-minute 16:9 explainer on
what machine learning actually does in superconductor search. It is an
evidence-first review, not a discovery announcement.

## Deliverable

- **Master:** 3840 x 2160, 16:9, 24 fps, exactly 03:00
- **Renderer:** Remotion / React / TypeScript inside the supplied
  `brutalist.art-main` workspace
- **Narration:** 16 beats generated locally with Kokoro (`am_onyx`), measured
  and used as the master clock
- **Evidence:** typeset citations held on screen at the moment of each claim,
  plus one computed chart of published measured critical temperatures

## The argument

**AI does not discover superconductors. It reorders the search queue. The
laboratory still decides.**

The film shows that confirmation is a five-link chain — rank, stability,
synthesis, zero-resistance measurement, Meissner effect — and that machine
learning touches exactly one link. It then stress-tests its own rubric against
LK-99, the 2023 room-temperature superconductivity claim that collapsed under
replication.

## The framework: CLAIM

Five questions, on screen at 00:26, before any example. Labelled on screen as
the presenter's review framework — it is not a feature of any dataset or model.

| Axis | Question |
|---|---|
| **C** — Composition | Is there an exact, synthesizable formula? |
| **L** — Labels | Measured Tc, or a computed proxy? |
| **A** — Applicability | Is the candidate inside the training distribution? |
| **I** — Independent | Has another laboratory reproduced it? |
| **M** — Measurement | Zero resistance *and* Meissner — at what pressure? |

I and M are the two axes no model can supply. That is the film's thesis, and
the LK-99 case is where it is demonstrated rather than asserted.

## What the film claims, and what it does not

**It supports:** the composition of the standard public training table
(21,263 measured superconductors, 81 composition-derived features, no
structural inputs); the measured critical-temperature record from 1911 to 2019
with high pressures stated; the five-stage confirmation chain; and the
published LK-99 replication record.

**It explicitly does not claim:** a new superconductor, a screening campaign it
did not run, or any acceleration figure. The funnel in Scene 05 is labelled an
illustrative schematic on screen and in narration.

**One open item.** The ±9.5 K RMSE in Scene 04 is believed correct but is
flagged VERIFY in [FACTCHECK.md](FACTCHECK.md) and must be confirmed against
Hamidieh 2018 §4 before public release. See [PROOF-COMPLIANCE.md](PROOF-COMPLIANCE.md)
for the resulting ship verdict.

## Folder map

```text
can-ai-discover-new-quantum-materials-16x9/
├── src/CanAIDiscoverQuantumMaterials.tsx  # complete 4K Remotion composition
├── mp3/                                   # 16 Kokoro narration beats + timings.json
├── scripts/                               # sync, render, verify, QC stills
├── output/                                # rendered master (gitignored)
├── _qc/                                   # preflight + final QA stills (gitignored)
├── beat_sheet.json                        # authored source of truth
├── final_beat_sheet.json                  # archived post-audio snapshot
├── todo.json                              # machine-readable beat + open-item ledger
├── CURRENT-RENDER-MANIFEST.md             # canonical 180 s render map
├── SOURCE-SCRIPT.md                       # exact narration in this cut
├── PRODUCTION-PLAN.md                     # 10-scene visual and evidence map
├── SHOTLIST.md                            # shot-by-shot legibility contract
├── PROOF-COMPLIANCE.md                    # skeptical review, rubric, ship verdict
├── FACTCHECK.md                           # claim-by-claim verdicts and open items
├── SOURCES.md                             # full citations, grouped by scene
├── PEDAGOGY.md                            # narration gate and register audit
├── ASSET-PROVENANCE.md                    # origin of every asset
├── REFERENCE-ANALYSIS.md                  # what the references informed
├── INTEGRATION.md                         # Remotion registry contract
├── STATUS.md / ToDo.md                    # stage and remaining work
└── FINAL-QA.md                            # rendered-master verification
```

`CURRENT-RENDER-MANIFEST.md`, the TypeScript composition, and
`SOURCE-SCRIPT.md` are the authoritative runtime documents.

## Prerequisites

- Windows PowerShell 5.1+ or PowerShell 7+
- Node.js 20+
- `runtime/remotion` dependencies installed
- A local Chrome or Chrome Headless Shell for Remotion
- `ffmpeg` / `ffprobe` on PATH
- Python 3.12 with `kokoro-onnx` (only to regenerate narration)

No remote API, model account, or paid service is required. Everything runs
locally and free.

## Build

From this directory:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\render-4k.ps1
```

The script syncs the composition and audio into the workspace renderer, renders
the MP4, then runs verification. Output:

```text
output/can-ai-discover-new-quantum-materials-4k.mp4
```

Sync only:

```powershell
.\scripts\sync-to-remotion.ps1
```

Verify an existing master:

```powershell
.\scripts\check-video.ps1 -VideoPath .\output\can-ai-discover-new-quantum-materials-4k.mp4
```

Extract eleven QC stills:

```powershell
.\scripts\qc-stills.ps1 -VideoPath .\output\can-ai-discover-new-quantum-materials-4k.mp4
```

## Regenerate the narration

From the workspace root:

```powershell
python runtime/scripts/generate_audio_kokoro.py youtube/mycroft-thesisguard-brief/can-ai-discover-new-quantum-materials-16x9
```

This rewrites `mp3/beat-*.mp3` and `mp3/timings.json` and stamps
`actual_duration_s` back into `beat_sheet.json`. **If any duration changes,
update `AUDIO_BEATS` in the composition to match** — the audio is the clock,
and the composition must follow it, never the reverse.

## Development preview

After syncing, from `runtime/remotion`:

```powershell
npm run studio
```

Choose **Quantum-Materials / CanAIDiscoverQuantumMaterials**.

## Publishing

There is no publishing machinery here and none was used. A rendered master is
not authorization to upload. Before any public release, resolve the open
VERIFY item in [FACTCHECK.md](FACTCHECK.md) and read
[PROOF-COMPLIANCE.md](PROOF-COMPLIANCE.md).
