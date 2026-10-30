/**
 * PhysicsEngine01.tsx — body scenes for "Who Does the Math." (physics engine, 1 of 17).
 *
 * Reel: books/physics-engine/youtube/who-does-the-math
 * Host: Param Madan · voice Kokoro af_bella
 * Source: github.com/jashshah127/humanitariansai/physics-engine @ 2dc4aa4
 *
 * CONTRACT (illustrations/kit.tsx): every scene here is a pure function of
 * useP() — normalized progress across the beat's audio duration. No wall clock,
 * no state, no CSS transitions. Seeking any frame renders identically.
 *
 * COLOR: claude palette, one terracotta moment per beat. The accent always
 * marks the solver side, or the element that decides — SymPy in B01, the
 * problem-solving engine in B02, Verify in B03, the deciding question in B04.
 *
 * FACT NOTE: every figure is the repo's own reported result at the pinned
 * commit, ledgered in the reel's SOURCES.md. Figures that will move as the
 * card library grows (coverage) carry an "as of" line and are props.
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

/** A bordered card with a label, a title and optional body line. */
const Card: React.FC<{
  label?: string; title: string; body?: string; o: number; hot?: boolean; w?: number;
  titleSize?: number;
}> = ({ label, title, body, o, hot = false, w, titleSize = 58 }) => (
  <div style={{
    width: w, padding: '28px 36px', background: CLAUDE.CARD,
    border: `${hot ? 3 : 2}px solid ${hot ? ACCENT : HAIR}`, opacity: o,
    transform: `translateY(${(1 - o) * 24}px)`,
    display: 'flex', flexDirection: 'column', gap: 10,
  }}>
    {label && <div style={{
      fontFamily: SANS, fontSize: 26, letterSpacing: 3.4, textTransform: 'uppercase', color: SOFT,
    }}>{label}</div>}
    <div style={{
      fontFamily: SERIF, fontSize: titleSize, lineHeight: 1.12, fontWeight: 600,
      color: hot ? ACCENT : INK,
    }}>{title}</div>
    {body && <div style={{ fontFamily: SANS, fontSize: 34, lineHeight: 1.35, color: SOFT }}>{body}</div>}
  </div>
);

/* ────────────────────────────────────────────────────────────────────────────
 * B00B — the promise. Three things this video proves.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe1Promise: React.FC<{ spark?: string; headline?: string }> = ({
  spark = 'Why watch this.',
  headline = 'Three things, no background needed.',
}) => {
  const p = useP();
  const head = ease(remap(p, 0.04, 0.18, 0, 1));
  const items = [
    { v: 'Who', c: 'reads, and who calculates', hot: true },
    { v: 'When', c: 'an answer can be trusted', hot: false },
    { v: 'What', c: 'is proven, and what is not', hot: false },
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
        position: 'absolute', left: SAFE.x, top: SAFE.y + 360, width: SAFE.w,
        display: 'flex', justifyContent: 'center', gap: 34,
      }}>
        {items.map((n, i) => (
          <Tile key={n.v} value={n.v} caption={n.c} accent={n.hot} w={520}
            o={ease(remap(p, 0.16 + i * 0.17, 0.32 + i * 0.17, 0, 1))} />
        ))}
      </div>
      <RecordStrip
        text="Every term gets defined the first time it shows up."
        o={remap(p, 0.80, 0.92, 0, 1)}
      />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B01 — the BLUF. Words to the model, math to the solver.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe1Split: React.FC<{ spark?: string }> = ({ spark = 'Split the job.' }) => {
  const p = useP();
  const left = ease(remap(p, 0.04, 0.22, 0, 1));
  const right = ease(remap(p, 0.44, 0.62, 0, 1));
  const Col: React.FC<{
    who: string; what: string; jobs: string[]; o: number; hot?: boolean; t0: number;
  }> = ({ who, what, jobs, o, hot = false, t0 }) => (
    <div style={{
      width: 800, padding: '42px 52px', background: CLAUDE.CARD,
      border: `${hot ? 3 : 2}px solid ${hot ? ACCENT : HAIR}`,
      opacity: o, transform: `translateY(${(1 - o) * 28}px)`,
      display: 'flex', flexDirection: 'column', gap: 16,
    }}>
      <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 4, textTransform: 'uppercase', color: SOFT }}>{what}</div>
      <div style={{ fontFamily: SERIF, fontSize: 100, fontWeight: 600, color: hot ? ACCENT : INK, lineHeight: 1.05 }}>{who}</div>
      <div style={{ height: 2, background: HAIR, margin: '6px 0' }} />
      {jobs.map((j, i) => (
        <div key={j} style={{
          fontFamily: SANS, fontSize: 50, color: INK, lineHeight: 1.3,
          opacity: ease(remap(p, t0 + i * 0.06, t0 + 0.08 + i * 0.06, 0, 1)),
        }}>— {j}</div>
      ))}
    </div>
  );
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 136, width: SAFE.w,
        display: 'flex', justifyContent: 'center', gap: 64,
      }}>
        <Col who="The model" what="Language model · words" o={left} t0={0.14}
          jobs={['reads the problem', 'picks the formula', 'explains the answer']} />
        <Col who="The solver" what="SymPy + pint · math" o={right} t0={0.54} hot
          jobs={['does the algebra exactly', 'does the arithmetic', 'tracks every unit']} />
      </div>
      <RecordStrip
        text="The model never does arithmetic or algebra itself."
        o={remap(p, 0.80, 0.92, 0, 1)}
      />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B02 — not a game engine. Question in, structured solution out.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe1NotGame: React.FC<{ spark?: string }> = ({ spark = 'Not that kind.' }) => {
  const p = useP();
  const game = ease(remap(p, 0.04, 0.20, 0, 1));
  const strike = remap(p, 0.22, 0.32, 0, 1);
  const flow = ease(remap(p, 0.36, 0.52, 0, 1));
  const out = (i: number) => ease(remap(p, 0.52 + i * 0.07, 0.62 + i * 0.07, 0, 1));
  // A ball's arc for the game-engine panel: fixed geometry, no time.
  const arc = Array.from({ length: 9 }, (_, i) => {
    const x = 40 + i * 50;
    const y = 250 - 210 * Math.sin((Math.PI * i) / 8);
    return { x, y };
  });
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 150, width: SAFE.w, height: 600,
        display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 80,
      }}>
        <div style={{ position: 'relative', opacity: game * (1 - 0.55 * strike), display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 18 }}>
          <svg width={600} height={360} viewBox="0 0 500 300">
            <line x1={10} y1={280} x2={490} y2={280} stroke={SOFT} strokeWidth={4} />
            {arc.map((a, i) => (
              <circle key={i} cx={a.x} cy={a.y} r={i === 8 ? 22 : 9} fill={i === 8 ? INK : SOFT} opacity={i === 8 ? 1 : 0.5} />
            ))}
          </svg>
          <div style={{ position: 'relative' }}>
            <div style={{ fontFamily: SERIF, fontSize: 72, color: INK, fontWeight: 600 }}>Game engine</div>
            <div style={{
              position: 'absolute', left: -16, right: -16, top: '54%', height: 7,
              background: ACCENT, transformOrigin: 'left', transform: `scaleX(${strike})`,
            }} />
          </div>
          <div style={{ fontFamily: SANS, fontSize: 32, letterSpacing: 3, textTransform: 'uppercase', color: SOFT }}>makes things fall and bounce</div>
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 24, opacity: flow, transform: `translateY(${(1 - flow) * 26}px)`, width: 960 }}>
          <div style={{ fontFamily: SANS, fontSize: 32, letterSpacing: 4, textTransform: 'uppercase', color: SOFT }}>This one</div>
          <div style={{ fontFamily: SERIF, fontSize: 84, fontWeight: 600, color: INK, lineHeight: 1.05 }}>Problem-solving engine</div>
          <div style={{ padding: '26px 32px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, fontFamily: SERIF, fontSize: 44, color: INK, lineHeight: 1.3 }}>
            "Two blocks hang over a pulley. Find the acceleration."
          </div>
          <div style={{ display: 'flex', gap: 16 }}>
            {['answer', 'formula used', 'every assumption'].map((t, i) => (
              <div key={t} style={{
                padding: '18px 28px', border: `2px solid ${HAIR}`, background: CLAUDE.CARD,
                fontFamily: SANS, fontSize: 38, color: INK, opacity: out(i), whiteSpace: 'nowrap',
              }}>{t}</div>
            ))}
          </div>
        </div>
      </div>
      <RecordStrip
        text="A tool the Medhavy learning platform calls when a student asks a physics question."
        o={remap(p, 0.80, 0.92, 0, 1)}
      />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B03 — the five-step pipeline, lit one step at a time, with the loop-back.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe1Pipeline: React.FC<{ spark?: string }> = ({ spark = 'Five steps.' }) => {
  const p = useP();
  const steps = [
    { n: 'Parse', d: 'knowns, unknowns, units' },
    { n: 'Retrieve', d: 'candidate formula cards' },
    { n: 'Plan', d: 'conditions met? solvable?' },
    { n: 'Solve', d: 'SymPy does the math' },
    { n: 'Verify', d: 'units + a second path' },
  ];
  // Each step owns a slice of the narration; the current one is solid ink.
  const starts = [0.04, 0.16, 0.36, 0.60, 0.72];
  const loop = ease(remap(p, 0.48, 0.58, 0, 1));
  const W = 322, G = 28, TOP = SAFE.y + 190, H = 380;
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + (SAFE.w - (5 * W + 4 * G)) / 2, top: TOP,
        display: 'flex', gap: G,
      }}>
        {steps.map((s, i) => {
          const o = ease(remap(p, starts[i], starts[i] + 0.08, 0, 1));
          const last = i === 4;
          return (
            <div key={s.n} style={{
              width: W, height: H, padding: '32px 26px', background: CLAUDE.CARD,
              border: `${last ? 3 : 2}px solid ${last ? ACCENT : HAIR}`,
              opacity: 0.25 + 0.75 * o, transform: `translateY(${(1 - o) * 20}px)`,
              display: 'flex', flexDirection: 'column', gap: 14,
            }}>
              <div style={{ fontFamily: MONO, fontSize: 30, color: SOFT }}>{`0${i + 1}`}</div>
              <div style={{ fontFamily: SERIF, fontSize: 68, fontWeight: 600, color: last ? ACCENT : INK }}>{s.n}</div>
              <div style={{ fontFamily: SANS, fontSize: 38, lineHeight: 1.3, color: SOFT }}>{s.d}</div>
            </div>
          );
        })}
      </div>
      {/* Loop-back: Plan → Retrieve when a known is missing. */}
      <svg style={{ position: 'absolute', left: 0, top: 0, opacity: loop }} width={1920} height={1080}>
        {(() => {
          const x0 = SAFE.x + (SAFE.w - (5 * W + 4 * G)) / 2;
          const rx = x0 + (W + G) * 1 + W / 2, px = x0 + (W + G) * 2 + W / 2, y = TOP + H;
          return (
            <>
              <path d={`M ${px} ${y + 8} C ${px} ${y + 100}, ${rx} ${y + 100}, ${rx} ${y + 16}`} fill="none" stroke={INK} strokeWidth={4} strokeDasharray="12 10" />
              <polygon points={`${rx - 14},${y + 34} ${rx + 14},${y + 34} ${rx},${y + 10}`} fill={INK} />
              <text x={(rx + px) / 2} y={y + 132} textAnchor="middle" fontFamily={SANS} fontSize={32} fill={SOFT} letterSpacing={2}>GAP? GET ANOTHER CARD</text>
            </>
          );
        })()}
      </svg>
      <RecordStrip
        text="Out comes one solution object: answer, formula, assumptions, checks."
        o={remap(p, 0.86, 0.95, 0, 1)}
      />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B04 — the three routes, decided before solving.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe1Routes: React.FC<{ spark?: string }> = ({ spark = 'Decide first.' }) => {
  const p = useP();
  const q = ease(remap(p, 0.04, 0.16, 0, 1));
  const routes = [
    { k: 'Exactly one card fits', t: 'Final answer', b: 'Same output every time.', code: 'deterministic_script' },
    { k: 'More than one fits', t: 'Every answer back', b: 'The AI picks the formula, not the math.', code: 'ambiguous_multiple_ deterministic_paths' },
    { k: 'None fit', t: 'Says so', b: 'AI takes over; the gap is logged.', code: 'no_deterministic_path' },
  ];
  const starts = [0.18, 0.40, 0.68];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 104, width: SAFE.w,
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 48,
      }}>
        <div style={{
          padding: '18px 52px', border: `3px solid ${ACCENT}`, background: CLAUDE.CARD,
          fontFamily: SERIF, fontSize: 70, color: ACCENT, fontWeight: 600,
          opacity: q, transform: `translateY(${(1 - q) * 22}px)`,
        }}>How many formula cards fit?</div>
        <div style={{ display: 'flex', gap: 34 }}>
          {routes.map((r, i) => {
            const o = ease(remap(p, starts[i], starts[i] + 0.10, 0, 1));
            return (
              <div key={r.k} style={{
                width: 552, minHeight: 400, padding: '36px 38px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`,
                opacity: o, transform: `translateY(${(1 - o) * 24}px)`,
                display: 'flex', flexDirection: 'column', gap: 14,
              }}>
                <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 3, textTransform: 'uppercase', color: SOFT }}>{r.k}</div>
                <div style={{ fontFamily: SERIF, fontSize: 72, fontWeight: 600, color: INK, lineHeight: 1.08 }}>{r.t}</div>
                <div style={{ fontFamily: SANS, fontSize: 40, lineHeight: 1.35, color: INK }}>{r.b}</div>
                <div style={{ fontFamily: MONO, fontSize: 26, color: SOFT, marginTop: 'auto', lineHeight: 1.4 }}>{r.code}</div>
              </div>
            );
          })}
        </div>
      </div>
      <RecordStrip
        text="Deciding first is what makes the answer repeatable."
        o={remap(p, 0.88, 0.96, 0, 1)}
      />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B05 — the receipts. Repo-reported results.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe1Proof: React.FC<{ spark?: string; asOf?: string }> = ({
  spark = 'The receipts.', asOf = 'Repo-reported checks · commit 2dc4aa4 · Oct 2026',
}) => {
  const p = useP();
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 150, width: SAFE.w, height: 440,
        display: 'flex', justifyContent: 'center', gap: 34,
      }}>
        <Tile value="16/16" caption="test problems correct" accent w={520} size={170}
          o={ease(remap(p, 0.06, 0.22, 0, 1))} />
        <Tile value="10×" caption="runs, identical output" w={520} size={170}
          o={ease(remap(p, 0.30, 0.46, 0, 1))} />
        <div style={{
          width: 580, padding: '36px 36px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`, justifyContent: 'center',
          opacity: ease(remap(p, 0.54, 0.70, 0, 1)), transform: `translateY(${(1 - ease(remap(p, 0.54, 0.70, 0, 1))) * 26}px)`,
          display: 'flex', flexDirection: 'column', gap: 14,
        }}>
          <div style={{ fontFamily: SANS, fontSize: 26, letterSpacing: 3, textTransform: 'uppercase', color: SOFT }}>OpenStax pulley problem</div>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline' }}>
            <div style={{ fontFamily: SANS, fontSize: 36, color: SOFT }}>Textbook</div>
            <div style={{ fontFamily: SERIF, fontSize: 88, color: INK, fontWeight: 600 }}>3.27</div>
          </div>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline' }}>
            <div style={{ fontFamily: SANS, fontSize: 36, color: SOFT }}>Engine</div>
            <div style={{ fontFamily: SERIF, fontSize: 88, color: ACCENT, fontWeight: 600 }}>3.2667</div>
          </div>
          <div style={{ fontFamily: SANS, fontSize: 28, color: SOFT }}>metres per second²</div>
        </div>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 630, textAlign: 'center',
        fontFamily: MONO, fontSize: 30, color: SOFT, opacity: remap(p, 0.10, 0.20, 0, 1),
      }}>{asOf}</div>
      <RecordStrip text="Same answer, just not rounded." o={remap(p, 0.84, 0.94, 0, 1)} />
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B06 — what is NOT proven. The team's own list.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe1Honest: React.FC<{ spark?: string; asOf?: string }> = ({
  spark = 'Not proven yet.', asOf = 'As of commit 2dc4aa4 · Oct 2026 · from the team’s EVALUATION.md + COVERAGE.md',
}) => {
  const p = useP();
  const rows = [
    { k: 'Parsing', v: 'unmeasured', d: 'demo inputs arrive already parsed' },
    { k: 'Baseline', v: 'none yet', d: 'plain chatbot not measured on the same set' },
    { k: 'Coverage', v: '180 : 1', d: 'rigid-body problems per card, of 1,226 real problems', hot: true },
    { k: 'Deployed', v: 'no', d: 'no student has used it' },
  ];
  const starts = [0.06, 0.22, 0.42, 0.70];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 80, top: SAFE.y + 104, width: SAFE.w - 160,
        display: 'flex', flexDirection: 'column', gap: 24,
      }}>
        {rows.map((r, i) => {
          const o = ease(remap(p, starts[i], starts[i] + 0.10, 0, 1));
          return (
            <div key={r.k} style={{
              padding: '30px 44px', background: CLAUDE.CARD,
              border: `${r.hot ? 3 : 2}px solid ${r.hot ? ACCENT : HAIR}`, opacity: o,
              transform: `translateX(${(1 - o) * -30}px)`,
              display: 'flex', alignItems: 'center', gap: 40,
            }}>
              <div style={{ width: 260, fontFamily: SANS, fontSize: 32, letterSpacing: 3, textTransform: 'uppercase', color: SOFT }}>{r.k}</div>
              <div style={{ width: 360, fontFamily: SERIF, fontSize: 74, fontWeight: 600, color: r.hot ? ACCENT : INK }}>{r.v}</div>
              <div style={{ flex: 1, fontFamily: SANS, fontSize: 38, lineHeight: 1.3, color: INK }}>{r.d}</div>
            </div>
          );
        })}
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, bottom: 90, textAlign: 'center',
        fontFamily: MONO, fontSize: 28, color: SOFT, opacity: remap(p, 0.08, 0.18, 0, 1),
      }}>{asOf}</div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B07 — the verdict. Three questions to ask of any AI answer.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe1Verdict: React.FC<{ spark?: string }> = ({ spark = 'Ask three things.' }) => {
  const p = useP();
  const qs = ['Who did the math — model or solver?', 'Did anything check the units?', 'Would it say if it didn’t know?'];
  const starts = [0.10, 0.22, 0.32];
  return (
    <IlluStage spark={spark} sparkPos="top">
      <div style={{
        position: 'absolute', left: SAFE.x + 160, top: SAFE.y + 104, width: SAFE.w - 320,
        display: 'flex', flexDirection: 'column', gap: 20,
      }}>
        {qs.map((q, i) => {
          const o = ease(remap(p, starts[i], starts[i] + 0.10, 0, 1));
          return (
            <div key={q} style={{
              padding: '20px 44px', background: CLAUDE.CARD, border: `2px solid ${HAIR}`,
              opacity: o, transform: `translateY(${(1 - o) * 22}px)`,
              display: 'flex', alignItems: 'center', gap: 36,
            }}>
              <div style={{ fontFamily: SERIF, fontSize: 70, fontWeight: 600, color: SOFT, width: 70 }}>{i + 1}</div>
              <div style={{ fontFamily: SERIF, fontSize: 60, color: INK, fontWeight: 600 }}>{q}</div>
            </div>
          );
        })}
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 700, textAlign: 'center',
        fontFamily: SERIF, fontSize: 80, fontWeight: 600, color: INK,
        opacity: ease(remap(p, 0.74, 0.88, 0, 1)),
      }}>
        Words to the model. <span style={{ color: ACCENT }}>Math to the solver.</span>
      </div>
      <div style={{
        position: 'absolute', left: SAFE.x, width: SAFE.w, top: SAFE.y + 830, textAlign: 'center',
        fontFamily: SANS, fontSize: 36, color: SOFT, opacity: remap(p, 0.60, 0.72, 0, 1),
      }}>The numbers will change as the card library grows. The rule won't.</div>
    </IlluStage>
  );
};

/* ────────────────────────────────────────────────────────────────────────────
 * B09 — the outro. Title, terracotta period, host name, credit line.
 * ──────────────────────────────────────────────────────────────────────────── */
export const Pe1Outro: React.FC<{ title?: string; handle?: string; subline?: string }> =
({ title = 'Who Does the Math.', handle = 'Param Madan', subline = 'Physics Engine · 1 of 17' }) => {
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
        fontFamily: SERIF, fontSize: 190, lineHeight: 1.04, fontWeight: 600, color: INK,
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
