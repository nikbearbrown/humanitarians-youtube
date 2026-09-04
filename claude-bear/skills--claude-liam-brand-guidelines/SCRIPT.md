# SCRIPT.md — Claude, Branded. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-brand-guidelines` (Teardown, examining Anthropic's
`brand-guidelines` skill) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop, no verdict);
cold open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone asked whether Claude just invents a look for their slides. It
doesn't invent anything — it copies. So here's the real question: can
Claude copy a brand's exact look onto my slides?

## Act I — Stakes: the skill, and the anchor slide

**NB01 — SKILL.md, and nothing else** (source B01)
A skill is a folder Claude reads before it touches your file. This one
holds a single thing: SKILL.md — the brand guide, written in plain
language, and nothing else.

**NB02 — One plain slide, in** (ANCHOR PLANTED)
Hand it a plain slide — a title, three bullet points, whatever font came
default — and ask for the Anthropic look on the way back out.

## Act II — The wrong guess, and the case that breaks it

**NB03 — "So it's picking a look?"** (WRONG GUESS)
So the natural guess is that Claude is making a design call here —
picking colors and fonts that feel like Anthropic, the way a person
would.

**NB04 — Same spec, two decks** (BREAK)
Brand two completely different decks and you get the exact same seven
hex codes and the exact same two fonts, both times. That's not taste —
that's a lookup.

## Act III — What it actually does

**NB05 — Read, then write** (source B02)
The pipeline is three steps, always in this order: a document comes in,
Claude reads SKILL.md, the document goes out restyled. No loop, no
back-and-forth.

**NB06 — The exact hex, not a guess** (source B03)
The colors are exact hex values straight from the file: a near-black for
text and dark backgrounds, a cream for light ones, and one accent orange
as the primary.

**NB07 — Three accents, rotating** (source B03)
Two more grays handle secondary elements and subtle backgrounds, and two
more accents — a blue, a green — rotate in behind the orange on every
shape that isn't text.

**NB08 — 24pt is the line** (source B04)
Typography works the same way: Poppins on anything twenty-four points
and up, Lora on everything smaller, with Arial and Georgia as fallbacks
if those fonts aren't installed.

## Act IV — The anchor returns

**NB09 — The same slide, now on-spec** (ANCHOR PAYOFF)
Back to that plain slide: the title is now bold Poppins in near-black,
the three bullets sit in Lora, and each bullet's icon shape has picked
up one of the three rotating accents.

## Act V — Both directions

**NB11 — Run it again, get the same** (DIRECTION A)
Feed it the same deck a hundred times and you get the identical result a
hundred times — same hex, same fonts, same rotation, because none of it
is improvised.

**NB12 — It can't see the room** (DIRECTION B — ONE FLAG)
But hand it a deck meant for a bright projector, and — the one inference
in this video — it very likely keeps that same cream background anyway:
the spec has no way to sense the room it'll be shown in.

## Close

**BCRY — carry-out**
Claude doesn't invent your brand — it copies the exact spec from one
file, the same way, every single time.

**BHTF — your turn**
Your turn. Paste this into Claude: I have a slide deck I want to look
like it came from Anthropic. Use the brand-guidelines skill. Start by
telling me the exact colors and fonts you're about to apply, and why,
before you touch any code. That last clause is the point — it makes the
spec's boundaries visible, right where you'd otherwise assume Claude is
guessing.

**BOUT — outro**
Claude, Branded. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| 1 stakes | NB01, NB02 | the skill's anatomy, then the anchor slide planted |
| 2 wrong guess | NB03 (guess), NB04 (break) | "picking a look" broken by identical output across two decks |
| 3 mechanism | NB05, NB06, NB07, NB08 | pipeline, then colors (x2), then typography |
| 4 anchor | NB02 (plant) → NB09 (payoff) | same plain slide, restyled |
| 5 both directions | NB11, NB12 | holds: identical output on repeat. flips: can't sense the room (flagged as this video's one inference) |
| 6 carry-out | BCRY | "copies... every single time" |

## Beat-count note (redo)

Source has 9 filled beats (B00 ClaudeComposerAsk cold open + B01-B05 five
`BrandGuidelines*` REMOTION body beats, hardcoded to the CLAUDE fidelity
token palette + BVDT verdict + BHTF handoff + BOUT outro). This redo
expands the five source body beats to eleven (NB01-NB09, NB11-NB12) to
give the WRONG-GUESS and BOTH-DIRECTIONS laws their own dedicated beats
(the Teardown source folded "no creativity" and "cannot adapt to
context" into a single B05 design-tell beat; Plain separates the wrong
guess/break from the both-directions pair, per hai-simple's spine) and
to plant/pay off a concrete ANCHOR (one plain slide, NB02 → NB09) that
the source's B00 line ("give Claude a PowerPoint...") implied but never
carried through as a recurring visual. B01's anatomy beat (SKILL.md /
LICENSE.txt folder listing) is folded into NB01's narration rather than
kept as a separate beat — the folder contents are a one-line fact, not a
distinct teaching point. Source's five `BrandGuidelines*.tsx` components
are not reused: they import the CLAUDE token file directly (no
ink/accent/bg props), so they render in the Claude fidelity skin, not
the humanitarians palette — same seam already logged on multiple
`books--claude-liam-*` and `k12-teacher-skills--*` siblings. NB01-NB09,
NB11-NB12 are built fresh as GRAPHIC (Manim) beats on the shared generic
chip-row template instead, carrying the same facts (SKILL.md contents,
pipeline order, all seven hex values, both font names and thresholds,
the design-tell's two facts split across NB11/NB12) in the humanitarians
palette. No source beat was ai-video-prompt, pantry, or a human-drop
slot — NO-GENAI/NO-PANTRY LAW required no substitution beyond B00 (the
source's B00 was already `ClaudeComposerAsk`, REMOTION, not a puppet
ask — only its role as a non-hesitant cold open needed replacing).

Landing at 15 beats total: B00 + 11 GRAPHIC body beats (NB01-NB09,
NB11-NB12) + BCRY + BHTF + BOUT.
