# BUILD-LOG — bulk-ingestion-at-scale (week 2)

Built with **brutalist.art** (`ai-explainer`, channel `claude-hai`) from
`video_script_week2.md`. Free/local throughout: Kokoro TTS + Remotion + ffmpeg.
**$0.00 spent. No API key used.**

Second episode of the Private AI Valuation Agent series; sibling of
`../2026-08-08-Verifying-Private-AI-Valuations`.

---

## Inputs, and where they came from

| File | Origin |
|---|---|
| `narration_script.md` | Copy of `docs/video_script_week2.md` in the Mycroft repo — author-written, 438 spoken words, target 2:55. |
| `figdata_week2.json` | Copy of `docs/_figdata_week2.json`. The Mycroft repo queries this straight from the built Parquet, so no figure number is typed by hand. **Every on-screen number in this reel is a prop read from this file.** |
| `pantry/w2-*.png` + `pantry/w2-*.svg` | **Moved** (not copied) from `mycroft/images/private-ai-valuation-agent/`, as requested. Reference for the rebuild only — never slotted as media (REBUILD LAW). |

**On moving the images.** They were untracked in the Mycroft working tree, so the move was
irreversible there — but they are regenerable (`scripts/make_week2_figures.py` rebuilds all
three SVGs from `_figdata_week2.json`), and this folder is git-tracked, so the net effect is
that these figures are under version control for the first time. Both PNG **and** SVG were
moved: week 1's fact-check records that its SVG sources were lost from the Mycroft tree, and
leaving the sources behind to be orphaned the same way would have repeated that.

---

## The 33-point staircase is injected, not transcribed

B03 plots all 33 Anthropic period ends. Rather than typing them into the beat sheet, they are
read out of `figdata_week2.json` and written into `shot.remotion.props.series` by script. The
component then plots exactly what it is given. This keeps the Mycroft project's own P3
discipline — a chart cannot drift from the panel it describes — across the toolkit boundary.
Re-running the injection is idempotent.

---

## Decisions taken during the build

| # | Decision | Why |
|---|---|---|
| 1 | **The script's two combined shots were split into four beats.** | The script holds the staircase and the archive-lag problem on ONE figure ("stay on the staircase, point to the dashed line"), and pairs both traps into one shot. Split into B03/B05 and B06/B07 so no beat carries two ideas. No claim added or dropped. |
| 2 | **B05 teaches the lag MECHANISM, not the missing point.** | The script's shot note asks for the dashed line and the hollow circle. That shows *that* a mark is missing; it does not show *why*. B05 rebuilds it as period-covered vs filed, braced at ~56 days, with the archive band reaching only 30 Apr — because the cause is the part that reshapes week 3. The hollow $589 circle is kept, outside the boundary. |
| 3 | **B04 and B06 are deliberately inverse moves.** | B04 groups 24 registrations into 7 families; B06 collapses 5 apparent managers into 1. Same idea from both directions, two beats apart, in different visual languages. This is *why* B04's number is seven, and the reel shows the mechanism rather than asserting it. |
| 4 | **Greeting rotated to `Hej, HAI`.** | Week 1 used `Ola`. The hello lexicon rotates by reel so the channel does not repeat a language within a series. HAI takes only the short forms (Hi · Ola · Hej · Ciao). |
| 5 | **Kicker is `Irreducibly Human`, not a per-video topic.** | GATE L rule 7: `claude-hai` has a FIXED slot-1 series name in `runtime/qc/brand_labels.json`. Week 1 failed this gate by writing a per-video topic; that lesson is applied up front here, so GATE L passed on the first run. |
| 6 | **B06 is the shortest body beat (43 words).** | The script itself nominates the Fidelity trap as the first thing to cut if the reel runs long. It is kept, but written tight. |
| 7 | **`BulkIngestionAtScale.tsx` duplicates week 1's chrome helpers rather than importing them.** | Reel-local self-containment is the toolkit's existing convention (`DashboardThatLied.tsx`, `FluencyTrap.tsx` each define their own), and it guarantees week 1's signed master still re-renders byte-identically no matter what week 2 needs. |

---

## Toolkit state

All seven Windows/portability defects found during week 1 are still fixed and were exercised
again here — `npx` resolution, UTF-8 IO across the runtime scripts, `run.sh` path form, the
ffmpeg `drawtext` font path, GATE V sampling the clean cut, and the frame-keyed bookend scenes
being sized from `durationInSeconds`. **No new toolkit defects surfaced in this build**, which
is the first end-to-end run on a fresh reel since those fixes landed.

Added for this reel: `runtime/remotion/src/BulkIngestionAtScale.tsx` (seven components) and its
`BulkIngestionAtScale` folder in `Root.tsx`. Nothing else in the toolkit was modified.

---

## Visual QC — what LOOKING at the frames caught

GATE V's first pass reported 0 BLOCKER / 1 MAJOR. Reading the PNGs found three more things the
gate did not flag, two of them real.

| Beat | Defect | Severity | Fix |
|---|---|---|---|
| B05 | `low-contrast` — ink/background separation 0.29, under the 0.30 floor | MAJOR (gate) | The archive band was a 0.24 wash of terracotta on cream and the axis was a bare rule with no ticks. Band raised to 0.45, month ticks + labels added (31 Jan → 30 Jun), archive labels enlarged and darkened. The ticks are the real fix: they make "reaches only 30 Apr" read as a *position* rather than an assertion. |
| B06 | The five cards collapsed at 0.80 and left the lower two-thirds of the frame empty | MAJOR (missed by gate — bbox still spanned the frame) | Caption moved into the space the stack vacates, at 54px serif. |
| B06 | Fidelity's own card stayed at full opacity under the resolved card — two cards drawn at one position | MINOR | All five now fade as they merge. |
| B06 | `text-decoration: line-through` on a 150px serif rendered as a hairline artifact | MINOR | Struck rule drawn explicitly instead, and it now animates. |
| B04 | 24 ticks collapsed onto 7 identical x positions, so "24 → 7" read as ticks vanishing | MINOR | Each tick fans slightly within its cluster, so a cluster stays visibly a *group* of registrations. |
| B04 | Caption arrived at 0.90 and was still fading up as the beat ended | MINOR | Moved to 0.86–0.94. |

Frames re-read after each fix. Final pass: **22 frames, 0 BLOCKER, 0 MAJOR.**

---

## Gates

| Gate | State |
|---|---|
| **FACTCHECK** | 20 of 20 rows traced to `figdata_week2.json` or the Mycroft worklog. **Row 16 is derived rather than quoted** and is flagged for author confirmation. |
| **PROOF GATE / CHECKS-REPORT** | PASS — 7 SHOW / 4 justified-HOLD / 0 PUNT. Teaching arc 6/6. Written before the first compile. |
| **GATE P (pedagogy)** | **PASS — signed by the author (Om Mali), 2026-08-16**, after reviewing the slate cut. Covers the two structural splits, the FACTCHECK row-16 derivation, the B09 handoff prompt and the palette deviation. Audio for the pre-signature review cut was generated with `--no-gate`, recorded here rather than passed silently; the gate was re-run WITHOUT the override after signing and passes on its own. Narration is unchanged between the review cut and the master, so no audio was regenerated. |
| **GATE L** (beat-mix lint) | PASS on the first run — the fixed `claude-hai` kicker was set at authoring time. |
| **GATE V** (frame-level visual QC) | PASS — 22 frames, 0 BLOCKER, 0 MAJOR → `_qc/REPORT.md`. |
| **GATE F** | Not triggered — no Manim beats, so `SHOTLIST.md`/`PROMPTS.md` are not required. |

---

## Build facts

- **11 beats**, all filled by Remotion. Zero slates.
- **Audio**: Kokoro `am_onyx` (the fellow's persistent voice, unchanged from week 1), **180.70s
  (3:00.7)**. Measured durations are the master clock and are written into each scene's
  `durationInSeconds` prop, so every animation re-times to its real narration.
- **Seven reel-local scenes**, seven different visual schemes. No two consecutive body beats
  share one (ILLUSTRATE LAW).
- **Deliverables**: `bulk-ingestion-at-scale.mp4` — clean master, **3840×2160, 24fps, 180.7s**;
  `bulk-ingestion-at-scale-slate.mp4` — 1080p review cut with beat IDs and running timecode.
  Both mirrored into `mp4/`.
- **Never published.** The master stays in this folder. Publishing is a separate, explicitly
  human-authorized step that this toolkit does not perform.

## Finalization (2026-08-16)

GATE P signed. Before rendering the master, every beat was checked for staleness against its
scene source: `BulkIngestionAtScale.tsx` carries an mtime newer than the B01/B02/B03/B05/B07
renders, but the only edits after those renders were the B04 caption timing and the B06 caption
position — scoped entirely to `W2Convergence` and `W2FidelityTrap`, both of which were
re-rendered afterwards. Nothing else needed rebuilding.

`./art final` writes only the master, so `mp4/` was refreshed by hand afterwards. GATE V was
re-run against the 4K master itself (not the 1080 cut): **22 frames, 0 BLOCKER, 0 MAJOR.**
