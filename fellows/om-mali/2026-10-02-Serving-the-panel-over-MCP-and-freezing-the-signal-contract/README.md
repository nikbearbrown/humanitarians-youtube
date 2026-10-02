# Serving the panel over MCP and freezing the signal contract

Four figures and a 3:00 narration script. Two deliverables: a read-only MCP server that lets an
AI assistant query the marks panel directly, and a frozen JSON signal another system can parse
without guessing.

| File | Beat | What it shows |
|---|---|---|
| `w10-bounding.png` | 0:35 | The same query serialised whole (575k chars, ~143k tokens) against bounded (18k) |
| `w10-tools.png` | 1:15 | Six read-only tools, rows returned versus rows available, response sizes |
| `w11-contract.png` | 1:50 | The signal's nine top-level keys, and the ten field names it refuses |
| `w11-guards.png` | 2:30 | Three guards with a draft that fails each — the invented ranking is the surprise |

SVG sources sit beside each PNG. PNGs are 2917 × 1750. `figdata.json` is the measured data every
figure was drawn from, and `signal_example.json` is a real emitted signal.

## Rules

- Every number is queried from the live database and the live signal at build time
  (`scripts/make_week1011_figures.py` in the project repo) and dumped to `figdata.json` before
  anything is drawn. No figure carries a hand-typed value.
- Both QA passes were run: the layout audit reports **0/24 flagged**, and each PNG was read and
  checked for substance.
- Six palette tokens from `brutalist/DESIGN.md`, nothing else. Red is the primary series, never
  a warning colour.

## The three things not to get wrong on camera

**Token bounding is the deliverable, not a detail.** A server that speaks the protocol
correctly and answers with 143,000 tokens is a server nobody can use. The summary describes the
*whole* result set, not the returned page — one computed over page one would say "3 managers"
about a company held by thirty.

**Read-only is a design decision.** Earlier in the project a resolution decision was established
as needing a named human. A tool a model can call to record one is the opposite of that. The
server exposes every judgment already made and shows what's still open; it cannot create one.

**The refused fields are structural, not stylistic.** These filings give a fund's share count,
never the company's shares outstanding, so no company valuation is derivable. A field for one
would invite a consumer to fill it from elsewhere and inherit that source's error.

## Why the grounding check wasn't enough

The honest centre of this episode. The commentary model gets the computed figures and nothing
else — no database, no tools, no retrieval — so a number in its prose that isn't in those
figures is a fabrication, and that is mechanically checkable.

It passed. And the draft still said one company had the fewest marks, one sentence before
saying a different company had the fewest. Every number was real; the *ranking* was invented,
and it contradicted itself inside a paragraph.

Three more checks followed — superlatives, placeholders, length — with a failed draft handed
back to the model carrying the specific complaint, up to three attempts. What none of them catch
is a wrong qualitative adjective with a correct number attached, which is why every rendering is
labelled model output rather than a verified claim.

## What the figures do not show

The two model-facing failures that arrived late and are worth knowing:

- **An empty note was accepted as a success**, reported as "0 words". An empty draft passes every
  content check trivially — nothing to fabricate, nothing to rank, no placeholder. A reasoning
  model had spent its whole token budget on a hidden channel. Length became the fourth check.
- **Spelled-out numbers were unchecked.** A draft wrote "across sixty-one groups", which was
  correct and would have passed identically had it been wrong, because the check only read
  digits.

## Three setup defects, all the same shape

Mentioned in the close and worth the detail here. Getting the server to launch from a real client
took three attempts, and each failure was invisible from inside the server:

1. a `cwd` key the client never applies before resolving the module,
2. a `--cwd` flag that does not exist on the CLI,
3. a default registration scope that binds the server to whichever directory the command ran in.

The server's own selftest passed through all three. So did an in-process protocol test that
supplied `cwd` itself. **A test finds this class of bug only if it withholds what the real caller
withholds** — which is now a test that starts the server from a temporary directory with no
working directory and no `PYTHONPATH` set.

Confirmed afterwards by observation rather than inference: a real client reports the server
connected.

---

## The built reel

Built with **brutalist.art** (`ai-explainer`, channel `claude-hai`) — free and local throughout:
Kokoro TTS, Remotion, ffmpeg. **$0.00 spent, no API key used.**

Twelve beats, 3:32, in **both orientations**: `Mycroft_OmMali_02_10_2026.mp4` (3840×2160) and
`vertical/serving-the-panel-over-mcp-and-freezing-the-signal-contract-916.mp4` (2160×3840). The
9:16 cut is a **re-layout, not a crop** — both render from the same components and the same
props, and carry the identical narration MP3s.

The four figures above travel in `pantry/` as **reference**. Every beat is rebuilt native
(REBUILD LAW); no PNG is slotted as media.

| Document | What it is |
|---|---|
| `BUILD-PROMPT.md` | the single paste-ready prompt that rebuilds this reel end to end |
| `BUILD-LOG.md` | decisions taken, every defect found by reading frames, three toolkit fixes |
| `CHECKS-REPORT.md` | the PROOF GATE — per-beat SHOW/HOLD classification, written before the first compile |
| `FACTCHECK.md` | 20 rows. **Read rows 6, 12, 15 and 19 before signing.** |
| `PEDAGOGY.md` | GATE P — what the author is being asked to sign off on |
| `description.txt` | the written version of the episode |

### Two beats this README's own figures do not contain

**The envelope is not free.** Both figures show bounding on `get_marks`, where it cuts 575,299
characters to 17,976 — a 97% saving. Measured across all six tools it makes five of them
**bigger**: `list_unresolved` +49%, `list_companies` +34%, `get_fund_exposure` +31%,
`compare_managers` +28%, `get_propagation` +19%. It pays for itself on exactly one tool. The
build asserts five costlier and exactly one cheaper, so a future measurement that made bounding
free would fail rather than ship a beat whose framing had gone stale.

**Eleven companies against ten.** `w10-tools.png` says `list_companies` returns 11 rows;
`w11-contract.png` says the signal publishes 10. Both are correct — the eleventh has zero marks
— and both appear in this folder. A viewer who notices and is not told would be right to
distrust everything else on screen, so the reel reconciles it on camera.

### Three values are not in `figdata.json`

The fourth guard, the two late misses, and the three setup bugs. Each is passed into the build
as a named constant and each beat that uses one says so on screen. **The fourth guard is the
load-bearing one**: `figdata.json` carries three guards and `w11-guards.png` is titled "Three
guards", while the script says four. The reel draws the fourth below a dashed rule, labelled as
postdating the figure, rather than showing four rows of equal provenance.

### Six claims verified against the live server

The MCP server was running during the build, so six FACTCHECK rows were checked by calling the
tool rather than trusting the figure — including the 11-against-10 (`list_companies` reports 11
companies, 10 with marks, and names the one with zero) and the paging behaviour
(`page.returned` 50, `page.remaining` 2101, cursor present).

Nothing here is published. The masters stay in this folder.
