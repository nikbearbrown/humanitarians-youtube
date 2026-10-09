# Uday S.

**Role:** Developer  
**Project:** _to be filled in_  
**GitHub:** [@Udaydsmls](https://github.com/Udaydsmls)

Weekly work reports and AI explainers for the `@HumanitariansAI` channel, built
on the Brutalist audio-first chassis.

## Voice choice

**Voice:** Onyx (`am_onyx`)
**Register:** Pragmatist — method first, then when it applies and when it does not.
**Channel chip / handle on cut:** `@HumanitariansAI`

`am_onyx` was selected by the fellow and is recorded in every episode
`beat_sheet.json`. It is kept across this series; a change would be an explicit,
documented re-voice decision, not a per-episode default.

Note for the weekly-fixtures cut: `am_onyx` replaced an earlier `af_bella` pass
at the fellow's request. Because the toolkit is audio-first, that re-voice
re-timed the whole reel and every Manim scene was re-authored to the new
measured clock — see that episode's `BUILD-LOG.md`, "REVISION 2".

## Reports in this folder

- [2026-08-27 — Build the Defects First](./2026-08-27-weekly-fixtures-before-validators/) —
  weekly work report on `mycroft` @ `9ef4e7f`: building a defect corpus (3 clean
  fixtures, 18 catalogued defects) before writing any validator, then revising
  step 1 to verify provenance. 13 beats · ~3:02 · plus a 9:16 Short (~1:27).
- [2026-08-27 — State Space Models and Mamba](./2026-08-27-state-space-models-and-mamba/) —
  AI explainer on the `claude-hai` channel key: a STATE / UPDATE / COST rubric,
  applied to RNNs and Transformers, then SSM → S4 → Mamba, then the copying
  ceiling the rubric predicts. 12 beats · ~3:35 · plus a 9:16 Short (~1:48).
- [2026-09-03 — Transport, Do Not Repair](./2026-09-03-mycroft-weekly-transport-do-not-repair/) —
  weekly work report on `mycroft` @ `bdc1bc1`, **episode 2**: three questions for
  any pipeline stage (DECIDES / REFUSES / EVIDENCE), both steps scored on them,
  and the CRLF bug that breaks axis 3. 13 beats · ~3:22.
- [2026-09-03 — The Brand That Didn't Exist](./2026-09-03-generative-engine-optimization/) —
  topic explainer on Generative Engine Optimization: three levers (PARAMETRIC /
  PRESENCE / QUALITY), each measured, then a brand that does not exist reaching
  90% mention rate. 11 beats · ~3:04.
- [2026-09-10 — Both Sets Scored 64](./2026-09-10-mycroft-weekly-both-sets-scored-64/) —
  weekly work report on `mycroft` @ `253ee74`, **episode 3**: three questions to
  ask of any number a pipeline emits, and a corrupted fixture set that reports
  the same headline score as the clean one. 13 beats · ~3:34.
- [2026-09-10 — The Gap You Can Actually Close](./2026-09-10-zero-day-vulnerability/) —
  topic explainer on zero-day vulnerabilities, **defensive/educational only**:
  three clocks (ATTACKER / VENDOR / DEFENDER), and the argument that most
  defenders guard the smallest of the three gaps. 10 beats · ~2:51.
- [2026-09-17 — It Never Says Pass](./2026-09-17-mycroft-weekly-it-never-says-pass/) —
  weekly work report on `mycroft` @ `aa0c0fe`, **episode 4, the finale**: three
  questions for any automated report, and a gate that is satisfiable by doing
  nothing. Six of six steps written. 13 beats · ~3:33 · **4K**.
- [2026-09-18 — The Constraint Isn't Speed](./2026-09-18-6g-and-iot/) —
  topic explainer on 6G and IoT: three constraints (POWER / COVERAGE / COST PER
  NODE), speed on none of them, and a vendor's own forecast that 40% of 2030 IoT
  connections still won't use 6G. 11 beats · ~3:51 · **4K**.
- [2026-09-25 — Passing For The Wrong Reason](./2026-09-25-mycroft-weekly-passing-for-the-wrong-reason/) —
  weekly work report on `mycroft` @ `4157a8e`, **episode 5**: three questions for
  any automated check, and two gates that were passing because a TODO marker was
  still there. 13 beats · ~3:10.
- [2026-09-25 — The Arrow Points The Other Way](./2026-09-25-quantum-ai/) —
  topic explainer on quantum AI: the demonstrated wins run the other way — machine
  learning improving quantum error correction, not qubits speeding up pattern
  finding. 11 beats · ~3:49.
- [2026-10-02 — The Status Is A Claim](./2026-10-02-mycroft-weekly-the-status-is-a-claim/) —
  weekly work report on `mycroft` @ `8c13b87`, **episode 6**: three questions for
  any status field, and what it costs to write down the evidence behind one.
  12 beats · ~3:15.
- [2026-10-02 — Levels, Not Layers](./2026-10-02-hope-nested-learning/) —
  topic explainer on HOPE and nested learning. The brief called it a training
  method; it is an architecture, and the video corrects that on screen.
  11 beats · ~3:27.
- [2026-10-09 — Green Because It Wasn't Looking](./2026-10-09-mycroft-weekly-green-because-it-wasnt-looking/) —
  weekly work report on `mycroft` @ `fbd30b6`, **episode 7**: a conformance check
  that was passing because of what it never opened — 187 files before, 743 after.
  12 beats · ~3:38.
- [2026-10-09 — One Model, Three Numbers](./2026-10-09-small-models-coding-rl/) —
  topic explainer on small models, coding agents and RL: one model posts four
  different scores on the same benchmark, and which one gets quoted decides
  whether it looks state of the art. 11 beats · ~3:31.

The two 2026-08-27 folders carry a `short/` subfolder: a derivative 1080×1920 cut
for YouTube Shorts, reusing the parent's audio with only the funnel outro
regenerated. Both Shorts pass GATE V with **BLOCKER 0**. Everything from
2026-09-03 on is landscape only so far.

**Masters went 4K from 2026-09-17.** The first six reels shipped 1080p cuts from
4K sources; the two newest are true 3840×2160, recompiled by `./art final` from
the same slots with no beat re-rendered. The earlier six can be upgraded the
same way whenever it is wanted.

**Series continuity:** the Mycroft weekly is a running series, and each episode
picks up the previous ledger — ep 1 opens on six steps marked `[TODO: DEV]` and
closes on "gate 2 cannot clear"; ep 2 resolves two rows of that list; ep 3's
falsifiability beat lands back on ep 1's frozen corpus; ep 4 closes the ledger
at six of six steps and finds the same ep-1 defect one level up (a gate with
nothing to fail). Watch them in order:
`9ef4e7f` → `bdc1bc1` → `253ee74` → `aa0c0fe` → `4157a8e` → `8c13b87` → `fbd30b6`.

**Dual-use note:** *The Gap You Can Actually Close* is a security topic handled
defensively. It explains what the term names, reports published statistics, and
argues where defensive effort pays off — no exploitation technique, no
vulnerability-research method, no unpatched flaw named. GTIG's per-vendor
targeting breakdown was available and deliberately cut.

**One exception to the voice/name convention:** *The Brand That Didn't Exist* is
a topic explainer, not a work report, and per the author's instruction it carries
**no personal names anywhere** — its intro speaks none. Every other reel here
opens with "I'm Uday S.".

## Rendered videos

The rendered cuts are in Google Drive, not in this repo:

<https://drive.google.com/drive/folders/1T7zrj41hh10qB0qOU1LD3qJF6VL0qV0K>

Review copies only. That folder held the two 2026-08-27 reels and their Shorts
when it was linked; the 2026-09-03 masters may still need uploading.

## Publishing

No package here is authorized for publication. Masters and all audio/video
assets stay out of git; only the beat sheets, scene source, and review paperwork
are tracked here. The Drive folder above is a review location, not a release.

## Frictional log

Every work subfolder here carries its own `FRICTIONAL.md` — a dated record of the process
behind that specific piece of work, kept beside the evidence it describes: what was tried
and expected, where it resisted and what was done next, what Claude or another person
contributed and what was accepted, changed or rejected, and what is now understood or
still open. Append as you go; never rewrite an earlier entry. It is not graded and not a
performance review. See <https://www.humanitarians.ai/fellows> for what an entry contains.

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# Uday S.

This folder organizes video projects built around beat sheets. Each project
README explains the subject and documents the free local rebuild workflow.

## Rebuild toolkit

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

<!-- END BRUTALIST REBUILD GUIDE -->
