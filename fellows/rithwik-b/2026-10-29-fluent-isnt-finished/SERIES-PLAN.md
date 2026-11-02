# AI Fluency × Brutalist — series blueprint (4 films, 2–4 min each)

## Intake (inferred — confirm or correct)

- **Audience:** Humanitarians AI fellows who use Claude most days but have never
  built a video with the Brutalist toolkit. The series doubles as onboarding.
- **Series outcome (measurable):** given any step in a Brutalist build, the viewer
  can (a) name which AI-fluency skill it exercises — *describe*, *evaluate*,
  *trust-or-verify*, *combine judgment* — and (b) say whether Claude or the human
  owns that step, and name the gate that enforces it.
- **Channel / voice:** `claude-hai` skin, `@HumanitariansAI` chip, Kokoro
  **Bella** (`af_bella`, Plain register — per `skills/make/hai/SKILL.md`; free).
- **Skill:** `ai-explainer` chassis — cold open → hesitant-writer BLUF → body →
  verdict → Your Turn → title outro.
- **Evidence:** the real `hello-test` build from this session (its audio, its
  contact sheet, its GATE F refusal) is the worked example. Receipts, not mockups.

## The through-line

> AI Fluency is the skill. Brutalist is the receipt.
> Claude does the build; it cannot watch the video. Every gate in the toolkit
> marks the spot where a human's judgment has to come back in.

## The four films

| # | Title (a claim, not a topic) | Fluency skill | Film outcome — after it, the viewer can… | Brutalist evidence on screen |
|---|---|---|---|---|
| 1 | **Fluent Isn't Finished** | Combine human judgment with AI | state the asymmetry (Claude builds, can't watch) and sort 6 build steps into *Claude owns* / *human owns* | HOW-TO §1 quote; the pipeline `IDEAS → SCRIPT → AUDIO → VISUALS → QC`; sort animation |
| 2 | **The Beat Sheet Is the Prompt** | Write effective prompts (description) | name a beat's three parts — narration, show, scene — and explain why audio is generated first | the real `beat_sheet.json` (code beat); Kokoro measuring 2.39 s; the clock becoming timing |
| 3 | **Look at the Frames** | Evaluate outputs critically | read a QC contact sheet and classify a defect as blocker / major / fine | the real `qc-contact-sheet.png`; GATE V report (0 blockers); a slate as an honest "I can't make this" |
| 4 | **Trust, Then Verify** | When to trust vs. verify | decide which claims in a script need a source before the final cut | the real GATE F refusal; `FACTCHECK.md` row format; "never publish — the master is yours" |

## Per-film beat spine (~13 beats, ~350–450 words → ~2.5–3.5 min)

| Beat | Role | Scene |
|---|---|---|
| B00 | Cold open — the ask lands answered | `ClaudeComposerAsk` (hello: Hi · Ola · Hej · Ciao, one per film) |
| B01 | BLUF — the hesitant writer corrects the misconception | `BrutalistHesitantWriter` (≥9 s, lead silence 0.8 s) |
| B02–B08 | Body — one idea per beat, each illustrated | `ShowTellCard`, `ClaudeCodeBeat` (real files), `ClaudeWindow`, rendered stills of the real build |
| B09 | Worked example — the hello-test receipt | real artifact from this session |
| B10 | Verdict — what the skill buys you, where it bites | card |
| B11 | Your Turn — a prompt read aloud and discussed | `ClaudeComposerAsk` (`Your turn.`) |
| B12 | Title outro | `ClaudeTitleOutro` |

Misconceptions the hesitant writer corrects (one per film):
1. "AI fluency means ~~getting perfect output~~ → knowing which judgment stays yours."
2. "A good prompt is ~~a clever sentence~~ → a complete description of the work."
3. "If it rendered, ~~it's done~~ → someone has to look at it."
4. "Polished means ~~true~~ → checked."

## Fact-check status (GATE F inputs)

| Claim from the brief | Status | Plan |
|---|---|---|
| AI fluency = prompting, evaluating, trust/verify, combining judgment, workflows | Consistent with public AI-fluency framings | Use, attributed to the brief, no named institution |
| "Botspeak" is how Humanitarians AI teaches it | **Unverified** (no public source found) | Omit unless you supply a link |
| Definition credited to Stanford HAI | **Unverified / likely mis-attribution** | Omit |
| Brutalist = show real work, document what failed | Matches toolkit HOW-TO §1 | Use, cite HOW-TO.md |
| Brutalist = "uploading videos" | **Contradicts toolkit** ("Nothing here ever publishes") | Reframe: the master stays with you; posting is a human decision |
| Claude cannot watch the video | HOW-TO.md §1 | Use, cite |

## Build cost

$0.00 — Kokoro + Remotion, local. ~50 beats total; each film compiles to a
review cut, then gets a frame-level QC pass. Final masters require a signed
`FACTCHECK.md` per film (GATE F) — I'll draft them; the sign-off is yours.
