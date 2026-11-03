# MIDJOURNEY PART 2 — "Writing The Prompt"

**Runtime 3:16, 11 beats.** Part 1 shipped at 3:19.

## Why this part exists

It was **not in the original five-part plan at all** — the author raised the
gap on 2026-09-07. It sits at Part 2 because teaching dials before words is
backwards: varying a vague prompt returns four vague variations, and no
stylize value fixes an unclear subject.

Placing it here cost a **re-cut of Part 1**, which had already shipped a spoken
promise that Part 2 was the action rail. Three Part-1 beats were re-rendered
(BHTF, B04's two rail cards, B07's Upscale handoff) and every downstream part
shifted by one. Part 1 never states the series count, which is the only reason
that was possible — see `VIDEO-PIPELINE.md` §7.

---

## The spine: Midjourney's own seven, not our segmentation

**This is the one part in the series whose subject cannot be verified by a
screenshot.** Prompt craft is not a UI fact. So the evidence standard is
different, and stated explicitly:

| Claim type | Standard | Source |
|---|---|---|
| Product UI | captures only | `Midjourney Screenshots/` |
| Prompt craft | vendor documentation, cited per claim | docs.midjourney.com |
| Commentary | clearly ours, set apart on screen | this series |

The seven elements come from **Prompt Basics**, in the vendor's order, with the
vendor's own example strings:

| # | Element | Their question | Their examples |
|---|---|---|---|
| 1 | Subject | Who or what? | person, animal, character, location, object |
| 2 | Medium | In what form? | photo, painting, illustration, sculpture, doodle, tapestry |
| 3 | Environment | Where? | indoors, outdoors, on the moon, underwater, in the city |
| 4 | Lighting | What kind? | soft, ambient, overcast, neon, studio lights |
| 5 | Color | In what shades? | vibrant, muted, bright, monochromatic, colorful, black and white, pastel |
| 6 | Mood | Feelings to evoke? | playful, calm, gloomy, energetic |
| 7 | Composition | How is it framed? | portrait, headshot, closeup, birds-eye view |

**An earlier draft of this part used eleven slots I had derived myself** by
segmenting the workspace prompt. That was replaced the moment the vendor's list
surfaced. Ours was plausible; theirs is authoritative, and the difference is the
whole point of §8.

---

## The worked example

A **real prompt from this workspace**, transcribed character-for-character from
`Create Tab.png` — the undead wolf enemy from the gothic adventure character
set. It earns its place twice over:

1. It answers **all seven** documented elements, without having been written
   from a checklist.
2. It makes **the one mistake the docs warn about** — six exclusions written in
   plain text — which makes it a better teaching object than a clean invented
   example would be.

Three other prompts (vampire mother, vampire boy, graveyard zombie) are visible
in the captures but **truncated by the product's own rail**. Nothing beyond
their visible opening may be depicted, so they are not used as evidence for the
seven-element claim.

---

## Beat table

| Beat | Act | Scene | Actual |
|---|---|---|---|
| B00 | Cold open | `ClaudeComposerAsk` | 16.1s |
| B01 | BLUF — seven questions | `MjL2Bluf` | 20.7s |
| B02 | Subject and Medium | `MjL2Pair1` | 20.0s |
| B03 | Environment and Lighting | `MjL2Pair2` | 21.6s |
| B04 | Colour and Mood | `MjL2Pair3` | 20.2s |
| B05 | Composition | `MjL2Solo` | 21.9s |
| B06 | A real prompt, scored against all seven | `MjL2Score` | 17.1s |
| B07 | What to leave out — and the `--no` trap | `MjL2No` | 23.8s |
| BVDT | Verdict | `ClaudeVerdictArtifact` | 19.2s |
| BHTF | Part 3 tease | `ClaudeComposerAsk` | 12.9s |
| BOUT | Outro | `ClaudeTitleOutro` | 2.9s |

---

## Scenes — three components, seven compositions

`MjL2Seven` serves **five beats** (B01–B05), differing only by `focus`. The
grid, every count and every label derive from the `MJ_SEVEN` array. Five
hand-rolled copies of a seven-card grid would drift within a day — the lesson
`sunoAdvancedPanel` paid for on Suno.

Each of the five still needs **its own `<Composition>`**, because
`durationInFrames` must equal that beat's audio length and every cue is a
fraction of it. A shared composition would be freeze-extended or truncated to
the other four and the cues would drift (`VIDEO-PIPELINE.md` §6).

- **`MjL2Seven`** — the 4-over-3 grid. Focused cards hold full colour; the rest
  **desaturate rather than fade**, because a translucent card over the cream
  page composites to a grey slab. Both directions of that mistake shipped on
  Suno.
- **`MjL2Score`** — the prompt in full on the left, the seven ticking off on the
  right. Ticks are drawn SVG, not emoji, after Part 1's missing-glyph fix.
- **`MjL2No`** — three columns: the quotation, the documentation, the fix. Then
  the word-splitting trap full width.

---

## What the cue pass caught before any render

Measuring anchors against the word clock found four problems that would each
have cost a re-render:

| Beat | Problem | Fix |
|---|---|---|
| B01 | `first` resolved at **0.921** — payoff line with 1.6s left | re-anchored to "comes back wrong" → 0.766 |
| B03 | both movements done by **0.257**, leaving ~13s static | added a third late movement (the in-prompt chips) |
| B02 · B04 · B07 | third/trap at **0.937 / 0.915 / 0.957** | re-anchored off the final phrase |
| B07 | `docs` anchor **orphaned** by a word trim | re-anchored to "describe what you do want" |

The orphaned anchor is exactly the failure `VIDEO-PIPELINE.md` §2 warns about:
a reworded line silently breaks its cue. The script caught it; reading would
not have.

---

## Register applied

- Host opens "Hi, I'm Rohaan from Humanitarians AI"; full name **once**, in BOUT.
- **The series count is never stated.**
- No version numbers. No pricing. No plan names.
- Heteronyms removed at draft: `object` (verb stress), `in a minute`,
  `read it against` → `check it against`, `is read` → `is taken`.
  `subject` is unavoidable — it is one of the seven element names.
- `--no` is spoken as "two dashes, then no" because Kokoro cannot voice glyphs.

---

## What this part deliberately does NOT claim

- That the other three prompts share all seven elements. **Their rails cut them
  off** — only the opening is legible.
- That the wolf images failed because of the plain-text negation. The docs call
  the pattern unreliable; the four images in the capture plainly worked. Going
  from "documented as unreliable" to "this failed" would be inference presented
  as observation.
- Anything about how the prompt was written. An earlier draft said "nobody was
  ticking boxes" and "an earlier attempt cut the paws off" — both invented, both
  cut, both now blocked by `check_beats.py`.
- Any parameter behaviour beyond `--no`. The dials are Part 4; this part is the
  words you type.
