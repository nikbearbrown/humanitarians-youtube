"""ch28_ledger.py — tally Novia's Chapter 28 fact-check workbook.

Numbers are from 28_factcheck_report_ai_only_editorial.md (2026-08-17),
companion to 28_factcheck_report.md (54 web-flagged sentences) and the
three-sheet workbook 28_factcheck_review.xlsx (not on disk at authoring).

This script does not scrape the web. It reconstructs the LEDGER:
  Sheet A  Chapter 28            — 54 flagged/verified (web)
  Sheet B  Chapter 28 - AI-Only  — 114 classified, not googled
  Sheet C  Chapter 28 - Editorial — 13 internal-consistency findings
Plus Part 3: 3 hallucination flags on the 114 AI-ONLY sentences.
"""
from __future__ import annotations

TOTAL = 168
AI_ONLY = 114
FLAGGED = 54  # STAT / GUIDELINE / APPROVAL / EVIDENCE / SPECIALIST / CURRENT
EDITORIAL = 13
HALLUCINATION_FLAGS = 3
TOPIC = "Nanotechnology in Cancer"

BY_FILE = {
    "1_Introduction_to_Nanotechnology_in_Cancer": 9,
    "2_Nanoparticles_for_Drug_Delivery": 30,
    "3_Clinical_Translation_and_Drug_Resistance": 33,
    "4_Nanomaterials_for_Imaging_and_Diagnosis": 17,
    "5_Theranostics_and_Multifunctional_Platforms": 18,
    "6_Summary": 7,
}

EDITORIAL_FINDINGS = [
    "Duplicate intro/summary sentence",
    "Duplicate AuNP CT-contrast sentence",
    "BBB defined twice in a row",
    "Protein-corona identity restated",
    "Near-verbatim multifunctional NP sentence",
    "Duplicate 'Combination Therapy Platforms' heading",
    "Unedited 'our targeted probe' voice",
    "UTF-8 encoding artifacts throughout",
    "PDA nanocarrier sentence fragment",
    "PEG stealth mechanism reversed",
    "siRNA/RISC mechanism reversed",
    "'Capable to' grammar",
    "Redundant article on protein corona",
]

HALLUCINATION = [
    "PEG prevents the liposome from recognizing clearance — backwards",
    "siRNAs assemble into endoribonuclease / RISC — backwards",
    "Gold has antitumor activity besides imaging — overstated",
]


def sheet_a_web() -> dict:
    return {"name": "Chapter 28", "rows": FLAGGED, "note": "web-verified"}


def sheet_b_ai_only() -> dict:
    assert sum(BY_FILE.values()) == AI_ONLY
    return {"name": "Chapter 28 - AI-Only", "rows": AI_ONLY, "by_file": BY_FILE}


def sheet_c_editorial() -> dict:
    return {"name": "Chapter 28 - Editorial", "rows": EDITORIAL, "findings": EDITORIAL_FINDINGS}


def first_pass() -> dict:
    return {"total": TOTAL, "flagged": FLAGGED, "ai_only_unlisted": TOTAL - FLAGGED}


def second_pass() -> dict:
    return {
        "total": TOTAL,
        "topic": TOPIC,
        "sheet_a": sheet_a_web(),
        "sheet_b": sheet_b_ai_only(),
        "sheet_c": sheet_c_editorial(),
        "hallucination_flags": HALLUCINATION_FLAGS,
        "most_significant": HALLUCINATION[0],
    }


if __name__ == "__main__":
    a = first_pass()
    b = second_pass()
    print("topic", TOPIC)
    print("first pass  flagged", a["flagged"], "of", a["total"], "— AI-only unlisted")
    print("second pass sheets", b["sheet_a"]["rows"], "+", b["sheet_b"]["rows"], "+", b["sheet_c"]["rows"])
    print("hallucination flags", b["hallucination_flags"], "of", AI_ONLY)
    print("most significant:", b["most_significant"])
    for name, n in BY_FILE.items():
        print(f"  {name:48} {n:3} AI-only")
