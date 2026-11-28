# SHOTLIST — Confidently Out Of Date

Week ending 2026-11-27 · `ai-` track · 8 beats · master 16:9 3840×2160.

SHOW authored before narration. Durations are the measured Kokoro `am_onyx`
MP3s — the master clock.

| # | Act | Scene | Audio | What the viewer WATCHES |
|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | 17.83s | Greeting (`Salaam, Jainil`) · the question types in · two output lines answer it |
| B01 | BLUF | `BrutalistHesitantWriter` | 11.82s (+0.8 lead) | Types **loudly**, deletes it, types **quietly** |
| B02 | SETUP | `StageRail` | 16.83s | Index built → the language moves → the index does not, with *nothing triggers a rebuild* |
| B03 | BODY | `PairedBars` | 18.24s | Four rows · rebuilt bar identical every time · stale bar absent on the last two |
| B04 | BODY | `CardSet` | 22.57s | Two cards: **a word it never saw** vs **a word that moved** |
| B05 | LAND | `StageRail` | 22.12s | Clock → canary → the metric that will not help, with *it barely moved* |
| B06 | HANDOFF | `ClaudeComposerAsk` | 19.63s | "Your turn." · the prompt types in and is read aloud |
| B07 | OUTRO | `HaiTitleOutro` | 3.58s | Title restate · `@HumanitariansAI` |

**Total 132.6s + 0.8s lead = 133.4s — 2:13.4.** Master window 2:00–5:00 ✓ ·
Short cap 3:00 ✓.

---

## The spine

Cold open → BLUF → what changes → the sweep → the two failures → the fix →
handoff → outro. Typing appears in exactly three beats.

## B04 is the reel

B03 shows a loud failure — all-new vocabulary, no vector, nothing comes back.
That is the boring half, because somebody notices an empty page.

B04 is the half the title refers to. The index **has** a vector for the
migrated word, it is confident about it, and it is pointing at where that word
used to live. Two cards, same recall of zero, and only one of them looks like
a failure. The terracotta sits on the quiet card.

## B02 and B05 are a deliberate rhyme

Both `StageRail`, three beats apart. B02 is what goes wrong; B05 is what to
do. Same shape, opposite job — so the fix reads as a change to the diagram
rather than a new idea.

## What this reel does not argue

It does not say stale indexes are always broken. The measured answer is that
staleness is **harmless** while queries still use old vocabulary — 100% recall
at half-new words, identical to a rebuilt index. The reel leads with that,
because a video that claimed constant catastrophe would be easy to disprove
and would deserve to be.

The first version of the experiment produced a **null result** — 98.5% vs
100%, no effect worth reporting. That is recorded in `FACTCHECK.md` rather
than hidden, and the fix was to change the question (how much new language
does it take?) rather than to reweight the queries until the effect appeared.

## A line that was corrected before compile

B05 originally said the similarity score "never dropped at all". It drops from
0.961 to 0.892. The line now states the actual move and the stage card prints
both figures. The argument is unchanged and the phrasing is now checkable.

## Accent discipline

One terracotta moment per beat: B01 the deleted word · B02 the unchanged
index · B03 the stale series · B04 the quiet-failure card · B05 the metric
that will not help · B07 the period.

## Fill (GATE V)

`PairedBars` runs four rows with `total: null`. That is the exact shape that
failed the fill floor on 2026-11-20 at 42% cover, before the component was
made to scale its row height by slot count (A25). Re-measured after that fix:
~65%. This reel was built on the fixed component — **and that is a
calculation, not an assumption carried over.**

B01 and B07 carry `qc.sparse` waivers, as on every prior reel.
