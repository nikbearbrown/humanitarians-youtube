# SOURCES — hai-brutalist-week-1

A progress report, so the sources are this week's own build output. Every number spoken is
a line that appeared in a terminal or a value read off a file. Claim-level verdicts are in
[FACTCHECK.md](FACTCHECK.md).

## The week's output — probed, not estimated

Four finished masters, each verified on disk with `ffprobe`:

| File | Dimensions | Duration |
|---|---|---|
| `hai-mcp-explained.mp4` | 3840x2160 | 160.79s (2:41) |
| `hai-mcp-explained-vertical.mp4` | 2160x3840 | 160.79s |
| `hai-agents-on-their-own.mp4` | 3840x2160 | 134.04s (2:14) |
| `hai-agents-on-their-own-vertical.mp4` | 2160x3840 | 134.04s |

Shown in B04. Re-probe before publishing if any is rebuilt.

## The finding — four lines of real failure

The week's main claim is a mistake, and each step of it is an actual output:

1. **The gate was skipping in silence.** `./art final` printed
   `[typecheck] missing dep: No module named 'scipy'` followed by `GATE T skipped —
   missing deps`, then exited zero. The typography gate had never run on this machine.
2. **Installing the library was not enough.** `type_check.py` then raised
   `TypeError: unsupported operand type(s) for |` on the annotation `float | None`. The
   default `python3` here is 3.9.6; that syntax needs 3.10 or newer.
3. **When it finally ran, it failed.** The first real GATE T run against
   `hai-agents-on-their-own/vertical` reported `GATE T: FAIL (8 pixel beats)` — B01 through
   B07 and B09 of B00-B09.
4. **By how much.** The gate measured a smallest text run of 38px against a 72px floor
   (1.9% of 3840). That is 0.53x — roughly half the size it needed to be at phone scale.

Shown in B05 and B06. These are first-party failures, not illustrations.

## Toolkit documentation

B02's description of what brutalist.art does is taken from the toolkit's own docs:
`RENDER-TARGETS.md` §1 (beat sheet to 4K master) and `CLAUDE.md` rule 6 (free by default).
Kokoro ran locally this session and reported $0.00. Marked SPEC-ASSERTED.

B03's four working terms — beat sheet, lane, gate, master — are drawn from the same docs and
from observed behaviour. They are working definitions, not quoted standards.

## Attributed position

B06's closing line, that no probe replaces opening the frame and looking at it, is advice
rather than a measurement. It is also the toolkit's own rule 4: *verify renders by LOOKING
at frames, never by the mp4 probe alone.*

## Narration

Kokoro `am_onyx`, generated locally at $0.00. Disclosed aloud in B00. The work, the commits
and the four films are the fellow's own.
