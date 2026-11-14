# Frictional log: How a QR Code Works

_Drafted by Claude on 2026-11-13 from this week's chat and the build log. Tanishaa: read it and correct anything that is not what happened._

## 2026-11-13 — Building "How a QR Code Works"
- **Working on:** a STEM explainer on how a phone reads a QR code, and why a covered code still scans. QR codes were one of my two topics when the team split the video work.
- **Tried:** chose QR codes from four options (Wi-Fi, noise-cancelling, QR codes, a Lyrical Literacy update). Expected the highest error-correction level ("30%") to survive about 30% of the code being covered.
- **Resisted:** the real test (`demo/qr_demo.py`, OpenCV reader) didn't match the 30%: the highest level still read with 17 × 17 of 37 × 37 squares covered, about 21% of the area, because the 30% counts codewords, not area. The fact-check also caught a wrong line in the first script ("most of a QR code isn't your message" is false at the lowest level). In the build, the outro title wrapped past the safe area, and the QR squares themselves kept being measured as too-small text in the vertical version. After watching it, I pointed out a long empty-screen gap around 1:56 before "It's good at"; the heading was waiting for "great at", so it now appears as soon as Bella asks the question.
- **Contributions:** Claude drafted the script, wrote the demo, the scenes (`scenes/QrScenes.tsx`) and the fact-check, and ran the build. I chose the topic, approved the fact-checked script, and caught the gap at 1:56.
- **Understand now:** error-correction percentages are about codewords, so a solid block of damage costs more than its area suggests. **Still unsure:** _[Tanishaa: what is still unclear to you?]_
