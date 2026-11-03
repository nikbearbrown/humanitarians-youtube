# CHECKS-REPORT — no-face-no-problem

## Chassis

User asked for a "Deep Explainer" at exactly 4:00, sourced from a
user-supplied article. The toolkit's actual `deep-explainer` skill targets
5-10 minutes (duration as an output, never a fixed target) and requires
~20-25% of body beats to be pantry/archival stills, routed through a
two-gate sourcing pipeline that can block on unresolved sourcing. Both
conflict with this request: a hard 4:00 target, and the user's own note
that no dedicated footage exists for this topic. Built instead on the
`ai-explainer` chassis (Claude composer cold open -> body -> handoff ->
outro), matching the precedent set on this user's three prior article-based
builds this session (death-of-the-generic-resume, ai-nonprofit-marketing,
rescue-reinvented).

## B00B presenter-intro pattern

"Hi, I'm Agrima" lives in its own dedicated B00B beat (name + lead-in),
not folded into B00's cold-open narration — the established fix from this
user's earlier death-of-the-generic-resume correction, applied proactively
from the start here.

## B01's deliberate departure from the composer-card pattern

Per the user's own materials note ("on-screen captions rather than a host
on camera for the relevant sections, which would actually reinforce the
article's own point"), B01 is built as an abstract stock-footage-style
card rather than a composer or presenter card — a deliberate creative
choice performing the article's subject, not a compromise being disclosed
apologetically.

## Hedged-stat handling

Two stats in the source article are explicitly hedged by the article
itself and sourced only to AI-content-tool vendor blogs with no
independent data: the "big share of new creator ventures" claim (B02) and
the "majority find faceless content more trustworthy" claim (B05). Both
are narrated with the article's own hedge language. B05 additionally
carries an EXPLICIT on-screen skepticism flag in its Manim visual — see
FACTCHECK.md for full sourcing detail.

## GATE A (static pre-flight)

- B00B_AgrimaIntro: WARN (text-only, no tracked shapes — expected)
- B01_TheHook: CLEAN
- B02_TheStrategy: CLEAN
- B03_TheVoiceGap: CLEAN
- B04_WhereItPays: WARN (text-only, no tracked shapes — expected)
- B05_TrustFinding: WARN (text-only, no tracked shapes — expected)
- B06_TheReframe: CLEAN
- B07_ClosingQuestion: WARN (text-only, no tracked shapes — expected)

Zero ERROR across all eight scenes. (B04 and B05 WARN despite having
card/box animations — a known GATE A stub quirk with `LaggedStart`/
single-mutation `.animate` calls not always registering as tracked shape
state; confirmed harmless by the real pixel-level GATE B pass below.)

## GATE B (real pixel-level layout audit)

- B00B_AgrimaIntro: 5 snapshots -> CLEAN
- B01_TheHook: 6 snapshots -> CLEAN
- B02_TheStrategy: 12 snapshots -> CLEAN (after a real fix — see below)
- B03_TheVoiceGap: 6 snapshots -> CLEAN
- B04_WhereItPays: 4 snapshots -> CLEAN
- B05_TrustFinding: 6 snapshots -> CLEAN
- B06_TheReframe: 7 snapshots -> CLEAN
- B07_ClosingQuestion: 5 snapshots -> CLEAN

**Real bug found and fixed**: B02's connecting arrows were computed with
too little clearance (`buff=0.08`) between each flow-node's edge and the
arrow terminus, flagging "label on a curve/line" warnings on 4 of the 5
node labels (the arrow tips sat close enough to the node text to register
as visual overlap). Fixed by widening the flow nodes (1.9 -> 2.0 units),
tightening inter-node spacing slightly to compensate, and increasing the
arrow `buff` to 0.24 with a larger tip ratio — re-verified CLEAN after the
fix, with no further warnings.

## Duration

Estimated ~240s across 11 beats (4:00), matching the user's "exactly 4
minutes" request for the 16:9 cut. Real durations are the Kokoro mp3
lengths, measured before rendering, per this toolkit's audio-first
principle — expect the actual total to land within the same rough range,
not forced to an exact frame count.
