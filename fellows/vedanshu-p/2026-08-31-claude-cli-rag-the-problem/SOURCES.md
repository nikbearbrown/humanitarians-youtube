# SOURCES — Watch The Obvious Fix Fail.

## Book source

- Book: *RAG Foundations* (author: Vedanshu Daxesh Patel)
- Chapter: `chapters/02-the-problem.md` — "Chapter 2 — The Problem: Why LLMs Alone Aren't Enough"
- Same source as the sibling ai-explainer reel `2026-08-18-claude-rag-the-problem`;
  full citation list (Ji et al. 2023, Huang et al. 2023, Shuster et al. 2021,
  OpenAI 2023, Liu et al. 2024) carries over unchanged — see that reel's
  `SOURCES.md` for the complete bibliography. This reel makes no new citation
  claims; it demonstrates the chapter's own argument as runnable code instead
  of narrating it.

## Code (THE ACTUAL-CODE LAW — real, run, not fabricated)

- `code/naive_assistant.py` — toy fixed-snapshot assistant; written for this
  reel, run for real via `python code/naive_assistant.py`. Output captured
  verbatim into beat B04:
  ```
  Q: How many weeks of parental leave do I get?
  A: You get 8 weeks of parental leave.

  Q: What's the wellness stipend policy?
  A: You get 12 wellness days a year, plus a $500 stipend.
  ```
- `code/naive_bigcontext.py` — same scenario, "obvious fix" of pasting the
  full manual in and scanning it with an unranked first-match keyword scan;
  run for real via `python code/naive_bigcontext.py`. Output captured
  verbatim into beat B07:
  ```
  Q: How many weeks of parental leave do I get?
  A: Vacation policy: employees accrue 15 vacation days annually. Requests for leave should be submitted two weeks in advance.
  ```
- Both scripts are free, local, dependency-free (Python stdlib only) — no
  API calls, no cost, consistent with Fellow-tier "no money, ever."
- `naive_bigcontext.py`'s failure was not staged after the fact — the wrong
  paragraph (vacation policy, containing the words "leave" and "weeks") was
  identified as the predicted first match BEFORE running the script, then
  confirmed by actually executing it. This is a genuine property of the
  unranked first-match scan, not a cherry-picked bad run.

## Invented specifics (disclosed, per DOUBLE-CHECK LAW)

- The exact numbers (8 weeks → 16 weeks parental leave; "12 wellness days
  plus a $500 stipend"; the five MANUAL paragraphs and their order) are
  invented FOR THE DEMO CODE — the chapter itself gives no specific figures
  (it uses "a benefit," "a benefit that was discontinued last year," "page
  12"/"page 31" as placeholders). Used consistently across both scripts and
  matched to the parental-leave/wellness framing already established in the
  sibling `claude-cli-rag-introduction` reel's sick-leave demo (same book,
  same style of toy example), so the numbers don't contradict anything
  claimed elsewhere in the series.
- No model version number, context-length figure, or cutoff date is spoken
  anywhere in this reel.

## What this reel does NOT claim

- `naive_bigcontext.py`'s keyword scan is explicitly labeled in its own
  comments as a simplified stand-in for "nothing decides which passage
  matters" — it does not claim to reproduce how a real transformer attends
  over long context (the actual "lost in the middle" finding is Liu et al.,
  2024, cited in the sibling ai-explainer reel, not re-asserted here as a
  property of this toy script).
- Chapter 2 itself presents no fix — both B04 and B07 are honestly stamped
  `bad`. This reel does not manufacture a resolution the source text doesn't
  give; it ends on the chapter's own bridge to Chapter 3 (representation).

## Anecdote used as the running example (B00–B08)

- The parental-leave / wellness-stipend scenario is an original toy example
  built for this reel, in the same register as the chapter's own "benefit
  the company never offered" / "benefit that was discontinued" examples —
  not lifted from the chapter's text, which uses generic placeholders rather
  than a named benefit.
