# Claude Didn't Learn Bioinformatics. It Read a File. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of
`knowledge-work-plugins/claude-liam-nextflow-development`, Teardown register,
batch skill-teardown format — never built: source beats were all SLATE, no
audio or media). Register: **Plain**. 7 beats, matching the source's beat
count exactly. Carry-out adapted from the source's verdict beat (CARRY-OUT.md,
GATE C) — already close to factual, tightened and de-judged.*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no
generation). **Narrator:** Liam, Kokoro `am_onyx` (unchanged from source).

| Beat | Act | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer cold open | "Someone assumes Claude was trained to run Nextflow pipelines — trained, like it learned biology somewhere. Not quite. It was told: handed a skill file it reads before acting. So how does that actually work?" | Writer types "Claude was trained to run\nNextflow pipelines.\nWait — how does that\nactually work?"; "trained" hesitates and corrects to "told" |
| B01 | anatomy | A Claude skill is a folder Claude reads before it works. This one is nextflow-development. Its SKILL.md holds the whole instruction set, in plain language — no hidden logic. Claude reads it, then acts. The file is the program. | `SkillTeardownAnatomy` — file tree, SKILL.md accented |
| B02 | pipeline | The pipeline is in the Steps section. Claude reads each step in order and executes it. Linear — no branching unless the step says so. | `SkillTeardownPipeline` — Read → Execute → Return |
| B03 | mechanism, both directions | This one has a fixed job: run nf-core pipelines — rnaseq, sarek, atacseq — on sequencing data, whether that's your own FASTQ files or a public dataset pulled from GEO or SRA. Inside that job it's reliable: same steps, every run. Outside it — a pipeline the file doesn't name, a format it doesn't expect — it has nothing to fall back on. | `SkillTeardownMechanism` — "Where it holds, where it doesn't." |
| **BVDT** | **6 CARRY-OUT** | nextflow-development isn't trained knowledge — it's a file Claude reads before it acts. Run rnaseq, sarek, or atacseq, and it runs the same steps every time. Know the edge: only what the file says. | `ClaudeVerdictArtifact` — heading retitled "In short" (was implicit "Verdict") |
| BHTF | your turn handoff | Your turn. Paste this into Claude: read the nextflow-development skill, then walk me through what you will do before you run anything — what pipeline you'd use, what inputs it expects, and what you'd check first. Asking it to explain before acting is what surfaces the real constraint logic. | `ClaudeComposerAsk` — "Your turn." |
| BOUT | outro | Claude didn't learn bioinformatics. It read a file. Liam, in for Bear. | `OutroCTA` — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`knowledge-work-plugins`, Teardown, batch format) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Nextflow Development." (flat title, batch-generated) | Sharpened into a real carry-out question: does the skill mean Claude *knows* the domain? |
| Facts | nextflow-development = SKILL.md instruction folder; runs nf-core rnaseq/sarek/atacseq on local FASTQs or GEO/SRA datasets; Steps section is linear; reliable inside spec, nothing outside it | unchanged |
| Beat count | 7 (B00, B01, B02, B03, BVDT, BHTF, BOUT) | 7 (same beat IDs) |
| B00 | `ClaudeComposerAsk` — "reading nextflow-development SKILL.md…" run card | `BrutalistHesitantWriter` (WRITER LAW) — "trained" → "told" |
| Register | Teardown ("Here is the Teardown moment... What it gets right... What it bites") | Plain — B03 rewritten from a verdict pronouncement into a both-directions statement (reliable inside the spec / nothing outside it); no ranking, no design judgment |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BVDT heading | implicit "Verdict" framing | "In short" — same facts, judgment-flavored framing removed |
| Body B01–B03 | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Claude-fidelity REMOTION) | **unchanged component choice** — already valid REMOTION, not AI-video/pantry/human-drop, so NO-GENAI/NO-PANTRY LAW required no substitution; content re-registered to Plain |
| Your Turn prompt | garbled run-on ("...on sequencing data. Read the nextflow-development skill and walk me through...") | cleaned into one paste-ready sentence, same request preserved |

**Never built, source-side:** the source `beat_sheet.json` had every beat
marked `SLATE` with no `mp3/`, no `media/`, no `SCRIPT.md` — this redo is the
first time the reel's narration exists as connected prose rather than
per-beat batch fragments.

**Known mixed-skin note:** `SkillTeardownAnatomy`, `SkillTeardownPipeline`,
`SkillTeardownMechanism`, and `ClaudeVerdictArtifact` are Claude-fidelity
REMOTION components with no ink/accent/bg override in their prop schemas
(confirmed by reading the `.tsx` zod schemas directly). Per PHASE 2's
instruction, only the cold open and the close carry the Humanitarians AI
skin; the body was already valid REMOTION under the source and is not one of
"the three things" this skill changes, so it stays as authored — same
precedent as the `claude-basics--claude-liam-four-places-your-data-goes`
redo.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes first | B00 — the naive "trained" framing, corrected before the mechanism starts |
| Wrong guess surfaced | B00 states it directly ("trained, like it learned biology") and B01 falsifies it ("The file is the program") |
| No design judgment | B03 rewritten from source's "What it gets right... What it bites" verdict pairing into a factual both-directions statement; BVDT's implicit verdict framing renamed "In short" |
| Both directions | B03 — reliable inside the named pipelines/inputs vs. nothing to fall back on outside them |
| Carry-out survives retelling | BVDT — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not asserting what "GEO" or "SRA" stand for on screen** — the source's
  own phrasing (public datasets from GEO/SRA) is kept as a proper-noun
  reference to the actual data repositories the skill targets, not expanded
  or explained, since the source SKILL.md text (not available locally to
  re-verify) is the authority on exact scope.
- **Not claiming nf-core, rnaseq, sarek, or atacseq are Claude products** —
  they are open bioinformatics pipeline names the skill orchestrates; the
  reel treats the skill as a wrapper, never as the origin of that tooling.
- **No verdict on whether a fixed-spec skill is the right way to do
  bioinformatics automation** — explaining the mechanism (file-driven,
  same steps every run) is not a ruling on whether that design choice is
  good, which would be Teardown's lane.

## Handoff prompt (BHTF, read aloud)

> "Read the nextflow-development skill, then walk me through what you will
> do before you run anything — what pipeline you'd use, what inputs it
> expects, and what you'd check first."

Why it's worth running: it turns the reel's "file, not training" point into
a live check — the viewer sees Claude cite the actual steps from the file
before doing anything, which is the tell that it's reading, not recalling.

---
**GATE P — signed:** Liam / hai-simple redo pass, 2026-09-04
