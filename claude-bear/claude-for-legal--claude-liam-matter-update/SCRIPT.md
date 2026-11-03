# SCRIPT.md — Claude, Matter Update. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-matter-update` (Teardown, a skill-explainer reel under
`anthropics/claude-for-legal/`) — question, facts, and body argument carried
over; narration re-registered to Plain (explain, then stop); cold open
replaced with the BrutalistHesitantWriter; close carries the Humanitarians AI
skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumes Claude remembers how their firm handles a case update, the
way a person would after doing it a few times. It doesn't remember anything —
so how does it know the steps at all?

## Act I — Stakes and the anchor

**B01 — Matters keep changing**
Every open matter keeps changing — a new filing, a settlement offer, a
missed deadline — and each change has to get written down the same way, on
every case.

**B02 — The anchor, planted**
Hold on to one case: Case forty-four seventy-one. A settlement offer just
came in, and it needs to go on the record.

## Act II — The wrong guess, and breaking it

**B03 — The easy assumption**
So the easy assumption is that Claude picks up your firm's habits the way a
new paralegal would — use it a few times, and it just remembers how you do
things here.

**B04 — Break it**
Open a brand-new conversation about a matter Claude has never touched, and
ask for the same kind of update. The same steps run immediately. There was
nothing to remember between conversations.

## Act III — The mechanism

**B05 — A skill is a folder**
What's actually there is a skill — a folder Claude reads before it acts.
This one is called matter-update.

**B06 — The one instruction**
Inside it, one instruction, in plain language: append a dated event to the
matter's history file, and refresh the log row to match.

**B07 — Five triggers**
It fires for five kinds of change: a new development, a status change, a
risk re-assessment, a deadline shift, a change in settlement authority.

**B08 — Read, then act**
Claude reads that file first, every single run, then follows the steps in
order — linear, no branching unless a step says so.

## Act IV — The anchor pays off, and both directions

**B09 — The anchor returns**
Back to Case forty-four seventy-one: the offer becomes a dated event in the
history file, and the log row updates to match — the file's recipe, not a
memory of this case.

**B10 — Direction A**
Ask for exactly what the file describes — a dated event, a refreshed row —
and it runs the same way, every time, on any matter.

**B11 — Direction B**
Ask for something the file never mentions — a strategy call, a new field, a
judgment about risk — and there's nothing to guess from. It only does what's
written.

## Close

**BCRY — carry-out**
Claude's skill isn't a memory of your firm's habits — it's a file it reads
fresh, every single time.

**BHTF — your turn**
Your turn. Here's the prompt — read it with me. Ask Claude: before you make
any change, read your instructions for this task in full, and tell me, step
by step, exactly what you're about to do — which file changes, and what you
won't touch unless I say so. Only then, go ahead. That clause matters —
explaining first turns Claude's next move visible before it happens.

**BOUT — outro**
Claude, Matter Update. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B01 | every matter keeps changing, logged the same way |
| Wrong guess | B03 → B04 | "it remembers our habits" corrected by a fresh, untouched matter running identically |
| Mechanism | B05–B08 | a skill is a folder; one instruction; five triggers; read-then-act |
| Anchor | B02 → B09 | Case 4471 planted with an incoming offer, paid off as the logged event |
| Both directions | B10 / B11 | exactly what's written runs reliably; anything the file doesn't cover gets no guess |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag. Every fact in this reel — the skill's name, its one
instruction (append a dated event, refresh the log row), its five triggers,
and its linear read-then-act execution — is carried over verbatim from the
locked source reel's narration (`claude-liam-matter-update`), which itself
paraphrases the `matter-update` SKILL.md directly. Nothing here is a new
inference introduced by this redo.

## Deliberately not claimed

No judgment on whether `matter-update` is well designed (the source's
Teardown "what it gets right / what it bites" framing is removed — this
reel states what the skill does and what it does not cover, not a verdict on
the design). No claim about what happens on a request outside the file's
scope beyond "there's nothing to guess from" — the reel doesn't speculate on
error behavior it hasn't observed.

## Beat-count note (redo)

Source is 7 beats (B00 cold open, B01 anatomy, B02 pipeline, B03 design
tell, BVDT verdict, BHTF handoff, BOUT outro) with no dedicated wrong-guess
or anchor beat. hai-simple's inherited laws (WRONG-GUESS, ANCHOR,
BOTH-DIRECTIONS, CARRY-OUT) are mandatory regardless of source shape, so the
body was expanded to 11 beats (B01–B11) to carry a stakes beat, a planted
anchor (Case 4471), the wrong guess and its falsifying case, the mechanism
split into its four component facts (skill-as-folder, the one instruction,
the five triggers, read-then-act), the anchor payoff, and both directions —
while introducing no fact beyond what the source's narration already
asserted. The source's BVDT (verdict) became BCRY (carry-out) with its
judgment language ("gets right" / "bites") replaced by the neutral
both-directions split (B10/B11). Logged per BUILD-LOG.md.
