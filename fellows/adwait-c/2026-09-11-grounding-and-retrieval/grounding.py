"""grounding.py — what a citation actually proves, and what it does not.

Part of the Agentic AI series (Humanitarians AI Fellows).

"It cited a source" is treated as the end of the argument. It is not. A citation can be
checked in two ways automatically, and the third check — the one that actually matters —
cannot be automated at all. This file makes that boundary concrete by running all three
against four claims.

No model and no API key: every check here is string work, which is the point. If a check
can be done with string work, it should never be delegated to a model.

    python3 grounding.py
"""

from __future__ import annotations

# --- the corpus the agent retrieved from ----------------------------------

CORPUS = {
    "handbook.md": (
        "Expenses over $500 require manager approval. "
        "Travel is reimbursed within 30 days of submission."
    ),
    "policy.md": (
        "Remote employees receive a $1,200 annual equipment stipend."
    ),
}

# --- four answers, each with a citation ------------------------------------
# (claim, cited document, the span the answer quoted, does the quote support the claim?)

CLAIMS = [
    ("Expenses over $500 need manager approval.", "handbook.md",
     "Expenses over $500 require manager approval.", True),
    ("Travel is reimbursed within 14 days.", "handbook.md",
     "Travel is reimbursed within 30 days of submission.", False),
    ("Remote employees get a $2,000 stipend.", "policy.md",
     "Remote employees receive a $2,000 annual equipment stipend.", False),
    ("Contractors get the same stipend.", "benefits.md",
     "Contractors receive the same stipend.", False),
]


# --- the three checks -----------------------------------------------------
# This is the beat B05 shows on screen, verbatim.

def check(claim: str, source: str, quote: str) -> str:
    """Two of the three checks a citation needs. The third is not in here.

    Machine-checkable: the source exists, and the quote appears in it verbatim.
    NOT machine-checkable: whether the quote actually supports the claim. That is a
    judgement about meaning, and nothing in this function attempts it.
    """
    if source not in CORPUS:
        return "MISSING_SOURCE"
    if quote not in CORPUS[source]:
        return "QUOTE_NOT_IN_SOURCE"
    return "CITATION_CHECKS_OUT"


if __name__ == "__main__":
    print("FOUR ANSWERS, EACH WITH A CITATION\n")
    print(f"{'claim':<42} {'automatic check':<20} {'actually true?'}")
    for claim, source, quote, supports in CLAIMS:
        result = check(claim, source, quote)
        truth = "yes" if supports else "NO"
        print(f"{claim:<42} {result:<20} {truth}")

    passed = [c for c in CLAIMS if check(c[0], c[1], c[2]) == "CITATION_CHECKS_OUT"]
    wrong = [c for c in passed if not c[3]]
    print(f"\n  citations that check out automatically : {len(passed)} of {len(CLAIMS)}")
    print(f"  of those, claims that are still FALSE  : {len(wrong)}")
    for c in wrong:
        print(f"\n  The check cannot catch this one:")
        print(f"    claim  {c[0]}")
        print(f"    quote  {c[2]}")
        print(f"    both the source and the quote are real. The claim still is not.")
