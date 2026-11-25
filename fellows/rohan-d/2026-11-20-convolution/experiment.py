"""Every number the convolution film shows (pure numpy; deterministic)."""
import numpy as np
img = np.array([[0, 0, 0, 9, 9, 9]] * 6, dtype=float)
k = np.array([[-1, 0, 1]] * 3, dtype=float)
def conv(a, k):
    n = a.shape[0] - k.shape[0] + 1
    m = a.shape[1] - k.shape[1] + 1
    return np.array([[float(np.sum(a[i:i + 3, j:j + 3] * k)) for j in range(m)] for i in range(n)])
out = conv(img, k)
print("image row", img[0].tolist())
print("kernel", k.tolist())
print("output (4x4):"); print(out)
print("window values row 0:", [float(np.sum(img[0:3, j:j + 3] * k)) for j in range(4)])
print("window 1 detail: left col sum", float(-img[0:3, 1].sum()), "right col sum", float(img[0:3, 3].sum()))
print("fully connected weights:", 36 * 16, " kernel weights:", 9)
sizes = [6]
for _ in range(3):
    sizes.append(sizes[-1] - 3 + 1)
print("size after each 3x3 conv, no padding:", sizes)
print("with 1-pixel zero padding: size stays", 6 + 2 - 3 + 1)
shifted = np.array([[0, 9, 9, 9, 9, 9]] * 6, dtype=float)
print("edge moved one column left ->", conv(shifted, k)[0].tolist())
