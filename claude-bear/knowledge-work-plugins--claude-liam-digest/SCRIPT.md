# Does Claude's Digest Skill Watch You All Week? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-digest`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone wonders whether Claude was quietly watching everything while they were away. It wasn't. Liam is here to take you through what the digest skill actually does, step by step." | writer types "All week I was away — / was Claude quietly / watching?", hesitates on "watching", corrects to "waiting" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that Claude has been quietly aware of everything happening across your sources, so asking for a digest just taps into something it already knows. But nothing runs until you ask — and even then, if you don't say how far back to look, it defaults to just one day. Come back from a week away, ask for a digest without saying "weekly," and what surfaces is Friday. Six days of decisions and mentions never make it in. | an "AWARE ALL WEEK" figure with a scattered eye-mark cluster, struck; an "ASK → DEFAULT DAILY" card lit instead |
| B02 | 3 mechanism / **4 anchor planted** | What the skill actually does: read one instruction file, then follow its steps in order — gather mentions and action items across your connected sources, group updates by project, and check whether you asked for daily or weekly. Watch the anchor: it's Monday, you've been gone all week, and you ask for a digest without naming a window. The file's default line fires — daily, unless told otherwise — and what comes back covers one day: yesterday's mentions, yesterday's decisions. The other six days sit outside it. | THE ANCHOR — four cards (ASKED / READS FILE / STEPS RUN / RETURNED), a "MONDAY, WEEK AWAY" token traveling through all four, landing beside a seven-box week strip with only the last box lit |
| B03 | **4 anchor payoff** / 5 both directions | That one day is what the file returns every time the window is left unset — ask again tomorrow without saying weekly, and you get today, identically, every time. But say weekly once, and the same file runs the same steps across all seven days instead, surfacing everything the daily default left out. Same file, same steps — what changes is only the word you remembered to say. | THE ANCHOR RETURNS, condensed; splits into two week strips: one box lit ("still unset — same default") and all seven lit ("said weekly — same steps, wider window") |
| **BCRY** | **6 carry-out** | A Claude digest isn't Claude quietly watching all week — it's a file that runs when you ask, and unless you say "weekly," it hands you one day and calls it done. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Run the digest skill on your own connected sources without saying whether you want daily or weekly, and see which window it defaults to. Then run it again, this time saying "weekly" explicitly, and compare what surfaces that the first pass missed. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Does Claude's Digest Skill Watch You All Week? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "quietly aware... taps into something it already knows"; falsified by "come back from a week away, ask without saying weekly, and what surfaces is Friday — six days never make it in" |
| Exactly one inference flag | none needed — every claim here is stated directly from the source sheet's own facts (no inference leap) |
| One anchor, planted early, paid off late | B02 -> B03 (Monday, week away, unnamed window: asked → reads file → steps run → returned "Friday only", then paid off into "ask again unset — same one day" / "say weekly — all seven") |
| Both failure directions | B03: "window left unset, same default every time" (holds) / "say weekly, and the window flips to all seven days" (flips) |
| No design judgment | B01/B02/B03 describe what the skill does and where its default sits; no verdict on whether defaulting to daily was the right design choice |

## Deliberately not claimed

- **Not that defaulting to daily is a flaw.** The source's BVDT framed
  "know the limit: only what the file says" as a verdict on the skill's
  reliability; Plain keeps only the mechanism (it defaults to daily unless
  told otherwise) and its two failure directions, no ruling on whether the
  default was the right call.
- **Not a claim about any specific team, tool, or connected source.** The
  anchor (Monday, a week away, asking without naming a window) is a
  generic, illustrative scenario — no invented dashboard or integration
  beyond what the source describes.
- **Not "the skill decides what matters."** The wrong-guess/falsification
  pair (B01) exists precisely to rule out the idea that Claude has private,
  standing awareness — it reads a file and runs steps against whatever
  window you specify, nothing it inferred independently.

## Handoff prompt (BHTF, read aloud)

> "Run the digest skill on your own connected sources without saying
> whether you want daily or weekly. See which window it defaults to. Then
> run it again, saying 'weekly' explicitly, and compare what surfaces that
> the first pass missed."

Why it's worth running: watching exactly how much silently disappears
behind an unset default — and how simply naming the window recovers it — is
the fastest way to see that the digest runs from a written file with a
stated default, not from continuous awareness, rather than just trusting
that it does.

---
**GATE P — signed:** ______________________ (human)
