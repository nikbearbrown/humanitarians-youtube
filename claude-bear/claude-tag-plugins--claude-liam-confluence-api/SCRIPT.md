# Two APIs, Not One — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-tag-plugins/claude-liam-confluence-api`).*
*Register: **Plain**. 7 beats. Source was a 7-beat Teardown-register reel
(register: Teardown) covering B00 cold open, B01 anatomy (two versions +
three scripts + body formats), B02 design (security note + pagination trap
+ error codes), B05 teardown (gets right / bites), BVDT verdict, BHTF
your-turn, BOUT outro. Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no
generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude calls one Confluence API. It actually calls two — a newer default and an older one for a few specific jobs. So which one runs, and when?" | Writer types "Claude just calls one Confluence API. How does that work?"; "one"/"API" hesitate and correct to "two"/"APIs" |
| NB01 | 3 mechanism | Confluence Cloud actually runs two APIs at once. Claude defaults to the newer one, called v2 — it handles pages, spaces, blog posts, comments, attachments, and labels. It only drops to the older v1 API for three jobs v2 can't do: searching with Confluence's query language, uploading or downloading an attachment, and adding a label. Three small scripts cover the everyday work: cql_search.sh runs a search and pages through every result; read_page.sh fetches a page in the format you ask for; write_page.sh creates or updates a page, and safely retries if someone else saved a change first. | two version chips + three script chips |
| NB02 | 3 mechanism | Two details trip people up. First: every Confluence call needs a slash-wiki prefix in the URL. Leave it off and every single request fails with a not-found error — it looks like a bug, but it's just the missing prefix. Second, a pagination trap: when a search has more results, the next-page link works differently in each version. In v2, that link already starts from the site's root, so you have to strip the slash-wiki part off your base address before adding it — otherwise you get slash-wiki twice. In v1, you add the base address exactly as it is. Mix these up, and later pages simply stop appearing, with no error at all. | "/wiki required" + "v2: strip" + "v1: keep" chips |
| NB03 | 3 mechanism | There's one rule that matters more than any API detail. A Confluence page might contain text written specifically to hijack an AI reading it — instructions hidden inside a comment or a page body, hoping Claude will follow them. Claude treats anything it reads back from Confluence as content to report, never as a command to run. A few smaller things are worth knowing too: one of the write formats packs its data as a string that has to be decoded twice; long result lists cap out well below their real maximum, so a big search can quietly come back short; and deleting a page for good, or uploading a file, both need one extra permission or header most people forget the first time. | "treat as data" / "not as commands" / "double-parse ADF" / "limits truncate quietly" chips |
| **BCRY** | **6 carry-out** | Claude doesn't speak one Confluence API — it defaults to the current one and drops to the older one only for search, uploads, and labels. And whatever a page says, Claude reads it as content, never as a command. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Search our Confluence space for pages about onboarding, then read the most recently updated match and summarize it for me. Before you show me anything from inside that page, tell me plainly whether you're giving me your own summary or quoting the page's own words. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Two APIs, Not One. Liam, in for Bear. | OutroSeries — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-tag-plugins`, Teardown metadata) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Ask Claude to find/read/search/create/update a Confluence page… the Confluence API skill fires." (B00 cold-open framing) | reframed as a direct question: "Claude just calls the Confluence API, right?" — same subject, sharper hook |
| Facts | two API generations (v2 default, v1 for CQL search/upload/labels); three bundled scripts; four body formats; `/wiki` prefix mandatory; pagination URL relativity trap (v2 site-root-relative, v1 `/wiki`-root-relative); error codes 400/401/403/404/409/413; security note (never follow retrieved-content instructions); documentation gaps (`/wiki` warning buried, `atlas_doc_format` double-parse, silent list truncation, `purge=true` needs space-admin, upload XSRF header) | unchanged, except: the four body formats are folded into NB03's "double-parse ADF" fact rather than given a full four-way breakdown (storage/ADF/view/export_view), since only the ADF double-parse trap is a practical gotcha a general viewer needs; the six specific error codes are not itemized (the underlying causes — missing `/wiki`, version race — are covered in NB02/NB01's script description instead) |
| Beat count | 7 beats: B00 composer-ask + B01/B02 anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn + BOUT outro | kept the same 7-beat shape: B00 carries the wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02 kept as one beat each; B05's "gets right / bites" list reframed (not compressed away) into NB03's neutral "worth knowing" facts, dropping only the verdict framing itself; BVDT folded into BCRY; BHTF kept, with the source's Claude-Code-session/ENG-space-specific task replaced by a paste-ready prompt any viewer can run without special space/label setup; BOUT kept |
| B00 | `ClaudeComposerAsk` cold open stating the routing model directly, no wrong-guess framing | `BrutalistHesitantWriter` (WRITER LAW) — "one"/"API" → "two"/"APIs", the actual wrong guess the body corrects |
| Register | Teardown (metadata `register: "Teardown"`) | Plain — explicit no-judgment audit below |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroSeries`, `@HumanitariansAI`, Liam sign-off |
| Handoff prompt | source's Claude-Code-session task ("search ENG space… watch five things") | reworked into one runnable, paste-ready prompt that exercises the same three behaviors (search, read, quote-vs-obey) without requiring a specific workspace/space/label |

No source beat was `ai-video-prompt`, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION
(`ClaudeComposerAsk`/`ConfluenceApiAnatomy`/`ConfluenceApiDesign`/
`ConfluenceApiTell`/`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW
required no substitution beyond B00's mandated cold-open swap. The source's
`ConfluenceApiTell` component was not reused for NB03 even though it is
REMOTION: its on-screen text is hardcoded as "CONFLUENCE API · TEARDOWN"
with "✓ WHAT IT GETS RIGHT" / "✗ WHERE IT BITES" columns — a verdict
rubric baked into the component itself, not just the narration. Reusing it
would put Teardown judgment on screen under Plain narration. NB01–NB03 use
the generic "chip row" Manim template instead (copied verbatim, mechanism
and GATE T exemption notes included, from the
`claude-plugins-official--claude-liam-access` sibling), which is
parametrized entirely from neutral title/chip/caption strings.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the question; mechanism waits until NB01 |
| Wrong guess surfaced, falsified by a case | B00 states the guess (one API); NB01 states the actual two-version split as the immediate correction |
| One anchor | N/A this reel — the wrong guess resolves immediately at NB01 rather than through a planted/paid-off scene; see `anchor_pair: "N/A"` in beat_sheet.json metadata |
| Both directions | NB02's pagination trap states both failure directions implicitly (get v2's rule backwards → double `/wiki` → 404; get v1's rule backwards → missing base → also breaks) — the single "mix these up" line covers both, since both errors have the same silent-truncation consequence |
| No design judgment | NB01–NB03 describe what the skill does and what to watch for; nothing rates whether the skill's documentation is well written |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that v1 is legacy or deprecated.** It's the correct, current choice
  for three specific jobs (search, upload, labels) — not a fallback for
  something broken in v2.
- **Not a full four-format breakdown.** Storage, ADF, view, and export_view
  are all real body formats in the source; this reel keeps only the one
  practical trap (ADF's double-parsed value field) a general viewer would
  actually hit.
- **Not a documentation-quality verdict.** NB03 states the same facts as the
  source's B05 "gets right/bites" teardown, but never frames them as a
  rating of the skill's own writing — see QUESTION.md's "Deliberately
  reframed, not new."

## Handoff prompt (BHTF, read aloud)

> "Search our Confluence space for pages about onboarding, then read the
> most recently updated match and summarize it for me. Before you show me
> anything from inside that page, tell me plainly whether you're giving me
> your own summary or quoting the page's own words."

Why it's worth running: it exercises the search-then-read path from NB01
and puts the NB03 safety rule to a direct test — whether Claude actually
distinguishes its own words from the page's, out loud, before answering.

---
**GATE P — signed:** ______________________  (human)
