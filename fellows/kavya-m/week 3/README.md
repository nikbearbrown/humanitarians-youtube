# Week 3

**Group:** Brutalist team · **Reporting week:** 2026-09-28 through 2026-10-04

Two videos were produced this week, each in its own folder with its own beat sheet and full evidence trail.

| Folder | Video | Runtime | Beats |
|---|---|---|---:|
| [kavya-opentelemetry-ai-agents/](kavya-opentelemetry-ai-agents/README.md) | OpenTelemetry for AI Agents | 2:18 | 9 |
| [kavya-brutalist-week3-progress/](kavya-brutalist-week3-progress/README.md) | Brutalist Progress, Week 3 | 1:59 | 8 |

The explainer contrasts a plain log with a trace for the same failed agent run. The log only says the
run finished with a warning. The trace's spans point at the search step that returned zero hits. The
demo uses a small stdlib tracer shaped like OpenTelemetry's span model, not the SDK. The progress
reel reports a third week on the pipeline with zero new bugs, and the caveat that it reused only
already-proven components.

Both are Remotion-only builds against brutalist.art at `b21f625`, voice Kokoro `am_onyx`, with the
AI-voice disclosure spoken in B00. Renders are not committed; see each folder's README for its export
details and Drive link.
