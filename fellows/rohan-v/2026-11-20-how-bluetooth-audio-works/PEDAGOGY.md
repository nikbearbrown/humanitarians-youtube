# PEDAGOGY — "How Bluetooth Audio Works"

How the reel is built to teach someone who uses wireless earbuds every day but has never been told how the music
gets there.

## The register

*No assumed knowledge* and *the viewer has to learn something*: one test track followed from the phone to the
ears, through three problems in order (too much data, a crowded radio, lost packets); each problem shown, measured
or simulated, and its fix named; then the viewer hears the buffer's trade-off for themselves; company claims kept
apart from my numbers; and an ending on three things to do.

## The shape

| Beat | Job | What the viewer can do after it |
|---|---|---|
| B00 ASK | the question: phone to earbuds, and why it lags or cuts out | expect a small version, built and tested |
| B01 TOO MUCH DATA | CD stereo is about 1,400 kbit/s; SBC squeezes my track to about 330, under a quarter | explain why music is compressed before it is sent |
| B02 THE RADIO | 79 channels, up to 1,600 hops a second, shared with Wi-Fi; 17% of tries failed, about 1% with adaptive hopping | say what hopping is for, and why Wi-Fi gets in the way |
| B03 CODECS | phone and headphones agree on one; SBC, AAC, aptX, LDAC; more data is harder to send | read a codec setting on their phone and know what it trades |
| B04 THE BUFFER | lost packets are re-sent, so the earbuds keep a reserve; 30 glitches, 3, none; then listen | explain why a bigger buffer means fewer gaps and more delay, and hear a gap |
| B05 LIP SYNC | a couple of hundred milliseconds behind; videos hold the picture back, games can't | say why videos stay in sync and games feel laggy |
| B06 LE AUDIO | LC3, and Auracast to any number of earbuds | know what LE Audio adds |
| B07 WHAT TO DO | keep the phone close, a better codec if offered, game mode for games | improve their own setup |
| B08 OUTRO | sign-off | — |

## Choices worth defending

- **One path, in order.** Every beat is the next thing that happens to the same music on its way from the phone,
  so each fix answers the problem just shown: the squeeze answers too much data, hopping answers Wi-Fi, the buffer
  answers lost packets, and the buffer's cost (delay) leads straight into lip sync.
- **One colour language.** Music is always violet, the link blue, Wi-Fi orange, a try that gets through green and a
  lost one red, in 3D and in the HUD, so B02's bursts and B04's gaps read without a legend.
- **Hear it, don't just see it.** B04 ends with the same four seconds played through the simulated link twice. The
  window was picked as typical, not dramatic: the 6 s whose small-buffer glitch rate is closest to that buffer's
  average, so the one stutter you hear is a fair sample, not the worst moment.
- **Simulation and measurement kept apart.** The data rates are measured from real encoders' bytes; the radio and
  buffer numbers are "my simulation", with settings I chose. B02's numbers are the Wi-Fi-only figures, because body
  blocking isn't introduced until B04, and B04 then names both causes.
- **No quality ranking.** The run gives no codec a quality score: no listening test was run, and a waveform match
  is unfair to codecs built around hearing. B03 says only that more data can sound better.
- **Company claims attributed.** "The Bluetooth SIG says" introduces LC3's claim; Apple's devices "prefer" AAC; LDAC
  is "up to" 990.
