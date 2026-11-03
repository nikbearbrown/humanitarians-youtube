# FRICTIONAL — Prove Nothing Broke.

- **Folder:** `2026-10-19-jboss-migrator-overview` · reporting week **2026-10-19 → 2026-10-25**
- **Dates inside this folder's artifacts:** design notes pasted, built and QC'd 2026-10-28
  (after the reporting week — see the README evidence index)
- Append dated entries below; never rewrite an earlier one.

---

## Entry — week of 2026-10-19 · written later, on 2026-10-28

> Reconstructed from the files in this folder on the day the reel was built.
> Drafted with Claude Code from those files; reviewed and confirmed by Mohammed on 2026-10-28.

**1. Date and what I was working on**
- A 3:35 reel presenting the *design* of a JBoss migrator: move a JBoss EAP 7.2 app on Java 8
  to EAP 8 on Java 17, and prove the migration never touched business logic or the UI.
  It is a design, not a shipped tool, and B00 says so.

**2. What I tried, and what I expected**
- A six-stage pipeline built from real tools:
  - Red Hat MTA (Konveyor) to inventory mandatory / optional / potential issues;
  - OpenRewrite recipes (`UpgradeToJava17`, `JakartaEE10`, `MigrateToHibernate61`,
    `JUnit4to5Migration`) for lossless code edits;
  - Eclipse Transformer for `javax → jakarta` in third-party jars;
  - JBoss CLI scripts or the WildFly Server Migration Tool to regenerate server config;
  - an LLM step that only *proposes* fixes;
  - characterization tests plus a diff guard that fails the run if protected code changes.
- Expected the masters to pass the house gate this time.

**3. Where it resisted, and what I did next**
- Preview stills caught layout defects before the 4K render: holes in the portrait annotation
  grid (B02), empty pipeline cards (B03), dead space in the log/test cards (B04), a clipped
  "MANDATORY" pill (B05), small type (B06–B08), and a truncated recipe column (B08).
  All fixed before rendering.
- **Same gate conflict as the Cortex and snowshift reels:** B01 is a typing beat, so it is
  mostly empty at the 50% / 85% samples. `compile.py` refused both aspects
  (`build-state.json`, 2026-10-28 20:02 and 21:01). The masters were joined from the
  compiler's own clips and have **not** passed `./art final`.

**4. What Claude or another person contributed — accepted, changed, rejected**
- Claude built the reel and QC from my design notes.
- Kept the source's "honest limits" un-softened: custom security modules, vendor-specific
  JNDI lookups and Seam need a human. No completion percentage is claimed.
- `QC-STATUS.md` records that I had not reviewed the cut at build time; I reviewed it afterwards
  on 2026-10-28.

**5. What I understand now, and what I still do not**
- Understood: tools migrate the mechanics; the proof that nothing broke has to come from
  characterization tests and a diff guard, not from the build going green.
- Started the code the same evening: [`55c4dcb`](https://github.com/mdhussainshariff/mycroft-nikbearbrown/commit/55c4dcb)
  "Add jboss-migrator: config-driven JBoss EAP upgrade orchestrator" on branch `jboss-migrator`.
- Open: the OpenRewrite recipe package paths still need confirming. The B07 `pass → pass`
  results in the video are illustrative; the migrator has not yet been run on an application.

**Evidence in this folder**
- [`QC-STATUS.md` — Gate V and frame review, 2026-10-28](QC-STATUS.md) · [`build-state.json`](build-state.json) · [`vertical/build-state.json`](vertical/build-state.json)
- [`FACTCHECK.md` — tool facts and illustrative labels](FACTCHECK.md) · [`CHECKS-REPORT.md`](CHECKS-REPORT.md) · [`PROMPTS.md`](PROMPTS.md)
- [`compile-16x9.log`](compile-16x9.log) · [`render-16x9.log`](render-16x9.log)
- Masters: [16:9](https://drive.google.com/file/d/1x3qaq8DK7e7wsPWpLcXuouCnvzPYp0fU/view) · [9:16](https://drive.google.com/file/d/1Euh_WxXFnlUjKojfC_dcBpj-wUq53xZO/view)
- Code: [branch `jboss-migrator`](https://github.com/mdhussainshariff/mycroft-nikbearbrown/tree/jboss-migrator)
