# READ-ALOUD — Gate P sheet (the work video)

*Same Logic, Two Languages* · generated from `beat_sheet.json` (built from `SCRIPT.md`) by `make_read_sheet.py`.

**How to run Gate P:** read each beat out loud at speaking pace. Listen for rhythm and emphasis,
whether each match's turn lands (B05, B07, B09), and whether the honest parts sound candid rather
than apologetic: every gap in this film is in my own work, found and fixed. Mark anything that trips you in the box. A reply of "Gate P PASS" (with any notes) is
recorded verbatim in `PEDAGOGY.md`. No audio is generated before that.

## Say-it-right checklist (Kokoro's own phonemes, checked; confirm by ear)

| Word | Should sound like | Kokoro | Where |
|---|---|---|---|
| Tanmay Kulkarni | kul-KAR-nee, as you say it | `tˈænmeɪ kˈʌlkɑːɹni` | B02, B13 |
| My-croft (respelled) | MY-kroft. Plain "Mycroft" came out MICK-roft (mˈɪkɹɔft); captions keep "Mycroft" | `maɪkɹˈɔft` | B02, B09 |
| agentic | ay-JEN-tik | `eɪdʒˈɛntɪk` | B02 |
| JavaScript / Python | JAH-vuh-script / PY-thon | `dʒˈɑːvə skɹˈɪpt / pˈaɪθən` | throughout |
| Fixture Co | FIX-cher koh, as written | `fˈɪkstʃɚ kˈoʊ` | B03, B08 |
| Romeo / Quebec | ROH-mee-oh / kwuh-BEK | `ɹˈoʊmɪˌoʊ / kwᵻbˈɛk` | B08 |
| parity | PAIR-uh-tee | `pˈæɹᵻɾi` | B05 |
| zero point six two five | every digit separate | `zˈiəɹoʊ pˈɔɪnt sˈɪks tˈuː fˈaɪv` | B01, B08 |
| live (data / mode / access) | LIVE as in "alive", not "liv" | `lˈaɪv` | B10 |
| "read" removed | past-tense "read" was voiced as "reed" (ɹˈiːd) in B04 and B09; reworded to "went through" / "put … side by side" | `—` | B04, B09 |

## Quotes: read exactly as written (verified verbatim in Mycroft's own files, 2026-10-04)

| Beat | Quote | Source |
|---|---|---|
| B02 | "both a book and a working agentic repository" | Mycroft README (upstream main @ f596c75) |
| B09 | "no artifact silently wins" | Mycroft SNICKERDOODLE.md, principle P6 |

## Deliberate echoes the lint flagged (your call by ear)

| Beat | Lines | Note |
|---|---|---|
| B01 | "Ask JavaScript… Ask Python…" and "Same number. Same request. Two answers." | deliberate parallels; they are the hook |
| B07 | "I moved… I swapped…" | deliberate: the two changes, side by side |
| B11 | "Nothing deleted. Nothing renamed." | deliberate pair |

## The script

### [0:00] B01 · COLD OPEN, one number, two answers

_Tone: curious, a little puzzled; let "Two answers." sit for a beat_

Here's one number. Zero point six two five. Ask JavaScript to round it to two decimal places, and you get zero point six three. Ask Python the same thing, the everyday way, and you get zero point six two. Same number. Same request. Two answers. I had just rewritten a finance detector from one of those languages into the other. So the question I couldn't put down was this. If my version had quietly done that somewhere, would I have noticed?

_On screen: two columns. Left `JavaScript: (0.625).toFixed(2)` → **"0.63"**. Right `Python: f"{0.625:.2f}"` → **"0.62"**._

> ☐ reads cleanly   ☐ note: ______________________

### [0:25] B02 · WHAT THIS IS

_Tone: friendly, plain; a contribution, not a boast_

Hi, this is Tanmay Kulkarni, in for Humanitarians AI. This week I worked on a contribution to My-croft, which describes itself as "both a book and a working agentic repository" for finance. Its recipes are reusable pipelines. I picked one, a contradiction detector, and rewrote its core logic from the original workflow's JavaScript into Python, so the recipe has scripts that run. This video is about one thing. How I checked that my version still says the same thing. It came down to three matches.

_On screen: presenter; the Mycroft README line (quote + source); the recipe name; the two columns labelled "original workflow (JavaScript)" and "my port (Python)"._

> ☐ reads cleanly   ☐ note: ______________________

### [0:52] B03 · THE DETECTOR, in one breath

_Tone: brisk and clear; the last line ("No real company is judged") said gently_

Here's what it does. It reads five kinds of evidence about a company. The guidance it gives on earnings calls, the risks it admits, the questions analysts pressed on, news sentiment, and engineering activity. Six patterns look for places where two of those disagree, and every disagreement becomes a flag for a person to review. To test it, I invented sixteen companies. Every name ends in "Fixture Co." No real company is judged in this video.

_On screen: five source cards → six pattern rows → a flag card marked "for human review"; a strip of fictional names (Alpha Fixture Co … Romeo Fixture Co)._

> ☐ reads cleanly   ☐ note: ______________________

### [1:16] B04 · MATCH ONE, the answers before the code

_Tone: patient; this is the slower, careful habit_

The first match is my own reading against the original. Before writing a single line of Python, I did something slower. I went through the original JavaScript, pattern by pattern, and wrote down the flags it should raise for each of those sixteen companies. Thirteen flags, written down first. Because if I write the expected answers after my code exists, I'll just write down whatever my code says, mistakes included.

_On screen: match 1 lights up: "my reading ↔ the original". `expected-flags.json` with its basis line highlighted: "Reasoned from the ORIGINAL JavaScript before any port existed". Counter: 16 companies · 13 flags._

> ☐ reads cleanly   ☐ note: ______________________

### [1:38] B05 · MATCH TWO, the first comparison

_Tone: the first turn: pleased, then honest doubt at "Then it started to bother me"_

The second match is the real comparison. My parity check takes the original JavaScript straight out of the workflow file. It runs it right beside my Python, on the same sixteen companies, and compares the two, field by field. Every flag, every sentence of evidence, word for word. Sixteen out of sixteen agreed. And that felt good for about a minute. Then it started to bother me. A match only tells you something if a mismatch could have shown up. So where could these two actually differ?

_On screen: match 2 lights up: "my Python ↔ the original JavaScript". Sixteen rows tick to **agree**. "16 / 16". Then the question holds on screen._

> ☐ reads cleanly   ☐ note: ______________________

### [2:05] B06 · THE SEAMS between the two languages

_Tone: explanatory, a little nerdy delight at the differences_

Some places, I knew about. JavaScript and Python don't always agree. That rounding tie is one. Another: JavaScript prints one point zero as just "one," while Python prints "one point zero." And a fallback written with two vertical bars keeps an empty list in JavaScript, where Python's "or" skips past it. A flag's wording carries numbers like these, so I made my Python copy JavaScript's behavior on each one, on purpose.

_On screen: three seam rows, JS | Python: `(0.625).toFixed(2)` "0.63" | "0.62"; `String(1.0)` "1" | `str(1.0)` "1.0"; `[] || "x"` `[]` | `[] or "x"` `'x'`. Then the port's three helpers: `js_to_fixed`, `js_str`, `js_or`, and a real flag from Quebec Fixture Co: `confidence=1` · `avg score 0.63`._

> ☐ reads cleanly   ☐ note: ______________________

### [2:28] B07 · WHERE MY TEST DATA NEVER STOOD

_Tone: the honest part: slower, no defensiveness; "It was doing its job" is relief, not excuse_

Here's the part I want to be honest about. To see whether my comparison would notice a difference, I made small changes to my own copy. I moved one threshold from zero point six to zero point six one. I swapped in Python's own rounding. And the comparison said everything still agreed. It was doing its job. My test companies just never stood on the line. Not one of them sat at exactly zero point six, and no news average landed exactly on a tie.

_On screen: the changed line in my copy (`>= 0.6` → `>= 0.61`), then the rounding swap; the comparison stays **agree** for every company. Label: "my copy, changed on purpose, scratch run"._

> ☐ reads cleanly   ☐ note: ______________________

### [2:55] B08 · STANDING ON THE LINE

_Tone: the fix lands: steady, then a small smile at "better test data"_

So I added two companies built to stand exactly there. Romeo Fixture Co gives guidance at a confidence of exactly zero point six. Quebec Fixture Co has a news average of exactly zero point six two five. Run the same two changes again, and each one fails on the company placed for it. The threshold, on Romeo. The rounding, on Quebec. The fix wasn't new code. It was better test data.

_On screen: two new rows: `FXR · confidence 0.60` and `FXQ · news average 0.625`. Re-run: threshold change → **FXR disagrees**; rounding change → **FXQ disagrees**._

> ☐ reads cleanly   ☐ note: ______________________

### [3:17] B09 · MATCH THREE, two files that were both mine

_Tone: closer to home: candid, owning it ("I wrote both of them")_

The third match was closer to home, because both sides were mine. At the last review, I put the human report side by side with its machine log, for the run that's designed to stop early on bad data. The report said thirteen rows were rejected. The log said zero. Same run, two different stories, and I wrote both of them. The log was only counting a later step, one that never got to run. My-croft's own rules say no artifact silently wins. So now one list feeds both files, anything that wasn't checked says "not checked," and a new test compares the two.

_On screen: match 3 lights up: "my report ↔ my log". Before: report "Rejects: 13", log `"rejects": []`. After: both 13; "Duplicates: Not checked: step 4 did not run". The P6 line with its source._

> ☐ reads cleanly   ☐ note: ______________________

### [3:50] B10 · WHERE I STOPPED

_Tone: calm and clear: stopping here is a decision, not an apology_

Everything you've seen ran on invented data. No database, no news feed, and no AI model was ever called. Live data, the model's answers, what happens when a real service times out: none of that is tested. So at the approval step, I declined live mode, on the record, and wrote down what would need to be true first. That call belongs to the people with live access.

_On screen: "sample data only · 0 live calls". The gate-5 record: `decision: deny`, its four preconditions._

> ☐ reads cleanly   ☐ note: ______________________

### [4:11] B11 · LEAVING IT AS I FOUND IT

_Tone: warm and careful: respect for a shared space_

And because this is a shared repository, I held myself to one rule. Add, never remove. Every change is a new file for this one recipe, or an update to this recipe's own page. Plus a few lines added to the end of two shared files. Nothing deleted. Nothing renamed. It's on my fork now, waiting for review.

_On screen: the GitHub comparison: "115 added · 3 modified · 0 removed · 0 renamed"._

> ☐ reads cleanly   ☐ note: ______________________

### [4:30] B12 · CLOSE, one question

_Tone: direct, to the viewer; slow down on the last sentence_

So if you've ever rewritten something you depend on, in a new language, a new tool, or just a cleaner version, here's the question I'd leave you with. Where would your two versions most likely disagree? Find that one spot, and make sure a single test is standing exactly on it.

_On screen: the two columns, with one marker placed exactly on the line between them._

> ☐ reads cleanly   ☐ note: ______________________

### [4:46] B13 · OUTRO

_Tone: warm sign-off_

Same Logic, Two Languages. Tanmay Kulkarni, in for Humanitarians AI. Signing off.

_On screen: title card._

> ☐ reads cleanly   ☐ note: ______________________

_Estimated runtime 4:50 (919 words at 3.17 words/s, the voice's measured pace). Kokoro audio becomes the master clock once generated, and cues are then timed on the Whisper clock._

Every sentence traces to `FACTCHECK.md` (refs under each beat in `SCRIPT.md`). The mechanical pass
(`gate_p_lint.py`): three over-long sentences (B03, B05, B11) are already split; the remaining flags are
the NAME checklist above, the echoes above, and bare decimals (they are values, not quantities with units).
