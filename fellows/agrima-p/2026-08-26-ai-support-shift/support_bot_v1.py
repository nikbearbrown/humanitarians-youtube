# support_bot_v1.py — Claude Code output: keyword-matching support bot
# (the "old way" — like a phone tree, just typed instead of pressed)

RULES = [
    (["password", "reset", "locked out"],
     "To reset your password, go to Settings > Security > Reset Password."),
    (["refund", "money back"],
     "Refunds are processed within 5-7 business days after approval."),
    (["hours", "open"],
     "Our support hours are Monday-Friday, 9am-6pm EST."),
]
FALLBACK = "Sorry, I didn't understand that. Press 1 for billing, 2 for account help, 3 for a human agent."


def respond(message):
    text = message.lower()
    for keywords, reply in RULES:
        if any(k in text for k in keywords):
            return reply
    return FALLBACK


if __name__ == "__main__":
    tests = [
        "how do I reset my password",
        "I want my money back for this refund",
        "my card was charged twice by mistake and I'm really upset",
    ]
    for t in tests:
        print(f"> {t}")
        print(respond(t))
        print()
