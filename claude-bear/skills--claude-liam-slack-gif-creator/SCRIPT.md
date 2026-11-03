# SCRIPT.md — Slack GIF Creator (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-slack-gif-creator` (Teardown, examining Anthropic's
`slack-gif-creator` skill) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict);
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
You might picture asking Claude for a bouncing star GIF, and it just
makes the whole animation for you, start to finish. It doesn't — it
assembles what you actually draw. Liam, in for Bear.

## Act I — Stakes: the two formats, and the anchor ask

**NB01 — two formats, one enforced spec** (source B01)
Slack enforces exact numbers for these GIFs: emoji ones at 128 by 128
pixels, under 3 seconds; message ones at 480 by 480, same frame rate and
color range. Miss the numbers, and Slack won't take the file.

**NB02 — the ask, planted** (ANCHOR PLANTED)
Picture this ask: a bouncing star emoji GIF for the team channel —
eye-catching, and it has to land inside those Slack limits. Hold onto
that.

## Act II — The wrong guess, and the case that breaks it

**NB03 — "ready-made templates?"** (WRONG GUESS)
So the natural guess: the skill ships ready-made animations — ask for
bounce, and out comes a finished bounce dot gif.

**NB04 — no bounce() to call** (BREAK)
But there's no bounce function to call. Easing hands back a curve,
GIFBuilder assembles the frames — the actual drawing, where the star sits
on each frame, is PIL code you write yourself.

## Act III — What it actually does

**NB05 — GIFBuilder: frames in, GIF out** (source B01)
GIFBuilder takes width, height, and frame rate, accepts your PIL frames
one at a time, then saves with color quantization — 48 colors and
optimize-for-emoji, for the emoji track.

**NB06 — easing: progress in, motion out** (source B01)
The easing module turns a progress value from zero to one into a smoothed
number — seven curves: bounce out, elastic out, ease in, and more — and
that number drives your drawing.

**NB07 — validate before it ships** (source B01)
Before anything ships, two functions check it: validate-gif for a full
compliance report, is-slack-ready for a quick yes or no — the same
numeric rules from the spec, checked automatically.

**NB08 — one flag: named gaps, not all gaps** (source B05, ONE FLAG)
One flag: the skill names five limitations up front — no complex-shape
helper, no text guidance, no dithering fix, no loop-matching helper, and
you install the dependencies yourself. That's what's documented, not a
guarantee of everything.

## Act IV — The anchor returns

**NB09 — the star, built and checked** (ANCHOR PAYOFF)
Back to that bouncing star: draw it frame by frame with PIL, drive the
bounce with bounce-out easing, let GIFBuilder assemble and quantize it —
then don't call it done until is-slack-ready says yes.

## Act V — Both directions

**NB10 — what a pass proves** (DIRECTION A)
When it passes, that's real: the file is the right size, under the time
limit, inside the color budget — Slack will accept it.

**NB11 — what a pass doesn't prove** (DIRECTION B, source B05)
But passing doesn't mean it looks good: a heart or a snowflake still needs
hand-drawn polygon math, dithering at 48 colors isn't checked, and a
seamless loop only happens if you matched the first and last frame
yourself.

## Close

**BCRY — carry-out**
Slack GIF Creator hands you the exact numbers and the assembly toolkit.
The drawing is still yours — and it isn't done until the validator says
so.

**BHTF — your turn**
Your turn. Paste this into Claude: make me a pulsing fire emoji GIF for
Slack. It should loop smoothly, feel energetic, and stay under three
seconds. Use the Slack GIF Creator skill. Then watch three things: does it
look up the emoji spec before writing any code? Does it use GIFBuilder and
the easing module instead of reinventing frame assembly? And does it call
is-slack-ready or validate-gif before calling the GIF done?

**BOUT — outro**
Slack GIF Creator. Liam, in for Bear.

## Beat-count note

15 beats total: B00 (hesitant writer) + 11 GRAPHIC body beats (NB01-NB11,
Manim chip-row) + BCRY + BHTF + BOUT — same shape and count as the
`skills--claude-liam-pptx` and `skills--claude-liam-claude-api` siblings.
The source's B02 (8 animation concepts) and part of B05 (the "gets right"
half of the teardown) are folded into NB06/NB07's mechanism beats and
NB08's flag rather than kept as a separate self-demo beat — Plain register
explains the mechanism and stops, it does not itemize a teardown's "what
it gets right" list. The source's five documented "bites" (no
complex-shape helper, no text-rendering guidance, no dithering fix, no
loop-matching helper, dependencies not pre-installed) become NB08's one
inference flag (they're a named, not necessarily complete, list) and
NB11's both-directions beat (three of the five bites — shapes, dithering,
looping — recur there as concrete things a passing validator does not
check).

## Register audit (Plain)

| Move | Beat | Check |
|---|---|---|
| 1 stakes | NB01, NB02 | mechanism (GIFBuilder/easing) waits until NB05 |
| 2 wrong guess | NB03 | ready-made-template guess, stated plausibly |
| 2 break | NB04 | falsified by a case: no `bounce()`, PIL drawing is yours |
| 3 mechanism | NB05, NB06, NB07 | GIFBuilder, easing, validators |
| 3 one flag | NB08 | exactly one — named gaps aren't a complete list |
| 4 anchor | NB02 -> NB09 | the bouncing-star ask, planted then paid off |
| 5 both directions | NB10, NB11 | what a pass proves / doesn't prove |
| 6 carry-out | BCRY | spec+toolkit vs. drawing vs. validation gate |
| no judgment | — | NB08/NB11 state what's checked and what isn't; never rule on whether the skill was built well |

## Deliberately not claimed

- **Not "the skill is incomplete."** NB08's flag states the skill *names*
  five limitations up front; it does not claim those are all the
  limitations that exist, and does not editorialize about whether that's
  a design flaw (that would be Teardown judgment).
- **Not "validation checks quality."** NB10/NB11 keep compliance
  (dimensions, timing, color count) and quality (shape accuracy, dithering
  smoothness, loop seamlessness) as two separate, non-overlapping claims.
- **No accusation of anyone being misled.** The "ready-made templates"
  guess in NB03 is an ordinary newcomer assumption, treated as one.

## Handoff prompt (BHTF, read aloud then discussed)

> "Make me a pulsing fire emoji GIF for Slack. It should loop smoothly,
> feel energetic, and stay under 3 seconds. Use the Slack GIF Creator
> skill."

What to watch for: does Claude look up the emoji spec (128x128, under 3s,
48-128 colors) before writing any code; does it use GIFBuilder and the
easing module rather than reinventing frame assembly; does it call
`is_slack_ready` or `validate_gif` before declaring the GIF done.

---
**GATE P — signed:** ______________________  (human)
