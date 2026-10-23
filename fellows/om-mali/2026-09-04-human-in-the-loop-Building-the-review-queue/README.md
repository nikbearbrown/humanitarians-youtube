# 2026-09-04 - Building the human review queue

**Week covered:** 2026-08-31 - 2026-09-06

**Video:** [Mycroft_OmMali_04_09_2026.mp4](https://drive.google.com/drive/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv)

**Process log:** [FRICTIONAL.md](./FRICTIONAL.md)

## Result

The Private AI Valuation Agent works out a per-share price for private companies such as Anthropic, OpenAI, SpaceX and Databricks, using the quarterly reports that US mutual funds are required to file with the SEC: a fund must disclose what a holding is worth in dollars and how many shares it owns, and dividing one by the other gives a price for a company that has no share price.

Some filings cannot be matched to a company automatically. This week built the
system that handles those — and its central claim is what the software does
**not** do: it sorts, groups and presents, and decides nothing.

- **4,537 of 5,806 holdings (78%) were matched with no human involvement.**
- **The remaining 1,269 holdings turned out to be only 8 real questions.** The
  same ambiguity is asked once, not once per holding, so one answer applies to
  every filing that shares it. All 8 were answered by a named person in seven
  commands.
- **Those 8 answers do not point the same way, which is why a person is
  needed.** One case looked like a stock split and was a reporting convention;
  one was a genuine 10-for-1 split, caught before it entered the data as a 90%
  price crash; one was an ordinary repricing. **Software treating all three the
  same way would be wrong two times out of three.**
- **The queue found a deliberately planted error on its own** — 28 holdings of
  a company that had been flagged as a known false positive — without being
  told to look for it.
- **An unplanned server crash proved the system is more robust than its tests
  claim.** Paused reviews survived the crash and a cold restart with nothing
  lost.
- **The whole run was repeated on a different database with nothing copied
  across, and produced identical figures**, which turns a claim about
  reproducibility into evidence.

## Rules

- Every number in every figure is queried from the project's Postgres at build time
  (`scripts/make_week6_figures.py` in the project repo) and dumped to `figdata_week6.json`
  before anything is drawn. No figure carries a hand-typed number.
- Both QA passes were run: `npm run audit:layout` reports **0 errors on all five**, and each
  PNG was read and checked for substance.
- Six palette tokens from `brutalist/DESIGN.md`, nothing else. Red is the primary series, never
  "danger" — here it marks the human's share of the work, which is the subject of the week.

## The one thing not to get wrong on camera

**The AI decided nothing.** It routed, grouped and presented. All 45 recorded decisions carry a
human name and a written reason, and the code rejects a decision missing either. Seventy-eight
percent resolved unaided and twenty-two percent needed a person — that is the design working,
not a shortfall.

## Three corrections these figures forced

Worth knowing, because the prose said something different until the figures were built:

1. **There were three suspected-split questions, not four.** An earlier write-up said "all four
   split triggers" and "wrong three times out of four". Counted from the database: three
   questions, 9 cards, 925 holdings — so it is **two times out of three**. Fixed in the project
   docs and the RUN_LOG as well as here.
2. **Perplexity's unchanged value is $4,228,993.75, not $4,228,994.** An earlier query rounded
   it before the number reached a decision rationale. The figure now shows the filed value to
   the cent, which makes the point better: ten times the shares, the same dollars exactly.
3. **The X.AI list needed its security titles.** Three of the 24 spellings share one issuer name
   and differ only in the title, so without them the figure showed three identical rows — which
   reads as a data error rather than as the point.

---

## The built reel

*(Appended by the brutalist.art build. Everything above is the original figure brief and is
unmodified.)*

Rebuilt as a 12-beat `ai-explainer` / `claude-hai` reel — **twelve beats, zero slates, $0.00**.
Free/local throughout: Kokoro TTS + Remotion + ffmpeg.

**Two masters, one edit.** 16:9 at 3840×2160 and 9:16 at 2160×3840, from the same components,
the same props and the same narration mp3s. The vertical cut is a re-layout, not a crop.

| Where | What |
|---|---|
| `building-the-human-review-queue.mp4` | 16:9 master, 3840×2160 |
| `vertical/building-the-human-review-queue-916.mp4` | 9:16 master, 2160×3840 |
| `*-slate.mp4` | review cuts with beat IDs and running timecode |
| `PEDAGOGY.md` | GATE P — what the author is asked to sign |
| `FACTCHECK.md` | 20 rows; read 6, 12, 18 and 19 |
| `CHECKS-REPORT.md` | PROOF GATE, written before the first compile |
| `BUILD-LOG.md` | decisions, and what reading the frames caught |
| `BUILD-PROMPT.md` | the paste-ready prompt that rebuilds both cuts |
| `build_beat_sheet.py` | the injection — every on-screen number, under assertions |

The five figures listed above were used as REFERENCE and rebuilt as native animated scenes
(REBUILD LAW). They now live in `pantry/`, were never slotted as media, and were never copied
into `images/`.

**One correction this build made to the script.** The 2:00 section says the three price steps
"looked identical — a price falling by exactly ten". Two are ×10; Anthropic's is **×4.0**
(`12.18 → 48.94` over one quarter). The rendered beat labels each magnitude, so the original
line contradicted its own frame. The narration now says the three *tripped the same detector*,
which is both true and the actual point. See `FACTCHECK.md`.
