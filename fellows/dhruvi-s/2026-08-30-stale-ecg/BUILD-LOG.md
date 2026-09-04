# BUILD-LOG — stale-ecg

*A Stale ECG Is Worse Than No ECG* · cli-explainer · @HumanitariansAI ·
Kokoro `af_bella` (Bella, Pragmatist register) · free pipeline, never published.

---

## 2026-08-29 — authored, built, both cuts compiled (Claude Code session)

- **HUMAN NOTE (logged first):** Dhruvi Shah — "generate video report" for
  `mimic-research`, a MIMIC-IV cardiac ECG-staleness study. Skill chosen from
  four options: **cli-explainer** ("something I built (code)"). Channel chosen:
  **@HumanitariansAI**. Scope chosen: **core 11 beats** over the 13-beat option
  that would have added the equity finding. Later: "we need this in 9:16 and
  16:9."

- **OWNERSHIP DECISION:** built into `mimic-research/youtube/stale-ecg/` per the
  toolkit's standing rule that videos travel with their book, never into the
  toolkit folder. The reel is self-contained; the eight Remotion components it
  needs live in the toolkit's scene library (unavoidable — that is where the
  renderer resolves them).

- **ENVIRONMENT:** machine was bare. Installed `ffmpeg` + `node` (Homebrew),
  then `pango`/`cairo`/`pkg-config` after `manimpango` failed to build. Python
  3.14 was the system default and is too new for the pinned deps — built a 3.12
  venv. Kokoro model (310MB + 27MB voices) downloaded by `./setup --install`.
  Manim never came up: pip resolved an **x86_64** `pycairo` on an arm64 Mac and
  a cached wheel from a failed source build kept reinstating it. Routed around
  it — every visual in this reel is Remotion, so Manim was never on the path.
  **Still broken; not blocking this reel.**

- **TTS constraints, established empirically before writing narration.**
  Synthesised a probe clip and transcribed it back with faster-whisper to hear
  what the voice actually says. Three of four tokens were mangled:
  `MIMIC-IV` → "Mimicroman 4", `AUROC` → "OROC", `0.8574` → "0, 8574".
  `ECG` was safe. All narration therefore spells numbers as words and keeps
  exact figures on screen only. Constraint recorded in `beat_sheet.json`
  metadata so it is not silently reintroduced.

- **GATE L (library-first):** ran `./art scenes` for five beat needs before
  authoring. The library's generic `BarChart` cannot express a confidence
  interval or an underpowered state, and the near hits were all content-specific
  figures for other reels. Recorded as genuine PUNTs → built the components.

- **Plan:** 12 beats in the required cli-explainer spine (11 authored; B08 split
  into B08/B08B when the summary ran long). Audio-first: Kokoro generated and
  measured before any visual. **Locked total 4:18 (258.01s)** — durations in the
  beat sheet are ground truth.

- **Components authored (8, all now in the toolkit's index at 596 renderable):**
  `EcgAverageTrap`, `EcgStalenessBars`, `EcgWithinPatientDecay`,
  `EcgVerdictPanel`, and the portrait set `EcgAverageTrap916`,
  `EcgStalenessBars916`, `ClaudeCodeBeat916`, `OutroSeries916`.
  `ClaudeCodeBeat916` closed a real library gap: the landscape component sizes
  type from `height`, so *any* portrait code beat in this toolkit would have
  silently overflowed its card.

- **Captions:** `align.py` → word-level timing from each beat's mp3
  (12 beats aligned, 0 fallbacks). SRT derived from that plus measured beat
  offsets: 85 cues, last cue ends 04:17.48 against a 04:18.01 video.

- **9:16 derivation:** Shorts cap is 3:00; parent is 4:18. The auto-planner
  proposed dropping **B04 and B07 — both output beats** — because it targets the
  longest middle beats, which in this reel are the payoffs. **Overridden.**
  Applied the cli-explainer rule instead (single cycle, no revision, point to
  the long): dropped B05–B07, B08, B08B. Result **2:34 (154.09s)**, 8/8 slots
  filled. `shorts.py` auto-wrote an outro narration stitched from dropped-beat
  fragments ("also covers a stale ecg is worse than no ecg, Train once on the
  fresh…") — ungrammatical; hand-rewritten and re-voiced.

---

## Corrections made during build

Every one of these passed `ffprobe` and was caught only by looking at frames.

| # | Beat | Defect | Fix |
|---|---|---|---|
| 1 | B08B | Mitigation confidence bounds were **inferred** from a range of point estimates rather than read from source | Replaced with verbatim values from `within_patient.json` |
| 2 | B01 | Bars did not encode value — `+0.0003` drawn the same height as `+0.0053`, so the frame contradicted the data it existed to expose | Bar length now scales with \|value\| |
| 3 | B08 | "IN TRAINING / AT DEPLOYMENT" distributions were **invented shapes** that read as data | Replaced with the real cohort mix (53.9 / 12.1 / 14.1 / 19.9 % of 144,668) and `train_lag = 0` |
| 4 | B10 (short) | Auto-generated outro narration ungrammatical | Hand-written |
| 5 | B07, B04-916 | Label/whisker and label/zero-rule collisions | Right-aligned band labels; cream chip interrupts the rule behind row labels |
| 6 | `description.txt` | Called the decay "stable across 5 of 5 fold seeds" — the **sign** holds in 5/5, but per-seed contrast magnitude runs +0.0061 to +0.0094 against a +0.0092 headline | Rewritten to claim sign replication only. Caught at GATE F by re-reading `seed_summary`, not the write-up |

**Process failure worth recording:** the first re-render attempt passed four
beat IDs to `--only`, which accepts one. The argparse error was swallowed by a
pipe that returned exit 0, so the run reported success while rendering nothing.
Had the exit code been trusted, corrected beats would have shipped uncorrected.
This is exactly the failure the VISUAL QC LAW exists to catch.

---

## Gate status

- [x] **GATE L** — library-first search run before authoring; misses logged to `TEMPLATE-MISSES.md`.
- [x] **Audio lock** — 4:18 (258.01s) 16:9 · 2:34 (154.09s) 9:16. Beat-sheet durations are the clock.
- [x] **PROOF GATE** — `CHECKS-REPORT.md`: 12/12 beats SHOW or justified HOLD, no unresolved PUNTs.
- [x] **Source trace** — `SOURCES.md`: every on-screen number traced to `results/results.json` or `results/within_patient.json`. Corrections logged.
- [x] **GATE F** — `FACTCHECK.md`, re-verified 2026-08-30 against the JSON rather than the write-up. 20 rows: 18 PASS, 2 FIXED, 1 hedged (B07's interpolated zero-crossing, row #15) escalated to human judgement. No narration fixes required → no audio regeneration.
- [x] **VISUAL QC** — `_qc/REPORT.md` + `qc-sheet.png`. All 12 beats frame-inspected; 5 defects found and fixed; contact sheet re-cut after.
- [x] **Data-use check** — aggregates only. No patient-level data, no row-level records, no identifiers. Consistent with the PhysioNet DUA the source repo operates under.
- [ ] **GATE P — narration sign-off: PENDING.** See `NARRATION-GATE-P.md`. Not an agent signature.
- [ ] **Final master** — `./art final` not yet run; current 16:9 is the clean compile, `stale-ecg-slate.mp4` is the earlier review cut.

---

## Known issues, carried forward

1. **`OutroSeries` renders on white** while every other beat sits on the
   humanitarians cream — a visible flash on the final cut of the 16:9. The
   portrait `OutroSeries916` authored here grounds on cream and does not have
   this problem. Backporting means either retinting a shared component (affects
   other reels) or a reel-local variant.
2. **The compiler flags a skin warning** on B10: *"palette=claude but the outro
   is 'OutroSeries' — OUTRO LAW wants ClaudeTitleOutro"*. This is a deliberate
   deviation, not a defect: `ClaudeTitleOutro` and its lock are claude-liam
   only, and this is an HAI-channel reel. Recorded so nobody "fixes" it.
3. **B04 runs 34.3s**, over the doctrine's split ceiling. Kept whole because the
   beat carries one argument; it splits cleanly at the underpowered-bin
   explanation if it drags on review.
4. **Upstream, in the source repo (not mine to change):** `results.json` stores
   `bootstrap_p_no_decay: 0.0`. With 1,000 replicates the correct report is
   `p < 0.001`, which is what `README.md` already says. A one-line fix in the
   JSON writer.
5. **Manim is not functional** on this machine (arm64/x86_64 `pycairo`).
   Irrelevant to this reel; will block any future reel with equation beats.

---

## Human feedback log

**2026-08-29** — Dhruvi Shah, on scope: chose the core 11-beat cut over the
13-beat version, keeping the reel to one finding proven twice. Equity finding
(Medicaid 23.0% vs Private 16.8% stale-ECG exposure) scoped out; it is the
obvious candidate for a second reel.

**2026-08-29** — Dhruvi Shah, on channel: @HumanitariansAI. Consequence applied:
Bella / Pragmatist register and the HAI outro rather than the claude-liam
default of Liam / Teardown / `ClaudeTitleOutro`.

**2026-08-30** — Dhruvi Shah: both aspect ratios required. 9:16 derived per the
Shorts law, with the planner override recorded above.

**2026-08-30** — Dhruvi Shah: requested `BUILD-LOG.md` and
`NARRATION-GATE-P.md`, noting the convention across other fellows' episodes
(adwait-changan, sai-pranavi-j, komal-bg).
