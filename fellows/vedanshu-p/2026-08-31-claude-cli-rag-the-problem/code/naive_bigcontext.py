# naive_bigcontext.py — the "obvious fix": paste the WHOLE manual into
# context instead of a tiny fixed dict, and scan it for something relevant.
# No real retrieval/ranking — just a crude first-match keyword scan, standing
# in for what happens when nothing decides WHICH passage actually answers
# the question. The correct passage is in here. That isn't enough.

MANUAL = [
    "Vacation policy: employees accrue 15 vacation days annually. "
    "Requests for leave should be submitted two weeks in advance.",

    "Health insurance: coverage begins on day one of employment.",

    "Remote work: employees may work remotely up to two days per week.",

    "Parental leave: effective this year, employees receive 16 weeks of "
    "parental leave, updated from the previous 8-week allowance.",

    "Expense reimbursement: submit receipts within 30 days of purchase.",
]

def naive_scan(question: str) -> str:
    words = set(question.lower().replace("?", "").split())
    for paragraph in MANUAL:                  # first match wins — no ranking
        para_words = set(paragraph.lower().replace(".", "").replace(",", "").split())
        if words & para_words:
            return paragraph
    return "I don't know."

if __name__ == "__main__":
    q = "How many weeks of parental leave do I get?"
    print(f"Q: {q}")
    print(f"A: {naive_scan(q)}")
