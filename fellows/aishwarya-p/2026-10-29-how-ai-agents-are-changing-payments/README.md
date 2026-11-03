# 2026-10-29 - How AI Agents Are Changing Payments (STEM/AI concept video)

**Week covered:** 2026-10-24 - 2026-10-30

**Video:** `how-ai-agents-are-changing-payments.mp4` (16:9) · `how-ai-agents-are-changing-payments-short.mp4` (9:16)

**YouTube:** Not yet published.

## Result

A concept video on AI agents in payments, built around one distinction: an agent with read access can give a wrong answer, while an agent with write access can make a wrong payment.

It covers four things:
- **Klarna's 2024 customer-service assistant:** its own launch numbers, then its 2025 move back toward human agents.
- **The first live agentic payments in Europe, June 2026:** ING in the Netherlands, then Nordea in Finland, both pilots using Mastercard Agent Pay.
- **Google's Agent Payments Protocol (AP2):** it records what a user asked for and approved.
- **The open question:** who is responsible when an agent makes a wrong payment.

**Not finished:** the video leaves the accountability question open on purpose. The sources don't settle it.

---

## The built reel

| | |
|---|---|
| 16:9 master | `how-ai-agents-are-changing-payments.mp4`: 3840×2160, 24fps, 165.83s |
| 9:16 short | `short/how-ai-agents-are-changing-payments-short.mp4`: 2160×3840, 24fps, 170.33s; all 8 beats plus a silent end card; no channel-title overlay in the short's beat sheet |
| review cut | `how-ai-agents-are-changing-payments-slate.mp4` |
| beats | 8: 4 Remotion bookends (B00A, B00, B05, B06) and 4 Manim content beats (B01-B04) |
| voice | Kokoro `af_bella` |
| build | 8 of 8 beats filled (`STATUS.md`) |
| gates | GATE P: `PEDAGOGY.md` signed `VERDICT: PASS` · GATE V master: 16 frames, 0 BLOCKER, 10 MAJOR · GATE V short: 18 frames, 0 BLOCKER, 9 MAJOR |

---

## Figure → beat map

| Beat | Act | Scene | Duration | What it argues |
|---|---|---|---|---|
| B00A | Intro | `ClaudeComposerAsk` | 11.14s | Presenter summary |
| B00 | Intro | `ClaudeComposerAsk` | 16.47s | Cold open: June 2026, an agent in Finland makes a real purchase and payment |
| B01 | Method | `B01_KlarnaAssistant` | 33.40s | Klarna, February 2024: 2.3M conversations, two-thirds of chats, the equivalent work of 700 full-time agents (its own numbers); 2025 return to human agents |
| B02 | Method | `B02_ReadVsWrite` | 23.79s | Read access risks a wrong answer; write access risks a wrong payment. Klarna's release is silent on moving money. |
| B03 | Change | `B03_FirstAgenticPayments` | 32.44s | June 2026 pilots: ING (customer approves the final choice), then Nordea (end to end); Agent Pay and agentic tokens; not yet available |
| B04 | Open question | `B04_Accountability` | 31.12s | AP2: intent mandate + cart mandate = an audit trail. Proof is not liability; still open. |
| B05 | Next steps | `ClaudeComposerAsk` | 11.71s | Handoff: write the limits for one payment you'd delegate |
| B06 | Outro | `ClaudeTitleOutro` | 5.76s | Title restate |

Manim scenes are in [scenes.py](./scenes.py).

## Things not to get wrong

1. **"Two-thirds", not "67%".** That's Klarna's own wording; 67% is a rounding of it.
2. **"The equivalent work of 700 full-time agents" is a workload comparison.** It is not 700 jobs cut.
3. **Klarna's figures are its own and were not independently verified.**
   - B01 says "Klarna's own numbers".
   - B01 also includes the 2025 reversal, when the CEO said quality had suffered. That's sourced through two secondary reports (Entrepreneur and Computing) of one Bloomberg interview; the Bloomberg piece itself wasn't read.
4. **Klarna's assistant is not called "read-only".** Its release doesn't say whether it could move money, so the video says that and no more.
5. **"Executing trades" was dropped.** No source found shows an agent executing trades, so write access is illustrated with paying an invoice and making a purchase.
6. **Both European payments were pilots.** Neither is available to customers yet.
7. **Only Nordea's payment is described as end to end.** In ING's, the customer approved the final choice.
8. **The Nordea date is given as "June".** Nordea's page gives 5 June and CX Network gives 6 June.
9. **AP2 is Google's proposal, quoted in its own words, not an adopted standard.** The video makes no claim about who uses it.
10. **"Proof isn't liability" is the video's framing.** Google's announcement allocates no liability and describes no dispute process, and the video doesn't guess who should pay.

See [PEDAGOGY.md](./PEDAGOGY.md) for the full evidence table and sources.

## Known defects

From the build's Gate V reports (`_qc/REPORT.md` for the master and `short/_qc/REPORT.md` for the short):

- **Master:** 10 MAJOR `underfill` flags (content fills less than 55% of the safe area) on B01, B02, B03, B04, B06. No BLOCKERs.
- **Short:** 9 MAJOR `underfill` flags on B01, B02, B03, B04, B06, END. No BLOCKERs.

## Files

- [README.md](./README.md): this page.
- [NARRATION.md](./NARRATION.md): the approved narration, one paragraph per beat.
- [beat_sheet.json](./beat_sheet.json): the edit: 8 beats, narration, scene per beat, measured audio durations, build stamp, and the source list in its metadata note.
- [scenes.py](./scenes.py): the four Manim content scenes (B01-B04).
- [PEDAGOGY.md](./PEDAGOGY.md): act structure, evidence table with sources, friction protected, `VERDICT: PASS`.
