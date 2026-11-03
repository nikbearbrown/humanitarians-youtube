import React from 'react';
import { useCurrentFrame, useVideoConfig, interpolate, spring } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { useRise, Eyebrow, SparkLine, Page, Card } from './IndexedOrInvisible';
import { Grader } from './EvalCartoon';

/**
 * SynthData — scene set for "The Test That Couldn't Fail".
 *
 * Subject: a CTGAN synthetic-data notebook whose evaluation declares success on
 * results that, read literally, are failures. Every number rendered here was
 * reproduced by re-running the notebook's own dataset code at seed 42.
 *
 * Motion brief: heavier than the Idx/Eval sets — particle systems, physical
 * metaphors, a two-character duel. Still palette-only (cream / ink / terracotta),
 * still duration-agnostic (everything settles early and holds).
 */

const S = CLAUDE_FONT.serif;
const U = CLAUDE_FONT.ui;
const M = CLAUDE_FONT.mono;

const GHOSTBAR = CLAUDE.PILL;

/** deterministic pseudo-random so renders are reproducible frame to frame */
const rnd = (i: number, salt = 1) => {
  const x = Math.sin(i * 12.9898 * salt + 78.233) * 43758.5453;
  return x - Math.floor(x);
};
/** box–muller-ish bell from two uniforms */
const bell = (i: number, salt = 1) => {
  const u = Math.max(1e-6, rnd(i, salt));
  const v = rnd(i + 1000, salt);
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
};

// ── 1. SynthGanDuel — generator vs discriminator, as a tug of war ───────────

export const synthGanDuelSchema = z.object({});

export const SynthGanDuel: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const inn = useRise(4);
  // the rope oscillates, converging toward the middle as they reach equilibrium
  const decay = Math.exp(-frame / 90);
  const pull = Math.sin(frame / 7.5) * 90 * decay;
  const settle = 1 - decay;
  const lean = Math.sin(frame / 7.5) * 7 * decay;

  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="how a GAN is trained" />
      </div>

      <svg width="100%" height="100%" style={{ position: 'absolute', inset: 0, opacity: inn }}>
        {/* the rope */}
        <line x1={620 + pull} y1={520} x2={1300 + pull} y2={520}
          stroke={CLAUDE.INK_SOFT} strokeWidth={5} strokeLinecap="round" />
        {/* centre marker */}
        <line x1={960} y1={470} x2={960} y2={570} stroke={CLAUDE.SPARK}
          strokeWidth={3} strokeDasharray="8 8" opacity={0.55} />
        <Grader x={470 + pull} y={520} scale={2.0} mood="stern" lean={lean} />
        <Grader x={1450 + pull} y={520} scale={2.0} mood="pleased" lean={-lean} />
      </svg>

      <div style={{ position: 'absolute', left: 150, top: 640, width: 460, textAlign: 'center', opacity: inn }}>
        <div style={{ fontFamily: U, fontSize: 30, fontWeight: 600, color: CLAUDE.INK }}>GENERATOR</div>
        <div style={{ fontFamily: U, fontSize: 23, color: CLAUDE.INK_SOFT, marginTop: 8 }}>
          invents rows that look real
        </div>
      </div>
      <div style={{ position: 'absolute', right: 150, top: 640, width: 460, textAlign: 'center', opacity: inn }}>
        <div style={{ fontFamily: U, fontSize: 30, fontWeight: 600, color: CLAUDE.INK }}>DISCRIMINATOR</div>
        <div style={{ fontFamily: U, fontSize: 23, color: CLAUDE.INK_SOFT, marginTop: 8 }}>
          tries to spot the fakes
        </div>
      </div>

      <div style={{
        position: 'absolute', left: 0, right: 0, top: 810, textAlign: 'center',
        opacity: settle, transform: `translateY(${(1 - settle) * 14}px)`,
      }}>
        <span style={{ fontFamily: S, fontSize: 46, color: CLAUDE.INK }}>
          They stop when neither can win.
        </span>
      </div>

      <SparkLine text="Equilibrium is the training signal — not accuracy." delay={70} />
    </Page>
  );
};

// ── 2. SynthRandomReveal — the "real" data is np.random ─────────────────────

export const synthRandomRevealSchema = z.object({});

const COLS: [string, string][] = [
  ['Age', 'np.random.randint(20, 80)'],
  ['BMI', 'np.random.normal(27, 4.0)'],
  ['BloodPressure', 'np.random.randint(90, 180)'],
  ['Cholesterol', 'np.random.randint(120, 300)'],
  ['GlucoseLevel', 'np.random.normal(110, 25)'],
  ['SleepHours', 'np.random.normal(6.8, 1.2)'],
  ['Diabetes', 'np.random.choice([0, 1])'],
];

export const SynthRandomReveal: React.FC = () => {
  const stamp = useRise(70, 18);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 70 }}>
        <Eyebrow text="what the “real” dataset actually is" />
      </div>

      <div style={{ position: 'absolute', left: 130, right: 130, top: 172 }}>
        {COLS.map(([name, call], i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(5 + i * 8);
          return (
            <div key={name} style={{
              display: 'flex', alignItems: 'center', gap: 26, marginBottom: 11,
              opacity: t, transform: `translateX(${(1 - t) * -18}px)`,
            }}>
              <div style={{ width: 300, fontFamily: U, fontSize: 28, color: CLAUDE.INK }}>{name}</div>
              <Card style={{ flex: 1, padding: '13px 22px' }}>
                <span style={{ fontFamily: M, fontSize: 24, color: CLAUDE.INK_SOFT }}>{call}</span>
              </Card>
            </div>
          );
        })}
      </div>

      <div style={{
        position: 'absolute', right: 150, top: 300,
        transform: `rotate(-11deg) scale(${0.7 + stamp * 0.3})`, opacity: stamp,
      }}>
        <div style={{
          border: `5px solid ${CLAUDE.SPARK}`, borderRadius: 12, padding: '16px 30px',
          background: 'rgba(250,249,245,0.92)',
        }}>
          <span style={{
            fontFamily: U, fontSize: 46, fontWeight: 700, letterSpacing: 3,
            color: CLAUDE.SPARK,
          }}>DRAWN INDEPENDENTLY</span>
        </div>
      </div>

      <SparkLine text="No column was allowed to depend on any other." delay={86} />
    </Page>
  );
};

// ── 3. SynthParticleHist — 10,000 points forming, then morphing ─────────────

export const synthParticleHistSchema = z.object({});

const NPART = 460;
const BINS = 26;

export const SynthParticleHist: React.FC = () => {
  const frame = useCurrentFrame();
  const fly = interpolate(frame, [6, 56], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const morph = interpolate(frame, [86, 140], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const label = useRise(96);

  const L = 190, R = 1730, TOP = 250, BOT = 700;
  const bw = (R - L) / BINS;

  // real: tight bell. synthetic: slightly wider + shifted (what CTGAN actually produced)
  const counts = { real: new Array(BINS).fill(0), syn: new Array(BINS).fill(0) };
  const pts: { bin: number; kR: number; kS: number }[] = [];
  for (let i = 0; i < NPART; i++) {
    const zr = bell(i, 1) * 0.135 + 0.52;
    const zs = bell(i, 2.7) * 0.168 + 0.545;
    const br = Math.max(0, Math.min(BINS - 1, Math.floor(zr * BINS)));
    const bs = Math.max(0, Math.min(BINS - 1, Math.floor(zs * BINS)));
    pts.push({ bin: br, kR: counts.real[br]++, kS: counts.syn[bs]++ });
    (pts[i] as any).binS = bs;
  }

  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 70 }}>
        <Eyebrow text="ten thousand rows, one distribution" />
      </div>

      <svg width="100%" height="100%" style={{ position: 'absolute', inset: 0 }}>
        <line x1={L} y1={BOT} x2={R} y2={BOT} stroke={CLAUDE.BORDER} strokeWidth={2} />
        {pts.map((p, i) => {
          const bS = (p as any).binS as number;
          const binNow = p.bin + (bS - p.bin) * morph;
          const kNow = p.kR + (p.kS - p.kR) * morph;
          const tx = L + binNow * bw + bw / 2;
          const ty = BOT - 8 - kNow * 11;
          // fly in from a scattered cloud
          const sx = L + rnd(i, 3) * (R - L);
          const sy = TOP + rnd(i, 5) * (BOT - TOP);
          const e = fly * fly * (3 - 2 * fly);
          const x = sx + (tx - sx) * e;
          const y = sy + (ty - sy) * e;
          const col = morph > 0.5 ? CLAUDE.SPARK : CLAUDE.INK_SOFT;
          return <circle key={i} cx={x} cy={y} r={4.4} fill={col} opacity={0.72} />;
        })}
      </svg>

      <div style={{
        position: 'absolute', left: 130, top: 760, opacity: label,
      }}>
        <div style={{ fontFamily: S, fontSize: 46, color: CLAUDE.INK }}>
          {morph > 0.5 ? 'Synthetic: the same shape, slightly wider.' : 'Real: a bell, because it was drawn as one.'}
        </div>
      </div>

      <SparkLine text="Reproducing a marginal is the easiest thing a generator can do." delay={128} />
    </Page>
  );
};

// ── 4. SynthPValueRain — seven p-values, all zero ───────────────────────────

export const synthPValueRainSchema = z.object({});

const PVALS: [string, string][] = [
  ['Age', '0.0000'], ['BMI', '0.0000'], ['BloodPressure', '0.0003'],
  ['Cholesterol', '0.0000'], ['GlucoseLevel', '0.0000'],
  ['SleepHours', '0.0000'], ['HealthRiskScore', '0.0000'],
];

export const SynthPValueRain: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const line = useRise(6);
  const verdict = useRise(104, 20);
  const LINE_Y = 470;

  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 70 }}>
        <Eyebrow text="the rule the notebook wrote down" />
      </div>

      {/* the threshold */}
      <div style={{
        position: 'absolute', left: 130, right: 130, top: LINE_Y, opacity: line,
      }}>
        <div style={{ borderTop: `3px dashed ${CLAUDE.SPARK}` }} />
        <div style={{
          fontFamily: M, fontSize: 24, color: CLAUDE.SPARK, marginTop: 8,
        }}>p &gt; 0.05  →  “statistically similar”</div>
      </div>

      {/* falling p-values */}
      {PVALS.map(([name, p], i) => {
        const t0 = 14 + i * 9;
        const drop = spring({ frame: frame - t0, fps, config: { damping: 14, stiffness: 90, mass: 1.1 } });
        const y = 200 + drop * 420;
        const x = 190 + i * 232;
        return (
          <div key={name} style={{
            position: 'absolute', left: x, top: y, width: 210, textAlign: 'center',
            opacity: drop > 0.02 ? 1 : 0,
          }}>
            <div style={{ fontFamily: M, fontSize: 40, color: CLAUDE.SEND }}>{p}</div>
            <div style={{ fontFamily: U, fontSize: 18, color: CLAUDE.INK_SOFT, marginTop: 6 }}>{name}</div>
          </div>
        );
      })}

      <div style={{
        position: 'absolute', left: 0, right: 0, top: 830, textAlign: 'center',
        opacity: verdict, transform: `scale(${0.9 + verdict * 0.1})`,
      }}>
        <span style={{ fontFamily: S, fontSize: 62, color: CLAUDE.INK }}>
          Seven out of seven. All below the line.
        </span>
      </div>

      <SparkLine text="By the notebook's own criterion, every numeric column failed." delay={122} />
    </Page>
  );
};

// ── 5. SynthMovingGoalpost — the criterion slides ───────────────────────────

export const synthMovingGoalpostSchema = z.object({});

export const SynthMovingGoalpost: React.FC = () => {
  const frame = useCurrentFrame();
  const slide = interpolate(frame, [50, 96], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const ease = slide * slide * (3 - 2 * slide);
  const inn = useRise(4);
  const ks = [0.069, 0.092, 0.030, 0.051, 0.049, 0.098, 0.050];
  const names = ['Age', 'BMI', 'BP', 'Chol', 'Gluc', 'Sleep', 'Risk'];

  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 70 }}>
        <Eyebrow text={ease > 0.5 ? 'the rule the summary used' : 'the rule as written'} />
      </div>

      <div style={{ position: 'absolute', left: 150, right: 150, top: 210, opacity: inn }}>
        {/* the criterion card — slides across and swaps */}
        <div style={{
          transform: `translateX(${ease * 760}px)`,
          width: 640,
        }}>
          <Card accent style={{ padding: '22px 28px', background: '#FBEEE8' }}>
            <div style={{ fontFamily: U, fontSize: 21, letterSpacing: 2, color: CLAUDE.SPARK }}>
              {ease > 0.5 ? 'CRITERION — AS SUMMARISED' : 'CRITERION — AS STATED'}
            </div>
            <div style={{ fontFamily: M, fontSize: 32, color: CLAUDE.INK, marginTop: 12 }}>
              {ease > 0.5 ? 'KS statistic < 0.1' : 'p-value > 0.05'}
            </div>
          </Card>
        </div>

        {/* the seven columns, judged by whichever rule is live */}
        <div style={{ display: 'flex', gap: 20, marginTop: 60, alignItems: 'flex-end' }}>
          {ks.map((v, i) => {
            const pass = ease > 0.5;   // under KS<0.1 all pass; under p>0.05 none do
            return (
              <div key={names[i]} style={{ flex: 1, textAlign: 'center' }}>
                <div style={{
                  height: 30 + v * 1900, borderRadius: 10,
                  background: pass ? '#FBEEE8' : GHOSTBAR,
                  border: `2px solid ${pass ? CLAUDE.SPARK : CLAUDE.GHOST}`,
                  transition: 'none',
                }} />
                <div style={{ fontFamily: M, fontSize: 21, color: CLAUDE.INK, marginTop: 12 }}>{v.toFixed(3)}</div>
                <div style={{ fontFamily: U, fontSize: 18, color: CLAUDE.INK_SOFT, marginTop: 4 }}>{names[i]}</div>
                <div style={{
                  fontFamily: U, fontSize: 19, fontWeight: 700, marginTop: 10,
                  letterSpacing: 1.5, color: pass ? CLAUDE.SPARK : CLAUDE.GHOST,
                }}>{pass ? 'PASS' : 'FAIL'}</div>
              </div>
            );
          })}
        </div>
      </div>

      <SparkLine text="Same seven numbers. The goalpost moved, not the data." delay={104} />
    </Page>
  );
};

// ── 6. SynthChiSquareProof — the test that measures nothing ─────────────────

export const synthChiSquareProofSchema = z.object({});

export const SynthChiSquareProof: React.FC = () => {
  const a = useRise(5);
  const shuffle = useRise(34);
  const result = useRise(64, 20);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="a test that cannot detect what it claims to" />
      </div>

      <div style={{ position: 'absolute', left: 130, right: 130, top: 180 }}>
        <Card style={{ padding: '22px 28px', opacity: a }}>
          <span style={{ fontFamily: M, fontSize: 24, color: CLAUDE.INK_SOFT }}>
            chi2_contingency(pd.crosstab(real[col], synthetic[col]))
          </span>
        </Card>

        <div style={{ marginTop: 34, fontFamily: U, fontSize: 30, color: CLAUDE.INK, opacity: shuffle }}>
          The control: shuffle one column. The marginals are now <em>identical</em> by construction.
        </div>

        <div style={{ display: 'flex', gap: 24, marginTop: 30, opacity: result }}>
          {[['Gender', '0.5693'], ['Smoking', '0.3430'], ['PhysicalActivity', '0.5790']].map(([c, p]) => (
            <Card key={c} style={{ flex: 1, padding: '26px 24px', textAlign: 'center' }}>
              <div style={{ fontFamily: U, fontSize: 22, color: CLAUDE.INK_SOFT }}>{c}</div>
              <div style={{ fontFamily: M, fontSize: 46, color: CLAUDE.SEND, marginTop: 12 }}>p={p}</div>
              <div style={{ fontFamily: U, fontSize: 20, color: CLAUDE.SPARK, marginTop: 10 }}>“similar”</div>
            </Card>
          ))}
        </div>

        <div style={{ marginTop: 36, opacity: result }}>
          <Card accent style={{ padding: '26px 30px', background: '#FBEEE8' }}>
            <div style={{ fontFamily: S, fontSize: 44, color: CLAUDE.INK, lineHeight: 1.3 }}>
              It passes when the columns match — and passes when they are unrelated.
            </div>
          </Card>
        </div>
      </div>

      <SparkLine text="A test that always passes is not evidence. It is decoration." delay={86} />
    </Page>
  );
};

// ── 7. SynthBaseRate — the model that only ever says No ─────────────────────

export const synthBaseRateSchema = z.object({});

export const SynthBaseRate: React.FC = () => {
  const frame = useCurrentFrame();
  const inn = useRise(4);
  const n = Math.min(9, Math.floor(interpolate(frame, [16, 96], [0, 9], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' })));
  const acc = useRise(100, 20);
  const bob = Math.sin(frame / 11) * 5;

  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="what the model actually learned" />
      </div>

      <svg width="100%" height="100%" style={{ position: 'absolute', inset: 0, opacity: inn }}>
        <Grader x={330} y={470 + bob} scale={2.2} mood="pleased" />
      </svg>

      <div style={{ position: 'absolute', left: 560, top: 240, right: 130 }}>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 14, width: 900 }}>
          {Array.from({ length: 9 }, (_, i) => (
            <div key={i} style={{
              width: 168, padding: '14px 0', textAlign: 'center', borderRadius: 10,
              background: i < n ? CLAUDE.CARD : 'transparent',
              border: `2px solid ${i < n ? CLAUDE.BORDER : 'transparent'}`,
              opacity: i < n ? 1 : 0,
              fontFamily: U, fontSize: 26, color: CLAUDE.INK,
            }}>“No”</div>
          ))}
        </div>

        <div style={{ marginTop: 44, opacity: acc, display: 'flex', gap: 60, alignItems: 'baseline' }}>
          <div>
            <div style={{ fontFamily: M, fontSize: 76, color: CLAUDE.INK }}>0.785</div>
            <div style={{ fontFamily: U, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 6 }}>TSTR accuracy</div>
          </div>
          <div>
            <div style={{ fontFamily: M, fontSize: 76, color: CLAUDE.SEND }}>0.7847</div>
            <div style={{ fontFamily: U, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 6 }}>base rate of “No”</div>
          </div>
        </div>
      </div>

      <SparkLine text="It never once predicted diabetes. F1 was exactly zero." delay={116} />
    </Page>
  );
};

// ── 8. SynthControlRun — the control nobody ran ─────────────────────────────

export const synthControlRunSchema = z.object({});

export const SynthControlRun: React.FC = () => {
  const a = useRise(5);
  const b = useRise(40);
  const punch = useRise(76, 18);
  const row = (title: string, sub: string, acc: string, f1: string, t: number, accent: boolean) => (
    <div style={{ flex: 1, opacity: t, transform: `translateY(${(1 - t) * 18}px)` }}>
      <Card accent={accent} style={{ padding: '28px 30px', background: accent ? '#FBEEE8' : CLAUDE.CARD }}>
        <div style={{ fontFamily: U, fontSize: 21, letterSpacing: 2, color: accent ? CLAUDE.SPARK : CLAUDE.INK_SOFT }}>{title}</div>
        <div style={{ fontFamily: U, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 10 }}>{sub}</div>
        <div style={{ display: 'flex', gap: 46, marginTop: 22 }}>
          <div><div style={{ fontFamily: M, fontSize: 48, color: CLAUDE.INK }}>{acc}</div>
            <div style={{ fontFamily: U, fontSize: 19, color: CLAUDE.INK_SOFT }}>accuracy</div></div>
          <div><div style={{ fontFamily: M, fontSize: 48, color: CLAUDE.SEND }}>{f1}</div>
            <div style={{ fontFamily: U, fontSize: 19, color: CLAUDE.INK_SOFT }}>F1</div></div>
        </div>
      </Card>
    </div>
  );
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="the control the notebook never ran" />
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 200, display: 'flex', gap: 30 }}>
        {row('TRAIN SYNTHETIC → TEST REAL', 'the notebook’s experiment', '0.785', '0.000', a, false)}
        {row('TRAIN REAL → TEST REAL', 'the same data, no GAN involved', '0.785', '0.000', b, true)}
      </div>
      <div style={{
        position: 'absolute', left: 130, right: 130, top: 620,
        opacity: punch, transform: `translateY(${(1 - punch) * 16}px)`,
      }}>
        <div style={{ fontFamily: S, fontSize: 60, color: CLAUDE.INK, lineHeight: 1.24 }}>
          Real data scores exactly the same.<br />The synthetic data was never the problem.
        </div>
      </div>
      <SparkLine text="Zero positive predictions, either way." delay={96} />
    </Page>
  );
};

// ── 9. SynthCorrelationGrid — searching for signal that isn't there ─────────

export const synthCorrelationGridSchema = z.object({});

const CORRS: [string, number][] = [
  ['Age', -0.0024], ['BMI', -0.0065], ['BloodPressure', -0.0139],
  ['Cholesterol', 0.0007], ['GlucoseLevel', -0.0099], ['SleepHours', 0.0097],
];

export const SynthCorrelationGrid: React.FC = () => {
  const frame = useCurrentFrame();
  const closing = useRise(92, 20);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="correlation with the prediction target" />
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 190 }}>
        {CORRS.map(([name, r], i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(6 + i * 11);
          const w = Math.abs(r) * 5200;   // exaggerated so the bar is visible at all
          return (
            <div key={name} style={{
              display: 'flex', alignItems: 'center', gap: 24, marginBottom: 16, opacity: t,
            }}>
              <div style={{ width: 330, fontFamily: U, fontSize: 27, color: CLAUDE.INK }}>{name}</div>
              <div style={{ flex: 1, height: 30, background: GHOSTBAR, borderRadius: 6, position: 'relative' }}>
                <div style={{
                  position: 'absolute', left: '50%', top: 0, bottom: 0, width: 2, background: CLAUDE.GHOST,
                }} />
                <div style={{
                  position: 'absolute', top: 4, bottom: 4, borderRadius: 4,
                  background: CLAUDE.SPARK,
                  left: r < 0 ? `calc(50% - ${w}px)` : '50%', width: Math.max(3, w),
                }} />
              </div>
              <div style={{ width: 150, textAlign: 'right', fontFamily: M, fontSize: 26, color: CLAUDE.INK_SOFT }}>
                {r >= 0 ? '+' : ''}{r.toFixed(4)}
              </div>
            </div>
          );
        })}
      </div>
      <div style={{
        position: 'absolute', left: 130, right: 130, top: 700, opacity: closing,
      }}>
        <Card accent style={{ padding: '28px 32px', background: '#FBEEE8' }}>
          <div style={{ fontFamily: S, fontSize: 48, color: CLAUDE.INK, lineHeight: 1.28 }}>
            Every bar is noise. There was never a pattern to learn.
          </div>
        </Card>
      </div>
      <SparkLine text="Bars magnified 5,000× to be visible at all." delay={110} />
    </Page>
  );
};

// ── 10. SynthVerdictScale — who actually failed ─────────────────────────────

export const synthVerdictScaleSchema = z.object({});

export const SynthVerdictScale: React.FC = () => {
  const frame = useCurrentFrame();
  const inn = useRise(5);
  const tipT = interpolate(frame, [40, 90], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const ease = tipT * tipT * (3 - 2 * tipT);
  const wobble = Math.sin(frame / 6) * 2.2 * Math.exp(-Math.max(0, frame - 90) / 30);
  const tilt = ease * 13 + (frame > 40 ? wobble : 0);
  const cx = 960, cy = 430, arm = 400;
  const lx = cx - arm * Math.cos(tilt * Math.PI / 180);
  const ly = cy - arm * Math.sin(tilt * Math.PI / 180) * -1;
  const rx = cx + arm * Math.cos(tilt * Math.PI / 180);
  const ry = cy + arm * Math.sin(tilt * Math.PI / 180) * -1;

  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="so which part actually failed?" />
      </div>

      <svg width="100%" height="100%" style={{ position: 'absolute', inset: 0, opacity: inn }}>
        <line x1={cx} y1={cy} x2={cx} y2={cy + 250} stroke={CLAUDE.INK_SOFT} strokeWidth={6} />
        <line x1={lx} y1={ly} x2={rx} y2={ry} stroke={CLAUDE.INK} strokeWidth={7} strokeLinecap="round" />
        <circle cx={cx} cy={cy} r={13} fill={CLAUDE.SPARK} />
        <line x1={lx} y1={ly} x2={lx} y2={ly + 70} stroke={CLAUDE.BORDER} strokeWidth={3} />
        <line x1={rx} y1={ry} x2={rx} y2={ry + 70} stroke={CLAUDE.BORDER} strokeWidth={3} />
      </svg>

      <div style={{
        position: 'absolute', left: lx - 210, top: ly + 70, width: 420, textAlign: 'center',
        opacity: inn,
      }}>
        <Card style={{ padding: '22px 20px' }}>
          <div style={{ fontFamily: U, fontSize: 30, fontWeight: 600, color: CLAUDE.INK }}>THE GENERATOR</div>
          <div style={{ fontFamily: U, fontSize: 22, color: CLAUDE.INK_SOFT, marginTop: 8 }}>
            reproduced the marginals it was given
          </div>
        </Card>
      </div>
      <div style={{
        position: 'absolute', left: rx - 210, top: ry + 70, width: 420, textAlign: 'center',
        opacity: inn,
      }}>
        <Card accent style={{ padding: '22px 20px', background: '#FBEEE8' }}>
          <div style={{ fontFamily: U, fontSize: 30, fontWeight: 600, color: CLAUDE.SEND }}>THE EVALUATION</div>
          <div style={{ fontFamily: U, fontSize: 22, color: CLAUDE.INK_SOFT, marginTop: 8 }}>
            moved the goalpost and skipped the control
          </div>
        </Card>
      </div>

      <SparkLine text="CTGAN did its job. The scoreboard did not." delay={96} />
    </Page>
  );
};
