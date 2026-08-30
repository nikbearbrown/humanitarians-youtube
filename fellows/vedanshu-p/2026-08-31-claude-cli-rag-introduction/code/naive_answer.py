# naive_answer.py — a toy LLM answering only from its frozen training data.
# No retrieval step: whatever it "learned" at training time is all it has.

TRAINING_SNAPSHOT = {
    "sick_leave_days_per_year": 10,   # what the model saw during training
}

def answer(question: str) -> str:
    if "sick" in question.lower():
        days = TRAINING_SNAPSHOT["sick_leave_days_per_year"]
        return f"You get {days} sick days this year."
    return "I don't know."

if __name__ == "__main__":
    q = "How many sick days do I get this year?"
    print(f"Q: {q}")
    print(f"A: {answer(q)}")
