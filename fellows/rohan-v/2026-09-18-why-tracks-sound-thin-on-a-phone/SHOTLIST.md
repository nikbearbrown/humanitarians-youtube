# SHOTLIST — "Why Your Track Sounds Thin On A Phone"

Seven beats, 124.97s (2:05). Every duration is the measured Kokoro narration
length; the visuals are cut to fit the voice, never the other way round.

**This reel is word-clock choreographed.** `align.py` (faster-whisper) measured
when every word is actually spoken, `cues.json` names an anchor phrase per
reveal, and `sync_cues.py` resolved those phrases into fractions and wrote them
into the beat sheet at `shot.remotion.props.cues`. Nothing below is a guessed
timing — the *cue* column is the fraction of the beat at which that phrase
leaves the narrator's mouth. 28 cues, 28 resolved, 0 unmatched.

| Beat | Act | In | Dur | Component | Lane |
|---|---|---|---|---|---|
| B00 | ASK | 0:00 | 17.94s | `ClaudeComposerAsk` | chassis |
| B01 | BACKGROUND | 0:17 | 21.95s | `MonoTwoSidesOneSpeaker` | **new** |
| B02 | ANALOGY → IDEA | 0:39 | 20.59s | `MonoDoorToWaves` | **new** |
| B03 | MECHANISM | 1:00 | 19.22s | `MonoWhatSurvives` | **new** |
| B04 | SUBTLER CASE | 1:19 | 18.92s | `MonoHolesNotSilence` | **new** |
| B05 | WHAT TO DO | 1:38 | 17.13s | `HaiApplyCard` | library |
| B06 | OUTRO | 1:55 | 9.22s | `HaiTitleOutro` | library |

The shape follows the same correction that reshaped the sibling reel — *"Explain
it as if the viewer is new to the topic completely"*. Two whole beats go by
before the word "cancel" does any work: B01 establishes that music has two sides
and that one speaker has to add them, and B02 makes adding-to-nothing obvious
with a door.

## Choreography — what happens, and on which word

### B01 `MonoTwoSidesOneSpeaker` — two sides, two destinations

| cue | spoken phrase | what the viewer sees |
|---|---|---|
| 0.102 | "a left and a right" | two lanes, LEFT in ink and RIGHT in blue, carrying visibly different waves |
| 0.269 | "makes music feel wide" | SLIGHTLY DIFFERENT — THAT IS THE WIDTH |
| 0.361 | "Headphones keep them apart" | left card: two separate cups, two separate paths down from the two lanes |
| 0.717 | "one single speaker" | right card: PHONE · LAPTOP · SMART SPEAKER, a single breathing cone |
| 0.940 | "add them together" | both paths bend inward and meet at a terracotta **+**; *one cone, one position* |

Both destinations stay on screen together. The beat is a contrast, and a contrast
needs its two halves visible at the same instant.

### B02 `MonoDoorToWaves` — a door that actually moves

| cue | spoken phrase | what the viewer sees |
|---|---|---|
| 0.044 | "pushing the same door" | a door on its hinge, two figures either side |
| 0.133 | "push the same way" | both arrows one way; the door **swings** on a sine; IT SWINGS OPEN |
| 0.311 | "one pushes while the other pulls" | the right arrow flips; the wave panel arrives and the two lanes go out of phase |
| 0.457 | "does not move at all" | the door locks to zero with a faint jitter; NOTHING MOVES · *both of them working just as hard* |
| 0.808 | "Where they agree" | the sum lane collapses to a flat line reading NOTHING; the closing sentence lands |

The door swinging is the whole beat. A still diagram of two opposed arrows is a
physics figure; a door that moves and then refuses to is an argument.

**A bug worth recording:** in an earlier pass the two arrows pointed the same way
during the "pushing against each other" state, contradicting the narration on
screen. `person(1, opposed > 0.5 ? -1 : 1, …)` fixes it. Caught by reading the
contact sheet frame by frame, not by any gate.

### B03 `MonoWhatSurvives` — position first, outcome second

| cue | spoken phrase | what the viewer sees |
|---|---|---|
| 0.012 | "built a track and measured" | three rows arrive: bass, vocal, wide airy layer |
| 0.177 | "both sitting in the centre" | the two centred rows light; their stereo-field strips show one dot in the middle |
| 0.257 | "came through untouched" | their bars hold at full length · **unchanged** |
| 0.451 | "wide, airy layer" | the third row's strip shows two dots pushed to the edges · SPREAD ACROSS BOTH SIDES |
| 0.763 | "Effectively gone" | its bar collapses; **−49.5 dB — effectively gone** |

The position strip on the left is what makes this teach rather than report. You
can see which parts are in the middle *before* any bar moves, so the result reads
as predictable — and predictability is the thing a viewer can apply.

Position markers use `Circle` from `@remotion/shapes` rather than a div with
`borderRadius: 999`: a real SVG circle stays perfectly round when the 1080 layout
is rendered at 2× for 4K, where a rounded div can show flat spots.

### B04 `MonoHolesNotSilence` — the honest caveat

| cue | spoken phrase | what the viewer sees |
|---|---|---|
| 0.014 | "rarely that dramatic" | the caveat, in prose: total silence is the clean example |
| 0.208 | "delaying one side" | two sine paths, one dashed and arriving slightly late |
| 0.470 | "only certain frequencies cancel" | a strip of 26 solid segments, low notes to high |
| 0.705 | "lose holes out of it" | roughly a third of the segments **punch out**, comb-spaced |
| 0.913 | "hollow rather than silent" | the verdict |

**The axis carries no numbers, on purpose.** The measurement behind this beat
predicted nulls at 830 Hz and 2500 Hz and then landed on all four predicted
positions — it is the most interesting result in either week-04 reel, and it is
not on screen. A viewer meeting stereo for the first time does not need a
comb-filter chart; the *shape* is the lesson. The numbers are in
[MEASUREMENTS.txt](./MEASUREMENTS.txt).

### B05 `HaiApplyCard` — the ten-second check

| cue | spoken phrase | what the viewer sees |
|---|---|---|
| 0.018 | "costs ten seconds" | the card's eyebrow and lede |
| 0.195 | "switch your track to mono" | step 1 |
| 0.358 | "vocal jumps forward" | step 2 |
| 0.599 | "usual culprits" | steps 3 and 4, then the spark line |

### B06 `HaiTitleOutro` — `close` at 0.369

The HAI end card, not `ClaudeTitleOutro`. That component is locked to
@NikBearBrown by `OUTRO-LOCK.md` and silently ignores `handle` and `subline`, so
a reel for @HumanitariansAI that used it would end on the wrong channel.

## Emphasis discipline

Every new component routes its stage weights through `exclusive()` from
`cueKit`: each highlight **retires as the next one arrives**. Without it all five
stages of a beat are lit by its end, and the frame reads as five competing
emphases instead of a walkthrough.

## Continuous motion

| Beat | What is always moving |
|---|---|
| B01 | both lanes' waves scroll; the single cone breathes on `noise2D` |
| B02 | the door swings on a sine, then jitters against itself before locking |
| B03 | nothing needs to — the bar collapse is the event |
| B04 | both sine paths scroll, one permanently behind the other |

## Shell early, content on the word

A beat's *layout* — card, panel, axis, footnote — arrives as soon as its section
is introduced; the thing that teaches waits for the phrase that earns it. This was
adopted after Gate V failed B02 for underfill (50% against a 55% floor): the
canvas-fill law measures the bounding box of all ink, and with the wave panel
keyed to `agree` (0.808) the right half of that frame was genuinely empty at its
midpoint. Moving the panel to `opposite` fixed the gate **and** improved the
teaching — the viewer now watches the two lanes go out of phase as the narration
says they do, instead of meeting an already-collapsed sum.

## 9:16

Native portrait re-render via THE ONDA CHECK — `shorts.py` rewired all seven
beats to their `916` siblings, four of them written for this reel. Never a crop.

What actually changed, rather than shrank:

| Beat | Landscape | Portrait |
|---|---|---|
| B01 | two lanes above, two destination cards side by side | cards **stay** side by side — the beat is a contrast, and a contrast read top-to-bottom becomes a sequence. The lanes shorten and carry fewer cycles so the two sides still read as *different* |
| B02 | door in a left column, waves in a right one | a sequence: door, then the bridge sentence alone, then the waves. The door assembly centres on the frame so both figures fit at full size |
| B03 | each row reads across — name, position, outcome | each row becomes a card read downward; bars still start at the same x so the collapse is still one vertical comparison |
| B04 | 26 band segments | 18 — at 936px wide, 26 segments leave teeth thinner than the gaps once a third punch out. `isHole` is written in terms of the count, so the null spacing keeps its shape |

Content is confined to the active band y 230–1440; the top 12% and bottom 25%
belong to platform UI.
