# Visual Plan — "Repo Sensei, Week Three"

progress report · 16:9 and 9:16 · palette `claude` (PAPER `#FAF9F5`, INK `#3D3929`,
SOFT `#73705F`, TERRACOTTA `#D97757`) · serif display, mono for code.

## Lane-mix decision

**13 of 20 beats (65%) are Manim**, drawn in `scenes.py`. Zero VOX.

The earlier reels in this series were Remotion-only, which caps every beat at a typographic
card: an eyebrow, a heading, bullet lines. That is adequate for stating a claim and useless
for explaining a mechanism. This episode's subject *is* a mechanism — a parse tree, a four
stage pipeline, a trace running down through three layers, a citation pointing at a file.
Those are drawings, not bullet points, so they are drawn.

Remotion is kept only where a card is genuinely the right object: the opening composer, the
four-term definition table, the real tree-sitter query shown as code, and the outro.

## The three acts

- **I — The problem** (B01-B04). A hundred thousand lines, one question, and an answer with
  nothing underneath it. Ends on the pull quote.
- **II — How it works** (B05-B11). The pipeline, the parser, the queries, the trace, the
  citation. This is the explanatory spine and it is entirely drawn.
- **III — Nine days in** (B12-B19). Measured numbers counting up, the monorepo map, a real
  query, and an honest status bar showing what does *not* work yet.

Each act opens with a two-second numeral card so the viewer can feel the structure.

## Figures

| Scene | What it draws |
|---|---|
| `B02_BigRepo` | 112 file cells; one terracotta question mark lands on them |
| `B03_ConfidentGuess` | A fluent answer card, an arrow, an empty dashed box labelled `source?` |
| `B06_Pipeline` | CLONE / PARSE / INDEX / ANSWER, arrows between, each lighting in turn |
| `B07_TreeSitter` | Source on the left, a syntax tree growing node by node on the right |
| `B08_Queries` | Five query chips over three language tags |
| `B09_Trace` | UI / API / DATABASE stacked, a terracotta spine lighting each |
| `B10_Citation` | An answer snapping by arrow to a `defs.scm:14` chip |
| `B13_Counters` | Four measured numbers counting up from zero |
| `B14_Monorepo` | The four parts of the repo, wired |
| `B16_Honest` | Two progress bars: indexing works, answering does not yet |

## Honesty constraint

No product screenshot appears anywhere. The project is nine days old and the answering path
is unfinished; `B16_Honest` says so on screen. A mocked-up result would be the exact failure
this series argues against.
