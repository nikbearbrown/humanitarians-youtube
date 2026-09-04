# Content Creation Isn't One Post for Everywhere. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-content-creation`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00, B01, B02, B03, BVDT, BHTF, BOUT). Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes this skill just writes a blog post. It doesn't — it drafts marketing content across six channels, each formatted its own way: blog, social, email, landing pages, press releases, case studies." | Writer types "Can Claude write my blog post?"; "blog" hesitates and corrects to "marketing", "post" hesitates and corrects to "content" |
| B01 | 1 anatomy | This kind of writing is built from something called a skill — a folder Claude reads before it works. Inside is one file, written in plain language, that spells out exactly what each channel's version needs to look like. Claude reads the file, then follows it. The file is the whole program. | a folder opens to reveal SKILL.md (highlighted), references/, scripts/ |
| B02 | 2 mechanism — pipeline | The steps run in order: read the file, work through each step exactly as written — draft the piece, fit it to the channel's format, then return the result. Nothing runs out of sequence unless a step itself says so. | three cards: Read SKILL.md -> Draft + fit to channel -> Return result |
| B03 | 3 constraint | For this skill, there are exactly six formats it covers: blog posts, social media, email newsletters, landing pages, press releases, and case studies — each with its own shape, from SEO-optimized copy on a blog to a headline and a call to action on a landing page. Ask for a seventh kind of writing and there's no format that covers it. | six format rows filling in with checkmarks; a boundary line, faint field beyond captioned "nothing outside this list" |
| **BCRY** | **4 carry-out** | Content creation here isn't one post copied everywhere — it's six different formats, each built to its own channel's rules, from one instruction file. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: I just published a new blog post about backyard composting. Give me a short social media post, a two-line email subject and preview, and one landing-page headline with a call to action — built for each channel, not the same paragraph three times. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Content Creation Isn't One Post for Everywhere. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-content-creation`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Content Creation." — a skill-teardown title | reframed as an actually-askable question: does content creation mean one piece of copy reused everywhere, or something channel-specific |
| Facts | `content-creation` drafts marketing content across channels — blog posts, social media, email newsletters, landing pages, press releases, and case studies; use it for channel-specific formatting, SEO-optimized copy, headline options, or calls to action; a skill = a folder Claude reads before acting; SKILL.md is the instruction set; execution is linear (read -> execute steps in order -> return); the boundary is only what the file specifies gets covered, same input same output every run | unchanged |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("blog post" -> "marketing content") |
| Register | Teardown — B03 named itself "the Teardown moment" and graded the skill ("what it gets right… what it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the same six-format boundary as a fact, no grading language; BCRY states the mechanism as a carry-out sentence, not a verdict |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice |
| BVDT -> BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, "Hola, Liam" skin | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | garbled truncated string ("I want to draft marketing content across channels — blog posts, social media, em. Read the content-creation skill and walk me through what you will do before you do it.") referencing a skill file the general viewer won't have installed | rewritten as a clean, genuinely runnable prompt that asks Claude directly to draft the same announcement across three channels and compare the shapes — same teaching point, no dependency on a plugin skill file the viewer doesn't have |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the source
was already all-Remotion (`ClaudeComposerAsk` × 2, three `SkillTeardown*` cards,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`) — so the NO-GENAI/NO-PANTRY LAW required
no substitution beyond the WRITER LAW and channel-skin row already require.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real stakes before B01's anatomy or B02's pipeline |
| Wrong guess surfaced | B00 ("blog post" -> "marketing content") |
| No design judgment | B03 states the six-format boundary as a fact ("nothing outside this list gets checked"), not a critique of the skill's design; BCRY states the mechanism, not a verdict on whether six formats is the right number |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that one draft is silently reused across channels.** The skill's whole
  point is that it never does this — every format listed gets its own pass.
  No claim is made that the underlying facts or offer differ per channel, only
  the shape of the writing.
- **Not a claim that six is a limit on marketing writing in general.** The
  source scoped the skill to "only what the file specifies"; this redo keeps
  that boundary as stated fact, not as a limitation to be argued with.
- **Not a verdict on whether six formats is the right set.** The source's B03
  graded the skill ("what it gets right… what it bites"); this redo removes
  that framing per Plain register and states the boundary without grading it.

## Handoff prompt (BHTF, read aloud)

> "I just published a new blog post about backyard composting. Give me a
> short social media post, a two-line email subject and preview, and one
> landing-page headline with a call to action — built for each channel, not
> the same paragraph three times."

Why it's worth running: it puts the reel's whole claim to a direct test —
paste it, and check whether the three outputs actually differ in shape
(length, structure, what leads) or whether it's the same paragraph wearing
three labels.

---
**GATE P — signed:** ______________________  (human)
