# Registering the HowQrCodesWork scenes in Brutalist

`QrScenes.tsx` goes in `brutalist.art/runtime/remotion/src/`. Add these two pieces to `runtime/remotion/src/Root.tsx`, then run `./art scene-index`.

Import:

```tsx
import {
  QrHook, qrHookSchema, QrHook916, QrGrid, qrGridSchema, QrGrid916, QrFinders, qrFindersSchema, QrFinders916, QrReadPath, qrReadPathSchema, QrReadPath916, QrRecovery, qrRecoverySchema, QrRecovery916, QrDemo, qrDemoSchema, QrDemo916, QrLogo, qrLogoSchema, QrLogo916,
} from './QrScenes';
```

Compositions:

```tsx
      <Folder name="HowQrCodesWork">
        <Composition id="QrHook" component={QrHook} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={qrHookSchema} defaultProps={qrHookSchema.parse({matrix: ['1'], cover: 0, points: [], coverAt: 0.2, readAt: 0.5})} />
        <Composition id="QrHook916" component={QrHook916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={qrHookSchema} defaultProps={qrHookSchema.parse({matrix: ['1'], cover: 0, points: [], coverAt: 0.2, readAt: 0.5})} />
        <Composition id="QrGrid" component={QrGrid} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={qrGridSchema} defaultProps={qrGridSchema.parse({matrix: ['1'], sizeLabel: '1 × 1', gridAt: 0.1, bitAt: 0.2, darkAt: 0.3, lightAt: 0.4, historyAt: 0.6, nameAt: 0.8, history: '', name: ''})} />
        <Composition id="QrGrid916" component={QrGrid916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={qrGridSchema} defaultProps={qrGridSchema.parse({matrix: ['1'], sizeLabel: '1 × 1', gridAt: 0.1, bitAt: 0.2, darkAt: 0.3, lightAt: 0.4, historyAt: 0.6, nameAt: 0.8, history: '', name: ''})} />
        <Composition id="QrFinders" component={QrFinders} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={qrFindersSchema} defaultProps={qrFindersSchema.parse({matrix: ['1'], findAt: 0.1, findersAt: 0.3, angleAt: 0.5, timingAt: 0.7})} />
        <Composition id="QrFinders916" component={QrFinders916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={qrFindersSchema} defaultProps={qrFindersSchema.parse({matrix: ['1'], findAt: 0.1, findersAt: 0.3, angleAt: 0.5, timingAt: 0.7})} />
        <Composition id="QrReadPath" component={QrReadPath} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={qrReadPathSchema} defaultProps={qrReadPathSchema.parse({matrix: ['1'], text: 'h', startAt: 0.1, byteAt: 0.4, spellAt: 0.5, maskAt: 0.7})} />
        <Composition id="QrReadPath916" component={QrReadPath916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={qrReadPathSchema} defaultProps={qrReadPathSchema.parse({matrix: ['1'], text: 'h', startAt: 0.1, byteAt: 0.4, spellAt: 0.5, maskAt: 0.7})} />
        <Composition id="QrRecovery" component={QrRecovery} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={qrRecoverySchema} defaultProps={qrRecoverySchema.parse({low: {version: 3, data: 55, recovery: 15}, high: {version: 5, data: 46, recovery: 88}, levels: [], msgAt: 0.1, recAt: 0.2, rsAt: 0.3, levelsAt: 0.5, lowAt: 0.7, highAt: 0.9})} />
        <Composition id="QrRecovery916" component={QrRecovery916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={qrRecoverySchema} defaultProps={qrRecoverySchema.parse({low: {version: 3, data: 55, recovery: 15}, high: {version: 5, data: 46, recovery: 88}, levels: [], msgAt: 0.1, recAt: 0.2, rsAt: 0.3, levelsAt: 0.5, lowAt: 0.7, highAt: 0.9})} />
        <Composition id="QrDemo" component={QrDemo} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={qrDemoSchema} defaultProps={qrDemoSchema.parse({low: ['1'], high: ['1'], lowFail: 7, lowOk: 6, highOk: 17, highPct: 21, setupAt: 0.1, growAt: 0.3, lowAt: 0.6, highAt: 0.8})} />
        <Composition id="QrDemo916" component={QrDemo916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={qrDemoSchema} defaultProps={qrDemoSchema.parse({low: ['1'], high: ['1'], lowFail: 7, lowOk: 6, highOk: 17, highPct: 21, setupAt: 0.1, growAt: 0.3, lowAt: 0.6, highAt: 0.8})} />
        <Composition id="QrLogo" component={QrLogo} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={qrLogoSchema} defaultProps={qrLogoSchema.parse({matrix: ['1'], small: ['1'], logoModules: 1, logoAt: 0.1, damageAt: 0.3, fillAt: 0.5, costAt: 0.7})} />
        <Composition id="QrLogo916" component={QrLogo916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={qrLogoSchema} defaultProps={qrLogoSchema.parse({matrix: ['1'], small: ['1'], logoModules: 1, logoAt: 0.1, damageAt: 0.3, fillAt: 0.5, costAt: 0.7})} />
      </Folder>
```

## GATE T exemption (runtime/scripts/type_check.py)

The portrait QR scenes draw a real module grid whose squares read as sub-floor "text runs". Add to `HAND_DRAWN_PATTERNS` (§8.1 only; every other check still runs):

```python
    "QrHook916", "QrReadPath916", "QrLogo916",
```
