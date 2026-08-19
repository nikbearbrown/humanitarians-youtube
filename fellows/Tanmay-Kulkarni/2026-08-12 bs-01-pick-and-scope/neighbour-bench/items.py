"""Role statements for the adjacent-profession-test bench.

Six base cases across three domains. Each base has four variants, and the whole
experiment turns on how they differ:

    full      bounded role + a detail only this role could write.  Expect PASS.
    generic   bare professional category.  Expect FAIL.  (known-fail anchor)
    swapped   SAME word count and SAME number of domain terms as `full`, but the
              identifying detail is replaced with domain-flavoured detail the
              nearest neighbour could equally claim.  Expect FAIL.
              >>> This is the length/jargon control — the arm the source draft
              >>> never had.  A PASS here means the verdict tracks length and
              >>> jargon density, not exclusion.
    stripped  `full` with the identifying phrase removed entirely (shorter).
              Expect FAIL.
              >>> This is the Q3 falsifier.  A PASS here means the phrase we
              >>> called load-bearing was not load-bearing.

`swapped` and `stripped` are both expected to FAIL but for different reasons, so
they stay distinguishable: one isolates specificity from verbosity, the other
tests whether the named phrase carries the exclusion.

Ground truth is fixed by construction — the model's opinion is never needed to
score a trial. `nearest_neighbour` is the human-designated answer, used to check
whether the model draws the same boundary a person would (framework question 4).
"""

BASES = [
    # ---------------------------------------------------------------- healthcare
    {
        "id": "H1",
        "domain": "healthcare",
        "nearest_neighbour": "night-shift clinical nurse",
        "load_bearing": "verifies discharge medication orders against Beers Criteria",
        "variants": {
            "full": {
                "text": "Clinical pharmacist on night shift who verifies discharge medication "
                        "orders against Beers Criteria before the patient leaves the unit.",
                "domain_terms": ["clinical pharmacist", "night shift",
                                 "discharge medication orders", "Beers Criteria", "unit"],
                "expected": "PASS",
            },
            "swapped": {
                "text": "Clinical pharmacist on night shift who works with the care team on "
                        "patient safety across the hospital's inpatient units.",
                "domain_terms": ["clinical pharmacist", "night shift", "care team",
                                 "patient safety", "inpatient units"],
                "expected": "FAIL",
            },
            "stripped": {
                "text": "Clinical pharmacist on night shift.",
                "domain_terms": ["clinical pharmacist", "night shift"],
                "expected": "FAIL",
            },
            "generic": {
                "text": "Healthcare professional.",
                "domain_terms": ["healthcare professional"],
                "expected": "FAIL",
            },
        },
    },
    {
        "id": "H2",
        "domain": "healthcare",
        "nearest_neighbour": "pediatric ICU nurse",
        "load_bearing": "titrates ventilator settings for infants during weaning trials",
        "variants": {
            "full": {
                "text": "Respiratory therapist in a pediatric ICU who titrates ventilator "
                        "settings for infants during weaning trials.",
                "domain_terms": ["respiratory therapist", "pediatric ICU",
                                 "ventilator settings", "weaning trials"],
                "expected": "PASS",
            },
            "swapped": {
                "text": "Respiratory therapist in a pediatric ICU who supports the "
                        "multidisciplinary team in delivering evidence-based care.",
                "domain_terms": ["respiratory therapist", "pediatric ICU",
                                 "multidisciplinary team", "evidence-based care"],
                "expected": "FAIL",
            },
            "stripped": {
                "text": "Respiratory therapist in a pediatric ICU.",
                "domain_terms": ["respiratory therapist", "pediatric ICU"],
                "expected": "FAIL",
            },
            "generic": {
                "text": "Clinical staff member.",
                "domain_terms": ["clinical staff"],
                "expected": "FAIL",
            },
        },
    },
    # ------------------------------------------------------------------- finance
    {
        "id": "F1",
        "domain": "finance",
        "nearest_neighbour": "commercial relationship manager",
        "load_bearing": "re-underwrites covenant breaches on middle-market revolving facilities",
        "variants": {
            "full": {
                "text": "Credit analyst at a regional bank who re-underwrites covenant "
                        "breaches on middle-market revolving facilities.",
                "domain_terms": ["credit analyst", "regional bank", "covenant breaches",
                                 "middle-market", "revolving facilities"],
                "expected": "PASS",
            },
            "swapped": {
                "text": "Credit analyst at a regional bank who supports relationship "
                        "managers on portfolio risk oversight.",
                "domain_terms": ["credit analyst", "regional bank", "relationship managers",
                                 "portfolio", "risk oversight"],
                "expected": "FAIL",
            },
            "stripped": {
                "text": "Credit analyst at a regional bank.",
                "domain_terms": ["credit analyst", "regional bank"],
                "expected": "FAIL",
            },
            "generic": {
                "text": "Finance professional.",
                "domain_terms": ["finance professional"],
                "expected": "FAIL",
            },
        },
    },
    {
        "id": "F2",
        "domain": "finance",
        "nearest_neighbour": "AML compliance officer",
        "load_bearing": "clears sanctions-screening false positives on correspondent-bank wire traffic",
        "variants": {
            "full": {
                "text": "Financial crime investigator who clears sanctions-screening false "
                        "positives on correspondent-bank wire traffic the same business day.",
                "domain_terms": ["financial crime investigator", "sanctions screening",
                                 "false positives", "correspondent bank", "wire traffic"],
                "expected": "PASS",
            },
            "swapped": {
                "text": "Financial crime investigator who works closely with compliance "
                        "stakeholders to strengthen the anti-money-laundering control "
                        "framework firmwide.",
                "domain_terms": ["financial crime investigator", "compliance stakeholders",
                                 "anti-money-laundering", "control framework", "firmwide"],
                "expected": "FAIL",
            },
            "stripped": {
                "text": "Financial crime investigator.",
                "domain_terms": ["financial crime investigator"],
                "expected": "FAIL",
            },
            "generic": {
                "text": "Compliance professional.",
                "domain_terms": ["compliance professional"],
                "expected": "FAIL",
            },
        },
    },
    # --------------------------------------------------------------- engineering
    {
        # The source draft's own non-healthcare example (bs-01 B05).
        "id": "E1",
        "domain": "engineering",
        "nearest_neighbour": "platform engineer on the same payments team",
        "load_bearing": "reviewing a pull request that touches the fraud-detection service",
        "variants": {
            "full": {
                "text": "Backend engineer on the payments team reviewing a pull request that "
                        "touches the fraud-detection service.",
                "domain_terms": ["backend engineer", "payments team", "pull request",
                                 "fraud-detection service"],
                "expected": "PASS",
            },
            "swapped": {
                "text": "Backend engineer on the payments team working across many services "
                        "to improve overall system reliability.",
                "domain_terms": ["backend engineer", "payments team", "services",
                                 "system reliability"],
                "expected": "FAIL",
            },
            "stripped": {
                "text": "Backend engineer on the payments team.",
                "domain_terms": ["backend engineer", "payments team"],
                "expected": "FAIL",
            },
            "generic": {
                "text": "Software engineer.",
                "domain_terms": ["software engineer"],
                "expected": "FAIL",
            },
        },
    },
    {
        "id": "E2",
        "domain": "engineering",
        "nearest_neighbour": "on-call platform engineer",
        "load_bearing": "deciding whether to roll back a canary deployment mid-incident",
        "variants": {
            "full": {
                "text": "Site reliability engineer on call, deciding whether to roll back a "
                        "canary deployment mid-incident.",
                "domain_terms": ["site reliability engineer", "on call", "roll back",
                                 "canary deployment", "incident"],
                "expected": "PASS",
            },
            "swapped": {
                "text": "Site reliability engineer on call, maintaining service health and "
                        "uptime across the production estate.",
                "domain_terms": ["site reliability engineer", "on call", "service health",
                                 "uptime", "production estate"],
                "expected": "FAIL",
            },
            "stripped": {
                "text": "Site reliability engineer on call.",
                "domain_terms": ["site reliability engineer", "on call"],
                "expected": "FAIL",
            },
            "generic": {
                "text": "Infrastructure professional.",
                "domain_terms": ["infrastructure professional"],
                "expected": "FAIL",
            },
        },
    },
]

VARIANTS = ("full", "swapped", "stripped", "generic")

# Revision 2. The pilot showed the verdict is dominated by *which* neighbour the
# model picks, so the neighbour becomes a controlled variable:
#   pinned  the designated neighbour is supplied in the prompt. Verdict measures
#           exclusion given a fixed neighbour — ground truth is well-defined here.
#   free    the model picks its own, exactly as the source draft's CTA has it.
#           Measures neighbour-choice behaviour, including degenerate choices.
ARMS = ("pinned", "free")

# Head noun of the subject's own title, for detecting a degenerate free-arm choice
# (Haiku answered "hospital pharmacist" for a clinical pharmacist — the same
# profession, not an adjacent one, which makes the item fail without testing it).
ROLE_NOUN = {
    "H1": "pharmacist",
    "H2": "respiratory therapist",
    "F1": "credit analyst",
    "F2": "investigator",
    "E1": "backend engineer",
    "E2": "site reliability engineer",
}


def trials():
    """Flatten BASES into one dict per (base, variant)."""
    for base in BASES:
        for variant in VARIANTS:
            v = base["variants"][variant]
            yield {
                "base_id": base["id"],
                "domain": base["domain"],
                "variant": variant,
                "statement": " ".join(v["text"].split()),
                "expected": v["expected"],
                "nearest_neighbour": base["nearest_neighbour"],
                "load_bearing": base["load_bearing"],
                "role_noun": ROLE_NOUN[base["id"]],
                "n_words": len(v["text"].split()),
                "n_domain_terms": len(v["domain_terms"]),
            }


def match_report():
    """Audit the full-vs-swapped match. This is the design's load-bearing claim:
    if these two are not matched on length and jargon, the length confound is
    not controlled and no sample size fixes it."""
    rows = []
    for base in BASES:
        f = base["variants"]["full"]
        s = base["variants"]["swapped"]
        fw, sw = len(f["text"].split()), len(s["text"].split())
        ft, st = len(f["domain_terms"]), len(s["domain_terms"])
        rows.append({
            "base_id": base["id"],
            "full_words": fw, "swapped_words": sw, "word_delta": sw - fw,
            "full_terms": ft, "swapped_terms": st, "term_delta": st - ft,
        })
    return rows


if __name__ == "__main__":
    print(f"{len(BASES)} bases x {len(VARIANTS)} variants = "
          f"{len(BASES) * len(VARIANTS)} items\n")
    print("full-vs-swapped match audit (deltas should be near zero):")
    print(f"{'base':<6}{'words f/s':>12}{'Δ':>5}{'terms f/s':>12}{'Δ':>5}")
    worst_w = worst_t = 0
    for r in match_report():
        print(f"{r['base_id']:<6}{r['full_words']:>5}/{r['swapped_words']:<6}"
              f"{r['word_delta']:>+5}{r['full_terms']:>5}/{r['swapped_terms']:<6}"
              f"{r['term_delta']:>+5}")
        worst_w = max(worst_w, abs(r["word_delta"]))
        worst_t = max(worst_t, abs(r["term_delta"]))
    print(f"\nworst word delta: {worst_w}   worst domain-term delta: {worst_t}")
