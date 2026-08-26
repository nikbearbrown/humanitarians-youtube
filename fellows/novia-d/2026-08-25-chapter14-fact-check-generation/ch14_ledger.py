"""ch14_ledger.py — tally Novia's Chapter 14 fact-check workbook.

Numbers are from 14_factcheck_report_ai_only_editorial.md (2026-08-06),
companion to 14_factcheck_report.md (46 web-flagged sentences) and the
three-sheet workbook 14_factcheck_review.xlsx.

This script does not scrape the web. It reconstructs the LEDGER:
  Sheet A  Chapter 14            — 46 flagged/verified (web)
  Sheet B  Chapter 14 - AI-Only  — 92 classified, not googled
  Sheet C  Chapter 14 - Editorial — 8 internal-consistency findings
Plus Part 3: 5 hallucination flags on the 92 AI-ONLY sentences.
"""
from __future__ import annotations

TOTAL = 138
AI_ONLY = 92
FLAGGED = 46  # STAT / GUIDELINE / APPROVAL / EVIDENCE / SPECIALIST / CURRENT
EDITORIAL = 8
HALLUCINATION_FLAGS = 5

# AI-ONLY counts by source file (editorial report Part 1)
BY_FILE = {
    "1_Introduction": 8,
    "2_Components": 33,
    "3_Stroma": 13,
    "4_Inflammation": 17,
    "5_ECM": 16,
    "6_Summary": 5,
}

# Editorial findings (Part 2) — labels only; full text lives in the report
EDITORIAL_FINDINGS = [
    "Redundant CAF definitions",
    "Missing conjunction",
    "Failed drugs presented as current",
    "90% unique-to-pancreatic vs lung desmoplasia",
    "IL-23 assigned to two pathways",
    "Mixed British/American spelling",
    "Awkward 'augment consequences'",
    "CARR AND UNDERWOOD caps",
]

# Hallucination sanity flags (Part 3) — 5 of 92
HALLUCINATION = [
    "Type-1 vs IFN-gamma imprecision",
    "DCs grouped as direct killers",
    "Th2/Th17 uniformly tumor-promoting",
    "'Checkpoint blockade' as escape (term backwards)",
    "IL-17 upregulates IL-23 — cause/effect reversed",  # most significant
]


def sheet_a_web() -> dict:
    return {"name": "Chapter 14", "rows": FLAGGED, "note": "web-verified"}


def sheet_b_ai_only() -> dict:
    assert sum(BY_FILE.values()) == AI_ONLY
    return {"name": "Chapter 14 - AI-Only", "rows": AI_ONLY, "by_file": BY_FILE}


def sheet_c_editorial() -> dict:
    return {"name": "Chapter 14 - Editorial", "rows": EDITORIAL, "findings": EDITORIAL_FINDINGS}


def first_pass() -> dict:
    """What the original web report captured — and only that."""
    return {"total": TOTAL, "flagged": FLAGGED, "ai_only_unlisted": TOTAL - FLAGGED}


def second_pass() -> dict:
    """The workbook as shipped: three sheets + hallucination reread."""
    return {
        "total": TOTAL,
        "sheet_a": sheet_a_web(),
        "sheet_b": sheet_b_ai_only(),
        "sheet_c": sheet_c_editorial(),
        "hallucination_flags": HALLUCINATION_FLAGS,
        "most_significant": HALLUCINATION[-1],
    }


if __name__ == "__main__":
    a = first_pass()
    b = second_pass()
    print("first pass  flagged", a["flagged"], "of", a["total"], "— AI-only unlisted")
    print("second pass sheets", b["sheet_a"]["rows"], "+", b["sheet_b"]["rows"], "+", b["sheet_c"]["rows"])
    print("hallucination flags", b["hallucination_flags"], "of", AI_ONLY)
    print("most significant:", b["most_significant"])
    for name, n in BY_FILE.items():
        print(f"  {name:16} {n:3} AI-only")
