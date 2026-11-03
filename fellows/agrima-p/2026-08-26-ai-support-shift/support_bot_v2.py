# support_bot_v2.py — Claude Code output: intent-style support bot (revision)
# Simplified illustration of what NLU-based matching does differently: it
# scores MEANING signals instead of one exact phrase, and it recognizes when
# a message is urgent/emotional enough to hand off to a human. This is NOT a
# real trained language model — it's a small heuristic standing in for one,
# built to show the SHAPE of the improvement, not claim to BE one.

INTENTS = {
    "reset_password": {
        "signals": ["password", "reset", "login", "locked out", "can't sign in", "forgot"],
        "reply": "To reset your password, go to Settings > Security > Reset Password.",
    },
    "refund": {
        "signals": ["refund", "money back", "charged twice", "double charge", "overcharged"],
        "reply": "Refunds are processed within 5-7 business days after approval.",
    },
    "hours": {
        "signals": ["hours", "open", "when are you available"],
        "reply": "Our support hours are Monday-Friday, 9am-6pm EST.",
    },
}
ESCALATE_SIGNALS = ["upset", "angry", "unacceptable", "mistake", "furious", "frustrated"]


def score(text, signals):
    return sum(1 for s in signals if s in text)


def respond(message):
    text = message.lower()
    best_intent, best_score = None, 0
    for name, info in INTENTS.items():
        s = score(text, info["signals"])
        if s > best_score:
            best_intent, best_score = name, s

    urgent = any(sig in text for sig in ESCALATE_SIGNALS)

    if best_intent:
        reply = INTENTS[best_intent]["reply"]
        if urgent:
            reply += " I can see this is frustrating — connecting you with a human agent now, just in case."
        return reply
    if urgent:
        return "This sounds like it needs a closer look — connecting you with a human agent."
    return "I'm not fully sure I understood — can you rephrase, or say 'agent' for a human?"


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
