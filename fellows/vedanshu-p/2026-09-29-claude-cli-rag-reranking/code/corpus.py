"""corpus.py — a small help-desk collection, and Chapter 9's own vague question.

The question is the chapter's, verbatim: "Can I still get my old benefits back?"
Chapter 9 uses it to make a specific point — that "old benefits" could mean a
retired healthcare plan, a discontinued perk, or a benefit the employee opted
out of earlier, so a literal search on this phrasing retrieves "a scattered,
low-precision set of chunks touching lightly on several different benefits
topics."

The corpus is written so that is actually TRUE rather than asserted. Three
things here talk about old benefits without answering the question:

  BO-100  a benefits overview that lists everything and resolves nothing
  RP-220  an archive of retired plans that says they are closed
  OE-300  the open-enrolment calendar, which is about timing, not reversal

and one thing answers it:

  RE-410  the re-enrolment process for a discontinued or opted-out benefit

EQ-150 is the surface trap: "get your old laptop back" shares the question's
literal shape ("get … old … back") while sharing none of its meaning. It is
here to give a lexical near-miss something to grab.

NOTHING HERE IS TUNED TO A RESULT. The passages were written once, as a help
desk would write them, and whatever the retriever does with them is what the
reel reports.
"""

DOCUMENTS = {
    "RE-410": """Benefit Re-enrolment After Opt-Out or Discontinuation

An employee who previously declined a benefit, or whose benefit was
discontinued when a plan was retired, may request re-enrolment. Submit the
re-enrolment form to People Operations naming the benefit and the date of the
original opt-out. Requests are reviewed within ten business days.

Re-enrolment outside the annual window requires a qualifying life event, or
written approval from a People Operations partner where the original
discontinuation was initiated by the company rather than the employee.""",

    "BO-100": """Employee Benefits Overview

The company offers medical, dental and vision coverage, a retirement savings
plan with employer matching, paid parental leave, a commuter allowance, and an
annual wellness stipend. Coverage levels vary by employment classification.

This overview is a summary. For the governing terms of any individual benefit,
consult that benefit's own policy document or contact People Operations.""",

    "RP-220": """Retired Benefit Plans

The following plans are closed and no longer accept participants: the legacy
PPO medical plan, the transit subsidy programme, and the home-office equipment
allowance introduced in an earlier policy cycle.

Employees enrolled in a retired plan before its closure keep their existing
coverage until the stated end date. Retired plans do not accept new enrolment
under any circumstances.""",

    "OE-300": """Open Enrolment Window

Open enrolment runs for three weeks each autumn. During the window employees
may add, change or drop benefits for the following plan year without providing
a reason.

Outside the window, changes generally require a qualifying life event such as
marriage, the birth or adoption of a child, or a change in a spouse's
coverage.""",

    "EQ-150": """Equipment Return and Reissue

Employees returning a laptop, monitor or other issued hardware should book a
collection with IT Support. If you need to get your old device back after a
return — for example where a replacement has not yet arrived — contact IT
Support directly and reference the original return ticket.

Hardware held for more than ninety days after return is wiped and recycled.""",

    "TR-114": """Training and Certification Reimbursement

The company reimburses approved coursework, certification fees and conference
attendance where these are relevant to the employee's role. Obtain written
approval from your manager before incurring the cost.

Submit receipts within sixty days. Reimbursement is processed with the
following month's payroll.""",

    # ── the confusable neighbours ────────────────────────────────────────────
    # A six-document corpus of well-separated topics is not a retrieval test;
    # every question has exactly one plausible home and the first pass cannot
    # realistically get it wrong. These are the documents a real help desk has:
    # several that each talk about enrolment, coverage, eligibility, or "your
    # plan" without being the one you want.
    "HC-500": """Medical Plan Coverage Levels

Employees may select employee-only, employee-plus-one, or family coverage under
the current medical plan. Coverage level determines both the payroll deduction
and the annual out-of-pocket maximum.

Changing coverage level is treated the same as changing plans and follows the
same timing rules.""",

    "EL-120": """Benefit Eligibility

Full-time employees are eligible for all benefits from their first day.
Part-time employees working twenty hours or more per week are eligible for
medical, dental and vision coverage but not for the wellness stipend.

Contractors and interns are not eligible for company benefits.""",

    "QL-330": """Qualifying Life Events

A qualifying life event allows a benefits change outside the open enrolment
window. Recognised events include marriage, divorce, birth or adoption, a
dependant losing other coverage, and a change in a spouse's employment.

Notify People Operations within thirty days of the event. After thirty days the
change must wait for the next open enrolment.""",

    "WS-260": """Wellness Stipend

The annual wellness stipend reimburses gym memberships, fitness equipment and
approved wellness apps. The stipend resets each January and does not carry
over.

Employees who opted out of the stipend in a previous year are automatically
included again the following year without needing to request it.""",

    "PR-180": """Payroll Deductions for Benefits

Benefit premiums are deducted from each pay period. A mid-year benefits change
adjusts the deduction from the next full pay period, not retroactively.

Questions about a specific deduction amount should go to Payroll rather than
People Operations.""",

    "CB-140": """COBRA and Continuation Coverage

Employees leaving the company may continue medical, dental and vision coverage
under COBRA for the statutory period. Election paperwork is sent to the address
on file within fourteen days of the last working day.

Continuation coverage is not the same as re-enrolment and is not available to
current employees.""",

    "DP-390": """Dependant Coverage

Dependants may be added to an existing plan during open enrolment or within
thirty days of a qualifying life event. Documentation of the relationship is
required.

A dependant removed from coverage may be added again later, subject to the same
timing rules as any other change.""",

    "ST-210": """Stipend and Allowance Programmes

Active allowance programmes are the commuter allowance and the annual wellness
stipend. The home-office equipment allowance is no longer active.

Allowance programmes are separate from insured benefits and follow their own
approval routes.""",
}

# Chapter 9's own vague question, verbatim from §"Worked example".
QUESTION = "Can I still get my old benefits back?"

# The chapter's own suggested rewrite, verbatim from §"Worked example".
# NOT generated by a model — see SOURCES.md. This reel measures the EFFECT of
# the chapter's rewrite; it does not claim to have produced it.
REWRITE = ("process for re-enrolling in a previously discontinued or "
           "opted-out employee benefit")

# HAND-WRITTEN REWRITES — read this before reading the numbers.
#
# Chapter 9 describes two ways to produce these: HyDE (ask a model for a
# hypothetical ANSWER and embed that) and Rewrite-Retrieve-Read (a trained model
# rewrites the query). Both need a language model. This machine has no LLM and
# no network, so neither can be run here.
#
# So these rewrites are written BY HAND, in the style Rewrite-Retrieve-Read
# describes: state the thing being asked about in the vocabulary a policy
# document would use. The first one is the chapter's own, verbatim.
#
# What this reel therefore measures is REAL: the effect of a better query on a
# real retriever. What it does NOT show is a model producing the rewrite. The
# rewriting step is the one part of this chapter this machine cannot run, and
# the reel says so rather than implying an LLM was in the loop.
REWRITES = {
    "Can I still get my old benefits back?":
        REWRITE,
    "How do I get my laptop back after I returned it?":
        "retrieving returned hardware from IT support before a replacement arrives",
    "When am I allowed to change my health plan?":
        "open enrolment window and qualifying life event rules for changing a benefit election",
    "Will the company pay for a certification course?":
        "reimbursement for approved certification fees and coursework",
    "Is the transit subsidy still open to join?":
        "retired benefit plans closed to new enrolment",
    "What does the company actually offer as benefits?":
        "summary list of employee benefits offered by the company",
}

GOLD_DOC = "RE-410"
GOLD_PARA = 0

# A question set, not a single question. One query tells you almost nothing
# about a retriever — re-ranking either helps on a given question or it does
# not, and the only way to say anything honest about "does re-ranking help" is
# to ask more than once. Gold is scored at DOCUMENT level: any chunk of the
# right document counts, which avoids arguing about which paragraph of a
# correct document is the correct paragraph.
QUESTIONS = [
    ("Can I still get my old benefits back?", "RE-410"),
    ("How do I get my laptop back after I returned it?", "EQ-150"),
    ("When am I allowed to change my health plan?", "OE-300"),
    ("Will the company pay for a certification course?", "TR-114"),
    ("Is the transit subsidy still open to join?", "RP-220"),
    ("What does the company actually offer as benefits?", "BO-100"),
]


def chunks():
    """Split on blank lines, but keep a document's title with its first paragraph.

    Structure-aware chunking, per Chapter 4. The naive version — split on blank
    lines and nothing else — made every document's TITLE its own 20-to-50
    character chunk. Those title chunks then competed with real passages in
    retrieval, and "Retired Benefit Plans" (a heading, containing no policy at
    all) outranked the paragraph that actually answers the question.

    A title is a label for the passage beneath it, not an answer to anything.
    Attaching it to that passage is the fix, and it is the chapter-4 lesson
    showing up one chapter later.
    """
    out = []
    for doc, text in DOCUMENTS.items():
        paras = [p.strip() for p in text.split("\n\n") if p.strip()]
        if len(paras) > 1 and "\n" not in paras[0] and len(paras[0]) < 60:
            paras = [paras[0] + "\n\n" + paras[1]] + paras[2:]
        for i, para in enumerate(paras):
            out.append({"id": f"{doc}#{i}", "doc": doc, "para": i, "text": para})
    return out


if __name__ == "__main__":
    cs = chunks()
    print(f"{len(DOCUMENTS)} documents -> {len(cs)} chunks")
    for c in cs:
        mark = "  <-- GOLD" if c["id"] == f"{GOLD_DOC}#{GOLD_PARA}" else ""
        print(f"  {c['id']:10} {len(c['text']):4d} chars{mark}")
    print()
    print("question:", QUESTION)
    print("rewrite :", REWRITE)
