# FACTCHECK — Sample Rate and the Nyquist Limit

- Sampling stores discrete measurements of a continuous pressure wave. Sample rate is measurements per second.
- Shannon/Nyquist sampling theorem (bandlimited case): a signal whose spectrum is limited to B Hz is uniquely recoverable from uniform samples at fs > 2B. Nyquist frequency is fs/2.
- Compact Disc Digital Audio: 44,100 Hz sample rate (Red Book). The associated Nyquist frequency is 22,050 Hz. Human hearing is often cited ~20 kHz as a practical ceiling; 22.05 kHz is the unique-pitch ceiling of that rate, not a claim that everyone hears to 22 kHz.
- 16 kHz is a common rate for speech models (e.g. Whisper's default input resampling). Nyquist then is 8 kHz. Energy above that is removed by anti-alias filtering if the converter is designed correctly; it folds (aliases) if it is not.
- Aliasing: frequencies above Nyquist are indistinguishable from lower frequencies (they "fold"). A spectrogram of an aliased file can show energy at the wrong place.
- Upsampling / inserting zeros / interpolating does not restore frequencies that were never captured. High sample rates do not recover band-limited sources.
- Teaching plots are schematic (not a lab ADC capture). Dot counts illustrate "enough vs too few," not a specific ADC.
