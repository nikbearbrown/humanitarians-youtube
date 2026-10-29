# Ontologies for Observability at Scale — Kavya Mehta

Built following the house `ai-explainer` paperwork (see CHECKS-REPORT.md,
FACTCHECK.md, SOURCES.md, SHOTLIST.md, PROMPTS.md, STATUS.md, BUILD-LOG.md)
and the required-content rules in
[docs/FELLOWS-SUBMISSION.md](../../docs/FELLOWS-SUBMISSION.md) — README
section below follows that guide's own template.

## This week's contribution

**Question:** at scale, three teams can name the same service three
different ways — does a bigger model fix that, or is it a modeling
problem?

**Prediction:** modeling problem — no model size fixes a naming collision
that was never resolved to begin with.

**What I built/tried:** an explainer on observability ontologies (entity
types, relationships, stable identifiers, shared vocabulary), illustrated
with a worked example: a payment service named three different ways by
three teams, and what an agent's dependency query sees with and without a
canonical entity resolving them.

**Observed result:** without an ontology, an agent asking "what depends on
payments?" sees only one of three real variants. With one, every variant
maps to a single canonical entity and the agent sees the full graph. Honest
boundary: an ontology can't reason about a span that was never emitted — it
fixes meaning, not missing instrumentation.

**Next experiment:** apply the same canonical-entity exercise to a real
service naming collision in one of my own projects (CabStream's own
Terraform-defined resources would be a natural next target).

## Human and AI work

**My decisions, implementation and verification:** I directed the topic
(adapting an existing house explainer into my own submission-compliant
version), reviewed the narration script, and visually checked the rendered
frames before accepting the build as done.

**AI tools/voices used and what they generated:** Claude (this session)
adapted the beat sheet and narration from an earlier house-branded version
built the same session; Kokoro `am_onyx` (free, local TTS) generated the
narration audio; Remotion rendered every visual from authored props — no
stock footage, no generative image/video models.

**What I rejected or corrected:** the source reel
(`claude-liam-ontologies-observability-scale`) carried `@NikBearBrown`
branding, the "Liam, in for Bear" framing, and no required intro line —
all replaced for this submission. Separately, and more significantly: this
reel's first compile used the tool's default 720p output; caught via a
resolution check prompted by an unrelated discovery (see BUILD-LOG.md) and
recompiled correctly before delivery.

**What remains unverified or failed:** none outstanding for this reel.

## Reproduce

**Brutalist version/commit and date checked:** `b21f6253a336098f3f55847a9525ae6868ccbdb7`, 2026-10-10 (repo HEAD at build time, checked 2026-10-29).

**Source commit used for this export:** same as above.

**Beat sheet and custom scene files:** [`beat_sheet-16x9-landscape.json`](beat_sheet-16x9-landscape.json), [`beat_sheet-9x16-vertical.json`](beat_sheet-9x16-vertical.json). No custom scene files.

**Commands/dependencies:**
```
python3 runtime/scripts/generate_audio_kokoro.py youtube/kavya-ontologies-observability-scale
python3 runtime/scripts/remotion_scenes.py youtube/kavya-ontologies-observability-scale
python3 runtime/scripts/compile.py youtube/kavya-ontologies-observability-scale --review --no-timecode --force --height 2160
./art vertical youtube/kavya-ontologies-observability-scale
python3 runtime/scripts/remotion_scenes.py youtube/kavya-ontologies-observability-scale/vertical
python3 runtime/scripts/compile.py youtube/kavya-ontologies-observability-scale/vertical --review --no-timecode --force --height 3840
```
**Note the explicit `--height 2160` / `--height 3840`** — `compile.py`
defaults to 720p; this is the fix for the bug documented in BUILD-LOG.md.
Requires ffmpeg and Node/npx on `PATH`.

**Approvals and checks:** no human sign-off records exist yet. GATE T
report: [TYPECHECK.md](TYPECHECK.md) — PASS, 8/8. GATE V: spot-checked
manually — see CHECKS-REPORT.md.

## Watch and review

- Landscape — **3840×2160 (verified via `ffprobe`)** — 2:00.17 — SHA-256 `f2d8ac1ed54a1840bce761282b2f3d4057e02dc8eb27b28ca204d06cfe0771f0` — **not yet uploaded to Drive** (local at `kavya-ontologies-observability-scale-slate.mp4`)
- Vertical — **2160×3840 (verified via `ffprobe`)** — 2:00.17 — SHA-256 `d02ce18efc0b9c01f1d76def1894ccd09c312a1a1bbd000e9a3c35fc858415c2` — **not yet uploaded to Drive** (local at `vertical/kavya-ontologies-observability-scale-vertical-slate.mp4`)
- Sources/large assets Drive link: n/a
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending — not applicable (personal project, not a Humanitarians AI fellow submission)
