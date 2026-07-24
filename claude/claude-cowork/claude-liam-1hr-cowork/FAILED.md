# FAILED — render failures after 2 attempts

## B08 — SlateCard

- **Pattern**: `SlateCard`
- **Reason**: `SlateCard` is not registered as a Remotion Composition in `Root.tsx`. The component exists at `runtime/remotion/src/scenes/SlateCard.tsx` but has no `<Composition>` entry.
- **Fallback**: compile.py will render B08 as a PIL-generated slate card (cream ground, dark ink, beat ID, narration excerpt). This is an acceptable fallback for a verdict beat.
- **Fix**: Add `SlateCard` to `Root.tsx` registrations if this pattern is needed in future reels.
