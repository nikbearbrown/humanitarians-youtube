# Beat Sheet (APPROVED — Gate P, 2026-08-30): "The Update That Almost Lied About What It Sent"

**Creator:** Sai Pranavi Jeedigunta | Weekly work report
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo, `scripts/regulatory-intel/`)
**Phase:** 2 — approved for narration lock / audio generation. Both open FACTCHECK items resolved
2026-08-30: B05's forward-looking framing approved as written; the "12" count was re-verified live
at build time (21:04) rather than shipped as the original `A7-VERIFICATION.md` snapshot — identical
12 ids confirmed. See `FACTCHECK.md`.

---

## Premise

**What this covers:** one specific fix from this week's continued Layer 1 hardening pass on the
same pipeline as the 2026-07-26 report: the "Mark email sent" Postgres node was re-deriving its
own copy of "what counts as high-priority" instead of reading it from the node that actually built
the email — and that copy had silently drifted from the real rule. Chosen because it has a clean,
measured before/after (12 real rows in the live table right now that the old query would have
wrongly flipped) and a sharp, general lesson: a step that re-derives someone else's rule is a
second copy of the truth waiting to drift.

**What this deliberately leaves out:** the still-open B2 (source misclassification) and B3
(Google News link unwrapping — confirmed this week to be a bigger scrape-based task, not a quick
fix) are candidates for a future report, not this one.

**Source status:** Real engineering work. Every number below traces to
`/Users/pranavijs/mycroft/scripts/regulatory-intel/A7-VERIFICATION.md` (2026-08-30) and
`logs/RUN_LOG.md`'s two 2026-08-30 entries. See `SOURCES.md` for the full claim → source mapping.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated, matches program's fixed format |
| B03 Setup | The two rules side by side: `urgency_score > 6` (High Priority Filter) vs. the old `urgency_score > 7 OR impact_level IN (...)` (Mark email sent) | Both conditions legible simultaneously, not sequential |
| B04 Discovery | `determineImpactLevel()` snippet, the `isEnforcement` bypass line highlighted | The exact line that lets impact_level outrun urgency_score |
| B05 Proof | Live query + row count (12) + one real example row on screen | Number and query both visible, not narration-only |
| B06 Fix | Before/after SQL, `id = ANY($1::int[])` highlighted | Full before AND after query visible together |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi Jeedigunta |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "The Update That Almost Lied About What It Sent" + @HumanitariansAI. No narration.

**B01. Exec summary (~0:04–0:18)**
VO: "Hi, I'm Sai Pranavi Jeedigunta. This video is about a database update in the same regulatory
pipeline from last week — one that could mark high-priority alerts 'emailed' even when no email
had actually gone out for them — and the fix that scoped it to only what was actually sent."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:18–0:28)**
VO: "In that same pipeline, I found a step whose only job is to record 'this got emailed' — and it
was using its own copy of the rule for what counts as high-priority, instead of checking what the
email step had actually sent."
Visual: the "Mark email sent" node, isolated, with a question mark over its condition.

**B03. Setup (~0:28–0:48)**
VO: "The alert path is simple: insert the item, filter for anything with an urgency score above
six, build an email from exactly those rows, send it, then mark those rows sent. Two steps decide
what 'high priority' means here — and they were supposed to agree."
Visual: two condition boxes side by side — `urgency_score > 6` (High Priority Filter, feeds the
email) vs. the old `urgency_score > 7 OR impact_level IN ('Critical','High')` (Mark email sent).
*[Source: `A7-VERIFICATION.md` "The bug" section]*

**B04. Discovery (~0:48–1:08)**
VO: "Here's why they didn't agree. The scoring node sets impact level from the score — except for
one shortcut: if the text matches an enforcement or fraud keyword, it jumps straight to High or
Critical, no matter how low the score is. So an item scoring five or six can still read
'Critical' — low enough that the email filter would never pick it up, but high enough that the old
update would still flip it to 'sent.'"
Visual: the `determineImpactLevel()` function, the `isEnforcement` / `isFraud` bypass line
highlighted in the same color as the mismatch arrows from B03.
*[Source: `A7-VERIFICATION.md` "Why the two rules disagree"]*

**B05. Proof (~1:08–1:28)**
VO: "I queried the live table for exactly that mismatch. Twelve real rows, right now — including
an actual SEC enforcement action, 'SEC Charges 21 Individuals With Alleged Wide-Reaching Insider
Trading Scheme' — that the email filter would never select, but that the old query would have
silently marked sent the next time it ran."
Visual: query on screen, result count "12", one example row (id 153) shown with its title,
urgency_score (5), and impact_level (Critical).
*[Source: `A7-VERIFICATION.md` "Live measurement (2026-08-30)" — full 12-row table there.
NOTE for FACTCHECK: forward-looking claim only — "would have," not "were."]*

**B06. Fix (~1:28–1:48)**
VO: "The fix: stop re-deriving the rule. Read the exact ids the email step already produced, and
only mark those sent."
Visual: before/after SQL sitting together — old blanket `WHERE` clause vs. new
`WHERE id = ANY($1::int[])`, id source (`High Priority Filter` node) annotated.
*[Source: `A7-VERIFICATION.md` "Fix"; commit `03ad1e0` in `mycroft`]*

**B07. Takeaway (~1:48–2:03)**
VO: "A step that copies someone else's rule instead of reading their output isn't wrong today.
It's wrong the day the two drift apart — and by then nothing threw an error to tell you."
Visual: statement card.

**B08. Sign-off (~2:03–2:08)**
VO: "Fixed with Claude Code, verified against the live table before it ever ran again in
production."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi Jeedigunta.

---

## Production Gate Self-Check (pre-review)

- [x] Both conditions (B03) legible on screen simultaneously, not sequential cuts
- [x] The `isEnforcement` bypass line (B04) is the actual code, not paraphrased
- [x] The "12" claim (B05) is on screen as a number tied to a visible query, not narration-only
- [x] B05 narration says "would have," not "were" — forward-looking claim only (see FACTCHECK.md)
- [x] At least one real, non-noise example row named and legible (SEC insider-trading case)
- [x] Before/after SQL (B06) both visible together
- [x] Silent title card present; brand/fellow sign-off card present

**Estimated runtime:** ~2:08 draft estimate. **Measured runtime: 121.46s (2:01.46)**, from Kokoro
`af_bella` audio (B00 silent 4.05s + B01-B08 measured narration), per the toolkit's audio-first
rule. 16:9 master renders at 121.41s (4K, 3840x2160).

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-08-30. Both FACTCHECK open items
resolved (see `FACTCHECK.md`). Cleared to generate Kokoro audio and proceed to previz.

---

## Production complete — 2026-08-30

Audio locked, `scenes.py` authored (9 Manim scenes), 4K master rendered and GATE V clean
(0 BLOCKER, 0 MAJOR), 9:16 short built with hand-authored portrait relayouts and GATE V clean
(0 BLOCKER, 2 MAJOR — both on the toolkit's auto-generated silent END card only). See
`BUILD-LOG.md` for the full build record and `README.md` for the production-state summary.
Deliverables: `Mycroft_SaiPranaviJeedigunta_20260830_16x9.mp4`,
`Mycroft_SaiPranaviJeedigunta_20260830_9x16.mp4`. Publishing NOT authorized (per task scope).
