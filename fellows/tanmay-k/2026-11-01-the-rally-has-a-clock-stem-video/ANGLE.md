# Week 29 — Topic Video Angle (proposal, not yet chosen)

## What the source gives us
Pong's rules are few (top-down, paddles move only up/down, fixed laws, first to 11), and the essay claims there is
**no perfect defense**. It never says when that is true. That is the open question.

## Proposed angle: "The Number That Ends the Rally"
The claim "no perfect defense" is not a law of Pong. It is one inequality between two speeds, and it can be found
exactly. Defender sees the ball's direction the instant it is hit and has one flight time T = W / vx to reach the
landing spot. The attacker can aim anywhere in the field, so the defender's best waiting spot is the middle, and the
worst landing is half the free height away. Perfect defense exists only if

    paddle speed x flight time  >=  (H - paddle) / 2      i.e.  vp / vx  >=  (H - h) / (2W)

For Pong-like proportions that is a paddle moving about a quarter as fast as the ball sideways.
**Measured** (`angle_check.py`, our own brute-force search, Pong-like 858x525, paddle 60): threshold ratio 0.272
measured vs 0.272 predicted, at four ball speeds. So the inequality is right for this model.

Why it is a film: the ball speeds up each hit, so T shrinks, so vp x T falls through the line. Every rally has a
built-in clock, and the film can show the exact hit on which a flawless defender becomes beatable. "No perfect
defense" is then a design decision, a dial the designer set, not a mystery. The essay's own prompt 3 (which single
rule breaks the balance?) gets a measured answer: slow the paddle, or let the contact point stop steering the ball.

## Why it is unique
- Repo: no mechanism content on Pong at all (only a games-history film). Our Weeks 15-28: nothing on games,
  geometry of play, or thresholds in a rule set.
- Not a framework/checklist shape. Candidate structure: the film IS one rally, replayed with the paddle-speed dial
  turned down until the defender breaks. The ending is the dial reading, not a rubric. Differs from Week 24's
  list-as-chapters and Week 27's three-things-you-could-change.

## Boundaries (so we don't over-claim)
- The inequality is our derivation on a stated simplified model (instant ball-direction visibility, attacker can
  aim anywhere, no edge effects, no spin). Say so on screen; do not attribute it to the essay or to any real
  Atari/arcade machine.
- The essay HTML is not in the repo; cite only what the beat sheet quotes. No Atari footage or marks: our own
  drawn rectangles and simulation only (no copyright, no politics, no real people).

## Still to do before building
1. Check the model against a stricter sim (discrete paddle, ball speed-up per hit) and record the hit number.
2. Read-aloud audit of other fellows' narration for "paddle speed / ball speed / angle" (content sweep of all refs).
3. Facts to verify: nothing numeric about the real 1972 hardware unless sourced.

---
## Results of the pre-build checks (2026-10-30)

### 1. All-refs content sweep (`sweep.py`, `sweep.out`)
60,568 text blobs reachable from all 104 remote refs, case-insensitive:

| Idea | Files outside the pong folder | Verdict |
|---|---|---|
| pong | 6: `CONVERSION-LOG-hai.md`, `claude-for-design/README.md` (index row), a NEU-ISE "AI: a guide for..." post, a workplace-software lecture deck, and `design/pong/beat_sheet*.json` (an older copy of this same essay) | No mechanism content. Same essay, or passing mentions. |
| paddle + ball | 0 outside the pong beat sheets | clear |
| "no perfect defense" | 0 outside the pong beat sheets (the essay's own line) | clear |
| speed ratio | 11 files, all group/phase velocity in quantum mechanics | False positives. Different physics. |
| atari | history-of-video-games film and a Spacewar essay | History, not mechanism. |
| reachab* | 359 files | Common word in agent/verification builds. Not about games. |

Caveats: the NEU-ISE post's Pong context was not read (the post is not on `origin/main`); read it before the script is
final. Sweep is text only.

### 2. Stricter simulation (`angle_check2.py`)
Discrete ticks, ball speeds up 5% per hit (start 6 px/tick), defender waits mid-field then runs, attacker searches
every aim. First hit at which some shot cannot be defended:

| Paddle speed (px/tick) | Predicted by the inequality | Simulated (aim reaches whole field) | Simulated (aim limited to a quarter of ball speed) |
|---|---|---|---|
| 1.0 | broken from the first hit | hit 0 | hit 0 |
| 1.5 | broken from the first hit | hit 0 | hit 4 |
| 2.0 | after 4.2 hits | **hit 5** | hit 9 |
| 3.0 | after 12.6 hits | **hit 13** | hit 18 |

The closed form matches the search to within the rounding up to the next whole hit. The last column is the new finding:
**narrowing how far the contact point can steer the ball delays the break by 4-5 hits.** That is the measured answer to
the essay's "which single rule breaks the balance" prompt: the paddle-speed dial and the hit-steering rule are the two
levers, and both are now numbers.

Scope: a model, not a reproduction of any specific machine. Paddle speed, field size and speed-up rate are our own
stated values. Say so on screen.

### Status
Angle holds. Next: pick the structure (rally replay with the dial turning down), then BEATS-DRAFT, FACTCHECK and the
read-aloud before any build, per the front-load rule.
