import React from 'react';
import { useCurrentFrame, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { useRise, Eyebrow, SparkLine, Page, Card } from './IndexedOrInvisible';
import { Grader } from './EvalCartoon';
import { Robo } from './KidEval';

/**
 * KidAlign — the kid-friendly cut of "teaching a machine to be nice".
 *
 * Subject: a from-scratch alignment notebook (NumPy only) covering SFT, a reward
 * model, best-of-n, RLHF with and without a KL penalty, and DPO. It deliberately
 * runs the unleashed case to show reward hacking, which the notebook itself calls
 * "the single most important plot".
 *
 * Every figure is parsed from the notebook's recorded outputs at build time.
 * Claude palette only: cream, warm ink, one terracotta.
 */

const S = CLAUDE_FONT.serif;
const U = CLAUDE_FONT.ui;
const M = CLAUDE_FONT.mono;

const Stage: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <svg viewBox="0 0 1920 1080" width={1920} height={1080}
    style={{ position: 'absolute', left: 0, top: 0, pointerEvents: 'none' }}>
    {children}
  </svg>
);
const bob = (f: number, a = 5, s = 0.055) => Math.sin(f * s) * a;

// ── 1. KidReviewBot — the machine writes, the truth scores ─────────────────

export const kidReviewBotSchema = z.object({
  before: z.string().default('-0.061'),
  after: z.string().default('+0.568'),
  sample: z.string().default(''),
});
export type KidReviewBotProps = z.infer<typeof kidReviewBotSchema>;

export const KidReviewBot: React.FC<KidReviewBotProps> = ({ before, after, sample }) => {
  const frame = useCurrentFrame();
  const a = useRise(6);
  const b = useRise(40);
  const card = (t: number, label: string, score: string, hero: boolean) => (
    <div style={{ flex: 1, opacity: t, transform: `translateY(${(1 - t) * 18}px)` }}>
      <Card accent={hero} style={{ padding: '28px 32px', background: hero ? '#FBEEE8' : CLAUDE.CARD }}>
        <div style={{ fontFamily: U, fontSize: 24, letterSpacing: 2, color: hero ? CLAUDE.SEND : CLAUDE.INK_SOFT }}>
          {label}
        </div>
        <div style={{ fontFamily: M, fontSize: 76, color: CLAUDE.INK, marginTop: 10 }}>{score}</div>
        <div style={{ fontFamily: U, fontSize: 22, color: CLAUDE.INK_SOFT }}>niceness score</div>
      </Card>
    </div>
  );
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="show it what good looks like" />
      </div>
      <Robo x={320} y={430} scale={2.0} frame={frame} happy={b > 0.4} />
      <div style={{ position: 'absolute', left: 620, right: 130, top: 300, display: 'flex', gap: 36 }}>
        {card(a, 'BEFORE', before, false)}
        {card(b, 'AFTER 200 EXAMPLES', after, true)}
      </div>
      {sample && b > 0.3 ? (
        <div style={{ position: 'absolute', left: 620, right: 130, top: 600, opacity: b }}>
          <Card style={{ padding: '22px 26px' }}>
            <span style={{ fontFamily: M, fontSize: 25, color: CLAUDE.INK }}>{sample}</span>
          </Card>
        </div>
      ) : null}
      <SparkLine text="Nobody told it to be nice. We just showed it nice ones." delay={56} />
    </Page>
  );
};

// ── 2. KidNoisyLabels — people disagree ────────────────────────────────────

export const kidNoisyLabelsSchema = z.object({
  agreePct: z.string().default('77.3%'),
  agreeN: z.number().default(0.773),
});
export type KidNoisyLabelsProps = z.infer<typeof kidNoisyLabelsSchema>;

export const KidNoisyLabels: React.FC<KidNoisyLabelsProps> = ({ agreePct, agreeN }) => {
  const frame = useCurrentFrame();
  const N = 40;
  const lit = Math.min(N, Math.floor(interpolate(frame, [12, 90], [0, N],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' })));
  const nRight = Math.round(N * agreeN);
  const punch = useRise(100);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="but people are not perfect judges" />
      </div>
      <div style={{
        position: 'absolute', left: 130, top: 230, width: 1100,
        display: 'grid', gridTemplateColumns: 'repeat(10, 1fr)', gap: 16,
      }}>
        {Array.from({ length: N }, (_, i) => {
          const on = i < lit;
          const right = i < nRight;
          return (
            <div key={i} style={{
              aspectRatio: '1 / 1', borderRadius: 12,
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              background: !on ? CLAUDE.PILL : right ? '#FBEEE8' : CLAUDE.PILL,
              border: `2px solid ${!on ? CLAUDE.BORDER : right ? CLAUDE.SPARK : CLAUDE.GHOST}`,
              fontFamily: U, fontSize: 30,
              color: right ? CLAUDE.SEND : CLAUDE.GHOST,
            }}>{on ? (right ? '✓' : '✗') : ''}</div>
          );
        })}
      </div>
      {punch > 0.02 ? (
        <div style={{ position: 'absolute', left: 130, right: 130, top: 720, opacity: punch }}>
          <div style={{ fontFamily: S, fontSize: 52, color: CLAUDE.INK, lineHeight: 1.3 }}>
            Only {agreePct} of the time do they pick the genuinely better review.
          </div>
          <div style={{ fontFamily: U, fontSize: 28, color: CLAUDE.INK_SOFT, marginTop: 14 }}>
            Whatever we build next has to learn from opinions that are sometimes just wrong.
          </div>
        </div>
      ) : null}
      <SparkLine text="The lesson starts out slightly wrong. That matters later." delay={108} />
    </Page>
  );
};

// ── 3. KidJudgeBlindSpot — where the judge is fooled ───────────────────────

export const kidJudgeBlindSpotSchema = z.object({
  rows: z.array(z.object({
    text: z.string(), truth: z.string(), judge: z.string(), fooled: z.boolean(),
  })).default([]),
});
export type KidJudgeBlindSpotProps = z.infer<typeof kidJudgeBlindSpotSchema>;

export const KidJudgeBlindSpot: React.FC<KidJudgeBlindSpotProps> = ({ rows }) => {
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="the judge has blind spots" />
      </div>
      <div style={{ position: 'absolute', left: 120, right: 120, top: 180 }}>
        <div style={{ display: 'flex', gap: 24, marginBottom: 16 }}>
          <span style={{ flex: 1, fontFamily: U, fontSize: 21, letterSpacing: 2, color: CLAUDE.INK_SOFT }}>THE REVIEW</span>
          <span style={{ width: 170, textAlign: 'right', fontFamily: U, fontSize: 21, letterSpacing: 2, color: CLAUDE.INK_SOFT }}>REALLY IS</span>
          <span style={{ width: 200, textAlign: 'right', fontFamily: U, fontSize: 21, letterSpacing: 2, color: CLAUDE.SEND }}>JUDGE SAYS</span>
        </div>
        {rows.map((r, i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(8 + i * 13);
          return (
            <div key={i} style={{
              display: 'flex', gap: 24, alignItems: 'center', opacity: t,
              padding: '15px 18px', marginBottom: 10, borderRadius: 10,
              background: r.fooled ? '#FBEEE8' : 'transparent',
              border: `1px solid ${r.fooled ? CLAUDE.SPARK : CLAUDE.BORDER}`,
            }}>
              <span style={{ flex: 1, fontFamily: M, fontSize: 24, color: CLAUDE.INK }}>{r.text}</span>
              <span style={{ width: 170, textAlign: 'right', fontFamily: M, fontSize: 28, color: CLAUDE.INK_SOFT }}>{r.truth}</span>
              <span style={{
                width: 200, textAlign: 'right', fontFamily: M, fontSize: 28,
                color: r.fooled ? CLAUDE.SEND : CLAUDE.INK_SOFT,
                fontWeight: r.fooled ? 700 : 400,
              }}>{r.judge}</span>
            </div>
          );
        })}
      </div>
      <SparkLine text="It never learned what “not” means — and it adores repeated words." delay={84} />
    </Page>
  );
};

// ── 4. KidBestOfN — try lots, keep the best ────────────────────────────────

export const kidBestOfNSchema = z.object({
  rows: z.array(z.object({ n: z.string(), score: z.string(), bar: z.number() })).default([]),
});
export type KidBestOfNProps = z.infer<typeof kidBestOfNSchema>;

export const KidBestOfN: React.FC<KidBestOfNProps> = ({ rows }) => {
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="the lazy trick that works" />
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 240 }}>
        {rows.map((r, i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(10 + i * 16);
          const hero = i === rows.length - 1;
          return (
            <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 26, marginBottom: 32, opacity: t }}>
              <span style={{ fontFamily: U, fontSize: 28, color: CLAUDE.INK_SOFT, width: 230 }}>
                write {r.n}, keep the best
              </span>
              <div style={{ flex: 1, height: 48, background: CLAUDE.PILL, borderRadius: 10, overflow: 'hidden' }}>
                <div style={{
                  width: `${r.bar * 100 * t}%`, height: '100%',
                  background: hero ? CLAUDE.SPARK : CLAUDE.GHOST,
                }} />
              </div>
              <span style={{
                fontFamily: M, fontSize: 32, width: 140, textAlign: 'right',
                color: hero ? CLAUDE.SEND : CLAUDE.INK,
              }}>{r.score}</span>
            </div>
          );
        })}
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 700 }}>
        <div style={{ fontFamily: S, fontSize: 46, color: CLAUDE.INK, lineHeight: 1.3 }}>
          No training at all. Just more tries, and a judge to pick.
        </div>
      </div>
      <SparkLine text="Sometimes the cheapest idea is the one that works." delay={90} />
    </Page>
  );
};

// ── 5. KidCheating — the centrepiece: reward hacking ───────────────────────

export const kidCheatingSchema = z.object({
  pts: z.array(z.object({
    it: z.number(), judge: z.number(), truth: z.number(), gram: z.number(),
  })).default([]),
  hacked: z.string().default(''),
});
export type KidCheatingProps = z.infer<typeof kidCheatingSchema>;

export const KidCheating: React.FC<KidCheatingProps> = ({ pts, hacked }) => {
  const frame = useCurrentFrame();
  if (!pts.length) return <Page><div /></Page>;
  const prog = interpolate(frame, [14, 120], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const shown = Math.max(2, Math.ceil(pts.length * prog));
  const X0 = 240, X1 = 1180, Y0 = 220, Y1 = 580;
  const maxIt = pts[pts.length - 1].it || 1;
  const sx = (it: number) => X0 + (X1 - X0) * (it / maxIt);
  // map score range [-3.2, +2.0] onto the plot box
  const sy = (v: number) => Y1 - (Y1 - Y0) * ((v + 3.2) / 5.2);
  const path = (key: 'judge' | 'truth') =>
    pts.slice(0, shown).map((p, i) => `${i ? 'L' : 'M'} ${sx(p.it)} ${sy(p[key])}`).join(' ');
  const cur = pts[Math.min(pts.length - 1, shown - 1)];
  const reveal = useRise(126);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="now let it chase the judge's score, with no rules" />
      </div>
      <Stage>
        {/* zero line */}
        <line x1={X0} y1={sy(0)} x2={X1} y2={sy(0)} stroke={CLAUDE.BORDER} strokeWidth={2} strokeDasharray="6 7" />
        <path d={path('judge')} fill="none" stroke={CLAUDE.SPARK} strokeWidth={7} strokeLinecap="round" />
        <path d={path('truth')} fill="none" stroke={CLAUDE.INK} strokeWidth={7} strokeLinecap="round" opacity={0.65} />
        <circle cx={sx(cur.it)} cy={sy(cur.judge)} r={11} fill={CLAUDE.SPARK} />
        <circle cx={sx(cur.it)} cy={sy(cur.truth)} r={11} fill={CLAUDE.INK} opacity={0.65} />
      </Stage>
      <div style={{ position: 'absolute', left: X1 + 30, top: Y0 - 30, width: 440 }}>
        <div style={{ fontFamily: U, fontSize: 25, color: CLAUDE.SEND }}>what the judge scores it</div>
        <div style={{ fontFamily: M, fontSize: 60, color: CLAUDE.SEND }}>
          {cur.judge >= 0 ? '+' : ''}{cur.judge.toFixed(2)}
        </div>
        <div style={{ height: 22 }} />
        <div style={{ fontFamily: U, fontSize: 25, color: CLAUDE.INK_SOFT }}>what it is actually worth</div>
        <div style={{ fontFamily: M, fontSize: 60, color: CLAUDE.INK }}>
          {cur.truth >= 0 ? '+' : ''}{cur.truth.toFixed(2)}
        </div>
        <div style={{ height: 22 }} />
        <div style={{ fontFamily: U, fontSize: 25, color: CLAUDE.INK_SOFT }}>still proper sentences</div>
        <div style={{ fontFamily: M, fontSize: 60, color: cur.gram < 0.5 ? CLAUDE.SEND : CLAUDE.INK }}>
          {Math.round(cur.gram * 100)}%
        </div>
      </div>
      {reveal > 0.02 && hacked ? (
        <div style={{ position: 'absolute', left: 130, right: 130, top: 680, opacity: reveal }}>
          <div style={{ fontFamily: U, fontSize: 24, letterSpacing: 2, color: CLAUDE.SEND, marginBottom: 12 }}>
            WHAT IT WRITES NOW
          </div>
          <Card style={{ padding: '24px 28px', border: `2px solid ${CLAUDE.SPARK}`, background: '#FBEEE8' }}>
            <span style={{ fontFamily: M, fontSize: 26, color: CLAUDE.INK, lineHeight: 1.5 }}>{hacked}</span>
          </Card>
        </div>
      ) : null}
      <SparkLine text="The score went up. Everything the score was meant to measure fell apart." delay={134} />
    </Page>
  );
};

// ── 6. KidLeash — the KL penalty ───────────────────────────────────────────

export const kidLeashSchema = z.object({
  rows: z.array(z.object({
    beta: z.string(), score: z.string(), gram: z.string(), variety: z.string(), hero: z.boolean(),
  })).default([]),
});
export type KidLeashProps = z.infer<typeof kidLeashSchema>;

export const KidLeash: React.FC<KidLeashProps> = ({ rows }) => {
  const frame = useCurrentFrame();
  const a = useRise(6);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="the fix — put it on a lead" />
      </div>
      <Stage>
        <Grader x={260} y={330} scale={1.5} mood="neutral" />
        <path d={`M 300 330 Q 440 ${370 + Math.sin(frame * 0.07) * 16} 560 350`}
          fill="none" stroke={CLAUDE.SPARK} strokeWidth={5} strokeLinecap="round" opacity={a} />
      </Stage>
      <Robo x={640} y={330} scale={1.3} frame={frame} happy />
      <div style={{ position: 'absolute', left: 130, right: 130, top: 470 }}>
        <div style={{ display: 'flex', gap: 24, marginBottom: 14 }}>
          <span style={{ width: 220, fontFamily: U, fontSize: 21, letterSpacing: 2, color: CLAUDE.INK_SOFT }}>LEAD LENGTH</span>
          <span style={{ flex: 1, fontFamily: U, fontSize: 21, letterSpacing: 2, color: CLAUDE.INK_SOFT }}>HOW GOOD</span>
          <span style={{ width: 200, fontFamily: U, fontSize: 21, letterSpacing: 2, color: CLAUDE.INK_SOFT }}>STILL SENSIBLE</span>
          <span style={{ width: 170, fontFamily: U, fontSize: 21, letterSpacing: 2, color: CLAUDE.INK_SOFT }}>VARIETY</span>
        </div>
        {rows.map((r, i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(14 + i * 15);
          return (
            <div key={i} style={{
              display: 'flex', gap: 24, alignItems: 'center', opacity: t,
              padding: '18px', marginBottom: 10, borderRadius: 10,
              background: r.hero ? '#FBEEE8' : 'transparent',
              border: `1px solid ${r.hero ? CLAUDE.SPARK : CLAUDE.BORDER}`,
            }}>
              <span style={{ width: 220, fontFamily: M, fontSize: 28, color: CLAUDE.INK }}>{r.beta}</span>
              <span style={{ flex: 1, fontFamily: M, fontSize: 30, color: r.hero ? CLAUDE.SEND : CLAUDE.INK }}>{r.score}</span>
              <span style={{ width: 200, fontFamily: M, fontSize: 28, color: CLAUDE.INK_SOFT }}>{r.gram}</span>
              <span style={{ width: 170, fontFamily: M, fontSize: 28, color: CLAUDE.INK_SOFT }}>{r.variety}</span>
            </div>
          );
        })}
      </div>
      <SparkLine text="Short lead: safe but samey. Long lead: free to go wrong." delay={76} />
    </Page>
  );
};

// ── 7. KidScoreboard — everything, side by side ────────────────────────────

export const kidScoreboardSchema = z.object({
  rows: z.array(z.object({
    name: z.string(), score: z.string(), bar: z.number(), gram: z.string(),
    good: z.boolean(), bad: z.boolean(),
  })).default([]),
});
export type KidScoreboardProps = z.infer<typeof kidScoreboardSchema>;

export const KidScoreboard: React.FC<KidScoreboardProps> = ({ rows }) => {
  const MID = 0.52; // where zero sits across the bar track
  // scale by the largest magnitude present so a -3.00 cannot overflow its track
  const maxAbs = Math.max(1e-6, ...rows.map((r) => Math.abs(r.bar)));
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="everything we tried, side by side" />
      </div>
      <div style={{ position: 'absolute', left: 120, right: 120, top: 190 }}>
        {rows.map((r, i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(8 + i * 12);
          const w = (Math.abs(r.bar) / maxAbs) * 0.44;
          const col = r.bad ? CLAUDE.GHOST : r.good ? CLAUDE.SPARK : CLAUDE.INK_SOFT;
          return (
            <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 20, marginBottom: 16, opacity: t }}>
              <span style={{
                width: 310, fontFamily: U, fontSize: 25,
                color: r.good ? CLAUDE.INK : CLAUDE.INK_SOFT,
                fontWeight: r.good ? 600 : 400,
              }}>{r.name}</span>
              <div style={{ flex: 1, position: 'relative', height: 40 }}>
                <div style={{
                  position: 'absolute', left: `${MID * 100}%`, top: 0, bottom: 0,
                  width: 2, background: CLAUDE.BORDER,
                }} />
                <div style={{
                  position: 'absolute', top: 4, height: 32, borderRadius: 6, background: col,
                  left: r.bar >= 0 ? `${MID * 100}%` : `${(MID - w) * 100}%`,
                  width: `${w * 100 * t}%`,
                }} />
              </div>
              <span style={{ width: 130, textAlign: 'right', fontFamily: M, fontSize: 28, color: CLAUDE.INK }}>{r.score}</span>
              <span style={{ width: 120, textAlign: 'right', fontFamily: M, fontSize: 24, color: CLAUDE.INK_SOFT }}>{r.gram}</span>
            </div>
          );
        })}
      </div>
      <SparkLine text="The one that cheated scored worst of all — by the measure that counted." delay={100} />
    </Page>
  );
};
