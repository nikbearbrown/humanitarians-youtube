# BUILD-LOG — Transport, Do Not Repair

Skill: `cli-explainer` spine, weekly work-report application.
Channel: `claude-hai` (@HumanitariansAI, Kokoro `am_onyx`, Pragmatist).
Subject: mycroft @ `bdc1bc1`, 2026-09-03. Episode 2 of the Mycroft weekly.

## Where the episode came from

The commit message describes *what changed*. The strongest material was what it
did not summarise: the ingest script's own load-bearing rule.

> An ingest script that cleans data destroys the evidence that cleaning was needed.

That line gave the episode its title, its thesis, and axis 2 of the framework.
The lesson for next week is in PROMPTS.md: **ask what the code refuses to do**,
not only what it does.

## Continuity

Deliberately built as a sequel. Last episode's ledger closed on "run-envelope
absent · gate 2 cannot clear"; B01 opens on that same list and resolves two rows
of it. The ledger is the series' through-line, so B10 restates it in the same
shape. Anyone watching both sees a project move, not two disconnected reports.

## PROOF compliance

| Criterion | This cut |
|---|---|
| Explicit framework | B02 — DECIDES / REFUSES / EVIDENCE, shown as a structure at **20.16s**, ahead of the first example at 47.10s |
| Reusable rubric | The three questions apply to any pipeline stage; B11 turns them on the viewer's own code |
| Worked example | Both steps scored on the same axes (B05, B08) — opposite jobs, one rubric |
| Falsifiability | B09 — axis 3 broken in practice, and the framework predicts it: evidence that moves with the platform is not evidence |
| Active task | B11 — copyable prompt + GOOD/BAD discriminator |
| Friction | Weakest again (see PROOF-REVIEW.md) — a work report mostly delivers |

## Honesty correction made during the build

The first draft of B09 put **invented hash prefixes** on screen as stand-ins for
"two different digests". That is an invented figure, which the REBUILD LAW
forbids outright. It was replaced with real ones: the actual file's bytes hashed
under each line ending —

```
sample/clean/news-finnhub.json
  LF    3,180 bytes   sha256 441291ec…
  CRLF  3,261 bytes   sha256 42fdf8fc…
```

— which is both honest and a better beat, because a viewer can reproduce it.
Recorded here rather than quietly fixed.

Also corrected: the commit message says step 3 catches "3 parse errors". That is
a rollup — the manifest's own taxonomy for those three is 2 `malformed_row` plus
1 `unparseable_file`. The script's `parse_errors` field does return 3, so the
on-screen label is the script's term and correct; the narration avoids restating
it as a manifest class. Logged in FACTCHECK.md row 11.

## Gate record

```
GATE L   library-first searched before authoring; no reusable hit; six beats
         authored as Manim data animations, none slated
GATE F   paperwork set written before render
GATE A   static pre-flight — one fix: B05 was pure typography with no shape to
         change. Given the geometry its content implies (bordered scorecard
         cells drawn per row) rather than suppressed
GATE W   clean on all six, first pass
GATE B   pixel-true — 0 errors, 0 warnings, FIRST PASS. The layout helpers
         carried over from the previous two reels (kicker buff 0.72, content-
         adaptive box widths, fit_src() reserving the citation strip, never a
         line drawn through text) cost three re-renders to learn and zero here
GATE V   clean cut: 404 frames, BLOCKER 0, MAJOR 39 (35 underfill · 4 low-contrast)
```

`./art run` prints "26 BLOCKER" because GATE V reads `*-slate.mp4`, the review
cut, whose timecode burn-in sits outside title-safe by construction. Against the
clean cut there are none.

Underfill is 8.7% of sampled frames, down from 14% on the previous episode —
build-in ramps plus the sparse outro card. The 4 low-contrast flags all co-occur
with 10–11% fill readings: near-blank frames at beat openings with too little
ink to measure a luminance separation, not content that is hard to read.
Accepted and documented, not silenced with `ART_STRICT=0`.

## Deliverable

```
TransportDoNotRepair_UdaySonawane_2026-09-03.mp4   1920x1080   202.16s (3:22)
```

4K master needs no re-render (Manim at 2160p24, Remotion at `--scale=2`):
`./art final <reel>` builds it from the same slots. Nothing here publishes.
