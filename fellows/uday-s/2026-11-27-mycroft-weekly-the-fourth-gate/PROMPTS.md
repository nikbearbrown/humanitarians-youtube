# PROMPTS — The Fourth Gate

The three composer beats, verbatim as they appear on screen.

## B00 — cold open

```
claude "I'm signing this promotion off — what is wrong with the evidence?"
```

Answered:
- three gates cannot fail as written
- a fourth has the same defect, unnamed
- and one of the three is the opposite bug

## B03 — the week's ask

```
claude "run every gate test against something broken — which ones still pass?"
```

Answered:
- run each gate against a planted defect
- outside the repository, read-only
- report what cannot fail, and why

## B10 — your turn (the scaffolded task)

```
claude "plant the exact defect this check exists to catch, then run it — what is the exit code?"
```

With the discriminator on screen:
- **GOOD:** non-zero, naming what it caught
- **BAD:** zero, or zero no matter what
- a check never run against a defect is a guess

## Why the task is shaped this way

It is one command, it needs no knowledge of mycroft, and both outcomes teach
something. The phrasing — *plant the exact defect this check exists to catch* —
matters: running a check against working code tells you nothing, which is how
four gates in this repository survived review for weeks.

It is also the task that produced this episode's two original findings. Gate 4's
self-match only became visible once the script was deleted and the real TODOs
removed; gate 6's `exit 1` only became visible once it was run at all.
