# Can AI Catch Its Own Mistakes? I Ran the Experiment

A **5:22** film at **3840×2160**. It asks a plain question — when a model gets
something wrong and you ask it to check its own work, does it catch the mistake,
or does it just agree with itself? — and then spends most of its runtime on the
part that turned out to matter more: **how you test a claim like that at all.**

This is a **repo-topic** episode. It did not come from my own week's work — it
was built from a topic that already existed in this repository. What that topic
was, what was wrong with it, and everything that was added on top are all set
out below, because that provenance is the point of this lane.

Working title during production was *"The Control You Didn't Run"* — kept in
`beat_sheet.json` under `metadata.working_title`.

---

## Where this came from

**Source topic, already in this repo:**
[`claude-for-artificial-intelligence/nbb-cli-agent-self-verification-failure`](../../../claude-for-artificial-intelligence/nbb-cli-agent-self-verification-failure)

I picked it deliberately: I went through the other fellows' branches first to
find a topic nobody had claimed, and this one was untouched.

That folder is one of **three persona wrappers around a single shared body** —
the siblings are
[`cli-agent-self-verification-failure`](../../../claude-for-artificial-intelligence/cli-agent-self-verification-failure)
and
[`claude-liam-cli-agent-self-verification-failure`](../../../claude-for-artificial-intelligence/claude-liam-cli-agent-self-verification-failure),
and their body beats are byte-identical (10/10 and 10/11). The draft's own
`PEDAGOGY.md` says as much: *"NBB wrapper reuses locked body pedagogy."* So this
is one idea in three costumes, not three topics.

**The draft's central claim, verbatim from its `beat_sheet.json` (B01):**

> "This is not hallucination — it is a structural failure of self-reference. **A
> system cannot reliably audit its own output** when the output and the audit
> share the same underlying mechanism."

That sentence is the film's cold open, quoted on screen with its file path
beneath it.

**This follows the same pattern as the Klarna episode in this folder.** That
film's source draft was built around invented companies (*TechServe*,
*StreamlineOS*) and was replaced with a real, primary-sourced case. Repo topics
are scaffolds. Replacing the scaffold with real research is the job here, not a
departure from it.

## What was wrong with the original

Four defects, all verifiable in the source file:

| # | Defect | Evidence |
|---|---|---|
| 1 | States a **structural impossibility** as settled fact | B01, quoted above |
| 2 | **No measured number anywhere** — asserts the model "frequently" confirms wrong answers, with no tally | zero rate or percentage strings across all narration fields |
| 3 | **The experiment cannot run** — it calls `claude-3-5-haiku-20241022`, retired 19 Feb 2026 | `beat_sheet.json` |
| 4 | **The design cannot support the conclusion** — two arms that both change everything at once | B02–B06 |

Its `PEDAGOGY.md` is four lines and ends `VERDICT: PASS`, with no evidence
discipline and no sourcing.

**Defect 4 is the interesting one, and the film does not mock the draft for it.**
Asking the model to check itself, then checking it in Python, changes *both* the
provenance and the checker. The result comes out identical whether the cause is
self-reference or the puzzle simply being hard. That is a subtle and extremely
common mistake, and naming it is the teach. **No person is named anywhere in
the film.**

## What was built on top of it

| | Original draft | This episode |
|---|---|---|
| Evidence | none | 33 wrong expressions, 99 verdicts, every transcript shipped |
| Model | `claude-3-5-haiku` (retired) | Haiku 4.5 + Sonnet 5, three configurations |
| Design | 2 arms — cannot isolate a cause | 4 arms — isolates provenance |
| Claim | "cannot reliably audit its own output" | "below about nine percent **on this task**," with a stated bound |
| Teaches | a conclusion | a reusable method |

**1. Built the missing arm.** The same wrong expression is shown to the model
twice — once inside its own conversation, where it looks like its own work, and
once in a fresh conversation as a stranger's submission. Character-for-character
identical; only the apparent owner changes. That arm is what separates
"self-reference" from "hard puzzle," and it is what the draft had no way to do.

**2. Ran it, and reported what came back.** Zero misses out of 33. Gap 0.0 in
all three configurations. **The blind spot did not reproduce** — which is not
the result I went looking for.

**3. Kept the draft's advice while correcting its reason.** The draft says two
things that sound like one thing. *"Add an external verifier"* survives intact.
*"A system cannot audit itself"* is contradicted — it did, 33 times out of 33.
The reason to keep the external check is **not** that the model structurally
cannot self-audit; it is that **you don't know the rate for your task until you
measure it, and measuring requires the check anyway.** The external verifier is
the instrument, not the safety net. Both sentences are on screen together, one
intact and one struck through, both verbatim with their source paths.

**4. Showed my own failed attempt.** Revision 1 added the missing arm — and then
the models were accurate enough that the key configuration produced **zero**
wrong answers and therefore no data at all. A control that never fires is not a
control. That failure is in the film, with its `n = 0` table on screen, because
it is the reason the framework has a fourth question.
`experiment/results-20260811T065935Z.json` is that run, shipped here as
evidence.

**5. Grounded it in the published literature, with peer-review status stated on
screen.** The draft cites nothing. This episode cites two papers and labels the
one that is a preprint as a preprint, on the frame.

## The method the film hands over

Any claim of the form *"it fails **because** of X"* has to survive four
questions:

1. **What is the claimed cause?**
2. **What rival explanation produces the same observation?**
3. **Is there a test where *only* that cause changes?**
4. **Will that test actually collect data?**

The film applies the instrument three times — to the source draft, to my own
revision 1, and to revision 2 — and each fails at a different question. The
draft fails 2 and 3; revision 1 passes 1–3 and fails 4; revision 2 passes.

That uneven mapping is deliberate evidence: a framework reverse-engineered to
fit its examples produces a clean one-failure-per-case diagonal. This one does
not have one.

## Files

- **`can-ai-catch-its-own-mistakes.mp4`** — the final cut, uploaded separately
  through the web UI (see the note at the bottom). Every beat holds on its
  finished frame for a full second before a hard cut, giving the viewer time to
  read it. No crossfades.
- **`EXPERIMENT.md`** — the primary source. Method, results, statistics, and the
  limits of the null. Every figure on screen traces here.
- **`experiment/`** — the runnable harness and **both** result sets, loose and
  browsable rather than zipped:
  - `verify_bench.py` — the measurement instrument. Exact rational arithmetic
    (`fractions.Fraction`), AST-whitelist evaluation instead of `eval()`, and a
    deterministic `--dry-run` mode that needs no API key.
  - `results-20260812T014950Z.json` — the run the film reports.
  - `results-20260811T065935Z.json` — **revision 1**, the run that failed. Kept
    because the film shows it.
  - `README.md` — how to run it.
- **`beat_sheet.json`** — the complete build: narration, measured audio
  durations, and every Remotion component and prop.
- **`FACTCHECK.md`** — claim-by-claim audit: verdict, evidence, source, and
  every correction applied.
- **`PEDAGOGY.md`** — thesis, framework, falsifiability case, act structure, the
  PROOF rubric score, and the GATE P sign-off.
- **`QC-REPORT.md`** — the full build log: every defect found by looking at
  frames, the PROOF checkpoint that caught two gate violations before the beat
  sheet, the author review that sent the finished cut back for two more, and the
  gate verification on the shipped master.

## Sourcing

Three classes of source, treated differently on screen:

- **Verbatim from the draft** — quoted with its `beat_sheet.json` path visible.
- **Published literature** — cited on screen **with peer-review status stated**.
  [Huang et al., ICLR 2024](https://arxiv.org/abs/2310.01798) is peer-reviewed;
  [Tsui, arXiv:2507.02778](https://arxiv.org/abs/2507.02778) is labelled
  `preprint` on the frame.
- **My own measurement** — cited to the results JSON, which ships here.

The film never claims self-verification is reliable in general, never claims
Tsui is refuted, and **names no person**.

## Reproducing the experiment

```bash
cd experiment
python3 -m venv .venv && .venv/bin/pip install anthropic
python3 verify_bench.py --dry-run     # no key, no spend — inspect the pipeline
```

Then supply your own `ANTHROPIC_API_KEY` and run it for real — about 144 short
calls, well under a dollar. `--dry-run` output is labelled **NOT evidence**
everywhere it appears, because canned responses cannot support a finding.

Every prompt, reply, verdict and grade is in the results JSON. The summary is
derived from it and can be recomputed independently.

## Production notes

**Voice: Kokoro `am_onyx` ("Onyx"), warm first-person register.** This is a
documented departure from this series' standing `af_bella` choice and from the
toolkit's Onyx/Teardown pairing — see the Voice section of
[the fellow README](../README.md).

**Lane:** repo-topic, the same lane as the Klarna episode. Work-derived episodes
(CommBank, Lemonade) carry a different register and act structure and are not
mixed with these.

Built with the [Brutalist](https://github.com/nikbearbrown/brutalist.art) free,
local video toolkit (Kokoro TTS + Remotion) — no paid APIs, no keys.

---

**Note on the video file.** This repo's `.gitignore` excludes `*.mp4`, so `git
add` silently skips it — the cut is uploaded through the GitHub web UI instead.
Check with `git check-ignore -v <file>.mp4` before assuming anything was staged.
Never run a broad `git add .` here, and confirm the branch first: this is a
shared repo.
