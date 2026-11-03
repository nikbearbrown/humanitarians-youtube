# SHOTLIST — `yatra-this-week-gordy` ("This Week, Gordy.")

Typed work order. Every slot is machine-rendered; **nothing is owed by a human**.
No pantry item, no still to source, no screen recording, no HOLD.

Channel `claude-yatra` · handle `@Yatra` · voice Kokoro `af_bella` ·
palette `claude` (fidelity — never retint) · 16:9 master, 9:16 derived.

| Beat | Len | Act | Scene (16:9 / 9:16) | The shot |
|---|---|---|---|---|
| B00 | 12.46s | COLD OPEN | `ClaudeComposerAsk` / `…916` | Cream composer, greeting `Jambo, Yatra`. Ask types in, send arms terracotta, three result lines land — the third names the unclosed stage. |
| B01 | 10.88s | BLUF | `WkBluf` / `…916` | Three stated facts, each with a status chip. The third — the unpublished articles — lands in terracotta with a NOT YET chip. Closer: "An honest week, not a finished one." |
| B02 | 12.63s | FRAMEWORK | `WkPipeline` / `…916` | Five stages draw left-to-right with connectors: PICK · USE · MAKE · WRITE · PUBLISH. All UNLIT. PUBLISH reddens on "a week can end mid-pipeline". |
| B03 | 14.81s | THE TOOL | `WkTool` / `…916` | "Gordy" large; the tool page's own sentence as a quoted italic block; six coverage chips; audience line; URL in mono; citation; terracotta note that one line is all the page publishes. |
| B04 | 4.74s | ASK | `ClaudeComposerAsk` / `…916` | Composer with the real generation prompt for B05's board. `output: []` — the result IS B05. |
| B05 | 11.61s | RESULT | `WkStatus` / `…916` | The same five stages as rows. First four fill solid with CLOSED chips; PUBLISH stays hollow, terracotta, OPEN, detail "with Nina for review — Substack once approved". Tally: 4 of 5 closed. |
| B06 | 13.63s | THE DELIVERABLE | `WkShip` / `…916` | Graphics → Humanitarians AI · LinkedIn page, with a terracotta **MADE** chip on the wire. No artwork drawn — see FACTCHECK. |
| B07 | 12.33s | THE ARTICLES | `WkReview` / `…916` | Two DASHED EMPTY slots labelled only "Article 1"/"Article 2" under a withheld band. Review track: WRITTEN (filled) → IN REVIEW · NINA (terracotta) → SUBSTACK (hollow, never filled). |
| B08 | 12.57s | LIMITS | `WkNotClaiming` / `…916` | Two columns: WHAT I'M CLAIMING (ink) vs WHAT I'M NOT CLAIMING (terracotta), three items each, divider drawn first. |
| B09 | 15.66s | VERDICT | `ClaudeVerdictArtifact` / `…916` | Artifact page; four lines, one per spoken clause, the review state restated rather than implied closed. |
| B10 | 16.96s | YOUR TURN | `ClaudeComposerAsk` / `…916` | Greeting `Your turn.`; prompt types as read aloud; three-item rubric stacks in. |
| B11 | 4.86s | OUTRO | `ClaudeTitleOutro` / `…916` | "This Week, Gordy." poster serif, terracotta period, `@Yatra`, no subline. |

**Total 143.14s — 2 min 23 s.**

## Standing rules this shotlist is built against

- **ILLUSTRATE LAW.** Claude UI at B00, B04, B09, B10, B11 only. Every other
  beat illustrates. B02 and B05 share the five-stage subject but are laid out
  differently (columns vs rows) and are three beats apart — a callback, not
  wallpaper.
- **ONE terracotta per beat**, always marking the unclosed stage.
- **Typing in exactly two beats**: B00 and B10 (B04 is the sanctioned ask
  micro-beat of the ask→result pair).
- **Every externally-checkable claim carries its source.** Only B03 has one to
  carry; it renders the citation and the URL.

## Chapters (computed from `mp3/timings.json`)

```
0:00  The ask
0:12  The week in one breath
0:23  The method: five stages
0:35  Gordy
0:50  Asking for the board
0:55  Four closed, one open
1:07  The graphics
1:20  Two articles, in review
1:33  What I'm not claiming
1:45  The recap
2:01  Your turn
2:18  Outro
```

## What a human could optionally upgrade

Nothing is required. The slot contract still applies: drop `media/B0X.mp4` (or
`pantry/B0X-916.mp4` for the vertical) and re-run `./art run` to swap any beat
by filename without touching the edit.

**One thing deliberately NOT upgradeable by mock-up:** B06 does not draw the
LinkedIn graphics. If you want the real assets on screen, supply them as
`pantry/B06.png` (or `-916`) — inventing artwork for that beat is a
FACTCHECK violation, not a styling choice.
