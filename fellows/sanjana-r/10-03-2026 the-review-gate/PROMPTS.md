# PROMPTS — The Review Gate

On-screen Claude prompts (the ASK→RESULT receipts and the handoff). These are the
verbatim strings rendered in the composer beats.

## T03 — ASK (generates the scoreboard, T04)
> Here's my raw two-week review tracker -- dates, fellows, counts, approve or modify,
> GitHub yes/no. Total it up and lay out a scoreboard: how many reviewed, approved vs
> sent back, and how many had code on GitHub. Don't rename or re-judge anything.

## T08 — HANDOFF (the viewer's scaffolded task)
> Here's a log of work I review regularly.
> [PASTE YOUR LOG]
>
> 1. SCOREBOARD: total it -- how many, how many passed vs sent back, and any
>    compliance column (e.g. code committed).
> 2. BUILD THE GATE: from the reasons things got sent back, draft a 3-check gate I
>    can apply to EVERY item the same way.
> 3. For each check give me the PASS test and the FAIL action.
> Don't re-judge my past calls -- just build the repeatable gate.

**Good vs bad result (read-and-discuss, per HANDOFF LAW):** a good answer returns a
scoreboard plus three or four checks each with a concrete pass test and a fail action
you can actually run. A bad answer just says "looks good" — the gut call the gate replaces.

## Short — S02 handoff
> Here's a log of work I review [PASTE]. Turn the reasons I send things back into a
> 3-check gate -- each with a pass test and a fail action -- that I can run on every
> item the same way.

## Build prompt
See BUILD-PROMPT.md for the single paste-ready prompt that rebuilds the whole cut.
