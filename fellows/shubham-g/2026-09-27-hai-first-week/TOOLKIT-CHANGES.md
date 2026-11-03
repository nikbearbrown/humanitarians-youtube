# TOOLKIT-CHANGES — local patches to brutalist.art used for this build

Builds on the patches listed in `../2026-09-26-social-ai-brand-visibility/TOOLKIT-CHANGES.md`.

New file (copy in `scenes/`):
- `runtime/remotion/src/scenes/PartnerBridge.tsx` — `PartnerBridge` (1920×1080) and `PartnerBridge916` (1080×1920), registered in `Root.tsx`.

Backward-compatible prop additions (defaults leave earlier reels unchanged):
- SocialOneToMany `cols`; SocialLoop `signalsLabel`; HandleTitleOutro `scale` and `\n` line breaks (both aspects).
- ClaudeVerdictArtifact (16:9) `largeText`; ClaudeVerdictArtifact916 `textScale` (the chip moves above the card when set).
- The active SocialLoop stage is highlighted with a warm-grey border instead of ink.
