# SOURCES — How Bluetooth Audio Works

Full notes, confidence levels and the "don't say" list: `week-13/_research/facts-bluetooth.md`. Checked
2026-11-19. bluetooth.com, Business Wire and TechPowerUp refused automated fetching, so the Bluetooth SIG's wording
comes from search-engine extracts of its pages or press text quoted by reputable outlets; pages marked "read" were
read in full on the owner's own site.

## Too much data

- CD quality: 44,100 × 16 bits × 2 channels = 1,411,200 bit/s (Red Book arithmetic). B01.
- Wikipedia, "SBC (codec)": SBC is the one codec every A2DP device must support; the "High Quality" setting is
  328 kbit/s at 44.1 kHz (345 at 48 kHz), the default on most systems. <https://en.wikipedia.org/wiki/SBC_(codec)>.
  B01, B03.
- Bluetooth SIG, A2DP implementation conformance statement: SBC mandatory; AAC, MPEG-1/2 and ATRAC optional.
  <https://files.bluetooth.com/download/a2dp-ics-p16ed3-pdf>. B01, B03.
- A BlueZ (Linux Bluetooth) patch discussion on SBC bitpools, on the linux-bluetooth mailing list (2019). URL in
  the fact sheet (§2); left out here because it contains a contributor's name. Background; not stated.

## The radio

- Bluetooth SIG, technology overview: Classic Bluetooth (BR/EDR) in the 2.4 GHz band, 79 channels 1 MHz apart.
  <https://www.bluetooth.com/learn-about-bluetooth/tech-overview/>. B02.
- MathWorks, "Comparison of Bluetooth BR/EDR and Bluetooth LE".
  <https://www.mathworks.com/help/bluetooth/gs/comparison-of-bluetooth-bredr-and-bluetooth-le.html>. B02.
- Rohde & Schwarz, application note 1C108: "a maximum hop rate of 1600 Hz" (multi-slot packets, which audio uses,
  hop less often, hence "up to").
  <https://scdn.rohde-schwarz.com/ur/pws/dl_downloads/dl_application/application_notes/1c108/1C108_0e_Bluetooth_BR_EDR_AFH.pdf>.
  B02.
- Dr. Dobb's, "Bluetooth/Wi-Fi co-existence", and a 2003 UCL paper: adaptive frequency hopping (Bluetooth 1.2,
  2003) drops busy channels such as Wi-Fi and keeps at least 20.
  <https://drdobbs.com/mobile/bluetoothwi-fi-co-existence/196802355>,
  <https://www.ee.ucl.ac.uk/lcs/previous/LCS2003/125.pdf>. B02.
- Wikipedia, "2.4 GHz radio use": the band is shared with Wi-Fi and microwave ovens.
  <https://en.wikipedia.org/wiki/2.4_GHz_radio_use>. B02.

## Codecs

- Apple, via MacRumors (2021): iPhone and AirPods are "limited to the Bluetooth AAC codec".
  <https://www.macrumors.com/2021/05/17/airpods-apple-music-lossless-audio/>. B03. Apple's AAC bit rate is not
  confirmed (an iPhone was once seen negotiating about 262 kbit/s:
  <https://lists.apple.com/archives/bluetooth-dev/2016/Apr/msg00015.html>), so the film gives none.
- Qualcomm, "Why aptX" (read): 384 kbit/s at 48 kHz. <https://www.aptx.com/why-aptx>; Wikipedia, "aptX": 352 kbit/s
  at 44.1 kHz, a fixed 4:1. <https://en.wikipedia.org/wiki/AptX>. B03.
- Qualcomm, "aptX HD" (read): 576 kbit/s at 48 kHz, 24-bit. <https://www.aptx.com/aptx-hd>. Background; not stated.
- Sony, "LDAC" (read): 330, 660 or 990 kbit/s; lossy. <https://www.sony.co.jp/en/Products/LDAC/>. B03.
- Android Open Source Project, Bluetooth services: AAC, aptX, aptX HD and LDAC supported besides SBC since Android
  8.0 (checked in the fact check). <https://source.android.com/docs/core/connect/bluetooth/services>. B03.

## Delay and lip sync

- SoundGuys, "Android Bluetooth latency" (Mar 2021): four phones, 100 runs per codec; averages of 308 ms (SBC) to
  369 ms (AAC). <https://soundguys.com/android-bluetooth-latency-22732>. B05.
- RTINGS, "Latency": 166–173 ms on one Bluetooth headset, 7 ms wired.
  <https://www.rtings.com/headphones/learn/latency>. B05 (with SoundGuys, the "170–370 ms" on screen).
- Buffering at each stage, and re-sends up to a flush timeout, are why a bigger buffer costs delay (fact sheet §5).
  B04.
- Delay Reporting (AVDTP 1.3, used by A2DP 1.3; SIG A2DP ICS above). Android: "Implement AVDTP delay reports"
  (merged Feb 2018). <https://android.googlesource.com/platform/packages/modules/Bluetooth/+/82fc8edc52>. iOS:
  supported since iOS 8.2 (Apple bluetooth-dev list).
  <https://lists.apple.com/archives/bluetooth-dev/2017/Aug/msg00009.html>. Results vary by device and app (a VLC
  issue: <https://code.videolan.org/videolan/vlc-android/-/issues/1487>), hence "can". B05.
- aptX Low Latency, about 40 ms, is for a dedicated transmitter, not phones (read).
  <https://www.aptx.com/aptx-low-latency>. Why B07 gives no figure for game modes; not stated.

## LE Audio, LC3 and Auracast

- Bluetooth SIG, "Bluetooth SIG unveils LE Audio, the next generation of Bluetooth audio" (CES, 6 Jan 2020), and XDA
  Developers' report of it: LE Audio with a new codec, LC3, which improves on SBC "even at a 50% lower bit rate".
  <https://www.bluetooth.com/press/bluetooth-sig-unveils-le-audio-the-next-generation-of-bluetooth-audio/>,
  <https://www.xda-developers.com/bluetooth-sig-introduces-le-audio-lc3-codec-support-multi-stream-audio-hearing-aids-audio-sharing/>.
  B06.
- Bluetooth SIG, LE Audio FAQ: "same, or slightly better" at "less than half the bit rate".
  <https://www.bluetooth.com/media/le-audio/le-audio-faqs/>. B06 (attributed: "The Bluetooth SIG says").
- Bluetooth SIG blog, "Just announced: the complete suite of LE Audio specifications is now available" (12 Jul
  2022): Auracast broadcast audio.
  <https://www.bluetooth.com/blog/just-announced-the-complete-suite-of-le-audio-specifications-is-now-available/>.
  B06.
- Bluetooth SIG, "How Auracast works": any number of in-range receivers can join one broadcast (checked in the fact
  check). <https://www.bluetooth.com/auracast/how-it-works/>. B06.

## Evidence and tools

- `bluetooth.py`, `mix_listen.py`, `build_hf.py`, `hyperframes/scenes/` and `evidence/` in this folder; the shared
  week kit in `week-13/_kit/` (`hfkit.py`, `kit3.js`, `add_qc.py`, `vertical_strings.py`); `week-13/run_audio.sh`.
- ffmpeg's SBC, aptX, aptX HD and AAC encoders (the codecs in the run are ffmpeg's implementations, not any
  company's code).
- three.js 0.187.0 (MIT licence), shipped in `hyperframes/assets/` (`three.module.min.js`, `three.core.min.js`,
  `three-LICENSE.txt`); vendored for the week in `week-13/_vendor`.
- HyperFrames (HTML rendered to video, GSAP timeline); Kokoro `af_bella` for the narration; Source Serif 4 and
  Inter for type; Apple, Android and ffmpeg marks from the toolkit's `icons/logos/`.
