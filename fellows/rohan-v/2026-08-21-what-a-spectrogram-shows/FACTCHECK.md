# FACTCHECK — What a Spectrogram Shows

- A magnitude spectrogram is a time-frequency map of energy (typically |STFT|), not a picture of "what the sound is." Standard DSP: Oppenheim & Schafer.
- Axes: time (horizontal) × frequency (vertical) is the librosa.specshow convention used here as a teaching default. Other orientations exist; this reel is consistent, not universal.
- A waveform is pressure vs time and does not uniquely display pitch content.
- A voiced vowel shows a harmonic stack (F0 plus integer multiples), not a single line. Brightness is energy, not correctness or identity.
- STFT window length trades time resolution against frequency resolution. This is the uncertainty / window theorem of the STFT, not a software bug.
- Phase is discarded in a magnitude spectrogram. Two signals can share |STFT| and still cancel (or not reconstruct) without a phase estimate (Griffin & Lim, 1984).
- Overlapping sources add in the time-frequency plane and can smear; a stain is not proof of one source.
- A noise floor / display floor hides quiet events (many consonants are low-energy).
- Rainbow / jet colormaps can invent false contours (Borland & Taylor, 2007). This reel uses brightness, not a rainbow.
- Teaching diagrams are redrawn and simplified — not measured from a named recording.
