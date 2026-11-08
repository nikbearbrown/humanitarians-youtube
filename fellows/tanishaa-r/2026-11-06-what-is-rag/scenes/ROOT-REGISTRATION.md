# Registering the RAG scenes in Brutalist

`RagScenes.tsx` goes in `brutalist.art/runtime/remotion/src/`. Add these two pieces to `runtime/remotion/src/Root.tsx`, then run `./art scene-index`.

Import (next to the other reel-local imports):

```tsx
// ── what-is-rag (Humanitarians AI fellow explainer) — reel-local components ──
import {
  RagTwoAnswers, ragTwoAnswersSchema, RagPipeline, ragPipelineSchema,
  RagEmbeddingMap, ragEmbeddingMapSchema, RagRetrievalDemo, ragRetrievalDemoSchema,
  RagWhenToUse, ragWhenToUseSchema, HaiTitleOutro, haiTitleOutroSchema,
  RagTwoAnswers916, RagPipeline916, RagEmbeddingMap916, RagRetrievalDemo916, RagWhenToUse916, HaiTitleOutro916,
} from './RagScenes';
```

Compositions (inside the root `<>…</>`, beside the other `<Folder>`s):

```tsx
      <Folder name="Rag">
        <Composition id="RagTwoAnswers" component={RagTwoAnswers} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ragTwoAnswersSchema} defaultProps={ragTwoAnswersSchema.parse({question: 'Can I submit Lab 3 late?', leftAnswer: 'Yes, late work is always accepted.'})} />
        <Composition id="RagPipeline" component={RagPipeline} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ragPipelineSchema} defaultProps={ragPipelineSchema.parse({stages: [{name: 'Retrieve', detail: 'find matching passages'}, {name: 'Augment', detail: 'add them to the prompt'}, {name: 'Generate', detail: 'answer from that text'}], stageAt: [0.1, 0.4, 0.7]})} />
        <Composition id="RagEmbeddingMap" component={RagEmbeddingMap} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ragEmbeddingMapSchema} defaultProps={ragEmbeddingMapSchema.parse({chunks: [{label: 'late labs', x: 0.3, y: 0.4}, {label: 'extensions', x: 0.4, y: 0.6}, {label: 'grading', x: 0.7, y: 0.3}], question: {label: 'late?', x: 0.35, y: 0.5}, nearest: ['late labs', 'extensions'], highlight: 'extensions'})} />
        <Composition id="RagRetrievalDemo" component={RagRetrievalDemo} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ragRetrievalDemoSchema} defaultProps={ragRetrievalDemoSchema.parse({question: 'q', method: 'TF-IDF', results: [{section: 's', text: 't', score: 0.4}], answer: 'a', citation: 'c'})} />
        <Composition id="RagWhenToUse" component={RagWhenToUse} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ragWhenToUseSchema} defaultProps={ragWhenToUseSchema.parse({useHeader: 'Use it when', useItems: [{text: 'a', at: 0.1}], skipHeader: 'Skip it when', skipItems: [{text: 'b', at: 0.5}], warning: 'w', warningAt: 0.8})} />
        <Composition id="HaiTitleOutro" component={HaiTitleOutro} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={haiTitleOutroSchema} defaultProps={haiTitleOutroSchema.parse({title: 'What Is RAG?'})} />
        <Composition id="RagTwoAnswers916" component={RagTwoAnswers916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ragTwoAnswersSchema} defaultProps={ragTwoAnswersSchema.parse({question: 'Can I submit Lab 3 late?', leftAnswer: 'Yes, late work is always accepted.'})} />
        <Composition id="RagPipeline916" component={RagPipeline916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ragPipelineSchema} defaultProps={ragPipelineSchema.parse({stages: [{name: 'Retrieve', detail: 'find matching passages'}, {name: 'Augment', detail: 'add them to the prompt'}, {name: 'Generate', detail: 'answer from that text'}], stageAt: [0.1, 0.4, 0.7]})} />
        <Composition id="RagEmbeddingMap916" component={RagEmbeddingMap916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ragEmbeddingMapSchema} defaultProps={ragEmbeddingMapSchema.parse({chunks: [{label: 'late labs', x: 0.3, y: 0.4}, {label: 'extensions', x: 0.4, y: 0.6}, {label: 'grading', x: 0.7, y: 0.3}], question: {label: 'late?', x: 0.35, y: 0.5}, nearest: ['late labs', 'extensions'], highlight: 'extensions'})} />
        <Composition id="RagRetrievalDemo916" component={RagRetrievalDemo916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ragRetrievalDemoSchema} defaultProps={ragRetrievalDemoSchema.parse({question: 'q', method: 'TF-IDF', results: [{section: 's', text: 't', score: 0.4}], answer: 'a', citation: 'c'})} />
        <Composition id="RagWhenToUse916" component={RagWhenToUse916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={ragWhenToUseSchema} defaultProps={ragWhenToUseSchema.parse({useHeader: 'Use it when', useItems: [{text: 'a', at: 0.1}], skipHeader: 'Skip it when', skipItems: [{text: 'b', at: 0.5}], warning: 'w', warningAt: 0.8})} />
        <Composition id="HaiTitleOutro916" component={HaiTitleOutro916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={haiTitleOutroSchema} defaultProps={haiTitleOutroSchema.parse({title: 'What Is RAG?'})} />
      </Folder>
```

The logo the scenes use is `logos/humanitarians/humanitarians-logo-1.svg` from the toolkit, copied to `runtime/remotion/public/logos/humanitarians/`.
