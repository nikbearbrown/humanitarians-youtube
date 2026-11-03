# Sources

## Primary source

This report documents the author's own project ("Mycroft") — an n8n workflow that turns public
Hacker News discussion into a per-company Buzz Score and a Groq-generated Community Opinion
summary, backed by a Postgres database and a live dashboard. There is no external primary source
to cite: the narration describes the author's own pipeline, its formulas, a real bug and fix, and
a real limitation the author found in their own data.

## Asset provenance

Every still (`media/B03.png`–`B17.png`, sourced from `pantry/`) is the author's own screenshot of
their own n8n workflow canvas, Supabase/Postgres data, or dashboard UI. Per each beat's
`media/*.source.txt` sidecar:

> URL: n/a — own screenshot from the author's n8n workflow / Supabase / dashboard
> License: own work
> Credit: not required (own project material)

No external rights clearance is needed — unlike an explainer that uses NASA/NOIRLab-style
licensed archive imagery, every visual here is the author's own product.

## Provenance rule

Narration is limited to claims about the author's own system: its architecture, its formulas
(e.g. the four capped Buzz Score components), a specific real bug (Groq strict-JSON-mode
rejecting quote-heavy comments) and its fix, and a specific real limitation found in production
(the Bento/Show HN misattribution case). See `FACTCHECK.md` for why these claims are
author-asserted rather than independently source-checked, and what that means for review.
