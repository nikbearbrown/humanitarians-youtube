import React from 'react';
import { useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { useRise, Eyebrow, SparkLine, Page, Card } from './IndexedOrInvisible';

/**
 * CausalMapping — scene set for "The Variable That Vanished".
 *
 * Subject: a notebook on SES → health causality whose "causal-aware" model
 * adjusts for the mediators carrying the very effect it set out to measure.
 * Every number rendered here is recomputed at build time by re-running the
 * notebook's own data-generating process at seed 42.
 *
 * Duration-agnostic: springs settle early, loops are continuous, counters clamp.
 */

const S = CLAUDE_FONT.serif;
const U = CLAUDE_FONT.ui;
const M = CLAUDE_FONT.mono;

// ── shared bits ─────────────────────────────────────────────────────────────

const Node: React.FC<{
  x: number; y: number; label: string; t: number; accent?: boolean; dim?: boolean; w?: number;
}> = ({ x, y, label, t, accent, dim, w = 190 }) => (
  <div style={{
    position: 'absolute', left: x - w / 2, top: y - 27, width: w,
    opacity: t * (dim ? 0.32 : 1), transform: `scale(${0.85 + 0.15 * t})`,
    background: accent ? '#FBEEE8' : CLAUDE.CARD,
    border: `${accent ? 2 : 1}px solid ${accent ? CLAUDE.SPARK : CLAUDE.BORDER}`,
    borderRadius: 10, padding: '11px 6px', textAlign: 'center',
    fontFamily: U, fontSize: 21, fontWeight: 600,
    color: accent ? CLAUDE.SEND : CLAUDE.INK,
    boxShadow: '0 2px 10px rgba(61,57,41,0.05)',
  }}>{label}</div>
);

const Edge: React.FC<{
  x1: number; y1: number; x2: number; y2: number; t: number;
  dashed?: boolean; dim?: boolean; clamped?: boolean;
}> = ({ x1, y1, x2, y2, t, dashed, dim, clamped }) => {
  const len = Math.hypot(x2 - x1, y2 - y1);
  const ang = (Math.atan2(y2 - y1, x2 - x1) * 180) / Math.PI;
  return (
    <div style={{
      position: 'absolute', left: x1, top: y1,
      width: len * t, height: clamped ? 5 : 2,
      background: clamped ? CLAUDE.SPARK : CLAUDE.GHOST,
      opacity: dim ? 0.25 : 1,
      transformOrigin: '0 50%', transform: `rotate(${ang}deg)`,
      borderTop: dashed ? `2px dashed ${CLAUDE.GHOST}` : undefined,
      backgroundImage: dashed ? 'none' : undefined,
    }} />
  );
};

/** Particles travelling a straight segment, looping. */
const Flow: React.FC<{
  x1: number; y1: number; x2: number; y2: number;
  frame: number; count?: number; blocked?: number; speed?: number;
}> = ({ x1, y1, x2, y2, frame, count = 5, blocked = 0, speed = 0.011 }) => (
  <>
    {Array.from({ length: count }, (_, i) => {
      const phase = ((frame * speed) + i / count) % 1;
      const stop = blocked > 0 ? Math.min(phase, blocked) : phase;
      const px = x1 + (x2 - x1) * stop;
      const py = y1 + (y2 - y1) * stop;
      const fade = blocked > 0 && phase > blocked ? 0 : 1;
      return (
        <div key={i} style={{
          position: 'absolute', left: px - 5, top: py - 5,
          width: 10, height: 10, borderRadius: 5,
          background: CLAUDE.SPARK, opacity: 0.85 * fade,
        }} />
      );
    })}
  </>
);

// ── 1. CausalDagBuild — the DAG assembles itself ────────────────────────────

export const causalDagBuildSchema = z.object({});

export const CausalDagBuild: React.FC = () => {
  const n = [useRise(4), useRise(12), useRise(20), useRise(28), useRise(36), useRise(44)];
  const e = [useRise(16), useRise(24), useRise(32), useRise(40), useRise(48), useRise(54)];
  const EDU = { x: 300, y: 300 }, INC = { x: 700, y: 210 }, ENV = { x: 700, y: 400 };
  const LIFE = { x: 1120, y: 300 }, ACC = { x: 1120, y: 470 }, HLT = { x: 1560, y: 360 };
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="the notebook's own causal diagram" />
      </div>
      <div style={{ position: 'absolute', inset: 0, top: 90 }}>
        <Edge x1={EDU.x + 95} y1={EDU.y} x2={INC.x - 95} y2={INC.y} t={e[0]} />
        <Edge x1={EDU.x + 95} y1={EDU.y} x2={ENV.x - 95} y2={ENV.y} t={e[1]} />
        <Edge x1={INC.x + 95} y1={INC.y} x2={LIFE.x - 95} y2={LIFE.y} t={e[2]} />
        <Edge x1={ENV.x + 95} y1={ENV.y} x2={ACC.x - 95} y2={ACC.y} t={e[3]} />
        <Edge x1={LIFE.x + 95} y1={LIFE.y} x2={HLT.x - 95} y2={HLT.y} t={e[4]} />
        <Edge x1={ACC.x + 95} y1={ACC.y} x2={HLT.x - 95} y2={HLT.y} t={e[5]} />
        <Node x={EDU.x} y={EDU.y} label="Education" t={n[0]} accent />
        <Node x={INC.x} y={INC.y} label="Income" t={n[1]} />
        <Node x={ENV.x} y={ENV.y} label="Environment" t={n[2]} />
        <Node x={LIFE.x} y={LIFE.y} label="Lifestyle" t={n[3]} w={210} />
        <Node x={ACC.x} y={ACC.y} label="Access to care" t={n[4]} w={230} />
        <Node x={HLT.x} y={HLT.y} label="Health" t={n[5]} accent />
      </div>
      <SparkLine text="Education reaches health only by travelling through the middle." delay={62} />
    </Page>
  );
};

// ── 2. CausalPipeFlow — open vs clamped ─────────────────────────────────────

export const causalPipeFlowSchema = z.object({
  mode: z.enum(['open', 'clamped']).default('open'),
  caption: z.string().default(''),
  sparkLine: z.string().default(''),
});
export type CausalPipeFlowProps = z.infer<typeof causalPipeFlowSchema>;

export const CausalPipeFlow: React.FC<CausalPipeFlowProps> = ({ mode, caption, sparkLine }) => {
  const frame = useCurrentFrame();
  const t = useRise(4);
  const clampIn = useRise(26, 18);
  const clamped = mode === 'clamped';
  const LANES = [
    { y: 250, label: 'Diet' },
    { y: 360, label: 'Exercise' },
    { y: 470, label: 'Smoking' },
    { y: 580, label: 'Access' },
  ];
  const X1 = 470, X2 = 1450;
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text={clamped ? 'now adjust for all of them' : 'how the effect actually travels'} />
      </div>
      <div style={{ position: 'absolute', inset: 0, opacity: t }}>
        {/* source + sink */}
        <Node x={300} y={415} label="Education" t={t} accent w={215} />
        <Node x={1610} y={415} label="Health" t={t} accent w={190} />

        {LANES.map((ln, i) => (
          <React.Fragment key={ln.label}>
            {/* pipe */}
            <div style={{
              position: 'absolute', left: X1, top: ln.y - 15, width: X2 - X1, height: 30,
              background: CLAUDE.PILL, borderRadius: 15,
            }} />
            <div style={{
              position: 'absolute', left: X1 + 16, top: ln.y - 44,
              fontFamily: U, fontSize: 19, color: CLAUDE.INK_SOFT,
            }}>{ln.label}</div>
            {/* particles */}
            <Flow x1={X1 + 14} y1={ln.y} x2={X2 - 14} y2={ln.y} frame={frame}
              count={6} blocked={clamped ? 0.42 : 0} speed={0.009 + i * 0.001} />
            {/* the clamp */}
            {clamped ? (
              <div style={{
                position: 'absolute', left: X1 + (X2 - X1) * 0.42 - 13, top: ln.y - 33,
                width: 26, height: 66, borderRadius: 6,
                background: CLAUDE.SEND, opacity: clampIn,
                transform: `scaleY(${0.4 + 0.6 * clampIn})`,
              }} />
            ) : null}
          </React.Fragment>
        ))}
      </div>
      {caption ? (
        <div style={{
          position: 'absolute', left: 130, right: 130, top: 700,
          fontFamily: S, fontSize: 46, color: CLAUDE.INK, lineHeight: 1.28,
          opacity: clamped ? clampIn : t,
        }}>{caption}</div>
      ) : null}
      <SparkLine text={sparkLine} delay={44} />
    </Page>
  );
};

// ── 3. CausalVanish — 6.20 collapses to 0.047 ───────────────────────────────

export const causalVanishSchema = z.object({
  total: z.number().default(6.2),
  adjusted: z.number().default(0.047),
  pvalue: z.number().default(0.821),
});
export type CausalVanishProps = z.infer<typeof causalVanishSchema>;

export const CausalVanish: React.FC<CausalVanishProps> = ({ total, adjusted, pvalue }) => {
  const frame = useCurrentFrame();
  const grow = interpolate(frame, [10, 52], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const drop = interpolate(frame, [78, 116], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const shown = total * grow * (1 - drop) + adjusted * drop;
  const pIn = useRise(122);
  const MAXH = 380, SCALE = MAXH / total;
  const h = Math.max(3, shown * SCALE);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="the effect of education on health" />
      </div>
      <div style={{
        position: 'absolute', left: 0, right: 0, top: 150, height: MAXH + 60,
        display: 'flex', alignItems: 'flex-end', justifyContent: 'center', gap: 130,
      }}>
        {/* the bar */}
        <div style={{ textAlign: 'center' }}>
          <div style={{
            fontFamily: M, fontSize: 66, color: drop > 0.5 ? CLAUDE.GHOST : CLAUDE.INK,
            marginBottom: 16,
          }}>{shown < 1 ? shown.toFixed(3) : shown.toFixed(2)}</div>
          <div style={{
            width: 210, height: h, background: drop > 0.5 ? CLAUDE.PILL : CLAUDE.SPARK,
            borderRadius: '10px 10px 0 0', margin: '0 auto',
            border: drop > 0.5 ? `2px dashed ${CLAUDE.GHOST}` : 'none',
          }} />
          <div style={{
            fontFamily: U, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 16,
          }}>{drop > 0.5 ? 'after adjusting for the mediators' : 'true total effect, per level'}</div>
        </div>
      </div>
      {pIn > 0.02 ? (
        <div style={{
          position: 'absolute', left: 130, right: 130, top: 720, opacity: pIn,
        }}>
          <Card style={{ padding: '24px 30px', background: '#FBEEE8', border: `1px solid ${CLAUDE.SPARK}` }}>
            <span style={{ fontFamily: M, fontSize: 30, color: CLAUDE.SEND }}>p = {pvalue.toFixed(3)}</span>
            <span style={{ fontFamily: U, fontSize: 28, color: CLAUDE.INK, marginLeft: 22 }}>
              — indistinguishable from zero
            </span>
          </Card>
        </div>
      ) : null}
      <SparkLine text="Six points of real effect, adjusted into nothing." delay={130} />
    </Page>
  );
};

// ── 4. CausalDeadEdge — signal drowned by noise ─────────────────────────────

export const causalDeadEdgeSchema = z.object({
  signal: z.number().default(0.000506),
  noise: z.number().default(0.05),
  ratio: z.number().default(99),
  corr: z.number().default(0.0821),
});
export type CausalDeadEdgeProps = z.infer<typeof causalDeadEdgeSchema>;

export const CausalDeadEdge: React.FC<CausalDeadEdgeProps> = ({ signal, noise, ratio, corr }) => {
  const frame = useCurrentFrame();
  const a = useRise(5);
  const b = useRise(30);
  const W = 1180;
  const noiseW = W;
  const sigW = Math.max(3, W * (signal / noise));
  const jitter = Math.sin(frame * 0.5) * 3;
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="the edge that exists only in prose" />
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 190 }}>
        <Card style={{ padding: '22px 26px', fontFamily: M, fontSize: 25, color: CLAUDE.INK_SOFT, opacity: a }}>
          access = 0.2 + <span style={{ color: CLAUDE.SEND }}>0.00000001 * income</span>
          {'  '}+ 0.003*(env-50) + N(0, 0.05)
        </Card>

        <div style={{ marginTop: 54, opacity: b }}>
          <div style={{ fontFamily: U, fontSize: 22, color: CLAUDE.INK_SOFT, marginBottom: 10 }}>
            noise contribution
          </div>
          <div style={{
            width: noiseW, height: 58, background: CLAUDE.PILL, borderRadius: 8,
            transform: `translateX(${jitter}px)`,
          }} />
          <div style={{ fontFamily: M, fontSize: 24, color: CLAUDE.INK, marginTop: 8 }}>
            {noise.toFixed(4)}
          </div>

          <div style={{ fontFamily: U, fontSize: 22, color: CLAUDE.INK_SOFT, margin: '34px 0 10px' }}>
            income contribution
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 20 }}>
            <div style={{ width: sigW, height: 58, background: CLAUDE.SPARK, borderRadius: 4 }} />
            <span style={{ fontFamily: M, fontSize: 24, color: CLAUDE.SEND }}>{signal.toFixed(6)}</span>
          </div>
        </div>

        <div style={{ marginTop: 46, opacity: b }}>
          <span style={{ fontFamily: S, fontSize: 48, color: CLAUDE.INK }}>
            {Math.round(ratio)}× smaller than the noise it sits in.
          </span>
          <span style={{ fontFamily: U, fontSize: 26, color: CLAUDE.INK_SOFT, marginLeft: 22 }}>
            r = {corr.toFixed(4)}
          </span>
        </div>
      </div>
      <SparkLine text="The arrow is in the diagram. It is not in the data." delay={58} />
    </Page>
  );
};

// ── 5. CausalEstimands — two questions, two right answers ───────────────────

export const causalEstimandsSchema = z.object({
  total: z.number().default(6.2),
  direct: z.number().default(0.0),
});
export type CausalEstimandsProps = z.infer<typeof causalEstimandsSchema>;

export const CausalEstimands: React.FC<CausalEstimandsProps> = ({ total, direct }) => {
  const a = useRise(6);
  const b = useRise(24);
  const card = (t: number, q: string, val: string, sub: string, accent: boolean) => (
    <div style={{ flex: 1, opacity: t, transform: `translateY(${(1 - t) * 18}px)` }}>
      <Card accent={accent} style={{
        padding: '32px 34px', height: '100%',
        background: accent ? '#FBEEE8' : CLAUDE.CARD,
      }}>
        <div style={{ fontFamily: U, fontSize: 25, color: CLAUDE.INK_SOFT, lineHeight: 1.45, minHeight: 116 }}>
          {q}
        </div>
        <div style={{ fontFamily: M, fontSize: 68, color: accent ? CLAUDE.SEND : CLAUDE.INK, marginTop: 18 }}>
          {val}
        </div>
        <div style={{ fontFamily: U, fontSize: 22, color: CLAUDE.INK_SOFT, marginTop: 10 }}>{sub}</div>
      </Card>
    </div>
  );
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="two different questions" />
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 200, display: 'flex', gap: 40 }}>
        {card(a, '“If someone gets more education, how much healthier do they end up — by any route?”',
          total.toFixed(2), 'total effect — the policy question', true)}
        {card(b, '“Holding diet, exercise, smoking and access fixed, what does education add on its own?”',
          direct.toFixed(2), 'direct effect — what the model reported', false)}
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 700 }}>
        <div style={{ fontFamily: S, fontSize: 46, color: CLAUDE.INK, lineHeight: 1.3 }}>
          Both numbers are correct. Only one answers the title.
        </div>
      </div>
      <SparkLine text="Adjustment did not remove bias here. It changed the question." delay={48} />
    </Page>
  );
};

// ── 6. CausalScoreboard — income, where the method works ────────────────────

export const causalScoreboardSchema = z.object({
  naive: z.number().default(0.000353),
  adjusted: z.number().default(0.000143),
  truth: z.number().default(0.00015),
});
export type CausalScoreboardProps = z.infer<typeof causalScoreboardSchema>;

export const CausalScoreboard: React.FC<CausalScoreboardProps> = ({ naive, adjusted, truth }) => {
  const rows: [string, number, boolean][] = [
    ['naive model — income alone', naive, false],
    ['causal-aware model', adjusted, true],
    ['ground truth in the generator', truth, true],
  ];
  const MAX = Math.max(naive, adjusted, truth);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="credit where it is due — income" />
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 220 }}>
        {rows.map(([label, v, good], i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(8 + i * 18);
          return (
            <div key={label} style={{ marginBottom: 40, opacity: t }}>
              <div style={{ fontFamily: U, fontSize: 25, color: CLAUDE.INK_SOFT, marginBottom: 12 }}>{label}</div>
              <div style={{ display: 'flex', alignItems: 'center', gap: 24 }}>
                <div style={{
                  width: 1020 * (v / MAX) * t, height: 52, borderRadius: 8,
                  background: good ? CLAUDE.SPARK : CLAUDE.PILL,
                  border: good ? 'none' : `1px solid ${CLAUDE.BORDER}`,
                }} />
                <span style={{ fontFamily: M, fontSize: 30, color: CLAUDE.INK }}>{v.toFixed(6)}</span>
              </div>
            </div>
          );
        })}
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 690 }}>
        <div style={{ fontFamily: S, fontSize: 44, color: CLAUDE.INK, lineHeight: 1.3 }}>
          For income, the adjustment worked — almost exactly.
        </div>
      </div>
      <SparkLine text="The method is sound. It was pointed at the wrong variable." delay={70} />
    </Page>
  );
};

// ── 7. CausalCellOrder — the notebook cannot run top to bottom ──────────────

export const causalCellOrderSchema = z.object({});

export const CausalCellOrder: React.FC = () => {
  const frame = useCurrentFrame();
  const a = useRise(6);
  const boom = useRise(46, 15);
  const CELLS: [number, string, boolean][] = [
    [24, 'corr = df_clean[corr_vars].corr()', true],
    [27, 'df_clean = df_missing.copy()', false],
  ];
  const shake = boom > 0.05 ? Math.sin(frame * 1.5) * 5 * Math.max(0, 1 - (frame - 46) / 28) : 0;
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="run it top to bottom" />
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 230, opacity: a }}>
        {CELLS.map(([num, code, uses]) => (
          <div key={num} style={{
            marginBottom: 32,
            transform: uses ? `translateX(${shake}px)` : 'none',
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 20 }}>
              <span style={{ fontFamily: M, fontSize: 24, color: CLAUDE.GHOST, width: 110 }}>
                In [{num}]
              </span>
              <Card style={{
                flex: 1, padding: '22px 26px',
                border: `1px solid ${uses && boom > 0.3 ? CLAUDE.SPARK : CLAUDE.BORDER}`,
                background: uses && boom > 0.3 ? '#FBEEE8' : CLAUDE.CARD,
              }}>
                <span style={{ fontFamily: M, fontSize: 25, color: CLAUDE.INK }}>{code}</span>
              </Card>
              <span style={{
                fontFamily: U, fontSize: 21, letterSpacing: 1.6, width: 120,
                color: uses ? CLAUDE.SEND : CLAUDE.INK_SOFT,
              }}>{uses ? 'USES' : 'DEFINES'}</span>
            </div>
          </div>
        ))}
        {boom > 0.05 ? (
          <div style={{ marginTop: 24, opacity: boom }}>
            <Card style={{ padding: '26px 30px', border: `2px solid ${CLAUDE.SPARK}`, background: '#FBEEE8' }}>
              <div style={{ fontFamily: M, fontSize: 28, color: CLAUDE.SEND }}>
                NameError: name 'df_clean' is not defined
              </div>
              <div style={{ fontFamily: U, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 12 }}>
                cell 24 reads it · cell 27 creates it
              </div>
            </Card>
          </div>
        ) : null}
      </div>
      <SparkLine text="It only ever ran because the cells were executed out of order." delay={74} />
    </Page>
  );
};

// ── 8. CausalQuote — the notebook's own words, checked ──────────────────────

export const causalQuoteSchema = z.object({
  quote: z.string().default(''),
  source: z.string().default(''),
  verdict: z.string().default(''),
});
export type CausalQuoteProps = z.infer<typeof causalQuoteSchema>;

export const CausalQuote: React.FC<CausalQuoteProps> = ({ quote, source, verdict }) => {
  const q = useRise(5);
  const v = useRise(34);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="what the notebook says" />
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 210 }}>
        <div style={{ opacity: q, transform: `translateY(${(1 - q) * 14}px)` }}>
          <div style={{
            borderLeft: `4px solid ${CLAUDE.SPARK}`, paddingLeft: 34,
            fontFamily: S, fontStyle: 'italic', fontSize: 50, lineHeight: 1.35, color: CLAUDE.INK,
          }}>{quote}</div>
          <div style={{ fontFamily: U, fontSize: 22, color: CLAUDE.GHOST, marginTop: 18, paddingLeft: 38 }}>
            {source}
          </div>
        </div>
        {v > 0.02 ? (
          <div style={{ marginTop: 56, opacity: v, transform: `translateY(${(1 - v) * 14}px)` }}>
            <Card style={{ padding: '30px 34px', background: '#FBEEE8', border: `1px solid ${CLAUDE.SPARK}` }}>
              <div style={{ fontFamily: U, fontSize: 21, letterSpacing: 2.4, color: CLAUDE.SEND, textTransform: 'uppercase' }}>
                measured
              </div>
              <div style={{ fontFamily: S, fontSize: 46, color: CLAUDE.INK, marginTop: 14, lineHeight: 1.3 }}>
                {verdict}
              </div>
            </Card>
          </div>
        ) : null}
      </div>
      <SparkLine text="" delay={200} />
    </Page>
  );
};
