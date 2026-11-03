# FRICTIONAL — Prove The Number Changed.

- **Folder:** `2026-09-14-data-contract-simulation` · reporting week **2026-09-14 → 2026-09-20**
- **Dates inside this folder's artifacts:** build authorised and beat sheet 2026-08-31
  (before the reporting week — see the README evidence index)
- Append dated entries below; never rewrite an earlier one.

---

## Entry — week of 2026-09-14 · written later, on 2026-10-28

> Reconstructed after the fact from the files in this folder, not written at the time.
> Drafted with Claude Code from those files; reviewed and confirmed by Mohammed on 2026-10-28.

**1. Date and what I was working on**
- A 2:06 `cli-explainer` reel about the metric-impact simulation I added to the data
  contract agent in Mycroft (`Data_Quality_Agent/`, branch `feature/metric-impact-simulation`,
  commit `4469968`).

**2. What I tried, and what I expected**
- Showed the real `simulate.py` code and the test suite's own assertions. The revision
  cycle (B05–B07) is the actual design problem: a schema change (`amount_cents → amount`)
  that compiles and passes tests but leaves `fct_mrr` 100× low.

**3. Where it resisted, and what I did next**
- Narration said "three models go red"; the measured `as_is_failures` is **four**
  (`stg_subscriptions` fails, three marts are blocked behind it). Corrected, and B04 lists
  all six models.
- B07's average was invented in the first draft; replaced with the value implied by the
  published pair (108,176.33 / 1,152 = 93.90).
- An interrupted render left B05 at 30.06 s instead of 13.14 s. The compile would have
  stretched it silently; caught by auditing every beat's duration against its mp3.
- B01 first rendered half-empty; type enlarged and re-checked.
- The Windows cp1252 console killed long runs on em dashes; prefixing scripts with
  `PYTHONIOENCODING=utf-8` fixed it.

**4. What Claude or another person contributed — accepted, changed, rejected**
- Claude built the sheet (`build_sheet.py`), scenes and QC. GATE P was signed by
  delegation in-session on 2026-08-31.
- Accepted a `type-on` motion warning (54% of beats) as structural to the explainer format.
- Left `x0.01` rendering as `X0.01` as cosmetic.

**5. What I understand now, and what I still do not**
- Understood: the only honest warning about a schema change is to rebuild the marts and
  measure; the claim worth making is the *ratio*, which the test asserts and the data can't change.

**Evidence in this folder**
- [`QC.md` — visual QC, 0 BLOCKER / 0 MAJOR](QC.md) · [`qc/master_t62.png`](qc/master_t62.png) · [`qc/916_B01_t13.png`](qc/916_B01_t13.png)
- [`SOURCES.md` — file-level sources and corrections](SOURCES.md) · [`PEDAGOGY.md`](PEDAGOGY.md) · [`README.md`](README.md)
- Code: `mdhussainshariff/Mycroft` commit `4469968` (branch `feature/metric-impact-simulation`)
