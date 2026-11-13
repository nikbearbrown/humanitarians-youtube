# SCRIPT: *Same Logic, Two Languages* (Short, 9:16)

**Draft 2, 2026-10-04.** Rewritten at Tanmay's request: draft 1 (1:10) was too hurried to give the context. A
short-only script (standing rule: a Short is one complete story, never long-form beats stitched together), now about
2:00, well inside YouTube's 3-minute Shorts limit. One arc: the hook number → what I was doing and on what → what the
detector does, on invented companies → answers first, then the match → why the match told me almost nothing → my own
changes went unnoticed → why → two companies placed on the line → where I stopped, and the question, with my name at
the start and the end. Numbers in words for the voice; digits on screen. "My-croft" is the Kokoro respelling
(captions show "Mycroft").

## Continuity: one table, one story

**Words:** every beat opens on the one before it.

| Cut | The join |
|---|---|
| S01 → S02 | "…gives zero point six two." → "**That mattered to me** because of what I was working on." |
| S02 → S03 | "…so the recipe has scripts that run." → "**Here's what it does.**" |
| S03 → S04 | "No real company is judged here." → "**Before writing any Python**, I…" |
| S04 → S05 | "Sixteen out of sixteen agreed." → "**And that told me almost nothing.**" |
| S05 → S06 | "…whether my check would notice if it didn't." → "**So I changed my own copy.**" |
| S06 → S07 | "The comparison still agreed." → "**It was doing its job.**" |
| S07 → S08 | "…no news average exactly on a tie." → "**So I added two companies** built to stand exactly there." |
| S08 → S09 | "It was better test data." → "**All of this ran on invented data.**" |

**Picture:** the same two-column table throughout (original JavaScript left, my Python right), each beat opening in
the state the last one ended in: S01 the 0.625 row (≠) → S02 the two ported nodes (→) → S03 five sources, six
patterns, the invented companies → S04 the 13 expected flags, then the 16-company grid ticking "=" → S05 the three
language differences (≠) → S06 my changed copy (scratch run) → S07 the 14 test companies at the time, all "=" → S08
+ FXR, FXQ (≠) → S09 "0 live calls", then the ring between the two versions, then the end card.

---

### S01 · HOOK, one number, two answers
> Hi, this is Tanmay Kulkarni, in for Humanitarians AI. Here's one number. Zero point six two five. Ask JavaScript to round it to two places, and you get zero point six three. Ask Python the same thing, the everyday way, and it gives zero point six two.

*On screen:* name chip; JS `(0.625).toFixed(2)` "0.63" ≠ Python `f"{0.625:.2f}"` "0.62". *Refs:* L1.

### S02 · WHAT I WAS WORKING ON
> That mattered to me because of what I was working on. My-croft describes itself as "both a book and a working agentic repository" for finance. Its recipes are reusable pipelines. I picked one, a contradiction detector, and rewrote its core logic from the original workflow's JavaScript into Python, so the recipe has scripts that run.

*On screen:* the README quote with its source; rows "Aggregate All Signals" → `aggregate()`, "Run Pattern Detection Engine" → `detect()`. *Refs:* R1, C1, C2.

### S03 · WHAT THE DETECTOR DOES
> Here's what it does. It reads five kinds of evidence about a company, from what it says on earnings calls to the tone of its news. It flags every place where two of them disagree, for a person to review. To test it, I invented sixteen companies. No real company is judged here.

*On screen:* five source chips → "every disagreement becomes a flag, for a person to review" → "16 invented companies: Alpha Fixture Co … Romeo Fixture Co". *Refs:* C3, C4.

### S04 · ANSWERS FIRST, THEN THE MATCH
> Before writing any Python, I went through the original JavaScript and wrote down the thirteen flags it should raise. Then I ran the original right beside my version, on all sixteen companies, comparing every flag word for word. Sixteen out of sixteen agreed.

*On screen:* `expected-flags.json` · "13 flags · 16 companies · written first"; then the parity row (=) and the 16-company grid ticking "="; "16 / 16". *Refs:* C5, C6.

### S05 · WHY THAT TOLD ME ALMOST NOTHING
> And that told me almost nothing. A match only means something if a mismatch could have shown up. And the two languages really do differ, like that rounding tie. So I made my Python copy JavaScript's behavior on purpose. The question was whether my check would notice if it didn't.

*On screen:* the three language differences, each ≠ (`toFixed` vs Python rounding, `String(1.0)` "1" vs "1.0", `[] || "x"` vs `[] or "x"`); then the helpers `js_to_fixed`, `js_str`, `js_or`. *Refs:* L1, L2, L3, C7.

### S06 · I CHANGED MY OWN COPY
> So I changed my own copy. One threshold, from zero point six to zero point six one. Then Python's own rounding, in place of JavaScript's. The comparison still agreed.

*On screen:* rows `confidence >= 0.6` | `confidence >= 0.61` and `toFixed rounding` | `Python's rounding`, both "=" ("comparison: 14 / 14 agree"); right column "MY COPY · changed on purpose", badge "SCRATCH RUN · NOT THE SHIPPED CODE". *Refs:* C8.

### S07 · NOBODY STOOD ON THE LINE
> It was doing its job. None of my test companies stood on the line. Not one had a confidence of exactly zero point six, and no news average landed exactly on a tie.

*On screen:* the 14 test companies at the time, all "="; the note "None of them stood on the line". *Refs:* C8.

### S08 · STANDING ON THE LINE
> So I added two companies built to stand exactly there. Romeo, at a confidence of exactly zero point six. Quebec, with a news average of exactly zero point six two five. Run the same two changes again, and each one fails, on the company placed for it. The fix wasn't new code. It was better test data.

*On screen:* FXR and FXQ join the grid and turn "≠"; the rows turn "≠": "now fails on FXR · Romeo Fixture Co", "now fails on FXQ · Quebec Fixture Co"; the note "The fix wasn't new code. It was better test data." *Refs:* C8, C9.

### S09 · WHERE I STOPPED, AND THE QUESTION
> All of this ran on invented data. No database, no news feed, and no AI model was ever called, and live mode stays off until the people with live access decide. So, if you've rewritten something you depend on, where would your two versions disagree? Put one test exactly there. I'm Tanmay Kulkarni, for Humanitarians AI. The full story is in Same Logic, Two Languages.

*On screen:* "0 live calls · gate 5: deny"; then "your original" | ring | "your rewrite", "↑ one test, standing exactly here"; then the end card: *Same Logic, Two Languages*, Tanmay Kulkarni, @HumanitariansAI. *Refs:* C12.
