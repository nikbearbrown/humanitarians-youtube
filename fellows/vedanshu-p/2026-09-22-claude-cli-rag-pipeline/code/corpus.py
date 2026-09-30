"""corpus.py — raw help-desk source documents, BEFORE ingestion.

Note what this file does NOT contain: chunks. Chapter 7's first stage is
*ingest*, and ingest is the thing that turns documents into chunks — so the
pipeline has to be handed whole documents or the first stage would have nothing
to do. Each entry here is a multi-paragraph policy document, exactly as it would
arrive from a share drive.

The question the reel traces is the chapter's own worked example:

    "How many vacation days do I get in my first year?"

VA-101 is the gold document, and its FIRST paragraph is the one that answers the
question. The corpus is stacked to make the trace informative rather than
flattering:

  * SL-140 (sick leave) and BO-001 (benefits overview) are the two "plausibly
    related chunks" the chapter predicts will come back alongside the right one.
  * BO-001 mentions vacation WITHOUT giving a first-year number, so a retriever
    that grabs it looks reasonable and still fails to answer.
  * VA-101's own later paragraphs discuss carry-over and scheduling, so even
    within the right document, the wrong chunk can win.
"""

DOCUMENTS = {
    "VA-101": (
        "Vacation Policy VA-101. First-year employees accrue 12 paid vacation days. "
        "From the second year onward this rises to 15 days, and to 20 days after "
        "five years of continuous service.\n\n"
        "Unused vacation may be carried over into the following calendar year up to "
        "a maximum of 5 days. Carried-over days expire on 31 March.\n\n"
        "Vacation must be scheduled with your manager at least two weeks in advance "
        "for absences longer than three consecutive days."
    ),
    "SL-140": (
        "Sick Leave Policy SL-140. Employees receive 10 paid sick days per calendar "
        "year, available from the first day of employment.\n\n"
        "Sick days do not carry over and are not paid out on departure. A doctor's "
        "note is required for absences of more than three consecutive days."
    ),
    "BO-001": (
        "Benefits Overview BO-001. This overview summarises the benefits available "
        "to full-time employees, including vacation, sick leave, health coverage, "
        "parental leave and the tuition reimbursement programme.\n\n"
        "Each benefit is governed by its own policy document. Consult the specific "
        "policy for accrual rates, eligibility windows and claim procedures."
    ),
    "PL-220": (
        "Parental Leave Policy PL-220. Primary caregivers receive 16 weeks of paid "
        "leave; secondary caregivers receive 8 weeks.\n\n"
        "Leave must begin within 12 months of the birth or placement and may be "
        "taken in no more than two separate blocks."
    ),
    "HC-500": (
        "Health Coverage Policy HC-500. Medical, dental and vision plans begin on "
        "the first day of the month following your start date.\n\n"
        "Dependants may be added during onboarding or during the annual open "
        "enrolment window each November."
    ),
    "TR-114": (
        "Tuition Reimbursement Policy TR-114. The company reimburses approved degree "
        "coursework up to $5,250 per calendar year.\n\n"
        "Employees must be full-time and receive a grade of B or better for the "
        "reimbursement to be issued."
    ),
}

QUESTION = "How many vacation days do I get in my first year?"

# The chunk that actually answers it: VA-101's first paragraph.
GOLD_DOC = "VA-101"
GOLD_PARA = 0
GOLD_FACT = "12"
