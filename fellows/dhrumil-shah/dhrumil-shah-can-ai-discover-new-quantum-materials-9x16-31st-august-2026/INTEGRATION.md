# Remotion integration contract — 9:16

`scripts/sync-to-remotion.ps1` copies the composition to
`runtime/remotion/src/quantum-materials/` and stages the 16 reused narration
beats into `runtime/remotion/public-quantum-materials/quantum-materials/audio/`,
then verifies the registry before allowing a render.

The workspace `runtime/remotion/src/Root.tsx` already contains the
registration below. If this folder is copied into a fresh compatible
brutalist.art workspace, add it before running the sync script.

```tsx
import {
  CanAIDiscoverQuantumMaterials9x16,
  QM_9X16_TOTAL_FRAMES,
} from './quantum-materials/CanAIDiscoverQuantumMaterials9x16';
```

```tsx
<Folder name="Quantum-Materials">
  <Composition
    id="CanAIDiscoverQuantumMaterials"
    component={CanAIDiscoverQuantumMaterials}
    durationInFrames={QM_TOTAL_FRAMES}
    fps={24}
    width={3840}
    height={2160}
  />
  <Composition
    id="CanAIDiscoverQuantumMaterials9x16"
    component={CanAIDiscoverQuantumMaterials9x16}
    durationInFrames={QM_9X16_TOTAL_FRAMES}
    fps={24}
    width={2160}
    height={3840}
  />
</Folder>
```

Both cuts live in the same `Quantum-Materials` folder and share the
`public-quantum-materials` public directory, which is why the audio only needs
staging once.

The sync script throws if `CanAIDiscoverQuantumMaterials9x16` is absent from
`Root.tsx`, so a clean clone cannot silently render the 16:9 composition into
a file named 9:16.

## Development preview

After syncing, from `runtime/remotion`:

```powershell
npm run studio
```

Choose **Quantum-Materials / CanAIDiscoverQuantumMaterials9x16**.

## Known non-blocking warning

`@remotion/paths` is on 4.0.490 while the rest of the workspace is on 4.0.486,
so the CLI prints a version-mismatch banner on every invocation. It does not
affect this composition and renders complete normally. Shared with the 16:9
cut and the sibling Mycroft films.
