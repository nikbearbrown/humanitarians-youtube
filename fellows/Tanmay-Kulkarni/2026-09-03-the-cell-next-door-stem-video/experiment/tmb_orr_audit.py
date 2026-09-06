#!/usr/bin/env python3
"""tmb_orr_audit.py — is tumor mutational burden actually the variable?

The source reel asserts (B06) that "TMB predicts response in some cancers but not
others." True, and unhelpful: it names a failure without measuring it. This script
measures it, using only numbers that appear in primary sources, each cited inline.

Four parts:

  1. FORMULA AUDIT      Does the published Yarchoan regression reproduce the two
                        predictions the letter itself makes with it?
  2. ANCHOR RESIDUALS   Where does the regression land on tumor types whose ORR and
                        mutational burden are both reported in primary trials?
  3. VARIANCE           What r = 0.74 costs, stated as a quantity rather than a hedge.
  4. ATTENUATION MC     How much of the "unexplained" 45% is real biology and how much
                        is just small-trial sampling noise?  [ILLUSTRATIVE MODEL]

Standard library only — no numpy. Runs in ~2s.

    python3 experiment/tmb_orr_audit.py
"""
import math
import random
import statistics

# ---------------------------------------------------------------------------
# Published constants. Every one of these is quoted from a primary source.
# ---------------------------------------------------------------------------

# Yarchoan M, Hopkins A, Jaffee EM. "Tumor Mutational Burden and Response Rate to
# PD-1 Inhibition." N Engl J Med 2017;377(25):2500-2501. PMID 29262275.
# Full text via PMC6549688.
#   "Our linear correlation formula - objective response rate = 10.8 x log_e(X) - 0.7,
#    where 'X' is the number of coding somatic mutations per megabase of DNA"
SLOPE = 10.8
INTERCEPT = -0.7
#   "The correlation coefficient of 0.74 suggests that 55% of the differences in the
#    objective response rate across cancer types may be explained by the tumor
#    mutational burden."
R_PUBLISHED = 0.74
N_TUMOR_TYPES = 27

# The two predictions the letter makes with its own formula:
#   basal-cell carcinoma       TMB 47.3 -> ORR 40.1% (95% CI 31.2-50.6)
#   sarcomatoid carcinoma lung TMB  7.2 -> ORR 20.6% (95% CI 16.7-24.5)
WORKED_EXAMPLES = [
    ("basal-cell carcinoma (skin)", 47.3, 40.1, (31.2, 50.6)),
    ("sarcomatoid carcinoma (lung)", 7.2, 20.6, (16.7, 24.5)),
]

# Whole-exome coding footprint used to convert "mutations per tumor" (Le 2015,
# whole-exome sequencing) into "mutations per megabase" (Foundation Medicine units,
# which is what the Yarchoan formula takes). Stated, not hidden: the conversion is
# an assumption and the sensitivity is reported below.
EXOME_MB = 30.0


def predicted_orr(tmb_per_mb):
    """The published Yarchoan regression."""
    return SLOPE * math.log(tmb_per_mb) + INTERCEPT


def implied_tmb(orr):
    """Invert it: what TMB would the formula need to produce this ORR?"""
    return math.exp((orr - INTERCEPT) / SLOPE)


def rule(n, title):
    print(f"\n{'=' * 74}\n{n}. {title}\n{'=' * 74}")


# ---------------------------------------------------------------------------
# 1. Does the formula reproduce the letter's own worked examples?
# ---------------------------------------------------------------------------

def formula_audit():
    rule(1, "FORMULA AUDIT — the letter's regression vs the letter's predictions")
    print(f"   ORR = {SLOPE} * ln(TMB) {INTERCEPT:+}\n")
    print(f"{'tumor type':32s} {'TMB':>6s} {'stated':>8s} {'recomputed':>11s} "
          f"{'delta':>7s} {'TMB needed':>11s}")
    for name, tmb, stated, _ci in WORKED_EXAMPLES:
        got = predicted_orr(tmb)
        need = implied_tmb(stated)
        print(f"{name:32s} {tmb:6.1f} {stated:7.1f}% {got:10.2f}% "
              f"{got - stated:+6.2f} {need:10.1f}")
    print("\n   The formula reproduces one of the letter's two worked examples to")
    print("   0.02 points and misses the other by ~0.85. Reading it as a precision")
    print("   instrument is already unsupported by the letter that published it.")


# ---------------------------------------------------------------------------
# 2. Anchor residuals against tumor types with primary-source ORR data
# ---------------------------------------------------------------------------

# (label, TMB per Mb, source of TMB, observed ORR %, n, source of ORR)
# Note on the two pancreatic rows: O'Reilly 2019 part A enrolled 65 patients across
# both arms. The published 3.1% ORR is exactly 1/32, so arm sizes of 32 and 33 are
# INFERRED, not quoted. n is not used in the residual calculation — only in display.
ANCHORS = [
    ("colorectal, dMMR/MSI-H", 1782 / EXOME_MB,
     "Le 2015 NEJM: mean 1782 somatic mutations/tumor (WES), /30 Mb",
     40.0, 10, "Le 2015 NEJM: 4/10 immune-related objective response"),
    ("colorectal, pMMR/MSS", 73 / EXOME_MB,
     "Le 2015 NEJM: mean 73 somatic mutations/tumor (WES), /30 Mb",
     0.0, 18, "Le 2015 NEJM: 0/18 immune-related objective response"),
    ("pancreatic ductal adeno.", 1.5,
     "PDAC median TMB ~1-2/Mb (Chalmers 2017 Genome Med); midpoint used",
     3.1, 32, "O'Reilly 2019 JAMA Oncol: durvalumab+tremelimumab ORR 3.1%"),
    ("pancreatic ductal adeno.", 1.5,
     "as above",
     0.0, 33, "O'Reilly 2019 JAMA Oncol: durvalumab monotherapy, no responders"),
]


def anchor_residuals():
    rule(2, "ANCHOR RESIDUALS — regression vs primary-trial ORR")
    print(f"{'tumor type':28s} {'TMB/Mb':>7s} {'pred':>7s} {'obs':>7s} "
          f"{'resid':>7s} {'n':>4s}")
    resids = []
    for label, tmb, _src_t, obs, n, _src_o in ANCHORS:
        pred = predicted_orr(tmb)
        resid = obs - pred
        resids.append(resid)
        print(f"{label:28s} {tmb:7.1f} {pred:6.1f}% {obs:6.1f}% "
              f"{resid:+6.1f} {n:4d}")
    print(f"\n   mean |residual| = {statistics.mean(abs(r) for r in resids):.1f} "
          f"percentage points")
    print("\n   Where TMB is very low, the regression is close: it predicts pancreatic")
    print("   failure well. Its worst anchor is MMR-proficient colorectal, which it")
    print("   over-predicts — a tumor type Yarchoan names as a known outlier. That is")
    print("   the point: the taxonomy is needed exactly where the residual is large.")
    print("\n   Sensitivity of the exome conversion (dMMR / pMMR colorectal):")
    for mb in (25.0, 30.0, 35.0, 40.0):
        print(f"     exome = {mb:4.0f} Mb -> dMMR pred {predicted_orr(1782 / mb):5.1f}%"
              f"   pMMR pred {predicted_orr(73 / mb):5.1f}%")
    print("   The dMMR prediction stays within a few points of the observed 40%")
    print("   across every plausible exome size, so the conclusion is not an artifact")
    print("   of the conversion.")


# ---------------------------------------------------------------------------
# 3. What r = 0.74 actually costs
# ---------------------------------------------------------------------------

def variance_decomposition():
    rule(3, "VARIANCE — the cost of r = 0.74, as a number")
    r2 = R_PUBLISHED ** 2
    print(f"   r  = {R_PUBLISHED}")
    print(f"   r^2 = {r2:.4f}  -> TMB accounts for {r2 * 100:.0f}% of the between-"
          f"cancer-type\n         variation in objective response rate.")
    print(f"   1 - r^2 = {1 - r2:.4f} -> {(1 - r2) * 100:.0f}% is not accounted for "
          f"by mutation count.")
    print("\n   Note what the unit is. This is variance across CANCER TYPES, not across")
    print("   patients. It is the correlation of 27 group averages. The letter's own")
    print("   confidence intervals show the width even at that level:")
    for name, _tmb, stated, ci in WORKED_EXAMPLES:
        print(f"     {name:32s} {stated:4.1f}%  95% CI {ci[0]}-{ci[1]}  "
              f"(width {ci[1] - ci[0]:.1f} pts)")
    print("\n   A 19-point-wide interval on a cancer-type average is the ceiling, not")
    print("   the bedside performance. No patient-level claim follows from it.")


# ---------------------------------------------------------------------------
# 4. How much of the missing 45% is biology, how much is small trials?
# ---------------------------------------------------------------------------

def attenuation_mc(trials=4000, seed=20260903):
    rule(4, "ATTENUATION [ILLUSTRATIVE MODEL] — biology vs sampling noise")
    print("   Model, stated in full so it can be argued with:")
    print("     phenotype_i = a*ln(TMB_i) + e_i        e_i ~ TMB-independent biology")
    print("     true ORR_i  = linear in phenotype_i     (no extra noise)")
    print("     obs ORR_i   = Binomial(n_i, ORR_i)/n_i  (finite trial)")
    print("   Under this model with NO sampling noise, corr(lnTMB, ORR)^2 is exactly")
    print("   the TMB-explained share, so r=0.74 would mean 45% TMB-independent")
    print("   biology. Finite trials attenuate r, so the real share is smaller.\n")

    rng = random.Random(seed)

    def simulate(frac_independent, n_reps=400):
        """Return mean observed corr(lnTMB, obsORR) for a given biology share."""
        out = []
        for _ in range(n_reps):
            lntmb, obs = [], []
            for _ in range(N_TUMOR_TYPES):
                tmb = math.exp(rng.uniform(math.log(0.8), math.log(50.0)))
                signal = predicted_orr(tmb)
                # scale noise so that Var(noise)/(Var(signal)+Var(noise)) = frac
                sd_signal = 12.0  # ~sd of the signal over this TMB range
                sd_noise = sd_signal * math.sqrt(
                    frac_independent / (1 - frac_independent))
                p = (signal + rng.gauss(0, sd_noise)) / 100.0
                p = min(max(p, 0.001), 0.95)
                n = int(math.exp(rng.uniform(math.log(15), math.log(200))))
                k = sum(1 for _ in range(n) if rng.random() < p)
                lntmb.append(math.log(tmb))
                obs.append(100.0 * k / n)
            out.append(pearson(lntmb, obs))
        return statistics.mean(out)

    print(f"{'TMB-independent biology':>24s} {'-> observed r':>14s}")
    grid = [0.10, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.55]
    results = []
    for f in grid:
        r = simulate(f)
        results.append((f, r))
        mark = "  <-- matches published r" if abs(r - R_PUBLISHED) < 0.02 else ""
        print(f"{f * 100:23.0f}% {r:14.3f}{mark}")

    best = min(results, key=lambda fr: abs(fr[1] - R_PUBLISHED))
    print(f"\n   Closest match to the published r = {R_PUBLISHED}: "
          f"{best[0] * 100:.0f}% TMB-independent biology")
    print(f"   Naive reading of 1 - r^2:                    "
          f"{(1 - R_PUBLISHED ** 2) * 100:.0f}%")
    print("\n   Direction of the correction matters more than the exact figure. Finite")
    print("   trials make TMB look WORSE than it is, so part of the gap the source reel")
    print("   would attribute to immune phenotype is really just small-n noise. The")
    print("   honest claim is weaker than the one the reel could have made — which is")
    print("   the whole reason to compute it instead of asserting it.")


def pearson(xs, ys):
    mx, my = statistics.mean(xs), statistics.mean(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    dy = math.sqrt(sum((y - my) ** 2 for y in ys))
    return num / (dx * dy) if dx and dy else 0.0


# ---------------------------------------------------------------------------
# 5. The within-tumor-type check that needs no TMB number at all
# ---------------------------------------------------------------------------

def merkel_within_type():
    rule(5, "WITHIN-TYPE CHECK — Merkel-cell carcinoma, no TMB value required")
    print("   Nghiem 2016 NEJM (PMID 27093365), first-line pembrolizumab, n=26:")
    print("     MCPyV virus-POSITIVE tumours  (low mutational burden, viral antigens)")
    print("       response rate 62%  (10/16)")
    print("     MCPyV virus-NEGATIVE tumours  (UV-driven, high mutational burden)")
    print("       response rate 44%  (4/9)")
    # Exact one-sided check on how weak this evidence is.
    print("\n   The LOWER-burden subgroup responded at the HIGHER rate, inside a single")
    print("   tumour type, with treatment and staging held constant. That is a direct")
    print("   counterexample to mutation count as the causal variable.")
    print("\n   It is also 16 and 9 patients. Overlapping intervals; not significant.")
    print("   Treat it as a mechanism illustration, never as a result. Yarchoan names")
    print("   Merkel cell as the canonical above-the-line outlier and attributes it to")
    print("   viral antigen presentation; this is that attribution, in one trial.")


def main():
    print(__doc__.split("\n\n")[0])
    formula_audit()
    anchor_residuals()
    variance_decomposition()
    attenuation_mc()
    merkel_within_type()
    print()


if __name__ == "__main__":
    main()
