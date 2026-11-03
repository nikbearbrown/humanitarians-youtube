# PROMPTS — on-screen Claude prompts in "The Risk Register"

ASCII-only (Remotion render constraint on this machine).

## T00 — cold open (the question)
> The AI in my project tools can auto-build and score a whole risk register. Can I trust
> it to catch the risks that actually matter?

## T04 — the ask (build the register)
> Draft and score a risk register for this project: probability and impact for each risk,
> pulled only from the plan I gave you. Don't invent risks to fill the page, and list
> separately anything you can't assess without project context I haven't provided.

## T08 — the handoff (copy/paste this — the scaffolded viewer task)
> Build me a risk register for the project below.
> [PASTE YOUR PLAN]
> 1. SCORE only the risks you can justify from the plan (probability x impact).
> 2. SEPARATELY list every assumption you made + everything you canNOT assess
>    without my team, vendors, and timeline.
> 3. Do NOT invent risks to fill the page.
> Give me (a) the scored register and (b) the 'blind spots' list.

**Good answer:** a scored register PLUS an honest blind-spots list naming what it couldn't
assess. **Bad answer:** a wall of green with no blind-spots list — the sign to go hunt the
project-specific risk yourself.
