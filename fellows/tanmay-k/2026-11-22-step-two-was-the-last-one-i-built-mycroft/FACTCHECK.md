# FACTCHECK — work video (angle A, "Step Two Was the Last One I Built")

Method: exported the merged repo (`git archive fef5caa`) to a scratch folder, made a second copy, and in the copy changed `504.5625` to `540.5625` in `sample/clean/NVDA.json` (the manifest untouched). Ran steps 1, 2, 3 and 5 on both with the repo's own scripts, sample mode, `--now 2026-10-10T00:00:00+00:00` for steps 1/3/5. Nothing in the repository was touched.

| Claim in the narration | Rerun result | Verdict |
|---|---|---|
| Clean set: step 5 total 65,098.13, cost 53,800.00, return 21.00% | `step 5 pass … 65098.13 … gain 11298.13 (21.00%)` | confirmed |
| Tampered: step 1 stops, naming the file | `step 1 stop: fixture changed since the manifest froze it: clean/NVDA.json` | confirmed |
| Tampered: step 3 passes, five promoted, none rejected | `step 3 pass: 5 promoted, 0 rejected` | confirmed |
| Tampered: step 5 total 66,898.13, +1,800.00, return 24.35% | `66898.13 … gain 13098.13 (24.35%)`; 66,898.13 − 65,098.13 = 1,800.00 | confirmed |
| Step 2 on tampered: four ingested, one turned away, hash mismatch | `set clean: 4 ingested, 1 rejected`; audit: differs from the SHA-256 frozen in manifest.json (frozen 2633560d6573, found 41b042800dad) | confirmed |
| Step 2 on clean: five ingested, none rejected | `set clean: 5 ingested, 0 rejected` | confirmed |
| Six sets: step 2 vs step 3 file counts | step 2 ingested+rejected: clean 5+0, defective 4+1, quality-duplicate 6+0, quality-far 5+0, quality-missing 4+0, quality-move 5+0; step 3 looked at 5, 5, 6, 5, 4, 5 files (defective: 0 promoted, 5 rejected) | confirmed: same files each time |
| Six fixture sets | `sample/` holds clean, defective, quality-duplicate, quality-far, quality-missing, quality-move (+ two manifests) | confirmed |
| Step 3 reads no provenance record | `grep -ci provenance` on the step 3 script at the merge commit: 0 | confirmed (B06) |
| Step 3 also checks the ticker is in the portfolio and the price is a finite number above zero | step 3 script contract, read at the merge commit | confirmed (B08 says so) |
| Recipe text at merge still says step 2 / step 4 "is still open" | recipe lines 64 and 76 | confirmed (B11 relies on this) |
| Step 5 reads step 3's records, not step 4's | recipe line 76 | confirmed |
| Merged PR adds 19 files, 1,964 lines | `git diff --stat 2ccd74e fef5caa` | confirmed |
| NVDA digits 504.5625 → 540.5625 | edit above | confirmed |

Not rerun: the self-test's 28 checks (cited from `logs/portfolio-price-fetcher/ingest-self-test-results.md`, not by this pass); commit ids 4c9d10f / fef5caa / 894be6c are read from `git log`.
Limits stated in the film: sample mode, invented prices, one pair swapped, one file, one recipe; no live call.

Note: step 3 still reads the sample folder directly; it does not consume step 2's output (the recipe is unedited). B07 says wiring that is the next change.
