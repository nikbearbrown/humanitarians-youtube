# Half the Data Is Fake: Catching AI Junk Before It Hits Your Pipeline — Kavya Mehta

STEM/AI topic film for the Humanitarians AI weekly submission (`docs/FELLOWS-SUBMISSION.md`).
It comes in two native exports: 16:9 at 3840×2160 and 9:16 at 2160×3840.

## This week's contribution

- **Question:** when a batch arriving at a pipeline is half junk, the kind a careless AI-assisted
  backfill, a bot or a scraper produces, what should stop it before it reaches the dashboard?
- **Prediction:** checking properties of the data (provenance, value ranges, near-duplication) will catch
  most of it without trying to detect AI-written text, which can't be done reliably.
- **What I built/tried:** `demo/junk_gate_demo.py`. Twenty synthetic rider-feedback rows, exactly half of
  them junk: templated near-duplicate comments, impossible values, rows with no source. The same batch is
  loaded twice, once with no checks and once through a validation gate that quarantines rows instead of
  deleting them.
- **Observed result:**
  - With no gate, all 20 rows load and the average rating reads **4.30**.
  - With the gate, **9** rows are quarantined (3 no source, 4 out of range, 2 near-duplicates) and the
    average drops to **3.55**. The true average of the real rows is **3.40**.
  - **One junk row (id 202) still passed.** Its identical twin was rejected for a different reason first,
    so the first copy of the template was never compared.
- **Next experiment:** fix the ordering gap by running the near-duplicate check across all rows,
  including rejected ones. Then run the gate on a real CabStream batch and see which rule catches the most.

## Human and AI work

- **My decisions, implementation and verification:** I chose the topic. I drafted the script with help
  from Claude Code and reviewed the demo output and the rendered frames.
- **AI tools/voices used and what they generated:** Claude Code helped draft the beat sheet and write the
  demo script and these docs. Kokoro `am_onyx` (local text-to-speech) generated the narration. It is a
  synthetic voice, disclosed in B00 and on the B08 card.
- **What I rejected or corrected:** the first run reported only "quarantined 9", which hid that one junk
  row got through. The demo now prints the row that slipped and the true average, so the video states the
  gate's miss instead of implying it caught everything.
- **What remains unverified or failed:** the data is synthetic, so the result shows the method, not a
  real-world junk rate. The gate does not detect AI-written text; fluent, plausible fakes would pass it.

## Reproduce

- **Brutalist version/commit and date checked:** `b21f6253a336098f3f55847a9525ae6868ccbdb7` (2026-10-10),
  plus local scene changes (`HarnessParts`, `HarnessTerminal`, `HarnessBoundaryCard`, see `toolkit-changes/`).
  Checked 2026-10-29.
- **Source commit used for this export:** add after committing this folder.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16),
  `demo/junk_gate_demo.py`.
- **Commands:** see `BUILD-PROMPT.md`. There are no external inputs.
- **Checks:** `FACTCHECK.md` (fact-check gate clean), `CHECKS-REPORT.md`, `SHOTLIST.md`, `PROMPTS.md`,
  `SOURCES.md`, `BUILD-LOG.md`, `TYPECHECK.md`, `_qc/REPORT.md`.

## Watch and review

- Landscape — 3840×2160 — 2:26.4 — SHA-256 `8e52da12ea5edad8773dd5ec16c8016a1e543e9c83c870802953eb3c79279820`
- Vertical — 2160×3840 — 2:26.4 — SHA-256 `cdf5e7feb21af120c606368286df2773f27d53126f63838a325b129a9454fbf6`
- Drive folder: https://drive.google.com/drive/folders/1YhX5prPlG97izfShV5QS5-tVPJLIN_Cf
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending
