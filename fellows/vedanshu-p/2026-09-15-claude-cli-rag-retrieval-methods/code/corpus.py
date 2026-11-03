"""corpus.py — a small help-desk knowledge base, and the two queries from
Chapter 6's worked example.

The passages are written, not generated, because this chapter's claim is about
WHICH KIND OF MATCH succeeds — an exact code vs. a paraphrase — and that depends
on the words in the text, so the text has to be real prose with real overlap
properties.

The collection is deliberately adversarial in both directions:

  * TE-330 (travel) and PD-207 (professional development) both contain the word
    "reimbursement", so query 1 cannot be won by the word "reimbursement" alone
    — only the code TR-114 identifies the right chunk.
  * PD-207 and CE-118 are both about paying for employee education, so query 2
    has near-miss neighbours in meaning, not just in wording.

GOLD is TR-114 for BOTH queries: Chapter 6's example is two employees asking
about the same tuition-reimbursement policy in completely different ways.
"""

PASSAGES = {
    "TR-114": "Tuition Reimbursement Policy TR-114. The company reimburses approved "
              "degree coursework up to $5,250 per calendar year. Employees must be "
              "full-time and receive a grade of B or better.",
    "PD-207": "Professional Development Policy PD-207. Each employee has an annual "
              "budget for conferences and workshops, claimed through expense "
              "reimbursement after the event.",
    "CE-118": "Certification Exam Policy CE-118. The company pays exam fees for "
              "role-relevant professional certifications, once per certification "
              "per employee.",
    "TE-330": "Travel Expense Policy TE-330. Airfare, lodging and ground transport "
              "are eligible for reimbursement. Submit receipts within 30 days of "
              "return.",
    "PL-220": "Parental Leave Policy PL-220. Primary caregivers receive 16 weeks of "
              "paid leave; secondary caregivers receive 8 weeks.",
    "VA-101": "Vacation and PTO Policy VA-101. Full-time employees accrue 15 paid "
              "days off per year, rising to 20 days after five years of service.",
    "HC-500": "Health Coverage Policy HC-500. Medical, dental and vision plans begin "
              "on the first day of the month following your start date.",
    "IT-010": "Equipment Request Policy IT-010. Submit a hardware ticket through the "
              "IT service desk to request a new laptop or monitor.",
    "RL-440": "Relocation Policy RL-440. Approved relocations include a moving "
              "allowance and up to 60 days of temporary housing.",
    "WL-712": "Wellness Stipend Policy WL-712. A monthly stipend may be applied to "
              "gym memberships, fitness classes or wellness apps.",
    "RT-900": "Remote Work Policy RT-900. Employees may work remotely up to three "
              "days per week with manager approval.",
    "SE-055": "Security Training Policy SE-055. All staff complete annual security "
              "awareness training within 30 days of the assignment date.",
}

# Chapter 6's two employees, asking about the SAME policy.
QUERIES = [
    ("exact code",  "What's the reimbursement limit under policy code TR-114?"),
    ("paraphrase",  "Does the company help pay for grad school?"),
]

GOLD = "TR-114"
