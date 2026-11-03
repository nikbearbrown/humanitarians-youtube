# SOURCES — The Constraint Isn't Speed

A topic explainer on the emergence of 6G and its pros and cons for IoT. 6G is a
forward-looking subject where most coverage is vendor projection, so the reel
reports only what a named standards body or a named forecast says, and labels
forecasts as forecasts.

| On screen | Beat | Source |
|---|---|---|
| six IMT-2030 usage scenarios, three inherited and three new | B03 | ITU-R IMT-2030 framework recommendation |
| immersive / massive / hyper-reliable low latency (inherited) | B03 | same — carried from the IMT-2020 scenarios |
| ubiquitous connectivity / AI and communication / integrated sensing (new) | B03 | same |
| Rel-21 begins normative 6G work | B03 | 3GPP Release 21 |
| Stage-3 protocol specs Dec 2028 · ASN.1/OpenAPI freeze Mar 2029 | B03 | 3GPP Release 21 timeline |
| first commercial systems ~2030 | B01, B03 | 3GPP/ITU-R schedule; Ericsson states specs ready end-2028 enabling first commercial systems by 2030 |
| ambient IoT device 1 — ~1 µW peak, no amplifier, no carrier generator, backscatters an external CW | B04 | 3GPP ambient IoT study (Rel-19) |
| ambient IoT device 2 — a few hundred µW, amplifier + internal CW generator | B04 | same |
| battery-free, harvesting radio / thermal / solar | B04 | same |
| Rel-19 study and work item; Rel-20 extends to higher-power device types | B04 | 3GPP |
| connection density 10⁶–10⁸ devices/km², 1–100× IMT-2020 | B05 | ITU-R IMT-2030 framework |
| integrated sensing — the network as instrument | B05 | ITU-R IMT-2030, ISAC usage scenario |
| 2030 mix: 60% 4G/5G broadband IoT, 40% NB-IoT + LTE-M | B07 | Ericsson Mobility Report, IoT connections forecast |
| over 7 billion cellular IoT connections by 2030 | B07 | same (~11% CAGR) |
| NB-IoT and LTE-M introduced 2015–2017 | B07 | Ericsson — the two 3GPP massive-IoT technologies, introduced between 2015 and 2017 |

## Reference links

- ITU-R IMT-2030 — https://www.itu.int/en/ITU-R/study-groups/rsg5/rwp5d/imt-2030/pages/default.aspx
- 3GPP Release 21 — https://www.3gpp.org/specifications-technologies/releases/release-21
- 3GPP Release 19 Ambient IoT — https://www.3gpp.org/technologies/rel19-aiot
- Ericsson Mobility Report, IoT connections outlook — https://www.ericsson.com/en/reports-and-papers/mobility-report/dataforecasts/iot-connections-outlook

## Precision notes

- **"~2030" is always spoken as approximate.** No date beyond the 3GPP
  milestones is stated as fixed, because deployment dates are not standardised.
- **The 2030 connection mix is a forecast**, and the reel says "projects" and
  "forecast", never "will be".
- **"a few hundred µW"** is the study's own phrasing for device 2, not a
  rounded figure I chose.
- **Network-side energy** is described qualitatively (denser cells, more radio
  chains, wideband processing) because no single authoritative figure exists
  for 6G network energy; no number is put on screen for it.

## Claims deliberately NOT made

- **No peak-data-rate or latency figure for 6G.** They exist in the framework,
  but the reel's whole argument is that they are not the binding constraint for
  IoT — quoting them would undercut the point and date the reel.
- **No claim that 6G will or will not succeed.** The verdict is scoped to IoT
  deployment decisions.
- **No vendor product claims**, and no named chipset, operator or launch.
- **No spectrum-band specifics.** Band allocation is still in progress; stating
  it would be stating a moving target as settled.
- **No claim that 5G "failed".** The reel uses the 2030 forecast as evidence
  about adoption drivers, not as a verdict on a previous generation.
