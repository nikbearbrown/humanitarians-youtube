# SOURCES.md — the-agent-that-was-told-what-to-do

Primary source: `09_the_agent_that_was_told_what_to_do.md` (the authored
script with inline `[VISUAL: …]` stage directions, narration lightly
revised — see "Corrections applied to narration" below) and
`09_narration_tts_ready.txt` (the condensed narration actually spoken,
split by beat). Both live in this folder.

## Scope (per established series convention)

Like STEM2, STEM6, STEM7, and STEM8, this is a **general conceptual
explainer** about prompt injection as a category of problem, not a
first-person account of this project's own implementation. Per the
channel's standing note, STEM videos don't need to match the real product
code (`D:\Code\mycroft\verification-layer`). Every claim below is checked
against standard, widely-documented understanding of prompt injection in
LLM-based agents, not against a specific file or line reference.

## Corrections applied to narration

Per the standing house style convention (first raised on STEM6, now
applied proactively): three instances of a repeated "isn't X. It's Y."
contrastive construction were rewritten in the source script for natural
spoken cadence — no factual or structural content changed:

| # | Location | What changed |
|---|---|---|
| 1 | B00 (cold open) | "isn't really about the agent malfunctioning. It's about the agent working exactly as designed" → "less about the agent malfunctioning and more about the agent working exactly as designed" |
| 2 | B02 (worked example) | "The agent isn't being clever or malicious. It's doing exactly what an email-reading agent is supposed to do" → "The agent is just doing exactly what an email-reading agent is supposed to do... no cleverness or malice involved" |
| 3 | B07/closing | "the gap isn't a flaw in the agent at all. It's a flaw in the very idea of trusting text..." → "the gap sits somewhere else entirely — in the very idea of trusting text..." |

## Factual claims (DOUBLE-CHECK LAW)

| Beat | Claim | Verdict | Basis |
|------|-------|---------|-------|
| B01 | LLMs process instructions and content-to-read as the same token stream, with no architectural channel separation between them | ✓ | Correct and precise — this is the well-documented structural root cause of prompt injection: everything in the context window is just text the model attends to, with no built-in provenance tag distinguishing "system-authorized command" from "content being summarized" |
| B01 | A model has no hard, built-in wall preventing text encountered while reading from being treated as a command | ✓ | Follows directly from the above; this is the standard framing used across security writing on the topic |
| B02 | Hidden text (e.g. white-on-white) in a document can carry an instruction invisible to a human but readable by the model | ✓ | A well-documented, real category of prompt-injection technique (steganographic/invisible-text injection in emails, web pages, documents) |
| B02 | The specific email-forwarding scenario | ⚠ **illustrative** | A constructed worked example, not a logged incident — declared here per DOUBLE-CHECK LAW, consistent with prior episodes' worked-example precedent |
| B03 | Prompt injection is a structurally different problem from the autonomy/permission question, because it requires no permission grant from the user at all | ✓ | Correct and is the episode's key distinguishing claim — autonomy is a user-side decision about what an agent is allowed to do; injection is an attacker-side action that doesn't touch that decision at all, only what the agent reads |
| B04 | Keeping an agent's core system instructions in versioned code (not runtime-modifiable input) reduces, but does not eliminate, injection risk | ✓ | Standard mitigation guidance — locking the system prompt away from user/tool-controlled input shrinks the attack surface for instruction *replacement*, but doesn't prevent an injected instruction from *competing* alongside a legitimate task |
| B05 | Multi-agent cross-examination (from `when-two-agents-disagree`, STEM6) has the same shared-contamination blind spot applied here: agents pulling from the same poisoned source will agree, not disagree | ✓ | Direct logical parallel to STEM6's own established claim — arbitration-by-disagreement structurally cannot catch agreement, regardless of whether that agreement is correct or both agents were fooled by the same source |
| B06 | A human approval gate's real strength is bounded by what it actually surfaces to the human, not by its mere existence | ✓ | Standard human-factors/UI-security principle — an approval step that doesn't display a side-effect cannot be relied on to catch that side-effect, regardless of how careful the human reviewing it is |
| B07 | Prompt injection is an active, unsolved category of problem, not one with a complete mitigation checklist | ✓ | Accurate and widely acknowledged in security discussion of LLM agents — no mitigation discussed (or currently known) fully closes the gap between "the model reads arbitrary text" and "arbitrary text can influence the model" |
| B10 | This is the fifth and, as of this writing, final video in the "Accountability" mini-series (STEM5–STEM9) | ✓ | Matches the channel's own prior PEDAGOGY.md notes (STEM6's) describing the series as five episodes, and no STEM10 script exists in `youtube/` as of this writing — confirmed by directory listing, not assumed |

## Anti-staleness check (DOUBLE-CHECK LAW)

No model name, vendor, version number, or benchmark score appears in the
narration. Every mechanism described (token-level instruction/data
conflation, hidden-text injection, autonomy vs. injection, the three
mitigations and their limits) is a general, structural property of
LLM-based agents, not tied to a specific product generation, so the reel
should not date.

## Simplifications (declared)

- **The email-forwarding scenario (B02) is illustrative**, not a logged
  incident from any real system.
- **The two-doors metaphor (B03) and the locked-box metaphor (B04) are
  teaching devices**, not literal descriptions of any specific system's
  architecture.
- **B05's callback to STEM6 restates that reel's own already-verified
  claim** rather than introducing a new one — see STEM6's SOURCES.md for
  the original verification of the shared-contamination blind spot.

## Content carried and cut

| Source | Status | Note |
|---|---|---|
| Title card (recipe blog, hidden instruction reveal) | Carried, relocated | Used as the closing beat's own visual (B07) rather than the cold open, since the end card explicitly reprises it; B00 is locked to `ClaudeComposerAsk` per COLD OPEN LAW |
| "The Gap" section | Carried | B01 |
| "A Worked Example" section | Carried | B02 |
| "Why This Isn't the Same Problem..." section | Carried | B03 |
| "The Mitigations" section | Carried, split | B04/B05/B06 — each of the three named mitigations gets its own beat and its own honest limit, rather than three bullet points crowded into one hold |
| "Sitting With the Actual State" section | Carried | B07, deliberately not reframed as a tidy recap — this reel's own script insists the honest ending isn't a clean framework, so B07/B08 both preserve that framing rather than manufacturing false resolution |
| End card (recipe blog, flickering "could this be an instruction?") | Carried | Folds into B07 rather than a separate beat, since it's the visual enactment of that beat's own point |
| Key Takeaways (7 bullets) | Carried, condensed to 4 | B08's verdict covers takeaways 1, 2, 6, and 7 directly; takeaways 3–5 (worked example, locking instructions, cross-examination's hole) are each their own dedicated beat (B02, B04, B05) rather than compressed into the recap |

## Free pipeline — no paid spend

Kokoro `am_onyx` (local, free) is the planned narration engine. No
ElevenLabs, no FLUX, no paid services. No publishing — the master stays in
this folder. **Audio has not yet been generated as of this writing — see
PEDAGOGY.md, GATE P is PENDING.**
