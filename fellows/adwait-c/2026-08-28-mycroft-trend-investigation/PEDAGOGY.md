# PEDAGOGY — Gate P (narration review before audio)

Weekly work video · 2026-08-28 · Mycroft Finance Investigator

## The one idea

**The feature compares three months. The engineering is that it tries fifteen separate times
to refuse before it will — and then ships the "why did this happen" field deliberately blank.**

A summary of the feature would lead with "it compares monthly EBITDA." That is the least
interesting true sentence about it. The week's actual work was the refusal surface and the
claim boundary, so that is what the video is about.

## HAI PM criteria

1. **Brutalist format** — `ai-explainer`, 13 beats, zero slates.
2. **4K at source** — 3840×2160.
3. **Both aspect ratios** — 9:16 derived via `./art shorts` after the 16:9 master locks.
4. **Formatting clean** — frame-level visual QC; both mono tables sized against a computed
   wrap budget.
5. **Intro line, verbatim** — *"Hi, I am Adwait Changan, and this video is about the
   multi-month trend investigation I built this week for the Mycroft Finance Investigator."*
6. **Real takeaway** — the viewer leaves with a rule they can apply to their own pipeline:
   list every number in your output, and ask what would have to be true for it to be wrong.
   B01 is the rule; BHTF makes them run it.

## PROOF compliance

- **Framework before examples** — B01 states the three admission conditions at ~22 s, before
  the first table appears at B03.
- **Falsifiability — B07, and it is real, not staged.** A recurrence detector that flags
  everything is worthless. `payroll` is favourable in all three periods and the same detector
  returns `NO`. That negative case is in the actual generated report; it is the control that
  makes the three `YES` results meaningful.
- **Side-by-side** — B03 holds all three periods in one frame; B07 holds all four categories
  in one frame. Nothing is compared in voiceover only.
- **Worked example** — B03 is the admission rule applied to three real runs.

## Structure (13 beats, ~4 min)

Hook with the intro line → **the admission rule** (B01) → how the engine re-derives rather
than re-reads (B02) → **the real EBITDA table** (B03) → the refusal surface (B04–B06,
including ten verbatim lines of the tamper check) → **falsifiability: payroll** (B07) → the
claim boundary and who owns "why" (B08–B09) → verdict → scaffolded task → outro.

## Honesty notes confirmed at this gate

- [x] **Every figure is copied from the generated report**, not from the PR summary prose:
      `reports/generated/mycroft-finance-investigator-trend-week35.md`. EBITDA 261,000 /
      230,000 / 265,000; movements −31,000 and +35,000; category impacts as tabled.
- [x] **"Fifteen refusal paths" was counted, not estimated** — `inspect.getsource(_load_run)`
      contains exactly 15 `raise TrendError` statements. The module has 30 in total; the
      narration says fifteen and scopes it to the loader, which is where they are.
- [x] **B05 is verbatim** via `inspect.getsource`, dedented only. Ten lines, as narrated.
- [x] **Synthetic data is named as synthetic**, the recipe is named as `DRAFT`, and the
      materiality threshold is named as an unapproved fixture — in B09 and again in the
      verdict. None of this is hidden to make the result sound stronger.
- [x] **No causal language anywhere.** The video says revenue, COGS and opex *recur*; it
      never says why, because the system does not and must not. B08 makes that the point
      rather than a disclaimer.
- [x] **No forecast language.** The report's own classification is
      `HISTORICAL_COMPARISON_NOT_FORECAST`; the narration matches it.

## Verdict

- Plan: APPROVED — 13/13 Remotion, zero slates, no consecutive pattern repeats.
- Narration: APPROVED — body beats 38–62 words.
- Fact-check (`FACTCHECK.md`): CLEARED.

> VERDICT: PASS (FINAL scope) — prepared by the build agent under the fellow's standing
> delegation. Unlocks audio and the clean master render. Does **not** authorize publishing,
> Drive upload, or notification.
