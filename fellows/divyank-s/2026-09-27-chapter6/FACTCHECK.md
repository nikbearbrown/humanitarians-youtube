# FACTCHECK — Claude, Packaged. (Chapter 6 — Export to Canvas)

Source: `ai1-cli/chapters/06-export-to-canvas.md` (read in full), cross-checked
against `ai1-cli/research/06-export-to-canvas.md` and the actual
`build-canvas.sh` script in the repo.

| # | Claim | Tag | Note |
|---|---|---|---|
| 1 | `.imscc` is a Common Cartridge package — a ZIP archive with an XML manifest | Cited | Chapter body + research doc, citing 1EdTech's own Common Cartridge spec |
| 2 | The standard comes from 1EdTech, formerly IMS Global (renamed 2022) | Cited | Chapter footnote [^cc]; research doc §A notes the 2022 rebrand explicitly |
| 3 | Current implementation profile is v1.3; importers also accept v1.0–1.2 | Cited | Chapter body + research doc §A |
| 4 | Common Cartridge is importable by Canvas, Moodle, Blackboard, and other conforming LMSs | General/stable | The chapter's own interoperability claim; these are the standard's actual adopters, not a promotional endorsement |
| 5 | `build-canvas.sh` is a thin wrapper around `build-imscc-standard.py` | General/stable | Verified directly — read the actual `build-canvas.sh` in this repo; it is a 7-line wrapper that execs `build-imscc-standard.py "$@"` |
| 6 | Renaming `.imscc` to `.zip` lets you inspect the manifest and resource folders directly | General/stable | A ZIP-format fact, stated in the chapter as a worthwhile exercise |
| 7 | Worked example: a signed plan sequenced *Foundations → Voice-of-Customer → Offers → Sales Page*; an import landed the modules alphabetically, *Offers* before *Foundations* | Cited | The chapter's own worked example, used verbatim |
| 8 | An import can finish without error and still show an empty course if resources never linked in the manifest | Cited | The chapter's own "what can go wrong" table, row 2 |
| 9 | Module order carries real pedagogy — the only reliable check is against the signed `architecture.md`, not memory | Cited | The chapter's own "what can go wrong" table, row 3, plus its closing argument |

## Explicitly excluded

- Any claim about current Canvas/Moodle/Blackboard product versions, pricing,
  or UI specifics — the chapter itself boxes the import-UI details as
  "perishable" and says to treat them as an intent, not a fixed spec.
- No benchmark numbers or market-share claims about any LMS.
- No claim that this reel's own `build-canvas.sh` run was actually executed
  against a live LMS this session — the video narrates the chapter's method
  and its own worked example, not a fresh run.
