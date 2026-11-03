# BUILD-LOG — claude-for-legal--claude-liam-matter-update

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-matter-update/beat_sheet.json`
— a 7-beat Teardown skill-teardown reel (`matter-update` Anthropic Skill:
append a dated event to a matter's history file and refresh the log row).
No SCRIPT.md existed on the source; its `beats[*].narration_text` served as
the locked narration per the redo contract. The source's `source_skill`
path (`/Users/bear/.../claude-for-legal/litigation-legal/skills/matter-update/SKILL.md`)
does not exist on this machine — same missing-path situation already logged
on the `hiring-review`/`case-brief`/`form-generation`/`build-guide` siblings.
Treated the facts already captured in the source's narration as ground
truth (per redo contract, facts are carried over, not re-derived from a
source file this machine doesn't have) and never touched the source reel's
folder.

**Facts kept unchanged:** the skill's name (matter-update); its one
instruction (append a dated event to a matter's history file, refresh the
log row); the five triggers (new development, status change, risk
re-assessment, deadline shift, settlement-authority change); linear
read-then-act execution (Claude reads SKILL.md, then follows the steps in
order, no branching unless a step says so). The source's Teardown "what it
gets right (repeatable results) / what it bites (anything outside the
spec)" framing was replaced with a neutral both-directions split (B10/B11)
— what happens when a request matches the file exactly, and what happens
when it doesn't — no verdict on the design.

**Beat-count adjustment (logged per SCRIPT.md):** source is 7 beats (B00
cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF
handoff, BOUT outro) with no dedicated wrong-guess or anchor beat.
hai-simple's inherited laws (WRONG-GUESS, ANCHOR, BOTH-DIRECTIONS,
CARRY-OUT) are mandatory regardless of source shape, so the body expanded
to 11 beats (B01–B11): a stakes beat, a planted anchor (Case 4471 — a
settlement offer arrives), the wrong guess and its falsifying case (a
fresh, untouched matter runs identically), the mechanism split into its
four component facts, the anchor payoff, and both directions — introducing
no fact beyond what the source's narration already asserted. Same scale as
the `hiring-review` sibling redo (11 body beats).

**B00 WRITER LAW:** naive framing — a newcomer assumes Claude remembers how
their firm handles a case update, the way a person would after a few uses;
corrected on screen: "remember" → "know" (the real mechanism: Claude reads
a written file, it doesn't recall anything). Typed text: "How does Claude /
remember how our / firm logs a case / update?" Reused the tuned
BrutalistHesitantWriter performance parameters from the `books--building-
plugins` sibling (charMs 46, hesitateBetween 12, mistakeRate 5) since the
text length was comparable. Measured 10.1s (≥8s TIMING LAW floor); verified
by frame pull at t=9.5s that the corrected final question ("How does Claude
know how our firm logs a case update?") is fully typed and legible well
before the beat ends.

**Body beats:** all 11 rebuilt as Manim GRAPHIC scenes via one shared
generic "chip row" renderer in `scenes.py` (title + up to 5 labeled chips,
optional connecting arrows, optional accent/strike, caption) — the same
proven renderer as the `books--claude-liam-building-plugins` sibling,
copied verbatim and re-parametrized. Anchor pair: B02 plants "CASE 4471" /
"SETTLEMENT OFFER" (two chips, arrow between); B09 returns the identical
two-chip composition, both now accented — "logged, not remembered."

**GATE T — three fix passes, all logged:**
1. First pass (before compile — `build.status` unstamped for GRAPHIC beats,
   same order-of-operations issue as the `hiring-review` sibling): B07
   (bbox-overlap, false positive) and B09 (contrast). B09 was real: both
   anchor-payoff chips were accented (cream-on-terracotta), making 100% of
   the frame's visible text share the low-contrast pairing — same defect
   class as the `books--building-plugins` sibling's B14/B18. **Fixed at the
   root:** dropped to a single accented chip (`accent=[1]`), restoring a
   mixed frame. Also renamed the B07 "RISK RE-ASSESSMENT" chip label to
   "RISK REASSESSMENT" (no hyphen) as a precaution, though the hyphen
   turned out not to be the actual cause of B07's flag.
2. Second pass (after first compile, `build.status` now stamped): B07's
   bbox-overlap re-surfaced at the identical coordinates. Verified by frame
   pull at t=3s — all five chip labels sit cleanly inside their own boxes,
   no text-on-text overlap. Confirmed the same documented false-positive
   class as the `deposition-prep`/`hiring-review` siblings (INK border ring
   registers as its own text-run blob, whose bbox encloses its own interior
   label). Added `BLB07Scene` to `type_check.py`'s
   `BBOX_OVERLAP_EXEMPT_PATTERNS` with the verification recorded inline.
3. Third pass: B04 and B11 — the only two beats using `strike=` chips —
   failed kerning §8.4 ("max inter-glyph gap 53px > threshold 18px").
   Diagnosed by calling `check_kerning_sanity`'s own row-scan logic
   directly against the raw 1080p manim frames: the peak-ink row it locked
   onto was the TITLE text (not the chip row), because MUTE (`#5D584F`,
   mean brightness ≈87) sits *above* the checker's `<80` ink-detection
   threshold — struck-chip text wasn't counted as ink at all, so in beats
   where every chip was struck (B11) or struck+accented (B04, whose
   accented chip's cream text also isn't ink-colored), the chip row had too
   little detected ink and the row-scan fell back to a sparse serif-tip row
   in the bold title, misreading it as a huge kerning gap. **Fixed at the
   root:** darkened MUTE to `#46423B` (mean ≈65, safely under the
   threshold) so struck text is reliably detected as ink and the row-scan
   locks onto the correct, well-spaced chip row. Also found and fixed a
   second, independent, real defect while inspecting B10's frame: the chip
   label "SAME RESULT, EVERY TIME" (23 chars) crossed the renderer's
   `len<=22` font-size bucket into the smaller bold font, where Pango
   rendered it with visibly uneven, gappy inter-glyph spacing — a genuine
   legibility defect, not a false positive. **Fixed at the root:**
   shortened to "SAME RESULT, EVERY RUN" (22 chars), which renders cleanly.

**GATE T final pass: PASS, 0 FAILs.**

Compiled with `compile.py --force` (recompiled twice, after each fix
batch): 15/15 beats real (no slate), master born natively 4K (3840×2160,
compile.py's 4K LAW), 130.4s. `content-check`/`frame-check`/`lane-check`
all PASS. Non-blocking warning: motion histogram `graphic:11 remotion:4`
(73%, over the ~40% pantry cap) — logged as structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF + BOUT all
REMOTION by skill contract, against 11 Manim body beats for a 15-beat reel;
same disposition as the `books--claude-liam-building-plugins` sibling.

**Gate V:** pulled 16 frames at 8s spacing across the full 130.4s runtime,
plus targeted frame pulls at B00's correction window, B07/B09/B10/B11 after
each fix, and the BOUT tail. Read every one directly. B00's correction
("remember"→"know") lands well inside the beat with margin. The B02→B09
anchor pair reads as the same object returning (identical two-chip
composition, both accented at payoff). BCRY/BHTF/BOUT are centered,
legible, safe-inset; BHTF correctly shows `@HumanitariansAI` (not the
`ClaudeComposerAsk` Root.tsx default `@NikBearBrown`, via the explicit
`folderLabel` override). No remaining blockers.

**Audio:** ffprobe confirms an AAC mono stream present, master mtime
(1788127217) newer than beat_sheet.json's (1788126003);
`ffmpeg -af volumedetect`: mean_volume **-23.9 dB**, max -2.9 dB —
comfortably above the -40 dB floor.

Metadata file written: `claude-for-legal--claude-liam-matter-update.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Playlist note:
`SUBJECT.json`'s `family` is `"claude-for-legal"`, which has no literal
prefix match in `skills/make/hai-simple/loop/playlists.json`'s map (no
`claude-for-legal*` key exists); fell through to matching `SUBJECT.json`'s
`skill` field, `"hai-simple"`, which IS a literal key in the map →
**"Claude Basics"**. Per the DELIVERY CONTRACT format, the description also
carries the direct code link.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
