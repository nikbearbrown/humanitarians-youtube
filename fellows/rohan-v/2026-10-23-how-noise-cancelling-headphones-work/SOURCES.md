# SOURCES — How Noise-Cancelling Headphones Work

Full notes, confidence levels and the "do not say" list: `week-09/_research/facts-anc.md`. Checked 2026-10-23.

## Principle and history

- P. Lueg, "Process of silencing sound oscillations," US Patent 2,043,416, 1936. Anti-phase cancellation. B01.
- H. F. Olson & E. G. May, "Electronic Sound Absorber," *JASA* 25(6):1130–1136, 1953. Background.

## How headphones do it

- Rivera Benois et al., overview of ANC headphone architectures (feedforward, feedback, hybrid), 2018; IEEE
  WASPAA 2023 paper on speech and ANC. B02, B04.
- Apple support: AirPods use outward- and inward-facing microphones. B02.
- Sony headphone manual: noise cancelling works primarily on low-frequency noise. B00, B05.
- National Research Council of Canada (1993): ANC most effective below about 1 kHz. B05 background.
- B. Widrow & M. E. Hoff, adaptive switching circuits (LMS), 1960 WESCON record; S. M. Kuo & D. R. Morgan,
  *Active Noise Control Systems*, 1996 (filtered-x LMS; standard reference). B02.

## Passive isolation and listening

- DAGA 2019 (HEAD acoustics) and *Canadian Acoustics* 2002: passive isolation works mostly above ~200 Hz; ANC and
  passive together cover the range. B05.
- World Health Organization, safe listening guidance (page dated Mar 2026): well-fitted noise-cancelling
  headphones so you don't need to raise the volume. B06.

## Evidence

- `anc.py`, `export_anc_data.py` and `evidence/` in this folder.
