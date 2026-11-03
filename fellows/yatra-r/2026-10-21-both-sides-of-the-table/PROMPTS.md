# PROMPTS — `yatra-both-sides-of-the-table`

## Open slots

**None.** Every beat is machine-rendered from `beat_sheet.json`. Free path only
(Kokoro + Remotion + ffmpeg).

One deliberate non-slot, which is a refusal rather than a gap: **B09 does not show a
working prompt injection.** `TblInject` renders generic resume headings and a hidden layer
labelled *"written for the screening AI, not for a reader"*. Showing real injected text
would be supplying a technique, not illustrating a statistic. There is no prop that could
carry one.

---

## The prompts that appear on screen

### B00 — the cold-open ask

```
Hiring has become AI on both sides — companies screening with it, candidates
using it to get past the screening. Walk me through what each side is actually
doing and whether anyone trusts the outcome. Cite every figure on screen and
add none of your own.
```

Result lines beneath it (COLD OPEN LAW — the ask lands answered):

```
the employers: 86% of organizations now use AI somewhere in hiring
the candidates: 4 in 5 job seekers use AI in their search
the result: only 26% of applicants trust AI to evaluate them fairly
```

Greeting: `Sawadee, Bella` · folder chip: `@Yatra` · running: `reading both sides…`

### B04 — the generation ask (ASK→RESULT LAW; B05 is the result)

```
Draw a hiring table with four seats: the company and its screening AI on one
side, the candidate and their AI on the other. Show the two AIs exchanging with
each other while both humans wait. No numbers — the arrangement is the point.
```

Greeting: `The ask,` · running: `drawing the table…` · no output lines — the next beat IS
the output. "No numbers — the arrangement is the point" is literal: `TblTable` has no
numeric prop.

### B12 — the handoff (HANDOFF LAW: read aloud verbatim, then discussed)

```
Here is our hiring process, step by step. Tell me which steps a machine is
doing, which a human is doing, and at which exact step a person first reads a
candidate's name. Then tell me what a rejected candidate would be told about
that.
```

Rubric shown beneath, and spoken:

```
grade it: can it name the step a human first reads your name?
grade it: does it separate screening from deciding?
grade it: could you tell a rejected candidate the truth?
```

**Why this prompt:** every figure in this episode is about a process nobody can see from
the outside, so the useful question is not "is AI good at hiring" but "where, exactly, in
*our* process does a person enter". The third rubric line is the honest one — if the
answer to a rejected candidate would be embarrassing to give, that is the finding.

---

## Rebuilding

```bash
./art run   /Users/yatrarawat/Downloads/brutalist-reels/youtube/yatra-both-sides-of-the-table
./art final /Users/yatrarawat/Downloads/brutalist-reels/youtube/yatra-both-sides-of-the-table
```

Scene source: `runtime/remotion/src/scenes/TableSides.tsx` and `TableSides916.tsx`,
registered in `Root.tsx`. `TblSide` backs two beats and is registered at the **shorter**
of the two — see `SHOTLIST.md` for why.
