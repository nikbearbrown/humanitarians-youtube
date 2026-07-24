# FACTCHECK — vox-allow-button

Source chapter: `claude-agentic-ai/chapters/10-designing-human-approval-gates.md`

---

## Claims audit

| Claim | Verdict | Source / note |
|---|---|---|
| Researcher clicked Allow 40 times in two days; does not know what any command did | ✓ | Chapter 10 opening scene, verbatim |
| "A gate that gets clicked without being read is not supervision — it is the performance of supervision." | ✓ | Chapter 10, verbatim |
| A gate that says only Allow? is missing six things: action, target, reason, risk, reversibility, what to check afterward | ✓ | Chapter 10: "A gate that functions as supervision must give the human six things" — listed verbatim |
| Without those six, the human is clicking a button, not making a decision | ✓ | Chapter 10: "A gate that says only 'Allow?' is a speed bump. The human's foot lifts slightly and comes back down. Nothing has been evaluated." |
| Dev team approval example: approval 31 deletes six functions, three power production config that was never read | ILLUSTRATIVE | Adapted from chapter 10 dev team example. Numbers illustrative. |

---

## Exclusions confirmed

- No four-response gate taxonomy (approve/redirect/pause/stop) in depth. Pass.
- No risk-reversibility 2x2 grid explanation. Pass.
- No James Reason Swiss cheese model. Pass.

---

## Terms table

| Term | Debut beat | Prior beat creating the need |
|---|---|---|
| approval gate | B02 (cold open graphic) | B01 shows the clicking behavior |
| performance of supervision | B02 | B01 shows the empty dialog |
| six elements | B04 (mechanism) | B03 question creates the need |
| action / target / reason / risk / reversibility / check afterward | B04 | B04 fills each in sequence |
