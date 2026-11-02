/**
 * PhysicsEngine08.tsx — body scenes for "Check It Another Way." (physics engine, 8 of 12).
 *
 * Reel: books/physics-engine/youtube/check-it-another-way
 * Host: Param Madan · voice Kokoro af_bella
 * Source: github.com/jashshah127/humanitariansai/physics-engine @ 2dc4aa4
 *         (engine/pipeline.py verify(); formula_kb.py verify functions; golden set EM-004/005).
 *
 * CONTRACT (illustrations/kit.tsx): every scene here is a pure function of
 * useP() — normalized progress across the beat's audio duration. No wall clock,
 * no state, no CSS transitions. Seeking any frame renders identically.
 *
 * COLOR: claude palette, one terracotta moment per beat. The accent marks the
 * independent path, the residual, the failed physics, and the flagged label.
 */
import React from 'react';
import { AbsoluteFill } from 'remotion';
import { CLAUDE } from '../tokens/claude';
import { SAFE } from '../tokens/layout';
import { IlluStage, SERIF, SANS, MONO, remap, ease, useP } from '../illustrations/kit';

const INK = CLAUDE.INK;
const SOFT = CLAUDE.INK_SOFT;
const ACCENT = CLAUDE.SPARK;
const HAIR = CLAUDE.BORDER;

/** Small uppercase label that sets the frame's subject. */
const Eyebrow: React.FC<{ text: string; o: number }> = ({ text, o }) => (
  <div style={{
    fontFamily: SANS, fontSize: 34, letterSpacing: 5, color: SOFT,
    textTransform: 'uppercase', opacity: o, textAlign: 'center',
  }}>{text}</div>
);

/** A stat tile: big value over a small caption. */
const Tile: React.FC<{
  value: string; caption: string; o: number; accent?: boolean; w?: number; size?: number;
}> = ({ value, caption, o, accent = false, w = 500, size = 132 }) => (
  <div style={{
    width: w, padding: '34px 28px 30px', background: CLAUDE.CARD,
    border: `2px solid ${accent ? ACCENT : HAIR}`, opacity: o,
    transform: `translateY(${(1 - o) * 26}px)`,
    display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 12,
  }}>
    <div style={{
      fontFamily: SERIF, fontSize: size, lineHeight: 1.08,
      color: accent ? ACCENT : INK, fontWeight: 600,
    }}>{value}</div>
    <div style={{
      fontFamily: SANS, fontSize: 30, letterSpacing: 2.4, lineHeight: 1.3,
      textTransform: 'uppercase', color: SOFT, textAlign: 'center',
    }}>{caption}</div>
  </div>
);

/** The lesson line that lands at the end of a beat, under a terracotta rule. */
const RecordStrip: React.FC<{ text: string; o: number }> = ({ text, o }) => (
  <div style={{
    position: 'absolute', left: SAFE.x, width: SAFE.w, bottom: 96,
    opacity: o, transform: `translateY(${(1 - o) * 18}px)`,
    display: 'flex', justifyContent: 'center',
  }}>
    <div style={{
      borderTop: `3px solid ${ACCENT}`, paddingTop: 20, maxWidth: 1500,
      fontFamily: SERIF, fontSize: 44, lineHeight: 1.25, color: INK, textAlign: 'center',
    }}>{text}</div>
  </div>
);

/** One check card with a number, a title, a body and a pass line. */
const CheckCard: React.FC<{
  n: string; title: string; o: number; hot?: boolean; w?: number; h?: number; children: React.ReactNode;
}> = ({ n, title, o, hot = false, w = 520, h = 470, children }) => (
  <div style={{
    width: w, height: h, padding: '30px 38px', background: CLAUDE.CARD,
    border: `${hot ? 3 : 2}px solid ${hot ? ACCENT : HAIR}`, opacity: o,
    transform: `translateY(${(1 - o) * 24}px)`, display: 'flex', flexDirection: 'column', gap: 18,
  }}>
    <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: hot ? ACCENT : SOFT, textTransform: 'uppercase', fontWeight: hot ? 700 : 500 }}>Check {n}</div>
    <div style={{ fontFamily: SERIF, fontSize: 52, fontWeight: 600, color: INK, lineHeight: 1.1 }}>{title}</div>
    <div style={{ height: 2, background: HAIR }} />
    {children}
  </div>
);

/* ────────────────────────────────────────────────────────────────────────────
 * B00B — the promise. Three things this video shows.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe8Promise: React.FC<{ spark?: string; headline?: string }> = ({
  spark = 'Why watch this.',
  headline = 'How the engine checks itself.',
}) => {
  const p = useP();
  const head = ease(remap(p, 0.04, 0.18, 0, 1));
  const items = [
    { v: 'Every', c: 'the check all answers get', hot: false },
    { v: 'Stronger', c: 'laws of physics as tests', hot: false },
    { v: 'Labels', c: 'when a check fails', hot: true },
  ];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 110, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 26,
      }}>
        <Eyebrow text="What this video is" o={remap(p, 0, 0.08, 0, 1)} />
        <div style={{
          fontFamily: SERIF, fontSize: 92, lineHeight: 1.12, color: INK,
          textAlign: 'center', maxWidth: 1600, fontWeight: 600,
          opacity: head, transform: `translateY(${(1 - head) * 30}px)`,
        }}>{headline}</div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 370, width: SAFE.w, height: 360,
        display: 'flex', justifyContent: 'center', gap: 34,
      }}>
        {items.map((n, i) => (
          <Tile key={n.v} value={n.v} caption={n.c} accent={n.hot} w={520} size={120}
            o={ease(remap(p, 0.14 + i * 0.2, 0.30 + i * 0.2, 0, 1))} />
        ))}
      </div>
      <RecordStrip text="No physics or coding background needed." o={remap(p, 0.84, 0.94, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B01 — the BLUF. Three checks; 11 of 31 cards carry the third.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe8Three: React.FC<{ spark?: string }> = ({ spark = 'Three checks.' }) => {
  const p = useP();
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 100,
        display: 'flex', justifyContent: 'center', gap: 34,
      }}>
        <CheckCard n="1" title="Plug it back in" o={ease(remap(p, 0.06, 0.16, 0, 1))} h={440}>
          <div style={{ fontFamily: SANS, fontSize: 38, color: INK }}>every card</div>
        </CheckCard>
        <CheckCard n="2" title="Physically possible" o={ease(remap(p, 0.20, 0.30, 0, 1))} h={440}>
          <div style={{ fontFamily: SANS, fontSize: 38, color: INK }}>where it matters</div>
        </CheckCard>
        <CheckCard n="3" title="A different route" o={ease(remap(p, 0.38, 0.50, 0, 1))} hot h={440}>
          <div style={{ fontFamily: SERIF, fontSize: 80, fontWeight: 600, color: ACCENT, lineHeight: 1 }}>11 of 31</div>
          <div style={{ fontFamily: SANS, fontSize: 34, color: INK }}>cards</div>
        </CheckCard>
      </div>
      <RecordStrip text="Fail anything, and the answer is labeled — flagged for review, never hidden."
        o={remap(p, 0.78, 0.88, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B02 — check one. Substitute and measure the leftover (the residual).
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe8Residual: React.FC<{ spark?: string }> = ({ spark = 'Plug it back in.' }) => {
  const p = useP();
  const eq = ease(remap(p, 0.06, 0.16, 0, 1));
  const sub = ease(remap(p, 0.20, 0.32, 0, 1));
  const res = ease(remap(p, 0.40, 0.52, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 130,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 34,
      }}>
        <div style={{ fontFamily: MONO, fontSize: 60, color: INK, opacity: eq, whiteSpace: 'nowrap' }}>
          card equation:  I_total = I_branch1 + I_branch2
        </div>
        <div style={{ fontFamily: MONO, fontSize: 60, color: INK, opacity: sub, whiteSpace: 'nowrap' }}>
          2.2 − (1.2 + 1.0)
        </div>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 30, opacity: res }}>
          <div style={{ fontFamily: SANS, fontSize: 34, letterSpacing: 3, color: SOFT, textTransform: 'uppercase' }}>Residual</div>
          <div style={{ fontFamily: MONO, fontSize: 110, fontWeight: 700, color: ACCENT }}>≈ 0</div>
        </div>
      </div>
      <RecordStrip text="It runs on every card, every time." o={remap(p, 0.80, 0.90, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B03 — check two. Must-be-positive quantities.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe8Positive: React.FC<{ spark?: string }> = ({ spark = 'Physically possible?' }) => {
  const p = useP();
  const chips = ['speed', 'time', 'distance'];
  const bad = ease(remap(p, 0.56, 0.68, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 110,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 26,
      }}>
        <div style={{ fontFamily: SANS, fontSize: 30, letterSpacing: 3, color: SOFT, textTransform: 'uppercase', opacity: remap(p, 0.10, 0.16, 0, 1) }}>must_be_positive</div>
        {chips.map((c, i) => (
          <div key={c} style={{
            padding: '14px 32px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`,
            fontFamily: SERIF, fontSize: 52, fontWeight: 600, color: INK,
            opacity: ease(remap(p, 0.14 + i * 0.06, 0.20 + i * 0.06, 0, 1)),
          }}>{c}</div>
        ))}
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 330,
        display: 'flex', justifyContent: 'center', gap: 60, opacity: bad,
        transform: `translateY(${(1 - bad) * 20}px)`,
      }}>
        <div style={{ width: 640, padding: '30px 40px', background: CLAUDE.CARD, border: `2px solid ${HAIR}` }}>
          <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase' }}>Algebra</div>
          <div style={{ fontFamily: MONO, fontSize: 56, color: INK, marginTop: 10 }}>v = −2.37 ✓</div>
          <div style={{ fontFamily: SANS, fontSize: 32, color: SOFT, marginTop: 8 }}>satisfies v² = 5.625</div>
        </div>
        <div style={{ width: 640, padding: '30px 40px', background: CLAUDE.CARD, border: `3px solid ${ACCENT}` }}>
          <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: ACCENT, textTransform: 'uppercase', fontWeight: 700 }}>Physics</div>
          <div style={{ fontFamily: MONO, fontSize: 56, color: ACCENT, fontWeight: 700, marginTop: 10 }}>v &gt; 0 ✕</div>
          <div style={{ fontFamily: SANS, fontSize: 32, color: SOFT, marginTop: 8 }}>a speed can’t be negative</div>
        </div>
      </div>
      <RecordStrip text="The algebra can be right while the physics is impossible." o={remap(p, 0.84, 0.93, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B04 — check three. Same answer, different route: KCL, RC, orbit.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe8Second: React.FC<{ spark?: string }> = ({ spark = 'A different route.' }) => {
  const p = useP();
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 100,
        display: 'flex', justifyContent: 'center', gap: 34,
      }}>
        <CheckCard n="3 · circuit" title="Currents add up" w={560} o={ease(remap(p, 0.06, 0.16, 0, 1))} hot>
          <div style={{ fontFamily: MONO, fontSize: 40, color: INK, whiteSpace: 'nowrap' }}>1.2 + 1.0 = 2.2 A</div>
          <div style={{ marginTop: 'auto', fontFamily: SANS, fontSize: 32, color: SOFT }}>Kirchhoff’s current law</div>
        </CheckCard>
        <CheckCard n="3 · capacitor" title="63% after one τ" w={560} o={ease(remap(p, 0.40, 0.52, 0, 1))}>
          <div style={{ fontFamily: MONO, fontSize: 40, color: INK, whiteSpace: 'nowrap' }}>9 V × (1 − 1/e)</div>
          <div style={{ fontFamily: MONO, fontSize: 44, color: INK, fontWeight: 700 }}>= 5.69 V</div>
          <div style={{ marginTop: 'auto', fontFamily: SANS, fontSize: 32, color: SOFT }}>one time constant</div>
        </CheckCard>
        <CheckCard n="3 · orbit" title="Period, a second way" w={560} o={ease(remap(p, 0.80, 0.90, 0, 1))}>
          <div style={{ fontFamily: MONO, fontSize: 40, color: INK, whiteSpace: 'nowrap' }}>T = 2π·√(r³/GM)</div>
          <div style={{ marginTop: 'auto', fontFamily: SANS, fontSize: 32, color: SOFT }}>a second formula</div>
        </CheckCard>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B05 — laws of physics used as tests.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe8Laws: React.FC<{ spark?: string }> = ({ spark = 'Nature as a test.' }) => {
  const p = useP();
  const a = ease(remap(p, 0.04, 0.16, 0, 1));
  const b = ease(remap(p, 0.30, 0.42, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 110,
        display: 'flex', justifyContent: 'center', gap: 50,
      }}>
        {[
          { t: 'Escape vs. orbit', law: 'v_escape / v_orbit = √2', o: a, hot: true },
          { t: 'Heat engine', law: '0 < efficiency < 1', o: b, hot: false },
        ].map((x) => (
          <div key={x.t} style={{
            width: 760, padding: '36px 46px', background: CLAUDE.CARD,
            border: `${x.hot ? 3 : 2}px solid ${x.hot ? ACCENT : HAIR}`, opacity: x.o,
            transform: `translateY(${(1 - x.o) * 24}px)`, display: 'flex', flexDirection: 'column', gap: 18,
          }}>
            <div style={{ fontFamily: SERIF, fontSize: 56, fontWeight: 600, color: INK }}>{x.t}</div>
            <div style={{ height: 2, background: HAIR }} />
            <div style={{ fontFamily: MONO, fontSize: 44, fontWeight: 700, color: x.hot ? ACCENT : INK, whiteSpace: 'nowrap' }}>{x.law}</div>
          </div>
        ))}
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 470, textAlign: 'center',
        fontFamily: SERIF, fontSize: 64, fontWeight: 600, color: INK, opacity: remap(p, 0.62, 0.74, 0, 1),
      }}>Not two numbers compared — a rule nature enforces.</div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B06 — labels: verified, flagged for review, not run; and the limit.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe8Labels: React.FC<{ spark?: string }> = ({ spark = 'Every result labeled.' }) => {
  const p = useP();
  const rows = [
    { k: 'all checks pass', v: 'verified', at: 0.06, hot: false },
    { k: 'any check fails', v: 'solved — flagged for review', at: 0.18, hot: true },
    { k: 'answer in symbols', v: 'numeric checks: not run', at: 0.46, hot: false },
  ];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 180, width: SAFE.w - 360, top: SAFE.y + 100,
        display: 'flex', flexDirection: 'column', gap: 18,
      }}>
        {rows.map((r) => {
          const o = ease(remap(p, r.at, r.at + 0.07, 0, 1));
          return (
            <div key={r.k} style={{
              display: 'flex', alignItems: 'center', padding: '24px 40px', background: CLAUDE.CARD,
              border: `${r.hot ? 3 : 2}px solid ${r.hot ? ACCENT : HAIR}`, opacity: o,
            }}>
              <div style={{ width: 460, fontFamily: SANS, fontSize: 38, color: SOFT }}>{r.k}</div>
              <div style={{ fontFamily: MONO, fontSize: 42, fontWeight: 700, color: r.hot ? ACCENT : INK }}>{r.v}</div>
            </div>
          );
        })}
      </div>
      <RecordStrip text="The limit: 20 of the 31 cards have no independent path yet."
        o={remap(p, 0.80, 0.90, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B07 — the verdict. Two routes are evidence.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe8Verdict: React.FC<{ spark?: string }> = ({ spark = 'Ask for a second route.' }) => {
  const p = useP();
  const q = ease(remap(p, 0.06, 0.24, 0, 1));
  const sub = ease(remap(p, 0.40, 0.56, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 190, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 60,
      }}>
        <div style={{
          fontFamily: SERIF, fontSize: 100, fontWeight: 600, color: INK, opacity: q, lineHeight: 1.15,
          textAlign: 'center', maxWidth: 1650, transform: `translateY(${(1 - q) * 26}px)`,
        }}>One answer is a claim.<br />Two routes are <span style={{ color: ACCENT }}>evidence</span>.</div>
        <div style={{
          padding: '28px 48px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: sub,
          fontFamily: SANS, fontSize: 46, color: INK, maxWidth: 1400, textAlign: 'center', lineHeight: 1.35,
        }}>Ask it to check the answer another way. If they don’t match, look at that step.</div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B09 — the outro. Title, terracotta period, host name, credit lines.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe8Outro: React.FC<{ title?: string; handle?: string; subline?: string }> =
({ title = 'Check It Another Way.', handle = 'Param Madan', subline = 'Physics Engine · 8 of 12' }) => {
  const p = useP();
  const rise = ease(remap(p, 0.02, 0.30, 0, 1));
  const nameO = remap(p, 0.24, 0.48, 0, 1);
  const subO = remap(p, 0.44, 0.66, 0, 1);
  const hasDot = title.trim().endsWith('.');
  const stem = hasDot ? title.trim().slice(0, -1) : title.trim();
  return (
    <AbsoluteFill style={{
      background: CLAUDE.PAGE, display: 'flex', flexDirection: 'column',
      alignItems: 'center', justifyContent: 'center', gap: 30,
    }}>
      <div style={{
        fontFamily: SERIF, fontSize: 160, lineHeight: 1.04, fontWeight: 600, color: INK,
        maxWidth: SAFE.w, textAlign: 'center',
        opacity: rise, transform: `translateY(${(1 - rise) * 40}px)`,
      }}>
        {stem}{hasDot && <span style={{ color: ACCENT }}>.</span>}
      </div>
      <div style={{
        fontFamily: SERIF, fontSize: 86, color: INK, opacity: nameO,
        transform: `translateY(${(1 - ease(nameO)) * 22}px)`,
      }}>{handle}</div>
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 12, opacity: subO }}>
        {subline.split(' · ').map((line) => (
          <div key={line} style={{
            fontFamily: SANS, fontSize: 36, letterSpacing: 3, textTransform: 'uppercase',
            color: SOFT, textAlign: 'center', whiteSpace: 'nowrap',
          }}>{line}</div>
        ))}
      </div>
    </AbsoluteFill>
  );
};
