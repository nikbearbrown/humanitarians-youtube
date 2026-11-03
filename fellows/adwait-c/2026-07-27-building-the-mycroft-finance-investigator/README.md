# Weekly Research Report: Building the Mycroft Finance Investigator

**Fellow:** Adwait Changan
**Week ending:** July 27, 2026
**Voice:** Kokoro `am_onyx` — "Onyx, in for Humanitarians AI" · **Channel:** @HumanitariansAI
**Builder:** `deep-explainer` (brutalist.art) · **Register:** Pragmatist · **Aspect:** 16:9

From financial data to an evidence-backed agent. Over three weeks, Adwait built the Mycroft
Finance Investigator: (1) a synthetic SaaS dataset with schema, provenance, and validation;
(2) a deterministic engine that computes revenue, expense, payroll, and EBITDA variances,
applies materiality rules, reconciles control totals, and traces every calculation to its
source records; (3) a local investigation agent that conditionally selects finance tools,
retains evidence, records an execution trace, and writes separate machine- and
human-readable reports.

**The one idea:** the agent explains the *mathematical performance bridge* and leaves
*business causation and final approval* to a human finance reviewer. Where it stops is the
design.

The beat sheet has **13 beats (~3.4 min)**, all Remotion patterns that exist in the
pared-down toolkit, so the first compile renders real visuals with **zero slates** — no
Manim required.

## Production state

- Plan approval: **pending**
- Fact-check gate (`FACTCHECK.md`): **pending** — verify the reported metrics
- Narration approval (`PEDAGOGY.md`): **pending**
- Audio lock: **not started**
- Slate previz: **not rendered**
- Publishing: **not authorized**

## Build loop (from the toolkit root, Python 3.12 venv active)

```bash
source /Users/adwaitchangan/Study/Brutalist/brutalist.art/.venv/bin/activate
REEL="/Users/adwaitchangan/Study/Brutalist/humanitarians-youtube/fellows/adwait-changan/2026-07-27-building-the-mycroft-finance-investigator"

# 1. after the fellow signs Gate P (PEDAGOGY.md) and the fact-check:
python3 /Users/adwaitchangan/Study/Brutalist/brutalist.art/runtime/scripts/generate_audio_kokoro.py "$REEL"

# 2. compile the review cut, see what's left, then the clean master:
cd /Users/adwaitchangan/Study/Brutalist/brutalist.art
./art run  "$REEL"
./art todo "$REEL"
./art final "$REEL"
```

## Files

- `beat_sheet.json` — the narrative + visual plan (source of truth)
- `PEDAGOGY.md` — Gate P narration review + human sign-off
- `FACTCHECK.md` — claim-level evidence; resolve every `[VERIFY]` before audio
- `SOURCES.md` — the Mycroft project + reported results
- `BUILD-PROMPT.md` / `BUILD-LOG.md` — reproducible build instructions + decisions
- `media/`, `mp3/`, `clips/`, `manim/` — derived build artifacts (gitignored media)

**Git note:** `*.mp4` / `*.mp3` are gitignored — commit the beat sheet + paperwork, never the
rendered video. Anyone rebuilds it for free with brutalist.art.
