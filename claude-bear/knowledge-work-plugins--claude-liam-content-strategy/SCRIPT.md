# Content Strategy Isn't Writing Your Posts. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-content-strategy`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00, B01, B02, B03, BVDT, BHTF, BOUT). Carry-out written first (CARRY-OUT.md, GATE C).*

**Source note:** the source sheet's own narration had unfilled `>` template
gaps in B00, B03, BVDT, and BHTF (a batch-build defect, 2026-07-25), and its
`source_skill` path is not present in this local tree. The real facts below
were re-sourced from the actual public file,
`anthropics/knowledge-work-plugins/small-business/skills/content-strategy/SKILL.md`
on `github.com/anthropics/knowledge-work-plugins` — no fact here is invented.

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes this skill writes their social posts for them. It doesn't — it reads actual sales data from QuickBooks, PayPal, or Square and ranks what's selling, what's slowing, and what's trending, before any post gets written." | Writer types "Can Claude write my posts this week?"; "write" hesitates and corrects to "rank", "posts" hesitates and corrects to "sellers" |
| B01 | 1 anatomy | This kind of work is built from something called a skill — a folder Claude reads before it acts. Inside is one file that spells out exactly how raw sales numbers turn into a plan: pull the data, rank it, weigh the season, write the brief. Claude reads the file, then follows it. The file is the whole program. | a folder opens to reveal SKILL.md (highlighted), reference/gotchas.md, reference/examples/ |
| B02 | 2 mechanism — pipeline | The steps run in order: pull ninety days of sales data from QuickBooks, PayPal, or Square, rank it against seasonality, then hand back a thirty-day brief. Nothing skips ahead — the owner approves the brief before anything gets built from it. | three cards: Pull sales data -> Rank + weigh season -> Return brief for approval |
| B03 | 3 constraint | The brief itself has six parts: an executive summary, what to push hard, what to hold steady, what to reposition or pause, seasonal opportunities coming up, and recommended offers. That's the entire output — no calendar, no captions, no images. Those wait for the owner's approval and a separate skill. | six brief-section rows filling in with checkmarks; a boundary line, faint field beyond captioned "no calendar. no assets." |
| **BCRY** | **4 carry-out** | Content strategy here isn't Claude writing your posts — it's Claude reading your sales numbers and ranking what's working. It stops at the brief; building the posts is a separate step that needs your approval first. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. List your last month's top five sellers and slowest five — made-up numbers are fine. Ask Claude: rank these into what to push hard, what to hold steady, and what to reposition, and stop there, don't draft any actual posts yet. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Content Strategy Isn't Writing Your Posts. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-content-strategy`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Content Strategy." — a skill-teardown title, and its own narration had unfilled `>` template gaps in B00, B03, BVDT, BHTF | reframed as an actually-askable question: does content strategy mean Claude writes your posts, or ranks what's already selling |
| Facts | re-sourced from the real public SKILL.md (source sheet's own facts were incomplete/templated): pulls sales data from QuickBooks, PayPal, or Square (last 90 days); ranks top 3-5 performers, bottom 3-5 slow movers, trending up/down; layers in seasonality (user-provided or industry benchmark); builds a 30-day brief with six sections (executive summary, push hard, hold steady, reposition/pause, seasonal opportunities, recommended offers), 200-400 words; strategic output only, no calendar or assets; owner approves before it feeds `canva-creator`; a skill = a folder Claude reads before acting; SKILL.md is the instruction set; execution is linear | unchanged (now complete, since the source's own copy was missing them) |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting); narration text itself was broken (`"...Claude's job: >. What it gets right..."`) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("write my posts" -> "rank my sellers") |
| Register | Teardown — B03 named itself "the Teardown moment" and graded the skill ("what it gets right… what it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the same six-section boundary as a fact, no grading language; BCRY states the mechanism as a carry-out sentence, not a verdict |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice |
| BVDT -> BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, "Hola, Liam" skin | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | broken template string (`"I want to >. Read the content-strategy skill and walk me through what you will do before you do it."`) referencing a skill file and business connectors (QuickBooks/PayPal) the general viewer won't have installed | rewritten as a clean, genuinely runnable prompt: paste a short made-up sales list, ask Claude to rank it into push/hold/reposition and stop there — same teaching point, no dependency on a plugin skill or a connected accounting account |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the source
was already all-Remotion (`ClaudeComposerAsk` x2, three `SkillTeardown*` cards,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`) — so the NO-GENAI/NO-PANTRY LAW required
no substitution beyond the WRITER LAW and channel-skin row already require.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real stakes before B01's anatomy or B02's pipeline |
| Wrong guess surfaced | B00 ("write my posts" -> "rank my sellers") |
| No design judgment | B03 states the six-section boundary as a fact ("no calendar, no assets"), not a critique of the skill's design; BCRY states the mechanism, not a verdict on whether stopping at strategy is the right call |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that Claude never writes marketing content.** A separate skill
  (`canva-creator`, and the sibling `content-creation` skill covered in
  another reel) does exactly that. This reel's claim is scoped to what
  `content-strategy` itself produces: a ranked brief, not assets.
- **Not a claim that QuickBooks/PayPal/Square are the only possible data
  sources for a content plan in general.** The source scoped the skill to
  "only what the file specifies" (these three connectors); this redo keeps
  that boundary as stated fact, not as a limitation to argue with.
- **Not a verdict on whether requiring owner approval before the next skill
  is the right design.** The source's B03 graded the skill ("what it gets
  right… what it bites"); this redo removes that framing per Plain register
  and states the approval gate without grading it.

## Handoff prompt (BHTF, read aloud)

> "Here's what sold last month: [your top 5 sellers and your slowest 5,
> made-up numbers are fine]. Rank these into what to push hard, what to
> hold steady, and what to reposition or pause — and stop there, don't
> draft any actual posts yet."

Why it's worth running: it puts the reel's whole claim to a direct test —
paste a sales list, and check whether Claude actually stops at a ranked
brief instead of drifting into writing you a caption or a calendar.

---
**GATE P — signed:** ______________________  (human)
