"""How QR codes work: a real encode -> damage -> decode experiment.

Encodes one URL at all four error-correction levels (L, M, Q, H), then covers a
growing square in the middle of each code (leaving the three finder squares
alone) and asks OpenCV's QR reader to decode it. Records the largest share of
the code that can be covered while it still reads back correctly.
Writes qr_output.json plus PNGs used by the video.
"""
import json
import numpy as np
import segno
import cv2

TEXT = "https://www.youtube.com/@HumanitariansAI"
SCALE = 20  # pixels per module
QUIET = 4   # modules of white border


def matrix(qr):
    return np.array([[1 if v else 0 for v in row] for row in qr.matrix], dtype=np.uint8)


def to_img(m):
    n = m.shape[0]
    img = np.full(((n + 2 * QUIET) * SCALE,) * 2, 255, np.uint8)
    for y in range(n):
        for x in range(n):
            if m[y, x]:
                img[(y + QUIET) * SCALE:(y + QUIET + 1) * SCALE,
                    (x + QUIET) * SCALE:(x + QUIET + 1) * SCALE] = 0
    return img


det = cv2.QRCodeDetector()


def decode(img):
    data, pts, _ = det.detectAndDecode(img)
    return data


def cover(m, side, seed=None):
    """Cover a centred side x side block of modules with a grey 'sticker'."""
    n = m.shape[0]
    img = to_img(m).copy()
    c0 = (n - side) // 2
    a = (c0 + QUIET) * SCALE
    b = (c0 + side + QUIET) * SCALE
    img[a:b, a:b] = 255 if seed is None else 0  # white sticker
    return img


out = {"text": TEXT, "levels": {}}
for err in "LMQH":
    qr = segno.make(TEXT, error=err, micro=False, boost_error=False)
    m = matrix(qr)
    n = m.shape[0]
    assert decode(to_img(m)) == TEXT, err
    best = 0
    for side in range(1, n):
        if decode(cover(m, side)) == TEXT:
            best = side
        # finder squares are 7x7 at corners; a centred square of side s
        # reaches them when (n - s)//2 < 8
        if (n - side) // 2 < 9:
            break
    out["levels"][err] = {
        "version": qr.version,
        "modules": n,
        "designed_recovery_pct": {"L": 7, "M": 15, "Q": 25, "H": 30}[err],
        "largest_centre_cover_modules": best,
        "largest_centre_cover_pct_of_area": round(100 * best * best / (n * n), 1),
        "fails_at_modules": best + 1,
    }
    cv2.imwrite(f"qr_{err}.png", to_img(m))
    cv2.imwrite(f"qr_{err}_covered_ok.png", cover(m, best))
    cv2.imwrite(f"qr_{err}_covered_fail.png", cover(m, best + 1))
    print(err, out["levels"][err])

# Same URL, the small one (level L): count dark vs light, and bits
qrL = segno.make(TEXT, error="L", micro=False, boost_error=False)
mL = matrix(qrL)
out["level_L_dark_modules"] = int(mL.sum())
out["level_L_total_modules"] = int(mL.size)
out["text_bytes"] = len(TEXT.encode())
json.dump(out, open("qr_output.json", "w"), indent=2)

# --- for the video: the real module grids, and a round-logo test at level H ---
out["matrix"] = {err: ["".join(str(v) for v in row) for row in matrix(segno.make(TEXT, error=err, micro=False, boost_error=False))]
                 for err in "LH"}
out["mask"] = {err: segno.make(TEXT, error=err, micro=False, boost_error=False).mask for err in "LH"}
# codeword counts from ISO/IEC 18004 table 9 for the versions above
out["codewords"] = {"L": {"version": 3, "data": 55, "recovery": 15}, "H": {"version": 5, "data": 46, "recovery": 88}}


def logo(m, diam):
    n = m.shape[0]
    img = to_img(m).copy()
    c = (n / 2 + QUIET) * SCALE
    cv2.circle(img, (int(c), int(c)), int(diam * SCALE / 2), 255, -1)
    cv2.circle(img, (int(c), int(c)), int(diam * SCALE / 2 * 0.8), 90, -1)  # a grey disc "logo"
    return img


mH = matrix(segno.make(TEXT, error="H", micro=False, boost_error=False))
logo_ok = {d: decode(logo(mH, d)) == TEXT for d in range(7, 22, 2)}
out["logo_round_diameter_modules_reads"] = logo_ok
cv2.imwrite("qr_H_logo.png", logo(mH, 13))
print("logo", logo_ok)
json.dump(out, open("qr_output.json", "w"), indent=2)
