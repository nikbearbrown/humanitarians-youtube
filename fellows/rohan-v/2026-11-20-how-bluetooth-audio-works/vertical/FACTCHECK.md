# FACTCHECK — How Bluetooth Audio Works

Status: claims checked 2026-11-19 by Claude (Claude Code) against `week-13/_research/facts-bluetooth.md`,
`evidence/run.log` and `evidence/results.json`, plus a web check of four claims the fact sheet does not cover, with
four claims (rows 10, 12, 15, 27) held UNVERIFIED until their narration was reworded (done in the 2026-11-19 re-voice); Rohan V.'s review of the 4K
finals still to come.

Every spoken claim, plus the on-screen strings of B00, B07 and B08 (B01–B06 visuals not built at check time, so
their narration only), its source, and its verdict. "The run" means `bluetooth.py` → `evidence/run.log` /
`evidence/results.json` / `evidence/scene.json`. Part 1 is **real encoders**: a synthetic pop track (drums, bass,
piano, a lead; 60 s, 44.1 kHz, 16-bit stereo; seeds 1119 and 77) encoded with ffmpeg's SBC (328k, the High Quality
setting), aptX, aptX HD and AAC (ffmpeg's own encoder at 256k, not Apple's), with data rates measured from the
encoded bytes; no quality score. Parts 2 and 3 are a **simulation** of an A2DP link (seed 2402), not a measurement
of any radio: 120 s; packets of 14.5 ms of music (5 SBC frames), one try every 3.75 ms (a 5-slot packet plus its
1-slot reply), each try on a randomly chosen channel of 79; a Wi-Fi network on channels 24–46 (23 of 79), busy 55%
of the time in bursts; 16 body-blocking moments of 60–320 ms (92% of tries lost); a 1% random error elsewhere;
failed tries re-sent until the packet is too late to play; the headphones play each packet a fixed buffer time after
its music began. **Nothing here is any company's code.** Facts with URLs and confidence levels:
`week-13/_research/facts-bluetooth.md`. Confidence: HIGH / MED as graded there; "measured" = a number from the run;
"web" = checked on 2026-11-19 (sources under the table). Verdicts: PASS, CORRECTED (changed after review), EXEMPT
(a drawing, not a claim); UNVERIFIED = held, blocks GATE F.

| # | Beat | Claim (as spoken / shown) | Source | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | B00 | Opening line "Hi, I am … and this video is about …" | `docs/FELLOWS-SUBMISSION.md` line 29 | — | PASS (verbatim) |
| 2 | B00 | AI narration disclosed | on screen "Narration: AI voice (Kokoro af_bella), script by Rohan V." + `metadata.ai_disclosure` | — | PASS |
| 3 | B00 | How music gets from your phone to wireless earbuds, and why it sometimes lags or cuts out; I built a small version. Screen: "How does music get to my wireless earbuds?", "squeeze the music to a quarter / hop between radio channels / keep a little music in reserve" | `bluetooth.py` parts 1–3; run: SBC "1/4.3 of CD" (rounded, row 7) | — | PASS |
| 4 | B01 | CD-quality stereo is about fourteen hundred kilobits every second | §3: 44,100 × 16 × 2 = 1,411,200 bit/s; run "1,411.2 kbit/s" | HIGH | PASS |
| 5 | B01 | That's more than Bluetooth's audio link can reliably carry, so your phone squeezes the music first | web: Classic Bluetooth EDR is 3 Mbit/s raw, about 2.1 Mbit/s actual maximum throughput, shared with re-sends and Wi-Fi; audio is sent compressed because of that limit. CD audio would fit on paper with little headroom, hence "reliably" | MED | PASS |
| 6 | B01 | The codec every device must support is called SBC | §2 (the one codec every A2DP device must support) | HIGH | PASS |
| 7 | B01 | On my test track, about three hundred and thirty kilobits: under a quarter | run: "SBC: 330.7 kbit/s measured from the encoded bytes = 1/4.3 of CD" (23%); §2–§3 (High Quality SBC 328 kbit/s, "about a quarter") **Re-voiced 2026-11-19:** "under a quarter" (23%). | measured | PASS (rounded) |
| 8 | B02 | Classic Bluetooth splits its band into seventy-nine channels and hops between them, up to sixteen hundred times a second | §1 (79 × 1 MHz, 2402 + k MHz; "a maximum hop rate of 1600 Hz"; multi-slot audio packets hop less often, which is why "up to") | HIGH | PASS |
| 9 | B02 | It shares that band with Wi-Fi | §1 (2.4 GHz ISM band) | HIGH | PASS |
| 10 | B02 | "In my simulation, a busy Wi-Fi network made seventeen percent of tries fail." | run: "without adaptive hopping: 22.1% of tries lost (17.4% outside the body-blocking moments)". The 22% includes the 16 body-blocking moments, which B02 never mentions: re-running `link()` with the same seeds, 26% of the failed tries fall inside them. The Wi-Fi share is 17%. Proposed fix under the table **Re-voiced 2026-11-19:** Wi-Fi-only figure (17.4%, outside the body-blocking moments); the HUD draws `loss_quiet`. | measured | CORRECTED |
| 11 | B02 | Adaptive hopping skips the busy channels | §1 (Bluetooth 1.2, 2003; drops busy channels such as Wi-Fi, keeps at least 20); in the run the hop set drops channels 24–46, leaving 56 | HIGH | PASS |
| 12 | B02 | "Adaptive hopping skips the busy channels: about one percent." | run: "with adaptive hopping: 7.6% of tries lost (0.9% outside the body-blocking moments)". 90% of those remaining failures happen during body blocking, so the residual "eight percent" is almost entirely not Wi-Fi. The Wi-Fi-related figure falls 17% → about 1% (the 1% random error I put in). Proposed fix under the table **Re-voiced 2026-11-19:** 0.9% outside the body-blocking moments (the 1% random error); HUD shows 0.9%. | measured | CORRECTED |
| 13 | B03 | Your phone and headphones agree on a codec | §2; web: Android's codec list is tried in an order the manufacturer sets, and both ends must support the codec | HIGH | PASS |
| 14 | B03 | SBC is the baseline | §2 (mandatory for every A2DP device) | HIGH | PASS |
| 15 | B03 | "Apple's devices prefer AAC." | §4 (iPhone + AirPods "limited to the Bluetooth AAC codec"); web: Apple devices support SBC and AAC and use SBC when the headphones lack AAC. As spoken it says Apple always uses AAC. Proposed: "Apple's devices prefer AAC." **Re-voiced 2026-11-19:** now "prefer"; HUD tag "APPLE DEVICES PREFER AAC". | MED | CORRECTED |
| 16 | B03 | Many Android phones also offer aptX, at about three hundred and fifty kilobits | web: since Android 8.0 the platform supports AAC, aptX, aptX HD and LDAC besides SBC (aptX needs the maker's licence, hence "many"); §4: 352 kbit/s at 44.1 kHz, 384 at 48 kHz; run "aptX: 352.8 kbit/s" | HIGH | PASS |
| 17 | B03 | … or LDAC, at up to nine hundred and ninety | §4 (Sony owner page: 330 / 660 / 990 kbps; 909 at 44.1 kHz). "Up to" honours don't-say 4 | HIGH | PASS |
| 18 | B03 | More data can sound better, but it's harder to send without gaps | §4 (phones rarely hold LDAC's 990); general statement, "can". The run does not test bit rate against dropouts | MED | PASS (general) |
| 19 | B04 | Lost packets, from Wi-Fi or your own body, get sent again | §5 (A2DP over L2CAP/ACL, retries up to a flush timeout); `link()` re-sends until the packet is too late to play **Re-voiced 2026-11-19:** names both causes the simulation has (Wi-Fi and body blocking), so B02's Wi-Fi-only numbers and B04's glitches agree. | MED-HIGH | CORRECTED |
| 20 | B04 | To ride that out, the earbuds keep a little music in reserve: a buffer | §5 (a bigger buffer lets a re-sent packet arrive before it must play) | MED-HIGH | PASS |
| 21 | B04 | In two minutes of my simulation, a 50 ms buffer glitched thirty times; 200 ms, three times; 300, never | run §3 (adaptive hopping on, 120 s): "50 ms: 30 glitches", "200 ms: 3 glitches", "300 ms: 0 glitches". A glitch = a run of consecutive late or missing packets | measured | PASS |
| 22 | B04 | That reserve is the main reason Bluetooth lags | §5 (buffering at each stage; the bigger buffer costs delay; "phrase simply"). The headphone buffer is the main cause, not the only one **Re-voiced 2026-11-19:** now "the main reason". | MED-HIGH | PASS (simplified) |
| 23 | B04 | "Listen: a small buffer, then a big one." | `mix_listen.py` PLAN for B04: small_buffer.wav (50 ms) then large_buffer.wav (200 ms), 1.5–5.5 s of the 6 s window each, unedited, level-matched only. Small clip: glitches at 2.07 s and 2.20 s into the clip, both inside one body-blocking moment; big clip: none (run: "200 ms buffer, 0 glitches") | measured | PASS |
| 24 | B05 | Real earbuds are often a couple of hundred milliseconds behind | §5 (SoundGuys: 308–369 ms averages on Android; RTINGS: 166–173 ms on one headset vs 7 ms wired); sheet's script wording "often a couple of hundred milliseconds" | HIGH | PASS |
| 25 | B05 | For videos, the headphones can report that delay, and the phone holds the picture back to match | §6 (AVDTP 1.3 Delay Reporting; Android, merged Feb 2018; iOS since 8.2, "used to improve audio/video synchronization"). "Can" covers devices and apps that don't **Re-voiced 2026-11-19:** shortened; same claim. HUD: "170–370 ms · TWO PUBLISHED TESTS" (RTINGS 166–173, SoundGuys 308–369 averages). | HIGH / MED-HIGH | CORRECTED |
| 26 | B05 | A game can't hold back your button presses, so games can feel laggy | follows from rows 24–25: holding the picture back would add input delay | — | PASS (reasoning) |
| 27 | B06 | "Bluetooth's next generation, LE Audio, brings a new codec called LC3." | §7 (LE Audio, CES 2020, on Core 5.2, with LC3): the codec is right. But LE Audio is not a *version* of Bluetooth. Versions are Core 5.2 and later (6.x now), so "the newest version" tells the viewer LE Audio is the latest Bluetooth version. The SIG calls it "the next generation of Bluetooth audio". Proposed: "Bluetooth's next generation, LE Audio, brings a new codec called LC3." **Re-voiced 2026-11-19:** SIG wording ("next generation"). | HIGH | CORRECTED |
| 28 | B06 | The Bluetooth SIG says it beats SBC even at half the bit rate | §7 (SIG release: improvements over SBC "even at a 50% lower bit rate"); attributed to the SIG as the sheet asks | HIGH (as attributed) | PASS |
| 29 | B06 | Its broadcast feature, Auracast, lets one phone or TV stream to any number of earbuds nearby | §7 (Auracast broadcast audio, named in the July 2022 announcement); web, SIG Auracast pages: an unlimited number of in-range Auracast receivers can join one broadcast; sources include phones and TVs. Receivers must support Auracast. No date spoken (don't-say 5) | HIGH | PASS |
| 30 | B07 | Keep your phone close | advice; in the run, nearly all glitches with adaptive hopping on come from body blocking (row 12) | — | PASS (as advice) |
| 31 | B07 | Pick a better codec if your phone offers one | §4; row 18's caveat applies | — | PASS (as advice) |
| 32 | B07 | Use your earbuds' game mode for games | advice; no latency figure claimed for game modes (aptX Low Latency's 40 ms is not implied, don't-say 3) | — | PASS (as advice) |
| 33 | B07 | Screen: title "Better Bluetooth Sound", lede "Squeezed, hopped and buffered, every time you press play.", steps "Keep your phone close." / "Pick a better codec if offered." / "Use game mode for games.", spark "A quarter of the data, a little delay." | summary of B01–B05; "a quarter" as row 7 | — | PASS |
| 34 | B08 | "Squeeze it, hop around the noise, and keep a little in reserve." | summary of B01, B02, B04 | — | PASS |
| 35 | B08 | Screen: "How Bluetooth Audio Works", "@HumanitariansAI", "Rohan V." | title card | — | EXEMPT (title card) |

Web sources (2026-11-19): EDR throughput, electronics-notes.com "Bluetooth 2 with Enhanced Data Rate, EDR" and
Cambridge Wireless "The irresistible rise of Bluetooth audio"; Apple's SBC fallback, SoundGuys "Bluetooth codecs
ultimate guide" and Tom's Guide; Android codecs, https://source.android.com/docs/core/connect/bluetooth/services ;
Auracast receivers, https://www.bluetooth.com/auracast/how-it-works/ and the SIG's "An Overview of Auracast" paper
(search extracts: bluetooth.com refuses automated fetching, as the fact sheet notes).

## Fixed in the re-voice (2026-11-19; rows 7, 10, 12, 15, 19, 22, 25, 27 now CORRECTED)

- **Rows 10 and 12 (B02).** Current: "In my simulation, with a busy Wi-Fi network nearby, twenty-two percent of
  tries failed. Adaptive hopping skips the busy channels, and failures fell to under eight percent."
  Proposed (Wi-Fi only, the run's "outside the body-blocking moments" figures): "In my simulation, with a busy Wi-Fi
  network nearby, seventeen percent of tries failed. Adaptive hopping skips the busy channels, and failures fell to
  about one percent." Cues `twenty` → "seventeen" and `eight` → "about one" in `cues.json`, and the B02 scene must
  draw `loss_quiet`, not `loss`.
  Alternative that keeps the current numbers: "In my simulation, with busy Wi-Fi and a phone in a pocket, twenty-two
  percent of tries failed. Adaptive hopping skips the busy channels, and failures fell under eight percent."
- **Row 15 (B03).** "Apple's devices use AAC." → "Apple's devices prefer AAC." Cue `aac` "use AAC" → "prefer AAC".
- **Row 27 (B06).** "The newest version, LE Audio, brings a new codec called LC3." → "Bluetooth's next generation,
  LE Audio, brings a new codec called LC3." Cue `le` ("LE Audio") still resolves.

Change each verdict to CORRECTED once the audio is regenerated, aligned and re-synced.

## Arithmetic, checked separately

- **CD and the codecs.** 44,100 × 16 × 2 = 1,411.2 kbit/s. SBC: 1,411.2 ÷ 330.7 = 4.27, i.e. 23%; "a quarter"
  rounds up, as the fact sheet's "about a quarter" does (nominal High Quality SBC 328 kbit/s; ffmpeg's bytes, frame
  headers included, give 330.7). aptX is a fixed 4:1: 44,100 × 16 × 2 ÷ 4 = 352.8 exactly. aptX HD: 44,100 × 24 × 2 ÷
  4 = 529.2 (its 576 is at 48 kHz). AAC 272.1 kbit/s is not spoken (ffmpeg's encoder, set to 256k).
- **The link's clock.** 640 samples ÷ 44,100 = 14.5 ms of music per packet, 68.9 packets/s. One try = 6 slots ×
  625 µs = 3.75 ms, 267 tries/s, so the link has spare tries for re-sends, and it hops 267 times a second here (the
  "up to 1,600" is for single-slot packets).
- **Where the failures come from.** Wi-Fi alone predicts 23/79 × 55% ≈ 16.0%, plus the 1% random error ≈ 17%; the run
  finds 17.4% outside body blocking. With adaptive hopping the Wi-Fi channels are never used, and 0.86% remains, the
  1% random error. The body-blocking moments total 2.63 s (2.2% of the 120 s), but 674 tries fall inside them (6.3% of
  all tries without adaptive hopping, 7.5% with), because the link re-sends back to back there, and 92% of them fail.
  So they are 26% of all failed tries without adaptive hopping and 90% with it. (Checked by re-running `link()` with
  the program's own seeds from a scratch script; it reproduces 22.14% and 7.62%.)
- **The buffer.** A packet's music starts at t, it can leave at t + 14.5 ms and arrive at t + 18.3 ms at the earliest,
  and it plays at t + buffer. A 20 ms buffer leaves 1.7 ms of slack for re-sends, hence 103 glitches; at 300 ms even
  the longest body-blocking moment (320 ms at 92% loss) is ridden out.
- **The listening clips.** The 6 s window is 2.0–8.0 s of the track, picked as the stretch whose 50 ms glitch rate is
  closest to the average (2 vs 1.5 expected). `mix_listen.py` plays 1.5–5.5 s of it. Both small-buffer glitches
  (3.573 s and 3.703 s into the window) sit inside the body-blocking moment at 3.575–3.777 s, so they are heard as one
  stutter; `mix_listen.py`'s docstring calls it "one dropout, at 2.1 s".

## Not claimed

- That the radio, Wi-Fi traffic, body blocking or buffer numbers are measurements of real earbuds. They are a
  simulation with parameters I chose.
- Any quality ranking of the codecs: no listening test, and a waveform match is unfair to perceptual codecs.
- "SBC maxes out at 345 kbps", "Apple uses 256 kbps AAC", "aptX LL gives your phone 40 ms", "LDAC is lossless / always
  990", "Auracast was announced at CES 2020", "exactly 1,600 hops a second" (the sheet's don't-say list).
- That ffmpeg's AAC encoder is Apple's, or that its 272 kbit/s is what an iPhone sends.
- How much a game mode reduces latency.
