# Chapter 8 — Silent Mode

## Overview

Everything so far has been interactive. You segment, you listen, you pick the keeper reference, you approve a clip. That works beautifully for one film. It falls apart at 150 books. A hundred and fifty books at roughly twelve chapters each is about 1,800 videos — call it 300 hours of finished footage. Even at double speed, that is 150 hours of watching, a month of full-time work just to *review* rough drafts you have not yet touched. Silent mode is the answer, but only if you understand what it is actually for.

The temptation is to think silent mode is about removing the human — pressing go and coming back to 1,800 finished videos. It is not. Rendering is the cheap part; the cluster does that in its sleep. The scarce resource is your attention. So silent mode's real product is not the videos at all — it is the **triage layer** that tells you which of the 1,800 to open first. Each chapter gets a QC score from 0 to 100, a `decision_log.json` recording every choice the machine made and why, a contact sheet, a sixty-second preview, and a slot in a fleet manifest ranked worst-first. You watch full renders only where the machine flags trouble or the book matters most. A warehouse of rough drafts with no index is a warehouse you will never open.

The second thing to unlearn is that "silent" means "gate-free." Every gate from the earlier chapters existed for a reason — it sat at the cheapest point to fix a mistake. Silent mode does not delete those gates; it *defers* them. Each former human gate becomes one of two things: an **auto-policy** that decides and logs its justification, or an **agent slot** that an LLM fills. The plan gate auto-builds a starter and hands it off; the narration gate auto-extracts beats and hands them off; the render becomes an automated QC audit on the finished MP4. Your review then happens asynchronously against the decision log — surgical edits, not from-scratch builds. Gate-deferred, not gate-free.

This works because of the master-clock law from Chapter 3. Timing is *derived* from measured audio, never authored. So anything silent mode gets wrong is a swap, not a rebuild: replace a beat's narration, and captions, holds, and frame counts all re-derive themselves. That single property is what makes a rough draft safe to generate unattended — the human's later fix mechanically re-times everything downstream.

## The bottleneck is attention, not rendering

Sit with the arithmetic, because it dictates the whole design. Rendering 1,800 chapters is embarrassingly parallel — one Slurm array task per chapter, and a cluster chews through it. What does *not* parallelize is you. If the only output were 300 hours of video, you would have built a bottleneck, not a pipeline.

So silent mode inverts the deliverable. The MP4 is a byproduct; the review surfaces are the point. Triage in order of cost: the contact sheet and decision log first (seconds), the sixty-second preview second (a minute), the full rough render only for flagged or flagship chapters. Rank by QC score ascending and by book importance, and accept honestly that the long tail ships as rough-plus-spot-fixes. A volunteer — one of 150 — opens a chapter folder that already has a deck, figures, draft narration, a scaffolded Remotion project, and a score, and does only the human-only work: watch, note, fix the flagged beats, approve. They start from a watchable draft, not a blank page.

## Every gate becomes a policy or a slot

Walk `silent_run.py` and you can see each old gate turn into new machinery. Setup, assets, deck, script, audio, captions, visuals, scaffold, and QC are all deterministic — the script runs them directly and writes a line to `decision_log.json` for each: which runtime it copied, how many candidate figures it imported, whether the deck verified, how many beats the script guard flagged as reciting the slide, which pronunciations it applied, which render tier the media router chose per beat. None of these needs a human in the loop; they need a *record*, and they get one.

Only two gates are irreducibly the work of a language model, and silent mode is honest about not faking them. The **plan** stage builds a `deck_plan.starter.json` skeleton and then stops: authoring headlines that make a claim, writing speaker-notes that teach, binding figures to real asset ids — that is judgement a regex cannot do. The **extract** stage turns the deck into a `beat_sheet.json` of empty beats and stops again: writing narration that discusses the slide instead of reading it is the other genuine LLM job. At each, the orchestrator emits a work-packet and halts cleanly.

There is one more subtlety worth internalizing: an agent may *fill* these slots, but it may not *sign off* on them. Each gate writes a `.verified.json` sidecar — the same AI+1 verified-artifact pattern the book uses at its root. An agent can stub a sidecar (`verified: false`); only a human runs `verify.py sign`. So even in a fully automated fleet, the two decisions that most determine quality — the plan and the narration — carry a human signature before any audio money is spent. `STATUS.md` in each folder shows the two-row gate table at a glance.

## Three modes, identical bookkeeping

The clever move is that the *same* two slots can be filled three different ways, and the deterministic bookkeeping does not change one bit. The `--mode` flag chooses only *who runs the LLM*:

- **`agent`** — an agent process (interactive Fable, or headless Claude Code on the cluster) reads the packet and writes the plan or narration directly. Best for flagship chapters and for setting the quality bar during a pilot.
- **`api`** — the packet becomes a Claude Batch API request under `packets/*.request.json`; results write back programmatically. This is the fleet default: cost-bounded, scalable, no babysitting.
- **`handoff`** — the packet becomes a `.prompt.md` you paste into any LLM, saving its reply for a re-run. The lowest-tech fallback, and fully ✅ — no key required to *route* the work.

Whichever you pick, `decision_log.json`, the sidecars, `STATUS.md`, and the QC report come out identically. The pilot's whole job is to run `agent` mode by hand until you trust the quality bar, then wire `api` mode to hit it at scale. ✅ Note too that the render half — TTS, forced alignment with faster-whisper, Remotion — is free and local; the pipeline needs *zero* image-generation services for lectures. You can drive the entire draft pass on your own hardware, or on open models on a cluster, at near-zero marginal cost.

## From one chapter to the fleet

`silent_run.py` is the atom: one chapter in, one rough lecture folder out. `batch_run.py` is the fleet layer — it walks `books/*/chapters/*.md`, calls the orchestrator per chapter (skipping obvious front and back matter), and rolls every `qc_report.json` and `decision_log.json` into a single `fleet_manifest.json`, sorted worst-first: blocked and unscored chapters float to the top, then ascending QC score. That manifest, not the video pile, is your dashboard. Locally it is a simple loop; on the cluster each `(book, chapter)` is one array task, and the manifest is the same either way.

## Worked example

Take the skepticism book's Chapter 2 — argument-dense, full of `$$…$$` derivation blocks. Run one chapter in agent mode:

`python scripts/silent_run.py books/computational-skepticism-for-ai --chapter 02 --mode agent`

Setup makes the folder and copies the runtime; assets imports 20 candidate figures into the pool. The plan stage builds a starter — and here the pilot earned its keep: the starter emitted **72 slides**, because `build_plan.py` makes one equation slide per `$$` block and the multiplication-rule section alone has ten derivation steps. Seventy-two slides is not a lecture, it is a wall. That is exactly the lesson a pilot exists to surface cheaply — on two books, not 150 — and it becomes a new auto-policy: consolidate consecutive equations within a section, cap slides-per-section. Re-run, and you get a sane ~35.

The orchestrator then halts cleanly at Agent Slot 1 with a packet under `packets/01-author-plan.md` and a stubbed sidecar on the starter. Fable authors `deck_plan.json`; a human signs it; you resume with `--from deck`. The deck emits and verifies, extract produces the beat sheet, and it halts again at Agent Slot 2 for narration. Fill it, sign it, resume. On your Mac — where ElevenLabs, node, and faster-whisper live — run `--only audio captions scaffold qc`: audio locks the master clock, captions align, Remotion scaffolds, and QC scores the result. The manifest now has one real row instead of a blocked one.

## Exercises

**Exercise 8.1 — Run one chapter and read the trail.** Run `silent_run.py` on a single chapter in `handoff` mode until it halts. Open `decision_log.json` and `STATUS.md`, and in three sentences describe where it stopped, what auto-decisions it logged before stopping, and which gate is awaiting a human signature. (Artifact: your three-sentence summary plus the `decision_log.json`.)

**Exercise 8.2 — Score and triage.** Complete one chapter through the `qc` stage and record its 0–100 score and verdict. Then explain which single check, if it flipped from fail to pass, would move the chapter across the 70-point "watchable-draft" threshold — and whether that check is an auto-policy or a signed gate. (Artifact: the `qc_report.json` plus your one-paragraph triage note.)

**Exercise 8.3 — Design the missing auto-policy.** The pilot found the 72-slide equation blow-up. Pick one other decision in `decision_log.json` you would *not* want a machine making silently across 1,800 chapters, and write the auto-policy that should replace it: the rule, what it logs, and the failure it prevents. (Artifact: a short policy spec — rule, log line, prevented failure.)
