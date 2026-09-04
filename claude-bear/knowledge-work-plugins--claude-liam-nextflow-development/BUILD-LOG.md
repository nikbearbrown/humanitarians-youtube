# BUILD-LOG — knowledge-work-plugins--claude-liam-nextflow-development

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-nextflow-development/beat_sheet.json`
(Teardown register, batch skill-teardown format — never built: every source
beat was `SLATE`, no `mp3/`, no `media/`, no `SCRIPT.md`). Question, facts,
and beat count (7: B00, B01, B02, B03, BVDT, BHTF, BOUT) carried over from the
source. Facts: the nextflow-development Anthropic skill is a folder Claude
reads before acting (SKILL.md instruction set, LICENSE.txt, references/,
scripts/); its Steps section runs linearly; its job is running nf-core
pipelines (rnaseq, sarek, atacseq) on sequencing data (local FASTQs or
public GEO/SRA datasets); reliable inside that spec, nothing outside it.

**What changed from source:**
- B00 replaced the source's `ClaudeComposerAsk` "reading SKILL.md…" run card
  with `BrutalistHesitantWriter` (WRITER LAW): writer types "Claude was
  trained\nto run Nextflow.\nHow?", hesitates on "trained", corrects to
  "told" — the naive assumption (Claude was *trained* on bioinformatics)
  falsified by the real mechanism (Claude was *told*, via a file it reads).
- Register Teardown → Plain: B03 rewritten from the source's verdict
  pronouncement ("Here is the Teardown moment... What it gets right... What
  it bites...") into a factual both-directions statement ("reliable inside
  the spec, nothing outside it") — same facts, no ranking, no design
  judgment. BVDT's implicit "Verdict" framing renamed "In short," same
  recap facts.
- Close re-skinned: `ClaudeTitleOutro`/@NikBearBrown → `OutroCTA`/
  @HumanitariansAI, Liam sign-off ("Claude didn't learn bioinformatics. It
  read a file. Liam, in for Bear.").
- Body beats B01–B03 reuse the source's `SkillTeardownAnatomy` /
  `SkillTeardownPipeline` / `SkillTeardownMechanism` REMOTION components
  unchanged in visual grammar — already valid REMOTION (never AI-video,
  pantry, or human-drop), so NO-GENAI/NO-PANTRY LAW required no
  substitution beyond B00. Content re-registered to Plain; `folderLabel`
  set to `@HumanitariansAI` on B00/BHTF.
- Your Turn prompt (BHTF) cleaned from the source's run-on sentence into one
  paste-ready Claude prompt, same request preserved (walk through the plan
  before running anything).

Full redo audit and register audit in SCRIPT.md.

**Bug found and fixed during build (GATE T / Gate V):**
1. GATE T (`type_check.py`) failed on B03: the `SkillTeardownMechanism`
   `body` prop was 20 words, over the §8.5 12-word on-screen pull-quote
   limit ("Run nf-core pipelines — rnaseq, sarek, atacseq — on sequencing
   data: local FASTQs or public datasets from GEO or SRA."). Shortened to a
   9-word label: "rnaseq · sarek · atacseq — sequencing data, local or
   GEO/SRA." Re-ran type_check.py: GATE T PASS.
2. Gate V frame pull on the first compile found B00's writer animation
   never finished: the original 4-line text ("Claude was trained to run /
   Nextflow pipelines. / Wait — how does that / actually work?", ~80 chars)
   didn't complete typing within the 11.3s beat window — at t=11s the
   writer was still mid-third-line ("Wait|"), so the beat cut to B01 before
   ever showing the real question. Shortened the on-screen text to "Claude
   was trained\nto run Nextflow.\nHow?" (~40 chars, matching the char
   budget of the working `four-places-data-goes` precedent). Re-rendered
   B00 alone (`remotion_scenes.py --only B00 --force`), confirmed by
   ffprobe/frame-pull: "trained" visibly typed in accent color at t=3s,
   corrected to "told" by t=5s, full text complete ("Claude was told to run
   Nextflow. How?") and held from t≈9.5s through the end of the beat.
   Recompiled the full cut afterward — never left a stale master pointing
   at the broken B00.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T (type_check.py): PASS, 0 FAILs after the B03 word-count fix
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840x2160, audio present, duration 84.2s; mp4 mtime
  (1788525574) newer than beat_sheet.json mtime (1788525494)
- Gate V: pulled 14 frames at 6s spacing plus targeted B00 frames at
  1/1.5/2/2.5/3/3.5/4/5/7/8.5/9.5/10.5/11s; read cold-open correction,
  anatomy file tree, pipeline diagram, mechanism card, carry-out artifact
  (paginated 1/2), Your Turn composer, outro. All legible, humanitarians
  palette (cream ground, terracotta asterisk accent, serif ink) on B00/
  BOUT, Claude-fidelity palette on body B01-B03/BVDT/BHTF (expected — see
  SCRIPT.md "Known mixed-skin note," those components have no ink/accent/bg
  override). No text overlap, no off-canvas text, safe inset respected. No
  blockers found after the B00 fix.

**Non-blocking note (motion histogram):** `remotion:7` — 100% REMOTION,
0% Manim/GRAPHIC. Structural, matching the source's original component
choices exactly (redo-mode preserves body argument and beat structure); the
source itself never used Manim for this beat sheet. Not reworked, per the
honesty rule, rather than inflating beat count to hit a pantry-mix ratio
that redo-mode doesn't authorize changing.

Metadata file written:
`knowledge-work-plugins--claude-liam-nextflow-development.md` (channel
@HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`
via the `knowledge-work-plugins` family prefix — plus the direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-04 — Phase 4 delivery

Master is already 3840x2160 (compile.py's 4K LAW forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects.
