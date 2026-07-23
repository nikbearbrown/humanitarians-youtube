# FACTCHECK — vox-how-to-vox (Gate F)

Every claim spoken, drawn, or carded in this film, verified against the
repository that the film describes. Sources are files in this repo at check
time (2026-07-06); scripts were grepped, not trusted from memory. This film's
subject is the pipeline itself, so the primary source for nearly every claim
is the doctrine file `aspects/explainer/vox-explainer/SKILL.md` ("SKILL.md"
below) and the scripts it names. Regenerate this file if any narration, viz
data, or card copy changes.

| beat | claim | verdict | source / derivation | fix |
|---|---|---|---|---|
| B01 | "Every film in this style is assembled the same way: mixed sources, one treatment, one flat plane." | ✓ (editorial framing) | SKILL.md "What Vox actually is" — the laundering function; "sources never match; the treatment does." "Every film" is the doctrine's own claim about the style. | — |
| B01 | "This film teaches that way — by building itself." | ✓ | True by construction: all DOCUMENT beats show this reel's files; B15/B21 are self-harvested frames (SHOTLIST harvest table). | — |
| B02 | "The tool is called Unreal Reels." | ✓ | README.md title; repo `github.com/nikbearbrown/unreal-reels`. | — |
| B03 | "It's a laundering function… each passes through one treatment and lands on one plane." | ✓ | SKILL.md, verbatim doctrine. | — |
| B03–B04 | Treatment numbers: desaturate ~80%, contrast 1.15, real newspaper scan ground | ✓ | SKILL.md "one treatment (desaturate ~80%, contrast 1.15, seated on a real newsprint scan)"; ground is a Chronicling America scan per design tokens. Narration says "about eighty percent" — hedged correctly. | — |
| B05 | "Two accent colors, serif labels with hairline underlines, one editor's pen per graphic. Decoration that isn't information gets deleted." | ✓ | SKILL.md restraint rules: two accents max; serif labels carry 1.5px hairline underlines; "One editor's-pen voice per graphic"; "delete anything decorative rather than informational." | — |
| B06 | "Underneath every film sits one file: a beat sheet." | ✓ | SKILL.md slot contract: `beat_sheet.json` — "single source of truth"; README: "The spine is beat_sheet.json." | — |
| B06 | "The highlighted entry is the beat you are watching right now." | ✓ (self-referential; production-dependent) | Holds iff the B06 grab shows the B06 entry — enforced by SHOTLIST harvest spec (grab after audio lock, B06 entry centered). Verify at Gate B. | verify on grab |
| B07 | "Audio is the master clock. The narration is generated first, then measured." | ✓ | SKILL.md "The clock"; `scripts/generate_audio.py` writes measured `actual_duration_s` (mutagen). "Never estimate from word count." | — |
| B08 | "Every beat declares its form — still, footage, document, graphic, card — and its source: archive, AI, or your own." | minor (defended) | SKILL.md two-axis table has SIX types — COMPOSITE omitted from narration for rhythm. Defended: COMPOSITE = treated plate + annotation plane (compiles like STILL); B08's graphic carries a footnote chip saying exactly that (beat_sheet viz.note). Sources verbatim: `archive \| ai \| own`. | footnote chip required in B08 scene |
| B08 | "Form locks early. Source swaps late." | ✓ | SKILL.md: type "locked at the plan gate, never changes when media swaps"; source "late-bound, swappable." | — |
| B09 | "Drop a better file in and rebuild — only that slot recompiles." | ✓ | SKILL.md slot contract: "Rebuild recompiles ONLY slots whose input hash changed"; `scripts/vox_compile.py` uses sha1 input hashing (grepped, lines 23/59). | — |
| B10 (card) | "SEVEN PHASES, FIVE GATES" | ✓ (fixed at this check) | SKILL.md Workflow: 7 numbered phases (plan, factcheck, audio, run, stills, video, assemble); explicit GATEs at plan / claims-hold / hear-it / watch-the-cut / ship = **5**. Card originally said FOUR — corrected in beat_sheet.json + script.md. | FIXED |
| B11 | "Beats of twenty-eight words or fewer." | ✓ | SKILL.md workflow step 1: "beats (≤~28 words)". This sheet complies: max 28 (checked programmatically at plan lint). | — |
| B12 | "The machine refuses to build a frame without this file." | minor (defended) | `scripts/vox_run.sh` lines 54–60: Gate F hard-fails when FACTCHECK.md is missing. Escape hatch `VOX_FACTS=0` exists but is labeled "previz only" — narration's absolute phrasing is the intended contract, hatch documented here. | — |
| B13 | "A script measures each duration to the millisecond." | ✓ | mutagen durations stored at ms-scale precision (e.g. film five B03 `7.548`). | — |
| B14 | "One command, free, local… audits the scenes, renders the graphics to the measured durations, and compiles a watchable cut." | ✓ | `scripts/vox_run.sh`: Gate A static check → Manim renders → Gate B → slot → outro → review compile; SKILL.md: "one command, free/local… ALWAYS a full watchable video." | — |
| B15 | "Slots you haven't filled render as slates… the first cut is always watchable." | ✓ | SKILL.md compile precedence: media > manim > png > **slate**; "pass 1 is always watchable." The on-screen slate is B15's own, from this reel's pass-1 cut. | verify frame is B15's slate |
| B16 | "A ready-to-run prompt for every generated image, archive links for every real one." | ✓ | SKILL.md typed shot list spec. This reel's SHOTLIST has a prompt for its 1 ai slot (B18); zero archive slots exist (nothing depicts a real person/event), so "every real one" is vacuously true here and true in general doctrine. | — |
| B17 | "A pantry… one command strips audio, crops documents, renames everything into its slot." | ✓ | `scripts/vox_pantry.py` (grepped): sound stripped from video (line ~95), DOCUMENT 16:9 crops (~109–110), renames to `media/<BID>.*`, sidecar stubs written (~15). | — |
| B17 | "Restored and beat-prefixed." | ✓ | SKILL.md pantry law: restoration pass (WARMONO/NATGEO per `aspects/stock-styles.md`), beat-id prefix required. | — |
| B18 | "Real people and real events require real archives, with a credit sidecar. A generated stand-in wears an ink X." | ✓ | SKILL.md provenance: sidecar required on archive slots; "Real people/events → real archives"; STAND-IN X until replaced. B18's portrait is deliberately generic + disclosed — the X is worn honestly. | — |
| B19 | "Rings, labels, and highlights live on a separate plane, keyed to word timestamps… the media below is never touched." | ✓ doctrine; ⚠ production route | SKILL.md: annotation "never baked into clips/"; word clock = `mp3/words.json` via `scripts/vox_align.py` (built, working). CAVEAT: the Remotion plane is NOT YET BUILT (REMOTION.md; HANDOFF). Route for the "now" ring: time it scene-side inside B19's Manim scene from words.json offsets (scenes render to measured durations, so word-precise timing is available at render). The doctrine claim stays true; the demo must be verified against the word clock before ship. | ring timing verified vs words.json at Gate B |
| B20 | "The vertical Short is a derivative, never a re-edit. Landscape composes side by side; portrait stacks top and bottom. Nothing renders twice." | ✓ | SKILL.md Shorts law, near-verbatim ("16:9 lays out SIDE BY SIDE; 9:16 stacks TOP AND BOTTOM"); `vox_short.py` symlinks slots — "nothing re-renders." | — |
| B21 | "Cuts before the last wear a burn-in — timecode, beat number, slot status… clean master is the same build, unmarked." | ✓ | SKILL.md: review burn-in = "global TC + beat id + beat-local clock + slot status… clean master = same assembly, no flag." | — |
| B22 | "The engine is free and local." | ✓ | docs/open-source-vs-paid.md: "The engine is open source and runs locally for free." All compile/render/assembly steps local. | — |
| B22 | "This film bought a narration and one still. Everything else was free." | ✓ (reconciled, rev. 2026-07-06) | Independent count from beat_sheet.json after the interface decision: ai-source slots = **B18 only** → 1 still; TTS = 26 beats, one voice → 1 narration (B22's own beat regenerated `--only B22` after this rewrite — a paid regen of one beat, still "a narration"). own-source slots (21) are Cowork/terminal captures, editor scans, Bear's photo, self-harvested frames = $0. Isotype in B22's scene: 1 crimson + 1 terracotta — matches. RE-CHECK if any slot's source changes. | recheck if plan changes |
| B23 | "Every document in this film is its own." | ✓ | By construction; the collage shows this reel's beat_sheet.json, SHOTLIST.md, FACTCHECK.md (this file — which therefore appears in the film it checks). | grab after docs final |
| B24 | "It's open source; the engine runs free on your machine." | ✓ | LICENSE: MIT © 2026 Nik Bear Brown; engine free per open-source-vs-paid.md. | — |
| B24 | "The tutorial that planned this film ships inside." | ✓ (pending commit) | `docs/TUTORIAL.md` exists in the working tree (written 2026-07-06, this session) — **must be committed before publish** or the claim is false for cloners. | commit docs/TUTORIAL.md before publish |
| B25 | "Yours is simpler: one story, a dozen beats, one afternoon." | editorial (precedented) | Labeled editorial. Precedent: films four and five each went chapter → published in one day (HANDOFF.md, 2026-07-05); a 12-beat film is materially smaller than this 26-beat one. | — |
| B26 | "Next: … turning music into a beat-synced video." | ✓ (intent) | Songbird aspect exists (`aspects/songbird/`); the next-film promise is a programming decision, Bear's to keep. | — |
| B07 viz | Duration bars drawn from THIS sheet's measured values | ✓ (deferred data) | Data does not exist until audio lock; scene renders LAST among graphics (SHOTLIST). Numbers are whatever generate_audio.py wrote — self-verifying. | render B07 scene after audio |
| B08 viz | Histogram: STILL 3 · FOOTAGE 5 · DOCUMENT 4 · GRAPHIC 7 · CARD 4 · COMPOSITE 3 | ✓ (rev. 2026-07-06) | Recomputed from beat_sheet.json after the interface decision (B25 STILL→FOOTAGE). The scene reads the sheet at import, so the drawn matrix self-updates; the swap demo shows B01's mark sliding ai→own — B01's actual history in this revision. No 3-in-a-row (B13/B14 FOOTAGE pair, then B15 STILL). | recheck if plan changes |

## Simplifications, defended

1. **B08 omits COMPOSITE from the spoken type list** (rhythm). Defended via the
   footnote chip in the B08 graphic: "COMPOSITE = STILL + the annotation plane."
2. **B12 states Gate F absolutely**; the `VOX_FACTS=0` previz escape exists but
   never produces a shippable render — the absolute phrasing is the contract.
3. **B13 "cloned voice"** — ElevenLabs voice `TyW6NH39JcFb5M3xdIIk` (Bear's
   clone). Accurate for this film; a viewer using stock TTS still fits "a voice
   model" — acceptable.

## Errata this pass

- **B10 card said "FOUR GATES"; the workflow has FIVE.** Fixed in
  beat_sheet.json and script.md before audio (this check's catch).

## Revision 2026-07-06 — the interface decision

All conversation moments became Cowork captures of the conversation that
made the film; machine moments are live terminal recordings; B04 is Bear's
own photograph; B18 remains the only generated image (the STAND-IN X needs
an object). Consequences applied: B22 narration rewritten (four stills →
one still) + audio regenerated `--only B22`; B22 isotype counts updated;
B08 histogram recomputed; B01/B25 shot blocks rewritten; SHOTLIST rebuilt
around the ten-step shoot plan. This revision is itself evidence for B09's
claim: only the changed slots recompile.

## Standing obligations before ship

- Commit `docs/TUTORIAL.md` (B24 claim).
- Regenerate B22 audio (`--only B22`) and re-run `vox_align.py` so the word
  clock matches the new mp3 — BEFORE the first vox_run.
- B04: Bear's photo pending upload; sidecar "own work."
- Cowork captures: light mode, cropped to the window, no personal content
  in frame (tabs, email subjects, sidebar recents).
- Verify B06/B15/B21/B23 self-referential frames show what the narration says
  they show (Gate B eyeball).
- Verify B19 ring lands on "now" against `mp3/words.json`.
- Re-run this factcheck if any narration, viz count, or slot source changes.
