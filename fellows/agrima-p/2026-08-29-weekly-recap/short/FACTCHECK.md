# FACTCHECK — weekly-recap/short

This Short is a full 16:9 -> 9:16 reformat of the parent reel (no beats were
cut — the parent is under the 3:00 Shorts cap). Every claim here is
identical to the parent's; see the parent `FACTCHECK.md` for the full
disclosure. Summary:

1. **"Published the AI nonprofit marketing article, with research behind
   it."** — user-supplied. Venue not specified, so "published this week" is
   used rather than inventing a platform name.
2. **"Produced the accompanying video (16:9 + 9:16)."** — independently
   true within this session: the `ai-nonprofit-marketing` reel was actually
   built, through the full pipeline, in both cuts.
3. **"Suffolk University talk, with Yatra, this Wednesday."** — user-
   supplied (a confirmed guest-speaker engagement); no invented details.
4. **"Two team meetings attended this week."** — user-supplied, mentioned
   in narration (B02) as context; not given its own visual card.

## THE ACTUAL-CODE LAW — code beats are real, not invented

`weekly_recap_v1.py` and `weekly_recap_v2.py` are genuine Python scripts in
the parent reel folder, both actually run to capture the CODE/OUTPUT beats'
real source and output — reused unchanged in this Short (same mp3s, same
Remotion props, portrait-rewired):

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

## Correction note

This file was updated to match the parent's corrected content (see the
parent `beat_sheet.json` metadata.note) — it previously still described the
original fashion-sustainability framing after the correction, which was a
gap; caught and fixed before pushing to GitHub.
