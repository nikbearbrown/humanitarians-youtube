# PROMPTS - Green Because It Wasn't Looking

No image or video generation was used. Manim + Remotion only, so there are no
model prompts to record. GATE F requires this file; its honest content is that
nothing was generated.

## Stills

None. No archival fetch, no `pantry/`, no Ken Burns beats. Every frame is drawn.

## Higgsfield

Not used, not installed, not offered. Fellow Tier build, entirely free: Kokoro
for narration, Manim and Remotion for picture.

## The on-screen prompts that ARE in the reel

Written, not generated, and shown to the viewer as content inside the composer:

**B00** - the week's ask

    claude "why does npm run verify pass when nothing has ever compiled the
            step scripts?"

**B03** - the ask, expanded

    claude "make conformance read the step scripts - and keep it fast enough
            that people still run it"

**B10** - the scaffolded task handed to the viewer

    claude "make this check print every path it opened, grouped by type - then
            tell me what it never opened"

The B10 prompt has to work on a stranger's CI, so it asks for an artifact rather
than a judgment: a list of paths grouped by type. "Then tell me what it never
opened" is the load-bearing clause - a check can only report what it looked at,
so the gap has to be computed against the repository, not against the check.
