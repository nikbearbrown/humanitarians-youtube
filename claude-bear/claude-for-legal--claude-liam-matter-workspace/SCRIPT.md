# SCRIPT.md — Claude, Matter Workspace. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-matter-workspace` (Teardown, skill-teardown format) —
question and true facts carried over; narration re-registered to Plain
(explain, then stop); cold open replaced with the BrutalistHesitantWriter;
close carries the Humanitarians AI skin.

**Source-fidelity note:** the source SKILL.md is not reachable from this
machine (see QUESTION.md / BUILD-LOG.md). Unlike the `matter-briefing`
sibling, the source's own beat_sheet.json narration does not spell out what
matter-workspace's per-matter deliverable is — only generic skill anatomy.
The one specific, load-bearing fact it does state is the design tell: "The
skill never reads across matters unless Cross-matter context is on in the
practice-level CLAUDE.md." Every specific claim below about isolation traces
to that sentence. Nothing about matter-workspace's actual per-matter output
is invented.

## B00 — cold open (BrutalistHesitantWriter)
You'd guess Claude already knows every matter you have, all blended
together. It doesn't — by default it stays inside just this one. Let's
see when that changes.

## Act I — the wrong guess

**B01 — Sounds like one shared pool**
Hear "Claude has a matter-workspace skill" and it sounds like every matter
you've ever discussed folds into one shared pool Claude can draw from
anytime.

**B02 — Broken, with a case** (pays off B00)
But open a brand-new matter and ask Claude about specifics from a
different case — it can't see them. By default, matter-workspace keeps
every matter walled off from every other one.

## Act II — the mechanism

**B03 — One file** (ANCHOR PLANTED)
Here's what a skill actually is: one file. matter-workspace is a folder
holding a single SKILL.md — plain-language instructions Claude reads
before it works on a matter, no hidden logic. The file is the program.

**B04 — Read it, then follow it in order**
Claude reads that file's Steps section and works through it in order —
linear, no branching unless a step itself says to branch.

**B05 — The one constraint worth knowing**
And here's the constraint worth knowing: by default, matter-workspace
never reads across matters. It only draws on another case once
cross-matter context is switched on in the practice's CLAUDE.md.

**B06 — The anchor returns** (ANCHOR PAYOFF)
So matter-workspace never gave Claude one shared pool across every case.
It just guarantees that every time it runs, Claude reads that same file
and stays inside the matter it's pointed at — unless that one switch is
on.

## Act III — both directions

**B07 — Neither one is proof**
Watching Claude answer correctly inside just one matter doesn't prove it's
blind to every other case — cross-matter context might already be
switched on. And Claude missing a detail from another matter doesn't
prove isolation is working — it might simply not have been asked.

## Close

**BCRY — carry-out**
A matter-workspace skill doesn't blend your cases into one pool — by
default it stays inside the matter it's pointed at, and it only reads
across matters once the practice turns that on in CLAUDE.md.

**BHTF — your turn**
Your turn. Paste this into Claude: read the matter-workspace skill and
tell me — by default, can you see anything from my other matters? Then
tell me exactly what would have to change, and where, for that to happen.

**BOUT — outro**
Claude, Matter Workspace. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | "a matter-workspace skill" sounds like one shared pool across every case |
| Wrong guess | B00 → B02 | "every" corrected to "just this one"; broken with the new-matter, can't-see-the-other-case case |
| Mechanism | B03–B05 | one file, read top to bottom, isolated-by-default with a named switch |
| Anchor | B03 → B06 | matter-workspace's single SKILL.md, planted then returned to |
| Both directions | B07 | staying inside one matter proves nothing about the switch; missing a detail proves nothing about isolation working |
| Carry-out | BCRY | one sentence, survives repetition |

## Beat-count note (redo)

Source is 7 beats (B00, B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF your-turn, BOUT outro) — the same compact skill-teardown
format as the `matter-briefing` sibling, with no explicit wrong-guess,
anchor, or both-directions beat. hai-simple's spine requires all three as
their own beats (WRONG-GUESS LAW / ANCHOR LAW / BOTH-DIRECTIONS LAW), so
this redo expands identically to that sibling: B01 (stakes) and B02 (wrong
guess, broken) are new; B03/B04/B05 carry the source's anatomy/pipeline/
design-tell facts across to the anchor; B06 is a new anchor-payoff beat;
B07 (both directions) is new. Result: B00 + 7 body beats + BCRY/BHTF/BOUT =
11 beats. No new legal-specific fact was invented anywhere in this
expansion beyond what the source's own B03 design tell already
established.

## One-flag audit

No inference-flag beat: every claim here traces either to the generic,
verifiable mechanism of a Claude skill (folder + SKILL.md, read-then-
execute, specification semantics) or to the source's own stated design
tell (cross-matter isolation, on by exception via CLAUDE.md). Nothing in
this script asserts what matter-workspace's actual per-matter output looks
like, since the source never states that either.
