# PROMPTS — It Never Ran

The three composer beats, verbatim as they appear on screen.

## B00 — cold open

```
claude "I switched to safe_load_all and the result is identical. why?"
```

Answered:
- the YAML batch had never executed
- a correct fallback hid it for five weeks
- and the fix had a second trap in it

## B03 — the week's ask

```
claude "instrument the batch runner — prove whether it executes at all, before changing more"
```

Answered:
- confirm the batch path actually fires
- confirm no fallback fired
- only touch lines I wrote

## B10 — your turn (the scaffolded task)

```
claude "break the fast path of this check deliberately — does anything in the output change?"
```

With the discriminator on screen:
- **GOOD:** the run says which path it took
- **BAD:** identical output either way
- a silent fallback is an untested primary

## Why the task is shaped this way

It is falsifiable in one run, needs no knowledge of mycroft, and produces an
answer that is immediately actionable either way. A viewer who gets the BAD
result has learned something about every green run their project has had since
that fallback was written — which is exactly what this episode is about.
