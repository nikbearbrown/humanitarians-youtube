# SOURCES — Episode 1, "What Makes an AI Agentic"

## Primary source

**`agent_loop.py`** — authored for this episode, shipped in this folder, runnable with no
dependencies and no API key.

- `run()` is the function reproduced verbatim in beat B06.
- Verified by execution on 2026-08-13: `python3 agent_loop.py` → `rows in the sales file: 3`
  (three data rows in the fixed three-row CSV that `read_file` returns, header excluded).
- `think()` is a deterministic stand-in, clearly documented as such in the file's docstring.
  The episode does not claim a model was called; it claims the loop's *shape* is what
  matters, and the file is written so that substituting a model call changes nothing in
  `run()`.

## Nothing else is cited, deliberately

This is a definitional episode. It makes no empirical claim that requires an external
citation, and it names no model, vendor, benchmark, or product. See `FACTCHECK.md` for the
claim-by-claim audit and the anti-dating search.

The one proper noun pointing outward is **Model Context Protocol**, named once in B00 as
the destination of the ten-episode playlist. It is not described, quoted, or characterised
in this episode — episodes 9 and 10 do that work, and will carry the specification link.

## Register rewrite (DOUBLE-CHECK LAW)

Nothing was parroted from a source, because there is no prose source. The episode's
argument — *agency is a trade, not an upgrade* — is the fellow's framing, and the
Teardown register earns its place at B08 and B09, where the mechanism is judged rather
than described.

## Toolkit provenance

- Built with `brutalist.art` (pared-down, free-only edition), skill `ai-explainer`.
- Voice: Kokoro `am_onyx` ("Onyx"), generated locally. Cost: $0.00.
- Remotion patterns used, all pre-existing in `runtime/remotion/src/Root.tsx`:
  `ClaudeComposerAsk`, `CwcConceptCard`, `ClaudeScienceLayerStack`, `ClaudeWindow`,
  `ClaudeScienceSourceFlow`, `ClaudeCodeBeat`, `ClaudeScienceChipGrid`,
  `MedhavyConceptCard`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`.
  No new scene component was written for this episode; no pattern was retinted.
