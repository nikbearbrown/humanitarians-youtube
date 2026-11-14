# FRICTIONAL — What We Ask For.

## 2026-11-13

**Tried / expected.** A new ai-explainer on how AI is redefining human creativity and labor, using
seven supplied findings from five sources (Gallup, AI Buzz, Envato via AI Buzz, Creativepool, RI
Study Post), the intro "Hi, this is Yatra, Social Media Manager at Humanitarians AI", `@Yatra`
everywhere, native 4K in 16:9 and 9:16. Arc: earnings didn't broadly fall → a split → meaning stays
human, ending on "what are we actually asking for, when we ask for art?"

**Where it resisted, and what was done next.**
- *Skill tier.* `deep-explainer` needs Bear's sign-off; built on `ai-explainer` instead.
- *Voice.* Asked for `af_kore`, but the toolkit's audio script only allows `am_onyx` / `af_bella`;
  used `af_bella`, the voice of every earlier @Yatra episode.
- *Length.* Narration measured 4:13.7, over the usual 1–3 minutes; kept at 4:14 by choice. The 9:16
  is therefore too long for an Instagram Reel.
- *Act cards.* First-pass part cards ran 1.5–2.2 s; lengthened their lines and regenerated only those.
- *Layout.* Frame QC caught three 16:9 defects (B03 label collision, B08 value overflowing the edge,
  B14 small type) and four 9:16 ones (B04, B09, B10, B13 overlaps). All fixed and re-checked.
- *iCloud.* Mid-render, macOS offloaded ~15,000 toolkit files to iCloud (disk 92% full) and Remotion
  failed with `dotenv.config is not a function`. Set the folder to Keep Downloaded, pulled the files
  back with `brctl download`, then finished the 9:16.

**What Claude contributed, and what was accepted / changed.** Claude drafted the beat sheet and
narration, wrote the eleven `Wwa*` scenes (`scenes/WhatWeAskFor.tsx`), ran audio/render/compile, and
did the frame-level QC. I chose the skill, branding, voice and length. No figure beyond the seven
supplied was added; the earnings beat is a schematic with no data plotted.

**Now understood / still open.**
- Keep the toolkit off an optimized iCloud Desktop, or pinned with Keep Downloaded.
- Open: the source reports were not independently re-checked in this build.
- Masters are local (not committed): `~/Downloads/brutalist-reels/youtube/yatra-what-we-ask-for/`.
