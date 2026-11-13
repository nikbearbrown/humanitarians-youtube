import React from 'react';
import { useCurrentFrame, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { useRise, Eyebrow, SparkLine, Page, Card } from './IndexedOrInvisible';
import { Grader } from './EvalCartoon';
import { Robo } from './KidEval';

/**
 * KidDiffusion — the kid-friendly cut of "how static becomes a picture".
 *
 * Subject: a from-scratch diffusion notebook (NumPy only). Unlike the earlier
 * teardown reels this one TEACHES — the notebook is careful work, with a
 * numerical gradient check, real baselines and honest trade-offs.
 *
 * The sprinkle/un-sprinkle scenes implement the notebook's actual forward
 * equation, x_t = sqrt(abar_t) * x0 + sqrt(1 - abar_t) * noise, with a linear
 * beta schedule from 1e-4 to 0.05 over T=200. The animation is the maths.
 *
 * Claude palette only: cream, warm ink, one terracotta.
 */

const S = CLAUDE_FONT.serif;
const U = CLAUDE_FONT.ui;
const M = CLAUDE_FONT.mono;

/** Deterministic per-point gaussian-ish noise (no reseeding across frames). */
const hashNoise = (i: number, k: number) => {
  const s = Math.sin(i * 127.1 + k * 311.7) * 43758.5453;
  const a = s - Math.floor(s);
  const s2 = Math.sin(i * 269.5 + k * 183.3) * 24634.6345;
  const b = s2 - Math.floor(s2);
  // Box–Muller
  return Math.sqrt(-2 * Math.log(a + 1e-6)) * Math.cos(2 * Math.PI * b);
};

/** The notebook's schedule: beta linear 1e-4 -> 0.05, T = 200. */
const T_STEPS = 200;
const ALPHA_BAR: number[] = (() => {
  const out: number[] = [];
  let run = 1;
  for (let i = 0; i < T_STEPS; i++) {
    const beta = 1e-4 + (0.05 - 1e-4) * (i / (T_STEPS - 1));
    run *= 1 - beta;
    out.push(run);
  }
  return out;
})();
const sqrtAB = (t: number) => Math.sqrt(ALPHA_BAR[Math.max(0, Math.min(T_STEPS - 1, Math.round(t)))]);

/** A swiss-roll style spiral, the notebook's toy dataset. */
const SPIRAL = (() => {
  const pts: [number, number][] = [];
  const N = 420;
  for (let i = 0; i < N; i++) {
    const u = i / N;
    const a = 1.6 * Math.PI * (1 + 1.9 * u);
    pts.push([a * Math.cos(a) * 0.055, a * Math.sin(a) * 0.055]);
  }
  return pts;
})();

/** Draw the dataset at diffusion step t, in a box of the given size. */
const Cloud: React.FC<{
  t: number; cx: number; cy: number; size: number; dim?: boolean; r?: number;
}> = ({ t, cx, cy, size, dim, r = 4 }) => {
  const sa = sqrtAB(t);
  const sn = Math.sqrt(1 - sa * sa);
  return (
    <>
      {SPIRAL.map(([x0, y0], i) => {
        const nx = hashNoise(i, 1), ny = hashNoise(i, 2);
        const x = sa * x0 + sn * nx * 0.42;
        const y = sa * y0 + sn * ny * 0.42;
        return (
          <circle key={i} cx={cx + x * size} cy={cy + y * size} r={r}
            fill={CLAUDE.SPARK} opacity={dim ? 0.3 : 0.72} />
        );
      })}
    </>
  );
};

const Stage: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <svg viewBox="0 0 1920 1080" width={1920} height={1080}
    style={{ position: 'absolute', left: 0, top: 0, pointerEvents: 'none' }}>
    {children}
  </svg>
);

// ── 1. KidSprinkle — making the mess ───────────────────────────────────────

export const kidSprinkleSchema = z.object({});

export const KidSprinkle: React.FC = () => {
  const frame = useCurrentFrame();
  const t = interpolate(frame, [18, 150], [0, T_STEPS - 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  const pct = sqrtAB(t) * 100;
  const a = useRise(4);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="step one — wreck the picture on purpose" />
      </div>
      <Stage>
        <Cloud t={t} cx={700} cy={560} size={300} />
      </Stage>
      <div style={{ position: 'absolute', right: 150, top: 330, width: 540, opacity: a }}>
        <div style={{ fontFamily: U, fontSize: 28, color: CLAUDE.INK_SOFT }}>
          sprinkles of mess added
        </div>
        <div style={{ fontFamily: M, fontSize: 86, color: CLAUDE.INK, marginTop: 6 }}>
          {Math.round(t)}<span style={{ fontSize: 40, color: CLAUDE.GHOST }}> / 200</span>
        </div>
        <div style={{ height: 1, background: CLAUDE.BORDER, margin: '28px 0' }} />
        <div style={{ fontFamily: U, fontSize: 28, color: CLAUDE.INK_SOFT }}>
          how much of the drawing is left
        </div>
        <div style={{ fontFamily: M, fontSize: 86, color: CLAUDE.SEND, marginTop: 6 }}>
          {pct.toFixed(1)}%
        </div>
        <div style={{
          marginTop: 20, height: 26, borderRadius: 13, background: CLAUDE.PILL, overflow: 'hidden',
        }}>
          <div style={{ width: `${pct}%`, height: '100%', background: CLAUDE.SPARK }} />
        </div>
      </div>
      <SparkLine text="Two hundred tiny sprinkles, and the spiral is gone." delay={158} />
    </Page>
  );
};

// ── 2. KidMessSpotter — the one question ───────────────────────────────────

export const kidMessSpotterSchema = z.object({});

export const KidMessSpotter: React.FC = () => {
  const frame = useCurrentFrame();
  const wrong = useRise(16);
  const right = useRise(46);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="the only question the machine is asked" />
      </div>
      <Stage>
        <Cloud t={118} cx={440} cy={500} size={250} r={3.4} />
      </Stage>
      <Robo x={1150} y={430} scale={1.9} frame={frame} />
      <div style={{ position: 'absolute', left: 820, top: 620, right: 120 }}>
        <div style={{ opacity: wrong, marginBottom: 26 }}>
          <Card style={{ padding: '22px 28px', opacity: 0.5 }}>
            <span style={{ fontFamily: U, fontSize: 21, letterSpacing: 2, color: CLAUDE.GHOST }}>NOT</span>
            <div style={{ fontFamily: S, fontSize: 40, color: CLAUDE.GHOST, marginTop: 8 }}>
              “What is this a picture of?”
            </div>
          </Card>
        </div>
        <div style={{ opacity: right, transform: `scale(${0.92 + 0.08 * right})` }}>
          <Card accent style={{ padding: '26px 30px', background: '#FBEEE8' }}>
            <span style={{ fontFamily: U, fontSize: 21, letterSpacing: 2, color: CLAUDE.SEND }}>INSTEAD</span>
            <div style={{ fontFamily: S, fontSize: 48, color: CLAUDE.INK, marginTop: 8 }}>
              “Which bit of this is the mess?”
            </div>
          </Card>
        </div>
      </div>
      <SparkLine text="It never has to know it is a spiral. It only has to spot the sprinkles." delay={64} />
    </Page>
  );
};

// ── 3. KidUnsprinkle — brushing the mess back off ──────────────────────────

export const kidUnsprinkleSchema = z.object({});

export const KidUnsprinkle: React.FC = () => {
  const frame = useCurrentFrame();
  const t = interpolate(frame, [14, 160], [T_STEPS - 1, 0], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  const done = useRise(168);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="step two — take the mess back off, a little at a time" />
      </div>
      <Stage>
        <Cloud t={t} cx={760} cy={540} size={300} />
      </Stage>
      <div style={{ position: 'absolute', right: 150, top: 380, width: 520 }}>
        <div style={{ fontFamily: U, fontSize: 28, color: CLAUDE.INK_SOFT }}>sprinkles removed</div>
        <div style={{ fontFamily: M, fontSize: 86, color: CLAUDE.INK, marginTop: 6 }}>
          {Math.round(T_STEPS - 1 - t)}<span style={{ fontSize: 40, color: CLAUDE.GHOST }}> / 200</span>
        </div>
        {done > 0.02 ? (
          <div style={{ marginTop: 34, opacity: done }}>
            <div style={{ fontFamily: S, fontSize: 48, color: CLAUDE.INK, lineHeight: 1.3 }}>
              A spiral nobody drew.
            </div>
          </div>
        ) : null}
      </div>
      <SparkLine text="It started from pure static. Nothing of the original was left." delay={172} />
    </Page>
  );
};

// ── 4. KidTwoWaysCheck — the gradient check ────────────────────────────────

export const kidTwoWaysCheckSchema = z.object({
  worstErr: z.string().default('1.5e-07'),
});
export type KidTwoWaysCheckProps = z.infer<typeof kidTwoWaysCheckSchema>;

export const KidTwoWaysCheck: React.FC<KidTwoWaysCheckProps> = ({ worstErr }) => {
  const frame = useCurrentFrame();
  const a = useRise(8);
  const b = useRise(26);
  const match = useRise(52);
  const ROWS = [
    ['-1.215836', '-1.215836'],
    ['+0.521207', '+0.521207'],
    ['+0.655957', '+0.655957'],
  ];
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="did they check their own homework?" />
      </div>
      <Stage>
        <Grader x={300} y={470} scale={1.9} mood="neutral" />
      </Stage>
      <Robo x={1640} y={450} scale={1.7} frame={frame} happy={match > 0.5} />
      <div style={{ position: 'absolute', left: 540, top: 250, width: 900 }}>
        <div style={{ display: 'flex', gap: 40, marginBottom: 18, opacity: a }}>
          <div style={{ flex: 1, fontFamily: U, fontSize: 24, letterSpacing: 2, color: CLAUDE.INK_SOFT }}>
            WORKED OUT BY HAND
          </div>
          <div style={{ flex: 1, fontFamily: U, fontSize: 24, letterSpacing: 2, color: CLAUDE.SEND }}>
            CHECKED BY COUNTING
          </div>
        </div>
        {ROWS.map(([x, y], i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(12 + i * 10);
          return (
            <div key={i} style={{ display: 'flex', gap: 40, marginBottom: 14, opacity: t }}>
              <div style={{ flex: 1 }}>
                <Card style={{ padding: '16px 22px', fontFamily: M, fontSize: 30, color: CLAUDE.INK }}>{x}</Card>
              </div>
              <div style={{ flex: 1, opacity: b }}>
                <Card style={{ padding: '16px 22px', fontFamily: M, fontSize: 30, color: CLAUDE.INK }}>{y}</Card>
              </div>
            </div>
          );
        })}
        {match > 0.02 ? (
          <div style={{ marginTop: 34, opacity: match }}>
            <Card accent style={{ padding: '26px 30px', background: '#FBEEE8' }}>
              <div style={{ fontFamily: S, fontSize: 44, color: CLAUDE.INK, lineHeight: 1.3 }}>
                Same answers, to seven decimal places.
              </div>
              <div style={{ fontFamily: M, fontSize: 26, color: CLAUDE.SEND, marginTop: 12 }}>
                worst difference: {worstErr}
              </div>
            </Card>
          </div>
        ) : null}
      </div>
      <SparkLine text="Two ways of working it out. One answer. That is how you know." delay={62} />
    </Page>
  );
};

// ── 5. KidBigSteps — DDPM vs DDIM ──────────────────────────────────────────

export const kidBigStepsSchema = z.object({
  rows: z.array(z.object({
    steps: z.string(), score: z.string(), ok: z.boolean(),
  })).default([]),
});
export type KidBigStepsProps = z.infer<typeof kidBigStepsSchema>;

export const KidBigSteps: React.FC<KidBigStepsProps> = ({ rows }) => {
  const frame = useCurrentFrame();
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="can we go faster? take bigger steps" />
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 190 }}>
        {rows.map((r, i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(8 + i * 16);
          const stepsN = parseInt(r.steps, 10) || 20;
          // many sampler steps -> many small footprints; few steps -> few big strides
          const n = Math.max(4, Math.min(26, Math.round(Math.sqrt(stepsN) * 1.9)));
          const dot = Math.max(14, Math.min(42, Math.round(150 / Math.sqrt(stepsN))));
          const stride = 1100 / n;
          const fell = !r.ok;
          return (
            <div key={r.steps} style={{ marginBottom: 30, opacity: t }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 26 }}>
                <span style={{ fontFamily: M, fontSize: 30, color: CLAUDE.INK, width: 200, whiteSpace: 'nowrap' }}>
                  {r.steps}
                </span>
                <div style={{ position: 'relative', flex: 1, height: 54 }}>
                  {Array.from({ length: n }, (_, k) => {
                    const appear = interpolate(frame, [10 + i * 16 + k * 1.2, 18 + i * 16 + k * 1.2],
                      [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
                    const last = fell && k === n - 1;
                    return (
                      <div key={k} style={{
                        position: 'absolute', left: k * stride, top: last ? 30 : 27 - dot / 2,
                        width: dot, height: last ? Math.round(dot * 0.45) : dot,
                        borderRadius: last ? dot / 3 : dot / 2,
                        background: fell ? CLAUDE.GHOST : CLAUDE.SPARK,
                        opacity: appear, transform: last ? 'rotate(34deg)' : 'none',
                      }} />
                    );
                  })}
                </div>
                <span style={{
                  fontFamily: M, fontSize: 28, width: 170, textAlign: 'right',
                  color: r.ok ? CLAUDE.INK : CLAUDE.SEND,
                }}>{r.score}</span>
                <span style={{
                  fontFamily: U, fontSize: 22, width: 150,
                  color: r.ok ? CLAUDE.INK_SOFT : CLAUDE.SEND,
                }}>{r.ok ? 'still a spiral' : 'falls apart'}</span>
              </div>
            </div>
          );
        })}
      </div>
      <SparkLine text="Fewer, bigger steps — until the steps are too big to land." delay={92} />
    </Page>
  );
};

// ── 6. KidJudgeScore — the scoreboard ──────────────────────────────────────

export const kidJudgeScoreSchema = z.object({
  rows: z.array(z.object({
    label: z.string(), score: z.string(), bar: z.number(), hero: z.boolean(),
  })).default([]),
});
export type KidJudgeScoreProps = z.infer<typeof kidJudgeScoreSchema>;

export const KidJudgeScore: React.FC<KidJudgeScoreProps> = ({ rows }) => {
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="a judge scores how real it looks — lower is better" />
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 180 }}>
        {rows.map((r, i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(6 + i * 11);
          return (
            <div key={r.label} style={{
              display: 'flex', alignItems: 'center', gap: 22, marginBottom: 20, opacity: t,
            }}>
              <span style={{
                fontFamily: U, fontSize: 25, width: 330,
                color: r.hero ? CLAUDE.INK : CLAUDE.INK_SOFT,
                fontWeight: r.hero ? 600 : 400,
              }}>{r.label}</span>
              <div style={{ flex: 1, height: 36, background: CLAUDE.PILL, borderRadius: 8, overflow: 'hidden' }}>
                <div style={{
                  width: `${Math.max(1.2, r.bar * 100 * t)}%`, height: '100%',
                  background: r.hero ? CLAUDE.SPARK : CLAUDE.GHOST, borderRadius: 8,
                }} />
              </div>
              <span style={{ fontFamily: M, fontSize: 26, width: 150, textAlign: 'right', color: CLAUDE.INK }}>
                {r.score}
              </span>
            </div>
          );
        })}
      </div>
      <SparkLine text="The made-up spirals land almost on top of the real ones." delay={92} />
    </Page>
  );
};

// ── 7. KidSteerDial — guidance trade-off ───────────────────────────────────

export const kidSteerDialSchema = z.object({
  rows: z.array(z.object({
    w: z.string(), acc: z.string(), spread: z.string(), accN: z.number(), spreadN: z.number(),
  })).default([]),
});
export type KidSteerDialProps = z.infer<typeof kidSteerDialSchema>;

export const KidSteerDial: React.FC<KidSteerDialProps> = ({ rows }) => {
  const frame = useCurrentFrame();
  const idx = Math.min(rows.length - 1,
    Math.floor(interpolate(frame, [16, 150], [0, rows.length], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' })));
  const row = rows[Math.max(0, idx)] || { w: '0', acc: '', spread: '', accN: 0, spreadN: 1 };
  const ang = -120 + 240 * (idx / Math.max(1, rows.length - 1));
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="now tell it which shape you want" />
      </div>

      {/* the dial */}
      <div style={{ position: 'absolute', left: 230, top: 300 }}>
        <svg width={360} height={360} viewBox="0 0 360 360">
          <circle cx={180} cy={180} r={128} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={3} />
          <circle cx={180} cy={180} r={128} fill="none" stroke={CLAUDE.PILL} strokeWidth={16} />
          <g transform={`rotate(${ang} 180 180)`}>
            <line x1={180} y1={180} x2={180} y2={74} stroke={CLAUDE.SPARK} strokeWidth={10} strokeLinecap="round" />
          </g>
          <circle cx={180} cy={180} r={17} fill={CLAUDE.INK} />
          <text x={180} y={300} textAnchor="middle"
            style={{ fontFamily: M, fontSize: 40, fill: CLAUDE.INK }}>w = {row.w}</text>
        </svg>
      </div>

      {/* the two numbers */}
      <div style={{ position: 'absolute', left: 720, top: 300, right: 130 }}>
        <div style={{ marginBottom: 46 }}>
          <div style={{ fontFamily: U, fontSize: 27, color: CLAUDE.INK_SOFT }}>lands on the shape you asked for</div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 22, marginTop: 10 }}>
            <div style={{ flex: 1, height: 44, background: CLAUDE.PILL, borderRadius: 10, overflow: 'hidden' }}>
              <div style={{ width: `${row.accN * 100}%`, height: '100%', background: CLAUDE.SPARK }} />
            </div>
            <span style={{ fontFamily: M, fontSize: 38, color: CLAUDE.INK, width: 150, textAlign: 'right' }}>
              {row.acc}
            </span>
          </div>
        </div>
        <div>
          <div style={{ fontFamily: U, fontSize: 27, color: CLAUDE.INK_SOFT }}>how different the shapes are</div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 22, marginTop: 10 }}>
            <div style={{ flex: 1, height: 44, background: CLAUDE.PILL, borderRadius: 10, overflow: 'hidden' }}>
              <div style={{ width: `${row.spreadN * 100}%`, height: '100%', background: CLAUDE.INK_SOFT }} />
            </div>
            <span style={{ fontFamily: M, fontSize: 38, color: CLAUDE.INK, width: 150, textAlign: 'right' }}>
              {row.spread}
            </span>
          </div>
        </div>
        <div style={{ marginTop: 44, fontFamily: S, fontSize: 42, color: CLAUDE.INK, lineHeight: 1.3 }}>
          One goes up. The other goes down.
        </div>
      </div>
      <SparkLine text="You can buy obedience. You pay for it in variety." delay={156} />
    </Page>
  );
};
