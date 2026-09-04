# FACTCHECK — weekly-recap

Every claim in this reel is the user's own first-person account of their own
real week, supplied directly in the build request — not sourced from any
external article, dataset, or third party (other than the video's own
companion reel, `ai-nonprofit-marketing`, which this session actually
built). Nothing here is independently verifiable by the toolkit beyond that,
so every beat is treated as first-person testimony, not a measured/sourced
claim, per the DOUBLE-CHECK LAW (NO FABRICATION, strip anything that could
date the video).

## Claims and their status

1. **"Published the AI nonprofit marketing article, with research behind
   it."** — user-supplied. The article and its underlying research are real
   within this session — see `Articles/ai-nonprofit-marketing-article.md`
   and the `ai-nonprofit-marketing` reel's own FACTCHECK.md, which
   attributes its statistics to three named sources (Planetary Labour, Slam
   Media Lab, Gigawatt Group). The user did not specify where the article
   was published, so this reel says "published this week" rather than
   naming a platform — no venue is invented.
2. **"Produced the accompanying video (16:9 + 9:16)."** — independently
   true within this session: the `ai-nonprofit-marketing` reel was in fact
   built this session, through the full pipeline (kickoff prompt, plan
   files, gates), and delivered in both 16:9 and 9:16 cuts.
3. **"Suffolk University talk, with Yatra, this Wednesday."** — user-
   supplied. Presented as the user's own statement (a confirmed guest-
   speaker engagement); no additional details (topic, time, room, audience
   size) are invented beyond what the user stated.
4. **"Two team meetings attended this week."** — user-supplied, mentioned
   in narration (B02) as context for the "done" side of the week; not given
   its own visual card, to keep the three-card structure clean (matching
   the original build's design).

## No fabricated numbers or named entities

No statistics, percentages, or dates are asserted anywhere in this reel
beyond what the user supplied or what the companion `ai-nonprofit-marketing`
reel already fact-checked. "This Wednesday" is used as relative framing per
the user's own words, not stamped to a specific calendar date.

## THE ACTUAL-CODE LAW — code beats are real, not invented

`weekly_recap_v1.py` and `weekly_recap_v2.py` are genuine Python scripts in
this reel folder. Both were **actually run** (not hand-typed as fake output)
to capture the CODE/OUTPUT beats' real source and real terminal output:

```
$ python3 weekly_recap_v1.py
- Published the AI nonprofit marketing article, with research behind it  (published this week)
- Produced the accompanying Brutalist video (16:9 + 9:16)  (brutalist.art)
- Suffolk University talk, with Yatra  (this Wednesday)

$ python3 weekly_recap_v2.py
DONE THIS WEEK
  - Published the AI nonprofit marketing article, with research behind it  (published this week)
  - Produced the accompanying Brutalist video (16:9 + 9:16)  (brutalist.art)
STARTING NEXT WEEK
  - Suffolk University talk, with Yatra  (this Wednesday)
```

The B03/B06 CODE beats show this real source (trimmed to the lines that
teach); the B04/B07 OUTPUT beats visualize this real output, not invented
data.

## Correction note

This reel's content was fully replaced per a corrected kickoff prompt (see
beat_sheet.json metadata.note) — the original build's fashion-sustainability
framing is gone, not layered underneath. This FACTCHECK.md reflects only the
corrected, currently-shipping content.
