# rag_answer.py — retrieve the current policy passage, THEN answer.
# Two separate jobs: retrieve() searches the document store; answer() writes,
# conditioned on what was found — not on training memory alone.

DOCUMENT_STORE = {
    "sick_leave_policy": (
        "Effective this year, employees receive 15 sick days annually "
        "(updated 8 months ago, replacing the previous 10-day allowance)."
    ),
}

def retrieve(question: str) -> str:
    if "sick" in question.lower():
        return DOCUMENT_STORE["sick_leave_policy"]
    return ""

def answer(question: str) -> str:
    passage = retrieve(question)
    if not passage:
        return "I don't know."
    return f"Based on the current policy: {passage}"

if __name__ == "__main__":
    q = "How many sick days do I get this year?"
    print(f"Q: {q}")
    print(f"Retrieved: {retrieve(q)}")
    print(f"A: {answer(q)}")
