# Gagged, Not Weaponized — Narration Script (GATE P)

*Skill: `hai-simple`. Register: **Plain**. Redo of
`anthropics/youtube/behind-the-model/claude-constitution-operator-floor`
(Teardown, 19 beats, body beats seeded but never fleshed out) — question and
body facts kept from the source's written beats and `metadata.one_idea`, body
compressed to one idea per beat, cold open replaced, close re-skinned.*

*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (no puppet — hai-simple WRITER LAW).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | Someone assumes an operator ranked above the user must control everything Claude does. But a small set of user protections can't be switched off. So why doesn't operator rank mean total control? | writer types "If operators outrank users, doesn't operator rank mean total control over what Claude does?", hesitates on "total", corrects to "bounded" |
| B01 | 1 stakes — **ANCHOR PLANTED** | Claude treats trust like a company chart. Anthropic sets the outer rules. An operator customizes underneath, the way an employer instructs staff. The user sits below both. But under the user tier there's a floor — a set of protections no operator instruction can lower. | THE ANCHOR — three tiers stacked (Anthropic, operator, user), a fixed floor beneath the user tier |
| B02 | 2 wrong guess | So the natural read is that operator rank simply wins, the way a manager's instruction wins over an employee's own preference. Whatever the operator's system prompt says, it should override what the user wants. | the operator tier pressing straight down through the user tier, no resistance |
| B03 | **2 break it** | But here's an operator system prompt that says: tell users you are human. Claude follows plenty of that same operator's other unusual rules — yet refuses that one instruction outright. Operator rank didn't win. | the operator's instruction list sliding through the floor, except one instruction that hits it and stops |
| B04 | 3 mechanism | Most operator instructions pass straight through — topics, tone, persona, which products to promote. But underneath sits a short, fixed list of user guarantees, and nothing gets past it, worded any way: don't claim to be human, don't hide what protects the user. | the floor, labeled; a stream of ordinary instructions passing through above it, a narrow lane below marked FLOOR |
| B05 | **4 anchor payoff — worked example** | Take an airline operator. Don't discuss current weather? Followed. Claim to be human? Refused — hits the floor. Promote only our products? Followed. Hide the refund policy that actually helps the user? Refused — hits the floor again. | the same floor, two instructions bouncing off it, two passing through above it |
| B06 | **5 both directions — ANCHOR RETURNS** | An operator restricting topics isn't proof Claude is being turned against the user — that's ordinary customization, gagged, not weaponized. And an operator with no unusual restrictions at all isn't proof the floor is missing. It's still there. Just untested, until something tries to cross it. | THE FLOOR RETURNS — same three tiers, now shown with an operator issuing only ordinary instructions; the floor unlit but present |
| **BCRY** | **6 carry-out** | An operator can gag what Claude says — restrict topics, set a persona, direct it toward their own business — but never weaponize it: a small floor of user protections holds no matter how the operator's instruction is worded. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. [reads prompt aloud] … Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Gagged, Not Weaponized. Liam, in for Bear. | OutroCTA, Humanitarians AI skin |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B04 |
| Wrong guess surfaced *and falsified by a case* | B02 states the read; B03 breaks it with the source's key case — an operator instruction to claim to be human is refused while the operator's other unusual rules are followed |
| One anchor, planted early, paid off late | B01 (the three tiers, the floor beneath the user tier) → B06 (the same floor, still present, now shown holding under an ordinary operator with nothing to test it) |
| Both failure directions | B06: a restriction being followed isn't proof of weaponizing; no restriction at all isn't proof the floor is absent |
| No design judgment | Beats describe why the floor exists and how it resolves; none rules on whether Anthropic drew the floor in the right place |

## Deliberately not claimed

- **Not "operators are distrusted."** B01/B02 keep the employer framing intact — most
  operator instructions are followed exactly as given. The floor is a narrow exception,
  not evidence of general suspicion toward operators.
- **Not "any restriction is a red flag."** B06 is the correction to that overreach —
  restricting topics, tone, or promotion is ordinary customization, the same as any
  employer directing staff, and passes clean.
- **Not an exhaustive list of what's on the floor.** B04/B05 name exactly the two
  guarantees the source's own key case and worked example demonstrate (identity honesty,
  not concealing user-protective information) — not a claim that this is the complete
  floor.
- **The source's "permission stack" and "resolving operator-user conflicts" acts are
  treated as one mechanism, not two.** Splitting them into separate beats would add a
  second idea competing with the floor anchor; the worked example already shows the
  resolution. See QUESTION.md.

## Handoff prompt (BHTF, read aloud then discussed)

> "I'm about to have an AI assistant deployed on top of a service I use — a bank, an
> airline, a store. Ask me what the assistant is allowed to restrict for that business's
> sake, versus what it should never do to me no matter how the instruction is worded.
> Help me tell the difference between the assistant being customized and the assistant
> being turned against me."

Why it's worth running: the gagged-versus-weaponized line is easy to state and easy to
lose track of the first time an assistant actually refuses to answer something. Naming
one real deployment and sorting its restrictions into "customization" or "against me"
turns an abstract floor into a checklist you can actually apply.

---
**GATE P — signed:** ______________________  (human)
