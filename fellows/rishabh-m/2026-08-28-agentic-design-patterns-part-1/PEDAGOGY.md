# PEDAGOGY — The Prompt Is Not The System (Part 1)

GATE P: narration reviewed before audio. Deliberately lean — act structure and
beat classification live in `CHECKS-REPORT.md`, evidence in `FACTCHECK.md`. This
file carries the judgment neither of those asks for: **what difficulty was kept
because it IS the lesson, and what was cut as extraneous.**

## Act structure — checked, detail in CHECKS-REPORT.md

Cold open with RESULT lines (ASK→RESULT at B00) ✓ · hesitant-writer BLUF at B01 ✓ ·
framework before examples (B02 before B03–B08) ✓ · worked example (B09) ✓ ·
falsifiability (B10) ✓ · verdict (B11) ✓ · handoff read aloud and discussed (B12) ✓ ·
title-restate outro (B13) ✓.

ILLUSTRATE LAW: the Claude UI appears at B00, B11, B12, B13 only. B02–B10 are
concept illustrations. No two consecutive beats share a visual scheme — the six
pattern beats differ by topology (chain, fan, split-merge, loop, gated chain,
graph), which is the thing being taught, not decoration.

## Friction protected

**KEPT — the cost line on every pattern beat.** Each diagram carries a `note`
naming what the pattern costs: the 3–5 step ceiling, the single point of
failure, the rate limiter, the uncapped loop, the security surface, the
debuggability. This is the friction. A version that only showed what each
pattern *does* would be easier to watch and would teach the wrong thing — that
these are free upgrades. They are trades, and the trade is the lesson.

**KEPT — B10, which argues against the reel's own thesis.** After nine beats of
"here are the patterns," the reel says: if the task is one step, or the output
must be deterministic, or a user is waiting, use a single call. This is
uncomfortable placement and it is the point. A viewer who leaves believing every
pipeline needs six patterns has been mis-taught. The source never makes this
argument; we added it.

**KEPT — the honest verb in B04.** "Models are overconfident" rather than the
softer "confidence scores can be unreliable." The blunt phrasing is what makes
the guardrail feel necessary.

**CUT — the source's interview Q&A blocks.** The source is interview-prep and
each pattern ends with a scripted question and a long model answer. Reciting
those on screen is a podcast: the voice would carry evidence the viewer cannot
see, which is the exact failure SHOW-DON'T-TELL LAW names. The *content* of the
answers survives where it earned a visual — read-only replicas and human
approval became the accent nodes in B07 and B09 — but the Q&A form is gone.

**CUT — the bracketed citation markers** (`[3, 6]`). They index a bibliography
not present in the source. Showing citation marks that resolve to nothing is
worse than showing none.

**CUT — arithmetic beyond the claim.** The source discusses token-cost
multiplication in reflection loops. B06 says "every cycle is another two calls"
and stops. The exact cost model varies per provider and would date the video.

## Register

HAI Plain, as specified: method, when to use it, when NOT to. Checked against
the audience — students and practitioners moving from single prompts to
production systems. No jargon the reel has not earned: "idempotent",
"cross-encoder", "DAG" all avoided or replaced with plain phrasing ("a graph,
not a line").

VERDICT: PASS
