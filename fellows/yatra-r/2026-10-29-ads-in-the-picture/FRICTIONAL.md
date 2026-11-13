# FRICTIONAL — Ads in the Picture.

## 2026-10-29

**Tried / expected.** A 1–3 minute ai-explainer on ChatGPT testing visual ads in image
generation, alongside the "dots" agents announcement — three supplied points, one source
(Jumpfly, October 2026), standard "Bella, in for Yatra" intro, `@Yatra` bug, true 4K in
16:9 and 9:16. Built with Claude Code on the brutalist.art toolkit, following the
`both-sides-of-the-table` reel as the template.

**Where it resisted, and what was done next.**
- *Length.* First narration measured 3:32 — over the brief and the Shorts cap. Trimmed
  twice (2:57, then 2:54) so the Short plus its 4.5 s endcard lands at 2:58.
- *"A first."* The brief framed this as ChatGPT's first ads. A search turned up early-2026
  reports of ads already running for US Free and Go users, so the reel says "a new visual
  ad format" and never "first". Logged in FACTCHECK.md.
- *Unverified source.* The Jumpfly piece itself could not be found online; the three
  points are rendered as reported and attributed, and FACTCHECK.md says so.
- *Layout collisions.* Preview stills showed the BLUF rails cutting through text (both
  aspects), the dot label under its pulse ring, a "?" clipping a word, and a portrait
  title running into its window. Fixed in the scene source before the 4K render.
- *Render time.* 4K renders of the shared composer scenes are slow; ran in the background.

**What Claude contributed, and what was accepted / changed.** Claude drafted the beat
sheet and narration, wrote the eight new `Adp*` scenes (`scenes/ChatAds.tsx`,
`ChatAds916.tsx`), ran audio/render/compile, and did the frame-level QC. The "first"
correction and the narration trims came from that pass; nothing beyond the three supplied
points was added.

**Now understood / still open.**
- Open: confirm the Jumpfly article directly before publishing.
- Open: whether to restore "first" in the framing — currently left out on purpose.
- Masters are local (not committed): `~/Downloads/brutalist-reels/youtube/yatra-ads-in-the-picture/`.
