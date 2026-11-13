# Registering the MidjourneySeeds scenes in Brutalist

`MjScenes.tsx` goes in `brutalist.art/runtime/remotion/src/`. Add these two pieces to `runtime/remotion/src/Root.tsx`, then run `./art scene-index`.

Import:

```tsx
import {
  MjPuzzle, mjPuzzleSchema, MjPuzzle916, MjNoise, mjNoiseSchema, MjNoise916, MjSteps, mjStepsSchema, MjSteps916, MjFour, mjFourSchema, MjFour916, MjSeed, mjSeedSchema, MjSeed916, MjDemo, mjDemoSchema, MjDemo916, MjInMidjourney, mjInMjSchema, MjInMidjourney916, MjYourTurn, mjYourTurnSchema, MjYourTurn916,
} from './MjScenes';
```

Compositions:

```tsx
      <Folder name="MidjourneySeeds">
        <Composition id="MjYourTurn" component={MjYourTurn} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={mjYourTurnSchema} defaultProps={mjYourTurnSchema.parse({prompt: 'a', steps: [], askAt: 0.1, runAt: 0.7, runText: ''})} />
        <Composition id="MjYourTurn916" component={MjYourTurn916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={mjYourTurnSchema} defaultProps={mjYourTurnSchema.parse({prompt: 'a', steps: [], askAt: 0.1, runAt: 0.7, runText: ''})} />
        <Composition id="MjPuzzle" component={MjPuzzle} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={mjPuzzleSchema} defaultProps={mjPuzzleSchema.parse({prompt: 'a', images: [], more: [], promptAt: 0.1, imagesAt: 0.2, againAt: 0.5, moreAt: 0.6, label: '', labelAt: 0.3, questionAt: 0.8})} />
        <Composition id="MjPuzzle916" component={MjPuzzle916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={mjPuzzleSchema} defaultProps={mjPuzzleSchema.parse({prompt: 'a', images: [], more: [], promptAt: 0.1, imagesAt: 0.2, againAt: 0.5, moreAt: 0.6, label: '', labelAt: 0.3, questionAt: 0.8})} />
        <Composition id="MjNoise" component={MjNoise} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={mjNoiseSchema} defaultProps={mjNoiseSchema.parse({noise: 'midjourney-seeds/noise_42.png', picture: 'midjourney-seeds/four_0.png', noiseAt: 0.1, label: '', labelAt: 0.1, quote: '', quoteAt: 0.4, cleanAt: 0.6})} />
        <Composition id="MjNoise916" component={MjNoise916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={mjNoiseSchema} defaultProps={mjNoiseSchema.parse({noise: 'midjourney-seeds/noise_42.png', picture: 'midjourney-seeds/four_0.png', noiseAt: 0.1, label: '', labelAt: 0.1, quote: '', quoteAt: 0.4, cleanAt: 0.6})} />
        <Composition id="MjSteps" component={MjSteps} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={mjStepsSchema} defaultProps={mjStepsSchema.parse({noise: 'midjourney-seeds/noise_42.png', picture: 'midjourney-seeds/four_0.png', prompt: 'a', promptAt: 0.1, noiseAt: 0.3, shapesAt: 0.5, diffAt: 0.7, caption: ''})} />
        <Composition id="MjSteps916" component={MjSteps916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={mjStepsSchema} defaultProps={mjStepsSchema.parse({noise: 'midjourney-seeds/noise_42.png', picture: 'midjourney-seeds/four_0.png', prompt: 'a', promptAt: 0.1, noiseAt: 0.3, shapesAt: 0.5, diffAt: 0.7, caption: ''})} />
        <Composition id="MjFour" component={MjFour} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={mjFourSchema} defaultProps={mjFourSchema.parse({noises: [], images: [], fourAt: 0.1, eachAt: 0.3, randomAt: 0.6, label: '', randomLabel: ''})} />
        <Composition id="MjFour916" component={MjFour916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={mjFourSchema} defaultProps={mjFourSchema.parse({noises: [], images: [], fourAt: 0.1, eachAt: 0.3, randomAt: 0.6, label: '', randomLabel: ''})} />
        <Composition id="MjSeed" component={MjSeed} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={mjSeedSchema} defaultProps={mjSeedSchema.parse({seed: 1234, prompt: 'a', noise: 'midjourney-seeds/noise_42.png', range: '', seedAt: 0.1, rangeAt: 0.3, flagAt: 0.5, lockAt: 0.8})} />
        <Composition id="MjSeed916" component={MjSeed916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={mjSeedSchema} defaultProps={mjSeedSchema.parse({seed: 1234, prompt: 'a', noise: 'midjourney-seeds/noise_42.png', range: '', seedAt: 0.1, rangeAt: 0.3, flagAt: 0.5, lockAt: 0.8})} />
        <Composition id="MjDemo" component={MjDemo} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={mjDemoSchema} defaultProps={mjDemoSchema.parse({four: [], a: 'midjourney-seeds/seed1234_a.png', b: 'midjourney-seeds/seed1234_b.png', forest: 'midjourney-seeds/seed1234_forest.png', prompt: 'a', prompt2: 'b', toyAt: 0.05, fourAt: 0.2, sameAt: 0.4, matchAt: 0.55, wordAt: 0.7, stayAt: 0.85, identical: true, toyLabel: 'toy'})} />
        <Composition id="MjDemo916" component={MjDemo916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={mjDemoSchema} defaultProps={mjDemoSchema.parse({four: [], a: 'midjourney-seeds/seed1234_a.png', b: 'midjourney-seeds/seed1234_b.png', forest: 'midjourney-seeds/seed1234_forest.png', prompt: 'a', prompt2: 'b', toyAt: 0.05, fourAt: 0.2, sameAt: 0.4, matchAt: 0.55, wordAt: 0.7, stayAt: 0.85, identical: true, toyLabel: 'toy'})} />
        <Composition id="MjInMidjourney" component={MjInMidjourney} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={mjInMjSchema} defaultProps={mjInMjSchema.parse({same: '', pct: '', find: 'a → b', sameAt: 0.1, pctAt: 0.4, findAt: 0.6})} />
        <Composition id="MjInMidjourney916" component={MjInMidjourney916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={mjInMjSchema} defaultProps={mjInMjSchema.parse({same: '', pct: '', find: 'a → b', sameAt: 0.1, pctAt: 0.4, findAt: 0.6})} />
      </Folder>
```

## Assets and GATE T settings

- Copy `assets/*.png` (output of `demo/seed_demo.py`) to `runtime/remotion/public/midjourney-seeds/`, and `icons/logos/midjourney/midjourney-01.svg` and `icons/logos/claude/claude-01.svg` to `runtime/remotion/public/logos/<name>/`.
- `runtime/scripts/type_check.py`: add `"MjNoise", "MjNoise916", "MjSteps", "MjSteps916", "MjFour", "MjFour916", "MjSeed", "MjSeed916"` to `HAND_DRAWN_PATTERNS` (TV-static specks read as sub-floor text; §8.1 only) and `"MjNoise", "MjNoise916", "MjSeed916"` to `BBOX_OVERLAP_EXEMPT_PATTERNS` (noise specks read as overlapping runs).
- The beat sheets declare `qc.contrast_regions` for B01–B06, so contrast is measured on the real text, not the toy pictures.
