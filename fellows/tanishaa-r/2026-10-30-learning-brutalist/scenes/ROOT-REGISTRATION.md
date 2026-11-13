# Registering the LearningBrutalist scenes in Brutalist

`LbScenes.tsx` goes in `brutalist.art/runtime/remotion/src/`. Add these two pieces to `runtime/remotion/src/Root.tsx`, then run `./art scene-index`.

Import:

```tsx
import {
  LbPipeline, lbPipelineSchema, LbChecklist, lbChecklistSchema, LbToolCards, lbToolCardsSchema,
  LbGates, lbGatesSchema, LbTwoFrames, lbTwoFramesSchema, LbSyncFix, lbSyncFixSchema,
  LbPipeline916, LbChecklist916, LbToolCards916, LbGates916, LbTwoFrames916, LbSyncFix916,
  LbTakeaway916, lbTakeawaySchema,
} from './LbScenes';
```

Compositions:

```tsx
      <Folder name="LearningBrutalist">
        <Composition id="LbTakeaway916" component={LbTakeaway916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={lbTakeawaySchema} defaultProps={lbTakeawaySchema.parse({artifactHeading: 'Takeaway', artifactLines: ['one']})} />
        <Composition id="LbPipeline" component={LbPipeline} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={lbPipelineSchema} defaultProps={lbPipelineSchema.parse({steps: [{name: 'Beat sheet', sub: 'one entry per moment'}, {name: 'Audio', sub: 'the clock'}], stepAt: [0.1, 0.4]})} />
        <Composition id="LbChecklist" component={LbChecklist} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={lbChecklistSchema} defaultProps={lbChecklistSchema.parse({title: './setup', items: [{label: 'Python', logo: 'python', ok: true, at: 0.2}]})} />
        <Composition id="LbToolCards" component={LbToolCards} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={lbToolCardsSchema} defaultProps={lbToolCardsSchema.parse({cards: [{name: 'ffmpeg', role: 'joins the beats', logos: ['ffmpeg'], at: 0.2}]})} />
        <Composition id="LbGates" component={LbGates} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={lbGatesSchema} defaultProps={lbGatesSchema.parse({gates: [{name: 'GATE T', desc: 'type', result: 'PASS', at: 0.2}]})} />
        <Composition id="LbTwoFrames" component={LbTwoFrames} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={lbTwoFramesSchema} defaultProps={lbTwoFramesSchema.parse({landscape: 'learning-brutalist/rag-land-57.png', vertical: 'learning-brutalist/rag-vert-57.png', landTag: '3840×2160', vertTag: '2160×3840', callout: 'Not a crop.'})} />
        <Composition id="LbSyncFix" component={LbSyncFix} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={lbSyncFixSchema} defaultProps={lbSyncFixSchema.parse({frame: 'learning-brutalist/rag-land-118.png', badge: 'Checks: PASS', words: ['a', 'b', 'c'], caption: 'c'})} />
        <Composition id="LbPipeline916" component={LbPipeline916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={lbPipelineSchema} defaultProps={lbPipelineSchema.parse({steps: [{name: 'Beat sheet', sub: 'one entry per moment'}, {name: 'Audio', sub: 'the clock'}], stepAt: [0.1, 0.4]})} />
        <Composition id="LbChecklist916" component={LbChecklist916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={lbChecklistSchema} defaultProps={lbChecklistSchema.parse({title: './setup', items: [{label: 'Python', logo: 'python', ok: true, at: 0.2}]})} />
        <Composition id="LbToolCards916" component={LbToolCards916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={lbToolCardsSchema} defaultProps={lbToolCardsSchema.parse({cards: [{name: 'ffmpeg', role: 'joins the beats', logos: ['ffmpeg'], at: 0.2}]})} />
        <Composition id="LbGates916" component={LbGates916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={lbGatesSchema} defaultProps={lbGatesSchema.parse({gates: [{name: 'GATE T', desc: 'type', result: 'PASS', at: 0.2}]})} />
        <Composition id="LbTwoFrames916" component={LbTwoFrames916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={lbTwoFramesSchema} defaultProps={lbTwoFramesSchema.parse({landscape: 'learning-brutalist/rag-land-57.png', vertical: 'learning-brutalist/rag-vert-57.png', landTag: '3840×2160', vertTag: '2160×3840', callout: 'Not a crop.'})} />
        <Composition id="LbSyncFix916" component={LbSyncFix916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={lbSyncFixSchema} defaultProps={lbSyncFixSchema.parse({frame: 'learning-brutalist/rag-land-118.png', badge: 'Checks: PASS', words: ['a', 'b', 'c'], caption: 'c'})} />
      </Folder>
```
