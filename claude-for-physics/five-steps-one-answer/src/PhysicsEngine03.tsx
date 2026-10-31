/**
 * PhysicsEngine03.tsx — body scenes for "Five Steps, One Answer." (physics engine, 3 of 17).
 *
 * Reel: books/physics-engine/youtube/five-steps-one-answer
 * Host: Param Madan · voice Kokoro af_bella
 * Source: github.com/jashshah127/humanitariansai/physics-engine @ 2dc4aa4
 *         (engine/pipeline.py, parse.py, formula_kb.py, models.py; golden set MECH-001).
 *
 * CONTRACT (illustrations/kit.tsx): every scene here is a pure function of
 * useP() — normalized progress across the beat's audio duration. No wall clock,
 * no state, no CSS transitions. Seeking any frame renders identically.
 *
 * COLOR: claude palette, one terracotta moment per beat. The accent always
 * marks the step in focus on the rail, and the value or card that step decides.
 *
 * ONE PROBLEM: B02–B06 carry the same car problem (v0 = 0, a = 2.5 m/s², t = 12 s
 * → v = 30 m/s, s = 180 m) through the five stages, under a shared StepRail.
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

const STEPS = ['Parse', 'Retrieve', 'Plan', 'Solve', 'Verify'];

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

/** The five-step rail across the top of B02–B06. Done steps ink, current step
 *  terracotta, steps ahead soft. */
const StepRail: React.FC<{ at: number }> = ({ at }) => {
  const p = useP();
  const o = remap(p, 0, 0.06, 0, 1);
  return (
    <div style={{
      position: 'absolute', left: SAFE.x, width: SAFE.w, top: 128, opacity: o,
      display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 18,
    }}>
      {STEPS.map((s, i) => {
        const cur = i === at;
        const done = i < at;
        return (
          <React.Fragment key={s}>
            {i > 0 && <div style={{ width: 54, height: 3, background: done || cur ? INK : HAIR }} />}
            <div style={{
              padding: '12px 26px', minWidth: 200, textAlign: 'center',
              background: cur ? ACCENT : CLAUDE.CARD,
              border: `2px solid ${cur ? ACCENT : done ? INK : HAIR}`,
              fontFamily: SANS, fontSize: 32, letterSpacing: 2.4, textTransform: 'uppercase',
              color: cur ? CLAUDE.CARD : done ? INK : SOFT, fontWeight: cur ? 700 : 500,
            }}>{i + 1} · {s}</div>
          </React.Fragment>
        );
      })}
    </div>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B00B — the promise. Three things this video shows.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe3Promise: React.FC<{ spark?: string; headline?: string }> = ({
  spark = 'Why watch this.',
  headline = 'One problem, all five steps.',
}) => {
  const p = useP();
  const head = ease(remap(p, 0.04, 0.18, 0, 1));
  const items = [
    { v: '5 steps', c: 'parse to verify', hot: false },
    { v: '1 car', c: 'followed all the way', hot: false },
    { v: 'A record', c: 'not just a number', hot: true },
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
            o={ease(remap(p, 0.12 + i * 0.22, 0.28 + i * 0.22, 0, 1))} />
        ))}
      </div>
      <RecordStrip text="No physics or coding background needed." o={remap(p, 0.84, 0.94, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B01 — the BLUF. Five steps, one job each; only Parse uses a model.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe3Steps: React.FC<{ spark?: string }> = ({ spark = 'One job each.' }) => {
  const p = useP();
  const jobs = [
    'reads the problem',
    'finds formulas that might help',
    'checks it can be solved',
    'does the math',
    'checks the answer',
  ];
  const tag = ease(remap(p, 0.62, 0.74, 0, 1));
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 150, width: SAFE.w,
        display: 'flex', justifyContent: 'center', gap: 22,
      }}>
        {STEPS.map((s, i) => {
          const o = ease(remap(p, 0.08 + i * 0.1, 0.18 + i * 0.1, 0, 1));
          const model = i === 0;
          return (
            <div key={s} style={{
              width: 322, height: 470, padding: '34px 28px', background: CLAUDE.CARD,
              border: `${model ? 3 : 2}px solid ${model && tag > 0 ? ACCENT : HAIR}`,
              opacity: o, transform: `translateY(${(1 - o) * 26}px)`,
              display: 'flex', flexDirection: 'column', gap: 18,
            }}>
              <div style={{ fontFamily: MONO, fontSize: 40, color: SOFT }}>{i + 1}</div>
              <div style={{ fontFamily: SERIF, fontSize: 66, fontWeight: 600, color: INK, lineHeight: 1.05 }}>{s}</div>
              <div style={{ height: 2, background: HAIR }} />
              <div style={{ fontFamily: SANS, fontSize: 38, color: INK, lineHeight: 1.3 }}>{jobs[i]}</div>
              <div style={{
                marginTop: 'auto', fontFamily: SANS, fontSize: 26, letterSpacing: 2.4,
                textTransform: 'uppercase', lineHeight: 1.3, opacity: tag,
                color: model ? ACCENT : SOFT, fontWeight: model ? 700 : 500,
              }}>{model ? 'Language model' : 'Fixed rules'}</div>
            </div>
          );
        })}
      </div>
      <RecordStrip text="Once the problem is read, the same input always takes the same path."
        o={remap(p, 0.84, 0.94, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B02 — parse. The sentence becomes knowns; each keeps its source phrase.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe3Parse: React.FC<{ spark?: string }> = ({ spark = 'Read, never compute.' }) => {
  const p = useP();
  const sent = ease(remap(p, 0.04, 0.14, 0, 1));
  const rows = [
    { sym: 'a', val: '2.5 m/s²', phrase: '“accelerates uniformly at 2.5 m/s²”', at: 0.18, hot: false },
    { sym: 't', val: '12 s', phrase: '“for 12 s”', at: 0.27, hot: false },
    { sym: 'v0', val: '0 m/s', phrase: '“starts from rest”', at: 0.36, hot: true },
  ];
  const ask = ease(remap(p, 0.46, 0.56, 0, 1));
  const Hl: React.FC<{ on: number; hot?: boolean; children: React.ReactNode }> = ({ on, hot = false, children }) => (
    <span style={{
      background: on > 0 ? (hot ? 'rgba(217,119,87,0.18)' : 'rgba(61,57,41,0.08)') : 'transparent',
      borderBottom: `3px solid ${on > 0 ? (hot ? ACCENT : INK) : 'transparent'}`,
    }}>{children}</span>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      <StepRail at={0} />
      <div style={{
        position: 'absolute', left: SAFE.x + 80, width: SAFE.w - 160, top: 262,
        padding: '30px 40px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`,
        fontFamily: SERIF, fontSize: 44, lineHeight: 1.4, color: INK, opacity: sent,
      }}>
        A car <Hl on={remap(p, 0.36, 0.37, 0, 1)} hot>starts from rest</Hl> and{' '}
        <Hl on={remap(p, 0.18, 0.19, 0, 1)}>accelerates uniformly at 2.5 m/s²</Hl>{' '}
        <Hl on={remap(p, 0.27, 0.28, 0, 1)}>for 12 s</Hl>. Find (a) the car’s{' '}
        <Hl on={remap(p, 0.46, 0.47, 0, 1)}>final speed</Hl> and (b) the{' '}
        <Hl on={remap(p, 0.46, 0.47, 0, 1)}>distance</Hl> it travels.
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x + 80, width: SAFE.w - 160, top: 508,
        display: 'flex', gap: 40,
      }}>
        <div style={{ flex: 1.55, display: 'flex', flexDirection: 'column', gap: 14 }}>
          <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase', opacity: sent }}>Knowns · with the phrase each came from</div>
          {rows.map((r) => {
            const o = ease(remap(p, r.at, r.at + 0.06, 0, 1));
            return (
              <div key={r.sym} style={{
                display: 'flex', alignItems: 'baseline', gap: 26, opacity: o,
                transform: `translateX(${(1 - o) * -24}px)`,
              }}>
                <div style={{ fontFamily: MONO, fontSize: 48, color: r.hot ? ACCENT : INK, fontWeight: 600, width: 330, whiteSpace: 'nowrap' }}>{r.sym} = {r.val}</div>
                <div style={{ fontFamily: SANS, fontSize: 32, color: SOFT, whiteSpace: 'nowrap' }}>← {r.phrase}</div>
              </div>
            );
          })}
        </div>
        <div style={{ flex: 0.6, display: 'flex', flexDirection: 'column', gap: 14, opacity: ask }}>
          <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase' }}>Asked</div>
          <div style={{ fontFamily: MONO, fontSize: 48, color: INK, fontWeight: 600 }}>v = ?</div>
          <div style={{ fontFamily: MONO, fontSize: 48, color: INK, fontWeight: 600 }}>s = ?</div>
        </div>
      </div>
      <RecordStrip text="The model reads. It must not solve anything, or compute any value."
        o={remap(p, 0.80, 0.90, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B03 — retrieve. 31 cards; the six that can give a speed or a distance light up.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe3Retrieve: React.FC<{ spark?: string }> = ({ spark = 'Pull every candidate.' }) => {
  const p = useP();
  const groups = [
    { name: 'Mechanics', n: 8, hits: [0, 3, 4, 7] },
    { name: 'Electricity & mag.', n: 8, hits: [] as number[] },
    { name: 'Waves', n: 9, hits: [0, 1] },
    { name: 'Heat', n: 6, hits: [] as number[] },
  ];
  // Mechanics hits: kinematics, incline, spring, orbit (MECH-001/004/005/008).
  const grid = ease(remap(p, 0.06, 0.20, 0, 1));
  const lit = ease(remap(p, 0.48, 0.58, 0, 1));
  const list = ease(remap(p, 0.58, 0.70, 0, 1));
  const names = ['Constant acceleration', 'Incline with friction', 'Spring energy',
    'Satellite orbit', 'Wave: v = f·λ', 'Wave from its equation'];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <StepRail at={1} />
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: 262,
        display: 'flex', justifyContent: 'center', gap: 56, opacity: grid,
      }}>
        {groups.map((g) => (
          <div key={g.name} style={{ width: 360, display: 'flex', flexDirection: 'column', gap: 14 }}>
            <div style={{ fontFamily: SANS, fontSize: 26, letterSpacing: 2.4, color: SOFT, textTransform: 'uppercase', whiteSpace: 'nowrap' }}>{g.name}</div>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: 12 }}>
              {Array.from({ length: g.n }, (_, i) => {
                const hit = g.hits.includes(i);
                return (
                  <div key={i} style={{
                    width: 78, height: 100, background: CLAUDE.CARD,
                    border: `${hit && lit > 0 ? 4 : 2}px solid ${hit && lit > 0 ? ACCENT : HAIR}`,
                    opacity: hit ? 1 : 1 - lit * 0.55,
                  }}>
                    <div style={{ margin: '18px 12px 0', height: 4, background: hit && lit > 0 ? ACCENT : HAIR }} />
                    <div style={{ margin: '12px 12px 0', height: 4, width: 36, background: HAIR }} />
                  </div>
                );
              })}
            </div>
          </div>
        ))}
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: 228 + 330,
        textAlign: 'center', fontFamily: SERIF, fontSize: 56, fontWeight: 600, color: INK, opacity: grid,
      }}>31 cards · <span style={{ color: lit > 0 ? ACCENT : INK }}>{lit > 0 ? '6 can give a speed or a distance' : 'equations, when they apply, common mistakes'}</span></div>
      <div style={{
        position: 'absolute', left: SAFE.x + 120, width: SAFE.w - 240, top: 228 + 430,
        display: 'flex', flexWrap: 'wrap', justifyContent: 'center', gap: '14px 18px', opacity: list,
      }}>
        {names.map((n) => (
          <div key={n} style={{
            padding: '10px 22px', border: `2px solid ${HAIR}`, background: CLAUDE.CARD,
            fontFamily: SANS, fontSize: 32, color: INK, whiteSpace: 'nowrap',
          }}>{n}</div>
        ))}
      </div>
      <RecordStrip text="Retrieve doesn’t check whether we have enough. That’s the next step’s job."
        o={remap(p, 0.82, 0.92, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B04 — plan. The closure check: five candidates miss a known, one closes.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe3Plan: React.FC<{ spark?: string }> = ({ spark = 'Can it close?' }) => {
  const p = useP();
  const rows = [
    { card: 'Spring energy', need: 'spring constant k', ok: false, at: 0.22 },
    { card: 'Incline with friction', need: 'angle, friction, distance', ok: false, at: 0.36 },
    { card: 'Satellite orbit', need: 'altitude h', ok: false, at: 0.40 },
    { card: 'Wave: v = f·λ', need: 'frequency, wavelength', ok: false, at: 0.44 },
    { card: 'Wave from its equation', need: 'wave number, angular frequency', ok: false, at: 0.48 },
    { card: 'Constant acceleration', need: 'v0, a, t — all given', ok: true, at: 0.56 },
  ];
  const head = remap(p, 0.04, 0.12, 0, 1);
  return (
    <IlluStage spark={spark} sparkPos="top">
      <StepRail at={2} />
      <div style={{
        position: 'absolute', left: SAFE.x + 150, width: SAFE.w - 300, top: 254,
        display: 'flex', flexDirection: 'column', gap: 10,
      }}>
        <div style={{
          display: 'flex', fontFamily: SANS, fontSize: 26, letterSpacing: 3, color: SOFT,
          textTransform: 'uppercase', opacity: head, padding: '0 28px',
        }}>
          <div style={{ width: 560 }}>Candidate card</div>
          <div style={{ flex: 1 }}>Needs</div>
          <div style={{ width: 200, textAlign: 'right' }}>Closure</div>
        </div>
        {rows.map((r) => {
          const o = ease(remap(p, r.at, r.at + 0.05, 0, 1));
          return (
            <div key={r.card} style={{
              display: 'flex', alignItems: 'center', padding: '14px 28px',
              background: CLAUDE.CARD, border: `${r.ok ? 3 : 2}px solid ${r.ok ? ACCENT : HAIR}`,
              opacity: o, transform: `translateY(${(1 - o) * 16}px)`,
            }}>
              <div style={{ width: 560, fontFamily: SERIF, fontSize: 42, fontWeight: 600, color: r.ok ? ACCENT : INK }}>{r.card}</div>
              <div style={{ flex: 1, fontFamily: SANS, fontSize: 32, color: r.ok ? INK : SOFT }}>{r.ok ? '' : 'missing: '}{r.need}</div>
              <div style={{
                width: 200, textAlign: 'right', fontFamily: MONO, fontSize: 34, fontWeight: 600,
                color: r.ok ? ACCENT : SOFT,
              }}>{r.ok ? '✓ closes' : '✕ gap'}</div>
            </div>
          );
        })}
      </div>
      <RecordStrip text="No card closes? Stop, name what’s missing, and log the gap — never guess."
        o={remap(p, 0.80, 0.90, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B05 — solve. SymPy substitutes and evaluates both equations.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe3Solve: React.FC<{ spark?: string }> = ({ spark = 'The solver does it.' }) => {
  const p = useP();
  const Line: React.FC<{ steps: string[]; ats: number[]; unit: string; y: number }> = ({ steps, ats, unit, y }) => (
    <div style={{
      position: 'absolute', left: SAFE.x, width: SAFE.w, top: y,
      display: 'flex', justifyContent: 'center', alignItems: 'baseline', gap: 30,
    }}>
      {steps.map((s, i) => {
        const o = ease(remap(p, ats[i], ats[i] + 0.06, 0, 1));
        const last = i === steps.length - 1;
        return (
          <React.Fragment key={i}>
            {i > 0 && <div style={{ fontFamily: MONO, fontSize: 54, color: SOFT, opacity: o }}>→</div>}
            <div style={{
              fontFamily: MONO, fontSize: last ? 76 : 54, fontWeight: 600, opacity: o,
              color: last ? ACCENT : INK, whiteSpace: 'nowrap',
            }}>{s}{last ? ` ${unit}` : ''}</div>
          </React.Fragment>
        );
      })}
    </div>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      <StepRail at={3} />
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: 262, textAlign: 'center',
        opacity: remap(p, 0.02, 0.10, 0, 1),
      }}>
        <span style={{
          padding: '10px 26px', border: `2px solid ${HAIR}`, background: CLAUDE.CARD,
          fontFamily: MONO, fontSize: 32, color: SOFT,
        }}>SymPy · symbolic math, exact by rule</span>
      </div>
      <div style={{ position: 'absolute', left: SAFE.x, width: SAFE.w, top: 368 }}>
        <Eyebrow text="Final speed" o={remap(p, 0.12, 0.18, 0, 1)} />
      </div>
      <Line steps={['v = v0 + a·t', '0 + 2.5 × 12', '30']} ats={[0.14, 0.28, 0.36]} unit="m/s" y={420} />
      <div style={{ position: 'absolute', left: SAFE.x, width: SAFE.w, top: 568 }}>
        <Eyebrow text="Distance" o={remap(p, 0.42, 0.48, 0, 1)} />
      </div>
      <Line steps={['s = v0·t + ½·a·t²', '½ × 2.5 × 144', '180']} ats={[0.44, 0.58, 0.68]} unit="m" y={620} />
      <RecordStrip text="No number is typed in by hand. Every value comes from the solver."
        o={remap(p, 0.80, 0.90, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B06 — verify. Plug back in; then a second, independent path to s.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe3Verify: React.FC<{ spark?: string }> = ({ spark = 'Check it twice.' }) => {
  const p = useP();
  const c1 = ease(remap(p, 0.04, 0.16, 0, 1));
  const c2 = ease(remap(p, 0.30, 0.42, 0, 1));
  const calc = ease(remap(p, 0.52, 0.64, 0, 1));
  const done = ease(remap(p, 0.76, 0.86, 0, 1));
  const Card: React.FC<{ n: string; title: string; o: number; children: React.ReactNode }> = ({ n, title, o, children }) => (
    <div style={{
      width: 790, height: 420, padding: '36px 44px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`,
      opacity: o, transform: `translateY(${(1 - o) * 24}px)`,
      display: 'flex', flexDirection: 'column', gap: 22,
    }}>
      <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, color: SOFT, textTransform: 'uppercase' }}>Check {n}</div>
      <div style={{ fontFamily: SERIF, fontSize: 54, fontWeight: 600, color: INK, lineHeight: 1.1 }}>{title}</div>
      <div style={{ height: 2, background: HAIR }} />
      {children}
    </div>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      <StepRail at={4} />
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: 258,
        display: 'flex', justifyContent: 'center', gap: 48,
      }}>
        <Card n="1" title="Plug the answers back in" o={c1}>
          <div style={{ fontFamily: MONO, fontSize: 40, color: INK, lineHeight: 1.5 }}>30 = 0 + 2.5 × 12<br />180 = ½ × 2.5 × 12²</div>
          <div style={{ marginTop: 'auto', fontFamily: MONO, fontSize: 38, color: INK, fontWeight: 600 }}>both sides match ✓</div>
        </Card>
        <Card n="2" title="Find s a different way" o={c2}>
          <div style={{ fontFamily: MONO, fontSize: 40, color: INK, lineHeight: 1.5 }}>v² = v0² + 2·a·s</div>
          <div style={{ fontFamily: MONO, fontSize: 40, color: INK, lineHeight: 1.5, opacity: calc }}>s = 900 ÷ 5 = 180 m</div>
          <div style={{ marginTop: 'auto', fontFamily: MONO, fontSize: 38, color: INK, fontWeight: 600, opacity: calc }}>same answer, two paths ✓</div>
        </Card>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: 730, textAlign: 'center', opacity: done,
      }}>
        <span style={{
          padding: '14px 40px', border: `3px solid ${ACCENT}`, background: CLAUDE.CARD,
          fontFamily: MONO, fontSize: 48, fontWeight: 700, color: ACCENT,
        }}>status: verified</span>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B07 — the verdict. A solution object, and three questions for any AI.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe3Verdict: React.FC<{ spark?: string }> = ({ spark = 'A record, not a number.' }) => {
  const p = useP();
  const fields = [
    { k: 'parse', v: 'v0 = 0, a = 2.5, t = 12' },
    { k: 'retrieve', v: '6 candidates → constant acceleration' },
    { k: 'plan', v: 'closure: solvable' },
    { k: 'solve', v: 'sympy.solve → v = 30, s = 180' },
    { k: 'verify', v: 'status: verified' },
  ];
  const obj = ease(remap(p, 0.04, 0.14, 0, 1));
  const ask = ease(remap(p, 0.66, 0.78, 0, 1));
  const qs = ['What did you read?', 'Which formula?', 'How did you check?'];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 180, width: SAFE.w - 360, top: 150,
        padding: '30px 44px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, opacity: obj,
        fontFamily: MONO, fontSize: 38, lineHeight: 1.55, color: INK,
      }}>
        <div style={{ color: SOFT }}>solution object {'{'}</div>
        {fields.map((f, i) => (
          <div key={f.k} style={{ paddingLeft: 48, opacity: ease(remap(p, 0.10 + i * 0.07, 0.15 + i * 0.07, 0, 1)), whiteSpace: 'nowrap' }}>
            <span style={{ color: SOFT }}>{f.k}:</span> {f.v}
          </div>
        ))}
        <div style={{ paddingLeft: 48, opacity: ease(remap(p, 0.46, 0.52, 0, 1)) }}>
          <span style={{ color: SOFT }}>route:</span> <span style={{ color: ACCENT, fontWeight: 700 }}>deterministic_script</span>
        </div>
        <div style={{ color: SOFT }}>{'}'}</div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: 720,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 22, opacity: ask,
        transform: `translateY(${(1 - ask) * 20}px)`,
      }}>
        <div style={{ fontFamily: SANS, fontSize: 30, letterSpacing: 3, color: SOFT, textTransform: 'uppercase' }}>Ask any AI answer</div>
        <div style={{ display: 'flex', gap: 28 }}>
          {qs.map((q) => (
            <div key={q} style={{
              padding: '16px 30px', border: `2px solid ${ACCENT}`, background: CLAUDE.CARD,
              fontFamily: SERIF, fontSize: 46, fontWeight: 600, color: INK, whiteSpace: 'nowrap',
            }}>{q}</div>
          ))}
        </div>
      </div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B09 — the outro. Title, terracotta period, host name, credit lines.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe3Outro: React.FC<{ title?: string; handle?: string; subline?: string }> =
({ title = 'Five Steps, One Answer.', handle = 'Param Madan', subline = 'Physics Engine · 3 of 17' }) => {
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
