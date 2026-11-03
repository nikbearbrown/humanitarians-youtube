/**
 * MoeExplainer.tsx — reel-local, DUAL-ASPECT Remotion components for
 * claude-hai-mixture-of-experts ("Mixture of Experts", @HumanitariansAI).
 *
 * Same contract as JevExplainer.tsx (whose stage helpers it reuses): each component
 * lays out natively for 16:9 (<Name>) and 9:16 (<Name>916) — never a crop — and
 * every motion is a pure function of progress, conformed via `durationSeconds`.
 * Parameter counts are the published figures (Mixtral 8x7B: 47B total / 13B active,
 * 2 of 8 experts per token; DeepSeek-V3: 671B total / 37B active) — see SOURCES.md.
 * Router scores and token words are illustrative and labelled so on screen.
 *
 *   MoeHook     — 671B parameters counts up; "work per token" is an open question
 *   MoeDense    — every token fires every unit; double the size, double the cost
 *   MoeExperts  — one big feed-forward block splits into 8 experts
 *   MoeRouter   — a token is scored against 8 experts; the top 2 are picked
 *   MoeSparse   — token after token, only its 2 experts run; the rest sit idle
 *   MoeScale    — total vs. active parameters, bars per model (published figures)
 *   MoeMemory   — all experts loaded in memory; only 2 compute
 */
import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from './tokens/claude';
import { SERIF, SANS, MONO, ACC_TEXT, ramp, ease, useStage, durMeta, Bug, Title, Spark, Card } from './JevExplainer';

const Note: React.FC<{ x: number; y: number; w: number; a: number; text: string; align?: 'left' | 'right' }> = ({ x, y, w, a, text, align = 'left' }) => (
  <div style={{ position: 'absolute', left: x, top: y, width: w, textAlign: align, fontFamily: SANS, fontSize: 42, color: CLAUDE.INK_SOFT, opacity: a }}>{text}</div>
);

// a drawn arrow (bar + head): the arrow glyph renders as a sub-floor blob at 4K (GATE T §8.1)
const Arrow: React.FC<{ w?: number; color?: string; a?: number }> = ({ w = 70, color = CLAUDE.INK_SOFT, a = 1 }) => (
  <span style={{ display: 'inline-flex', alignItems: 'center', verticalAlign: 'middle', opacity: a, margin: '0 16px' }}>
    <span style={{ width: w - 30, height: 8, background: color }} />
    <span style={{ width: 0, height: 0, borderTop: '20px solid transparent', borderBottom: '20px solid transparent', borderLeft: `30px solid ${color}` }} />
  </span>
);

// grid position of expert i: one row of n (landscape) or rows of `perRow` (portrait)
const gridPos = (i: number, perRow: number, x: number, y: number, w: number, h: number, gap: number) => ({
  left: x + (i % perRow) * (w + gap), top: y + Math.floor(i / perRow) * (h + gap),
});

// ===========================================================================
// MoeHook — a huge parameter count, and an open question: how much runs per token?
// ===========================================================================
export const moeHookSchema = z.object({
  title: z.string().default('Huge, and still fast?'),
  total: z.number().default(671),
  unit: z.string().default('parameters in one model'),
  source: z.string().default('DeepSeek-V3 (2024)'),
  askLabel: z.string().default('work per token'),
  sparkLine: z.string().default('How is it affordable?'),
  durationSeconds: z.number().optional(),
});
export const moeHookMeta = durMeta(5);
export const MoeHook: React.FC<z.infer<typeof moeHookSchema>> = ({ title, total, unit, source, askLabel, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 360 : 230;
  const count = Math.round(ease(ramp(t, 0.06, 0.4)) * total);
  const bar = ease(ramp(t, 0.06, 0.4));
  const ask = ease(ramp(t, 0.48, 0.58));
  const pulse = 0.7 + 0.3 * Math.sin(t * 30);
  const barTop = top + (P ? 380 : 330);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top, fontFamily: SERIF, fontSize: P ? 250 : 250, color: CLAUDE.INK, lineHeight: 1 }}>
        {count}B
      </div>
      <div style={{ position: 'absolute', left: S.x, top: top + (P ? 265 : 260), fontFamily: SANS, fontSize: P ? 48 : 52, color: CLAUDE.INK_SOFT }}>{unit}</div>
      <div style={{ position: 'absolute', left: S.x, top: barTop, width: S.w * bar, height: P ? 80 : 70, background: CLAUDE.INK, borderRadius: 10 }} />
      <div style={{
        position: 'absolute', left: S.x, top: barTop + (P ? 130 : 110), display: 'flex', alignItems: 'center', gap: 30, opacity: ask,
        flexWrap: 'wrap', width: S.w,
      }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 64 : 68, color: CLAUDE.INK }}>{askLabel}:</span>
        <span style={{
          display: 'inline-flex', alignItems: 'center', justifyContent: 'center', width: P ? 220 : 240, height: P ? 120 : 110,
          border: `5px dashed ${CLAUDE.SPARK}`, borderRadius: 16, fontFamily: SERIF, fontSize: 90, color: CLAUDE.INK, opacity: pulse,
        }}>?</span>
      </div>
      <Note x={S.x} y={barTop + (P ? 330 : 250)} w={S.w} a={ask} text={source} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// MoeDense — every token fires every unit; double the model, double the cost
// ===========================================================================
export const moeDenseSchema = z.object({
  title: z.string().default('Dense models run it all'),
  tokens: z.array(z.string()).default(['the', 'cat', 'sat', 'on', 'the', 'mat']),
  sparkLine: z.string().default('Size equals cost.'),
  durationSeconds: z.number().optional(),
});
export const moeDenseMeta = durMeta(5);
export const MoeDense: React.FC<z.infer<typeof moeDenseSchema>> = ({ title, tokens, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 320 : 210;
  const grow = ease(ramp(t, 0.5, 0.62));            // the model doubles
  const rows = 5;
  const cols = 6 + Math.round(6 * grow);
  const cardW = P ? S.w : 940;
  const cardH = P ? 500 : 720;
  const n = tokens.length;
  const idx = Math.min(n - 1, Math.floor(ramp(t, 0.06, 0.94) * n));
  const phase = (ramp(t, 0.06, 0.94) * n) % 1;       // each token: a flash then decay
  const lit = idx >= 0 ? Math.max(0, 1 - phase * 1.6) : 0;
  const pad = 60;
  const gx = (cardW - pad * 2) / 12;
  const gy = (cardH - 170) / rows;
  const r = Math.min(gx, gy) * 0.3;
  const barX = P ? S.x : S.x + cardW + 70;
  const barW = P ? S.w : S.r - barX;
  const barTop = P ? top + cardH + 60 : top + 90;
  const size = 0.45 + 0.45 * grow;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: S.x, top, width: cardW, height: cardH }}>
        <div style={{ position: 'absolute', left: pad, top: 30, fontFamily: MONO, fontSize: P ? 42 : 44, color: CLAUDE.INK }}>
          token<Arrow w={60} color={CLAUDE.INK} /><span style={{ color: CLAUDE.INK, fontWeight: 700 }}>"{tokens[idx]}"</span>
        </div>
        <svg width={cardW} height={cardH} style={{ position: 'absolute', left: 0, top: 0 }}>
          {Array.from({ length: rows * 12 }).map((_, k) => {
            const c = k % 12, rr = Math.floor(k / 12);
            if (c >= cols) return null;
            const on = lit > 0.05;
            return (
              <circle key={k} cx={pad + gx * (c + 0.5)} cy={130 + gy * (rr + 0.5)} r={r}
                fill={on ? CLAUDE.INK : CLAUDE.CARD} fillOpacity={on ? 0.4 + 0.6 * lit : 1}
                stroke={CLAUDE.INK_SOFT} strokeWidth={3} />
            );
          })}
        </svg>
      </Card>
      <div style={{ position: 'absolute', left: barX, top: barTop, width: barW }}>
        <div style={{ fontFamily: SANS, fontSize: P ? 44 : 50, color: CLAUDE.INK_SOFT }}>model size</div>
        <div style={{ marginTop: 14, height: P ? 64 : 100, width: barW * size, background: CLAUDE.INK, borderRadius: 10 }} />
        <div style={{ marginTop: P ? 36 : 80, fontFamily: SANS, fontSize: P ? 44 : 50, color: CLAUDE.INK_SOFT }}>cost per token</div>
        <div style={{ marginTop: 14, height: P ? 64 : 100, width: barW * size, background: ACC_TEXT, borderRadius: 10 }} />
        <div style={{ marginTop: P ? 30 : 80, fontFamily: SERIF, fontSize: P ? 64 : 84, color: CLAUDE.INK }}>
          {grow > 0.5 ? <>2× size<Arrow color={CLAUDE.INK} />2× cost</> : 'every unit fires'}
        </div>
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// MoeExperts — one big feed-forward block splits into many smaller experts
// ===========================================================================
export const moeExpertsSchema = z.object({
  title: z.string().default('Split into experts'),
  n: z.number().int().default(8),
  blockLabel: z.string().default('one big feed-forward block'),
  caption: z.string().default('8 experts in every layer (Mixtral)'),
  sparkLine: z.string().default('Many small specialists.'),
  durationSeconds: z.number().optional(),
});
export const moeExpertsMeta = durMeta(5);
export const MoeExperts: React.FC<z.infer<typeof moeExpertsSchema>> = ({ title, n, blockLabel, caption, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 420 : 330;
  const split = ease(ramp(t, 0.28, 0.55));
  const perRow = P ? 4 : n;
  const rowsN = Math.ceil(n / perRow);
  const gap = (P ? 28 : 24) * split;
  const w = (S.w - gap * (perRow - 1)) / perRow;
  const h = P ? 340 : 440;
  const areaH = rowsN * h + (rowsN - 1) * gap;
  const layerIn = ease(ramp(t, 0.02, 0.14));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top: top - 80, fontFamily: SANS, fontSize: 40, color: CLAUDE.INK_SOFT, opacity: layerIn }}>
        inside one layer of the model
      </div>
      {Array.from({ length: n }).map((_, i) => (
        <Card key={i} style={{
          ...gridPos(i, perRow, S.x, top, w, h, gap), width: w, height: h, opacity: layerIn,
          display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 10,
        }}>
          <span style={{ fontFamily: SERIF, fontSize: P ? 80 : 84, color: CLAUDE.INK, opacity: split }}>E{i + 1}</span>
          <span style={{ fontFamily: SANS, fontSize: 42, color: CLAUDE.INK_SOFT, opacity: split }}>expert</span>
        </Card>
      ))}
      {/* the undivided block sits over the grid, then dissolves as it splits */}
      <Card style={{
        left: S.x, top, width: S.w, height: areaH, opacity: layerIn * Math.max(0, 1 - split * 2.5),
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        fontFamily: SERIF, fontSize: P ? 70 : 76, color: CLAUDE.INK, textAlign: 'center',
      }}>{blockLabel}</Card>
      <div style={{
        position: 'absolute', left: S.x, top: top + areaH + (P ? 50 : 50), width: S.w,
        fontFamily: SERIF, fontSize: P ? 60 : 64, color: CLAUDE.INK, opacity: ease(ramp(t, 0.58, 0.7)),
      }}>{caption}</div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// MoeRouter — one token, scored against every expert; the top k are picked
// ===========================================================================
export const moeRouterSchema = z.object({
  title: z.string().default('The router picks'),
  token: z.string().default('"cat"'),
  scores: z.array(z.number()).default([0.05, 0.31, 0.04, 0.08, 0.02, 0.36, 0.06, 0.08]),
  k: z.number().int().default(2),
  note: z.string().default('illustrative scores'),
  sparkLine: z.string().default('Two of eight.'),
  durationSeconds: z.number().optional(),
});
export const moeRouterMeta = durMeta(5);
export const MoeRouter: React.FC<z.infer<typeof moeRouterSchema>> = ({ title, token, scores, k, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const n = scores.length;
  const topK = scores.map((s, i) => [s, i] as const).sort((a, b) => b[0] - a[0]).slice(0, k).map(([, i]) => i);
  const max = Math.max(...scores);
  const tokIn = ease(ramp(t, 0.04, 0.14));
  const rtIn = ease(ramp(t, 0.12, 0.24));
  const bars = ease(ramp(t, 0.28, 0.55));
  const pick = ease(ramp(t, 0.6, 0.7));
  // landscape: token → router on the left, expert rows on the right; portrait: token → router on top
  const headTop = P ? 330 : 470;
  const tokW = P ? 300 : 280, rtW = P ? 360 : 300, headH = P ? 150 : 150;
  const rtX = S.x + tokW + (P ? 90 : 100);
  const listX = P ? S.x : rtX + rtW + 110;
  const listW = P ? S.w : S.r - listX;
  const listTop = P ? headTop + headH + 70 : 230;
  const rowH = P ? 76 : 70, rowGap = P ? 14 : 16;
  const labelW = 110;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{
        left: S.x, top: headTop, width: tokW, height: headH, opacity: tokIn,
        display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: MONO, fontSize: 54, color: CLAUDE.INK,
      }}>{token}</Card>
      <div style={{ position: 'absolute', left: S.x + tokW + 14, top: headTop + headH / 2 - 40, fontFamily: SANS, fontSize: 60, color: CLAUDE.INK_SOFT }}><Arrow w={64} a={rtIn} /></div>
      <Card style={{
        left: rtX, top: headTop, width: rtW, height: headH, opacity: rtIn, background: CLAUDE.INK, border: `3px solid ${CLAUDE.INK}`,
        display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SERIF, fontSize: 60, color: CLAUDE.CARD,
      }}>router</Card>
      {!P && <div style={{ position: 'absolute', left: rtX + rtW + 24, top: headTop + headH / 2 - 40, fontFamily: SANS, fontSize: 60, color: CLAUDE.INK_SOFT }}><Arrow w={64} a={rtIn} /></div>}
      {scores.map((s, i) => {
        const chosen = topK.includes(i) && pick > 0.5;
        const dim = topK.includes(i) ? 1 : 1 - pick * 0.45;
        const y = listTop + i * (rowH + rowGap);
        const trackW = listW - labelW - 240;   // room for the '✓ picked' label
        return (
          <div key={i} style={{ position: 'absolute', left: listX, top: y, width: listW, height: rowH, opacity: dim * ease(ramp(t, 0.16 + i * 0.015, 0.26 + i * 0.015)) }}>
            <span style={{ position: 'absolute', left: 0, top: rowH / 2 - 28, fontFamily: MONO, fontSize: 46, fontWeight: chosen ? 700 : 400, color: CLAUDE.INK }}>E{i + 1}</span>
            <div style={{
              position: 'absolute', left: labelW, top: 8, height: rowH - 16, borderRadius: 8,
              width: Math.max(8, trackW * (s / max) * bars), background: chosen ? CLAUDE.SPARK : CLAUDE.INK_SOFT,
            }} />
            <span style={{
              position: 'absolute', left: labelW + trackW * (s / max) * bars + 20, top: rowH / 2 - 24,
              fontFamily: SANS, fontSize: 42, fontWeight: chosen ? 700 : 400, color: chosen ? CLAUDE.INK : CLAUDE.INK_SOFT, opacity: bars, whiteSpace: 'nowrap',
            }}>{chosen ? '✓ picked' : s.toFixed(2)}</span>
          </div>
        );
      })}
      <Note x={P ? S.x + tokW + 90 : S.x} y={P ? headTop + headH + 10 : headTop + headH + 40} w={P ? rtW : tokW + rtW + 100}
        a={bars} text={note} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// MoeSparse — token after token, only its chosen experts run; the rest sit idle
// ===========================================================================
export const moeSparseSchema = z.object({
  title: z.string().default('Only the chosen run'),
  n: z.number().int().default(8),
  steps: z.array(z.object({ token: z.string(), experts: z.array(z.number()) })).default([
    { token: '"the"', experts: [0, 3] },
    { token: '"cat"', experts: [1, 5] },
    { token: '"sat"', experts: [5, 6] },
  ]),
  sparkLine: z.string().default('The rest sit idle.'),
  durationSeconds: z.number().optional(),
});
export const moeSparseMeta = durMeta(5);
export const MoeSparse: React.FC<z.infer<typeof moeSparseSchema>> = ({ title, n, steps, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 340 : 250;
  const m = steps.length;
  const p = ramp(t, 0.06, 0.92) * m;
  const si = Math.min(m - 1, Math.floor(p));
  const local = p - si;
  const on = ease(ramp(local, 0.05, 0.3));
  const step = steps[si];
  const perRow = P ? 4 : n;
  const gap = P ? 26 : 22;
  const w = (S.w - gap * (perRow - 1)) / perRow;
  const h = P ? 300 : 340;
  const gridTop = top + (P ? 170 : 170);
  const rowsN = Math.ceil(n / perRow);
  const below = gridTop + rowsN * h + (rowsN - 1) * gap + 50;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top, fontFamily: MONO, fontSize: P ? 56 : 58, color: CLAUDE.INK, opacity: ease(ramp(t, 0.02, 0.1)) }}>
        token {si + 1}<Arrow w={70} color={CLAUDE.INK} />{step.token}
      </div>
      {Array.from({ length: n }).map((_, i) => {
        const run = step.experts.includes(i);
        return (
          <Card key={i} accent={run && on > 0.5} style={{
            ...gridPos(i, perRow, S.x, gridTop, w, h, gap), width: w, height: h,
            background: CLAUDE.CARD, borderWidth: run && on > 0.5 ? 8 : 3,
            opacity: run ? 1 : 0.75,   // idle stays readable (GATE V contrast)
            display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 8,
          }}>
            <span style={{ fontFamily: SERIF, fontSize: P ? 72 : 66, color: CLAUDE.INK }}>E{i + 1}</span>
            <span style={{ fontFamily: SANS, fontSize: 44, fontWeight: run && on > 0.5 ? 700 : 400, color: run && on > 0.5 ? CLAUDE.INK : CLAUDE.INK_SOFT }}>{run && on > 0.5 ? 'running' : 'idle'}</span>
          </Card>
        );
      })}
      <div style={{ position: 'absolute', left: S.x, top: below, width: S.w, fontFamily: SERIF, fontSize: P ? 68 : 72, color: CLAUDE.INK }}>
        {step.experts.length} of {n} experts run
      </div>
      <Note x={S.x} y={below + (P ? 100 : 92)} w={S.w} a={ease(ramp(t, 0.1, 0.2))} text="illustrative routing" />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// MoeScale — published totals vs. parameters actually used per token
// ===========================================================================
export const moeScaleSchema = z.object({
  title: z.string().default('Stored vs. used per token'),
  models: z.array(z.object({ name: z.string(), total: z.number(), active: z.number() })).default([
    { name: 'Mixtral 8x7B', total: 47, active: 13 },
    { name: 'DeepSeek-V3', total: 671, active: 37 },
  ]),
  note: z.string().default('each bar scaled to its own model · Mistral AI 2024, DeepSeek-AI 2024'),
  sparkLine: z.string().default('Capacity, not cost.'),
  durationSeconds: z.number().optional(),
});
export const moeScaleMeta = durMeta(5);
export const MoeScale: React.FC<z.infer<typeof moeScaleSchema>> = ({ title, models, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 460 : 260;   // portrait title wraps to two lines
  const rowStep = P ? 380 : 330;
  const barH = P ? 110 : 120;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {models.map((m, i) => {
        const y = top + i * rowStep;
        const tot = ease(ramp(t, 0.06 + i * 0.12, 0.3 + i * 0.12));
        const act = ease(ramp(t, 0.45 + i * 0.08, 0.6 + i * 0.08));
        const frac = m.active / m.total;
        return (
          <div key={m.name} style={{ position: 'absolute', left: S.x, top: y, width: S.w, opacity: ease(ramp(t, 0.04 + i * 0.12, 0.12 + i * 0.12)) }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline' }}>
              <span style={{ fontFamily: SERIF, fontSize: P ? 60 : 62, color: CLAUDE.INK }}>{m.name}</span>
              <span style={{ fontFamily: SANS, fontSize: P ? 44 : 48, color: CLAUDE.INK_SOFT }}>{Math.round(m.total * tot)}B total</span>
            </div>
            <div style={{ position: 'relative', marginTop: 16, height: barH, width: S.w, borderRadius: 12, background: CLAUDE.BORDER }}>
              <div style={{ position: 'absolute', left: 0, top: 0, height: barH, width: S.w * tot, borderRadius: 12, background: CLAUDE.INK_SOFT }} />
              <div style={{ position: 'absolute', left: 0, top: 0, height: barH, width: Math.max(10, S.w * frac) * act, borderRadius: 12, background: ACC_TEXT }} />
            </div>
            <div style={{ marginTop: 14, fontFamily: SANS, fontSize: P ? 46 : 48, fontWeight: 600, color: CLAUDE.INK, opacity: act }}>
              {m.active}B used per token
            </div>
          </div>
        );
      })}
      <Note x={S.x} y={top + models.length * rowStep + (P ? 0 : -20)} w={S.w} a={ease(ramp(t, 0.6, 0.7))} text={note} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// MoeMemory — every expert must be loaded; only a few compute
// ===========================================================================
export const moeMemorySchema = z.object({
  title: z.string().default('The catch: memory'),
  n: z.number().int().default(8),
  running: z.array(z.number()).default([1, 5]),
  memLabel: z.string().default('in memory: all 47B'),
  runLabel: z.string().default('computing: ~13B per token'),
  runFraction: z.number().default(13 / 47),
  source: z.string().default('Mixtral 8x7B figures (Mistral AI 2024)'),
  sparkLine: z.string().default('Stored, not used.'),
  durationSeconds: z.number().optional(),
});
export const moeMemoryMeta = durMeta(5);
export const MoeMemory: React.FC<z.infer<typeof moeMemorySchema>> = ({ title, n, running, memLabel, runLabel, runFraction, source, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 330 : 240;
  const cardW = P ? S.w : 960;
  const cardH = P ? 560 : 640;
  const pad = 40;
  const perRow = 4;
  const gap = 22;
  const w = (cardW - pad * 2 - gap * (perRow - 1)) / perRow;
  const h = (cardH - 130 - pad - gap) / 2;
  const run = ease(ramp(t, 0.55, 0.65));
  const meterX = P ? S.x : S.x + cardW + 70;
  const meterW = P ? S.w : S.r - meterX;
  const meterTop = P ? top + cardH + 50 : top + 40;
  const mem = ease(ramp(t, 0.1, 0.45));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: S.x, top, width: cardW, height: cardH, border: `4px solid ${CLAUDE.INK_SOFT}` }}>
        <div style={{ position: 'absolute', left: pad, top: 34, fontFamily: MONO, fontSize: 44, color: CLAUDE.INK }}>GPU memory</div>
        {Array.from({ length: n }).map((_, i) => {
          const loaded = ease(ramp(t, 0.1 + i * 0.04, 0.18 + i * 0.04));
          const hot = running.includes(i) && run > 0.5;
          return (
            <div key={i} style={{
              position: 'absolute', ...gridPos(i, perRow, pad, 120, w, h, gap), width: w, height: h, boxSizing: 'border-box',
              borderRadius: 12, border: `${hot ? 6 : 3}px solid ${hot ? CLAUDE.SPARK : CLAUDE.INK_SOFT}`,
              background: hot ? 'rgba(217,119,87,0.22)' : CLAUDE.PAGE, opacity: loaded,
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              fontFamily: SERIF, fontSize: P ? 60 : 62, color: CLAUDE.INK,
            }}>E{i + 1}</div>
          );
        })}
      </Card>
      <div style={{ position: 'absolute', left: meterX, top: meterTop, width: meterW }}>
        <div style={{ fontFamily: SANS, fontSize: P ? 44 : 46, color: CLAUDE.INK }}>{memLabel}</div>
        <div style={{ marginTop: 14, height: P ? 60 : 70, width: meterW * mem, background: CLAUDE.INK, borderRadius: 10 }} />
        <div style={{ marginTop: P ? 34 : 60, fontFamily: SANS, fontSize: P ? 44 : 46, color: CLAUDE.INK, opacity: run }}>{runLabel}</div>
        <div style={{ marginTop: 14, height: P ? 60 : 70, width: meterW * runFraction * run, background: CLAUDE.SPARK, borderRadius: 10 }} />
        <div style={{ marginTop: P ? 28 : 50, fontFamily: SANS, fontSize: 42, color: CLAUDE.INK_SOFT, opacity: run }}>{source}</div>
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
