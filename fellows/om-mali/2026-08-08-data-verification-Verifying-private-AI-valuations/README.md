# 2026-08-08 - Verifying private AI valuations from SEC filings

**Week covered:** 2026-08-03 - 2026-08-09

**Video:** [Mycroft_OmMali_08_08_2026.mp4](https://drive.google.com/drive/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv)

**Process log:** [FRICTIONAL.md](./FRICTIONAL.md)

## Result

The Private AI Valuation Agent works out a per-share price for private companies such as Anthropic, OpenAI, SpaceX and Databricks, using the quarterly reports that US mutual funds are required to file with the SEC: a fund must disclose what a holding is worth in dollars and how many shares it owns, and dividing one by the other gives a price for a company that has no share price.

This week tested whether that idea survives contact with real filings, by
checking it by hand before building anything.

- **19 Anthropic holdings were read directly from six fund families' filings** —
  Fidelity, T. Rowe Price, Alger, ARK, BlackRock and Capital Group — and the
  arithmetic holds. **Four of the six independently report the same price:
  $259.14.**
- **The funds agree with each other rather than disagree.** That was the
  surprise, and it changed the question the project asks: not "how far apart
  are these valuations" but "how quickly does a new price spread from one fund
  to the rest".
- **The rule the project had planned to use for picking out private holdings
  was wrong.** It found only one of the six managers, because two firms report
  a flag incorrectly and the others use a different placeholder code. It was
  replaced with a more reliable field and re-tested.
- **The bulk data matches the original filings exactly — 15 of 15, no
  mismatches.** Where a fund filed something incorrect, it is stored as filed
  rather than corrected, so the database never says something the SEC did not.
- **Two search traps were caught before they became data.** Searching for
  "Cohere" returns Coherent Corp, a listed optics manufacturer, and searching
  for "X.AI" mostly returns bonds rather than shares. Either would have
  produced a convincing price history for a company that was never there.
- **The list of companies to track was reviewed and fixed by a person**, with a
  written reason recorded for each company included or excluded.

---

## The episode

The premise in one line: a fund that holds private company stock must report that position's
**value in dollars** and its **balance in shares**. Divide one by the other and you have a
per-share price for a company with no public price.

Week one does not build that pipeline. It checks, by hand, whether the premise survives contact
with real filings — which is why the week's most useful output is a **defect report against its
own plan** rather than a working system.

| Document | What it is |
|---|---|
| `narration_script.md` | the spoken script, with timings measured rather than estimated |
| `BUILD-PROMPT.md` | the single paste-ready prompt that rebuilds this reel end to end |
| `BUILD-LOG.md` | decisions taken, and every defect found by reading frames |
| `CHECKS-REPORT.md` | the PROOF GATE — per-beat SHOW/HOLD classification, written before the first compile |
| `FACTCHECK.md` | 20 rows, each tracing a spoken claim to the filing or artifact behind it |
| `PEDAGOGY.md` | GATE P — what the author is being asked to sign off on |
| `description.txt` | the written version of the episode |

## The built reel

Built with **brutalist.art** (`ai-explainer`, channel `claude-hai`) — free and local
throughout: Kokoro TTS, Remotion, ffmpeg. **$0.00 spent, no API key used.**

Ten beats, 2:35, 3840×2160. **GATE P signed, all 20 FACTCHECK rows confirmed, GATE V clean.**
An earlier 6-beat static cut is archived at `_previous-build/` rather than deleted.

Nothing here is published. The masters stay in this folder.
