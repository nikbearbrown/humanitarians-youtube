// Root.registration.tsx — the exact lines this reel adds to
// brutalist.art/runtime/remotion/src/Root.tsx.
//
// remotion_scenes.py passes shot.remotion.pattern straight to
// `npx remotion render` as a composition id, so every pattern used by
// beat_sheet.json must be registered here or the render fails.
//
// durationInFrames is round(measured audio seconds x 30). Audio is generated
// first and its measured durations are the master clock.
//
// B00 and B08 use the shipped ClaudeComposerAsk composition, already
// registered upstream — no new entry is needed for those two.
//
// 1. Add this import at the top of Root.tsx:

import {MvbPromise, MvbFloorPlan, MvbWeapons, MvbOneOrg, MvbFourOrgs, MvbSplitBelts, MvbUndisputed, MvbTest, MvbOutro} from './scenes/MmaVsBoxing';

// 2. Add this block inside <RemotionRoot>:

{/* ── mma-vs-boxing — reel-local compositions ── */}
      <Folder name="MmaVsBoxing">
        <Composition id="MvbPromise" component={MvbPromise}
          durationInFrames={566} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="MvbFloorPlan" component={MvbFloorPlan}
          durationInFrames={486} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="MvbWeapons" component={MvbWeapons}
          durationInFrames={731} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="MvbOneOrg" component={MvbOneOrg}
          durationInFrames={812} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="MvbFourOrgs" component={MvbFourOrgs}
          durationInFrames={608} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="MvbSplitBelts" component={MvbSplitBelts}
          durationInFrames={670} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="MvbUndisputed" component={MvbUndisputed}
          durationInFrames={512} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="MvbTest" component={MvbTest}
          durationInFrames={597} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="MvbOutro" component={MvbOutro}
          durationInFrames={102} fps={30} width={1920} height={1080}
          defaultProps={{}} />
      </Folder>
