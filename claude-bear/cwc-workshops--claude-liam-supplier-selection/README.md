# Claude, Supplier Selection — The Score Behind the Pick

You'd guess Claude just picks whichever supplier is cheapest and calls it
done. It doesn't. A Claude skill is a folder Claude reads before it acts,
and this one, called "supplier-selection," has one file inside:
`SKILL.md` — plain language, no hidden logic. Open it and price is only
part of the story: the score weighs price, lead time, and reliability
together — fifty percent, thirty percent, twenty percent. Claude
normalizes price and lead time onto the same zero-to-one scale,
multiplies each factor by its weight, and adds them up. Highest score
wins; ties break on price, then lead time, then name. Feed it the same
quotes twice and the formula scores them identically, every time — that
repeatability is real. But SKILL.md also carries override notes that
never show up in the catalog data, and if one applies, it can beat the
top score.

**Topic:** CLAUDE SKILLS · ANTHROPIC
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/cwc-workshops--claude-liam-supplier-selection

---

## Chapters

0:00 The naive framing: "Claude just picks the cheapest"
0:10 The folder, one file: supplier-selection/SKILL.md
0:21 The wrong guess: lowest price wins?
0:31 The anchor: the weighted score, three factors
0:44 The mechanism: normalize, weight, sum
0:58 The anchor returns: same weights, an override can flip it
1:15 Carry-out
1:23 Your turn
1:35 Outro

---

## YOUR TURN

I'm going to hand you a short scoring formula with a few weighted factors
in it. Before you compute anything, tell me each factor's weight and how
you'd combine them — before you run the numbers.

Run that with any short weighted formula you have on hand — a rubric, a
scoring rule, anything with weights in it — not the video's supplier
example.

---

## Deliberately not claimed

No claim that price never matters — it carries the largest single weight
(50%) in the formula, just not the whole formula. No verdict on whether
"supplier-selection" is a *well-built* skill: the reel states what the
file contains and what Claude does with it, and stops there. No invented
supplier names, prices, or a specific override narrated — only the true,
generic fact that the formula's weights are fixed and that override notes
exist outside the catalog data and can change the pick.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics), including the Remotion writer-performance cold open. No
human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AnthropicSkills #AIExplained #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
