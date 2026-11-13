# naive_assistant.py — a toy assistant that only knows a small, fixed
# snapshot of facts, and answers fluently even when it's guessing or the
# fact it "knows" is out of date. No retrieval, no lookup — just what's
# hardcoded here, exactly like a model's frozen training data.

KNOWN = {
    "parental_leave_weeks": 8,   # true value when this was "trained" — has since changed
}

def answer(question: str) -> str:
    q = question.lower()
    if "parental" in q:
        weeks = KNOWN["parental_leave_weeks"]
        return f"You get {weeks} weeks of parental leave."
    if "wellness" in q:
        # not in KNOWN at all — answers confidently anyway (hallucination)
        return "You get 12 wellness days a year, plus a $500 stipend."
    return "I don't know."

if __name__ == "__main__":
    for q in [
        "How many weeks of parental leave do I get?",
        "What's the wellness stipend policy?",
    ]:
        print(f"Q: {q}")
        print(f"A: {answer(q)}")
        print()
