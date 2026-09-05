# SOURCES — `yatra-nobody-wrote-this` ("Nobody Wrote This.")

## The two sources

1. **Pangram Labs, "AI in Your Feed," July 2026** — the platform scan. Supplies
   claims 1–6 in `FACTCHECK.md`: the 41% LinkedIn figure, the 1-in-4
   cross-platform rate, the corpus/detection split (a third of ~1M posts scanned
   vs nearly 62% of AI content detected), the five-platform comparison, the 4.3%
   assisted share, and the "Enhance Post" / downranking contradiction.
2. **Tech Times** — supplies the EU AI Act Article 50 effective date
   (August 2, 2026), and is co-cited with Pangram Labs on the all-or-nothing
   4.3% figure.

Both were supplied by the human on 2026-09-01 and are cited on screen exactly as
given. No URL was provided for either; the on-screen citation is the publisher,
title and date as supplied.

## Where each citation renders

| Beat | On-screen citation |
|---|---|
| B02 | `Framing: Pangram Labs, "AI in Your Feed," July 2026` |
| B03 | `Pangram Labs, "AI in Your Feed," July 2026` |
| B05 | `Pangram Labs, "AI in Your Feed," July 2026` |
| B06 | `Pangram Labs, "AI in Your Feed," July 2026` |
| B07 | `Pangram Labs / Tech Times` |
| B08 | `Pangram Labs, "AI in Your Feed," July 2026` |
| B10 | per-block: `Tech Times` on the regulation block; the reputation block is tagged `INTERPRETATION` and reads `the narrator's read, not a published finding` |
| B11 | each verdict line carries its own parenthetical citation |

## Corrections applied under DOUBLE-CHECK LAW

Logged here because the law requires the rewrite to be visible, not assumed.

1. **De-sensationalised the frame.** The obvious headline — "AI slop is taking
   over social media" — is not supported by the data supplied, which shows
   Substack at ~10% and Reddit as low as 4% in the same scan. The reel's thesis
   was narrowed to the platform-specific claim the evidence actually makes, and
   B09 turns that low floor into the falsifier rather than burying it.
2. **Kept "generated" and "assisted" structurally separate.** These are two
   different bins in the source's own classification and the distinction is the
   reel's argument, so no beat blurs them into "AI-involved."
3. **Refused the derived third bin.** See `FACTCHECK.md` — 54.7% is available by
   subtraction and appears nowhere, in narration or on screen.
4. **Labelled the opinion.** The "personal brand is suspected by default"
   argument in B10 is the narrator's inference, not a finding in either source,
   and is tagged `INTERPRETATION` on screen beside the dated regulatory fact.
   Saying it only in the voice would have left the frame implying a citation it
   does not have.
5. **Stripped anything that dates the video.** No model names, no version
   numbers, no follower or engagement counts.
6. **Kept the ranges as ranges.** "25–29%" and "4–13%" are rendered with their
   ranges intact rather than collapsed to a single midpoint on screen; the
   midpoint exists only as a bar-drawing instruction, recorded in `FACTCHECK.md`.

## Prior art check (this is a NEW video, not a variation)

The toolkit already contains a LinkedIn-titled reel — `ClaudeLinkedin.tsx` /
`claude-linkedin-timing.json`, segment "Claude + Linkedin." — but it is a
different video on a different subject: how to train Claude on your own best
LinkedIn posts so it writes in your voice, ending in a `/linkedin-post` skill.
This reel shares no beat, no scene component, no narration and no thesis with
it. Noted here because the two sit adjacently in the repo and because this reel's
argument runs somewhat against that one's premise — worth Yatra's awareness
before both are published, but they are not variations of each other.

## Scene provenance

All nine illustration components are new for this reel and live in
`runtime/remotion/src/scenes/NobodyWroteThis.tsx` (+ `NobodyWroteThis916.tsx`),
with one deliberate reuse: `LnkFalsify` / `LnkFalsify916` alias `JdgStakes` /
`JdgStakes916` from `JudgmentIsTheJob`, whose shape (N named things, each with a
one-line why, plus a closer) is exactly B09's. No seeds, no generative assets, no
paid API calls — the whole build is Kokoro + Remotion + ffmpeg, free and local.
