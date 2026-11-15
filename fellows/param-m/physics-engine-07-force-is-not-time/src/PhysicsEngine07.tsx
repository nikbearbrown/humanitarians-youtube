/**
 * PhysicsEngine07.tsx — body scenes for "Force Is Not Time." (physics engine, 7 of 12).
 *
 * Reel: books/physics-engine/youtube/force-is-not-time
 * Host: Param Madan · voice Kokoro af_bella
 * Source: github.com/jashshah127/humanitariansai/physics-engine @ 2dc4aa4
 *         (engine/units.py, variable_glossary.py, eval/ci_check.py; PHASE1.md).
 *
 * CONTRACT (illustrations/kit.tsx): every scene here is a pure function of
 * useP() — normalized progress across the beat's audio duration. No wall clock,
 * no state, no CSS transitions. Seeking any frame renders identically.
 *
 * COLOR: claude palette, one terracotta moment per beat. The accent marks the
 * open item, the ×100 slip, the caught card, the colliding T, and the tool used.
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

/** A small mono chip — one value or name. */
const Chip: React.FC<{ text: string; o?: number; hot?: boolean; struck?: boolean; size?: number }> = ({
  text, o = 1, hot = false, struck = false, size = 40,
}) => (
  <span style={{
    display: 'inline-block', padding: '10px 24px', background: CLAUDE.CARD,
    border: `${hot ? 3 : 2}px solid ${hot ? ACCENT : HAIR}`, opacity: o, whiteSpace: 'nowrap',
    fontFamily: MONO, fontSize: size, fontWeight: 600, color: hot ? ACCENT : struck ? SOFT : INK,
    textDecoration: struck ? 'line-through' : 'none',
  }}>{text}</span>
);

/* ────────────────────────────────────────────────────────────────────────────
 * B00B — the promise. Three things this video shows.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe7Promise: React.FC<{ spark?: string; headline?: string }> = ({
  spark = 'Why watch this.',
  headline = 'Units, checked honestly.',
}) => {
  const p = useP();
  const head = ease(remap(p, 0.04, 0.18, 0, 1));
  const items = [
    { v: 'Why', c: 'units decide the answer', hot: false },
    { v: 'The check', c: 'what it does, and doesn’t', hot: false },
    { v: 'The swap', c: 'planned tool vs. used tool', hot: true },
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
          <Tile key={n.v} value={n.v} caption={n.c} accent={n.hot} w={520} size={96}
            o={ease(remap(p, 0.14 + i * 0.2, 0.30 + i * 0.2, 0, 1))} />
        ))}
      </div>
      <RecordStrip text="No physics or coding background needed." o={remap(p, 0.84, 0.94, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B01 — the BLUF. Labels are checked; the algebra doesn't carry units yet.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe7Labels: React.FC<{ spark?: string }> = ({ spark = 'Labels, not yet algebra.' }) => {
  const p = useP();
  const Col: React.FC<{ head: string; items: string[]; o: number; open?: boolean }> = ({ head, items, o, open = false }) => (
    <div style={{
      width: 760, padding: '36px 48px', background: CLAUDE.CARD,
      border: `${open ? 3 : 2}px solid ${open ? ACCENT : HAIR}`, opacity: o,
      transform: `translateY(${(1 - o) * 24}px)`, display: 'flex', flexDirection: 'column', gap: 18,
    }}>
      <div style={{ fontFamily: SERIF, fontSize: 60, fontWeight: 600, color: open ? ACCENT : INK }}>{head}</div>
      <div style={{ height: 2, background: HAIR }} />
      {items.map((t) => (
        <div key={t} style={{ fontFamily: SANS, fontSize: 40, color: INK, lineHeight: 1.3 }}>{open ? '○ ' : '✓ '}{t}</div>
      ))}
    </div>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 130, width: SAFE.w,
        display: 'flex', justifyContent: 'center', gap: 60,
      }}>
        <Col head="Checked now" o={ease(remap(p, 0.10, 0.24, 0, 1))}
          items={['every label is a real unit', 'card agrees with the dictionary']} />
        <Col head="Not yet" open o={ease(remap(p, 0.62, 0.74, 0, 1))}
          items={['units carried through the algebra']} />
      </div>
      <RecordStrip text="And the team says so plainly." o={remap(p, 0.86, 0.95, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B02 — why. Four quantities, four units; cm into a metres formula is ×100.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe7Why: React.FC<{ spark?: string }> = ({ spark = 'No unit, no answer.' }) => {
  const p = useP();
  const q = [
    { n: 'speed', u: 'm/s', at: 0.14 },
    { n: 'distance', u: 'm', at: 0.20 },
    { n: 'tension', u: 'N', at: 0.26 },
    { n: 'period', u: 's', at: 0.32 },
  ];
  const slip = ease(remap(p, 0.46, 0.60, 0, 1));
  const warn = ease(remap(p, 0.76, 0.86, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 110,
        display: 'flex', justifyContent: 'center', gap: 30,
      }}>
        {q.map((x) => (
          <Tile key={x.n} value={x.u} caption={x.n} w={340} size={100}
            o={ease(remap(p, x.at, x.at + 0.06, 0, 1))} />
        ))}
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 420,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 28, opacity: slip,
        transform: `translateY(${(1 - slip) * 20}px)`,
      }}>
        <Chip text="4 cm" size={50} />
        <div style={{ fontFamily: SANS, fontSize: 38, color: SOFT }}>into a formula that expects meters</div>
        <div style={{ fontFamily: MONO, fontSize: 54, color: SOFT }}>→</div>
        <Chip text="off by ×100" hot size={50} />
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x + 260, width: SAFE.w - 520, top: SAFE.y + 580,
        padding: '22px 36px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: warn,
      }}>
        <div style={{ fontFamily: MONO, fontSize: 26, color: SOFT }}>WAVE-BASIC-RELATION · pitfall</div>
        <div style={{ fontFamily: SERIF, fontSize: 42, color: INK, marginTop: 8 }}>“Mixing units — wavelength in cm with speed in m/s is the usual slip.”</div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B03 — two checks: a real dimension; card agrees with dictionary.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe7Checks: React.FC<{ spark?: string }> = ({ spark = 'Two checks.' }) => {
  const p = useP();
  const a = ease(remap(p, 0.06, 0.16, 0, 1));
  const b = ease(remap(p, 0.40, 0.50, 0, 1));
  const bad = ease(remap(p, 0.62, 0.72, 0, 1));
  const ci = ease(remap(p, 0.82, 0.90, 0, 1));
  const Card: React.FC<{ n: string; title: string; o: number; children: React.ReactNode }> = ({ n, title, o, children }) => (
    <div style={{
      width: 790, height: 430, padding: '32px 44px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`,
      opacity: o, transform: `translateY(${(1 - o) * 24}px)`, display: 'flex', flexDirection: 'column', gap: 20,
    }}>
      <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase' }}>Check {n}</div>
      <div style={{ fontFamily: SERIF, fontSize: 52, fontWeight: 600, color: INK, lineHeight: 1.1 }}>{title}</div>
      <div style={{ height: 2, background: HAIR }} />
      {children}
    </div>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 100,
        display: 'flex', justifyContent: 'center', gap: 48,
      }}>
        <Card n="1" title="A real dimension" o={a}>
          <div style={{ fontFamily: MONO, fontSize: 40, color: INK, whiteSpace: 'nowrap' }}>"m/s"  → length / time ✓</div>
          <div style={{ fontFamily: MONO, fontSize: 40, color: SOFT, whiteSpace: 'nowrap' }}>"m/ss" → not a unit ✕</div>
          <div style={{ marginTop: 'auto', fontFamily: SANS, fontSize: 34, color: SOFT }}>catches typos and nonsense units</div>
        </Card>
        <Card n="2" title="Card agrees with the dictionary" o={b}>
          <div style={{ fontFamily: MONO, fontSize: 40, color: INK, whiteSpace: 'nowrap' }}>dictionary: v in m/s</div>
          <div style={{ fontFamily: MONO, fontSize: 40, color: ACCENT, fontWeight: 700, opacity: bad, whiteSpace: 'nowrap' }}>card: v in m  → caught</div>
          <div style={{ marginTop: 'auto', fontFamily: SANS, fontSize: 34, color: SOFT }}>same variable, same dimension</div>
        </Card>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 590, textAlign: 'center', opacity: ci,
      }}>
        <span style={{
          padding: '12px 30px', border: `2px solid ${HAIR}`, background: CLAUDE.CARD,
          fontFamily: MONO, fontSize: 34, color: INK,
        }}>eval/ci_check.py · “unit/dimension consistency”</span>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B04 — the finding. T in newtons on one card, in seconds on two.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe7Collision: React.FC<{ spark?: string }> = ({ spark = 'One letter, two dimensions.' }) => {
  const p = useP();
  const t = ease(remap(p, 0.02, 0.12, 0, 1));
  const l = ease(remap(p, 0.10, 0.24, 0, 1));
  const r = ease(remap(p, 0.30, 0.46, 0, 1));
  const verdict = ease(remap(p, 0.76, 0.88, 0, 1));
  const Side: React.FC<{ head: string; unit: string; dim: string; cards: string; o: number }> = ({ head, unit, dim, cards, o }) => (
    <div style={{
      width: 640, padding: '30px 40px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`,
      opacity: o, transform: `translateY(${(1 - o) * 22}px)`, display: 'flex', flexDirection: 'column', gap: 12,
    }}>
      <div style={{ fontFamily: SERIF, fontSize: 56, fontWeight: 600, color: INK }}>{head}</div>
      <div style={{ fontFamily: MONO, fontSize: 44, color: INK }}>{unit} · {dim}</div>
      <div style={{ fontFamily: SANS, fontSize: 32, color: SOFT }}>{cards}</div>
    </div>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 120,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 44,
      }}>
        <Side head="Tension" unit="N" dim="a force" cards="the pulley card" o={l} />
        <div style={{ fontFamily: MONO, fontSize: 200, fontWeight: 700, color: ACCENT, opacity: t, lineHeight: 1 }}>T</div>
        <Side head="Period" unit="s" dim="a time" cards="the orbit and magnetic-field cards" o={r} />
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 480, textAlign: 'center',
        fontFamily: SANS, fontSize: 38, color: SOFT, opacity: remap(p, 0.54, 0.64, 0, 1),
      }}>Spotted by hand before. Now machine-detectable.</div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 580, textAlign: 'center',
        fontFamily: SERIF, fontSize: 80, fontWeight: 600, color: INK, opacity: verdict,
      }}>Force versus time can’t be a <span style={{ color: ACCENT }}>false alarm</span>.</div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B05 — the change. The dictionary now names both meanings.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe7Overloaded: React.FC<{ spark?: string }> = ({ spark = 'Say it out loud.' }) => {
  const p = useP();
  const rows = [
    { s: 'T', unit: '"N or s"', desc: 'tension, or period — read which from the problem', at: 0.06, hot: true },
    { s: 'R', unit: '"m or ohm"', desc: 'radius, or resistance — read which from the problem', at: 0.34 },
  ];
  const quote = ease(remap(p, 0.60, 0.72, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 110, width: SAFE.w - 220, top: SAFE.y + 100,
        display: 'flex', flexDirection: 'column', gap: 22,
      }}>
        <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase', opacity: remap(p, 0.02, 0.08, 0, 1) }}>The variable dictionary, today</div>
        {rows.map((r) => {
          const o = ease(remap(p, r.at, r.at + 0.08, 0, 1));
          return (
            <div key={r.s} style={{
              display: 'flex', alignItems: 'center', gap: 40, padding: '24px 40px', background: CLAUDE.CARD,
              border: `${r.hot ? 3 : 2}px solid ${r.hot ? ACCENT : HAIR}`, opacity: o,
            }}>
              <div style={{ fontFamily: MONO, fontSize: 90, fontWeight: 700, color: r.hot ? ACCENT : INK, width: 90 }}>{r.s}</div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                <div style={{ fontFamily: MONO, fontSize: 40, color: INK }}>unit: {r.unit}</div>
                <div style={{ fontFamily: SANS, fontSize: 36, color: SOFT }}>{r.desc}</div>
              </div>
            </div>
          );
        })}
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x + 110, width: SAFE.w - 220, top: SAFE.y + 560,
        padding: '26px 44px', background: CLAUDE.CARD, borderLeft: `6px solid ${ACCENT}`, opacity: quote,
      }}>
        <div style={{ fontFamily: SERIF, fontSize: 40, color: INK, lineHeight: 1.3 }}>Renaming the symbols: from a judgment call<br />to “a check with an objective trigger.”</div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B06 — honest. pint was planned; SymPy units ran; propagation still open.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe7Swap: React.FC<{ spark?: string }> = ({ spark = 'Planned vs. used.' }) => {
  const p = useP();
  const plan = ease(remap(p, 0.04, 0.14, 0, 1));
  const used = ease(remap(p, 0.30, 0.44, 0, 1));
  const open = ease(remap(p, 0.66, 0.78, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 110,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 40,
      }}>
        <div style={{
          width: 640, padding: '30px 42px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: plan,
          display: 'flex', flexDirection: 'column', gap: 12,
        }}>
          <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase' }}>The plan said</div>
          <div style={{ fontFamily: MONO, fontSize: 64, fontWeight: 700, color: SOFT, textDecoration: 'line-through' }}>pint</div>
          <div style={{ fontFamily: SANS, fontSize: 34, color: SOFT }}>couldn’t be installed — never ran once</div>
        </div>
        <div style={{ fontFamily: MONO, fontSize: 60, color: SOFT, opacity: used }}>→</div>
        <div style={{
          width: 640, padding: '30px 42px', background: CLAUDE.CARD, border: `3px solid ${ACCENT}`, opacity: used,
          display: 'flex', flexDirection: 'column', gap: 12,
        }}>
          <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: ACCENT, textTransform: 'uppercase', fontWeight: 700 }}>The team used</div>
          <div style={{ fontFamily: MONO, fontSize: 42, fontWeight: 700, color: INK, whiteSpace: 'nowrap' }}>sympy.physics.units</div>
          <div style={{ fontFamily: SANS, fontSize: 34, color: INK }}>present, and actually run</div>
        </div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x + 200, width: SAFE.w - 400, top: SAFE.y + 470,
        padding: '26px 44px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: open,
        transform: `translateY(${(1 - open) * 20}px)`, textAlign: 'center',
      }}>
        <div style={{ fontFamily: SANS, fontSize: 30, letterSpacing: 3, color: SOFT, textTransform: 'uppercase' }}>Written down, still open</div>
        <div style={{ fontFamily: SERIF, fontSize: 50, color: INK, marginTop: 10 }}>Units are checked on the labels — not carried through the solve.</div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B07 — the verdict. Check the units first.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe7Verdict: React.FC<{ spark?: string }> = ({ spark = 'Units first.' }) => {
  const p = useP();
  const q = ease(remap(p, 0.06, 0.24, 0, 1));
  const sub = ease(remap(p, 0.50, 0.66, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 190, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 60,
      }}>
        <div style={{
          fontFamily: SERIF, fontSize: 96, fontWeight: 600, color: INK, opacity: q, lineHeight: 1.15,
          textAlign: 'center', maxWidth: 1650, transform: `translateY(${(1 - q) * 26}px)`,
        }}>A tool that says what it <span style={{ color: ACCENT }}>didn’t</span> do<br />beats one that claims it all.</div>
        <div style={{
          padding: '28px 48px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: sub,
          fontFamily: SANS, fontSize: 46, color: INK, maxWidth: 1400, textAlign: 'center', lineHeight: 1.35,
        }}>Check the units first. If they don’t make sense, the number doesn’t either.</div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B09 — the outro. Title, terracotta period, host name, credit lines.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe7Outro: React.FC<{ title?: string; handle?: string; subline?: string }> =
({ title = 'Force Is Not Time.', handle = 'Param Madan', subline = 'Physics Engine · 7 of 12' }) => {
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
