# BUILD-PROMPT — stale-ecg

The prompt that would rebuild this reel from scratch, and the record of what the
build actually decided. Ships beside the beat sheet, as every reel does.

## The prompt

> `cli-explainer` the mimic-research repo — the ECG staleness finding.
> Channel `@HumanitariansAI`, Kokoro `af_bella`, Pragmatist register.
> Required spine, one revision cycle minimum. The revision is real and already in
> the repo: the binned analysis is confounded by case mix, and `within_patient.py`
> is the fix — use that as the CHANGE beat rather than inventing one.
> CODE beats show verbatim source from `analyze.py` and `within_patient.py`.
> Every number traces to `results/*.json`. MIMIC is credentialed: aggregate
> results only, no patient-level anything.
> Rebuild `fig2` and `fig6` as native animation — never screenshot them.

## Why this project fits the format

`cli-explainer` demands a check-and-change cycle, and most projects have to
manufacture one. This repo already contains three real ones, documented in its
own README: the removed grace window (154,012 → 145,613 links), the dropped
implausible gaps (20–80 year artifacts that would have *flattered* the
hypothesis), and the `"st "` substring bug that fired the ST-change flag on
~24,000 conduction blocks. The reel uses the largest of them — the case-mix
confound — as its B05 revision.

## Decisions taken during the build

**Register.** The reel was specified as `cli-explainer`, whose default is the
Teardown register on `@NikBearBrown` with Liam (`am_onyx`). The channel was set
to `@HumanitariansAI`, which is Bella's channel and the Pragmatist register —
*method, when to use it, when not to*. Pragmatist was chosen as the better fit
for a methods result, and the outro is the standard HAI card rather than
`ClaudeTitleOutro` (whose lock in `OUTRO-LOCK.md` is claude-liam only). Swapping
back to Liam is one metadata line plus a regenerate; the durations would shift
and the reel would recompile against the new clock.

**B08 split.** Authored as one 42.2 s SUMMARY beat. The measured audio put it
well past the split ceiling in `duration-planner` (~2–3× the 6–10 s mechanism
floor), and it was carrying two ideas — the mechanism, and the failed remedies.
Split into B08 (mechanism) and B08B (unresolved fix), 24.8 s and 22.9 s. This is
the audio-first loop doing its job: the clock exposed the problem, not taste.

**Four new components.** GATE L found no reusable hit for a signed chart with
intervals crossing zero. `BarChart` was a lead and was rejected on inspection —
it grows unsigned bars from a bottom baseline with no interval marks and no way
to mark a bin underpowered. Four PUNTs became four design cards, now in the
index at 592 renderable.

**Endpoint-only annotation on B07.** The three stale points sit within ~5% of
plot width of each other on a log axis; labelling all four collided. Only the
two endpoints whose intervals exclude zero are annotated — the same editorial
choice `fig6_within_patient.png` already makes.

## Defects caught by the frame-level QC pass

Frames were extracted and *looked at*, per the VISUAL QC LAW. The mp4 probe
passed on every one of these:

1. **B01 bar heights did not encode value.** Every bar was drawn at a constant
   height, so the +0.0003 bin rendered as tall as the +0.0053 bin. The frame
   misrepresented the mixture it exists to expose. Fixed to scale by |value|;
   the near-zero bin now correctly reads as a sliver.
2. **B07 header collisions.** The two-line title overlapped the cohort line, and
   the y-axis caption ran through the `+0.0056` value label. Fixed with fixed
   header baselines, a shorter title, and 1.35 whisker headroom.
3. **B07 value-label pileup.** Fixed by annotating endpoints only.
4. **B08B intervals carried no numbers** — "CI crosses 0" alone asks the viewer
   to take the claim on trust. Both contrasts now print with their bounds.

A fifth was caught before render and is logged in `SOURCES.md`: the mitigation
panel's confidence bounds were initially inferred from a range of point
estimates rather than read from `within_patient.json`.

## Rebuild

```bash
python3 runtime/scripts/generate_audio_kokoro.py <reel>     # the clock
python3 runtime/scripts/remotion_scenes.py <reel>           # the beats
./art run <reel>                                            # review cut
./art final <reel>                                          # clean master
```

Never published from here. The master stays in this folder.
