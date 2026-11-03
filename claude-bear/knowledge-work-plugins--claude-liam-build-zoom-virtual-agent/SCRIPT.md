# Claude Doesn't Chat With Your Customers — It Builds the Virtual Agent Integration — Narration Script

*Skill: `hai-simple` (redo of a Teardown skill-teardown). Register: **Plain**.
7 beats, matching the source's beat count.*
*Carry-out written first (CARRY-OUT.md). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter` (Remotion, humanitarians palette).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | Someone assumes build-zoom-virtual-agent means Claude itself becomes the assistant that chats with your customers. It doesn't — build-zoom-virtual-agent means Claude builds the integration code around Zoom's own Virtual Agent product. | Writer types "Does Claude / be my Zoom / virtual agent?", hesitates on "be", corrects to "build" |
| B01 | 1 anatomy | This skill is built from a skill — a folder Claude reads before it works. Inside are eight items: a RUNBOOK and a SKILL file, plus folders for Android, iOS, core concepts, references, common scenarios, and troubleshooting. Claude reads the file, then follows it. | A folder opens to reveal the eight items; SKILL.md highlighted |
| B02 | 2 mechanism | The steps run in order: read the file, work through each step exactly as written, then return the result. Nothing runs out of sequence unless a step itself says so. | Three-card pipeline: Read SKILL.md -> Execute steps in order -> Return result |
| B03 | 3 constraint | For this skill, the scope is five things: web embeds; Android or iOS wrapper integrations; knowledge-base sync; lifecycle handling; and troubleshooting. Each sits inside Zoom's existing Virtual Agent product — Claude fits code around it, it doesn't replace it. Ask for something outside those five and there's no mode that covers it. | Five scope-item rows fill in with checkmarks; boundary line, "nothing outside this list" |
| **BCRY** | **4 carry-out** | Build Zoom Virtual Agent doesn't hand you an AI that talks to your customers — it makes Claude build the integration: web embeds, Android or iOS wrapper code, knowledge-base sync, lifecycle handling, or troubleshooting, fitted around Zoom's own Virtual Agent product. | The carry-out sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Ask Claude: I want to embed Zoom's Virtual Agent in our app and keep its knowledge base in sync with our docs. Walk me through the pieces I'd need — the web embed, the mobile wrapper, and where knowledge-base sync tends to break — before writing any code. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Claude Doesn't Chat With Your Customers — It Builds the Virtual Agent Integration. Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | Source's B03/BVDT "gets it right / bites" trade-off framing dropped; B03 states the five-item scope as fact, BCRY states the build/talk distinction as fact — no verdict language |
| Wrong guess surfaced and falsified | B00 states the newcomer's assumption (Claude itself chats with customers) and the writer's own correction falsifies it on screen ("be" -> "build") |
| Facts unchanged from source | Anatomy (8 items), pipeline (linear, 3 phases), scope (5 items: web embeds, Android/iOS wrapper, KB sync, lifecycle, troubleshooting) all carried over verbatim |
| Carry-out | BCRY compresses the distinction (build the integration vs. hand over a talking agent), not the topic |

## Deliberately not claimed

- **Not that Claude replaces Zoom's Virtual Agent product.** The reel keeps
  the boundary stated by the source: Claude fits code around the existing
  product, it doesn't build a new conversational AI from scratch.
- **No accusation of anyone misleading anybody.** The misreading of "virtual
  agent" as "Claude personally becomes the agent" is an ordinary newcomer
  assumption, treated as one via the writer's own on-screen correction.

## Handoff prompt (BHTF, read aloud)

> "I want to embed Zoom's Virtual Agent in our app and keep its knowledge
> base in sync with our docs. Walk me through the pieces I'd need — the web
> embed, the mobile wrapper, and where knowledge-base sync tends to break —
> before writing any code."

---
**GATE P — signed (redo-mode, unattended build):** filmloop, 2026-09-02
