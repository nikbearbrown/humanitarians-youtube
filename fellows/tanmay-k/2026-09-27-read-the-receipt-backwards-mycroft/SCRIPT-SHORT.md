# SCRIPT — *Read the Receipt Backwards* (Short, 9:16)

## Continuity: one receipt, one story (Tanmay, 2026-09-28: "ensure these are in sync… not 2-3 beats stitched together")

**Words:** every beat opens on the one before it.

| Cut | The join |
|---|---|
| S01 → S02 | "Morgan never saw it." → "**So** now I read receipts backwards." |
| S02 → S03 | the question → the **bottom** line first ("The agent line was checked…") |
| S03 → S04 | "stopped before anything else runs." → "Then, while making this video, I found **another line like that**." |
| S04 → S05 | "compared in one spelling." → "**Both of those receipts looked perfect.**" |
| S05 → S06 | "…like the ones on the rest of this receipt." → "**Which leaves one line** on mine." |

**Picture:** from S02 on it's one receipt, and each beat opens in exactly the state the last one ended in.

| Cut | State carried across |
|---|---|
| S01 → S02 | the one scene change: the false receipt (hook) → the receipt the method reads |
| S02 → S03 | all lines pending; the sweep has just finished |
| S03 → S04 | agent + person stamped, person in focus |
| S04 → S05 | + category stamped |
| S05 → S06 | + amount, date, path stamped; sealed |
| S06 → S07 | every line stamped except merchant, which is boxed "carried · not checked"; then the end card |

Measured after render: last frame vs next first frame at every cut (as for the topic Short).


**Draft 1, 2026-09-28.** A short-only script (standing rule: a Short is one complete story, never
long-form beats stitched together). The same receipt, portrait: the hook, the move, two lines proven
live, the turn, the honest open line, and the ending, which answers the hook and points to the full
film. ~240 words, about 1:20. Years and money are written in words for the voice; the screen keeps
digits.

### S01 · HOOK, the false receipt
> Hi, this is Tanmay Kulkarni, in for Humanitarians AI. This receipt came out of an early version of my own build. An AI agent bought forty-two dollars and fifty cents of groceries, and the receipt says Morgan approved it. Morgan never saw it.

*On screen:* the Morgan receipt (badge RECONSTRUCTION · EARLY VERSION), `morgan-02` in focus. *Refs:* B7, B4.

### S02 · THE MOVE
> So now I read receipts backwards. Start at the bottom, and for every line, ask one question. Which step checked this, before it was written down?

*On screen:* the canonical receipt, all lines pending; the sweep runs bottom to top. *Refs:* G2.

### S03 · THE PERSON LINE
> The agent line was checked: registered, and verified. In that early version, the person line wasn't. Nothing compared who the agent belongs to with who it said it was buying for. Now one step does, and Devon's agent buying "for Morgan" is stopped before anything else runs.

*On screen:* `agent_id` stamped; `consumer_id` in focus; live terminal (v2): `('REJECTED', 'agent_consumer_mismatch')`; stamp "ownership check". *Refs:* B6, B7, B8.

### S04 · THE CATEGORY LINE
> Then, while making this video, I found another line like that. Devon's rule covered groceries until the end of twenty twenty-six. An order dated after that should come back to Devon. Spell the category with a capital H, and the lookup missed the rule, the demo's gate said yes, and it went through. Now every category is compared in one spelling.

*On screen:* Devon's rule chips; live terminal on the original build: `('COMPLETED', 'authorization_gate')`; then v2: `('ESCALATED', 'outside_timeframe')`; stamp "permissions · one spelling". *Refs:* B9, B10.

### S05 · THE TURN, the seal
> Both of those receipts looked perfect. Mastercard describes its record as tamper resistant, and a seal like that can show nobody changed the record. It can't make the lines true. That part comes from the checks before it, like the ones on the rest of this receipt.

*On screen:* the seal lands; the verbatim quote "a tamper-resistant record of what a user authorized" with its source; at "like the ones on the rest of this receipt", the amount, date and path stamps land (validation + limit, validation + window, path taken). *Refs:* M1, G1, B16, B12, B13.

### S06 · THE OPEN LINE, and the ending
> Which leaves one line on mine. Merchant. It's carried, not checked, because Mastercard hasn't published how that check works. So the build says so, instead of guessing. Every line is either earned, or honestly marked. The full video reads the whole receipt, and it's linked below.

*On screen:* the merchant line's open box "carried · not checked"; the M8 quote. Every line is now stamped or honestly boxed. *Refs:* B15, M8, M10.

### S07 · END CARD (silent, 3.5s)
> 

*On screen:* title card "Read the Receipt Backwards.", @HumanitariansAI, "Tanmay Kulkarni, in for Humanitarians AI".
