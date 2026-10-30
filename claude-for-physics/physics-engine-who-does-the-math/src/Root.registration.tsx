import {Pe1Promise, Pe1Split, Pe1NotGame, Pe1Pipeline, Pe1Routes, Pe1Proof, Pe1Honest, Pe1Verdict, Pe1Outro} from './scenes/PhysicsEngine01';

      {/* ── who-does-the-math (PhysicsEngine01) — reel-local compositions ── */}
      <Folder name="PhysicsEngine01">
        <Composition id="Pe1Promise" component={Pe1Promise}
          durationInFrames={705} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="Pe1Split" component={Pe1Split}
          durationInFrames={813} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="Pe1NotGame" component={Pe1NotGame}
          durationInFrames={781} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="Pe1Pipeline" component={Pe1Pipeline}
          durationInFrames={893} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="Pe1Routes" component={Pe1Routes}
          durationInFrames={858} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="Pe1Proof" component={Pe1Proof}
          durationInFrames={821} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="Pe1Honest" component={Pe1Honest}
          durationInFrames={790} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="Pe1Verdict" component={Pe1Verdict}
          durationInFrames={668} fps={30} width={1920} height={1080}
          defaultProps={{}} />
        <Composition id="Pe1Outro" component={Pe1Outro}
          durationInFrames={215} fps={30} width={1920} height={1080}
          defaultProps={{}} />
      </Folder>
