# SCRIPT.md — Web Application Testing (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-webapp-testing` (Teardown, examining Anthropic's
`webapp-testing` skill) — question, facts, and body argument carried over;
narration re-registered to Plain (explain, then stop, no verdict); cold open
replaced with the BrutalistHesitantWriter; close carries the Humanitarians
AI skin.

## B00 — cold open (BrutalistHesitantWriter)
At first this reads as testing the instant a page loads. Cross that out —
the real question is whether the page has gone idle, not just appeared on
screen. Liam, in for Bear.

## Act I — Stakes: the two situations, and the anchor ask

**NB01 — two situations, one decision first** (source B01)
The skill covers two situations: a static HTML file you can read directly,
and a dynamic web app that's actually running somewhere as a server. Which
one you're looking at decides everything that happens next.

**NB02 — the ask, planted** (ANCHOR PLANTED)
Picture this ask: a local React app on port 3000 — click Submit on a login
form, and check that a success message appears. Hold onto that request;
we'll come back to it.

## Act II — The wrong guess, and the case that breaks it

**NB03 — "loaded means ready?"** (WRONG GUESS)
So the natural guess: once a page has loaded, its buttons and fields are
already there, ready to grab.

**NB04 — shell loaded, not yet rendered** (BREAK)
But a dynamic app can finish loading its shell before its JavaScript has
actually drawn the real content. Inspect too early and what you're looking
at is a placeholder, not the button.

## Act III — What it actually does

**NB05 — wait for idle, first** (source B01, the critical rule)
The fix is one rule: wait for the network to go idle before you touch the
page at all. That single wait is what the majority of these failures come
down to.

**NB06 — the server, handled for you** (source B02)
A helper script manages the server itself, so your automation script holds
nothing but browser logic. One server: name it and its port. Two servers,
backend and frontend: name both, and the helper starts each in turn.

**NB07 — look, then act** (source B01, recon loop)
Reconnaissance before action: navigate, wait for idle, then screenshot or
inspect what actually rendered — before you decide on a single selector.

**NB08 — descriptive beats brittle** (source B02)
Once you can see the real page, favor descriptive selectors — matching by
text, by role, by an actual id — over a brittle absolute path through the
markup.

## Act IV — The anchor returns

**NB09 — the same login form, done right** (ANCHOR PAYOFF)
Back to that login form: the helper starts the app on port 3000, Claude
waits for idle, screenshots the rendered page, finds Submit by its visible
text, clicks it, and only then checks for the success message.

## Act V — Both directions

**NB10 — what one wait catches** (DIRECTION A)
When it's followed, it works: that one wait, in the right order, catches
the single most common way Playwright breaks on a dynamic page.

**NB11 — what's not walked through** (DIRECTION B — ONE FLAG)
One flag: nothing here says what to do next — a login wall, a locator that
still fails, a CI machine with no display. Those are real situations the
skill doesn't walk you through.

## Close

**BCRY — carry-out**
Loaded and rendered are two different moments. Wait for the page to go
idle before you touch anything — or you're testing a skeleton, not the
real page.

**BHTF — your turn**
Your turn. Paste this into Claude: I have a local React app running on
port 3000. Use the Web Application Testing skill to verify that clicking
the Submit button on a login form shows a success message. Then watch:
does it wait for the page to go idle before it looks for anything, or does
it inspect right away and risk grabbing a placeholder? That's the whole
gate.

**BOUT — outro**
Web Application Testing. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| 1 stakes | NB01, NB02 | the skill's two situations, then the anchor ask planted |
| 2 wrong guess | NB03 (guess), NB04 (break) | "loaded means ready" broken by the shell-vs-render case |
| 3 mechanism | NB05, NB06, NB07, NB08 | the idle rule, server handling, the recon loop, selector choice |
| 4 anchor | NB02 (plant) -> NB09 (payoff) | same login-form ask, executed correctly |
| 5 both directions | NB10, NB11 | holds: catches the single most common dynamic-app failure. flips: undocumented edges (login walls, failed locators, CI) aren't walked through — flagged as this video's one inference |
| 6 carry-out | BCRY | "loaded and rendered are two different moments... wait for idle" |

## Beat-count note (redo)

Source has 7 filled beats (B00 `ClaudeComposerAsk` cold open + B01/B02
Remotion body beats (`WebappTestingAnatomy`, `WebappTestingPatterns`) + B05
teardown (`WebappTestingTell`) + BVDT verdict + BHTF handoff + BOUT outro).
This redo expands the three source body beats to eleven (NB01-NB11) to give
the WRONG-GUESS and BOTH-DIRECTIONS laws their own dedicated beats (the
Teardown source folded the networkidle-placeholder insight and the
"gets right / bites" columns into narration threaded through B01/B02/B05;
Plain separates the wrong guess/break from the both-directions pair, per
hai-simple's spine) and to plant/pay off a concrete ANCHOR (the login-form
ask on port 3000 — NB02 -> NB09) that the source's own BHTF handoff line
used as its worked example but never carried through as a recurring beat
earlier in the reel.

Source's `WebappTesting*.tsx` components (`Anatomy`, `Patterns`, `Tell`) are
not reused: same seam already logged on the `docx`, `claude-api`, and
`mcp-builder` siblings — direct read confirms Claude-fidelity token imports
with no ink/accent/bg props, so they render in the Claude palette, not
humanitarians. Built fresh instead as 11 GRAPHIC (Manim) chip-row beats
(NB01-NB11) on the same shared generic template
(`scenes.py`/`render_scenes.py`/`build_beat_sheet.py`, copied from the
`claude-liam-docx` sibling's proven pattern), carrying the same facts in the
humanitarians palette (#F3EBDD/#2F2A26/#E4572E). No source beat was
ai-video-prompt, pantry, or a human-drop slot — NO-GENAI/NO-PANTRY LAW
required no substitution beyond B00 (the source's B00 was already
`ClaudeComposerAsk`, REMOTION, not a puppet ask — only its role as a
non-hesitant cold open needed replacing).

Landing at 15 beats total: B00 + 11 GRAPHIC body beats (NB01-NB11) + BCRY +
BHTF + BOUT.

**Fact-currency note:** the source skill file logged in the source sheet's
metadata (`../anthropics/skills/skills/webapp-testing/SKILL.md`) could not
be located on this machine as of this build (2026-09-04) — only the built
reel folder exists under `anthropics/skills/youtube/`, not a source
`skills/webapp-testing/` directory. Per the redo contract, facts (the
decision tree, the networkidle rule, `with_server.py` usage, selector
guidance, the three example scripts, the gets-right/bites list) are carried
over unchanged from the locked source script rather than re-verified
against a live skill file that could no longer be located.
