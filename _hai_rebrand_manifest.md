# HAI rebrand — final (2026-07-24)

Every beat_sheet.json under humanitarians_html/youtube rebranded to Humanitarians AI:

- Voice: am_onyx -> af_kore (0 residue)
- Persona: Liam -> Kore (0 residue)
- Handle: @NikBearBrown -> @HumanitariansAI
- Attribution: 'in for Bear' -> 'in for Humanitarians AI'
- Outro: outro_source 'AUTHOR.MD :: NikBearBrown' -> 'AUTHOR.MD :: Humanitarians AI'
- Register set to Pragmatist on all sheets

## Deliberately NOT changed

- 360 files still contain 'NikBearBrown' ONLY as Remotion component identifiers (NikBearBrownOutro / NikBearBrownCodeBlock / NikBearBrownTerminalAsk / NikBearBrownOpen, +916 variants) and in stale metadata.build.skin_warnings. There is NO registered HAI/Humanitarians component family (only NikBearBrown*, Medhavy*, Claude* exist), so renaming these would break renders. These are a build decision, not a text swap.
- 116 sheets in this tree carry outro_source 'AUTHOR.MD :: Medhavy.com' (Medhavy outro inside the HAI tree) — left as-is; not named in the instruction.

## Medhavy voice drift

- af_bella confirmed as Medhavy default; all Medhavy sheets were on af_kore. Switched af_kore -> af_bella across medhavy/, medhavy_com/, medhavi-cancer/ (voice fields + audio_note). 0 residue.
