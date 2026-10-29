# /hai Weekly Report — Week 6

| | |
|---|---|
| **Volunteer** | Kavya Mehta · AI Data Engineer · OPT, 20 hrs/week |
| **Profile** | [humanitarians.ai/kavya-mehta](https://www.humanitarians.ai/kavya-mehta) |
| **Project** | Brutalist (Humanitarians AI) · Manager: Jash |
| **Reporting week** | 2026-10-19 to 2026-10-25 |
| **Status** | Prepared with Addams from project evidence · confirmed by the volunteer on 2026-10-29 |

## Executive summary

Two videos were produced for this week: a topic explainer, *Half the Data Is Fake: Catching AI Junk
Before It Hits Your Pipeline* (2:26, 9 beats), and *CabStream, Week 3 Progress* (2:23, 8 beats). The
explainer's demo loads a half-junk batch with and without a validation gate, and reports the one junk row
the gate missed. The progress video covers the night CabStream's pipeline actually ran on Databricks. It
is explicit that the 1.57B-row total comes from my commit message, not a re-run count.

## Work completed

| Artifact | Link | Status |
|---|---|---|
| Topic explainer | [STEM WEEK 6](https://drive.google.com/drive/folders/19Y1_PpiDstUkySnQ4UQaIBI9EBJNWJEg) | Final |
| Progress video | [PROGRESS WEEK 6](https://drive.google.com/drive/folders/1m1U4j_JEu6FWTMhRIYnP5hk5NPQaFvaD) | Final |

**What the demo showed:** 20 synthetic rider-feedback rows, exactly half of them junk.
- **No gate:** all 20 rows load, and the average rating reads **4.30**.
- **Through the gate:** **9** rows are quarantined (3 no source, 4 out of range, 2 near-duplicates), and
  the average drops to **3.55**. The true average of the real rows is **3.40**.
- **One junk row (id 202) passed.** Its identical twin was rejected for a different reason first, so its
  text was never recorded for comparison.

**Progress video:** four commits on 2026-06-29:
- the Databricks cluster (auto-terminate) and a Key Vault secret scope
- a fix for a provider bootstrapping error
- a fix adding `prevent_destroy` to storage
- the Bronze ingestion and Silver processing notebooks: 1.57B rows and 252.3M rows, as described in the
  commit message

## Tier justification

| Activity | Tier | Argument |
|---|---|---|
| Producing both videos with Claude Code | **Tier 1** | AI-drafted production is AI fluency. |
| Explaining why row 202 slipped through | **Tier 5** | The miss comes from rule order, not from the near-duplicate rule. Rejecting a row before recording its text means its copy is never compared. Tracing the cause to the order of checks shows what would have happened otherwise: run the duplicate check on every row, and 202 is caught. |
| Keeping the miss in the video | **Tier 3 · Tier 4** | The first demo run printed only "quarantined 9", which implied the gate caught everything. Making it print the row that slipped and the true average shows the method's limit to viewers instead of overselling it. |
| Quarantine instead of delete | **Tier 3** | Deleting suspect rows removes them from any later review. Quarantining keeps a person in the decision about what data counts, including real rows a rule might flag wrongly. |
| `prevent_destroy` on CabStream storage | **Tier 5** | Compute is destroyed every session to save cost, but Bronze/Silver/Gold Delta tables are written once and read forever. Without `prevent_destroy`, one `terraform destroy` would erase the data along with the cluster. The fix separates what can be rebuilt from what can't. |
| Not repeating 1.57B as verified | **Tier 4** | The total is stated in a commit message, not re-counted. What the code does verify is one known month first (Jan 2023, checked against a local count of 3,066,766 rows) before scaling up. The video says exactly that and no more. |

## Struggle and friction

**Topic video:**
- The first demo run hid the gate's miss (see above). It was kept and reported, not tuned away.
- The landscape render chain died before the last beat with a Windows "fork: resource temporarily
  unavailable" error. It left an orphaned ffmpeg holding about 3.2 GB, and B08 failed once more until that
  process exited.
- In portrait, B05 sat exactly on the frame-fill threshold at its midpoint, so its footer was brought in
  0.6 s earlier.

**Progress video:** two infrastructure bugs, both fixed the same night:
- a provider bootstrapping error from dynamic data sources (removed)
- storage that `terraform destroy` would have wiped (`prevent_destroy` added)

## Hours (confirmed)

| Research | Exploration | Building | Review/QC | Documentation | Meetings | Total |
|---|---|---|---|---|---|---|
| 6 | 4 | 4 | 2 | 3 | 1 | 20 |

## Tools

- **Claude Code:** used.
- **Gru:** not used yet. The storage-vs-compute lifecycle decision is SDD material.
- **CRITIQ:** not used yet.

## Reflection

1. **Which gate rule would catch the most junk in CabStream?** Range checks are the first candidate. In a
   trip feed, the rows to test first are zero-minute trips, zero distance with a non-zero fare, negative
   fares, and pickup times after drop-off. Running the gate on one month of Bronze would show which rule
   actually fires most.
2. **How much should the 1.57B figure be trusted right now?** As a stated number, not a measured one. The
   only checked anchor is January 2023 (3,066,766 rows). A `COUNT(*)` on the Bronze Delta table, compared
   with the commit message, would turn it into a verified figure.

## Next steps

- **Next week:** run `COUNT(*)` on the Bronze and Silver Delta tables and compare with the 1.57B / 252.3M
  stated in the commit.
- **Next week:** fix the gate's ordering gap: compare text against every row seen, including rejected ones.
- **Next week:** run the validation gate on one month of CabStream Bronze, and record which rule catches
  the most.
