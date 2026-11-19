# PROOF — Review Results: "Name It, Own It, Date It." (RAID log)

*Reviewed with the PROOF protocol from the rendered 4K frames + narration of both cuts.
Creator: for Sanjana / @HumanitariansAI. Genre: **cli-explainer** (project management), so the
full teaching rubric applies, plus the production gate and no-fabrication rules.*

---

## Verdict

**clear-for-public.** Production gate **PASS**. Teaching rubric **strong**. No fabrication.

> A genuinely useful one-move method: stop asking AI to "list the risks" and make it *classify* —
> Risk / Assumption / Issue / Dependency, each owned and dated. The film earns the insight the way
> a good teardown does: it shows the lazy move failing first (one flat "risk" pile), then the fix,
> and the re-sort visibly catches what the flat list buried — two "already-happening" items
> re-typed from Risk to **Issue**, a Dependency that was never a risk, and two assumptions nobody
> owns flagged in orange. The code on screen is the real `raid.py`, run against the real
> `status_update.txt`.

Both the **16:9** and **9:16** cuts earn the same verdict.

---

## Production gate (binary)

| Check | Result | Note |
|---|---|---|
| **Evidence legible at assertion** | **PASS** | Every card, lane header, owner/date and code line is readable as named. GATE T (min-size, contrast, overflow) passes on both cuts; GATE V (fill + edge-bleed) passes on both after the portrait lane-fit + B08 note fixes. |
| **Sources on screen** | **PASS** | The on-screen RAID board is the exact stdout of `src/raid.py` over `src/status_update.txt` (2 Risk · 2 Assumption · 2 Issue · 1 Dependency; 2 gaps). See `../FACTCHECK.md`. |
| **No fabrication** | **PASS** | No invented metrics. The RAID definitions are standard PM; the demo data is synthetic and labelled as such; owner names are fictional placeholders. |
| **Show over say** | **PASS** | The failure (flat pile) and the fix (four sorted lanes + flagged gaps) are *shown* animating, not just narrated. |
| **Native 4K** | **PASS** | 16:9 = 3840×2160, 9:16 = 2160×3840, 24 fps, H.264 `yuv420p` +faststart. |

---

## Teaching rubric

| Criterion | Score | Note |
|---|---|---|
| Framework before examples | **2** | B01 defines R/A/I/D and the owner/date rule *before* any data appears. |
| Show over say | **2** | The re-sort is the lesson; you watch lines move into the right lane. |
| One honest revision | **2** | v1 "list the risks" → v2 "classify" is a single, motivated change — not a highlight reel. |
| Falsifiability / limits | **2** | B08 names two real failure modes: the model mis-types vague wording (Issue vs Risk), and it can't invent an owner — verify tense and ownership. |
| Scaffolded task (your turn) | **2** | B09 hands Sanjana a copy-paste prompt and a weekly cadence. |
| Register / brand | **2** | Claude palette, one terracotta accent used structurally for the gaps only; @HumanitariansAI in the intro chrome, a corner bug throughout, and the outro card. |

---

## The one thing to watch

**The type is a judgment call, not a lookup.** The whole method rests on classifying correctly —
and "already happening" vs "might happen" is exactly where a model (or a tired PM) slips. The film
says this out loud in B08; keep that caveat in — don't let the clean four-lane board imply the
typing is automatic truth. Read the tense, confirm the owner.

## Do next (punch list)

1. **[OPTIONAL]** A follow-up could show the *weekly re-run* — carrying last week's RAID log
   forward, closing gaps, and promoting a Risk that became an Issue.
2. **[OPTIONAL]** Offer a one-line "RAID health" check: % of items with an owner and a date.

## What works (keep)

- **The re-type reveal.** Moving the staging-server and analytics lines out of "risks" into
  **Issues** is the most convincing single moment — it proves classification beats listing.
- **Gaps as structure, not decoration.** Terracotta marks only the unowned/undated items.
- **Honest limit stated**, so the method doesn't oversell.
- **Legible and on-brand** at native 4K in both aspects; portrait holds all four lanes.

---

### Scorecard

| | 16:9 | 9:16 |
|---|---|---|
| Production gate | PASS | PASS |
| Teaching rubric | strong | strong |
| No fabrication | PASS | PASS |
| Verdict | clear-for-public | clear-for-public |
| Resolution | 3840 × 2160 | 2160 × 3840 |
