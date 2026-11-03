# QUESTION.md — skills--claude-liam-webapp-testing

**Question (redo, per SUBJECT.json `mode: "redo"`):** Is a web page that has
"loaded" already the same moment as a page that's actually ready to test?

**Source:** `anthropics/skills/youtube/claude-liam-webapp-testing/beat_sheet.json`
(Teardown, `claude-liam-webapp-testing`, examining Anthropic's `webapp-testing`
skill — already fully built, 7 filled beats). Question, facts, and body
argument carried over; narration re-registered to Plain (explain, then stop,
no verdict); cold open replaced with `BrutalistHesitantWriter`; close carries
the Humanitarians AI skin.

**Fact-currency note:** the source skill file logged in the source sheet's
metadata (`../anthropics/skills/skills/webapp-testing/SKILL.md`) could not be
located at that path on this machine — `find` across `anthropics/skills/`
turns up only the built `youtube/claude-liam-webapp-testing/` reel folder,
not a `skills/webapp-testing/` source directory. Same seam already logged on
the `docx`, `claude-api`, and `mcp-builder` siblings (skills tree reorganized
since these sources' 2026-07-18 builds). Per the redo contract, facts are
carried over unchanged from the locked source script (`beat_sheet.json`'s
`narration_text` fields) rather than re-verified against a live file that
could no longer be found.

**Facts carried from the locked source script:**
- Two branches: static HTML (read the file directly, script against a
  `file://` URL) vs. dynamic web app (needs a running server).
- Dynamic branch, server not yet running: `with_server.py --help` first,
  then start the server through the helper and write a Playwright script
  alongside it.
- Dynamic branch, server already running: go straight to
  reconnaissance-then-action.
- Reconnaissance-then-action, three steps: navigate and wait for
  `networkidle`; screenshot or inspect the rendered DOM; identify selectors
  from what actually rendered, then act.
- The critical rule: never inspect the DOM before waiting for `networkidle`
  on a dynamic app — inspect too early and the DOM shows placeholder
  elements, not real content.
- `with_server.py` manages the server lifecycle so the automation script
  holds only Playwright logic. One server: `--server` + `--port`. Two
  servers (backend + frontend): pass `--server` twice.
- Playwright pattern: `sync_playwright`, headless Chromium,
  `wait_for_load_state('networkidle')` before any DOM operation, close the
  browser when done. Prefer descriptive selectors (text, role, CSS, id) over
  absolute XPath.
- Three example scripts ship with the skill: `element_discovery`,
  `static_html_automation`, `console_logging`.
- Source's own teardown: gets right — recon-and-action framing, precise
  decision tree, the `networkidle` warning is the single most important
  piece, `with_server.py` removes lifecycle boilerplate, three example
  scripts ship. Bites — no error-recovery guidance, examples directory
  referenced but undescribed, `--help` given with no sample output, no
  auth/session guidance, no CI/headless notes.

**Carried-over anchor scenario** (used in the source's own BHTF handoff, now
planted and paid off inside the body instead): a local React app on port
3000 — click Submit on a login form, verify a success message appears.
