# Registering the TextToVoice scenes in Brutalist

`TtvScenes.tsx` goes in `brutalist.art/runtime/remotion/src/`. Add these two pieces to `runtime/remotion/src/Root.tsx`, then run `./art scene-index`.

Import:

```tsx
import {
  TtvTrickyLines, ttvTrickyLinesSchema, TtvPipeline, ttvPipelineSchema, TtvWave, ttvWaveSchema, TtvDemo, ttvDemoSchema,
  TtvTrickyLines916, TtvPipeline916, TtvWave916, TtvDemo916,
  TtvSpokenLines, ttvSpokenLinesSchema, TtvSpokenLines916,
} from './TtvScenes';
```

Compositions:

```tsx
      <Folder name="TextToVoice">
        <Composition id="TtvSpokenLines" component={TtvSpokenLines} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ttvSpokenLinesSchema} defaultProps={ttvSpokenLinesSchema.parse({lines: [[{w: 'A', at: 0.1}, {w: 'computer', at: 0.2}]]})} />
        <Composition id="TtvSpokenLines916" component={TtvSpokenLines916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ttvSpokenLinesSchema} defaultProps={ttvSpokenLinesSchema.parse({lines: [[{w: 'A', at: 0.1}, {w: 'computer', at: 0.2}]]})} />
        <Composition id="TtvTrickyLines" component={TtvTrickyLines} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ttvTrickyLinesSchema} defaultProps={ttvTrickyLinesSchema.parse({lines: [{parts: ['I ', 'read', ' it.'], hot: [1], note: 'red or reed?', at: 0.1}]})} />
        <Composition id="TtvTrickyLines916" component={TtvTrickyLines916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ttvTrickyLinesSchema} defaultProps={ttvTrickyLinesSchema.parse({lines: [{parts: ['I ', 'read', ' it.'], hot: [1], note: 'red or reed?', at: 0.1}]})} />
        <Composition id="TtvPipeline" component={TtvPipeline} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ttvPipelineSchema} defaultProps={ttvPipelineSchema.parse({steps: [{name: 'Clean up', detail: 'spell out', example: '$5 → five dollars'}], stepAt: [0.1]})} />
        <Composition id="TtvPipeline916" component={TtvPipeline916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ttvPipelineSchema} defaultProps={ttvPipelineSchema.parse({steps: [{name: 'Clean up', detail: 'spell out', example: '$5 → five dollars'}], stepAt: [0.1]})} />
        <Composition id="TtvWave" component={TtvWave} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ttvWaveSchema} defaultProps={ttvWaveSchema.parse({envelope: [0.1, 0.5, 0.3], otherEnvelope: [0.2, 0.4, 0.1], samples: [0.01, -0.02], sampleRate: 24000, styleSize: 256, bellaStyle: [0.1, -0.2], otherStyle: [0.3, 0.1]})} />
        <Composition id="TtvWave916" component={TtvWave916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ttvWaveSchema} defaultProps={ttvWaveSchema.parse({envelope: [0.1, 0.5, 0.3], otherEnvelope: [0.2, 0.4, 0.1], samples: [0.01, -0.02], sampleRate: 24000, styleSize: 256, bellaStyle: [0.1, -0.2], otherStyle: [0.3, 0.1]})} />
        <Composition id="TtvDemo" component={TtvDemo} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ttvDemoSchema} defaultProps={ttvDemoSchema.parse({rows: [{text: 'I read it.', hot: 'read', phonemes: 'aɪ ɹˈiːd ɪt.', bad: 'ɹˈiːd', said: 'said “reed”', at: 0.1}], bellaEnvelope: [0.1, 0.5], otherEnvelope: [0.2, 0.4], chip: 'same mistakes'})} />
        <Composition id="TtvDemo916" component={TtvDemo916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ttvDemoSchema} defaultProps={ttvDemoSchema.parse({rows: [{text: 'I read it.', hot: 'read', phonemes: 'aɪ ɹˈiːd ɪt.', bad: 'ɹˈiːd', said: 'said “reed”', at: 0.1}], bellaEnvelope: [0.1, 0.5], otherEnvelope: [0.2, 0.4], chip: 'same mistakes'})} />
      </Folder>
```
