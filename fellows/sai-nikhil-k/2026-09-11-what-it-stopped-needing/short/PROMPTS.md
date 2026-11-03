# PROMPTS — What It Stopped Needing

**There are no open generation slots in this reel.** Every beat is either a
registered Remotion composition rendered from props in `beat_sheet.json`, or a
still composed locally by `make_plates.py` from the author's own repository.
Nothing is pending an image model, a stock purchase, a Higgsfield clip or any
other external generation. No key is required and nothing costs money.

This file exists because GATE F requires it, and because two beats carry prompts
that matter — just not generation prompts.

---

## B00 — the on-screen typed ask

The `command` prop of `ClaudeComposerAsk`. It is **typed on screen and not
spoken**; the spoken words are `narration_text`, which differs.

> clauding 1.0.0 — a Swift menu bar app, rewritten in Python. 2,196 lines
> written, 2,843 deleted. Don't tell me it's leaner. Tell me which deletions were
> taste, which ones one design decision made unnecessary, and which one deleted a
> hazard instead of defending against it.

---

## B07 — the handoff prompt

The `command` prop of the second `ClaudeComposerAsk`. This one is **both typed on
screen and discussed in narration**, because it is the thing the viewer is meant
to take away and paste.

> Here is a rewrite I just finished. Go through everything it deleted and sort it
> into two piles: things I chose to remove, and things that stopped being
> necessary because of a decision made somewhere else. Then tell me which pile is
> bigger — and whether I have been taking credit for the second one.

---

## Why there is no Higgsfield beat

The three-way contract in `CLAUDE.md` applies per beat: CLI present and approved
→ clip; present and declined → free path; absent → free path silently. No beat in
this reel was authored as a candidate for an AI video clip. The one piece of
evidence is a rendering of a real interface, which must be exact — a generated
clip of "a menu bar" would be a picture of something that does not exist, in a
reel whose whole argument is about being precise regarding what is and is not
there.
