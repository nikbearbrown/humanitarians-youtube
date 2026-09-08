# Remotion integration contract

`scripts/sync-to-remotion.ps1` copies the composition to
`runtime/remotion/src/quantum-materials/` and the sixteen narration beats to
`runtime/remotion/public-quantum-materials/quantum-materials/audio/`, then
verifies the registry before allowing a render.

The workspace `runtime/remotion/src/Root.tsx` already contains the registration
below. If this folder is copied into a fresh compatible brutalist.art
workspace, add it before running the sync script.

```tsx
import {
  CanAIDiscoverQuantumMaterials,
  QM_TOTAL_FRAMES,
} from './quantum-materials/CanAIDiscoverQuantumMaterials';
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
</Folder>
```

The sync script throws if `CanAIDiscoverQuantumMaterials` is absent from
`Root.tsx`, so a clean clone cannot silently render the wrong composition.

## Development preview

After syncing, from `runtime/remotion`:

```powershell
npm run studio
```

Choose the **Quantum-Materials / CanAIDiscoverQuantumMaterials** composition.

## Known non-blocking warning

The workspace Remotion packages sit on 4.0.486 except `@remotion/paths`, which
is on 4.0.490. The CLI prints a version-mismatch banner on every invocation.
It does not affect this composition — `@remotion/paths` is not imported here —
and the render completes normally. Aligning the versions is workspace
housekeeping, not a change to this film.

The sibling Mycroft film records the same warning in its own compliance notes.
