# PROMPTS — Who Decides It's A Bug?

The two composer beats, verbatim as they appear on screen.

## B00 — cold open

```
claude "can AI replace beta testers for games and software?"
```

Answered:
- where a crash is the test: enormous scale
- where the answer must be judged: it discards failures
- where nobody can write the rule: nothing to automate

## B09 — your turn (the scaffolded task)

```
claude "for this testing tool: what is the oracle, and what happens to a failure it cannot judge?"
```

With the discriminator on screen:
- **GOOD:** a crash, or a spec you can point at
- **BAD:** "the AI figures out what's wrong"
- then ask what it does with failures it can't judge

## Why the task is shaped this way

Both halves map onto the framework. "What is the oracle" is B02's first card,
and it is answerable in one sentence by anyone who actually built the tool — so
a vague answer is itself the finding.

The second half is the one that changes decisions. Meta's own paper says the
tool cannot tell a real bug from a bad assertion without an automatable oracle,
and therefore discards failing tests. A viewer who asks their vendor what
happens to an unclassifiable failure, and gets no answer, has learned that their
green dashboard may be green for the same reason.
