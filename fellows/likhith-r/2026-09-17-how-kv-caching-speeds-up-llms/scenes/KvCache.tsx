/**
 * KvCache.tsx — reel-local, DUAL-ASPECT Remotion components for
 * claude-hai-kv-caching ("KV Caching", @HumanitariansAI).
 *
 * Same contract as JevExplainer.tsx / SpecDriven.tsx / RagPipeline.tsx (whose stage
 * helpers it reuses): each component lays out natively for 16:9 (<Name>) and 9:16
 * (<Name>916) — never a crop — and every motion is a pure function of progress,
 * conformed via `durationSeconds`. One running example ("The cat sat on the" → "mat")
 * is illustrative and labelled so on screen; vector shades are decorative.
 * Counts in KvScale and bytes in KvMemory come from the reel's evidence/kv_cache_toy.py.
 * Equations arrive as outlined SVG rows from runtime/scripts/typeset_math.py (MATH-TYPESETTING.md).
 *
 *   KvHook       — a reply that pauses before its first word, then streams quickly
 *   KvRecompute  — no cache: every step re-processes every earlier token (1, 3, 6, … 21)
 *   KvQkv        — each token makes a query, key, value; past keys and values never change
 *   KvStore      — reading the prompt fills the KV cache once (the pause); kept in memory
 *   KvDecode     — the new token's one query against the cached keys/values + the equation
 *   KvScale      — per-new-token work: t(t+1)/2 scores without a cache vs t with one
 *   KvMemory     — cache bytes grow with every token (Llama 2 7B shape, fp16)
 */
import React from 'react';
import { AbsoluteFill, Img } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from './tokens/claude';
import { SERIF, SANS, MONO, ramp, ease, useStage, durMeta, Bug, Title, Spark, Card } from './JevExplainer';

const mathSchema = z.object({ src: z.string(), aspect: z.number().positive(), expression: z.string().default('') });
const EMPTY_MATH = { src: '', aspect: 1, expression: '' };
const Math_: React.FC<{ m: z.infer<typeof mathSchema>; h: number; style?: React.CSSProperties }> = ({ m, h, style }) =>
  m.src ? <Img src={m.src} alt={m.expression} style={{ height: h, width: h * m.aspect, ...style }} /> : null;

const Small: React.FC<{ text: string; style?: React.CSSProperties }> = ({ text, style }) => (
  <div style={{ position: 'absolute', fontFamily: SANS, fontSize: 32, color: CLAUDE.INK_SOFT, ...style }}>{text}</div>
);

const TOKENS = ['The', 'cat', 'sat', 'on', 'the'];
// deterministic decorative shade for vector cells
const shade = (i: number, j: number, k: number) => 0.25 + 0.6 * Math.abs(Math.sin(i * 12.9898 + j * 78.233 + k * 37.719));

const Vec: React.FC<{ n?: number; cell: number; seed: number; row: number; a: number; tint?: string }> = ({ n = 5, cell, seed, row, a, tint = CLAUDE.INK_SOFT }) => (
  <div style={{ display: 'flex', gap: Math.max(3, cell * 0.12), opacity: a }}>
    {Array.from({ length: n }, (_, j) => (
      <div key={j} style={{ width: cell, height: cell, borderRadius: 4, background: tint, opacity: shade(seed, j, row) }} />
    ))}
  </div>
);

// ===========================================================================
// KvHook — a reply pauses before its first word, then the rest streams quickly
// ===========================================================================
export const kvHookSchema = z.object({
  title: z.string().default('Slow start, fast stream'),
  prompt: z.string().default('Tell me a story about a cat.'),
  reply: z.string().default('Once upon a time, a cat sat on the mat and watched the rain.'),
  pauseLabel: z.string().default('pause before the first word'),
  streamLabel: z.string().default('then word after word'),
  sparkLine: z.string().default('Why the pause?'),
  durationSeconds: z.number().optional(),
});
export const kvHookMeta = durMeta(5);
export const KvHook: React.FC<z.infer<typeof kvHookSchema>> = ({ title, prompt, reply, pauseLabel, streamLabel, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const words = reply.split(' ');
  const top = P ? 330 : 250;
  const cardH = P ? 560 : 390;
  const T0 = 0.12, T1 = 0.46, T2 = 0.8;        // prompt sent → first word → last word
  const pause = ramp(t, T0, T1);
  const shown = t < T1 ? 0 : Math.min(words.length, 1 + Math.floor(((t - T1) / (T2 - T1)) * words.length));
  const dots = t > T0 && t < T1 ? '.'.repeat(1 + (Math.floor(t * 60) % 3)) : '';
  // timeline: time runs left→right; the pause is one long block, each word a short tick
  const tlTop = top + cardH + (P ? 110 : 90);
  const tlW = S.w;
  const pauseW = tlW * 0.42;
  const tickW = (tlW - pauseW - 20) / words.length;
  const barT = P ? 24 : 40;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: S.x, top, width: S.w, height: cardH, padding: P ? '30px 36px' : '34px 44px', opacity: ease(ramp(t, 0.02, 0.1)) }}>
        <div style={{
          marginLeft: 'auto', width: 'fit-content', maxWidth: '80%', background: CLAUDE.PAGE, borderRadius: 14,
          padding: '14px 26px', fontFamily: SANS, fontSize: P ? 42 : 44, color: CLAUDE.INK,
        }}>{prompt}</div>
        <div style={{ marginTop: P ? 36 : 30, fontFamily: SERIF, fontSize: P ? 58 : 60, lineHeight: 1.3, color: CLAUDE.INK }}>
          {shown === 0
            ? <span style={{ color: CLAUDE.INK_SOFT }}>{dots}</span>
            : words.slice(0, shown).join(' ')}
        </div>
      </Card>
      <div style={{ position: 'absolute', left: S.x, top: tlTop, width: tlW, height: 90, opacity: ease(ramp(t, 0.1, 0.16)) }}>
        {/* thin solid bar: a structural accent (aspect > 15), never read as accent text */}
        <div style={{ position: 'absolute', left: 0, top: 45 - barT / 2, width: pauseW * pause, height: barT, borderRadius: barT / 2, background: CLAUDE.SPARK }} />
        <div style={{ position: 'absolute', left: 0, top: 45 - barT / 2, width: pauseW, height: barT, borderRadius: barT / 2, border: `3px dashed ${CLAUDE.BORDER}`, boxSizing: 'border-box' }} />
        {words.slice(0, shown).map((w, i) => (
          <div key={i} style={{
            position: 'absolute', left: pauseW + 20 + i * tickW, top: 45 - barT / 2, width: Math.max(6, tickW - 8), height: barT,
            borderRadius: 6, background: CLAUDE.INK_SOFT, opacity: 0.7,
          }} />
        ))}
      </div>
      <Small text={pauseLabel} style={{ left: S.x, top: tlTop + 108, width: pauseW, fontSize: P ? 34 : 36, opacity: ease(ramp(t, 0.2, 0.28)) }} />
      <Small text={streamLabel} style={{ left: S.x + pauseW + 20, top: tlTop + 108, width: tlW - pauseW - 20, fontSize: P ? 34 : 36, opacity: ease(ramp(t, 0.5, 0.58)) }} />
      <Small text="time →" style={{ right: (P ? 1080 : 1920) - S.r, top: tlTop - 52, fontSize: 30, opacity: ease(ramp(t, 0.1, 0.16)) }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// KvRecompute — without a cache, step t re-processes all t tokens so far
// ===========================================================================
export const kvRecomputeSchema = z.object({
  title: z.string().default('Without a cache'),
  tokens: z.array(z.string()).default([...TOKENS, 'mat']),
  counterLabel: z.string().default('tokens re-processed'),
  sparkLine: z.string().default('Every step, from scratch.'),
  durationSeconds: z.number().optional(),
});
export const kvRecomputeMeta = durMeta(6);
export const KvRecompute: React.FC<z.infer<typeof kvRecomputeSchema>> = ({ title, tokens, counterLabel, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const n = tokens.length;
  const top = P ? 320 : 240;
  const gridW = P ? S.w : 1180;
  const labelW = P ? 130 : 170;
  const cellW = (gridW - labelW) / n - 10;
  const rowH = P ? 92 : 100;
  const rowGap = P ? 12 : 12;
  const rowAt = (i: number) => 0.06 + i * 0.11;
  let total = 0;
  const rowsIn = tokens.map((_, i) => ramp(t, rowAt(i), rowAt(i) + 0.08));
  rowsIn.forEach((r, i) => { if (r > 0.5) total += i + 1; });
  const cx = P ? S.x : S.x + gridW + 90;
  const cy = P ? top + n * (rowH + rowGap) + 40 : top + 120;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {tokens.map((_, i) => {
        const a = ease(rowsIn[i]);
        const y = top + i * (rowH + rowGap);
        return (
          <React.Fragment key={i}>
            <div style={{ position: 'absolute', left: S.x, top: y, width: labelW, height: rowH, display: 'flex', alignItems: 'center',
              fontFamily: SANS, fontSize: P ? 34 : 36, color: CLAUDE.INK_SOFT, opacity: a }}>step {i + 1}</div>
            {tokens.slice(0, i + 1).map((tok, j) => {
              const isNew = j === i;
              // older tokens flash: they are being recomputed, not reused
              const flash = isNew ? 0 : Math.max(0, 1 - Math.abs((t - rowAt(i) - 0.04) / 0.05));
              return (
                <div key={j} style={{
                  position: 'absolute', left: S.x + labelW + j * (cellW + 10), top: y, width: cellW, height: rowH,
                  borderRadius: 10, boxSizing: 'border-box', border: `2px solid ${CLAUDE.BORDER}`,
                  background: isNew ? CLAUDE.CARD : `rgba(115,112,95,${0.14 + 0.22 * flash})`,
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  fontFamily: SERIF, fontSize: P ? 34 : 40, color: CLAUDE.INK, opacity: a,
                }}>{tok}</div>
              );
            })}
          </React.Fragment>
        );
      })}
      <div style={{ position: 'absolute', left: cx, top: cy, opacity: ease(ramp(t, 0.08, 0.16)) }}>
        <div style={{ fontFamily: SERIF, fontSize: P ? 150 : 190, lineHeight: 1, color: CLAUDE.SPARK }}>{total}</div>
        <div style={{ fontFamily: SANS, fontSize: P ? 38 : 42, color: CLAUDE.INK, marginTop: 10 }}>{counterLabel}</div>
        <div style={{ fontFamily: SANS, fontSize: 32, color: CLAUDE.INK_SOFT, marginTop: 10, width: P ? S.w : 520 }}>
          to write {n} tokens · grey = recomputed again
        </div>
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// KvQkv — every token makes a query, a key and a value; past K and V never change
// ===========================================================================
export const kvQkvSchema = z.object({
  title: z.string().default('Query, key, value'),
  tokens: z.array(z.string()).default(TOKENS.slice(0, 4)),
  fixedLabel: z.string().default('past keys and values never change'),
  why: z.string().default('earlier tokens never look at later ones'),
  sparkLine: z.string().default('Same K and V, every step.'),
  durationSeconds: z.number().optional(),
});
export const kvQkvMeta = durMeta(6);
export const KvQkv: React.FC<z.infer<typeof kvQkvSchema>> = ({ title, tokens, fixedLabel, why, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const n = tokens.length;
  const top = P ? 330 : 250;
  const colW = S.w / n;
  const cell = P ? 36 : 44;
  const fixed = ease(ramp(t, 0.56, 0.66));
  const rows: Array<{ k: string; name: string }> = [{ k: 'q', name: 'query' }, { k: 'k', name: 'key' }, { k: 'v', name: 'value' }];
  const rowY = (r: number) => top + (P ? 170 : 150) + r * (P ? 170 : 130);
  const boxTop = rowY(1) - (P ? 40 : 22), boxH = 2 * (P ? 170 : 130) - (P ? 40 : 4);
  const pastW = colW * (n - 1);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {tokens.map((tok, i) => {
        const a = ease(ramp(t, 0.05 + i * 0.05, 0.12 + i * 0.05));
        const x = S.x + i * colW;
        return (
          <React.Fragment key={i}>
            <Card style={{ left: x + 12, top, width: colW - 24, height: P ? 100 : 104, display: 'flex', alignItems: 'center', justifyContent: 'center',
              fontFamily: SERIF, fontSize: P ? 46 : 56, color: CLAUDE.INK, opacity: a }}>{tok}</Card>
            {rows.map((r, ri) => {
              const va = ease(ramp(t, 0.2 + i * 0.06 + ri * 0.02, 0.28 + i * 0.06 + ri * 0.02));
              const past = i < n - 1;
              const dimQ = r.k === 'q' && past ? 1 - 0.55 * fixed : 1;   // stays ≥ 45%
              return (
                <div key={r.k} style={{ position: 'absolute', left: x + 20, top: rowY(ri), display: 'flex', alignItems: 'center', gap: 14, opacity: va * dimQ }}>
                  <span style={{ fontFamily: SERIF, fontStyle: 'italic', fontSize: P ? 40 : 48, color: CLAUDE.INK, width: P ? 26 : 34 }}>{r.k}</span>
                  <Vec cell={cell} seed={i + 1} row={ri} a={1} n={P ? 4 : 5} />
                </div>
              );
            })}
          </React.Fragment>
        );
      })}
      <div style={{
        position: 'absolute', left: S.x + 4, top: boxTop, width: pastW - 8, height: boxH, borderRadius: 16,
        border: `4px solid ${CLAUDE.SPARK}`, opacity: fixed, boxSizing: 'border-box',
      }} />
      <div style={{ position: 'absolute', left: S.x, top: boxTop + boxH + 24, width: P ? S.w : pastW, opacity: fixed }}>
        <div style={{ fontFamily: SERIF, fontSize: P ? 50 : 56, color: CLAUDE.SPARK }}>{fixedLabel}</div>
        <div style={{ fontFamily: SANS, fontSize: P ? 36 : 38, color: CLAUDE.INK_SOFT, marginTop: 8, opacity: ease(ramp(t, 0.66, 0.74)) }}>{why}</div>
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// KvStore — reading the prompt fills the cache once (that's the pause)
// ===========================================================================
export const kvStoreSchema = z.object({
  title: z.string().default('The KV cache'),
  tokens: z.array(z.string()).default(TOKENS),
  sweepLabel: z.string().default('reading your prompt · the pause'),
  cacheLabel: z.string().default('KV cache · kept in memory'),
  keptLabel: z.string().default('kept, not recalculated'),
  sparkLine: z.string().default('Compute once, keep it.'),
  durationSeconds: z.number().optional(),
});
export const kvStoreMeta = durMeta(6);
export const KvStore: React.FC<z.infer<typeof kvStoreSchema>> = ({ title, tokens, sweepLabel, cacheLabel, keptLabel, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const n = tokens.length;
  const top = P ? 320 : 240;
  const chipW = S.w / n - 14;
  const chipH = P ? 92 : 100;
  const sweep = ramp(t, 0.12, 0.4);
  const cacheTop = top + chipH + (P ? 190 : 170);
  const pad = 24;                                // cache contents sit inside the outline, inside SAFE
  const labelW = P ? 70 : 90;
  const cellW = (S.w - 2 * pad - labelW) / n - 14;
  const cellH = P ? 210 : 134;
  const fill = (i: number) => ease(ramp(t, 0.18 + i * 0.045, 0.3 + i * 0.045));
  const glow = ease(ramp(t, 0.38, 0.45));
  const kept = ease(ramp(t, 0.52, 0.6));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {tokens.map((tok, i) => (
        <Card key={i} style={{ left: S.x + i * (chipW + 14), top, width: chipW, height: chipH, display: 'flex', alignItems: 'center', justifyContent: 'center',
          fontFamily: SERIF, fontSize: P ? 40 : 52, color: CLAUDE.INK, opacity: ease(ramp(t, 0.02 + i * 0.02, 0.08 + i * 0.02)) }}>{tok}</Card>
      ))}
      <div style={{ position: 'absolute', left: S.x, top: top + chipH + 18, width: S.w * sweep, height: 10, borderRadius: 5, background: CLAUDE.INK_SOFT, opacity: 0.55 }} />
      <Small text={sweepLabel} style={{ left: S.x, top: top + chipH + 44, fontSize: P ? 36 : 38, opacity: ease(ramp(t, 0.12, 0.2)) }} />
      <div style={{
        position: 'absolute', left: S.x, top: cacheTop - 20, width: S.w, height: 2 * cellH + 14 + 40, borderRadius: 20,
        border: `4px solid ${glow > 0.5 ? CLAUDE.SPARK : CLAUDE.BORDER}`, background: CLAUDE.CARD, boxSizing: 'border-box',
        opacity: ease(ramp(t, 0.14, 0.22)),
      }} />
      {['K', 'V'].map((row, ri) => (
        <React.Fragment key={row}>
          <div style={{ position: 'absolute', left: S.x + pad, top: cacheTop + ri * (cellH + 14), height: cellH, width: labelW, display: 'flex', alignItems: 'center',
            fontFamily: SERIF, fontStyle: 'italic', fontSize: P ? 54 : 64, color: CLAUDE.INK, opacity: ease(ramp(t, 0.16, 0.22)) }}>{row}</div>
          {tokens.map((tok, i) => (
            <div key={i} style={{
              position: 'absolute', left: S.x + pad + labelW + i * (cellW + 14), top: cacheTop + ri * (cellH + 14), width: cellW, height: cellH,
              borderRadius: 10, background: CLAUDE.PAGE, border: `2px solid ${CLAUDE.BORDER}`, boxSizing: 'border-box',
              display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 12,
              opacity: fill(i), transform: `translateY(${(1 - fill(i)) * -60}px)`,
            }}>
              <Vec cell={P ? 22 : 30} n={P ? 4 : 5} seed={i + 1} row={ri + 1} a={1} />
              <span style={{ fontFamily: SANS, fontSize: P ? 28 : 30, color: CLAUDE.INK_SOFT }}>{tok}</span>
            </div>
          ))}
        </React.Fragment>
      ))}
      {cacheLabel && <div style={{ position: 'absolute', left: S.x, top: cacheTop + 2 * cellH + 14 + 44, fontFamily: SERIF, fontSize: P ? 46 : 50,
        color: CLAUDE.INK, opacity: glow }}>{cacheLabel}</div>}
      <div style={{ position: 'absolute', top: cacheTop + 2 * cellH + 14 + (P ? (cacheLabel ? 110 : 44) : 52), fontFamily: SANS, fontSize: P ? 38 : 40,
        ...(P ? { left: S.x } : { right: 1920 - S.r }), color: CLAUDE.INK, opacity: kept }}>✓ {keptLabel}</div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// KvDecode — the new token's single query against the cached keys and values
// ===========================================================================
export const kvDecodeSchema = z.object({
  title: z.string().default('One new query'),
  tokens: z.array(z.string()).default(TOKENS),
  newToken: z.string().default('mat'),
  weights: z.array(z.number()).default([0.06, 0.34, 0.2, 0.08, 0.12, 0.2]),
  equation: mathSchema.default(EMPTY_MATH),
  note: z.string().default('K and V: read from the cache'),
  toyNote: z.string().default('illustrative weights'),
  sparkLine: z.string().default('Only the new query.'),
  durationSeconds: z.number().optional(),
});
export const kvDecodeMeta = durMeta(6);
export const KvDecode: React.FC<z.infer<typeof kvDecodeSchema>> = ({ title, tokens, newToken, weights, equation, note, toyNote, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const all = [...tokens, newToken];
  const n = all.length;
  const top = P ? 320 : 230;
  const labelW = P ? 60 : 80;
  const newW = P ? 0 : 250;                      // landscape: the new token's query sits right of the cache
  const cellW = (S.w - labelW - newW - (P ? 0 : 40)) / n - 12;
  const cellH = P ? 96 : 104;
  const append = ease(ramp(t, 0.1, 0.22));
  const qIn = ease(ramp(t, 0.2, 0.28));
  const score = (i: number) => ease(ramp(t, 0.3 + i * 0.03, 0.4 + i * 0.03));
  const eqIn = ease(ramp(t, 0.56, 0.66));
  const barTop = top + 2 * (cellH + 12) + 12;
  const barMax = P ? 170 : 130;       // tallest bar; keeps the smallest weight bar above the §8.1 run floor
  const qx = P ? S.x + S.w / 2 - 110 : S.r - newW + 30;
  const qy = P ? barTop + barMax + 60 : top + 20;
  const eqH = P ? 230 : 220;
  const eqTop = P ? qy + 250 : barTop + barMax + 56;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {['K', 'V'].map((row, ri) => (
        <React.Fragment key={row}>
          <div style={{ position: 'absolute', left: S.x, top: top + ri * (cellH + 12), height: cellH, width: labelW, display: 'flex', alignItems: 'center',
            fontFamily: SERIF, fontStyle: 'italic', fontSize: P ? 48 : 56, color: CLAUDE.INK }}>{row}</div>
          {all.map((tok, i) => {
            const isNew = i === n - 1;
            const a = isNew ? append : 1;
            return (
              <div key={i} style={{
                position: 'absolute', left: S.x + labelW + i * (cellW + 12), top: top + ri * (cellH + 12), width: cellW, height: cellH,
                borderRadius: 10, boxSizing: 'border-box', border: `2px solid ${CLAUDE.BORDER}`, background: isNew ? CLAUDE.CARD : CLAUDE.PAGE,
                display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 6,
                opacity: a, transform: `translateX(${(1 - a) * 80}px)`,
              }}>
                <Vec cell={P ? 16 : 22} n={4} seed={i + 1} row={ri + 1} a={1} />
                <span style={{ fontFamily: SANS, fontSize: P ? 42 : 44, color: isNew ? CLAUDE.INK : CLAUDE.INK_SOFT }}>{tok}</span>
              </div>
            );
          })}
        </React.Fragment>
      ))}
      {/* the query's score against every cached key */}
      {all.map((_, i) => {
        const w = weights[i] ?? 0.1;
        const h = barMax * (w / Math.max(...weights)) * score(i);
        return (
          <div key={i} style={{
            position: 'absolute', left: S.x + labelW + i * (cellW + 12) + cellW * 0.2, top: barTop + barMax - h, width: cellW * 0.6, height: h,
            borderRadius: 6, background: CLAUDE.INK_SOFT, opacity: 0.6,
          }} />
        );
      })}
      <Small text={toyNote} style={{ left: S.x + labelW, top: barTop + barMax + 8, fontSize: 38, opacity: score(0) }} />
      <div style={{ position: 'absolute', left: qx, top: qy, display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 12, opacity: qIn }}>
        <div style={{ fontFamily: SANS, fontSize: 40, color: CLAUDE.INK_SOFT }}>new token</div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
          <span style={{ fontFamily: SERIF, fontStyle: 'italic', fontSize: P ? 56 : 60, color: CLAUDE.SPARK }}>q</span>
          <Vec cell={P ? 30 : 34} n={4} seed={n} row={0} a={1} tint={CLAUDE.SPARK} />
        </div>
        <div style={{ fontFamily: SERIF, fontSize: P ? 88 : 58, color: CLAUDE.INK }}>“{newToken}”</div>
      </div>
      <div style={{ position: 'absolute', left: S.x, top: eqTop, width: S.w, display: 'flex', flexDirection: 'column', alignItems: P ? 'center' : 'flex-start', gap: 18, opacity: eqIn }}>
        <Math_ m={equation} h={Math.min(eqH, (S.w - 20) / equation.aspect)} />
        <div style={{ fontFamily: SANS, fontSize: 40, color: CLAUDE.INK_SOFT, textAlign: P ? 'center' : 'left', maxWidth: S.w }}>{note}</div>
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// KvScale — per-new-token work: t(t+1)/2 query-key scores vs t with the cache
// ===========================================================================
export const kvScaleSchema = z.object({
  title: z.string().default('Work for one new token'),
  rows: z.array(z.object({ t: z.number(), slow: z.number(), fast: z.number() })).default([
    { t: 10, slow: 55, fast: 10 }, { t: 100, slow: 5050, fast: 100 }, { t: 1000, slow: 500500, fast: 1000 },
  ]),
  slowMath: mathSchema.default(EMPTY_MATH),
  fastMath: mathSchema.default(EMPTY_MATH),
  source: z.string().default('query-key scores at position t · counted by evidence/kv_cache_toy.py'),
  sparkLine: z.string().default('Quadratic to linear.'),
  durationSeconds: z.number().optional(),
});
export const kvScaleMeta = durMeta(6);
const fmtN = (x: number) => Math.round(x).toLocaleString('en-US');
export const KvScale: React.FC<z.infer<typeof kvScaleSchema>> = ({ title, rows, slowMath, fastMath, source, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 330 : 240;
  const c0 = P ? 170 : 330;                      // column widths: t | without | with | ratio
  const cW = P ? (S.w - c0) / 2 : (S.w - c0 - 300) / 2;
  const headH = P ? 200 : 160;
  const rowH = P ? 190 : 150;
  const headIn = ease(ramp(t, 0.04, 0.12));
  const rowAt = (i: number) => 0.14 + i * 0.16;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top, width: S.w, height: headH, opacity: headIn }}>
        <div style={{ position: 'absolute', left: 0, bottom: 16, fontFamily: SANS, fontSize: P ? 34 : 38, color: CLAUDE.INK_SOFT }}>position</div>
        {[{ label: 'without cache', m: slowMath }, { label: 'with cache', m: fastMath }].map((c, ci) => (
          <div key={c.label} style={{ position: 'absolute', left: c0 + ci * cW, width: cW, bottom: 16, display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: 8 }}>
            <Math_ m={c.m} h={c.m.aspect > 1 ? (P ? 96 : 90) : (P ? 56 : 52)} />
            <div style={{ fontFamily: SANS, fontSize: P ? 34 : 38, color: CLAUDE.INK_SOFT }}>{c.label}</div>
          </div>
        ))}
        <div style={{ position: 'absolute', left: 0, right: 0, bottom: 0, height: 3, background: CLAUDE.BORDER }} />
      </div>
      {rows.map((r, i) => {
        const a = ease(ramp(t, rowAt(i), rowAt(i) + 0.06));
        const roll = ease(ramp(t, rowAt(i), rowAt(i) + 0.12));
        const last = i === rows.length - 1;
        const y = top + headH + 20 + i * rowH;
        const ratio = r.slow / r.fast;
        const ratioTxt = `${ratio.toFixed(1)}× less`;
        return (
          <React.Fragment key={r.t}>
            <div style={{ position: 'absolute', left: S.x, top: y, height: rowH * 0.62, display: 'flex', alignItems: 'center',
              fontFamily: SERIF, fontSize: P ? 52 : 60, color: CLAUDE.INK, opacity: a }}><i>t</i>&nbsp;=&nbsp;{fmtN(r.t)}</div>
            {[r.slow, r.fast].map((v, ci) => (
              <div key={ci} style={{ position: 'absolute', left: S.x + c0 + ci * cW, width: cW, top: y, height: rowH * 0.62, display: 'flex', alignItems: 'center', justifyContent: 'flex-end',
                fontFamily: MONO, fontSize: P ? 58 : 68, color: CLAUDE.INK, opacity: a }}>{fmtN(v * roll)}</div>
            ))}
            <div style={{
              position: 'absolute', opacity: ease(ramp(t, rowAt(i) + 0.1, rowAt(i) + 0.15)),
              ...(P ? { left: S.x + c0, top: y + rowH * 0.6, width: S.w - c0, textAlign: 'right' as const }
                    : { left: S.x + c0 + 2 * cW + 40, top: y, width: 260, height: rowH * 0.62, display: 'flex', alignItems: 'center' }),
              fontFamily: SANS, fontWeight: 600, fontSize: P ? 36 : 42, color: last ? CLAUDE.SPARK : CLAUDE.INK_SOFT,
            }}>{ratioTxt}</div>
          </React.Fragment>
        );
      })}
      <Small text={source} style={{ left: S.x, top: top + headH + 20 + rows.length * rowH + 10, width: S.w, fontSize: P ? 28 : 30, opacity: ease(ramp(t, 0.6, 0.7)) }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// KvMemory — the cache grows with every token (Llama 2 7B shape, 16-bit)
// ===========================================================================
export const kvMemorySchema = z.object({
  title: z.string().default('The price: memory'),
  tokens: z.number().default(4096),
  gib: z.number().default(2),
  marks: z.array(z.object({ tokens: z.number(), gib: z.number() })).default([
    { tokens: 1024, gib: 0.5 }, { tokens: 2048, gib: 1 }, { tokens: 4096, gib: 2 },
  ]),
  formula: mathSchema.default(EMPTY_MATH),
  legend: z.string().default('K and V · layers · heads · head size · bytes · tokens'),
  model: z.string().default('Llama 2 7B shape · 16-bit · one conversation · 0.5 MiB per token'),
  sparkLine: z.string().default('Longer context, bigger cache.'),
  durationSeconds: z.number().optional(),
});
export const kvMemoryMeta = durMeta(6);
export const KvMemory: React.FC<z.infer<typeof kvMemorySchema>> = ({ title, tokens, gib, marks, formula, legend, model, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 330 : 250;
  const grow = ease(ramp(t, 0.1, 0.62));
  const barH = P ? 64 : 100;         // thin solid bar: structural accent (aspect > 15), never read as text
  const barTop = top + (P ? 170 : 150);
  const nowTok = tokens * grow;
  const fIn = ease(ramp(t, 0.5, 0.6));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top, width: S.w, display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', opacity: ease(ramp(t, 0.04, 0.1)) }}>
        <span style={{ fontFamily: MONO, fontSize: P ? 50 : 60, color: CLAUDE.INK }}>{fmtN(nowTok)} <span style={{ fontFamily: SANS, fontSize: P ? 34 : 38, color: CLAUDE.INK_SOFT }}>tokens</span></span>
        <span style={{ fontFamily: MONO, fontSize: P ? 50 : 60, color: CLAUDE.INK }}>{(gib * grow).toFixed(2)} <span style={{ fontFamily: SANS, fontSize: P ? 34 : 38 }}>GiB</span></span>
      </div>
      <div style={{ position: 'absolute', left: S.x, top: barTop, width: S.w, height: barH, borderRadius: 14, border: `3px solid ${CLAUDE.BORDER}`, background: CLAUDE.CARD, boxSizing: 'border-box' }} />
      <div style={{ position: 'absolute', left: S.x + 6, top: barTop + 6, width: (S.w - 12) * grow, height: barH - 12, borderRadius: 10, background: CLAUDE.SPARK }} />
      {marks.map((m) => {
        const x = S.x + (S.w - 12) * (m.tokens / tokens);
        const a = ease(ramp(t, 0.1 + 0.52 * (m.tokens / tokens) - 0.02, 0.1 + 0.52 * (m.tokens / tokens) + 0.04));
        return (
          <React.Fragment key={m.tokens}>
            <div style={{ position: 'absolute', left: x - 1, top: barTop + barH, width: 3, height: 24, background: CLAUDE.INK_SOFT, opacity: a }} />
            <div style={{ position: 'absolute', left: x - 340, width: 340, top: barTop + barH + 30, textAlign: 'right', whiteSpace: 'nowrap', fontFamily: SANS, fontSize: P ? 30 : 34, color: CLAUDE.INK, opacity: a }}>
              {fmtN(m.tokens)} → {m.gib} GiB
            </div>
          </React.Fragment>
        );
      })}
      <div style={{ position: 'absolute', left: S.x, top: barTop + barH + (P ? 170 : 130), width: S.w, display: 'flex', flexDirection: 'column', alignItems: P ? 'center' : 'flex-start', gap: 16, opacity: fIn }}>
        <Math_ m={formula} h={Math.min(P ? 90 : 110, (S.w - 20) / formula.aspect)} />
        <div style={{ fontFamily: SANS, fontSize: P ? 32 : 36, color: CLAUDE.INK_SOFT, textAlign: P ? 'center' : 'left' }}>{legend}</div>
        <div style={{ fontFamily: SANS, fontSize: P ? 30 : 32, color: CLAUDE.INK_SOFT, textAlign: P ? 'center' : 'left', opacity: ease(ramp(t, 0.62, 0.7)) }}>{model}</div>
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
