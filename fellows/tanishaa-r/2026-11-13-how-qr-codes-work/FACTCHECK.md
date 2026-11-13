# Fact check — How a QR Code Works (script v2)

| Beat | Claim | Status | Source |
|---|---|---|---|
| B01 | Part of a code can be covered and it still reads | ✅ measured | demo: H reads with 17×17 of 37×37 covered |
| B02 | Our link is a 29 × 29 grid | ✅ measured | demo: version 3 at L and M (4·3+17 = 29) |
| B02 | Dark = 1, light = 0 | ✅ | standard convention (Thonky) |
| B02 | Invented in Japan, 1994, to track car parts; "Quick Response" | ✅ | Wikipedia (Denso Wave, Masahiro Hara) |
| B03 | Three finder squares locate the code and its rotation | ✅ | Wikipedia |
| B03 | Dotted timing lines between finders set the grid | ✅ | Thonky placement |
| B04 | Reading starts bottom-right, two columns at a time, up and down | ✅ | Thonky placement |
| B04 | 8 bits per byte spell the link | ✅ (byte mode) | demo text is 40 bytes, byte mode |
| B04 | A mask is flipped over the top to avoid hard-to-scan patches | ✅ | Thonky masking (eight masks; our L code uses mask 0, H uses mask 1) |
| B05 | Not all of the code is your message; recovery data is added | ✅ | 3-L: 55 data + 15 recovery codewords; 5-H: 46 data + 88 recovery |
| B05 | v1 said "most of a QR code isn't your message" | ❌ fixed | true at H, false at L → reworded to "carries more than your message" |
| B05 | Reed–Solomon; same idea as scratched CDs | ✅ | Wikipedia; HyperPhysics (CIRC) |
| B05 | Levels ≈ 7 / 15 / 25 / 30% | ✅ | Wikipedia; DevExpress (percent of codewords) |
| B06 | L fails at 7×7 covered; H reads with 17×17 ≈ 21% of the area ("about a fifth") | ✅ measured | demo/qr_output.json |
| B07 | Logos in the middle work because recovery data fills them in; costs a bigger code | ✅ | Wikipedia; demo: same link is 29×29 at L, 37×37 at H |
| B08 | Scammers put stickers over real codes; check the link first | ✅ | FTC alert 2023-12-06 |
| B08 | QR reads at an angle | ✅ | Wikipedia (finder patterns give orientation) |

**Caveats shown or said:** the 30% is of codewords, not area, so the video says "about a fifth" for the measured area. The demo uses one reader (OpenCV); phone apps may do a little better or worse.
