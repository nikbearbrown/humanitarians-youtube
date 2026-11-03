# PROMPTS — The Judgment Is the Job.

Every prompt this reel shows on screen, verbatim. Part of the GATE F paperwork set
(`FACTCHECK.md` · `SHOTLIST.md` · `PROMPTS.md`).

All three composer beats show prompts a viewer could genuinely paste into Claude. None is
a mock-up written to look good on camera.

---

## B00 — cold open (ASK, on screen)

**Greeting:** `Namaste, Liam` · **runningText:** `separating execution from judgment…`

> I run creative for a mid-size brand. AI now drafts our ad copy, taglines and social
> posts, and generates visual concepts too. Be blunt: which parts of my copywriters' and
> designers' jobs has this actually replaced, which parts has it left untouched, and what
> should I stop paying people to do?

**Result lines (the ask lands answered — COLD OPEN LAW):**

1. `replaced: producing options — copy, variants, concepts`
2. `untouched: deciding which one is right, and owning it`
3. `the job moved from making to judging`

The prompt is deliberately blunt ("what should I stop paying people to do") because the
reel's answer is *not* the comfortable one the phrasing invites. Setting up a question the
body then complicates is the Teardown move.

---

## B03 — the ask micro-beat of the one ASK→RESULT pair (on screen)

**Spark line:** `Every concept.` · **runningText:** `concepting…` · **Result:** B04

> Brief: launch a reusable water bottle for city commuters. Give me a wall of distinct
> visual ad concepts — different angles, different emotional registers — as concept cards
> I can react to. Don't pick a favourite. That part is my job.

ASK→RESULT LAW: this is the actual prompt behind B04's grid. The last line —
"Don't pick a favourite. That part is my job." — is the reel's thesis stated by the
operator inside the prompt itself, before the reel argues it.

---

## B08 — the handoff (on screen, READ ALOUD VERBATIM)

**Greeting:** `Your turn.` · **runningText:** `paste this into Claude…`

> Here are my last 5 pieces of ad copy or creative. For each one, tell me which part was
> execution — something AI could now produce — and which part was judgment only a person
> could make. Then tell me honestly what's left if you remove the execution.

**Rubric shown beneath (HANDOFF LAW — scaffolded, not "ask Claude about X"):**

1. `grade it: does it split EVERY piece?`
2. `grade it: does it disagree with you anywhere?`
3. `grade it: would a client pay for the leftover?`

Plus the spoken failure signal: *"If it says everything was judgment, you flattered
yourself."* The prompt is read aloud word for word, then graded — a handoff where the
prompt only appears on screen is a defect.

This prompt is the reel's whole argument turned into a tool: it makes the viewer run the
execution/judgment split on their own portfolio, and the third rubric item ("would a
client pay for the leftover?") is the uncomfortable one that makes it worth doing.

---

## Generation prompts — the five illustration beats

These are **not** generated media: they are deterministic renders of committed scene
source, so there is no image or video prompt to log. Recorded below is the authoring
intent each composition was built to satisfy.

| Beat | Composition | Authoring intent |
|---|---|---|
| B01 | `JdgDiverge` | One node ("the creative job") splits at "AI arrives": execution dives to the floor in ink, judgment climbs in terracotta. The BLUF *is* a split, so the picture must enact the split. |
| B02 | `JdgSplit` | Two columns filling item by item as each is named — left in ink (moved to the machine), right in terracotta (still yours) — closing on "the left column got dramatically faster · the right column did not move". |
| B04 | `JdgOptions` | A grid of concept cards popping in faster than the voice can list them, all equal and unranked; then ONE takes a terracotta ring on the spoken word "choosing". Generating is free; choosing is the job. |
| B05 | `JdgBranch` | Two job descriptions off one question, with B02's columns ghosted behind each branch so the example visibly uses the framework. Resolver: "the description is the whole difference". |
| B06 | `JdgStakes` | Four things the machine cannot own, each landing on its spoken phrase with a terracotta marker and a one-line why, closing on the self-test. |

All five carry the `@NikBearBrown` corner bug (LOGO LAW) via the shared stage in
`runtime/remotion/src/scenes/claudeStage.tsx`.

## Build prompt

See `BUILD-PROMPT.md`.
