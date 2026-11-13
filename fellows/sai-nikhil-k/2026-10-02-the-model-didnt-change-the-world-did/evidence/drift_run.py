"""drift_run.py — a model trained once, then left alone while the world moves.

    python3 drift_run.py > drift_run.out        # ~1 min, CPU, deterministic

Data: ELEC2 (Harries 1999; normalised by Bifet), OpenML dataset 151
"electricity", 45,312 half-hour rows from the New South Wales electricity
market, May 1996 – Dec 1998. Target: is the NSW price UP or DOWN relative to
its 24-hour moving average. File: ../data/electricity.arff (md5 checked below).

Protocol (fixed before looking at the result):
  * time is the row order: 48 rows a day, a "week" is 336 rows. (The file's
    normalised `date` column is not monotone at five rows, so it is not used,
    not even as a feature.)
  * FROZEN: one HistGradientBoostingClassifier (random_state=0) trained on the
    first 52 weeks, then never touched. Scored on every following 4-week block.
  * RETRAINED: the same recipe refit before each block on the 52 weeks just
    before it — what "retrain monthly" would have done.
  * Baselines per block: always predict the block's majority class (a ceiling
    for "always DOWN"-style guessing), and PERSISTENCE: predict the label of the
    previous half-hour — only possible because ELEC2's label arrives 30 min late.
  * Label-free alarm: the two-sample Kolmogorov–Smirnov statistic between the
    frozen model's scores P(UP) on its training year and on the block. Uses no
    labels from the block. Also KS on the NSW price input itself.
  * Features: day, period, nswprice, nswdemand — the New South Wales columns.
    The three Victoria columns (vicprice, vicdemand, transfer) are one constant
    fill until row 17,424, i.e. missing for all but the last day of the training
    year, so they are left out. (First pass used all seven; a check showed the
    frozen model had learned from that single day of Victoria data — its scores
    moved by up to 0.48 when those columns were reset. Both variants are printed
    at the end: the decay and recovery are the same either way.)
"""
import hashlib
import platform
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import scipy
import sklearn
from scipy.io import arff
from scipy.stats import ks_2samp, pearsonr
from sklearn.ensemble import HistGradientBoostingClassifier

HERE = Path(__file__).resolve().parent
ARFF = HERE.parent / "data" / "electricity.arff"
MD5 = "8ca97867d960ae029ae3a9ac2c923d34"          # OpenML's own checksum for file 2419
FEATURES = ["day", "period", "nswprice", "nswdemand"]
ALL_SEVEN = FEATURES + ["vicprice", "vicdemand", "transfer"]
TRAIN_WEEKS, BLOCK = 52, 4
ROWS_PER_WEEK = 48 * 7


def ks_by_hand(a, b):
    """sup_s |F_a(s) - F_b(s)| over the pooled sample points — the typeset D."""
    s = np.sort(np.concatenate([a, b]))
    fa = np.searchsorted(np.sort(a), s, side="right") / len(a)
    fb = np.searchsorted(np.sort(b), s, side="right") / len(b)
    return float(np.max(np.abs(fa - fb)))


def run(df, features):
    """Frozen vs retrained over every full block; returns the table and the frozen model."""
    train = df[df.week < TRAIN_WEEKS]
    frozen = HistGradientBoostingClassifier(random_state=0).fit(train[features], train.y)
    train_scores = frozen.predict_proba(train[features])[:, 1]
    rows = []
    for q in range(TRAIN_WEEKS, df.week.max() + 1, BLOCK):
        te = df[(df.week >= q) & (df.week < q + BLOCK)]
        if len(te) < ROWS_PER_WEEK * BLOCK:
            continue                                    # only full 4-week blocks
        win = df[(df.week >= q - TRAIN_WEEKS) & (df.week < q)]
        retrained = HistGradientBoostingClassifier(random_state=0).fit(win[features], win.y)
        s = frozen.predict_proba(te[features])[:, 1]
        ks_s = ks_2samp(train_scores, s).statistic
        assert abs(ks_s - ks_by_hand(train_scores, s)) < 1e-12
        rows.append({
            "after_wk": f"{q - TRAIN_WEEKS + 1}-{q - TRAIN_WEEKS + BLOCK}",
            "frozen": frozen.score(te[features], te.y),
            "retrained": retrained.score(te[features], te.y),
            "majority": max(te.y.mean(), 1 - te.y.mean()),
            "persistence": float((te.y.values[1:] == te.y.values[:-1]).mean()),
            "KS_score": ks_s,
            "KS_price": ks_2samp(train.nswprice, te.nswprice).statistic,
        })
    return pd.DataFrame(rows), frozen, train


def main():
    raw = ARFF.read_bytes()
    assert hashlib.md5(raw).hexdigest() == MD5, "electricity.arff is not OpenML's file"
    data, _ = arff.loadarff(ARFF)
    df = pd.DataFrame(data)
    for c in df.columns:
        if df[c].dtype == object:
            df[c] = df[c].str.decode("utf-8")
    df["day"] = df["day"].astype(int)
    df["y"] = (df["class"] == "UP").astype(int)
    df["week"] = np.arange(len(df)) // ROWS_PER_WEEK

    print("# drift_run — ELEC2, a frozen model vs the world")
    print(f"# python {platform.python_version()} · numpy {np.__version__} · pandas {pd.__version__} · "
          f"scipy {scipy.__version__} · scikit-learn {sklearn.__version__} · {platform.machine()}")
    print(f"# data: {ARFF.name} md5 {MD5} (matches OpenML) · rows {len(df):,} · weeks {df.week.max() + 1}")
    vic_from = int(np.argmax(df.vicprice.values != df.vicprice.values[0]))
    print(f"# vicprice/vicdemand/transfer are one constant fill until row {vic_from:,} "
          f"(week {vic_from / ROWS_PER_WEEK:.1f}) — Victoria's data only starts then")
    print(f"# date column decreases at rows {list(np.where(np.diff(df.date.values) < 0)[0])} — not used")

    t, frozen, train = run(df, FEATURES)
    print(f"# frozen model: features {FEATURES}, trained on weeks 0–{TRAIN_WEEKS - 1} "
          f"({len(train):,} rows), training accuracy {frozen.score(train[FEATURES], train.y):.3f}")
    print()
    print("## every full 4-week block after the freeze (accuracy; KS statistic D)")
    print(t.to_string(index=False, float_format=lambda v: f"{v:.3f}"))
    print()
    r_acc, p_acc = pearsonr(t.KS_score, t.frozen)
    worst = t.loc[t.frozen.idxmin()]
    print("## summary")
    print(f"  first block after the freeze: frozen {t.frozen.iloc[0]:.3f}")
    print(f"  worst block (weeks {worst.after_wk} after): frozen {worst.frozen:.3f}, "
          f"majority-class {worst.majority:.3f}, retrained {worst.retrained:.3f}, persistence {worst.persistence:.3f}")
    low = t[t.frozen < 0.75]
    print(f"  blocks with frozen < 0.75: {len(low)} of {len(t)} (weeks {low.after_wk.iloc[0]} … {low.after_wk.iloc[-1]} after)")
    print(f"  retrained beats frozen in {int((t.retrained > t.frozen).sum())} of {len(t)} blocks; "
          f"frozen beats retrained in {int((t.frozen > t.retrained).sum())}")
    print(f"  persistence range {t.persistence.min():.3f}–{t.persistence.max():.3f} (beats frozen in "
          f"{int((t.persistence > t.frozen).sum())} of {len(t)} blocks)")
    print(f"  KS on frozen scores: first block {t.KS_score.iloc[0]:.3f}, max {t.KS_score.max():.3f}, "
          f"last block {t.KS_score.iloc[-1]:.3f}")
    print(f"  Pearson r(KS_score, frozen accuracy) over {len(t)} blocks = {r_acc:.3f} (p = {p_acc:.1e})")
    t.to_csv(HERE / "drift_run.csv", index=False, float_format="%.4f")
    print()
    print("## robustness: the same protocol with all seven columns (Victoria included)")
    t7, frozen7, train7 = run(df, ALL_SEVEN)
    after = df[df.week >= TRAIN_WEEKS].copy()
    a = frozen7.predict_proba(after[ALL_SEVEN])[:, 1]
    for c in ("vicprice", "vicdemand", "transfer"):
        after[c] = train7[c].iloc[0]
    b = frozen7.predict_proba(after[ALL_SEVEN])[:, 1]
    print(f"  all-seven model: Victoria columns reset to their training fill moves its score by up to "
          f"{np.max(np.abs(a - b)):.2f} -> it DID learn from the one day of Victoria data in its training year")
    print(f"  all-seven frozen accuracy by block: {' '.join(f'{v:.3f}' for v in t7.frozen)}")
    print(f"  all-seven: first {t7.frozen.iloc[0]:.3f}, worst {t7.frozen.min():.3f}, "
          f"r(KS_score, acc) = {pearsonr(t7.KS_score, t7.frozen)[0]:.3f}, retrained wins {int((t7.retrained > t7.frozen).sum())} of {len(t7)}")


if __name__ == "__main__":
    main()
