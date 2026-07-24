# PEDAGOGY — claude-liam-m5-onboard

## Skill
m5-onboard (claude-plugins-official / cwc-makers)

## Learning objective
Understand M5Stack ESP32 onboarding: single orchestrator, physical button-dance requirement for native-USB boards, background-run pattern with streaming monitoring, and the Cardputer vs Cardputer-Adv firmware distinction.

## Prior knowledge assumed
Knows Python scripting; has done USB device work; unfamiliar with M5Stack ESP32 specifics or UIFlow.

## Key concepts
1. Single orchestrator: `onboard.py --apps buddy` runs detect → identify → flash → install in one command
2. Physical BtnG0+BtnRST dance required on native-USB boards — no software path into download mode
3. Run in background + tee + Monitor — foreground run looks like a hang; streaming is the fix
4. Cardputer vs Cardputer-Adv: same form factor, different firmware — user-intent question, not hardware fingerprint
5. NVS boot_option=2 + main.py: prevents UIFlow's BLE advertise from wedging the NimBLE controller

## VERDICT: PASS

The skill covers the full workflow with critical idiosyncrasies documented. Main gaps: NVS set_str failure mode and Linux dialout group requirement are buried in notes rather than the workflow section.
