# SOURCES.md — when-two-agents-disagree

Primary source: `06_when_two_agents_disagree.md` (the authored script with
inline `[VISUAL: …]` stage directions, narration already revised for
natural spoken cadence) and `06_narration_tts_ready.txt` (the condensed
narration actually spoken, split by beat). Both live in this folder.

## Scope check against this project's own code (DOUBLE-CHECK LAW)

Unlike `how-do-you-know-it-worked` (STEM5), which describes this project's
own mitigation code (`claims.py`, `verification.py`, `consistency.py`),
this script describes a **general multi-agent arbitration pattern** — it
is not a first-person account of code that exists in this repository.

Before writing this file, `accountability_layer/` (one level up from
`youtube/`) was searched directly for any existing arbitration or
multi-agent-disagreement implementation:

```
grep -rliE "arbitrat|disagree|divergen" accountability_layer/*.py
```

Result: only `consistency.py` matches, via its existing
`number_divergence_flag` — and that mechanism (covered in STEM5) compares
**one agent against itself across two runs**, not two independent agents
against each other. No `arbitration.py`, no two-agent debate loop, no
structured confidence/directional-vector comparator exists anywhere in
this codebase today. So this reel is checked against general
agent-engineering practice, the same basis STEM2 used, **not** against
this project's own files — claiming otherwise would fail the
DOUBLE-CHECK LAW.

## Factual claims (DOUBLE-CHECK LAW)

| Beat | Claim | Verdict | Basis |
|------|-------|---------|-------|
| B00/B01 | A system built from several specialized agents can produce two independently-reasoned, independently-sourced conclusions that flatly contradict each other | ✓ | Standard property of any multi-agent pipeline where agents don't share a single reasoning trace; not code-specific |
| B02 | Averaging two conflicting confidence scores or conclusions does not produce a more accurate answer, and destroys the information that they disagreed | ✓ | Correct as a general claim: an average of two independent estimates is only closer to truth than the wrong one if you assume both are equally likely to be right, which "they disagree" specifically tells you not to assume |
| B03 | Disagreement should be detected on structured signals (confidence score, directional/sentiment vector) rather than raw text similarity | ✓ | Correct and standard framing — text-similarity metrics (e.g. string diff, embedding cosine distance on raw output) are well known to conflate paraphrase with disagreement and vice versa |
| B04 | Unbounded multi-round debate between language models tends to converge on the more persuasive-sounding output rather than the more correct one | ✓ | Matches documented behavior in published multi-agent-debate research (models can be swayed by confident restatement independent of correctness) — stated qualitatively here, no specific paper or benchmark figure is cited on screen |
| B04/B05 | Capping arbitration at a single round is a deliberate design choice, not an arbitrary limit | ✓ | Stated as the reel's own argued position, not an external claim requiring a citation |
| B05/B06 | An "unresolved" outcome should be recorded as its own first-class output rather than silently resolved one way or the other | ✓ | Standard escalation/human-in-the-loop design principle; not code-specific |
| B07 | If both agents draw on the same contaminated or tampered-with source, they can independently reach the same wrong conclusion and agree with each other | ✓ | Logically follows from the detection mechanism's own definition (B03): a divergence-based trigger cannot fire on agreement, correct or not, by construction |
| B07 | This is a structural limit of arbitration-by-disagreement, not something a better threshold fixes | ✓ | Follows directly from the above — no threshold on a divergence signal can detect a case where there is no divergence to measure |
| B08/B09 | The four-rule framework (signal not noise / structure not wording / bound the round / unresolved must survive) | ✓ | Direct synthesis of the mechanisms already checked above; not a new claim |
| B11 | The next problem is whether an agent's memory across sessions is real recall or convincing pretense | ✓ | Matches this channel's own next-scripted reel, `youtube/STEM7/07_does_it_remember_or_just_pretend.md` ("Does It Remember, or Just Pretend To?"), confirming the tease is a real, already-scripted follow-up |

## Anti-staleness check (DOUBLE-CHECK LAW)

No model name, vendor, version number, or benchmark score appears in the
narration. Every mechanism described (structured-signal comparison,
single-round arbitration, unresolved-as-output, shared-contamination
blind spot) is a general architectural pattern, not tied to a specific
model generation or product, so the reel should not date. The one
project-specific claim (that no arbitration code currently exists in
`accountability_layer/`) should be re-checked if that codebase gains a
multi-agent module before this reel is built.

## Simplifications (declared)

- **The financial "margins improving / declining" scenario (B00–B02) is
  illustrative**, chosen for narrative concreteness and consistency with
  STEM5's own financial-analysis framing. It is not a logged trace from
  this or any real system.
- **"Confidence score" and "directional vector" (B03) are described
  generically**, not tied to a specific scoring formula or vector
  dimensionality — the reel states the *category* of signal (structured,
  not textual) rather than inventing a fake precise implementation to
  sound more concrete than the claim actually is.
- **The single-round arbitration debate (B04/B05) is presented as one
  reasonable design point**, not the only correct one. The reel does not
  claim this is how any specific product implements arbitration.

## Content carried and cut

| Source | Status | Note |
|---|---|---|
| Title card (two desks, nameplates, circled numbers) | Not built as a literal beat | Carried thematically into B00's composer output and B01's contradicting-mics framing; B00 is locked to `ClaudeComposerAsk` per COLD OPEN LAW |
| "Why This Wasn't a Problem Before" section | Carried | Becomes B01, doubling as the episode's framework/BLUF beat — the "disagreement is a signal, not a bug" reframe is stated here, before any mechanism |
| "The Naive Fix" section | Carried | B02, including the blender visual from the source `[VISUAL]` direction |
| "Detecting the Disagreement" section | Carried | B03 |
| "The Arbitration Step" section | Carried, split | B04 (the single-round mechanic + the crossed-out unbounded-debate contrast) and B05 (the resolved/unresolved branch) — split for the same reason STEM5 split its two-part mechanisms: each half is its own diagram, not one crowded hold |
| "What You Do With Unresolved" section | Carried | B06 |
| "The Part Nobody's Fully Solved" section | Carried | B07, the reel's dedicated falsifiability beat |
| Ending line ("the failure isn't two agents disagreeing…") | Carried, restructured | Folded into B08's framework beat and B09's verdict card rather than its own beat, since the ending's content is fully covered by the four-rule recap |
| Key Takeaways (6 bullets) | Carried, condensed to 4 | Compressed into the four-rule framework in B08/B09 for a clean on-screen count; no content from the six original takeaways is dropped — takeaway 6 (the blind spot) is B07's entire beat rather than a fifth recap line |

## Palette retint (declared, per STEM2/STEM5 precedent)

The source script's `[VISUAL]` directions call for green/red speech
bubbles and a green "AGREEMENT" / red "DIVERGENCE" gauge. Per the Claude
fidelity palette (no blue, no green — see `graphics_lib.py`'s header
comment), these are retinted: **ink** stands in for "agreement/resolved,"
**terracotta** stands in for "divergence/unresolved," carried by label and
position rather than a second hue.

## Free pipeline — no paid spend

Kokoro `am_onyx` (local, free) is the planned narration engine. No
ElevenLabs, no FLUX, no paid services. No publishing — the master stays in
this folder. **Audio has not yet been generated as of this writing — see
PEDAGOGY.md, GATE P is PENDING.**
