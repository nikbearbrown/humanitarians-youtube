# FRICTIONAL — Be the Sentence.

## 2026-11-05

**Tried / expected.** A 1–3 minute ai-explainer on AI-cited authority — SEO becoming "Search
Everywhere Optimization" — using seven supplied findings from six sources, the intro "Hi, this is
Yatra, Social Media Manager at Humanitarians AI", `@Yatra` bug, native 4K in 16:9 and 9:16.

**Where it resisted, and what was done next.**
- *Intro changed mid-build.* First brief said "[voice name], in for Yatra"; updated to the fixed
  first-person intro before any audio was generated.
- *Pronunciation.* Kokoro read "SEO" as "see-oh"; narration spells "S.E.O." and spoken years.
- *Length.* First narration measured 3:13; trimmed once to 2:52 so the Short lands at 2:56.8.
- *Layout.* Preview stills showed a bracket line cutting a label (B04) and a connector crossing
  chips (B09 portrait); fixed before the 4K render.
- *Bundling.* `remotion bundle` failed on broken `public/` symlinks to another machine; preview
  stills used an empty public dir instead. The pipeline renders were unaffected.

**What Claude contributed, and what was accepted / changed.** Claude drafted the beat sheet and
narration, wrote the nine new `Geo*` scenes (`scenes/AiCitedAuthority.tsx`, one component per scene
laying out for both aspects), ran audio/render/compile, and did the frame-level QC. No figure beyond
the seven supplied was added; no gap, remainder or multiple is printed.

**Now understood / still open.**
- Open: the source reports were not independently re-checked in this build.
- Masters are local (not committed): `~/Downloads/brutalist-reels/youtube/yatra-be-the-sentence/`.
