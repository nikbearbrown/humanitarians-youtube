# SCRIPT.md — Right Format, No Function. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-example-command` (Teardown review of the `example-command`
reference skill, `claude-plugins-official`) — question, facts, and body
argument carried over; narration re-registered to Plain (explain, then stop,
judgment removed); cold open replaced with the BrutalistHesitantWriter; close
carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
A newcomer expects that dropping the reference file into the skills folder
means the command already works. It doesn't — the file is a template, not a
working command. So what actually makes a slash command run?

## Act I — the shortcut, and the guess

**B01 — the shortcut**
You want a shortcut: type a slash, a name, maybe a word or two after it —
and have Claude do the same specific thing, the same way, every time.

**B02 — the wrong guess**
So it's easy to assume that once a file like that exists — right name,
right setup — the command already does something. That's the guess most
people building their first one make.

**B03 — break it**
Try it: run the reference example that ships with Claude's plugins, and
here's what comes back — a plain template. Parse the input. Perform the
action. Report the result. No folder created, no file touched, no action
taken.

## Act II — the five fields

**B04 — five fields**
Underneath, the file is five pieces of setup: a name, a description, an
argument hint, a list of allowed tools, and a model choice — one short
block of text at the top of the file.

**B05 — the anchor, planted ($ARGUMENTS)**
Here's the one that matters most: whatever you type after the command's
name lands, word for word, in a single spot inside the file — a slot called
ARGUMENTS. Type slash-greet Nik, and Nik shows up there, exactly as typed.

**B06 — argument-hint**
The argument hint is what a user sees before they've typed anything at
all — the little reminder text next to the command's name, showing the
kind of input it's expecting.

**B07 — allowed-tools**
Allowed tools does something else entirely: it pre-approves a specific
list of tools for this one command, so Claude can use them without asking
permission each time — but only for this command, not everywhere.

**B08 — model override**
And model lets this one command run on a different model than your
default conversation — a faster one for something simple, a stronger one
for something that needs more reasoning.

## Act III — the body, and the anchor's payoff

**B09 — the body pattern**
The body of the file follows the same three-step shape: parse whatever
arrived in ARGUMENTS, perform the actual work, then report back what
happened. In the reference file, that shape is described — not carried
out.

**B10 — the anchor returns**
So back to ARGUMENTS: type slash-greet Nik, and Nik really does arrive,
letter for letter, right where the file says it will. What doesn't happen
automatically is anything using it — that part, you still write yourself.

**B11 — one flag, and the legacy layout**
One flag: parse, perform, report is this file's own chosen shape, not a
rule Claude enforces elsewhere. The layout also has an older sibling — a
single file, commands slash name dot m d — which loads exactly the same
way; only the folder differs.

## Act IV — both directions

**B12 — direction A**
So matching the format perfectly doesn't prove the command does anything
real. The reference file matches it exactly, and running it still
produces only that template.

**B13 — direction B**
And skipping an optional field doesn't mean it's broken, either. Leave
out the argument hint, and the command still runs — users just won't see
that hint before they type.

## Close

**BCRY — carry-out**
Five fields and one slot called ARGUMENTS are the scaffold of a slash
command. Matching the format gets you the shape — what happens when
someone actually runs it is still yours to write.

**BHTF — your turn**
Your turn. Paste this into Claude: build me a real slash command called
slash word-count. It should take a file path as its required argument,
count the words in that file, and report the total back to me. Show me
the exact SKILL.md file you'd write for it, and then explain, in plain
terms, what ARGUMENTS actually contains the moment I run it.

**BOUT — outro**
Right Format, No Function. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00–B01 | the shortcut you want, before any mechanism |
| Wrong guess | B00 → B02 → B03 | "it already works" corrected, then falsified by running it |
| Mechanism | B04–B09, B11 | five fields, ARGUMENTS, argument-hint, allowed-tools, model, body pattern, legacy layout |
| Anchor | B05 → B10 | ARGUMENTS planted (verbatim injection), returned to as what still needs code |
| One flag | B11 | parse/perform/report is this template's shape, not a Claude rule |
| Both directions | B12–B13 | perfect format ≠ real action; missing optional field ≠ broken |
| Carry-out | BCRY | one sentence, survives repetition |

## Beat-count note (redo)

Source is 7 beats (Teardown chassis: B00 host cold open, B01 anatomy, B02
design, B05 teardown, BVDT verdict, BHTF handoff, BOUT outro) carrying three
very dense body beats (~35–65s each, several distinct facts per beat).
hai-simple's spine has no puppet host and no verdict-recap slot, so: B00 is
replaced by the BrutalistHesitantWriter; the three dense Teardown body beats
(B01 anatomy, B02 design, B05 teardown) are decomposed into 13 one-idea
GRAPHIC beats (B01–B13) at ≤150 words/beat, preserving every fact — the five
frontmatter fields, the ARGUMENTS injection point, argument-hint, allowed-tools
pre-approval, model override, the parse/perform/report body pattern, and the
skills/ vs. commands/ legacy equivalence; the Teardown "gaps" list (missing
model guidance, implicit ARGUMENTS parsing, Bash blast radius, no /help
guidance) is dropped as design judgment, not carried into Plain — the
WRONG-GUESS/BREAK-IT (B02–B03) and BOTH-DIRECTIONS (B12–B13) beats replace it
with facts framed as newcomer-useful distinctions instead of verdicts on the
template's design. BVDT (verdict) is dropped; the source's BHTF/BOUT facts
(handoff prompt, outro title) are kept and re-registered to the Humanitarians
AI skin. Result: B00 + 13 body + BCRY/BHTF/BOUT = 17 beats. Logged per
BUILD-LOG.md.
