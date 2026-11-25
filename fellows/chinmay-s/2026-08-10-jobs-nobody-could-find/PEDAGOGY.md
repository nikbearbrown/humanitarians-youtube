# PEDAGOGY — The Jobs Nobody Could Find (deep-explainer, claude-liam / Onyx)

A 5–7 minute documentary teardown built from a 12-week OPT engineering ship
log (`SOURCES.md` → addams.pdf, Humanitarians.ai / Jobsekr). The subject is the
ENGINEERING, not the person: two production systems, and one integrity rule
that governs both the code and the log itself.

## Thesis
A job board had 23,000 real listings that international students effectively
could not find. Two systems fixed that — a five-tier visa classifier and a
technical-SEO stack — and the through-line that makes the story worth telling
is the same rule in both places: **information is added, never overwritten**
(the no-data-only promotion guarantee in the data; the honest coda in the log).

## Act structure (deep spine — bookends fixed)
- B00 cold open (`ClaudeComposerAsk`) — Liam signs in, ask lands answered ✓
- ACT I (B01–B08) — the visa pipeline: problem → migration/cron → backfill →
  audit → the 5th (company) tier → overwrite-safety → close.
- ACT II (B09–B16) — the SEO system: invisibility → JSON-LD → page wiring →
  sitemap tree → landing pages → FAQ snippets → close.
- ACT III (B17–B22) — index + honest coda: Search Console → audit to ≥90 →
  end-to-end verify → handoff/docs → the stalled transition week.
- B23 VERDICT recap (`ClaudeVerdictArtifact`) → B24 YOUR TURN
  (`ClaudeComposerAsk`, "Your turn.") → B25 TITLE re-read (`ClaudeTitleOutro`) ✓
- IN-FOR-BEAR LAW: B00 "this is Liam, in for Bear"; B25 "Liam, in for Bear." ✓
- Each act opens on a Title-Case segment card (B01/B09/B17) ✓

## Beat-mix contract (body beats B01–B22, bookends/close exempt)
Target: vox ~20–25%, manim ~25–40%, remotion ~30–45%, cards remainder.
- VOX (5): B02, B10, B18, B21, B22  → ~23% ✓ (in-band)
- MANIM (4): B03, B04, B13, B19
- REMOTION (7): B05, B06, B07, B11, B12, B14, B15, B20  (B07 own-graphic)
- CARD (4): B01, B08, B09, B16, B17 (act cards + mini-verdicts)
No more than 2 consecutive same-lane body beats except intended.

## Evidence discipline (every claim traces to the source ship log)
| Claim in narration | Source (addams.pdf) | Verdict |
|---|---|---|
| Migration never run → 23K jobs all untagged until wk 1 | Wk 1 Exec Summary / Primary Objective | OK |
| Idempotent migration (IF NOT EXISTS), 15-min cron, secrets vs prod | Wk 1 Work Completed | OK |
| Backfill: page 1,000 at a time, batch write, 23K in <2 min | Wk 1 Work Completed | OK |
| Tag-distribution audit + sanity checks (no US untagged / no foreign tagged) | Wk 1 Claude Artifact | OK |
| 5th tier = company_has_sponsored from sponsorship history | Wk 2 Exec Summary / Work Completed | OK |
| no_data-only promotion; description always wins | Wk 2 Work Completed + Claude Artifact | OK |
| JobPosting JSON-LD: required + recommended + safe defaults | Wk 3 Work Completed | OK |
| Canonical, noindex for expired, robots.txt public/private split | Wk 4 Work Completed | OK |
| Sitemap index → jobs/companies/landing/pages; 50K shard; active-only | Wk 5–6 Work Completed | OK |
| 30 cities × 15 roles landing pages, server-rendered live data | Wk 7 Work Completed | OK |
| Per-page FAQ + FAQPage JSON-LD to beat duplicate-content | Wk 8 Work Completed | OK |
| Search Console verify + submit + request indexing; warnings appear | Wk 9 Work Completed | OK |
| Lighthouse ≥90; fix JobPosting/FAQ warnings at root | Wk 10 Work Completed | OK |
| End-to-end scrape → is_us_job → classify → indexable page → sitemap → GSC | Wk 11 Work Completed | OK |
| Docs + handoff so systems outlive the author | Wk 11 Work Completed | OK |
| Coda: AI+1 onboarding blocked, no access/task, hours below 20, reported straight | Wk 12 (partial/transition) | OK |

## Taste / sensitivity notes
- Register is Teardown of the BUILD, never of the person. No individual names
  in narration ("the PM", "another engineer"), even though the source names
  some — this is a local, non-publishing previz regardless (rule 6).
- Vendor/tool specifics (Supabase, Next.js, Google for Jobs, JSON-LD) are kept
  because they ARE the subject of this particular teardown; the DOUBLE-CHECK
  "strip the datable" law is relaxed for a project-specific demo, noted here.

## Gates remaining after this one
- Gate D1: first compile is a full-length SLATE PREVIZ (expected — pantry
  stills for the 5 vox beats not yet sourced).
- Gate D2: `SHOPPING.md` written AFTER audio lock (durations are real by then).

VERDICT: PASS — human signed GATE P on 2026-07-28 (narration reviewed and
approved before audio generation).
