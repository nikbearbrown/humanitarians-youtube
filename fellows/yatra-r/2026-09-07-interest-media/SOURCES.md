# SOURCES — `yatra-interest-media` ("Interest Media.")

## The one external attribution

**Gary Vaynerchuk** — credited for the *interest media* framing: the argument that social
media, as it was, is effectively gone, and that feeds now sort by interest rather than by
social connection.

Supplied by the human on 2026-09-11 as **an already-paraphrased summary**, with an explicit
instruction attached:

> "Please credit Gary Vaynerchuk by name as the source of the 'interest media' concept, and
> don't quote him directly — this script is already paraphrased."

### What is therefore NOT in this reel

- **No quotation.** Nothing attributed to him is rendered in quotation marks anywhere. This
  is enforced by the type: `SourceData` has `claimParaphrase` and **no `quote` field**, so
  there is no code path by which a verbatim sentence could be attached to his name.
- **No citation metadata.** No date, no venue, no podcast episode, no book, no URL. None was
  supplied, so none is invented. Inventing a plausible-looking citation for a real person's
  real idea would be worse than citing nothing.
- **No characterisation of him** beyond being the source of the framing — no claims about
  his business, his other views, or his track record.

### What IS on screen

B02 renders his name as an attribution card in ink (never in the accent — provenance is not
the point of the beat), with the paraphrase beneath it and a chip reading
`PARAPHRASED — NOT A QUOTE` directly under the attribution, so the disclaimer cannot be
separated from the credit.

The credit is repeated at B09 (`Framing credited to Gary Vaynerchuk — paraphrased
throughout, not quoted, and not a study.`) and again at B10's verdict page.

## Everything else is the human's own argument

The remaining content is the human's own reading of that framing, applied to their own work.
It is the genre's evidence — a first-person marketing essay — rather than citable fact:

| Claim | Beat |
|---|---|
| Feeds surface creators you don't follow | B00, B03 |
| The signals are what you watched, paused on, searched for | B00, B03, B10 |
| There is too much posted daily for a personal network to surface the best of it | B04 |
| Platforms stopped asking "who do you know" and started asking "what do you care about" | B05 |
| The old model gated reach behind an audience you had to build first | B07 |
| One well-made post can now reach people who never heard of the brand | B07, B10 |
| The question shifted from more followers to earning attention, one post at a time | B08, B10 |
| This is changing how Yatra thinks about content for Humanitarians AI | B10 |

B09 exists to draw the line between what that argument supports and what it does not — see
`FACTCHECK.md` for the full refusal list, and note that `ItmLimits` **requires** both a
`provenance` and a `falsifier` string, so the beat cannot be authored without telling the
viewer how to check the claim themselves ("Test it on your own feed.").

## Corrections applied under DOUBLE-CHECK LAW

1. **"Basically dead" is kept soft and attributed.** The paraphrase says *not gone,
   transformed* in the same breath, because the rhetorical "dead" is the source's framing,
   not a factual claim the reel makes in its own voice.
2. **No statistics, at all.** The human's standing instruction across this whole series is
   not to invent figures. This topic has none supplied, so the reel claims none — and the
   components cannot render one (no numeric prop exists in the `Itm*` family).
3. **"Thousands of followers" stays spoken, never drawn.** The script's phrase survives in
   B07's narration because it is the human's own rhetorical phrasing of their own point, but
   it is **not** rendered on screen as a figure — the old-model track is labelled
   `build an audience first`. If even the spoken phrasing should go, it is one line of
   `narration_text` plus a regenerate of that beat's audio.
4. **"Followers are worthless" is explicitly refused.** B09 states the actual claim:
   followers stopped being the *entry fee*, which is a different and weaker statement.
5. **"Every feed works the same way" is explicitly refused.** The reel does not claim
   uniformity across platforms, because nothing supplied supports it.
6. **No platform is named.** No TikTok, Instagram, X or YouTube — naming one would imply
   platform-specific claims the reel cannot support.
7. **No model names or version numbers** — they date the video.
8. **The narrator does not claim the first person.** B00 establishes that Bella is *reading
   Yatra's notes*, so the "I" of the body is attributed rather than impersonated.

## Prior art check

The human asked for a video that is **not a variation of any previous one**. Verified:

- **All eight illustration components are new** (`InterestMedia.tsx` /
  `InterestMedia916.tsx`). The `Wk*` (Gordy), `Lnk*` (Nobody Wrote This), `Rcp*` (Brandy),
  `Seo*` (Assisted Not Automated), `Ytw*` and `Jdg*` families are all untouched — nothing is
  re-exported or re-skinned.
- **Different subject.** The five prior episodes are either weekly work recaps or
  statistics-led explainers. This is a concept explainer with no data in it at all.
- **No narration reused** — checked against every prior cold open and outro on this channel.
- **Fresh greeting.** `Vanakkam` (Tamil) — Namaste, Kumusta, Sawubona, Hej, Merhaba and
  Jambo are already spent on the six prior reels here.
- **New narrator framing.** First episode on this channel to introduce a stand-in voice
  ("Bella, in for Yatra"), at the human's request.

## Scene provenance

All eight components are new for this reel. No seeds, no generative assets, no stock, no
pantry media, no paid API calls — Kokoro + Remotion + ffmpeg, free and local. Every beat in
both cuts is a deterministic render.

One detail worth recording: `ItmVolume`'s field of post-marks is laid out by a seeded
hash (`rnd()`), not `Math.random()`, because Remotion renders frames independently and out
of order — an unseeded field would flicker. Same seed, same layout, every render. `MARKS`
and `TICKS` are exported from the landscape module and **imported** by the portrait one, so
the two cuts of one reel cannot drift apart on density.
