# READ-ALOUD — Gate P sheet (the work video's Short)

*Read the Receipt Backwards (Short)* · generated from `beat_sheet.json` (built from `SCRIPT.md`) by `make_read_sheet.py`.

**How to run Gate P:** read each beat out loud at speaking pace. Listen for rhythm and emphasis,
whether it feels like one complete story rather than clips, and whether the open line (S06)
sounds confident rather than apologetic, since it's the build stopping where the public record
stops. Mark anything that trips you in the box. A reply of "Gate P PASS" (with any notes) is
recorded verbatim in `PEDAGOGY.md`. No audio is generated before that.

## Say-it-right checklist (every item already checked against Kokoro's phonemes)

| Word | Should sound like | Where |
|---|---|---|
| Tanmay Kulkarni | as you say it; checked ✓ | S01 |
| Mastercard / Devon / Morgan | checked ✓ | S01, S03–S06 |
| "tamper resistant" | two words for the voice (Whisper-confirmed on the long); the on-screen quote keeps the hyphen | S05 |
| "a capital H" | the letter aitch; checked ✓ | S04 |
| money and years | "forty-two dollars and fifty cents", "twenty twenty-six"; checked ✓ | S01, S04 |

## Quotes: read exactly as written (verified verbatim on Mastercard's own pages, 2026-09-28)

| Beat | Quote | Source |
|---|---|---|
| S05 | "a tamper-resistant record of what a user authorized" (on screen; the narration says "tamper resistant") | Mastercard, Verifiable Intent page, Mar 5 2026 |

## The script

### [0:00] S01 · HOOK, the false receipt

_Tone: friendly name, then quiet: let "Morgan never saw it" land_

Hi, this is Tanmay Kulkarni, in for Humanitarians AI. This receipt came out of an early version of my own build. An AI agent bought forty-two dollars and fifty cents of groceries, and the receipt says Morgan approved it. Morgan never saw it.

_On screen: the Morgan receipt (badge RECONSTRUCTION · EARLY VERSION), `morgan-02` in focus._

> ☐ reads cleanly   ☐ note: ______________________

### [0:13] S02 · THE MOVE

_Tone: the method, slow and plain_

So now I read receipts backwards. Start at the bottom, and for every line, ask one question. Which step checked this, before it was written down?

_On screen: the canonical receipt, all lines pending; the sweep runs bottom to top._

> ☐ reads cleanly   ☐ note: ______________________

### [0:21] S03 · THE PERSON LINE

_Tone: steady; relief at "Now one step does"_

The agent line was checked: registered, and verified. In that early version, the person line wasn't. Nothing compared who the agent belongs to with who it said it was buying for. Now one step does, and Devon's agent buying "for Morgan" is stopped before anything else runs.

_On screen: `agent_id` stamped; `consumer_id` in focus; live terminal (v2): `('REJECTED', 'agent_consumer_mismatch')`; stamp "ownership check"._

> ☐ reads cleanly   ☐ note: ______________________

### [0:36] S04 · THE CATEGORY LINE

_Tone: real discovery; a little surprise at "with a capital H"_

Then, while making this video, I found another line like that. Devon's rule covered groceries until the end of twenty twenty-six. An order dated after that should come back to Devon. Spell the category with a capital H, and the lookup missed the rule, the demo's gate said yes, and it went through. Now every category is compared in one spelling.

_On screen: Devon's rule chips; live terminal on the original build: `('COMPLETED', 'authorization_gate')`; then v2: `('ESCALATED', 'outside_timeframe')`; stamp "permissions · one spelling"._

> ☐ reads cleanly   ☐ note: ______________________

### [0:55] S05 · THE TURN, the seal

_Tone: the turn: slower, reflective_

Both of those receipts looked perfect. Mastercard describes its record as tamper resistant, and a seal like that can show nobody changed the record. It can't make the lines true. That part comes from the checks before it, like the ones on the rest of this receipt.

_On screen: the seal lands; the verbatim quote "a tamper-resistant record of what a user authorized" with its source; at "like the ones on the rest of this receipt", the amount, date and path stamps land (validation + limit, validation + window, path taken)._

> ☐ reads cleanly   ☐ note: ______________________

### [1:10] S06 · THE OPEN LINE, and the ending

_Tone: warm and confident; the open line is a feature, not an apology_

Which leaves one line on mine. Merchant. It's carried, not checked, because Mastercard hasn't published how that check works. So the build says so, instead of guessing. Every line is either earned, or honestly marked. The full video reads the whole receipt, and it's linked below.

_On screen: the merchant line's open box "carried · not checked"; the M8 quote. Every line is now stamped or honestly boxed._

> ☐ reads cleanly   ☐ note: ______________________

### [1:25] S07 · END CARD (silent, 3.5s)

_Tone: silent end card: nothing to read_



_On screen: title card "Read the Receipt Backwards.", @HumanitariansAI, "Tanmay Kulkarni, in for Humanitarians AI"._

> ☐ reads cleanly   ☐ note: ______________________

_Estimated runtime 1:25 (270 words at 3.17 words/s, the voice's measured pace). Kokoro audio becomes the master clock once generated, and cues are then timed on the Whisper clock._

Every sentence traces to `FACTCHECK.md` (refs under each beat in `SCRIPT.md`). The mechanical pass
(`gate_p_lint.py`): no BREATH or ECHO flags; the only flags are
the NAME checklist above and the letter H (intended).
