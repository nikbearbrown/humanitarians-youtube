"""evals.py — why you cannot review every run, and what to do instead.

Runnable, no dependencies, no API key. The numbers shown in the video are
printed by this file.

HONESTY NOTE: this is arithmetic about review capacity and sampling, not a
benchmark of any agent. It shows what sampling can and cannot tell you.
"""
from __future__ import annotations

SECONDS_PER_REVIEW = 90


def review_hours(runs_per_day: int, seconds: int = SECONDS_PER_REVIEW) -> float:
    """Human hours per day to read every run."""
    return runs_per_day * seconds / 3600


def missed_probability(failure_rate: float, sample: float) -> float:
    """Chance a failing run is NOT in a random sample of that fraction."""
    if not 0 <= failure_rate <= 1 or not 0 <= sample <= 1:
        raise ValueError("rates must be between 0 and 1")
    return 1 - sample


def undetected_failures(runs: int, failure_rate: float, sample: float) -> float:
    """Failing runs per day that nobody looks at."""
    return runs * failure_rate * (1 - sample)


if __name__ == "__main__":
    print("WHAT REVIEWING EVERY RUN COSTS")
    print(f"{'runs/day':>9}  {'human hours/day':>16}")
    for runs in (10, 100, 1000, 10000):
        print(f"{runs:>9}  {review_hours(runs):>16.1f}")

    print("\nSAMPLING 5% OF A 2% FAILURE RATE")
    print(f"{'runs/day':>9}  {'failures':>9}  {'reviewed':>9}  {'unseen':>7}")
    for runs in (100, 1000, 10000):
        f = runs * 0.02
        print(f"{runs:>9}  {f:>9.0f}  {f*0.05:>9.1f}  "
              f"{undetected_failures(runs, 0.02, 0.05):>7.1f}")

    print("\nDOES A BIGGER SAMPLE FIX IT?  (1000 runs/day, 2% failing)")
    for s in (0.05, 0.25, 0.50, 1.00):
        print(f"  sample {s:>4.0%}  ->  {undetected_failures(1000, 0.02, s):>5.1f} "
              f"failures unseen,  {review_hours(int(1000*s)):>5.1f} human hours/day")
