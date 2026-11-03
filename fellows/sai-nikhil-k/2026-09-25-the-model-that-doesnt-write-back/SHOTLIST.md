# SHOTLIST — The Model That Doesn't Write Back

Typed work order. Eleven beats, two deliverables (16:9 and the full-length
9:16), **no open slots**. Eight beats are registered Remotion compositions; three
(B01, B03, B06) are photo plates built by `make_plates.py` from freely licensed
Wikimedia Commons photographs. Nothing is generated, purchased or awaiting a key.

| Beat | Act | Lane | Asset | Motion | In 9:16? |
|---|---|---|---|---|---|
| B00 | ASK | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B01 | FAST THINKING | archival photos | `make_plates.py` · hero+2 · 3 photos | staged reveal + 2% push | yes → `pantry/B01-916.mp4` (re-composed) |
| B02 | TWO KINDS | remotion | `DivergentFates` | illustrate | yes → `DivergentFates916` |
| B03 | THREE QUESTIONS | archival photos | `make_plates.py` · triptych · 3 photos | staged reveal + 2% push | yes → `pantry/B03-916.mp4` (re-composed) |
| B04 | WHAT 0.8 MEANS | remotion | `TypesetMath` | illustrate | yes → `TypesetMath916` |
| B05 | FAST AND CHEAP | remotion | `ExecutedData` | illustrate | yes → `ExecutedData916` |
| B06 | WHAT IT ISN'T FOR | archival photos | `make_plates.py` · grid2x2 · 4 photos | staged reveal + 2% push | yes → `pantry/B06-916.mp4` (re-composed) |
| B07 | THE FAIR QUESTION | remotion | `BinaryBranch` | illustrate | yes → `BinaryBranch916` |
| B08 | VERDICT | remotion | `ClaudeVerdictArtifact` | illustrate | yes → `ClaudeVerdictArtifact916` |
| B09 | HANDOFF | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B10 | OUTRO | remotion | `LogoOutro` | illustrate | yes → `LogoOutro916` |

## The photographs (10)

Every file was fetched by `evidence/commons_fetch.py`, which refuses anything
that is not public domain, CC0, CC BY or CC BY-SA and writes a license sidecar
(`images/src/<slug>.json`: title, page, license, author, sha256, fetch time).
Reveal = when the photo fades in, cued to the word that names it.

| Beat | File | On-screen caption | License | Author | Source page | Reveal |
|---|---|---|---|---|---|---|
| B01 | `images/src/sw_jber_1950.jpg` | Operators connect calls | Public domain | David Bedard | https://commons.wikimedia.org/wiki/File:JBER_telephone_operators_connect_calls,_people_120124-A-ZY202-001.jpg | 0.00s |
| B01 | `images/src/sw_signal_corps.jpg` | One plug, one line, in a moment | Public domain | Lt. Fox, United States Army Signal Corps | https://commons.wikimedia.org/wiki/File:SC-49623_Signal_Corps_telephone_operators_at_switchboard.jpg | 5.21s |
| B01 | `images/src/kahneman.jpg` | Daniel Kahneman — “System 1”: fast, intuitive | CC BY-SA 2.0 | nrkbeta | https://commons.wikimedia.org/wiki/File:Daniel_Kahneman_(3283955327).jpg | 15.53s |
| B03 | `images/src/mail_sorting.jpg` | Choice — which option fits? | CC0 | Hadi | https://commons.wikimedia.org/wiki/File:Briefzentrum_H%C3%A4rkingen_11.jpg | 0.00s |
| B03 | `images/src/dalat_dials.jpg` | Score — where on your scale? | CC BY-SA 3.0 | Dragfyre | https://commons.wikimedia.org/wiki/File:Da_Lat_locomotive_dials.JPG | 5.28s |
| B03 | `images/src/rail_switch.jpg` | Noul — is this true? yes or no | CC0 | PIVISO | https://commons.wikimedia.org/wiki/File:Hand-operated_railroad_switch.jpg | 8.88s |
| B06 | `images/src/arithmometer.jpg` | Not a calculator — do the math in code | Public domain | MKFI | https://commons.wikimedia.org/wiki/File:Arithmometer_1860.JPG | 0.00s |
| B06 | `images/src/calendar_1914.jpg` | Reads dates as text — not as dates | Public domain | Unknown authorUnknown author | https://commons.wikimedia.org/wiki/File:1914-julian-gregorian-calendar-Greek-French.jpg | 6.54s |
| B06 | `images/src/trojan_horse.jpg` | Can be steered — by instructions hidden in the input | Public domain | Giovanni Domenico Tiepolo | https://commons.wikimedia.org/wiki/File:The_Procession_of_the_Trojan_Horse_in_Troy_by_Giovanni_Domenico_Tiepolo_(cropped).jpg | 8.81s |
| B06 | `images/src/typewriter.jpg` | Doesn't write — it only answers | Public domain | Department of the Interior. U.S. Fish and Wildlife Service.  | https://commons.wikimedia.org/wiki/File:Antique_Remington_typewriter_-_DPLA_-_2d0970de25ad0e1e4de9d2b410a36556.jpg | 11.64s |

No photograph is retouched, recoloured or composited into another. Each is
cover-cropped into its cell at a focus point chosen by looking, except the 1914
calendar, which is shown whole. `compile.py`'s archival desaturation is switched
off (`shot.treatment: "none"`) so the colour photographs stay in colour.

**Ordering hazard:** `remotion_scenes.py` writes its start-of-run copy of
`beat_sheet.json` back after every render. Never edit the sheet (or run
`build_beats.py`) while a render is in flight.
