import {Pe9Promise, Pe9Solver, Pe9Sources, Pe9Routes, Pe9Ambiguous, Pe9Why, Pe9Limit, Pe9Verdict, Pe9Outro} from './scenes/PhysicsEngine09';

      {/* ── same-problem-same-answer (PhysicsEngine09) — reel-local compositions ── */}
      <Folder name="PhysicsEngine09">
        <Composition id="Pe9Promise" component={Pe9Promise}
          durationInFrames={552} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="Pe9Solver" component={Pe9Solver}
          durationInFrames={684} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="Pe9Sources" component={Pe9Sources}
          durationInFrames={692} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="Pe9Routes" component={Pe9Routes}
          durationInFrames={726} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="Pe9Ambiguous" component={Pe9Ambiguous}
          durationInFrames={698} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="Pe9Why" component={Pe9Why}
          durationInFrames={700} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="Pe9Limit" component={Pe9Limit}
          durationInFrames={628} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="Pe9Verdict" component={Pe9Verdict}
          durationInFrames={395} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="Pe9Outro" component={Pe9Outro}
          durationInFrames={145} fps={30} width={1920} height={1080}
          defaultProps={{}} />
      </Folder>
