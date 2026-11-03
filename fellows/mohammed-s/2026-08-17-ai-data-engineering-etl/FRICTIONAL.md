# FRICTIONAL — ETL, Simplified

- **Folder:** `2026-08-17-ai-data-engineering-etl` · reporting week **2026-08-17 → 2026-08-23**
- **Dates inside this folder's artifacts:** built and GATE P signed 2026-08-30 · QC pass 2 2026-08-31
  (later than the reporting week — see the README evidence index)
- Append dated entries below; never rewrite an earlier one.

---

## Entry — week of 2026-08-17 · written later, on 2026-10-28

> Reconstructed after the fact from the files in this folder, not written at the time.
> Drafted with Claude Code from those files; reviewed and confirmed by Mohammed on 2026-10-28.

**1. Date and what I was working on**
- An explainer on how AI changes ETL. The topic was mine: *"how AI can be helpful in data
  engineering tasks… how ETL will be simplified."* Argument: AI collapses the glue, not the judgment.

**2. What I tried, and what I expected**
- An 11-beat sheet with a standalone E→T→L mechanism beat and five new Remotion scenes,
  each in both 16:9 and native 9:16.
- Expected the automated visual gate (Gate V) to be enough to catch layout defects.

**3. Where it resisted, and what I did next**
- Ran over 2:00. At GATE P the E/T/L beat was cut and its one load-bearing line folded into
  B01 → 10 beats, 1:59.99.
- Two renders were killed mid-step: B02 was left at its raw 30 s composition, and B03's
  correct clip was stranded in a temp file. Both were fixed by hand (`qc/NOTES-inflight.md`).
- **Gate V missed a real defect.** In 9:16 B03, the schema-diff header was half-buried under
  the first card — caused by my own earlier fix that pulled the cards up. Found only by
  looking at the frame. Also fixed 8 title-safe BLOCKERs (`EtlSpark` too high) and undersized
  type on B05. Re-rendered 8 beats, recompiled both masters → 0 BLOCKERs.

**4. What Claude or another person contributed — accepted, changed, rejected**
- Claude drafted the script, the scenes and the QC passes.
- Changed in fact-check: removed an invented "₹0.004 a row" drift figure, softened
  "transform is the only hard part", and cut an unsourced "afternoon instead of a fortnight"
  speed claim.
- Kept 8 `underfill` MAJORs after judging them by eye (title card, progressive reveal,
  the 9:16 platform-UI band) rather than inflating layouts to satisfy the metric.

**5. What I understand now, and what I still do not**
- Understood: a pipeline that runs is not a pipeline that is right — row-count
  reconciliation cannot see value drift (e.g. `float8 → numeric(12,2)`).
- Understood: an automated frame gate measures edge-bleed and fill, not collisions; frames have to be read.

**Evidence in this folder**
- [`qc/REPORT-final.md` — QC pass 2, 2026-08-31](qc/REPORT-final.md) · [`qc/NOTES-inflight.md`](qc/NOTES-inflight.md)
- [`FACTCHECK.md` — claim ledger and corrections](FACTCHECK.md) · [`PEDAGOGY.md` — GATE P signed 2026-08-30](PEDAGOGY.md)
- [`README.md` — change notes](README.md) · [`qc/contact_sheet.png`](qc/contact_sheet.png) · [`916/qc/contact_sheet.png`](916/qc/contact_sheet.png)
