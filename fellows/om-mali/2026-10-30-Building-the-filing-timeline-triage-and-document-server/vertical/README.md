# vertical/ — the 9:16 cut

`building-the-filing-timeline-triage-and-document-server-916.mp4` · **2160×3840**, 24fps,
205.45s — the same length as the 16:9 master, to the frame.

## It is a re-layout, never a crop

Every scene in `BuildingTheTriage.tsx` lays itself out natively at both sizes through one
helper:

```tsx
const { f } = useStage();     // f(landscape, portrait)
width: f(1180, 834)
```

Each component is registered twice in `Root.tsx` — once at 1920×1080 and once at 1080×1920
under its `<pattern>916` name — so there is one component and two registrations, not two
components. Nothing is cropped, letterboxed or scaled down from the landscape frame; rows
that sit side by side in 16:9 stack in 9:16, and the figures are re-measured for the
narrower safe area.

## The audio is the same audio

`make_vertical.py` derives `vertical/beat_sheet.json` from the landscape one and **copies the
twelve mp3s across**. Narration is never regenerated for this cut, so no number, no word and
no duration can differ between the two masters.

It matches the registration tuple shape in `Root.tsx`, not a naming convention — do not
"simplify" that regex back to a `W<digits>` pattern, which has silently missed a whole series
twice before.

## Portrait is tuned, not inherited

Two beats were re-laid-out after reading portrait frames; both are written up in
`../BUILD-LOG.md` §7. The one that was a genuine blocker:

> **B04** clipped every figure to its first two digits — `593` drew as `59` — because the
> track reserved width for a label column that portrait stacks *above* the track, while the
> value column still sat beside it.

Budget for this pass. Portrait has needed one every week since week 5.

## Gates

```
GATE V (explicit --mp4):  frames=24  BLOCKER=0  MAJOR=0
```

Check `_qc/REPORT.md` and `_qc/contact_sheet.png` here, not the landscape ones — GATE V can
pass 16:9 and fail 9:16 on the very same scene.
