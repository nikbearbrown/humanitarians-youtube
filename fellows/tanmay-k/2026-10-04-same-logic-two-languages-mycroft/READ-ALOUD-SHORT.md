# READ-ALOUD — Gate P sheet (the Short, 9:16) · draft 2

*Same Logic, Two Languages (Short)* · generated from `short/beat_sheet.json` (built from `short/SCRIPT.md`).

**What changed from draft 1:** draft 1 (7 beats, ~1:10) was too hurried to give the context. Draft 2 adds what Mycroft and the
recipe are (S02), what the detector does and why the companies are invented (S03), the answers written before the code (S04),
why the two languages differ (S05), and where I stopped (S09). About 2:05 at the voice's measured pace, inside YouTube's 3-minute limit.

**How to run Gate P:** read each beat out loud. Listen for whether it plays as one story (each beat opens on the one before it),
whether a viewer who never sees the long film would follow it, and whether your name lands in S01 and S09.
Reply "Gate P PASS" (with any notes). No Short audio is generated before that.

## Say-it-right checklist (Kokoro's own phonemes, checked 2026-10-04)

| Word | Should sound like | Kokoro | Where |
|---|---|---|---|
| Tanmay Kulkarni | kul-KAR-nee | `tˈænmeɪ kˈʌlkɑːɹni` | S01, S09 |
| My-croft (respelled) | MY-kroft; captions show "Mycroft" | `maɪkɹˈɔft` | S02 |
| agentic | ay-JEN-tik | `eɪdʒˈɛntɪk` | S02 |
| JavaScript / Python | JAH-vuh-script / PY-thon | `dʒˈɑːvə skɹˈɪpt` / `pˈaɪθən` | throughout |
| Romeo / Quebec | ROH-mee-oh / kwuh-BEK | `ɹˈoʊmɪˌoʊ` / `kwᵻbˈɛk` | S08 |
| live (mode / access) | LIVE as in "alive" | `lˈaɪv` | S09 |
| zero point six two five | every digit separate | `zˈiəɹoʊ pˈɔɪnt sˈɪks tˈuː fˈaɪv` | S01, S08 |

## Quote: read exactly as written

| Beat | Quote | Source |
|---|---|---|
| S02 | "both a book and a working agentic repository" | Mycroft README |

## The script

### [0:00] S01 · HOOK, one number, two answers

_Tone: warm hello, then curious; let the two numbers land_

Hi, this is Tanmay Kulkarni, in for Humanitarians AI. Here's one number. Zero point six two five. Ask JavaScript to round it to two places, and you get zero point six three. Ask Python the same thing, the everyday way, and it gives zero point six two.

_On screen: name chip; JS `(0.625).toFixed(2)` "0.63" ≠ Python `f"{0.625:.2f}"` "0.62"._

> ☐ reads cleanly   ☐ note: ______________________

### [0:13] S02 · WHAT I WAS WORKING ON

_Tone: friendly, plain: what I was doing, not a boast_

That mattered to me because of what I was working on. My-croft describes itself as "both a book and a working agentic repository" for finance. Its recipes are reusable pipelines. I picked one, a contradiction detector, and rewrote its core logic from the original workflow's JavaScript into Python, so the recipe has scripts that run.

_On screen: the README quote with its source; rows "Aggregate All Signals" → `aggregate()`, "Run Pattern Detection Engine" → `detect()`._

> ☐ reads cleanly   ☐ note: ______________________

### [0:30] S03 · WHAT THE DETECTOR DOES

_Tone: brisk and clear; "No real company is judged here" said gently_

Here's what it does. It reads five kinds of evidence about a company, from what it says on earnings calls to the tone of its news. It flags every place where two of them disagree, for a person to review. To test it, I invented sixteen companies. No real company is judged here.

_On screen: five source chips → "every disagreement becomes a flag, for a person to review" → "16 invented companies: Alpha Fixture Co … Romeo Fixture Co"._

> ☐ reads cleanly   ☐ note: ______________________

### [0:45] S04 · ANSWERS FIRST, THEN THE MATCH

_Tone: patient, then a small win at "Sixteen out of sixteen agreed."_

Before writing any Python, I went through the original JavaScript and wrote down the thirteen flags it should raise. Then I ran the original right beside my version, on all sixteen companies, comparing every flag word for word. Sixteen out of sixteen agreed.

_On screen: `expected-flags.json` · "13 flags · 16 companies · written first"; then the parity row (=) and the 16-company grid ticking "="; "16 / 16"._

> ☐ reads cleanly   ☐ note: ______________________

### [0:58] S05 · WHY THAT TOLD ME ALMOST NOTHING

_Tone: the turn: honest doubt, then purposeful_

And that told me almost nothing. A match only means something if a mismatch could have shown up. And the two languages really do differ, like that rounding tie. So I made my Python copy JavaScript's behavior on purpose. The question was whether my check would notice if it didn't.

_On screen: the three language differences, each ≠ (`toFixed` vs Python rounding, `String(1.0)` "1" vs "1.0", `[] || "x"` vs `[] or "x"`); then the helpers `js_to_fixed`, `js_str`, `js_or`._

> ☐ reads cleanly   ☐ note: ______________________

### [1:12] S06 · I CHANGED MY OWN COPY

_Tone: steady; let "The comparison still agreed." sit_

So I changed my own copy. One threshold, from zero point six to zero point six one. Then Python's own rounding, in place of JavaScript's. The comparison still agreed.

_On screen: rows `confidence >= 0.6` | `confidence >= 0.61` and `toFixed rounding` | `Python's rounding`, both "=" ("comparison: 14 / 14 agree"); right column "MY COPY · changed on purpose", badge "SCRATCH RUN · NOT THE SHIPPED CODE"._

> ☐ reads cleanly   ☐ note: ______________________

### [1:21] S07 · NOBODY STOOD ON THE LINE

_Tone: calm; "It was doing its job" is relief, not excuse_

It was doing its job. None of my test companies stood on the line. Not one had a confidence of exactly zero point six, and no news average landed exactly on a tie.

_On screen: the 14 test companies at the time, all "="; the note "None of them stood on the line"._

> ☐ reads cleanly   ☐ note: ______________________

### [1:31] S08 · STANDING ON THE LINE

_Tone: the fix lands; small smile at "better test data"_

So I added two companies built to stand exactly there. Romeo, at a confidence of exactly zero point six. Quebec, with a news average of exactly zero point six two five. Run the same two changes again, and each one fails, on the company placed for it. The fix wasn't new code. It was better test data.

_On screen: FXR and FXQ join the grid and turn "≠"; the rows turn "≠": "now fails on FXR · Romeo Fixture Co", "now fails on FXQ · Quebec Fixture Co"; the note "The fix wasn't new code. It was better test data."_

> ☐ reads cleanly   ☐ note: ______________________

### [1:47] S09 · WHERE I STOPPED, AND THE QUESTION

_Tone: calm about the limits, then direct to the viewer, then a warm sign-off_

All of this ran on invented data. No database, no news feed, and no AI model was ever called, and live mode stays off until the people with live access decide. So, if you've rewritten something you depend on, where would your two versions disagree? Put one test exactly there. I'm Tanmay Kulkarni, for Humanitarians AI. The full story is in Same Logic, Two Languages.

_On screen: "0 live calls · gate 5: deny"; then "your original" | ring | "your rewrite", "↑ one test, standing exactly here"; then the end card: *Same Logic, Two Languages*, Tanmay Kulkarni, @HumanitariansAI._

> ☐ reads cleanly   ☐ note: ______________________

_Estimated runtime 2:07 (432 words at 3.4 words/s, the pace Kokoro actually spoke the long film at). Every claim is a ✅ row in `../FACTCHECK.md` (L1–L3, R1, C1–C9, C12); nothing new is claimed._
