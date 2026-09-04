# How Does Claude Refresh a Deck?

Ask Claude to "refresh the deck with the new numbers" and it's tempting to
picture it reconsidering the whole slide — updating the commentary, the
trend language, maybe the framing along with the figure. That's not what's
happening. Anthropic's `deck-refresh` skill reads a written SKILL.md and
executes a linear pipeline: find every instance of one figure across the
deck, replace it with another, and leave everything else untouched. Watch
the anchor: $485M appears in the executive summary, again in the comps
table, and again in a footnote — three separate slides, each swapped in
turn to $512M. A deck where every figure changed isn't the same as a deck
that's still true — a sentence built on the old number doesn't get
rewritten just because the number did. A deck refresh is one figure,
swapped everywhere the step says to swap it — not Claude rewriting the
story.

**Topic:** DECK-REFRESH · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-deck-refresh

---

## Chapters

0:00 Refresh the deck — does Claude rewrite the story?
0:11 Reconsider the story, or find & replace?
0:30 One figure, three slides
0:48 Number changed, is the story still true?
1:09 Carry-out
1:17 Your turn
1:35 Outro

---

## YOUR TURN

"Give Claude a few sentences that repeat one figure in different
contexts — say, '$485M in revenue, up from $420M last quarter... book
value near $485M...' — and ask it to replace every instance of $485M with
$512M, and change nothing else. Then check whether a nearby sentence built
on the old number is still literally true, or whether the figure moved
while the sentence around it stayed exactly where it was."

Why it's worth running: watching whether the surrounding sentence keeps up
with the number is the fastest way to see the boundary of a figure swap,
instead of assuming the whole passage got reconsidered along with it.

---

## Deliberately not claimed

This reel redoes a published Teardown-register skill-showcase reel
(`claude-liam-deck-refresh`) in the Plain register for a general audience.
The underlying facts are unchanged from the source: the skill updates a
presentation with new numbers (quarterly refreshes, earnings updates, comp
rolls, rebased market data) by finding and replacing figures across an
existing deck — it does not reconsider the commentary, the trend
language, or the framing that figure sits inside. $485M -> $512M is the
source sheet's own literal worked example, kept because it's the concrete
case the source itself names — not an invented screen, template, or UI.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #FinancialServices #FinTech #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
