# Week 25 work video: angle B, "Checking my own version"

**Status: approved by Tanmay, 2026-10-04** (angle B; B09 kept; title *Same Logic, Two Languages*).

**Subject (plain words):** I rewrote the core of one Mycroft recipe, a detector that flags where a company's own
statements and outside signals about it disagree, from the original workflow's JavaScript into Python. This film is
about one question: **how do I know my version still says the same thing?**

**Working title (subject-first):** *I Rewrote It in Python. Does It Still Say the Same Thing?*
Alternatives: *Same Logic, Two Languages* · *Where My Copy Could Have Drifted*

---

## The angle

> **Two versions agreeing only counts where they had a chance to disagree.** My Python matched the original
> JavaScript on all 16 test companies the first time, and that was the least informative moment of the whole build.
> The useful work was finding the places where two versions *could* quietly drift apart: where the two languages
> behave differently, where a threshold sits, where two of my own files describe the same run. Then I put a test
> case standing exactly on each one. My own checking found three such places I had missed; each is fixed and now
> guarded.

**What the viewer leaves with (the reusable move):** before you trust a match, ask *where could these two differ?*,
and make sure at least one test stands exactly there.

**Why it fits Mycroft:** its constitution says an artifact may never silently win over its source (P6). A port is
only allowed to differ from its source on purpose, so you have to be able to *see* a difference if one appears.

## Structure: three pairs that must agree (shape taken from the subject)

The film is built as a translation. On screen, two columns: the **original JavaScript** on the left, **my Python** on
the right. Each act adds a pair that has to agree, and asks where that pair could drift:

1. **My reading ↔ the original** (I wrote the answers down before writing code)
2. **My Python ↔ the original JavaScript** (the language seams, and the threshold edge)
3. **My report ↔ my own log** (two of my own files, describing one run)

It ends on where I stopped checking, and a single open question. No numbered rubric, no "your turn" checklist.

| # | Beat | What it shows | Evidence (committed files) |
|---|---|---|---|
| B01 | Cold open | One number, 0.625. JavaScript rounds it to "0.63"; Python rounds it to "0.62". Same logic, two languages, two answers. "If my rewrite had done that inside a finance report, would I have noticed?" | `FIXTURE_MANIFEST.md` (FXQ); live run of both |
| B02 | What this is | Presenter. Mycroft in its own words; one recipe; I rewrote its detector in Python as my contribution. The question of the film | Mycroft `README.md`; the recipe |
| B03 | The detector in one breath | Five sources, six patterns, flags for a human. Shown with the fictional companies ("… Fixture Co"), so no real company is ever judged | recipe; `sample/clean/` |
| B04 | Pair 1: answers before code | Before writing any Python, I read the JavaScript and wrote down the 13 flags it should raise across 16 invented companies. Why: if I write expectations after the code, I just copy my own mistakes | `expected-flags.json` (basis field) |
| B05 | Pair 2: the first run | Python vs the original JavaScript, run side by side under Node: 16/16 agree, word for word. Then the turn: "That felt good for about a minute." A match only tells you something where a mismatch was possible | `…-parity-check.py` |
| B06 | The seams between languages | Where JS and Python differ: `a \|\| b`, rounding a tie, printing 1.0 as "1". My port imitates JavaScript on each, on purpose | `…-run-approved-tools.py` (`js_or`, `js_to_fixed`, `js_str`) |
| B07 | What my test data never visited | The honest part. I changed my own copy on purpose in small ways (0.6 → 0.61; Python rounding) to see whether the comparison would notice, and it **didn't**. Not because the check was weak: none of my 16 companies stood on the line. No one sat at exactly 0.6; no average landed on a tie. *(Kept short; boundary W21 B06 / W23 B11)* | self-test section B |
| B08 | Standing on the line | Two new companies: Romeo (FXR) at exactly 0.60, Quebec (FXQ) at exactly 0.625. Now each change is caught. The fix was test **data**, not code | `FIXTURE_MANIFEST.md` (FXQ, FXR); self-test B (3/3 caught) |
| B09 | Pair 3: my own two files | At the last review (gate 6), I read the report beside its machine log. On the run that stops early, the report said **13** rejected rows and the log said **0**. Same run, two stories, both mine. One list now feeds both, and a new check compares them | commit `d9cd514`; self-test section G |
| B10 | Where I stopped | Everything here is sample data. Live data, the model call, live failures: not tested, and I declined live mode on the record. The people with live access decide what's next | gate-5 and gate-6 records |
| B11 | Leaving it safe | A shared repo: everything added, nothing removed; the result is on my fork, waiting for review | GitHub compare (0 removed, 0 renamed) |
| B12 | Close | One open question: "If you rewrote something you rely on, where would the two versions most likely disagree, and does any of your tests stand exactly there?" | — |
| B13 | Outro | — | — |

Estimated ~4.5–5 minutes, about 700 words of narration.

**Short (9:16, one complete arc):** the 0.625 cold open → "they agreed on everything, and that told me almost
nothing" → no company stood on the line → two companies placed exactly on it → the takeaway question. Name in the
opening and closing frames, as in the 16:9.

## Framing rules

1. **No critique of anyone else's work.** The original workflow is "the original workflow": no author named, no
   faults listed. Every gap in this film is in **my** work: my test data, my report step.
2. **My gaps are evidence the checking worked.** Each is shown with its fix and the check that now guards it,
   never as a gotcha.
3. **Humble register.** "This is how I tried to check it, and what it caught", not "I proved". First person on the
   genuine turns (B05, B07, B09) only.
4. **Cite committed files only.** No workshop tools on screen (`build_fixtures.py`, `check_safe_diff.py`).
5. **No fellows named or compared.**
6. **Years and numbers in words** for Kokoro; "zero point six", "zero point six two five".

## Uniqueness audit (narration of every earlier work video: W15–W24, 10 films)

| Idea | Earlier hits | Verdict |
|---|---|---|
| Rewriting code in another language and checking it against the original | **0** | new (thesis) |
| Writing the expected answers before writing any code | **0** (W19 B06 "wrote down that I'd defined them" is about labelling inventions) | new |
| Language seams: rounding a tie, `\|\|`, number-to-text | **0** | new |
| Two of my own output files disagreeing about one run | **0** (W22 B04/B09 "two lists allowed to disagree" is a design choice, not a defect) | new |
| Contributing to someone else's repo | **0** | new |
| A deliberately broken version still passes | **W21 B06** ("one line moved… every output assertion still passes"), **W23 B10–B11** ("attack it on purpose") | **boundary:** B07 stays short, and its point is different: the inputs never stood on the line (test *data*), not what the tests assert (W21) or malformed input (W23). Avoid "break", "attack", "gently" |
| Coverage | **W20 B10** ("What's narrower is the coverage") | **boundary:** avoid the word "coverage"; say "where my test data stood" |
| "A check is more convincing when you watch it catch something" | **W20 B13** | avoid that phrasing |
| A step that never ran / "stayed dark" | **W21** (whole film), **W19 B09** | **boundary:** B09 is about two files disagreeing; the "not checked vs zero" detail stays a single line, without "dark" |
| "receipt", "fails closed", "on purpose" as a signature | W24, W19 B08, W24 B09–B10 | avoid "receipt" and "fails closed"; use "on purpose" at most once (B06) |

## To verify before the beat sheet (FACTCHECK)

- B01: re-run both roundings live on screen (already confirmed: JS "0.63", Python "0.62"; JS prints 1.0 as "1").
- B07/B08: **verified 2026-10-04** on a scratch copy of commit `d9cd514`. With FXQ and FXR removed, the comparison
  says 14/14 agree for the real port, for 0.6 → 0.61, and for Python rounding: neither change is noticed. With them
  back, the real port is 16/16, and each change fails exactly one company: 0.61 → FXR, Python rounding → FXQ.
  (Reproducible on screen; the committed self-test section B records the "with" half.)
- B04: confirm `expected-flags.json` says it was written before the port.
- B09: the numbers 13 and 0 from the previous version of the defective-run files (in commit `dd60da6`).

## Decisions for Tanmay

1. **Approve the angle** ("agreement only counts where it could have failed"; three pairs), or redirect.
2. **Title:** *I Rewrote It in Python. Does It Still Say the Same Thing?* (recommended), or an alternative.
3. **B09 (report vs log):** keep it as the third pair (recommended: it's the freshest, and fully my own), or drop it
   for a tighter film.
4. **The PR:** open it before the video goes up, so the description can link it?
