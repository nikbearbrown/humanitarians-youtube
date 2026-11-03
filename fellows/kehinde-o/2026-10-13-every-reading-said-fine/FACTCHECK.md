# FACTCHECK — Every Reading Said Fine

Source of record: `github.com/Kenny0bi/real-time-vitals-pipeline`. Every figure was
**computed in this session** by running the repo's own simulator and scorer, not
taken from its README (docs/EXECUTABLE-EVIDENCE.md).

Reproduce: import `VitalsSimulator(num_patients=12, seed=42)` and
`calculate_mews_from_dict`, take the first patient whose deterioration is not NONE,
and score 1,800 generated readings.

| # | Claim | Beat | Verdict | Where it comes from |
|---|---|---|---|---|
| 1 | Twelve patients, one reading each per second | B00, B02 | TRUE | Simulator configuration |
| 2 | Nine of twelve stable, three deteriorating | B02 | TRUE | Measured: 9 NONE, 3 RESPIRATORY at seed 42 |
| 3 | Five parameters are scored per reading | B02, B03 | TRUE | `mews_calculator.py`: HR, SBP, RR, temperature, AVPU |
| 4 | Each parameter scores 0 to 3 points, summed | B03 | TRUE | `mews_calculator.py` scoring bands |
| 5 | Five or more points means immediate review | B03, B04 | TRUE | Published MEWS threshold, implemented in the scorer |
| 6 | The second rule flags beyond three standard deviations from the patient's own rolling mean | B03 | TRUE | `anomaly_detector.py`, Shewhart rule |
| 7 | Oxygen saturation fell from 98 to 80, eighteen points | B00, B04 | TRUE | Measured over 1,800 readings |
| 8 | 62 percent of readings still scored two or below | B04 | TRUE | Measured: 1,117 of 1,800 = 62.1 percent |
| 9 | Only 1.3 percent crossed immediate review | B04 | TRUE | Measured: 24 of 1,800 = 1.3 percent |
| 10 | Five or more consecutive readings moving one way is flagged as sustained drift | B05 | TRUE | `anomaly_detector.py`, trend rule |
| 11 | 101 tests pass | B06 | TRUE | Ran `pytest`: 101 passed, 1 skipped |
| 12 | The trace refreshes with a moving erase bar, not a scrolling window | B06 | TRUE | Interface implementation and README design note |

## Arithmetic stated in the reel
- 1,117 / 1,800 = 62.1 percent. Checked.
- 24 / 1,800 = 1.3 percent. Checked.
- 98 minus 80 = 18 points. Checked.

## Deliberately not claimed
- Every patient is synthetic. No real patient data exists anywhere in the project,
  and the reel states this on screen rather than only in the description.
- No clinical advice, and no claim that this system would detect a real
  deterioration earlier than a clinician would.
- This is not presented as a medical device or a deployed system.
- The peak score reached 6, so the reel says the threshold was crossed rarely
  rather than never.
