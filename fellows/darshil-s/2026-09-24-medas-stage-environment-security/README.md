# Securing the Stage Environment

**Skill:** house darshil-s pattern (`ClaudeComposerAsk` / `GitHubCodeViewer` / `ClaudeVerdictArtifact` / `ClaudeTitleOutro`) · **Voice:** am_onyx (Darshil) · **Duration:** ~1:57 (8 beats) · **Status:** rendered (4K master produced)
**Destination:** `darshil-s/2026-09-24-medas-stage-environment-security`

## About this video — read the provenance note first

**Unlike every other reel in this book, this one is not built from a
fellow-supplied scope.**  The
five hardening changes shown (GitHub Environment protection rules, IAM
invoker restriction, Artifact Registry vulnerability-scan confirmation,
Cloud Run ingress restriction, and a log-based error-rate alert) are this
toolkit's own plausible synthesis, built on the real resource names from
`medas-stage-environment-provisioning`

The one piece that **is** fellow-supplied verbatim is the closing line
(B06's spoken narration): *"With staging now fully configured and
validated, the team has a reliable, production-like environment to test
every release — giving confidence before anything moves forward to
production."*

Week 3's project update (one of the two distinct videos required per week —
see `learning/` in this same folder for the companion **STEM/AI topic**
video, which explains the general security principles behind the five
invented changes).


```

## Rebuilding this video

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
python3 runtime/scripts/generate_audio_kokoro.py ../BrutalistVideo/darshil-s/2026-09-24-medas-stage-environment-security
python3 runtime/scripts/remotion_scenes.py       ../BrutalistVideo/darshil-s/2026-09-24-medas-stage-environment-security
./art final ../BrutalistVideo/darshil-s/2026-09-24-medas-stage-environment-security
```

Rendered locally at 3840x2160 (4K), free — Kokoro TTS + Remotion, no paid
services. Note: on this machine, `./art final`'s own QC-gate subprocess step
hit the same unresolved environment-specific failure as every other reel in
this book (not a content defect); the shipped master was produced by running
the identical encode command by hand (faster x264 preset) and verifying it
against the same QC checker and a manual frame review. Remotion renders used
`ART_RENDER_CONCURRENCY=4` (see `remotion_scenes.py`; defaults to 1).
