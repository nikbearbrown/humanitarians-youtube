# FACTCHECK — hai-brutalist-week-1

Status: **GATE F — drafted 2026-10-20. 6 rows VERIFIED-LOCAL, 2 rows SPEC-ASSERTED,
1 row ARGUMENT.**

Verdict vocabulary: **VERIFIED-LOCAL** = checked against first-party evidence produced on
this machine during the week being reported. **SPEC-ASSERTED** = a statement about how the
toolkit works, taken from its own documentation and consistent with local behaviour.
**ARGUMENT** = reasoning or advice, not a measurement.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B00 | This is Saurabh K.'s first week on brutalist.art; the narration voice is AI-generated, the work is his | **VERIFIED-LOCAL** | Kokoro `am_onyx`, generated locally this session at $0.00. Disclosure spoken aloud in B00 | Keep the disclosure spoken, not only written |
| 2 | B01/B04 | Four finished masters shipped this week | **VERIFIED-LOCAL** | Four files on disk, each probed: `hai-mcp-explained.mp4` + its `vertical/`, `hai-agents-on-their-own.mp4` + its `vertical/` | Re-probe if any is rebuilt |
| 3 | B04 | MCP, Explained is 2:41; Agents, On Their Own is 2:14; widescreen is 3840×2160 and vertical is 2160×3840 | **VERIFIED-LOCAL** | `ffprobe`: 160.79s and 134.04s; dimensions read from the same probe | Re-probe before publish |
| 4 | B02 | The toolkit turns a beat sheet into a 4K master, generates narration locally, and runs for free | SPEC-ASSERTED | `RENDER-TARGETS.md` §1 ("beat sheet → 4K master"); `CLAUDE.md` rule 6 (free by default); Kokoro ran locally this session and reported $0.00 | — |
| 5 | B03 | Four terms: beat sheet, lane, gate, master | SPEC-ASSERTED | Working definitions drawn from the toolkit's own docs and observed behaviour; not quoted standards | Keep as working definitions |
| 6 | B05 | The typography gate had never actually run on this machine — it skipped silently because a library was missing | **VERIFIED-LOCAL** | `./art final` printed `[typecheck] missing dep: No module named 'scipy'` followed by `GATE T skipped — missing deps` | — |
| 7 | B05 | Once the library was installed, it crashed on an old Python | **VERIFIED-LOCAL** | `type_check.py` raised `TypeError: unsupported operand type(s) for \|` on the annotation `float \| None`; the default `python3` on this machine is 3.9.6, and that syntax needs 3.10+ | — |
| 8 | B05 | When it finally ran, it failed 8 of 10 vertical beats | **VERIFIED-LOCAL** | First real GATE T run on `hai-agents-on-their-own/vertical`: `GATE T: FAIL (8 pixel beats)` — B01, B02, B03, B04, B05, B06, B07, B09 of B00–B09 | Recount if beats change |
| 9 | B06 | At phone size the type was about half the size it needed to be | **VERIFIED-LOCAL** | The gate measured a smallest text run of 38px against a 72px floor (1.9% of 3840) — 0.53× | Derived ratio; restate if the floor changes |
| 10 | B06 | No probe replaces opening the frame and looking at it | ARGUMENT | Advice, not a measurement. It is also the toolkit's own rule 4 ("Verify renders by LOOKING at frames… never by the mp4 probe alone") | Keep attributed as the project's position |

## Honesty notes

- **Narration is AI-generated** (Kokoro `am_onyx`), disclosed aloud in B00. The work, the
  commits and the four films are Saurabh K.'s.
- **Rows 6, 7, 8 and 9 are first-party failures**, not illustrations. Every number in the
  B05 card is an actual line of output from this week's builds.
- **The film reports a mistake as its main finding.** The gate was right and the frames were
  wrong; B06 states that plainly rather than presenting the week as a clean run.
- **Row 2 counts masters, not uploads.** Nothing has been published; `RENDER-TARGETS.md` §1
  is explicit that this toolkit renders and does not publish.
