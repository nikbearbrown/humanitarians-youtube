# Sources — How a QR Code Works

Checked 2026-11-11. (Denso Wave's own qrcode.com and denso-wave.com would not load from here, so the history is from Wikipedia, which cites them.)

1. Wikipedia, "QR code": https://en.wikipedia.org/wiki/QR_code (invented 1994 by Masahiro Hara of Denso Wave; for tracking automobile parts; "quick-response code"; three finder patterns; version 1 = 21×21 to version 40 = 177×177; levels L/M/Q/H ≈ 7/15/25/30% of codewords; Reed–Solomon; logos rely on error correction, usually level H).
2. Thonky, QR Code Tutorial, "Module Placement in Matrix": https://www.thonky.com/qr-code-tutorial/module-placement-matrix (timing patterns are dotted lines connecting the finder patterns; data placement starts at the bottom-right, going up in 2-module-wide columns, zigzagging).
3. Thonky, QR Code Tutorial, "Data Masking": https://www.thonky.com/qr-code-tutorial/data-masking (eight mask patterns; masking makes the code easier to scan).
4. HyperPhysics, "CD Response to Defects": https://hyperphysics.gsu.edu/hbase/Audio/cdplay4.html (CDs use cross-interleaved Reed–Solomon coding to correct scratches).
5. FTC Consumer Alert, "Scammers hide harmful links in QR codes to steal your information", 2023-12-06: https://consumer.ftc.gov/consumer-alerts/2023/12/scammers-hide-harmful-links-qr-codes-steal-your-information (scammers covering QR codes on parking meters with their own; "inspect the URL before you open it").
6. Vendor references agreeing on L/M/Q/H = 7/15/25/30%: https://docs.devexpress.com/CoreLibraries/DevExpress.XtraPrinting.BarCode.QRCodeErrorCorrectionLevel
7. Own experiment: `demo/qr_demo.py` → `demo/qr_output.json` (segno 1.6.6 encoder, OpenCV 5.0.0 QRCodeDetector).
