# Claude, Debug Zoom Integration. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `claude-liam` Teardown batch build).
Register: **Plain**. 7 beats ≈ 1:40.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** BrutalistHesitantWriter (Remotion, humanitarians palette).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone assumes that when a Zoom integration breaks, Claude just jumps in and fixes it right away. It doesn't. The real question: does Claude isolate which layer failed before it touches any code?" | writer types "A Zoom join breaks — does Claude just fix it right away?", hesitates on "fix", corrects to "isolate" |
| B01 | 1 stakes / 2 wrong guess falsified / 4 ANCHOR PLANTED | Take a Zoom integration where the join button spins and never connects. Before Claude touches anything, it reads `debug-zoom-integration` — a `SKILL.md` file naming five places the failure could be: authentication, webhooks, the SDK join call, MCP transport, or the real-time media stream itself. | THE ANCHOR — five layer cards draw in left to right, none lit; the "join button spins, never connects" scenario types in beneath |
| B02 | 3 mechanism | The skill's steps run in a fixed order: check one layer, confirm it's clean, move to the next — never skip ahead, never guess which layer to check first. | the five-card row; a check mark lands on each card in turn, left to right |
| B03 | **4 anchor payoff / 5 both directions** | Auth checks out. Webhooks check out. SDK join checks out. The break is in MCP transport — and only now, with the layer confirmed, does the skill propose a fix. Ask it about something outside those five layers, and it has nothing to add; the same steps just don't run. | THE ANCHOR RETURNS — checks land on auth/webhooks/SDK-join; MCP Transport gets the one accent mark and the fix note; a sixth "outside the five" card stays blank |
| **BCRY** | **6 carry-out** | Before Claude proposes a fix, it isolates which layer actually broke — same order, every time, and nothing outside that list. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. [reads generalized isolate-before-fix prompt] … Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Debug Zoom Integration. Liam, in for Bear. | OutroCTA, humanitarians palette |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00–B01; the ordered-check mechanism waits until B02 |
| Wrong guess surfaced *and falsified* | B00 states "fix it right away"; B01–B03 falsify it by showing the fix only lands after four layers are checked in order |
| One anchor, planted early, paid off late | B01 → B03 (the five-layer stack, the "join button spins" scenario) |
| Both directions | B03: the confirmed-break case (MCP transport) and the outside-scope case (nothing to add) |
| No design judgment | B03/BCRY state the sequencing fact (isolate before fix) — never a verdict on whether that much process is good or bad |

## Deliberately not claimed

- **Not a claim about real Zoom failures.** The "join button spins, break
  is in MCP transport" scenario is this reel's invented anchor, built to
  make the five layers and the isolate-first order visualizable.
- **No source truncation repeated.** The source sheet's B03/BVDT/BHTF
  narration truncate the skill's "use when…" clause mid-word; this script
  uses the complete sentence recovered from the source's own B00 fields.
- **No verdict on the skill's design.** The source's B03 ("what it gets
  right… what it bites") and BVDT ("Verdict") framings are Teardown
  judgment; Plain keeps the same mechanism as a sequencing fact only.

## Handoff prompt (BHTF, read aloud)

> "Before you propose any fix for this bug, walk me through every layer
> that could be responsible, and check them one at a time, out loud, in
> order — don't jump to a patch until you've isolated which one actually
> broke."

Why it's worth running: `debug-zoom-integration` only applies inside one
partner's Zoom plugin, which most viewers won't have installed — but the
isolate-before-fix habit it encodes transfers to any real bug in any Claude
coding session.

---
**GATE P — signed:** ______________________  (human)
