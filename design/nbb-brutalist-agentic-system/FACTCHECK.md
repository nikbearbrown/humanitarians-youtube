# FACTCHECK — nbb-brutalist-agentic-system

Source of truth: taxonomy provided verbatim in the build prompt (treated as ground truth per instructions).
Verified 2026-07-14. Regenerate if narration or viz data changes.

| # | Claim | Beat | Verdict | Source / derivation |
|---|-------|------|---------|---------------------|
| 1 | "Forty files moved" | B00 | ✓ editorial | Illustrative — narration says "what actually ran?" signals this as a setup for the puzzle, not a literal count |
| 2 | "fps=24 is a command — you get 24 frames per second, every run, guaranteed" | B02 | ✓ | Source: "A specifying input names its exact output: a hex code, an fps… Reproducible, versionable, safe to run unattended" |
| 3 | "register:Teardown is a bias" | B02 | ✓ | Source: "An influencing input only biases a distribution: a persona, a prompt" |
| 4 | "SPECIFIES vs INFLUENCES" axis definition | B03 | ✓ verbatim | Source: "Axis 1 — SPECIFIES vs INFLUENCES. A specifying input names its exact output… An influencing input only biases a distribution" |
| 5 | "Even at temperature zero, a persona is unlike a hex code" | B04 | ✓ verbatim | Source: "Even frozen (temp 0), a persona is unlike a hex code, because the input UNDERdetermines the output rather than naming it" |
| 6 | "INPUTS vs ARTIFACTS" axis definition | B05 | ✓ verbatim | Source: "Axis 2 — INPUTS vs ARTIFACTS. Inputs are authored beforehand (personas, parameters, scripts). Artifacts are what a run leaves behind (contract, logs, deliverable)" |
| 7 | "A beat sheet is both: input to compile, artifact of planning" | B05 | ✓ | Source: "these axes are independent" — beat_sheet.json is cited as both a contract artifact and an input to downstream steps |
| 8 | Six-layer input stack (Human → LLM → Conditioning text → Agent → Parameters → Scripts) | B07 | ✓ verbatim | Source: "THE INPUT STACK, top (most influencing) to bottom (most specifying):" — all six layers named in order |
| 9 | "Not a hierarchy of importance. A hierarchy of underdetermination." | B07 | ✓ editorial synthesis | Source: "Top influences, bottom specifies" — synthesis is accurate and defensible |
| 10 | "The LLM produces a distribution over outputs — no goal of its own" | B08 | ✓ verbatim | Source: "LLM (Claude): raw capability — a distribution over outputs. No goal on its own." |
| 11 | "Three sub-types that stack: method persona = WHAT… voice register = HOW… brand = WHOSE voice" | B09 | ✓ verbatim | Source: "Three sub-types that STACK: method persona = WHAT to produce… voice register = HOW it sounds… brand = WHOSE voice" |
| 12 | "Teardown is not its own agent — it's a parameter of a doer" | B09B | ✓ verbatim | Source: "A register/brand is a PARAMETER of a doer, not its own agent: one writer x many costumes, not many writers" |
| 13 | "An agent is a composite: LLM + conditioning text + tool-loop + goal" | B10 | ✓ verbatim | Source: "Agent: a COMPOSITE — LLM + conditioning text + tool-loop + goal" |
| 14 | Orchestrator "sequences work, owns the contract, hits the gates"; Doer "one focused job" | B10 | ✓ verbatim | Source: "orchestrator (sequences work, owns the contract, hits the gates) and doer (one focused job: write, scout, build, conform)" |
| 15 | Parameters: "eleven_multilingual_v2, stability 0.80, fps 24, ELEVENLABS_VOICE_*, kokoro voices" | B11 | ✓ | Source lists exact parameters; narration cites `stability 0.80, fps 24, a voice ID` — a correct subset |
| 16 | "Scripts: deterministic functions that consume parameters. Same in, same out." | B11 | ✓ verbatim | Source: "Scripts: deterministic functions that consume parameters. Same in, same out." |
| 17 | "generate_audio.py, remotion_scenes.py, compile.py" named as the utility belt | B11 | ✓ | These files exist in `runtime/scripts/` and are cited in source: "the shared 'utility belt' (runtime/scripts/*)" |
| 18 | Three artifact classes: contract / logs / deliverable | B12 | ✓ verbatim | Source: "THREE ARTIFACT CLASSES… Interface / contract: beat_sheet.json… Observability / logs… Deliverable: the mp4" |
| 19 | "Agents check DETERMINABLE things; the human checks JUDGEABLE things" | B13 | ✓ verbatim | Source: "THE JUDGMENT RULE. Agents check DETERMINABLE things… The human checks JUDGEABLE things" |
| 20 | Examples of determinable things: schema, exit, beat count, render match | B13 | ✓ | Source: "did the script exit clean, did the schema validate, is every beat filled, does the render match the deck" |
| 21 | Examples of judgeable things: interesting opening, joke landing, worth watching | B13 | ✓ | Source: "is the opening interesting, does the joke land, is it worth watching" |
| 22 | "Trust an agent to check taste and you have rebuilt AI slop" | B13 | ✓ verbatim | Source: "Trust an agent to check taste and you have rebuilt AI slop" |
| 23 | "Maximally informed, minimally autonomous" | B15 | ✓ verbatim | Source: "THE THESIS. Maximally informed, minimally autonomous." |
| 24 | "The determinism boundary IS the human-judgment boundary" | B15 | ✓ verbatim | Source: "The determinism boundary IS the human-judgment boundary" |

**Gate F verdict: PASS.** All 24 claims either quote the source verbatim or are labeled editorial. No invented numbers, people, quotes, or external citations needed. Deferred items are marked in metadata.deferred; they are not claimed in narration.
