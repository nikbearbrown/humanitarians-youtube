# FRICTIONAL — Bond Pricing and Duration: Price-Yield Curve with Claude

- **Folder:** `2026-08-10-bond-pricing` · reporting week **2026-08-10 → 2026-08-16**
- **Dates inside this folder's artifacts:** `beat_sheet.json` 2026-08-30
  (later than the reporting week — see the README evidence index)
- Append dated entries below; never rewrite an earlier one.

---

## Entry — week of 2026-08-10 · written later, on 2026-10-28

> Reconstructed after the fact from the files in this folder, not written at the time.
> Drafted with Claude Code from those files; reviewed and confirmed by Mohammed on 2026-10-28.

**1. Date and what I was working on**
- A reel on bond pricing, Macaulay/modified duration and convexity for a hypothetical
  $1,000, 5% coupon, 10-year bond, with Claude writing `bond_pricer.py` on screen.

**2. What I tried, and what I expected**
- Started from the sibling `claude-for-finance/bond-pricing-duration` project and expected
  to reuse its numbers.
- Revision cycle planned: duration-only estimate → add convexity → show the error shrink.

**3. Where it resisted, and what I did next**
- The sibling project's numbers did not check out. Price at 2% was claimed as ≈ $1,404;
  recomputed it is **$1,269.48**. Its "Macaulay duration 7.7 years" was actually the
  *modified* duration (Macaulay is **8.11**), and its code then divided by 1.05 a second time.
  Every figure was recomputed from the closed-form formulas instead (`FACTCHECK.md`).
- Visual QC (`qc/REPORT.md`) flagged **22 BLOCKER** `edge-bleed` frames — every sampled frame,
  all at the top-right edge — while the Manim layout audit found 0 errors.
  These were fixed (confirmed by me on 2026-10-28); the fix is not recorded in `qc/REPORT.md`,
  which still shows the earlier run.
- Two stock clips were slowed 3.1× and 3.6× to fill their beats; logged for replacement
  in `replace_log.md`, not replaced.

**4. What Claude or another person contributed — accepted, changed, rejected**
- Claude wrote the beat sheet, `scenes.py`, and the recomputation in `FACTCHECK.md`.
- Rejected: the prior project's figures.
- GATE P was **not** signed by me: under a "proceed without pausing" instruction, Claude
  self-audited as a stand-in, and `PEDAGOGY.md` says I had not yet watched the cut.
  I watched the finished cut afterwards (confirmed 2026-10-28).

**5. What I understand now, and what I still do not**
- Understood: the difference between Macaulay and modified duration, and why convexity
  closes most of the gap (+2% shock: duration-only off by $13.96, with convexity off by $1.04).
- Open: the primary-source citation (Macaulay 1938) was never fetched; the futures-hedge and
  callable-bond lines in the handoff are textbook extensions with no verified figures.

**Evidence in this folder**
- [`FACTCHECK.md` — recomputed figures and the correction](FACTCHECK.md)
- [`qc/REPORT.md` — Gate V visual QC](qc/REPORT.md) · [`qc/contact_sheet.png`](qc/contact_sheet.png)
- [`layout_audit.md` — 0 errors over 19 snapshots](layout_audit.md) · [`replace_log.md`](replace_log.md)
- [`PEDAGOGY.md` — Claude self-audit, not a human sign-off](PEDAGOGY.md)
