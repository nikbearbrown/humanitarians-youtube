# FRICTIONAL — agents-use-tools

> Draft prepared with Claude Code from the session record. Review, edit in your own words, then commit.

## 2026-10-02
**Tried / expected:** set up the Brutalist toolkit on Windows and build a ~90s explainer on agent tool use.
**Where it resisted:** the toolkit had not been run on Windows. Seven issues surfaced — `npx` not resolving from Python, an ffmpeg font-path escaping bug, two text-encoding crashes, a setup guard that always fails, a smoke-test slug the validator rejects, and a venv created without pip. Two blocked rendering entirely.
**What Claude contributed:** diagnosed and fixed the two blocking bugs (with my approval), wrote the beat sheet and three new scene components (+ portrait variants), ran the QC gates.
**Accepted / changed / rejected:** I cut the planned ~3 min to ~1:49; I approved each toolkit change individually; I rejected the review-cut timecode and beat labels in the final.
**Understood / open:** the quality gates caught real problems (a WCAG contrast failure, wrong channel kicker, a drifting number). Several QC loops were slow because causes were guessed before being measured. The toolkit fixes are local and not yet upstream.
