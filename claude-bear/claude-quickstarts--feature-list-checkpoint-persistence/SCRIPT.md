# Persisting Progress Across Context Windows. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `anthropics/claude-quickstarts/youtube/feature-list-checkpoint-persistence`).*
*Register: **Plain**. 8 beats, matching the source's beat count (B00–B07). Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes an agent picking up mid-project must remember where it stopped — like memory carries over. It doesn't. It rereads a file that tracks progress. Here's how that actually works." | Writer types "Claude just / remembers where / it left off? / How does it resume?"; "remembers" hesitates and corrects to "rereads" |
| B01 | 1 stakes — the problem | A context window has a limit. When an agent's conversation fills it, the session ends. The next session opens blank — no memory of what was done, what passed, what failed. Rereading everything burns half the new context. Guessing risks getting it wrong. | a session timeline: session one fills to the brim and stops; a boundary line; session two opens as an empty bar |
| B02 | 3 mechanism — external state | The fix: two external files. `feature_list.json` is the source of truth — two hundred entries, each with an id and a status, incomplete or passing. Git is the ledger — one commit per finished feature, so the history can't be disputed. Each session reads the file, finds the first incomplete entry, implements it, tests it, commits, and marks it passing. | feature_list.json and a git log drawn side by side; an arrow cycles through read → implement → test → commit → mark passing |
| B03 | 4 anchor — the file across the boundary | Watch the file itself, across the boundary. Session one flips features one through fifty from incomplete to passing, one commit at a time. The boundary passes. Session two opens the same file, finds item fifty-one as the first incomplete entry, and starts there — no replay of the first fifty. | THE ANCHOR: a vertical list of two hundred rows flipping status badges; a dividing line labelled "session boundary"; session two's read head lands on row 51 |
| B04 | 5 scope — what this doesn't cover | This covers the checkpoint-and-resume mechanism only: the file, the git ledger, the boundary, and the first-incomplete lookup. It doesn't cover how the two-hundred-item list gets written in the first place — that's a separate step — or what exactly makes a feature count as passing. | the same anchor list, boxed with a solid line; two items outside the box, dashed, unlabelled: "how the list is written" and "what counts as passing" |
| **BCRY** | **6 carry-out** | A context window is a workspace, not memory — when it fills, the session ends, and what carries over is whatever got written to a file and a git commit, not anything the agent remembers. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: externalize my agent's progress to a checkpoint file plus git commits, so a brand-new session can resume exactly where the last one stopped — then prove it by starting a fresh session and watching it pick up correctly. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Persisting Progress Across Context Windows. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`feature-list-checkpoint-persistence`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Persisting Progress Across Context Windows." | unchanged |
| Facts | context window is a workspace that empties between sessions; `feature_list.json` externalizes state (id + incomplete/passing per entry); git is the immutable per-feature ledger; each session reads, finds the first incomplete entry, implements, tests, commits, marks passing; scope excludes list-generation and the test framework | unchanged |
| Beat count | 8 (B00 cold open, B01 problem, B02 fix, B03 centerpiece, B04 honesty/scope, B05 verdict, B06 your turn, B07 outro) | 8 (B00 writer, B01 stakes, B02 mechanism, B03 anchor, B04 scope, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette |
| Register | Teardown — B05's `ClaudeVerdictArtifact` framed the recap as "what the body demonstrated," a verdict card | Plain — BCRY states the same mechanism as a carry-out sentence, no grading |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B04 skin | `ClaudeComposerAsk` command cards, fixed Claude palette | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's channel-skin row |
| B05 → BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | "Externalize my agent's progress to a feature_list.json + git so it can resume across sessions — then prove it picks up where it left off." | kept functionally identical (already a genuinely runnable, generic prompt) — read aloud in Plain register without the source's follow-up interrogation ("Does it handle partial test failures? …") |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the source
was already all-Remotion — so the NO-GENAI/NO-PANTRY LAW required no substitution
beyond what the WRITER LAW and channel-skin row already require. The source's three
empty-narration `BOOKEND`-lane beats (`BVDT`, `BHTF`, `BOUT`) were leftover template
scaffold, never part of the rendered 8-beat sequence, and are not carried into this redo.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00–B01; the external-state mechanism (B02) and the file mutating across the boundary (B03) wait until the blank-session problem is established |
| Wrong guess surfaced | B00 (remembers → rereads) |
| No design judgment | B04 states the scope boundary as a fact, not a critique; BCRY states the mechanism, not a verdict on whether this is the best checkpoint design |
| Anchor | B03 plants the file-across-the-boundary visual; referenced again in BCRY's "what carries over" line (no second full visual replay — an 8-beat, single-mechanism reel) |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that the agent remembers anything.** The whole point is that it doesn't —
  progress lives in the file and the git log, not in the model or the conversation.
- **Not a claim about how the 200-item feature list gets generated**, or what the
  test framework does — B04 states both are out of scope.
- **Not a verdict on whether this is the best checkpoint design.** The source's B05
  framed the recap as "what the body demonstrated" without grading it either; this
  redo keeps that non-judgment and removes any residual verdict framing (the
  "Verdict" card label itself) per Plain register.

## Handoff prompt (BHTF, read aloud)

> "Externalize my agent's progress to a checkpoint file plus git commits, so a
> brand-new session can resume exactly where the last one stopped — then prove
> it by starting a fresh session and watching it pick up correctly."

Why it's worth running: it's the reel's own claim, testable on any multi-session
agent task the viewer already has running, not a contrived example.

---
**GATE P — signed:** ______________________  (human)
