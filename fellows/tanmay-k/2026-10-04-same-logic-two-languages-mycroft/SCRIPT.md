# SCRIPT: *Same Logic, Two Languages* (Week 25 work video, Mycroft recipe contribution)

**Draft 3, 2026-10-04** (PROOF pre-production fixes 1–5 applied; B11's last sentence removed at Tanmay's request after the stills review: no "on my fork, waiting for review" line). Angle B, approved by Tanmay 2026-10-04 (see ANGLE.md). Structure: THREE MATCHES. Two columns
are on screen throughout, the original JavaScript (left) and my Python (right); each act adds a match that must hold.
About 880 words, roughly 5:00 at the voice's measured pace.

**Framing:** every gap in this film is in my own work (my test data, my report step). The original workflow is "the
original workflow": no author named, no faults listed. Humble, first person on the genuine turns (B05, B07, B09).

**TTS spelling:** numbers in words in the narration; digits and code names on screen only. "My-croft" is a respelling for Kokoro (it says MICK-roft otherwise); captions and on-screen text use "Mycroft".

---

### B01 · COLD OPEN, one number, two answers
> Here's one number. Zero point six two five. Ask JavaScript to round it to two decimal places, and you get zero point six three. Ask Python the same thing, the everyday way, and you get zero point six two. Same number. Same request. Two answers. I had just rewritten a finance detector from one of those languages into the other. So the question I couldn't put down was this. If my version had quietly done that somewhere, would I have noticed?

*On screen:* two columns. Left `JavaScript: (0.625).toFixed(2)` → **"0.63"**. Right `Python: f"{0.625:.2f}"` → **"0.62"**. *Refs:* L1.

### B02 · WHAT THIS IS
> Hi, this is Tanmay Kulkarni, in for Humanitarians AI. This week I worked on a contribution to My-croft, which describes itself as "both a book and a working agentic repository" for finance. Its recipes are reusable pipelines. I picked one, a contradiction detector, and rewrote its core logic from the original workflow's JavaScript into Python, so the recipe has scripts that run. This video is about one thing. How I checked that my version still says the same thing. It came down to three matches.

*On screen:* presenter; the Mycroft README line (quote + source); the recipe name; the two columns labelled "original workflow (JavaScript)" and "my port (Python)". *Refs:* R1, C1, C2.

### B03 · THE DETECTOR, in one breath
> Here's what it does. It reads five kinds of evidence about a company. The guidance it gives on earnings calls, the risks it admits, the questions analysts pressed on, news sentiment, and engineering activity. Six patterns look for places where two of those disagree, and every disagreement becomes a flag for a person to review. To test it, I invented sixteen companies. Every name ends in "Fixture Co." No real company is judged in this video.

*On screen:* five source cards → six pattern rows → a flag card marked "for human review"; a strip of fictional names (Alpha Fixture Co … Romeo Fixture Co). *Refs:* C3, C4.

### B04 · MATCH ONE, the answers before the code
> The first match is my own reading against the original. Before writing a single line of Python, I did something slower. I went through the original JavaScript, pattern by pattern, and wrote down the flags it should raise for each of those sixteen companies. Thirteen flags, written down first. Because if I write the expected answers after my code exists, I'll just write down whatever my code says, mistakes included.

*On screen:* match 1 lights up: "my reading ↔ the original". `expected-flags.json` with its basis line highlighted: "Reasoned from the ORIGINAL JavaScript before any port existed". Counter: 16 companies · 13 flags. *Refs:* C5.

### B05 · MATCH TWO, the first comparison
> The second match is the real comparison. My parity check takes the original JavaScript straight out of the workflow file. It runs it right beside my Python, on the same sixteen companies, and compares the two, field by field. Every flag, every sentence of evidence, word for word. Sixteen out of sixteen agreed. And that felt good for about a minute. Then it started to bother me. A match only tells you something if a mismatch could have shown up. So where could these two actually differ?

*On screen:* match 2 lights up: "my Python ↔ the original JavaScript". Sixteen rows tick to **agree**. "16 / 16". Then the question holds on screen. *Refs:* C6.

### B06 · THE SEAMS between the two languages
> Some places, I knew about. JavaScript and Python don't always agree. That rounding tie is one. Another: JavaScript prints one point zero as just "one," while Python prints "one point zero." And a fallback written with two vertical bars keeps an empty list in JavaScript, where Python's "or" skips past it. A flag's wording carries numbers like these, so I made my Python copy JavaScript's behavior on each one, on purpose.

*On screen:* three seam rows, JS | Python: `(0.625).toFixed(2)` "0.63" | "0.62"; `String(1.0)` "1" | `str(1.0)` "1.0"; `[] || "x"` `[]` | `[] or "x"` `'x'`. Then the port's three helpers: `js_to_fixed`, `js_str`, `js_or`, and a real flag from Quebec Fixture Co: `confidence=1` · `avg score 0.63`. *Refs:* L1, L2, L3, C7.

### B07 · WHERE MY TEST DATA NEVER STOOD
> Here's the part I want to be honest about. To see whether my comparison would notice a difference, I made small changes to my own copy. I moved one threshold from zero point six to zero point six one. I swapped in Python's own rounding. And the comparison said everything still agreed. It was doing its job. My test companies just never stood on the line. Not one of them sat at exactly zero point six, and no news average landed exactly on a tie.

*On screen:* the changed line in my copy (`>= 0.6` → `>= 0.61`), then the rounding swap; the comparison stays **agree** for every company. Label: "my copy, changed on purpose, scratch run". *Refs:* C8.

### B08 · STANDING ON THE LINE
> So I added two companies built to stand exactly there. Romeo Fixture Co gives guidance at a confidence of exactly zero point six. Quebec Fixture Co has a news average of exactly zero point six two five. Run the same two changes again, and each one fails on the company placed for it. The threshold, on Romeo. The rounding, on Quebec. The fix wasn't new code. It was better test data.

*On screen:* two new rows: `FXR · confidence 0.60` and `FXQ · news average 0.625`. Re-run: threshold change → **FXR disagrees**; rounding change → **FXQ disagrees**. *Refs:* C8, C9.

### B09 · MATCH THREE, two files that were both mine
> The third match was closer to home, because both sides were mine. At the last review, I put the human report side by side with its machine log, for the run that's designed to stop early on bad data. The report said thirteen rows were rejected. The log said zero. Same run, two different stories, and I wrote both of them. The log was only counting a later step, one that never got to run. My-croft's own rules say no artifact silently wins. So now one list feeds both files, anything that wasn't checked says "not checked," and a new test compares the two.

*On screen:* match 3 lights up: "my report ↔ my log". Before: report "Rejects: 13", log `"rejects": []`. After: both 13; "Duplicates: Not checked: step 4 did not run". The P6 line with its source. *Refs:* C10, C11, R2.

### B10 · WHERE I STOPPED
> Everything you've seen ran on invented data. No database, no news feed, and no AI model was ever called. Live data, the model's answers, what happens when a real service times out: none of that is tested. So at the approval step, I declined live mode, on the record, and wrote down what would need to be true first. That call belongs to the people with live access.

*On screen:* "sample data only · 0 live calls". The gate-5 record: `decision: deny`, its four preconditions. *Refs:* C12.

### B11 · LEAVING IT AS I FOUND IT
> And because this is a shared repository, I held myself to one rule. Add, never remove. Every change is a new file for this one recipe, or an update to this recipe's own page. Plus a few lines added to the end of two shared files. Nothing deleted. Nothing renamed.

*On screen:* the GitHub comparison against Mycroft's main branch: "115 added · 3 modified · 0 removed · 0 renamed". *Refs:* C13.

### B12 · CLOSE, one question
> So if you've ever rewritten something you depend on, in a new language, a new tool, or just a cleaner version, here's the question I'd leave you with. Where would your two versions most likely disagree? Find that one spot, and make sure a single test is standing exactly on it.

*On screen:* the two columns, with one marker placed exactly on the line between them. *Refs:* —.

### B13 · OUTRO
> Same Logic, Two Languages. Tanmay Kulkarni, in for Humanitarians AI. Signing off.

*On screen:* title card. *Refs:* —.
