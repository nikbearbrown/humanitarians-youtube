# PEDAGOGY — What It Stopped Needing

**GATE P. Unsigned. Audio will not run until a human signs the last line.**

Week of 2026-09-11 · clauding 1.0.0 · `weekly_updates/09-11-2/`
Second reel of this date. 09-11-1 is LoonNet; this one shares only the channel,
the host and the chassis.

---

## The ONE idea

> The rewrite deleted more than it wrote — and those deletions are not one kind
> of deletion.

Some things were dropped because the author decided he did not want them. Others
stopped being necessary because a single design decision dissolved the need for
them. And one was a hazard that the rewrite deleted the *conditions* for, rather
than defending against. "We made it leaner" collapses all three into a number,
which is exactly what this reel refuses to do.

---

## Act structure

| Beat | Act | Pattern | Carries |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Cold open. "This is Sai." The arithmetic, then the question the reel must earn. |
| B01 | THE OBJECT | `ClaudeScienceChipGrid` | What clauding is — three states, and what it refuses to ship as. |
| B02 | THE STATES | **STILL** | The entire interface, rendered. The evidence beat. |
| B03 | TWO KINDS | `DivergentFates` | The ONE idea. Stopped-needing vs chose-to-drop. |
| B04 | THE FORK | `BinaryBranch` | Harden the PATH lookup, or remove it. |
| B05 | WHAT SURVIVED | `ClaudeScienceChipGrid` | The behaviour carried over from upstream, credited. |
| B06 | VERDICT | `ClaudeVerdictArtifact` | One page, four lines. |
| B07 | HANDOFF | `ClaudeComposerAsk` | A prompt the viewer can paste. |
| B08 | OUTRO | `LogoOutro` | Sign-off. Five words. |

**ILLUSTRATE-LAW check.** The Claude UI appears at B00, B07 and the
verdict/outro only. Body beats run ChipGrid → STILL → DivergentFates →
BinaryBranch → ChipGrid — no two consecutive beats share a pattern. B01 and B05
are both ChipGrid but are separated by three beats, and they carry opposite
content on purpose: what the thing *is* versus what it *kept*.

**9:16.** Every pattern used has a registered `916` sibling, re-verified against
`Root.tsx` on 2026-09-11. The guide's default B01/B02 patterns
(`ClaudeScienceLayerStack`, `ClaudeScienceSourceFlow`) still have none and are
avoided for that reason alone. B02 is the only user-media beat; it carries a
hand-composed `pantry/B02-916.png` because a centre cut would slice the model and
effort text off the right of every row — which is the beat's whole point.

---

## Evidence and honesty

- **The raw material is the author's own prose.** He authorised the repository's
  `feat!` commit body and `CHANGELOG.md` 1.0.0 as this week's report in place of
  dictated bullets. Nothing was inferred from diffs alone.
- **Every figure was re-derived**, not taken on trust. The full table is in
  `SOURCES.md`. The 58-test count reconciles exactly: 46 plain test functions plus
  12 parametrised cases.
- **No benchmark appears anywhere.** No CPU, memory, launch-time or battery
  number, and no speed comparison against the Swift version — none was measured.
  The narration never says "faster".
- **B02 is a rendering and says so on its own face**, in both cuts.
- **Name the project, not the person.** The upstream is `claude-status-bar` or
  "the original" throughout, by the author's instruction — stricter than the
  repo's own README, which credits its author by name.
- **B03's second track is labelled a taste call** in the author's own voice. The
  reel does not dress a preference up as an engineering result.
- **B05 credits the upstream** for the behaviour that was kept. A rewrite reel
  that only lists what it removed would be taking credit for someone else's
  hard-won subtlety.

---

## Human review checklist

- [ ] **The ONE idea is yours** — that the deletions divide by *cause*, not by
      count. If you would rather the reel just said "it got smaller", say so now;
      it is the spine of B03, B06 and B07.
- [ ] **B03's framing** — "stopped needing" versus "chose to drop" — is an
      editorial cut the voice makes. Confirm the seven dropped features really
      were taste, not necessity.
- [ ] **B04 claims the PATH hazard was real** but never claims it was exploited.
      Confirm that is the line you want.
- [ ] **No benchmark, no adoption number, no "faster"** anywhere.
- [ ] **B02's plate** is labelled a rendering. Look at it. If you would rather
      ship a real screenshot, it replaces the plate — it does not relabel it.
- [ ] **The upstream author is not named** anywhere, in any file.
- [ ] **B06's four artifact lines** are the ones you would defend in a meeting.

---

## What happens after you sign

Audio unlocks. `generate_audio_kokoro.py` measures the real narration durations
and those become the master clock — the estimates in `beat_sheet.json` are
advisory only and are replaced. If a beat then runs long, change the words and
regenerate; never hand-edit a duration.

Estimated at `am_onyx` pace: ~149 s total, so the derived 9:16 cut has room under
the 180 s ceiling even before any beat is dropped.

---

To sign: replace the blank below with the four-letter word that means approved.

VERDICT: PASS    — reviewer: SAI NIKHIL KUNAPAREDDY  date: 09-11-2026
