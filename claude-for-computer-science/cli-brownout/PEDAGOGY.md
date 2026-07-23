# Pedagogy audit — cli-brownout

## Structure check
- B00 INTRO: brand open, sets register
- B01 PROBLEM: stakes before any terminal -- full battery, device resets; CR2032 internal resistance caps current at ~3mA; inference burst demands 8mA; supply sags below reset threshold
- B02 ASK: terminal command, explains what is being asked
- B03 CODE: key function shown, what to verify (V = V_oc - I*R)
- B04 OUTPUT: voltage trace with crimson sag crossing reset line; chip RESET TRIGGERED
- B05 CHANGE: revision command (add 100uF cap)
- B06 OUTPUT (revised): original trace (faint) and capped trace side by side, cap blunts sag
- B07 SUMMARY: two power questions -- energy vs instantaneous delivery
- B08 NEXT STEPS: find threshold in datasheet, measure burst, size cap
- B09 OUTRO: brand close

## Voice check
- No forbidden phrases ("obviously", "clearly", "important to understand", etc.)
- Problem stated first (B01) before any CLI
- Concrete numbers: 3V nominal, 1000 ohm R_int, 8mA pulse, 2V reset, 100uF cap
- No fabricated numbers beyond the candidate card

## CLI loop check
- At least one revision: YES (B05 CHANGE -> B06 revised output)
- SUMMARY and NEXT STEPS present: YES

VERDICT: PASS
