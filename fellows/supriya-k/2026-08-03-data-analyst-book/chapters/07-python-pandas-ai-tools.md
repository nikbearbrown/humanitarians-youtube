# Chapter 7 — Python & pandas for Analysts (+ AI Tools)

When the coding round wants Python, it usually wants **pandas**: load, clean, group, summarize, answer. This chapter also covers a question that's new to 2026 loops — *how do you use AI tools responsibly?*

> **What's tested here**
> A small data problem solved end-to-end in pandas, narrated clearly — plus judgment about when to trust AI-generated code.

## pandas in one screen

**pandas is a Python library for data manipulation and analysis.**[^pd] Two structures do the work:[^pd]
- **`Series`** — a 1-D labeled array.
- **`DataFrame`** — a 2-D labeled table; each column is a `Series` and can hold a different type. Built from dicts, arrays, or files (CSV, Excel, JSON, SQL).

Core operations you'll use constantly:[^pd]
- **Filter:** `df[df['col'] > 5]`
- **Group:** `df.groupby('key').agg(...)` (split-apply-combine)
- **Join:** `df.merge(other, on='key', how='left')`
- **Sort:** `df.sort_values('col', ascending=False)`

> **Limitation to mention:** pandas holds data in RAM and doesn't parallelize across cores or optimize query plans — fine for interview-sized data, not for billions of rows.[^pd]

## SQL ↔ pandas

Same question, two tools. "Revenue by city" is `GROUP BY city` in SQL and `df.groupby('city')['revenue'].sum()` in pandas. Being able to move between them is a strong signal.

## Working with AI tools (2026)

Interviewers now ask how you use tools like ChatGPT or Cursor. What they're listening for is **judgment — not abstinence, not blind trust.**[^trends7]

- **Lean on it** for boilerplate, syntax recall, and first drafts.
- **Read it line by line** when correctness matters — AI output can pass a surface smell test and still be subtly wrong (a filter applied after an aggregation, a silent type coercion).[^trends7]
- **What to say:** "I use AI to draft, then I verify against the data and check edge cases before I trust the result."

## Worked example

An invented **library-checkouts** CSV. Find the **top 5 books by checkouts among users who joined in 2025**:

```python
import pandas as pd

df = pd.read_csv("checkouts.csv", parse_dates=["user_joined", "checked_out"])
joined_2025 = df[df["user_joined"].dt.year == 2025]
top5 = (joined_2025
        .groupby("book_title")
        .size()
        .sort_values(ascending=False)
        .head(5))
```

Now an **AI-generated version** filtered *after* grouping — counting all users, then slicing — which quietly answers the wrong question. Spotting that is the skill.

![The correct pipeline (filter, then count) beside an AI version that filters after grouping — the misplaced step highlighted.](images/07-python-pandas-ai-tools-fig-01.png)

## Exercises

1. **(Warm-up.)** Use `groupby` to get **average session length per platform** from a described DataFrame.
2. **(Representative.)** Reproduce this SQL in pandas: `SELECT city, SUM(revenue) FROM sales GROUP BY city`.
3. **(Stretch.)** Given AI-generated pandas code for a stated task, decide whether to trust it, find any bug, and write two sentences you'd tell an interviewer about your AI-use approach.

---

*Next:* the round that rewards thinking over computing — the case/business interview.

[^pd]: Wikipedia, "pandas (software)," https://en.wikipedia.org/wiki/Pandas_(software) (accessed 2026-07-15).
[^trends7]: `blueprint-trends-notes.md` (2026 guides).
