# PEDAGOGY AUDIT — onprem-rag-chatbot
# "Chat With Your Own Data, Zero API Calls" | cli-explainer, persona override (Mohammed Hussain, Onyx, teardown palette)
# Auditor: Claude Sonnet 5 | 2026-08-23

## Source
User-provided guide: "Building a Private, On-Prem 'Chat With Your Data' System
with Open WebUI + Ollama" (Parts 1–4: core concepts, recommended stack, setup
walkthrough, workflow). No external fetch — the whole build is grounded in
this one document, pasted into the conversation.

## Criteria (required-spine cli-explainer rubric, skills/make/cli-explainer/SKILL.md)

### 1. REQUIRED SPINE PRESENT
B00 cold open (ClaudeComposerAsk, ask answered) → B01 PROBLEM (before any
prompt) → B02 ASK → B03 CODE → B04 CONTEXT (bonus mechanism beat — hardware
sizing) → B05 OUTPUT → B06 CHANGE (revision) → B07 CODE → B08 OUTPUT →
B09 SUMMARY → B10 NEXT STEPS (handoff) → B11 OUTRO. All required slots
present, in order, exactly one revision cycle (16:9 requirement met, none
doubled up).
**SCORE: PASS**

### 2. THE ACTUAL-CODE LAW
B03 shows the docker-compose.yml **verbatim** from the source's Part 3.1
(trimmed of nothing load-bearing — the `OLLAMA_BASE_URL` line, both services,
both named volumes are all present). B07 shows the real two pull/config
commands from Part 3.3 plus the Admin Panel settings path, not paraphrased.
Ask→code plausibility: B02's ask ("OLLAMA_BASE_URL must point at Ollama's own
container, never external") plausibly generates exactly the compose file in
B03; B06's ask ("pull nomic-embed-text, wire it as the RAG embedder, tighten
chunk size") plausibly generates exactly the commands in B07.
**SCORE: PASS**

### 3. THE REVISION LAW
B06→B07→B08 is a genuine second cycle: cycle 1 (B02–B05) only stands up the
containers and shows what happens with the embedder unconfigured (zero
retrieval, a confident but ungrounded answer). Cycle 2 adds the actual fix —
pulling the embedding model and setting chunk size — and produces a
materially different OUTPUT (grounded, cited, 3 chunks vs 0). This mirrors a
real, well-documented failure mode of RAG (no embedding model → no vectors →
no retrieval), not an invented bug for drama.
**SCORE: PASS**

### 4. OUTPUT BEATS ARE MOTION, NEVER STILL
B01, B04, B05, B08 are all Manim scenes (`scenes.py`) — test-rendered at
480p15 during authoring to confirm they execute cleanly with no edge
clipping and no missing glyphs (an early draft had an emoji question-mark
that failed to render and an answer card that bled past the frame edge on
both B05/B08 — both fixed and re-verified by extracting frames). None are a
static hold; all sweep/assemble/transform.
**SCORE: PASS**

### 5. NO FABRICATION / DOUBLE-CHECK LAW
- B03's compose file and B07's commands are source-verbatim (Part 3.1, 3.3).
- B04's hardware figures (8–16GB RAM for an 8B model, ~16–24GB for
  Qwen3-30B-A3B, 40–48GB+ for a 70B-class model, embedding models CPU-fine
  regardless) are the source's own Part 1 table — simplified to RAM-only
  bars for the on-screen chart (the source gives RAM-*or*-VRAM ranges) and
  captioned "Redrawn (simplified) from …" per the REBUILD LAW.
- B06/B07's "500–1000 token" chunk range and "chunk size matters more than
  model size" claim are the source's own Part 4 tip, not invented.
- **B05→B08's specific failure scenario (an HR handbook, a remote-work
  question, an invented "3 days" policy) is a CONSTRUCTED illustrative
  demo**, not a claim that this exact run happened. It's built from the
  source's own stated mechanics: an LLM "has no idea what's in your company
  wiki" without RAG, and RAG requires an embedding model to produce vectors
  before anything can retrieve. This is disclosed in the beat sheet's
  `metadata.note` and here, per the SELF-DEMO LAW's illustrative-construction
  allowance (same pattern the brand-palette-accessibility-auditor example
  uses for its contrast-ratio run).
- No model-version-drift language: model names are named as the source's
  current recommendation, not asserted as a permanent "best" choice.
**SCORE: PASS**

### 6. HANDOFF LAW
B10's prompt is read aloud and discussed, not just displayed: narration
explains what the four bracketed asks map to (hardware, embedding model,
chunk size, verification) and ties them back to the exact four decisions the
build just walked through. It's a genuinely runnable prompt with the
viewer's own hardware/documents substituted in, not a summary restated as a
question.
**SCORE: PASS**

### 7. REGISTER / PERSONA OVERRIDE APPLIED CORRECTLY
Teardown throughout — every CODE/OUTPUT beat states the mechanism then the
design judgment (B03: "one env var is the whole trick"; B06: "that's not a
model problem, it's a wiring problem"; B09: "the model didn't get smarter,
the pipeline finally had something to search"). Per your instruction this
build (matching the prior mycroft-credit-rating reel in this same folder):
the nbb persona's default IN-FOR-BEAR line and the `@NikBearBrown` channel
identity are dropped. B00 and B11 sign off as **Mohammed Hussain**; voice is
Kokoro `am_onyx` ("Onyx"); the Manim OUTPUT beats use the nbb teardown
palette (white `#FFFFFF` / ink `#2A1A0E` / crimson `#C8102E`, confirmed in the
rendered test frames) rather than the Claude cream/terracotta retint. The
Claude-skin composer/code/verdict/outro components (`ClaudeComposerAsk`,
`ClaudeCodeBeat`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`) necessarily
keep their fidelity look — per CLAUDE-BRAND.md they can't be retinted — but
every on-screen identity string inside them (`folderLabel`, outro `handle`)
is set to "Mohammed Hussain," not left at the `@NikBearBrown` default (a
small inconsistency I noticed in the prior reel and corrected here — flagged
below, not blocking).
**SCORE: PASS**

### 8. DURATION
Sum of `estimated_duration_s` = 289s (4:49) — an output of the content, not a
target: 12 beats covering a real 4-part setup guide (concepts, stack choice,
docker-compose, hardware sizing, RAG mechanics, a revision, and a handoff)
land naturally in the 4–5 minute range for a build reel this dense. Real
runtime will be re-measured from the generated Kokoro MP3s (audio-first rule,
never hand-fixed) once you sign off.
**SCORE: PASS**

## Open items (do not block this gate — flagged for the build steps after sign-off)
- **9:16 full-length reformat**: `ClaudeCodeBeat` has no portrait (`916`)
  sibling in `Root.tsx` yet — I'll author `ClaudeCodeBeat916.tsx` (same
  pattern as the existing `ClaudeTitleOutro916.tsx`/`ClaudeVerdictArtifact916.tsx`
  wrappers) before the 9:16 pass. `ClaudeComposerAsk916`,
  `ClaudeVerdictArtifact916`, and `ClaudeTitleOutro916` already exist. The
  four Manim OUTPUT scenes will get portrait counterparts (top-to-bottom
  restack, per the explainer skill's Shorts-law composition logic) in a
  parallel `916/scenes.py` — this is a FULL reformat of all 12 beats, nothing
  dropped, not the capped `./art shorts` derivative.
- **Corner LOGO-LAW mark**: left unset, as in the prior reel, since this
  build doesn't claim a channel identity. Tell me if you want a personal
  mark instead.
- Manim scenes were only test-rendered at 480p15 for correctness (no crashes,
  no clipping, no missing glyphs) — the real render happens after audio lock,
  to the beats' measured durations, via the normal `./art run` pass.

## Overall assessment
The build reconstructs a real, followable setup: the compose file and the
pull/config commands are the source's own, the hardware guidance is the
source's own table redrawn, and the one revision cycle demonstrates a real,
well-documented RAG failure mode (no embedder → no retrieval) using the
source's own stated mechanics rather than an invented bug. Nothing on screen
extends past what the source document actually says, and the one constructed
scenario (the HR-handbook demo) is disclosed as constructed, not claimed as
an observed event.

**VERDICT: PASS** — recommended by this audit; awaiting your sign-off before
any audio is generated (GATE P is a quality gate, not a formality — if
anything above reads wrong, tell me and I'll redraft the beat sheet before we
spend a single render).
