"""Cycle 1: retrieve an FAQ passage using literal word overlap.

No embeddings, no model, no dependencies beyond the standard library.
This is the "just match the words" approach a RAG pipeline might start
with before reaching for representation learning.
"""

PASSAGES = [
    ("HR-01", "Vacation and PTO: full-time employees accrue 15 paid days off "
              "per year, usable for vacation, personal time, or appointments. "
              "Unused days roll over up to a maximum of 5."),
    ("HR-02", "Sick leave: employees receive 10 paid sick days annually, "
              "separate from the standard vacation and PTO allotment."),
    ("HR-03", "Parental leave: employees are eligible for 12 weeks of paid "
              "parental leave following the birth or adoption of a child."),
    ("IT-01", "How do I request a new laptop? Submit a hardware ticket "
              "through the IT service desk portal and a replacement laptop "
              "will be issued within 3 business days."),
    ("IT-02", "Password resets: employees can reset their own network "
              "password through the self-service portal without contacting IT."),
    ("IT-03", "Software installs: standard business software is available "
              "for self-install from the internal app catalog; non-standard "
              "requests need manager approval."),
]

QUERY = "How do I request time off?"


def tokenize(text):
    return set(text.lower().replace("?", "").replace(":", "").split())


def word_overlap(a, b):
    wa, wb = tokenize(a), tokenize(b)
    return len(wa & wb) / len(wa | wb)


def main():
    print(f"query: {QUERY!r}\n")
    ranked = sorted(
        ((word_overlap(QUERY, text), pid) for pid, text in PASSAGES),
        reverse=True,
    )
    print("ranked by word overlap:")
    for score, pid in ranked:
        print(f"  {score:.3f}  {pid}")
    top_score, top_id = ranked[0]
    print(f"\ntop match: {top_id} (score {top_score:.3f})")


if __name__ == "__main__":
    main()
