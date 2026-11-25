"""Week 29 shared model: the one place every number on a slate comes from (no hand-typed figures).
Same model as angle_check*.py. Shots are numbered from one (shot = index + 1)."""
import math

class Field:
    def __init__(self, W=858.0, H=525.0, h=60.0, vx0=6.0, g=0.05):
        self.W, self.H, self.h, self.vx0, self.g = W, H, h, vx0, g
    def vx(self, n): return self.vx0 * (1 + self.g) ** n          # n = zero-based shot index
    def T(self, n): return self.W / self.vx(n)                      # flight ticks
    def fold(self, y):
        p = 2 * self.H; y %= p
        return p - y if y > self.H else y
    def line_full(self): return (self.H - self.h) / (2 * self.W)    # paddle/ball speed ratio, full aim
    def line_narrow(self, q): return q - self.h / (2 * self.W)      # aim limited to q x ball speed
    def lands(self, n, y_a, q=1.0, k=801):
        vy = q * self.vx(n)
        return [self.fold(y_a + (-vy + 2 * vy * i / (k - 1)) * self.T(n)) for i in range(k)]
    def defends(self, n, vp, y_a, q=1.0):
        L = self.lands(n, y_a, q)
        y_d = (min(L) + max(L)) / 2
        return max(abs(l - y_d) for l in L) <= vp * self.T(n) + self.h / 2
    def first_break(self, vp, q=1.0, nmax=200):
        for n in range(nmax):
            if not all(self.defends(n, vp, i * self.H / 20, q) for i in range(21)): return n
        return None
    def predict(self, vp, q=None):
        line = self.line_full() if q is None else self.line_narrow(q)
        if vp <= line * self.vx0: return 0
        return math.floor(math.log(vp / (line * self.vx0)) / math.log(1 + self.g)) + 1

OLD = Field()
NEW = Field(W=1200.0, H=500.0, h=50.0)
NOGROW = Field(g=0.0)

def checks():
    """Assert every figure the signed narration speaks. Returns the dict the slates use."""
    r = {}
    r['line_full'] = OLD.line_full()                    # 0.271
    r['line_narrow'] = OLD.line_narrow(0.25)            # 0.215
    r['line_new'] = NEW.line_full()                     # 0.1875
    r['line_card'] = Field(W=1000, H=500, h=50).line_full()   # 0.225
    r['bk_old'] = {vp: OLD.first_break(vp) for vp in (1.0, 2.0, 3.0)}
    r['bk_narrow'] = {vp: OLD.first_break(vp, 0.25) for vp in (1.0, 1.5, 2.0, 3.0)}
    r['bk_new'] = {vp: NEW.first_break(vp) for vp in (1.5, 2.5, 4.0)}
    r['pred_old'] = {vp: OLD.predict(vp) for vp in (1.0, 2.0, 3.0)}
    r['pred_narrow'] = {vp: OLD.predict(vp, 0.25) for vp in (1.0, 1.5, 2.0, 3.0)}
    r['pred_new'] = {vp: NEW.predict(vp) for vp in (1.5, 2.5, 4.0)}
    r['spd'] = {vp: math.log(vp / (r['line_full'] * 6.0)) / math.log(1.05) for vp in (2.0, 3.0)}
    r['nogrow'] = {vp: NOGROW.first_break(vp, nmax=200) for vp in (2.0, 3.0)}
    # narration: sixth/fourteenth shot, tenth/nineteenth, seventh/twenty-seventh, 0.271, 0.215, 0.188, 0.225
    assert r['bk_old'] == {1.0: 0, 2.0: 5, 3.0: 13}, r['bk_old']
    assert r['pred_old'] == {1.0: 0, 2.0: 5, 3.0: 13}, r['pred_old']
    assert r['bk_narrow'][2.0] == 9 and r['bk_narrow'][3.0] == 18 and r['bk_narrow'][1.5] == 4 and r['bk_narrow'][1.0] == 0
    assert r['pred_narrow'] == r['bk_narrow'], (r['pred_narrow'], r['bk_narrow'])
    assert r['bk_new'] == {1.5: 6, 2.5: 17, 4.0: 26} and r['pred_new'] == r['bk_new']
    assert abs(r['line_full'] - 0.271) < 5e-4 and abs(r['line_narrow'] - 0.215) < 5e-4
    assert abs(r['line_new'] - 0.1875) < 1e-9 and abs(r['line_card'] - 0.225) < 1e-9
    assert abs(r['spd'][2.0] - 4.24) < 0.01 and abs(r['spd'][3.0] - 12.56) < 0.01
    assert r['nogrow'] == {2.0: None, 3.0: None}
    return r

if __name__ == "__main__":
    import pprint; pprint.pprint(checks()); print("all narration figures reproduce")
