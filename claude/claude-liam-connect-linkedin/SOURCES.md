# SOURCES — claude-liam-connect-linkedin ("Claude, Gated.")

Source: Bear Brown research prompt "How to Connect Claude to LinkedIn."
ai-explainer (standard middle; NOT skill-teardown — source is a research
doc, not a SKILL.md). Audio: Kokoro af_kore (free, local), generated
2026-07-18 in the Cowork cloud session; durations are ground truth.

## Web-verified before scripting (DOUBLE-CHECK LAW)

| Claim (beat) | Verdict | Sources |
|---|---|---|
| hiQ v. LinkedIn settled Dec 2022, ~$500K, algorithms destroyed (B06) | CONFIRMED | Proskauer, Morgan Lewis, Privacy World, Wikipedia (hiQ Labs v. LinkedIn) |
| 9th Cir. (Apr 2022): scraping public/no-login data ≠ CFAA violation (B06) | CONFIRMED | Same case coverage; well-established precedent |
| No public LinkedIn API for connection requests / DMs on an ordinary account (B03, B04) | CONFIRMED | Every tool advertising it (LinkUp, HeroHunt, LinkedHelper) is the unofficial 3rd-party category the video warns about; LinkedIn's official messaging API is org/partner-gated |

## Verbatim / near-verbatim from the source doc

- "Anthropic … remote MCP servers are third-party services it doesn't own,
  operate, or endorse — reviews Directory listings against basic criteria
  but doesn't security-audit any given server" (B01) — Anthropic MCP docs,
  paraphrased faithfully.
- The three-job split (Publishing / Analytics / Outreach) and the
  asymmetry (B02–B03) — the source's Part 1 thesis.
- API surface details (B04) — source Part 1 table (Share on LinkedIn
  self-serve; Community Management API audit: verified domain, business
  email, corporate registration, OAuth screen recording).
- Cookie replay: li_at + JSESSIONID → internal Voyager API (B05) —
  source Part 2.
- Vendor red flags: send caps, randomized timing, multi-account rotation
  (B07) — source Part 2.
- Publishing setup + POST /rest/posts call (B08–B09) — source Part 3.
- Handoff prompt (BHTF) — tightened from source's "Standalone Copyable
  Prompt."

## Datable specifics deliberately handled (DOUBLE-CHECK LAW: strip what dates)

- "6,000+ extension signatures" — source claim, unverifiable; narrated as
  "extension signatures" with NO on-screen number.
- `Linkedin-Version: 202606` header — real but drifts; DROPPED from the
  on-screen curl (B09). Re-verify the current version at build time.
- OpenID Connect migration (Aug 2023; r_liteprofile/r_emailaddress
  deprecated) — context only, not an on-screen headline.
- souravdasbiswas/linkedin-mcp-server named in the source as one concrete
  official-API-only example; on screen the B08 command is generic
  (`claude mcp add linkedin … node …/dist/index.js`) to avoid endorsing/
  dating one specific third-party repo. Re-verify its scope handling at
  build time before recommending it by name.

## Ethical framing (crutch-vs-scaffold)

- The reel teaches viewers to RECOGNIZE and AVOID cookie-replay / outreach
  tools and to use the official path or human-sent outreach. Detection
  facts (B05) are framed as a consumer warning ("undetectable is the
  tell"), never as an evasion how-to. Verdict lands on the compliant /
  manual default (BVDT). No step in the video automates outreach or
  instructs on defeating LinkedIn's detection.

## Currency note

LinkedIn approval processes, API versions, and the unofficial-MCP
landscape shift often. Re-verify Community Management approval
requirements and any named MCP server's current scope handling at build
time (source's own closing note).
