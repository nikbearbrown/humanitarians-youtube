# BUILD-LOG — "How Apps Find a Song's Tempo"

What broke, what it cost, and what changed because of it. Built 2026-10-17 for the week of 12–16 Oct.

## 1 — Toolkit update first

`git fetch` brought 9 upstream commits (598 files: Remotion 4.0.535 and React 19, a Godot trailer
skill, new scenes, Gate W, type-gate and pronunciation work, and two new rules in CLAUDE.md: the
REMOTION VERSION LAW and the LOGO LAW). The merge conflicted in `type_check.py` (two independent
exemption lists, both kept), `package.json` / `package-lock.json` (upstream's versions taken), and the
generated `scenes.json` / `SCENE-DOC-TODO.md` (rebuilt with `./art scene-index`). Two local packages
that local scenes still import (`@remotion/google-fonts`, pinned to 4.0.535, and `remotion-bits`)
were kept; the first probe still failed to bundle because `remotion-bits` needs `culori`, which the
merge had dropped, so it was reinstalled (`--save-exact`). `tsc` shows only upstream errors.

## 2 — The first detector was measuring the wrong thing

`tempo.py` follows Ellis 2007 / librosa: an onset curve, its autocorrelation, a preference near 120
BPM, a dynamic-programming beat tracker. The first run looked wrong in three ways, each diagnosed
before anything was scripted:
- **Funk and drum and bass failed at strange ratios.** The bands were log-spaced, which gave the
  bass a third of the bands, so the kick and bass line dominated the onset curve. Switched to mel
  bands, as Ellis and librosa use.
- **The beat tracker was 70 ms late, then 25 ms early.** Frames were not centred (fixed), and a
  click test showed the onset curve itself peaks 24.8 ms before a hit (the window's lead). Beat times
  are now corrected by that measured latency: the tracker went from a 27 ms median error to 6 ms.
- **House came out at half tempo every time,** with a kick on every beat. My autocorrelation was
  computed over the whole clip; librosa's is averaged over 8-second windows, which favours shorter
  repeats. Switched to the windowed form, and kept the onset curve positive as librosa does.

## 3 — A kick drum without a click

The first synthetic kick was a pure low sweep; real kicks have a beater click. Without it, the
broadband clap drowned the kick in the onset curve. The click was added for realism (decided because
it is how a kick sounds, not to change a score), and the run was accepted as it came out.

## 4 — A cross-check, so the failures are the method's

Seventeen of forty exactly right looked low enough to be a bug, so librosa 0.11.0 (installed on D:,
outside the repo) was run on the same forty grooves: 22 of 40 right, and the same verdict as mine on 34
of 40: the same doubled ballads, halved drum and bass and 4/3 funk. The reel reports both.

## 5 — Rohan's constraint, and a new rule

- Rohan asked for **Western grooves only** after choosing the topic; the test set is rock, funk,
  house, hip hop, slow ballads, drum and bass, waltz and jazz swing.
- The **LOGO LAW** (new this week) means librosa, named on screen in B04 and B05, has to be shown by
  its logo. The toolkit had none; Rohan approved downloading librosa's own SVG from its repository,
  and it was added to `icons/logos/librosa/` (square canvas, 1024 PNG).

## 6 — Pronunciation

A free transcription of the narration heard "librosa" as "library", but the G2P gives /laɪbɹˈoʊsə/,
a normal reading, so it was kept. No researcher is named in the narration or on screen.

## 7 — Layouts found on probe stills (before any render)

Each new scene was probed at 50% and 97% of its beat in both cuts:
- **Portrait stacks ran into each other** (B01, B04, B06): three stats in a column collided with
  chips and the spark line. The phone layouts now put two stats per row.
- **B05's legend sat on the last grid row** on the phone: rows tightened, legend moved down.
- **B06's point labels sat on the curve** and on each other: both moved into the empty top band with
  dashed leaders.
- **librosa's mark was too small to read** in B04/B05: enlarged.
- **B02 was underfilled at mid-beat**: the onset curve now shows as a ghost from the start.

## 8 — The gates on 4K stills, then the contact sheets

The 4K probe (every new beat at 50%, 85% and 97%, both cuts) found what the 1080 stills couldn't:
- **§8.1 on the phone (72 px at 4K)**: lone words with no tall letters ("or", "a", "are", "more") in
  the phone strings, the "→" in "120 → 123.4", and B06's tick labels. Strings reworded, the arrow
  replaced by "to", B06's labels enlarged.
- **Data read as text**: B02's band image and B06's tracker line. Both joined type_check's DIEGETIC
  list with a comment, after the same frames were checked with the data masked (labels 44 px, pass).
- **§8.3**: B03's chip and spark line were still fading in at 97% (a half-transparent accent reads as
  #D97757): both now land before the beat's last words.
- **Gate V edge-bleed**: three phone chips and a chart label ran past the right title-safe edge;
  shortened or moved under the chart.
- **Contact sheet, after the finals**: B03's strip labels sat on the curve's spikes ("COPY" read as
  "CORY"); they now have a backing plate. B03 re-rendered in both cuts and both finals rebuilt.
- **Checked a frame of that master, and found a real bug**: the match curve was drawn up to one frame
  short of the current shift, so at 1.0 s it stopped on the rising edge and the "1.0 S" marker floated
  above a curve that never reached it (and the marker's x scale was 0.8% off the curve's). The curve now
  draws through the current shift, in full once the divisions arrive, on one shared x scale. B03
  re-rendered again and both finals rebuilt a third time.

## Render

Masters (`./art final`, receipts `*.verified.json` beside each file; SHA-256 re-checked on copy):

| Cut | File | Size | Length | SHA-256 |
|---|---|---|---|---|
| 16:9 | `landscape/TempoDetection_RohanV.mp4` | 3840×2160 | 202.08 s | `7ad56fbd866c2bef380e00b83fcfe1311f69a445f86ff793d8671155a32975af` |
| 9:16 | `vertical/TempoDetection_RohanV.mp4` | 2160×3840 | 202.08 s | `01d23230be380a8a3757502e8f5eda6d47aa028002b71c68db9bc754fc58bace` |

Gates on the accepted finals: GATE F pass; GATE T pass, 0 FAILs ([TYPECHECK.md](./TYPECHECK.md),
[vertical/TYPECHECK.md](./vertical/TYPECHECK.md)); Gate V clean, 0 BLOCKER / 0 MAJOR
(18 landscape and 18 portrait frames sampled). Looked at by eye: [qc-sheet-16x9.png](./qc-sheet-16x9.png),
[qc-sheet-9x16.png](./qc-sheet-9x16.png), plus single frames of the rebuilt beats.

Landscape: accepted on the first final, then rebuilt twice after B03's contact-sheet fixes (§8). Portrait: the same; both re-renders were B03 only. All on 2026-10-17/18.

Uploaded to Google Drive `2026-10-16/landscape/` and `2026-10-16/vertical/`; md5 of each Drive copy
matches the local master.
