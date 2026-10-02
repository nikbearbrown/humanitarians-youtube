# Fact-check gate — serving-the-panel-over-mcp-and-freezing-the-signal-contract (week 10)

Every number spoken or shown was checked against `figdata.json`, which
`scripts/make_week1011_figures.py` in the project repo queries from the live database and the
live signal at build time, or read directly out of `signal_example.json`. **Rows 6, 12, 15 and
18 are the ones to read before signing.**

Verdict types, as in weeks 1–9, plus one that is new this week:

- `LIVE-VERIFIED` — **new.** The MCP server was running during this build, and the claim was
  checked by calling the tool and reading the response, not by trusting the figure. The tool
  call and its result are in the build transcript.
- `REPRODUCIBLE` — re-run the committed query/script against the project database.
- `EXTERNALLY VERIFIABLE` — open the named artifact and read it.
- `AUTHOR-ASSERTED` — a fact about the author's own plan, repo, run, or decision.

| # | Claim | Beat | Verdict | Source |
|---|---|---|---|---|
| 1 | Two deliverables this week: a read-only MCP server and a frozen JSON signal | B00/B01/B09 | EXTERNALLY VERIFIABLE | Both exist in the project repo. The signal's emitted form travels with this reel as `signal_example.json`. |
| 2 | The server exposes exactly six tools | B00/B01/B04/B09 | LIVE-VERIFIED | `figdata.json` `tools[]` has six entries, and the running server advertises the same six by name: `list_companies`, `get_marks`, `compare_managers`, `get_propagation`, `get_fund_exposure`, `list_unresolved`. Asserted at injection. |
| 3 | `get_marks('Databricks, Inc.')` has 2,151 rows available | B00/B02/B04/B09 | LIVE-VERIFIED | Called in this build: `summary.marks` = **2151**, `page.total` = **2151**, `page.returned` = **50**, `page.remaining` = **2101**, and a `next_cursor` is present. Matches `tools[get_marks]` exactly. |
| 4 | Serialised whole that answer is 575,299 characters; bounded it is 17,976 | B02/B09 | REPRODUCIBLE | `tools[get_marks].unbounded_chars` / `.bounded_chars`, both asserted against their literal values. The 97% figure is derived at injection. |
| 5 | That is roughly 143,000 tokens | B02 | REPRODUCIBLE (derived) | 575,299 ÷ 4. **The ~4 chars/token ratio is an estimate, not a tokenizer count**, and the frame says so in its own token note rather than leaving it in the paperwork. |
| 6 | **The envelope makes five of the six tools BIGGER, by 19% to 49%** | B03/B09 | REPRODUCIBLE — **read this one** | Derived from `tools[]`: bounded exceeds unbounded for `list_companies` (+34%), `compare_managers` (+28%), `get_propagation` (+19%), `get_fund_exposure` (+31%) and `list_unresolved` (+49%). Only `get_marks` saves. **Neither the script nor either figure says this** — both show bounding on the one tool where it pays. The injection asserts 5 costlier and exactly 1 cheaper, so a future measurement that made bounding free would fail the build rather than ship a beat whose framing had gone stale. |
| 7 | Every answer is bounded twice — 50 rows AND 48,000 characters | B03/B09 | REPRODUCIBLE | `limits.default_limit` = 50, `limits.max_response_chars` = 48000, both asserted. The injection also asserts the bounded page is *under* the character ceiling, so the second bound is shown to actually bind. |
| 8 | Exactly one tool's answer was paged; the other five fit whole | B04 | REPRODUCIBLE | Derived and asserted: `rows_returned < rows_total` holds only for `get_marks`. That is the red row in `w10-tools.png`, and it is found by comparison rather than by index. |
| 9 | No tool writes a mark, clears a gate, or records a decision | B04/B09 | LIVE-VERIFIED | All six tools are reads; the running server advertises no write tool. The claim is an absence, so B04 draws it as one — three struck lines rather than a feature list. |
| 10 | A resolution decision needs a named human | B04 | AUTHOR-ASSERTED | A design decision established earlier in the project, restated here. It is the reason the server is read-only, not a consequence of it. |
| 11 | The signal has 9 top-level keys and refuses 10 field names | B01/B05/B09 | EXTERNALLY VERIFIABLE | `signal_example.json` is read directly by the build: its key list is the frame's key list, and `len()` is asserted equal to the 9 the figure claims. The injection also asserts that **none** of the refused names is present in the emitted file, so the frame proves the refusal rather than restating it. |
| 12 | **The quarterly note is checked four times, not three** | B07/B08/B09 | AUTHOR-ASSERTED — **read this one** | `figdata.json` carries **three** guards and `w11-guards.png` is titled "Three guards between the model and the note". The script and `README.md` say four. The fourth — a length check — was added after the figure was drawn, and is **not in `figdata.json`**. It is passed as the named constant `FOURTH_GUARD`, B07 draws it below a dashed rule as an addition rather than a fourth row of the same table, and the frame says where it comes from. If the fourth check is not real, B07's closing line and B09's last finding both need rewriting. |
| 13 | A draft claimed one company had the fewest marks, one sentence before claiming a different company did | B07/B09 | REPRODUCIBLE | `guards[]` carries the invented-ranking draft verbatim: "Databricks, Inc. has the lowest number of marks, at 2151." The injection asserts that row is present by its text, because it is the one B07 reads aloud. Databricks in fact has the **most** marks of any company in the universe — see row 14. |
| 14 | Every number in that draft was real, so the grounding check passed | B07/B09 | LIVE-VERIFIED | The draft's figure, 2151, is Databricks' true mark count (row 3). The *ranking* was the fabrication. This is the episode's central claim and it survives inspection: a number-level check cannot see a wrong superlative attached to a right number. |
| 15 | **The server lists 11 companies; the signal publishes 10** | B06 | LIVE-VERIFIED — **read this one** | `list_companies` returned `summary.companies` = **11** and `summary.with_marks` = **10**; the eleventh, Scale AI, Inc., has `marks: 0`. `signal.companies` = 10. Both numbers are correct and they answer different questions. On any frame that shows both this reads as a defect, so B06 reconciles it out loud. Asserted: listed − published == 1. |
| 16 | Four companies are suppressed this quarter, with a reason rather than a missing key | B05/B06/B09 | EXTERNALLY VERIFIABLE | `signal.suppressed` names X.AI Corp, Figure AI Inc., Perplexity AI, Inc. and Groq, Inc.; `signal_example.json`'s own `not_supported` list has the same length. Asserted equal. The live server's coverage status corroborates the shape: three are `watchlist`, one is `thin`. |
| 17 | `list_unresolved` returns zero rows, and that is an answer | B06 | LIVE-VERIFIED | Called in this build: `open_items` = **0**, `rows` = `[]`, and the summary states "nothing is unresolved: every ambiguity has a recorded human decision, every suspected split is adjudicated, and every Form D candidate identity is affirmed." Asserted as the only zero-row tool. |
| 18 | **An empty note was accepted as a success, and a spelled-out number went unread** | B08 | AUTHOR-ASSERTED — **read this one** | **Not in `figdata.json`.** Both come from `README.md`, are passed as `LATE_MISSES`, and B08's source line says so. These are the two failures that arrived late, and they are the reason the episode ends on its limits rather than on its deliverables. |
| 19 | Three setup bugs, all invisible from inside the server | B08/B09 | AUTHOR-ASSERTED | **Not in `figdata.json`.** Passed as `SETUP_BUGS`, from `README.md`: a `cwd` key the client never applies, a `--cwd` flag that does not exist, and a default registration scope that binds to the launch directory. Attributed on the frame. |
| 20 | 388 words accepted from `groq/openai/gpt-oss-120b` after retries | B07 | REPRODUCIBLE | `signal.commentary_words` = 388, `signal.commentary_model`, both asserted. The commentary is flagged `is_model_output` inside the signal itself rather than only in the paperwork. |

## What this cut deliberately does NOT claim

- **No company valuation.** N-PORT gives a fund's share count, never the company's shares
  outstanding. The contract refuses ten field names for exactly this reason, and B05 gives the
  structural argument rather than a stylistic one.
- **No claim that bounding is free.** Row 6. It costs on five of six tools.
- **No claim that the guards make the note true.** Row 14 — a wrong adjective with a correct
  number attached passes all four, which is why every rendering is labelled model output.
- **No claim that the server is timely.** Filings lag their period end by roughly 55–60 days,
  and the bulk sets lag those again. On the frame in B08.
- **No claim that zero unresolved items means zero ambiguity.** It means every ambiguity found
  so far has a recorded human decision.

## Wording changed from the script, and why

| Script | This cut | Why |
|---|---|---|
| "Same query, eighteen thousand characters instead of five hundred and seventy five thousand" | same, followed by a whole beat on what the envelope costs elsewhere | Row 6. The script's sentence is true of the tool it describes and not of the surface. |
| "Six tools… Nothing writes." | same, drawn as three struck absences rather than stated | SHOW-DON'T-TELL. The claim is an absence, so the frame shows absences. |
| "Three guards" (figure title) / "Four checks now" (script) | four, with the fourth drawn as a later addition and attributed | Row 12. The figure predates the fourth check; the reel cannot show three and say four without explaining which is older. |
| — (not in the script) | "the server lists eleven companies, the signal publishes ten" | Row 15. Both numbers appear in this reel's source material; a viewer who notices and is not told would be right to distrust the rest. |

## Before publishing

Rows 12, 18 and 19 are the three things in this reel that `figdata.json` does not contain. Each
is passed as a named constant and each beat that uses one says so on screen. **Row 12 is the one
that matters most**: the figure says three guards and the reel says four, and if the fourth is
not real then B07's close and B09's last finding are both wrong. Row 6 is where the reel argues
with its own source material, and row 15 is where it reconciles two of its own numbers rather
than hoping nobody notices. Everything else traces to `figdata.json` or `signal_example.json`
under an assertion, and rows 2, 3, 9, 14, 15 and 17 were additionally confirmed by calling the
live server during this build. Publishing remains a separate, explicitly authorized step.
