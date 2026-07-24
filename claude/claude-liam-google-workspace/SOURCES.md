# SOURCES — claude-liam-google-workspace ("Claude, Grounded.")

Source: Bear Brown research prompt "Claude + Gmail / Google Workspace."
ai-explainer (standard middle; NOT skill-teardown). Audio: Kokoro af_kore
(free, local), generated 2026-07-18 in the Cowork cloud session; durations
are ground truth.

## Web-verified against the LIVE Anthropic doc (DOUBLE-CHECK LAW)

Primary source: support.claude.com, "Use Google Workspace connectors"
(fetched 2026-07-18). The two most-datable claims, confirmed verbatim:

| Claim (beat) | Verdict | Exact wording pulled |
|---|---|---|
| Gmail draft-only, CANNOT send (B00, B02, B05, BVDT) | CONFIRMED | "Claude creates drafts in your Gmail account, but cannot send emails on your behalf"; "all emails must be sent manually through your Gmail account" |
| Calendar full read/write — create/update/delete (B02, B05) | CONFIRMED | Create, update, delete events; find mutual availability; manage attendees; recurring meetings |
| Drive beyond search — upload, folders, permissions, save output (B05) | CONFIRMED | Upload any file type; create folders; view permissions; "Save Claude-generated files directly to your Drive"; "extracts text content only … Images embedded in documents are not processed" |
| Training carve-out (B07, BVDT) | CONFIRMED verbatim | "We do not train our models on your Gmail, Drive, or Calendar connector data"; consumer copy-paste "may be used to improve our models" if opted in |
| Availability: all individual users; Team/Enterprise Owner enables first (B01, B06) | CONFIRMED | "Available for all Claude and Claude Desktop users"; "An Owner or Primary Owner must enable these connectors at the organization level before individual users can authenticate" |

Corroboration on the send boundary: an open `anthropics/claude-code`
GitHub feature request (#28575) asks to ADD a `gmail_send_draft` tool —
i.e. send does not currently exist. (Consumer-web search, 2026-07-18.)

## From the source doc (faithful paraphrase)

- The consent-scope confusion (B03): Google's OAuth screen lists a
  send-email scope Claude requests but never exercises — source Part "A
  second, quieter hook." Narration frames it as "granted ≠ used" and does
  NOT assert Claude can send.
- Work-account "Access blocked" fix via Google Admin console → mark Claude
  Trusted → ~15 min propagate (B06) — source Part 2.
- Known limitations: attachment metadata not content, some advanced Gmail
  filters unsupported, multi-call complex queries, Google rate limits,
  Drive text-only / no Doc comments (B08) — source Part 1 + Part 4.
- Handoff prompt (BHTF) — tightened from source's Standalone Copyable
  Prompt; points Claude at support.claude.com to re-verify.

## Datable specifics handled (DOUBLE-CHECK LAW — re-verify before record)

- Exact Google Admin console menu path + the ~15-min propagation window
  (B06): narrated at a level of generality that survives a menu rename;
  the precise path is in the BUILD-PROMPT for the on-screen card but flag
  it against the live doc before recording.
- Enterprise-managed-auth beta connector list (Asana/Atlassian/… not
  Google) and per-tool permission controls: source Part 3, admin-facing —
  DELIBERATELY LEFT OUT of this cut (source marks it a cuttable bonus
  segment; it dates fast). Not on screen.
- "May 22, 2026 last-updated" doc date: not put on screen as a headline;
  the doc is cited by name, not by a date that will look stale.

## Ethical / accuracy framing

- The whole reel's purpose is preventing an overclaim ("it can send / your
  email is used for training"). It states the send boundary and the
  training carve-out precisely and warns on camera against the flattened
  versions. BHTF makes the viewer verify against the live source — the
  video explicitly tells them not to trust it over the docs.

## Currency note

Connector capability boundaries (especially Gmail send) change; re-verify
against the live support article immediately before recording. Source's
own closing note.
