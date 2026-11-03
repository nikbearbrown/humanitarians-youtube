# Feedback: "What Had to Be Invented" — the Short (9:16)

**Verdict:** clear-for-public. **Trailer rubric 12/12.** Production gate **PASS**.

*Review 2: B02 trimmed, chrome fixed. See the bottom.*

One line: the cut keeps every promise it makes now, including the one it used to break.

`what-had-to-be-invented-short.mp4`, **2160×3840 @ 30 fps, 97.02s (1:37.0)**, h264 + aac,
7 beats, **−16.2 LUFS / −2.0 dBTP**, crest factor 4.96.

*Narration is the parent film's, reused verbatim except for two recorded trims. No new
words, so the parent Gate P signature of 09/13/2026 covers every word heard.*

*Scored against the trailer standard established in the topic-video Short's review, not
PROOF's explainer rubric — `PROOF.md` has no short-form provision, and scoring a trailer for
not teaching a full framework penalises it for being a trailer.*

---

## The problem — RESOLVED in review 2

**B02 says "I am going to walk five stages and show you which of the three each one took."
The Short then walks one.**

The cut runs B00 → B01 → B02 → ASK → B06 → B14 → END. Stage three is the only stage in it.
A viewer is told five are coming, gets the validation gate, and goes straight to the task
beat. That is a promise the cut does not keep, and it is the mirror image of the defect
already fixed one beat later: B06's audio was head-trimmed to remove "Stage three," because
that reference had nothing to point at. The same treatment was never applied to B02's tail.

**The fix is the same technique, on the other end of the beat.** Trim B02's final sentence at
the pause before "I am going to walk five stages." What remains ends on *"...or refuse, and
leave the hole exactly where the evidence stopped"* — a clean close for the framework, with
no forward promise. Roughly 5 seconds off an 18.2s beat, and no word is rewritten, so the
signature still holds.

This is worth fixing rather than waving through, because the promise is specifically about
structure: a viewer counting stages notices when four never arrive.

---

## Production gate — PASS

Scored against the rendered master with the platform's own UI zones shaded over every frame,
which is what caught the topic Short's sources sitting under the YouTube chrome.

| Criterion | Result |
|---|---|
| Evidence legible at the moment of assertion | **PASS** — all 7 beats sampled at 55% of their own duration; content complete and holding |
| Sources on screen, not just voiced | **PASS** — B00 carries `schedule_handoff.py` lines inline, B06 carries `validation_gate.py 5-8, 34-40 · Capital One blog, Mar. 5 2025`, both **inside the safe area** |
| Side-by-side at the moment of comparison | **PASS** — B06 holds the two confirmed check names above the constructor that refuses, so the confirmed and the not-published sit in one frame |
| Safe area | **PASS** — no text in the bottom UI band or the action-button column; card edges cross it, no text does |
| Loudness | **PASS with a stated trade** — −16.2 LUFS at −2.0 dBTP. Deliberately ~1.4 dB below the other three cuts, because reaching -14.9 took three normalisation passes and four AAC generations, which was audible. See review 3 |

---

## Rubric — 12/12

| Criterion | Score | Why |
|---|:--:|---|
| **Stands alone** | **2** | Both dangling references now trimmed and recorded — B06's opening and B02's closing |
| **One idea, not a summary** | **2** | One question, asked once, answered at the gate. It does not try to compress five stages into 100 seconds |
| **Sourced on screen** | **2** | Both claim-bearing beats carry an attributable source, in the safe area, landing with the chrome |
| **Demonstrates rather than asserts** | **2** | B06 shows the constructor raising, with the blog's own two check names quoted above it |
| **Leaves something for the film** | **2** | Four of five stages, the cost beat, the edge beat and the counts are all film-only, and the end card names what is missing |
| **Points at the film** | **2** | *"the full film — 4:42 / five stages, and where the framework stops"* |

**Friction is present and it is the best thing in this cut.** The silent `ASK` card puts the
three moves up with "which one?" and holds — then B06 answers. It cost no narration, so no
second read was needed, and it is the one moment the viewer participates.

---

## Minor, worth a pass before assembly

- **The `ASK` card's chrome reads "ASK ASK."** Beat id and act are the same string, so the
  header prints it twice. Cosmetic, one-line fix.
- **B06 has a dead band** of roughly 300 px between "assume one." and its citation. Nothing
  overlaps and nothing is unsafe; it is just loose in a format where vertical space is the
  scarce thing.

---

## What works

- **The silent ASK beat solves a real problem cleanly.** The parent's friction is a
  setup/payoff pair across five beats and neither half survives a 100-second cut. Building a
  new question out of material already on screen — and adding no words — got friction into
  the Short without touching the gate.
- **The end card was right first time.** It names the runtime and what the film holds that
  the Short does not, which is the lesson the topic Short had to learn the hard way.
- **B06 is the correct single stage to keep.** It is the only one where the build refuses
  rather than constructs, so the Short keeps the moment the method is most visible.
- **Vertical suits quoted code better than expected.** Re-wrapping the blog quotes and the
  constructor into a narrow column reads more like a file than the 16:9 version does.


---

## Review 2 — B02 trimmed

| Item | Outcome |
|---|---|
| B02's five-stages promise | **Trimmed.** The closing sentence was cut at the detected pause at **14.00s** (the gap runs 13.69–14.31s, the longest inside the beat). B02 now ends on *"...or refuse, and leave the hole exactly where the evidence stopped."* No audio regenerated, no word rewritten — the parent Gate P signature still covers every word heard. Recorded in the beat's `edit_note` |
| `ASK ASK` chrome | **Fixed.** The act is now `YOUR CALL`, so the header no longer prints the beat id twice |
| B06's dead band | **Left alone.** Nothing overlaps and nothing is unsafe; tightening it would have meant re-rendering a beat to buy whitespace |

Runtime 1:42.6 → **1:38.3**. Loudness came out **−14.9 LUFS / −2.3 dBTP** — closer to the
other three cuts than before the trim, because a shorter cut with the same content reaches
the band in the same three passes.

**Stands alone 1 → 2, so 12/12.** Both dangling references in this cut turned out to be
trims rather than rewrites: B06's opening sequence reference, and B02's closing promise. Same
technique, opposite ends of the beat. Worth noting as a pattern — when a Short inherits
narration written for a longer film, the breaks are usually at beat edges, and a trim at a
detected pause fixes them without reopening the gate.


---

## Review 3 — audio rebuilt, and a real defect I had missed

Tanmay listened to the cut and reported two things I had not caught: the narration was
breaking up, and there was a long dead pause partway through. Both were real. **I had
verified loudness and true peak on every pass and never once checked whether the audio
sounded right** — a file can sit exactly inside spec and still be damaged.

### The breakup: four generations of lossy audio

The old chain encoded AAC per beat, concatenated, and then `normalise.py` re-encoded the
whole file once per pass. Reaching the loudness band took three passes, so the delivered
audio had been through **four** lossy generations. Measured: crest factor had collapsed from
**10.4** in the source mp3s to **3.97**.

`build_short.py` is rebuilt so audio stays lossless until the last step:

```
per-beat mp3 -> padded PCM -> concat PCM -> loudnorm (PCM, one pass) -> AAC once
```

Video is concatenated by stream copy and never re-encoded. Result: **one** AAC generation,
crest factor **4.96**.

### The pause: 3.1 seconds of dead air

Located by measurement, not by ear-guessing — `silencedetect` put a single 3.11s silence at
47.98s, which is exactly the `ASK` beat. I had sized that hold at 3.0s by analogy with the
topic video's 2s silent hold, but **that hold sits inside a narrated beat**, with speech
either side of it. This one has silence on both sides, so it played as a stall.

`ASK` is now **1.8s**. The measured silence is 1.97s, and the reason is recorded in the
beat's `silent_note` so it is not "tidied" back up later.

### The cost, stated plainly

Single-pass normalisation on ~20 dB-crest narration undershoots, so the Short now sits at
**−16.2 LUFS** instead of −14.9 — about 1.4 dB quieter than the other three cuts. That is
the right trade: YouTube attenuates loud material and does not boost quiet material, so the
only consequence is that it plays slightly softer, whereas audible breakup is a defect.

**Do not run `normalise.py` on this file.** It would re-encode and undo the whole point. The
loudness stage now lives inside `build_short.py`, on the PCM, before the single encode.

### What this should change elsewhere

The other three Week 22 cuts have two AAC generations each and crest factors of 4.32–4.44 —
better than 3.97 but worse than they need to be. The same lossless chain would improve all
of them. Not done here, because it means recompiling the 4:42 and 4:52 masters, and that is
Tanmay's call rather than a change to make silently.
