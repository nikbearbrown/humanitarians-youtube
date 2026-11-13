# Registering the HowGpsWorks scenes in Brutalist

`GpsScenes.tsx` goes in `brutalist.art/runtime/remotion/src/`. Add these two pieces to `runtime/remotion/src/Root.tsx`, then run `./art scene-index`.

Import:

```tsx
import {
  GpsKeyPoints, gpsKeyPointsSchema, GpsKeyPoints916, GpsSky, gpsSkySchema, GpsSky916, GpsTimeDistance, gpsTimeDistanceSchema, GpsTimeDistance916, GpsCircles, gpsCirclesSchema, GpsCircles916, GpsClockError, gpsClockErrorSchema, GpsClockError916, GpsDemo, gpsDemoSchema, GpsDemo916, GpsRelativity, gpsRelativitySchema, GpsRelativity916,
  GpsTakeaway, gpsTakeawaySchema,
} from './GpsScenes';
```

Compositions:

```tsx
      <Folder name="HowGpsWorks">
        <Composition id="GpsTakeaway" component={GpsTakeaway} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={gpsTakeawaySchema} defaultProps={gpsTakeawaySchema.parse({artifactHeading: 'Three things to keep', artifactLines: ['one'], lineAt: [0.2]})} />
        <Composition id="GpsKeyPoints" component={GpsKeyPoints} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={gpsKeyPointsSchema} defaultProps={gpsKeyPointsSchema.parse({points: [{text: 'only listens', at: 0.2}]})} />
        <Composition id="GpsKeyPoints916" component={GpsKeyPoints916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={gpsKeyPointsSchema} defaultProps={gpsKeyPointsSchema.parse({points: [{text: 'only listens', at: 0.2}]})} />
        <Composition id="GpsSky" component={GpsSky} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={gpsSkySchema} defaultProps={gpsSkySchema.parse({altitudeLabel: '~20,000 km up'})} />
        <Composition id="GpsSky916" component={GpsSky916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={gpsSkySchema} defaultProps={gpsSkySchema.parse({altitudeLabel: '~20,000 km up'})} />
        <Composition id="GpsTimeDistance" component={GpsTimeDistance} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={gpsTimeDistanceSchema} defaultProps={gpsTimeDistanceSchema.parse({where: 'here', when: 'now', travelS: 0.0706, rangeKm: 21162, broadcastAt: 0.1, clockAt: 0.2, arriveAt: 0.4, mathAt: 0.6, resultAt: 0.8})} />
        <Composition id="GpsTimeDistance916" component={GpsTimeDistance916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={gpsTimeDistanceSchema} defaultProps={gpsTimeDistanceSchema.parse({where: 'here', when: 'now', travelS: 0.0706, rangeKm: 21162, broadcastAt: 0.1, clockAt: 0.2, arriveAt: 0.4, mathAt: 0.6, resultAt: 0.8})} />
        <Composition id="GpsCircles" component={GpsCircles} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={gpsCirclesSchema} defaultProps={gpsCirclesSchema.parse({c1At: 0.1, c2At: 0.3, c3At: 0.5, captionAt: 0.7, meetAt: 0.8, caption: 'Flattened'})} />
        <Composition id="GpsCircles916" component={GpsCircles916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={gpsCirclesSchema} defaultProps={gpsCirclesSchema.parse({c1At: 0.1, c2At: 0.3, c3At: 0.5, captionAt: 0.7, meetAt: 0.8, caption: 'Flattened'})} />
        <Composition id="GpsClockError" component={GpsClockError} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={gpsClockErrorSchema} defaultProps={gpsClockErrorSchema.parse({errorLabel: 'off', meters: 300, clockAt: 0.1, swellAt: 0.3, fourthAt: 0.6, whereAt: 0.8, whenAt: 0.9})} />
        <Composition id="GpsClockError916" component={GpsClockError916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={gpsClockErrorSchema} defaultProps={gpsClockErrorSchema.parse({errorLabel: 'off', meters: 300, clockAt: 0.1, swellAt: 0.3, fourthAt: 0.6, whereAt: 0.8, whenAt: 0.9})} />
        <Composition id="GpsDemo" component={GpsDemo} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={gpsDemoSchema} defaultProps={gpsDemoSchema.parse({place: 'Boston Common', ranges: [21162], travelMs: [70.59], clockUs: 1, ignoreM: 390.2, solvedUs: 1, setupAt: 0.1, ignoreAt: 0.4, solveAt: 0.7, foundAt: 0.8})} />
        <Composition id="GpsDemo916" component={GpsDemo916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={gpsDemoSchema} defaultProps={gpsDemoSchema.parse({place: 'Boston Common', ranges: [21162], travelMs: [70.59], clockUs: 1, ignoreM: 390.2, solvedUs: 1, setupAt: 0.1, ignoreAt: 0.4, solveAt: 0.7, foundAt: 0.8})} />
        <Composition id="GpsRelativity" component={GpsRelativity} durationInFrames={450} fps={30} width={1920} height={1080}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={gpsRelativitySchema} defaultProps={gpsRelativitySchema.parse({net: 38, gravity: 45, speed: 7, driftKm: 11, clocksAt: 0.1, whyAt: 0.3, driftAt: 0.6, fixAt: 0.8})} />
        <Composition id="GpsRelativity916" component={GpsRelativity916} durationInFrames={450} fps={30} width={1080} height={1920}
          calculateMetadata={({props}) => ({durationInFrames: Math.ceil(((props as any).durationSeconds ?? 15) * 30)})}
          schema={gpsRelativitySchema} defaultProps={gpsRelativitySchema.parse({net: 38, gravity: 45, speed: 7, driftKm: 11, clocksAt: 0.1, whyAt: 0.3, driftAt: 0.6, fixAt: 0.8})} />
      </Folder>
```
