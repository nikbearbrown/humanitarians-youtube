/**
 * RagPipeline.tsx — RAG / retrieval-augmented generation scenes: document chunking,
 * vector embeddings on a meaning map, vector database store, cosine similarity top-k
 * retrieval, prompt augmentation with context, grounded generation with citations.
 * Reel-local, DUAL-ASPECT Remotion components for claude-hai-rag-pipelines ("RAG Pipelines, End to End", @HumanitariansAI).
 *
 * Same contract as JevExplainer.tsx / SpecDriven.tsx (whose stage helpers it reuses):
 * each component lays out natively for 16:9 (<Name>) and 9:16 (<Name>916) — never a
 * crop — and every motion is a pure function of progress, conformed via `durationSeconds`.
 * One running example throughout (a store handbook + "Can I get my money back?") is
 * illustrative and labelled so on screen. The 2-D vectors are constructed toys; the
 * cosine scores in RagRetrieve are computed by the reel's evidence/cosine_toy.py.
 *
 *   RagHook      — the model's training data vs. your private docs it never saw
 *   RagRetrain   — retrain on every update (struck) vs. retrieve at query time
 *   RagEmbed     — a document is chunked; each chunk becomes a vector on a meaning map
 *   RagStore     — vectors land in a vector index (vector DB or in-database search)
 *   RagRetrieve  — the question is embedded; cosine similarity ranks chunks; top-k return
 *   RagAugment   — retrieved chunks + the question are assembled into one prompt
 *   RagGenerate  — the model answers from that context, citing the chunks it used
 */
import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from './tokens/claude';
import { SERIF, SANS, MONO, ramp, ease, useStage, durMeta, Bug, Title, Spark, Card } from './JevExplainer';
import type { Stage } from './JevExplainer';

// accent TEXT on cream must pass WCAG 4.5:1 (GATE T §8.3); SPARK #D97757 is 2.74:1, so text uses the deeper step
const ACCENT_TEXT = '#A44A32';

const Note: React.FC<{ x: number; y: number; w: number; a: number; text: string; align?: 'left' | 'right' }> = ({ x, y, w, a, text, align = 'left' }) => (
  <div style={{ position: 'absolute', left: x, top: y, width: w, textAlign: align, fontFamily: SANS, fontSize: 34, color: CLAUDE.INK_SOFT, opacity: a }}>{text}</div>
);

const Label: React.FC<{ text: string; style?: React.CSSProperties }> = ({ text, style }) => (
  <div style={{ position: 'absolute', fontFamily: SANS, fontSize: 38, color: CLAUDE.INK_SOFT, ...style }}>{text}</div>
);

// `word` / `short` are the portrait labels: 9:16 type is ~2× larger (GATE T floor = 1.9% of 3840px), so full sentences don't fit
const chunkSchema = z.object({ text: z.string(), vec: z.tuple([z.number(), z.number()]), word: z.string().optional(), short: z.string().optional() });
const DEFAULT_CHUNKS = [
  { text: 'Refunds within 30 days.', vec: [0.95, 0.25] as [number, number], word: 'Refunds', short: 'Refunds: 30 days' },
  { text: 'Returns need a receipt.', vec: [0.8, 0.55] as [number, number], word: 'Returns', short: 'Returns: receipt' },
  { text: 'Shipping takes 3–5 days.', vec: [0.35, 0.9] as [number, number], word: 'Shipping', short: 'Shipping: 3–5 days' },
  { text: 'Office hours: 9 to 5.', vec: [-0.2, 0.95] as [number, number], word: 'Office', short: 'Office: 9 to 5' },
];
const fmt = (v: [number, number]) => `[${v[0].toFixed(2)}, ${v[1].toFixed(2)}, …]`;

// ===========================================================================
// RagHook — the model knows its training data; your private docs sit outside it
// ===========================================================================
export const ragHookSchema = z.object({
  title: z.string().default('What the model never saw'),
  trained: z.array(z.string()).default(['public web text', 'books', 'code']),
  cutoff: z.string().default('frozen at a training cutoff'),
  docs: z.array(z.string()).default(['handbook.pdf', 'policies.docx', 'tickets.csv']),
  question: z.string().default('"What\'s our refund policy?"'),
  sparkLine: z.string().default('Not in its training data.'),
  durationSeconds: z.number().optional(),
});
export const ragHookMeta = durMeta(6);
export const RagHook: React.FC<z.infer<typeof ragHookSchema>> = ({ title, trained, cutoff, docs, question, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 430 : 270;               // portrait title wraps to two lines
  const colW = P ? S.w : (S.w - 90) / 2;
  const modelIn = ease(ramp(t, 0.04, 0.14));
  const docsIn = ease(ramp(t, 0.34, 0.46));
  const qIn = ease(ramp(t, 0.56, 0.64));
  const gap = ease(ramp(t, 0.7, 0.78));
  const docsX = P ? S.x : S.x + colW + 90;
  const docsTop = P ? top + 400 : top;
  const qTop = P ? docsTop + 330 : top + 530;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: S.x, top, width: colW, height: P ? 360 : 500, padding: P ? '26px 32px' : '34px 40px', opacity: modelIn }}>
        <div style={{ fontFamily: SERIF, fontSize: P ? 68 : 84, color: CLAUDE.INK }}>the LLM</div>
        <div style={{ fontFamily: SANS, fontSize: P ? 38 : 44, color: CLAUDE.INK_SOFT, margin: P ? '6px 0 22px' : '10px 0 40px' }}>knows what it was trained on</div>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 16 }}>
          {trained.map((x, i) => (
            <span key={x} style={{
              fontFamily: SANS, fontSize: P ? 40 : 42, color: CLAUDE.INK, padding: P ? '10px 22px' : '12px 24px', borderRadius: 999,
              border: `2px solid ${CLAUDE.BORDER}`, background: CLAUDE.PAGE, opacity: ease(ramp(t, 0.12 + i * 0.05, 0.2 + i * 0.05)),
            }}>{x}</span>
          ))}
        </div>
        <div style={{ fontFamily: SANS, fontSize: P ? 36 : 42, color: CLAUDE.INK_SOFT, marginTop: P ? 24 : 44, opacity: ease(ramp(t, 0.26, 0.34)) }}>{cutoff}</div>
      </Card>
      <Label text="your private documents" style={{ left: docsX, top: docsTop, opacity: docsIn }} />
      {docs.map((d, i) => (
        <Card key={d} style={{
          left: docsX + i * (P ? 22 : 28), top: docsTop + 64 + i * (P ? 64 : 100), width: (P ? S.w : colW) - 2 * (P ? 22 : 28) - 10,
          height: P ? 96 : 120, padding: '0 30px', display: 'flex', alignItems: 'center', gap: 20, opacity: docsIn,
          fontFamily: MONO, fontSize: P ? 38 : 46, color: CLAUDE.INK,
        }}>
          <span style={{ fontFamily: SANS, fontSize: 34, color: CLAUDE.INK_SOFT }}>🔒</span>{d}
        </Card>
      ))}
      <div style={{
        position: 'absolute', left: docsX, top: qTop, width: P ? S.w : colW,
        display: 'flex', alignItems: 'center', gap: 24, opacity: qIn, transform: `translateY(${(1 - qIn) * 14}px)`,
      }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 50 : 62, color: CLAUDE.INK, fontStyle: 'italic' }}>{question}</span>
        <span style={{
          fontFamily: SERIF, fontSize: P ? 110 : 120, lineHeight: 1, color: ACCENT_TEXT, opacity: gap,
          transform: `scale(${0.7 + 0.3 * gap})`,
        }}>?</span>
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RagRetrain — retraining per update is struck out; retrieve at query time instead
// ===========================================================================
export const ragRetrainSchema = z.object({
  title: z.string().default('Retrain or retrieve?'),
  retrain: z.object({ head: z.string(), steps: z.array(z.string()), cost: z.string() }).default({
    head: 'Retrain the model', steps: ['new doc', 'training run', 'new model'], cost: 'slow · expensive · repeat for every update',
  }),
  retrieve: z.object({ head: z.string(), steps: z.array(z.string()), cost: z.string() }).default({
    head: 'Retrieve at query time', steps: ['new doc', 'add to index', 'ready'], cost: 'the model stays the same',
  }),
  sparkLine: z.string().default('Look it up instead.'),
  durationSeconds: z.number().optional(),
});
export const ragRetrainMeta = durMeta(6);
export const RagRetrain: React.FC<z.infer<typeof ragRetrainSchema>> = ({ title, retrain, retrieve, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 330 : 270;
  const laneH = P ? 440 : 300;
  const laneGap = P ? 50 : 60;
  const strike = ease(ramp(t, 0.44, 0.54));
  const lanes = [
    { ...retrain, a0: 0.04, accent: false },
    { ...retrieve, a0: 0.5, accent: true },
  ];
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {lanes.map((ln, li) => {
        const a = ease(ramp(t, ln.a0, ln.a0 + 0.1));
        const y = top + li * (laneH + laneGap);
        const n = ln.steps.length;
        const stepW = P ? S.w - 60 : (S.w - 80 - 70 * (n - 1)) / n;
        const on = ln.accent && ease(ramp(t, 0.72, 0.8)) > 0.5;
        const dim = li === 0 ? 1 - strike * 0.45 : 1;
        return (
          <Card key={ln.head} accent={on} style={{ left: S.x, top: y, width: S.w, height: laneH, padding: P ? '24px 30px' : '26px 40px', opacity: a * dim }}>
            <div style={{
              fontFamily: SERIF, fontSize: P ? 54 : 58, color: CLAUDE.INK, marginBottom: P ? 14 : 22,
              textDecoration: li === 0 && strike > 0.5 ? 'line-through' : 'none', textDecorationColor: CLAUDE.SPARK, textDecorationThickness: 5,
            }}>{ln.head}</div>
            <div style={{ display: 'flex', flexDirection: P ? 'column' : 'row', alignItems: P ? 'stretch' : 'center', gap: P ? 12 : 0 }}>
              {ln.steps.map((s, i) => {
                const sa = ease(ramp(t, ln.a0 + 0.04 + i * 0.07, ln.a0 + 0.12 + i * 0.07));
                const slow = li === 0 && i === 1;
                const bar = slow ? ramp(t, 0.12, 0.44) * 0.62 : 0;   // the training run never finishes on screen
                return (
                  <React.Fragment key={s}>
                    {i > 0 && !P && <span style={{ width: 70, textAlign: 'center', fontFamily: SANS, fontSize: 44, color: CLAUDE.INK_SOFT, opacity: sa }}>→</span>}
                    <div style={{
                      width: stepW, height: P ? 62 : 92, borderRadius: 12, border: `2px solid ${CLAUDE.BORDER}`, background: CLAUDE.PAGE,
                      position: 'relative', overflow: 'hidden', display: 'flex', alignItems: 'center', justifyContent: 'center',
                      fontFamily: SANS, fontSize: P ? 38 : 42, color: CLAUDE.INK, opacity: sa,
                    }}>
                      {slow && <div style={{ position: 'absolute', left: 0, top: 0, bottom: 0, width: `${bar * 100}%`, background: 'rgba(115,112,95,0.18)' }} />}
                      <span style={{ position: 'relative' }}>{P && i > 0 ? `↓ ${s}` : s}</span>
                    </div>
                  </React.Fragment>
                );
              })}
            </div>
            <div style={{ fontFamily: SANS, fontSize: P ? 36 : 40, color: ln.accent ? ACCENT_TEXT : CLAUDE.INK_SOFT, marginTop: P ? 16 : 26, opacity: ease(ramp(t, ln.a0 + 0.24, ln.a0 + 0.32)) }}>{ln.cost}</div>
          </Card>
        );
      })}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RagEmbed — the document is chunked; each chunk becomes a vector on a meaning map
// ===========================================================================
export const ragEmbedSchema = z.object({
  title: z.string().default('Step 1 · Embed'),
  doc: z.string().default('handbook.md'),
  chunks: z.array(chunkSchema).default(DEFAULT_CHUNKS),
  pairNote: z.string().default('close in meaning, no shared keyword'),
  toyNote: z.string().default('toy 2-D vectors (real: hundreds of dimensions)'),
  sparkLine: z.string().default('Meaning, not keywords.'),
  durationSeconds: z.number().optional(),
});
export const ragEmbedMeta = durMeta(6);
export const RagEmbed: React.FC<z.infer<typeof ragEmbedSchema>> = ({ title, doc, chunks, pairNote, toyNote, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  if (P) return <RagEmbedPortrait st={st} title={title} doc={doc} chunks={chunks} sparkLine={sparkLine} />;
  const top = P ? 300 : 250;
  const listW = P ? S.w : 960;
  const rowH = P ? 92 : 118;
  const rowGap = P ? 14 : 20;
  const docIn = ease(ramp(t, 0.03, 0.1));
  // map: landscape right column; portrait below the chunk list
  const mapX = P ? S.x + 60 : S.x + listW + 70;
  const mapTop = P ? top + 70 + chunks.length * (rowH + rowGap) + 40 : top + 70;
  const mapW = P ? S.w - 120 : S.r - mapX - 20;
  const mapH = P ? 1270 - mapTop : 600;
  const ox = mapX + mapW * (P ? 0.28 : 0.24), oy = mapTop + mapH - 20;       // origin, so the negative-x chunk fits
  const sx = mapW * (P ? 0.68 : 0.66), sy = mapH - 50;
  const pair = ease(ramp(t, 0.72, 0.8));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top, fontFamily: MONO, fontSize: 42, color: CLAUDE.INK, opacity: docIn }}>
        {doc} <span style={{ fontFamily: SANS, fontSize: 36, color: CLAUDE.INK_SOFT }}>→ chunks → vectors</span>
      </div>
      {chunks.map((c, i) => {
        const split = ease(ramp(t, 0.1 + i * 0.05, 0.18 + i * 0.05));
        const vec = ease(ramp(t, 0.34 + i * 0.05, 0.42 + i * 0.05));
        const hot = i < 2 && pair > 0.5;
        return (
          <Card key={c.text} accent={hot} style={{
            left: S.x, top: top + 70 + i * (rowH + rowGap) + (1 - split) * -i * (rowH + rowGap) * 0.6, width: listW, height: rowH,
            padding: P ? '0 24px' : '0 30px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 16, opacity: split,
          }}>
            <span style={{ fontFamily: SERIF, fontSize: P ? 40 : 52, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>{c.text}</span>
            <span style={{ fontFamily: MONO, fontSize: P ? 30 : 34, color: CLAUDE.INK_SOFT, whiteSpace: 'nowrap', opacity: vec }}>{fmt(c.vec)}</span>
          </Card>
        );
      })}
      <svg width={P ? 1080 : 1920} height={P ? 1920 : 1080} style={{ position: 'absolute', left: 0, top: 0 }}>
        <g opacity={ease(ramp(t, 0.44, 0.52))}>
          <line x1={mapX} y1={oy} x2={mapX + mapW} y2={oy} stroke={CLAUDE.BORDER} strokeWidth={3} />
          <line x1={ox} y1={oy} x2={ox} y2={mapTop} stroke={CLAUDE.BORDER} strokeWidth={3} />
        </g>
        {chunks.map((c, i) => {
          const a = ease(ramp(t, 0.5 + i * 0.05, 0.58 + i * 0.05));
          const hot = i < 2 && pair > 0.5;
          return (
            <circle key={c.text} cx={ox + c.vec[0] * sx} cy={oy - c.vec[1] * sy} r={hot ? 22 : 18}
              fill={hot ? CLAUDE.SPARK : CLAUDE.INK_SOFT} opacity={a} />
          );
        })}
        {pair > 0 && (
          <ellipse cx={ox + 0.875 * sx} cy={oy - 0.4 * sy} rx={P ? 150 : 110} ry={P ? 170 : 130}
            fill="none" stroke={CLAUDE.SPARK} strokeWidth={4} strokeDasharray="14 10" opacity={pair} />
        )}
      </svg>
      {chunks.map((c, i) => (
        <div key={c.text} style={{
          position: 'absolute', left: ox + c.vec[0] * sx + (i < 2 ? -30 : 34), top: oy - c.vec[1] * sy - (i < 2 ? (i === 0 ? -30 : 76) : 22),
          transform: i < 2 ? 'translateX(-100%)' : 'none', whiteSpace: 'nowrap',
          fontFamily: SANS, fontSize: P ? 32 : 34, color: CLAUDE.INK, opacity: ease(ramp(t, 0.54 + i * 0.05, 0.62 + i * 0.05)),
        }}>{c.text.split(' ')[0].replace(':', '')}</div>
      ))}
      <Note x={mapX} y={P ? mapTop - 50 : mapTop - 56} w={mapW} a={pair} text={pairNote} align={P ? 'left' : 'left'} />
      <Note x={S.x} y={P ? 1270 : top + 70 + chunks.length * (rowH + rowGap) + 6} w={P ? S.w : listW} a={ease(ramp(t, 0.6, 0.7))} text={toyNote} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RagStore — vectors land in a vector index: a vector DB, or search in your DB
// ===========================================================================
export const ragStoreSchema = z.object({
  title: z.string().default('Step 2 · Store'),
  chunks: z.array(chunkSchema).default(DEFAULT_CHUNKS),
  storeLabel: z.string().default('vector index'),
  options: z.array(z.string()).default(['a vector database', 'or vector search inside your database']),
  lookup: z.string().default('built for fast similarity lookup'),
  sparkLine: z.string().default('Indexed for lookup.'),
  durationSeconds: z.number().optional(),
});
export const ragStoreMeta = durMeta(6);
export const RagStore: React.FC<z.infer<typeof ragStoreSchema>> = ({ title, chunks, storeLabel, options, lookup, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 300 : 270;
  const rowH = P ? 84 : 104;
  const rowGap = P ? 14 : 22;
  const listW = P ? S.w : 640;
  // the store: landscape right of the list, portrait below it
  const dbW = P ? 560 : 560, dbH = P ? 400 : 460;
  const dbX = P ? S.x + (S.w - dbW) / 2 : S.x + listW + 260;
  const dbY = P ? top + chunks.length * (rowH + rowGap) + 90 : top + 20;
  const dbIn = ease(ramp(t, 0.06, 0.16));
  const filled = ramp(t, 0.22, 0.62);
  const optIn = ease(ramp(t, 0.62, 0.72));
  const glow = ease(ramp(t, 0.76, 0.84));
  const rx = dbW / 2, ry = P ? 50 : 56;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {chunks.map((c, i) => {
        const fly = ease(ramp(t, 0.22 + i * 0.1, 0.34 + i * 0.1));
        const sx0 = S.x, sy0 = top + i * (rowH + rowGap);
        const tx = dbX + 70, ty = dbY + ry + 40 + i * 70;
        return (
          <div key={c.text} style={{
            position: 'absolute', left: sx0 + (tx - sx0) * fly, top: sy0 + (ty - sy0) * fly, width: listW - (listW - 420) * fly,
            height: rowH - (rowH - 60) * fly, borderRadius: 12, border: `2px solid ${CLAUDE.BORDER}`, background: CLAUDE.CARD,
            display: 'flex', alignItems: 'center', padding: '0 22px', boxSizing: 'border-box', gap: 16,
            fontFamily: MONO, fontSize: (P ? 32 : 36) - 6 * fly, color: CLAUDE.INK, whiteSpace: 'nowrap', overflow: 'hidden',
            opacity: ease(ramp(t, 0.03 + i * 0.03, 0.1 + i * 0.03)), zIndex: 2,
          }}>
            <span style={{ color: CLAUDE.INK_SOFT }}>c{i + 1}</span>{fmt(c.vec)}
          </div>
        );
      })}
      <svg width={P ? 1080 : 1920} height={P ? 1920 : 1080} style={{ position: 'absolute', left: 0, top: 0, opacity: dbIn }}>
        <path d={`M${dbX},${dbY + ry} L${dbX},${dbY + dbH - ry} A${rx},${ry} 0 0 0 ${dbX + dbW},${dbY + dbH - ry} L${dbX + dbW},${dbY + ry}`}
          fill={CLAUDE.CARD} stroke={glow > 0.5 ? CLAUDE.SPARK : CLAUDE.INK_SOFT} strokeWidth={5} />
        <ellipse cx={dbX + rx} cy={dbY + ry} rx={rx} ry={ry} fill={CLAUDE.PAGE} stroke={glow > 0.5 ? CLAUDE.SPARK : CLAUDE.INK_SOFT} strokeWidth={5} />
      </svg>
      <div style={{
        position: 'absolute', left: dbX, top: dbY + dbH + 18, width: dbW, textAlign: 'center',
        fontFamily: SERIF, fontSize: P ? 50 : 54, color: glow > 0.5 ? ACCENT_TEXT : CLAUDE.INK, opacity: dbIn,
      }}>{storeLabel}</div>
      <div style={{
        position: 'absolute', left: dbX + dbW - 150, top: dbY + ry - 20, fontFamily: SANS, fontSize: 34, color: CLAUDE.INK_SOFT,
        opacity: filled > 0.02 ? 1 : 0, zIndex: 3,
      }}>{Math.round(filled * chunks.length)}/{chunks.length}</div>
      <div style={{
        position: 'absolute', opacity: optIn,
        left: S.x, top: top + (P ? 40 : 60), width: P ? S.w : listW + 180,
      }}>
        {options.map((o, i) => (
          <div key={o} style={{ fontFamily: SERIF, fontSize: i === 0 ? 60 : 50, color: CLAUDE.INK, marginBottom: 26, lineHeight: 1.15 }}>{o}</div>
        ))}
      </div>
      <Note x={S.x} y={top + (P ? 250 : 330)} w={P ? S.w : listW + 120} a={glow} text={lookup} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RagRetrieve — embed the question; cosine similarity ranks the chunks; top-k return
// ===========================================================================
export const ragRetrieveSchema = z.object({
  title: z.string().default('Step 3 · Retrieve'),
  question: z.string().default('Can I get my money back?'),
  qvec: z.tuple([z.number(), z.number()]).default([0.9, 0.35]),
  chunks: z.array(chunkSchema).default(DEFAULT_CHUNKS),
  k: z.number().int().default(2),
  toyNote: z.string().default('toy 2-D vectors, computed scores'),
  sparkLine: z.string().default('Closest meaning wins.'),
  durationSeconds: z.number().optional(),
});
export const ragRetrieveMeta = durMeta(6);

// structured fraction: cos θ = (q · c) / (‖q‖ ‖c‖) — a real bar, bold vectors, italic θ
const CosineFormula: React.FC<{ size: number; a: number }> = ({ size, a }) => {
  const v = (s: string) => <span style={{ fontWeight: 700, fontStyle: 'normal' }}>{s}</span>;
  const part: React.CSSProperties = { padding: `0 ${size * 0.2}px`, whiteSpace: 'nowrap' };
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: size * 0.3, fontFamily: SERIF, fontSize: size, color: CLAUDE.INK, opacity: a }}>
      <span>cos <i>θ</i></span><span>=</span>
      <div style={{ display: 'inline-flex', flexDirection: 'column', alignItems: 'center' }}>
        <span style={part}>{v('q')} · {v('c')}</span>
        <span style={{ alignSelf: 'stretch', height: Math.max(3, size * 0.06), background: CLAUDE.INK, margin: `${size * 0.08}px 0` }} />
        <span style={part}>‖{v('q')}‖ ‖{v('c')}‖</span>
      </div>
    </div>
  );
};

export const RagRetrieve: React.FC<z.infer<typeof ragRetrieveSchema>> = ({ title, question, qvec, chunks, k, toyNote, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  if (P) return <RagRetrievePortrait st={st} title={title} question={question} qvec={qvec} chunks={chunks} k={k} sparkLine={sparkLine} />;
  const top = P ? 300 : 250;
  const cos = (a: [number, number], b: [number, number]) => (a[0] * b[0] + a[1] * b[1]) / (Math.hypot(...a) * Math.hypot(...b));
  const ranked = chunks.map((c) => ({ ...c, s: cos(qvec, c.vec) })).sort((x, y) => y.s - x.s);
  // plot: landscape left, portrait top
  const plotX = S.x, plotTop = top + 70;
  const plotW = P ? S.w : 760, plotH = P ? 340 : 620;
  const ox = plotX + plotW * 0.3, oy = plotTop + plotH;
  const R = Math.min(plotW * 0.66, plotH - 20);
  const qIn = ease(ramp(t, 0.16, 0.26));
  const fIn = ease(ramp(t, 0.3, 0.4));
  const listX = P ? S.x : S.x + plotW + 90;
  const listW = P ? S.w : S.r - listX;
  const listTop = P ? plotTop + plotH + 195 : top + 250;
  const rowH = P ? 72 : 96;
  const rank = ease(ramp(t, 0.46, 0.6));
  const pick = ease(ramp(t, 0.66, 0.74));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top, width: S.w, fontFamily: SERIF, fontSize: P ? 44 : 52, color: ACCENT_TEXT, fontStyle: 'italic', opacity: qIn }}>
        q = embed("{question}")
      </div>
      <svg width={P ? 1080 : 1920} height={P ? 1920 : 1080} style={{ position: 'absolute', left: 0, top: 0 }}>
        <defs>
          <marker id="rag-ah-ink" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill={CLAUDE.INK_SOFT} /></marker>
          <marker id="rag-ah-spark" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill={ACCENT_TEXT} /></marker>
        </defs>
        <line x1={plotX} y1={oy} x2={plotX + plotW} y2={oy} stroke={CLAUDE.BORDER} strokeWidth={3} />
        <line x1={ox} y1={oy} x2={ox} y2={plotTop} stroke={CLAUDE.BORDER} strokeWidth={3} />
        {chunks.map((c, i) => {
          const L = R / Math.hypot(...c.vec);
          const a = ease(ramp(t, 0.03 + i * 0.03, 0.1 + i * 0.03));
          const kept = ranked.findIndex((r) => r.text === c.text) < k;
          return (
            <line key={c.text} x1={ox} y1={oy} x2={ox + c.vec[0] * L} y2={oy - c.vec[1] * L}
              stroke={CLAUDE.INK_SOFT} strokeWidth={kept && pick > 0.5 ? 9 : 6} opacity={a * (kept || pick < 0.5 ? 1 : 0.45)} markerEnd="url(#rag-ah-ink)" />
          );
        })}
        {(() => {
          const L = R * 1.0 / Math.hypot(...qvec);
          return <line x1={ox} y1={oy} x2={ox + qvec[0] * L * qIn} y2={oy - qvec[1] * L * qIn} stroke={ACCENT_TEXT} strokeWidth={10} markerEnd="url(#rag-ah-spark)" opacity={qIn} />;
        })()}
      </svg>
      {chunks.map((c, i) => {
        const L = R / Math.hypot(...c.vec);
        return (
          <div key={c.text} style={{
            position: 'absolute', left: ox + c.vec[0] * L + 14, top: oy - c.vec[1] * L - (i === 0 ? -6 : 48), whiteSpace: 'nowrap',
            fontFamily: SANS, fontSize: P ? 30 : 32, color: CLAUDE.INK_SOFT, opacity: ease(ramp(t, 0.06 + i * 0.03, 0.14 + i * 0.03)),
          }}>c{i + 1}</div>
        );
      })}
      <div style={{ position: 'absolute', left: P ? S.x + 40 : listX, top: P ? plotTop + plotH + 30 : top + 70 }}>
        <CosineFormula size={P ? 50 : 54} a={fIn} />
      </div>
      {ranked.map((r, i) => {
        const orig = chunks.findIndex((c) => c.text === r.text);
        const kept = i < k;
        const y0 = listTop + orig * (rowH + 14), y1 = listTop + i * (rowH + 14);
        return (
          <Card key={r.text} accent={kept && pick > 0.5} style={{
            left: listX, top: y0 + (y1 - y0) * rank, width: listW, height: rowH, padding: P ? '0 24px' : '0 30px',
            display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 18,
            opacity: ease(ramp(t, 0.36 + orig * 0.03, 0.44 + orig * 0.03)) * (kept || pick < 0.5 ? 1 : 0.5),
          }}>
            <span style={{ fontFamily: SERIF, fontSize: P ? 38 : 52, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>
              <span style={{ fontFamily: SANS, color: CLAUDE.INK_SOFT, fontSize: P ? 30 : 40, marginRight: 14 }}>c{orig + 1}</span>{r.text}
            </span>
            <span style={{ fontFamily: MONO, fontSize: P ? 36 : 40, color: kept && pick > 0.5 ? ACCENT_TEXT : CLAUDE.INK, whiteSpace: 'nowrap' }}>
              {r.s.toFixed(2)}{kept && pick > 0.5 ? '  ✓' : ''}
            </span>
          </Card>
        );
      })}
      <Note x={listX} y={listTop + chunks.length * (rowH + 14) + 4} w={listW - (P ? 0 : 140)} a={pick} text={`top k = ${k} retrieved · ${toyNote}`} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RagAugment — retrieved chunks and the question are assembled into one prompt
// ===========================================================================
export const ragAugmentSchema = z.object({
  title: z.string().default('Step 4 · Augment'),
  instruction: z.string().default('Answer using only the context below.'),
  context: z.array(z.string()).default(['Refunds within 30 days.', 'Returns need a receipt.']),
  question: z.string().default('Can I get my money back?'),
  sparkLine: z.string().default('Context beside the question.'),
  durationSeconds: z.number().optional(),
});
export const ragAugmentMeta = durMeta(5);
export const RagAugment: React.FC<z.infer<typeof ragAugmentSchema>> = ({ title, instruction, context, question, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  if (P) return <RagAugmentPortrait st={st} title={title} question={question} sparkLine={sparkLine} />;
  const top = P ? 300 : 250;
  const srcW = P ? S.w : 640;
  const promptX = P ? S.x : S.x + srcW + 110;
  const promptW = P ? S.w : S.r - promptX;
  const promptTop = P ? top + 180 : top;
  const promptH = P ? 700 : 700;
  const pIn = ease(ramp(t, 0.03, 0.12));
  const ctxIn = ease(ramp(t, 0.36, 0.44));
  const qIn = ease(ramp(t, 0.56, 0.66));
  const head = (s: string, a: number) => (
    <div style={{ fontFamily: MONO, fontSize: P ? 32 : 34, color: CLAUDE.INK_SOFT, letterSpacing: 1, opacity: a, marginBottom: 10 }}>{s}</div>
  );
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Label text="retrieved chunks" style={{ left: S.x, top, opacity: ease(ramp(t, 0.04, 0.12)) }} />
      {context.map((c, i) => {
        const fly = ease(ramp(t, 0.18 + i * 0.08, 0.36 + i * 0.08));
        const x0 = S.x + (P ? i * (S.w / 2 + 6) : 0), y0 = top + 64 + (P ? 0 : i * 130);
        const x1 = promptX + 40, y1 = promptTop + (P ? 290 : 300) + i * (P ? 96 : 100);
        return (
          <React.Fragment key={c}>
          <div style={{ position: 'absolute', left: x0, top: y0, width: P ? S.w / 2 - 6 : srcW, height: P ? 84 : 96, borderRadius: 12,
            border: `3px dashed ${CLAUDE.BORDER}`, boxSizing: 'border-box', opacity: fly }} />
          <div style={{
            position: 'absolute', left: x0 + (x1 - x0) * fly, top: y0 + (y1 - y0) * fly,
            width: (P ? S.w / 2 - 6 : srcW) + ((promptW - 80) - (P ? S.w / 2 - 6 : srcW)) * fly, height: P ? 84 : 96,
            borderRadius: 12, border: `3px solid ${fly > 0.95 ? ACCENT_TEXT : CLAUDE.BORDER}`, background: CLAUDE.CARD, boxSizing: 'border-box',
            display: 'flex', alignItems: 'center', padding: '0 22px', gap: 14, zIndex: 3, whiteSpace: 'nowrap', overflow: 'hidden',
            fontFamily: SERIF, fontSize: P ? 34 : 52, color: CLAUDE.INK, opacity: ease(ramp(t, 0.06 + i * 0.04, 0.14 + i * 0.04)),
          }}>
            <span style={{ fontFamily: SANS, fontSize: P ? 28 : 40, color: CLAUDE.INK_SOFT }}>[{i + 1}]</span>{c}
          </div>
          </React.Fragment>
        );
      })}
      <Card style={{ left: promptX, top: promptTop, width: promptW, height: promptH, padding: P ? '26px 40px' : '30px 40px', opacity: pIn }}>
        <div style={{ fontFamily: SERIF, fontSize: P ? 50 : 54, color: CLAUDE.INK, marginBottom: 20 }}>the prompt</div>
        {head('INSTRUCTION', pIn)}
        <div style={{ fontFamily: SANS, fontSize: P ? 38 : 40, color: CLAUDE.INK, marginBottom: 24 }}>{instruction}</div>
        {head('CONTEXT', ctxIn)}
        <div style={{ height: context.length * (P ? 96 : 100) + 10 }} />
        <div style={{ marginTop: 10 }}>{head('QUESTION', qIn)}</div>
        <div style={{ fontFamily: SERIF, fontSize: P ? 44 : 54, color: CLAUDE.INK, fontStyle: 'italic', opacity: qIn, transform: `translateY(${(1 - qIn) * 12}px)` }}>"{question}"</div>
      </Card>
      {!P && <div style={{ position: 'absolute', left: S.x + srcW + 20, top: top + 260, fontFamily: SANS, fontSize: 64, color: CLAUDE.INK_SOFT, opacity: ease(ramp(t, 0.14, 0.22)) }}>→</div>}
      <Note x={P ? S.x : S.x} y={P ? promptTop + promptH + 16 : top + 360} w={P ? S.w : srcW} a={ease(ramp(t, 0.7, 0.8))} text="illustrative prompt" />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RagGenerate — the model answers from the context and points back at its chunks
// ===========================================================================
export const ragGenerateSchema = z.object({
  title: z.string().default('Step 5 · Generate'),
  answer: z.string().default('Yes: within 30 days of purchase, with your receipt.'),
  cites: z.array(z.string()).default(['Refunds within 30 days.', 'Returns need a receipt.']),
  sparkLine: z.string().default('Grounded, not guessed.'),
  durationSeconds: z.number().optional(),
});
export const ragGenerateMeta = durMeta(5);
export const RagGenerate: React.FC<z.infer<typeof ragGenerateSchema>> = ({ title, answer, cites, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  if (P) return <RagGeneratePortrait st={st} title={title} answer={answer} sparkLine={sparkLine} />;
  const top = P ? 300 : 260;
  const boxIn = ease(ramp(t, 0.03, 0.12));
  const typed = Math.floor(ramp(t, 0.16, 0.56) * answer.length);
  const cIn = ease(ramp(t, 0.58, 0.68));
  const link = ease(ramp(t, 0.68, 0.78));
  const flowW = P ? S.w : S.w;
  const stepW = P ? (S.w - 2 * 70) / 3 : 420;
  const flow = ['prompt + context', 'LLM', 'answer'];
  const ansTop = top + (P ? 200 : 210);
  const citeTop = ansTop + (P ? 440 : 270);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top, width: flowW, display: 'flex', alignItems: 'center', opacity: boxIn }}>
        {flow.map((f, i) => (
          <React.Fragment key={f}>
            {i > 0 && <span style={{ width: 70, textAlign: 'center', fontFamily: SANS, fontSize: 48, color: CLAUDE.INK_SOFT }}>→</span>}
            <div style={{
              width: stepW, height: P ? 110 : 120, borderRadius: 14, border: `3px solid ${CLAUDE.BORDER}`, background: CLAUDE.CARD,
              display: 'flex', alignItems: 'center', justifyContent: 'center', textAlign: 'center', boxSizing: 'border-box', padding: '0 12px',
              fontFamily: i === 1 ? SERIF : SANS, fontSize: i === 1 ? (P ? 50 : 56) : (P ? 32 : 40), color: CLAUDE.INK,
            }}>{f}</div>
          </React.Fragment>
        ))}
      </div>
      <Card accent={link > 0.5} style={{ left: S.x, top: ansTop, width: S.w, height: P ? 400 : 230, padding: P ? '28px 36px' : '30px 44px', opacity: boxIn }}>
        <div style={{ fontFamily: SANS, fontSize: 34, color: CLAUDE.INK_SOFT, marginBottom: 14 }}>Q: Can I get my money back?</div>
        <div style={{ fontFamily: SERIF, fontSize: P ? 54 : 64, color: CLAUDE.INK, lineHeight: 1.2 }}>
          {answer.slice(0, typed)}
          {typed >= answer.length && cites.map((_, i) => (
            <sup key={i} style={{ fontFamily: SANS, fontSize: P ? 32 : 40, color: ACCENT_TEXT, marginLeft: 6, opacity: cIn }}>[{i + 1}]</sup>
          ))}
        </div>
      </Card>
      <div style={{ position: 'absolute', left: S.x, top: citeTop, width: S.w, display: 'flex', flexDirection: P ? 'column' : 'row', gap: P ? 18 : 30, opacity: cIn }}>
        {cites.map((c, i) => (
          <div key={c} style={{
            flex: P ? undefined : 1, height: P ? 96 : 110, borderRadius: 12, boxSizing: 'border-box', padding: '0 26px',
            border: `3px solid ${link > 0.5 ? CLAUDE.SPARK : CLAUDE.BORDER}`, background: CLAUDE.CARD,
            display: 'flex', alignItems: 'center', gap: 16, fontFamily: SERIF, fontSize: P ? 40 : 52, color: CLAUDE.INK, whiteSpace: 'nowrap',
          }}>
            <span style={{ fontFamily: SANS, fontSize: P ? 30 : 40, color: ACCENT_TEXT }}>[{i + 1}]</span>{c}
          </div>
        ))}
      </div>
      <Note x={S.x} y={citeTop + (P ? cites.length * 114 + 6 : 130)} w={S.w} a={link} text="answer drawn from the retrieved context · illustrative" />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// PORTRAIT (9:16) layouts for RagEmbed / RagRetrieve / RagAugment / RagGenerate.
// GATE T's floor scales with frame height (72px glyph runs at 3840), so portrait
// type is roughly double the landscape size. What landscape shows side by side,
// portrait shows in sequence, with the switch timed to the narration.
// Every visible run here is sans ≥ PT.sans / serif ≥ PT.serif / mono ≥ PT.mono.
// ===========================================================================
const PT = { sans: 70, serif: 92, mono: 66, head: 58 } as const;
// arrows are thin, short glyphs: at text size they measure under the floor, so they get their own size
const Arrow: React.FC = () => <span style={{ fontFamily: SANS, fontSize: 120, lineHeight: 0.6, verticalAlign: '-0.08em', margin: '0 10px' }}>→</span>;
const PORTRAIT_CHUNKS = DEFAULT_CHUNKS;
const Pnote: React.FC<{ st: Stage; y: number; a: number; text: string }> = ({ st, y, a, text }) => (
  <div style={{ position: 'absolute', left: st.S.x, top: y, width: st.S.w, fontFamily: SANS, fontSize: PT.sans, lineHeight: 1.05, color: CLAUDE.INK_SOFT, opacity: a }}>{text}</div>
);
const pVec = (v: [number, number]) => `[${v[0].toFixed(2)}, ${v[1].toFixed(2)}]`;
const cosOf = (a: [number, number], b: [number, number]) => (a[0] * b[0] + a[1] * b[1]) / (Math.hypot(...a) * Math.hypot(...b));
type Chunk = z.infer<typeof chunkSchema>;
const wordOf = (c: Chunk) => c.word ?? c.text.split(' ')[0].replace(':', '');
const shortOf = (c: Chunk) => c.short ?? c.text;

// RagEmbed 9:16 — phase A: chunks → vectors (rows); phase B: the meaning map
const RagEmbedPortrait: React.FC<{ st: Stage; title: string; doc: string; chunks: Chunk[]; sparkLine: string }> = ({ st, title, doc, chunks, sparkLine }) => {
  const { t, S } = st;
  const rowsOut = ease(ramp(t, 0.34, 0.39));
  const mapIn = ease(ramp(t, 0.36, 0.41));
  const pair = ease(ramp(t, 0.66, 0.74));
  const mapTop = 600, mapBot = 1150;
  const ox = S.x + 260, oy = mapBot - 10;
  const sx = 560, sy = mapBot - mapTop - 60;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top: 300, fontFamily: MONO, fontSize: PT.mono, color: CLAUDE.INK, opacity: ease(ramp(t, 0.02, 0.08)), whiteSpace: 'nowrap' }}>
        {doc}<span style={{ fontFamily: SANS, fontSize: PT.sans, color: CLAUDE.INK_SOFT }}><Arrow />vectors</span>
      </div>
      {chunks.map((c, i) => {
        const a = ease(ramp(t, 0.05 + i * 0.03, 0.11 + i * 0.03)) * (1 - rowsOut);
        const vec = ease(ramp(t, 0.16 + i * 0.03, 0.22 + i * 0.03));
        return a <= 0.001 ? null : (
          <Card key={c.text} style={{
            left: S.x, top: 440 + i * 150, width: S.w, height: 128, padding: '0 28px', opacity: a,
            display: 'flex', alignItems: 'center', justifyContent: 'space-between', transform: `translateX(${(1 - ease(ramp(t, 0.05 + i * 0.03, 0.11 + i * 0.03))) * -40}px)`,
          }}>
            <span style={{ fontFamily: SERIF, fontSize: PT.serif, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>{wordOf(c)}</span>
            <span style={{ fontFamily: MONO, fontSize: PT.mono, color: CLAUDE.INK_SOFT, whiteSpace: 'nowrap', opacity: vec }}>{pVec(c.vec)}</span>
          </Card>
        );
      })}
      <div style={{ position: 'absolute', left: S.x, top: 420, width: S.w, fontFamily: SANS, fontSize: PT.sans, lineHeight: 1.1, color: ACCENT_TEXT, opacity: pair }}>
        close in meaning,<br />no shared keyword
      </div>
      <svg width={1080} height={1920} style={{ position: 'absolute', left: 0, top: 0, opacity: mapIn }}>
        <line x1={S.x} y1={oy} x2={S.r} y2={oy} stroke={CLAUDE.BORDER} strokeWidth={4} />
        <line x1={ox} y1={oy} x2={ox} y2={mapTop} stroke={CLAUDE.BORDER} strokeWidth={4} />
        {chunks.map((c, i) => {
          const hot = i < 2 && pair > 0.5;
          return <circle key={c.text} cx={ox + c.vec[0] * sx} cy={oy - c.vec[1] * sy} r={hot ? 30 : 24}
            fill={hot ? CLAUDE.SPARK : CLAUDE.INK_SOFT} opacity={ease(ramp(t, 0.38 + i * 0.02, 0.43 + i * 0.02))} />;
        })}
        {pair > 0 && <ellipse cx={ox + 0.875 * sx} cy={oy - 0.4 * sy} rx={150} ry={200} fill="none" stroke={CLAUDE.SPARK} strokeWidth={5} strokeDasharray="16 12" opacity={pair} />}
      </svg>
      {chunks.map((c, i) => {
        // Refunds / Returns labels sit left of their dots (the right edge is close); the others sit right
        const left = i < 2;
        return (
          <div key={c.text} style={{
            position: 'absolute', top: oy - c.vec[1] * sy - 44, whiteSpace: 'nowrap',
            left: ox + c.vec[0] * sx + (left ? -44 : 40), transform: left ? 'translateX(-100%)' : 'none',
            fontFamily: SANS, fontSize: PT.sans, color: CLAUDE.INK, opacity: mapIn * ease(ramp(t, 0.39 + i * 0.02, 0.44 + i * 0.02)),
          }}>{wordOf(c)}</div>
        );
      })}
      <Pnote st={st} y={1180} a={ease(ramp(t, 0.42, 0.48))} text="toy 2-D vectors" />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// RagRetrieve 9:16 — phase A: question vector + formula; phase B: the ranked scores
const RagRetrievePortrait: React.FC<{ st: Stage; title: string; question: string; qvec: [number, number]; chunks: Chunk[]; k: number; sparkLine: string }> = ({ st, title, question, qvec, chunks, k, sparkLine }) => {
  const { t, S } = st;
  const ranked = chunks.map((c, i) => ({ ...c, i, s: cosOf(qvec, c.vec) })).sort((x, y) => y.s - x.s);
  const qIn = ease(ramp(t, 0.14, 0.24));
  const fIn = ease(ramp(t, 0.34, 0.42));
  const aOut = ease(ramp(t, 0.58, 0.64));
  const listIn = ease(ramp(t, 0.62, 0.68));
  const rank = ease(ramp(t, 0.68, 0.78));
  const pick = ease(ramp(t, 0.8, 0.86));
  const ox = S.x + 300, oy = 930, R = 330;
  const rowY = (j: number) => 560 + j * 142;
  const mid = Math.ceil(question.split(' ').length / 2);
  const words = question.split(' ');
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top: 300, width: S.w, fontFamily: SERIF, fontSize: PT.serif, lineHeight: 1.1, color: ACCENT_TEXT, fontStyle: 'italic', opacity: qIn }}>
        “{words.slice(0, mid).join(' ')}<br />{words.slice(mid).join(' ')}”
      </div>
      <div style={{ opacity: 1 - aOut }}>
        <svg width={1080} height={1920} style={{ position: 'absolute', left: 0, top: 0 }}>
          <defs>
            <marker id="rag-p-ink" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill={CLAUDE.INK_SOFT} /></marker>
            <marker id="rag-p-acc" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill={ACCENT_TEXT} /></marker>
          </defs>
          <line x1={S.x} y1={oy} x2={S.r} y2={oy} stroke={CLAUDE.BORDER} strokeWidth={4} />
          {chunks.map((c, i) => {
            const L = R / Math.hypot(...c.vec);
            return <line key={c.text} x1={ox} y1={oy} x2={ox + c.vec[0] * L} y2={oy - c.vec[1] * L} stroke={CLAUDE.INK_SOFT} strokeWidth={8}
              markerEnd="url(#rag-p-ink)" opacity={ease(ramp(t, 0.03 + i * 0.03, 0.1 + i * 0.03))} />;
          })}
          {(() => { const L = R / Math.hypot(...qvec); return <line x1={ox} y1={oy} x2={ox + qvec[0] * L * qIn} y2={oy - qvec[1] * L * qIn} stroke={ACCENT_TEXT} strokeWidth={12} markerEnd="url(#rag-p-acc)" opacity={qIn} />; })()}
        </svg>
        {chunks.map((c, i) => {
          const L = (R + 50) / Math.hypot(...c.vec);
          return (
            <div key={c.text} style={{
              position: 'absolute', left: ox + c.vec[0] * L - 35, top: oy - c.vec[1] * L - 50, fontFamily: SANS, fontSize: PT.sans,
              color: CLAUDE.INK_SOFT, opacity: ease(ramp(t, 0.06 + i * 0.03, 0.13 + i * 0.03)),
            }}>c{i + 1}</div>
          );
        })}
        <div style={{ position: 'absolute', left: S.x + 40, top: 960 }}>
          <CosineFormula size={PT.serif} a={fIn} />
        </div>
      </div>
      {ranked.map((r, j) => {
        const kept = j < k;
        const y = rowY(r.i) + (rowY(j) - rowY(r.i)) * rank;
        return listIn <= 0.001 ? null : (
          <Card key={r.text} accent={kept && pick > 0.5} style={{
            left: S.x, top: y, width: S.w, height: 124, padding: '0 26px', display: 'flex', alignItems: 'center', justifyContent: 'space-between',
            opacity: listIn * (kept || pick < 0.5 ? 1 : 0.55),
          }}>
            <span style={{ fontFamily: SERIF, fontSize: PT.serif, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>{shortOf(r)}</span>
            <span style={{ fontFamily: MONO, fontSize: PT.mono, whiteSpace: 'nowrap', color: kept && pick > 0.5 ? ACCENT_TEXT : CLAUDE.INK }}>
              {r.s.toFixed(2)}{kept && pick > 0.5 ? ' ✓' : ''}
            </span>
          </Card>
        );
      })}
      <Pnote st={st} y={1130} a={pick} text={`top ${k} retrieved`} />
      <Pnote st={st} y={1210} a={pick} text="toy 2-D, computed scores" />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// RagAugment 9:16 — the prompt card fills the band; chunks slide into CONTEXT
const RagAugmentPortrait: React.FC<{ st: Stage; title: string; question: string; sparkLine: string }> = ({ st, title, question, sparkLine }) => {
  const { t, S } = st;
  const ctx = PORTRAIT_CHUNKS.slice(0, 2);
  const cardIn = ease(ramp(t, 0.03, 0.1));
  const qIn = ease(ramp(t, 0.56, 0.66));
  const head = (txt: string, a: number) => (
    <div style={{ fontFamily: MONO, fontSize: PT.head, color: CLAUDE.INK_SOFT, letterSpacing: 2, opacity: a, margin: '8px 0 12px' }}>{txt}</div>
  );
  const words = question.split(' ');
  const mid = Math.ceil(words.length / 2);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: S.x, top: 300, width: S.w, height: 850, padding: '26px 34px', opacity: cardIn }}>
        <div style={{ fontFamily: SERIF, fontSize: PT.serif, color: CLAUDE.INK, lineHeight: 1.1, marginBottom: 10 }}>The prompt</div>
        {head('CONTEXT', ease(ramp(t, 0.1, 0.18)))}
        {ctx.map((c, i) => {
          const slide = ease(ramp(t, 0.18 + i * 0.1, 0.32 + i * 0.1));
          return (
            <div key={c.text} style={{ position: 'relative', height: 124, marginBottom: 14 }}>
              <div style={{ position: 'absolute', inset: 0, borderRadius: 12, border: `3px dashed ${CLAUDE.BORDER}` }} />
              <div style={{
                position: 'absolute', inset: 0, borderRadius: 12, boxSizing: 'border-box', background: CLAUDE.CARD,
                border: `3px solid ${slide > 0.95 ? ACCENT_TEXT : CLAUDE.BORDER}`, display: 'flex', alignItems: 'center', gap: 18, padding: '0 22px',
                opacity: slide, transform: `translateX(${(1 - slide) * 520}px)`, whiteSpace: 'nowrap',
              }}>
                <span style={{ fontFamily: SANS, fontSize: PT.sans, color: CLAUDE.INK_SOFT }}>[{i + 1}]</span>
                <span style={{ fontFamily: SERIF, fontSize: PT.serif, color: CLAUDE.INK }}>{shortOf(c)}</span>
              </div>
            </div>
          );
        })}
        <div style={{ height: 16 }} />
        {head('QUESTION', qIn)}
        <div style={{ fontFamily: SERIF, fontSize: PT.serif, lineHeight: 1.12, color: CLAUDE.INK, fontStyle: 'italic', opacity: qIn, transform: `translateY(${(1 - qIn) * 14}px)` }}>
          “{words.slice(0, mid).join(' ')}<br />{words.slice(mid).join(' ')}”
        </div>
      </Card>
      <Pnote st={st} y={1170} a={ease(ramp(t, 0.7, 0.8))} text="illustrative prompt" />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// RagGenerate 9:16 — context → LLM → answer; the answer types; the citations light their chunks
const RagGeneratePortrait: React.FC<{ st: Stage; title: string; answer: string; sparkLine: string }> = ({ st, title, answer, sparkLine }) => {
  const { t, S } = st;
  const cites = PORTRAIT_CHUNKS.slice(0, 2);
  const flowIn = ease(ramp(t, 0.03, 0.1));
  const typed = Math.floor(ramp(t, 0.14, 0.54) * answer.length);
  const cIn = ease(ramp(t, 0.58, 0.66));
  const link = ease(ramp(t, 0.68, 0.76));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top: 300, width: S.w, fontFamily: SANS, fontSize: PT.sans, color: CLAUDE.INK_SOFT, opacity: flowIn, whiteSpace: 'nowrap' }}>
        context<Arrow /><span style={{ fontFamily: SERIF, fontSize: PT.serif, color: CLAUDE.INK }}>LLM</span><Arrow />answer
      </div>
      <Card accent={link > 0.5} style={{ left: S.x, top: 430, width: S.w, height: 450, padding: '24px 32px', opacity: flowIn }}>
        <div style={{ fontFamily: MONO, fontSize: PT.head, letterSpacing: 2, color: CLAUDE.INK_SOFT, marginBottom: 10 }}>ANSWER</div>
        <div style={{ fontFamily: SERIF, fontSize: PT.serif, lineHeight: 1.12, color: CLAUDE.INK }}>
          {answer.slice(0, typed)}
          {typed >= answer.length && cites.map((_, i) => (
            <span key={i} style={{ fontFamily: SANS, fontSize: PT.sans, color: ACCENT_TEXT, marginLeft: 10, opacity: cIn }}>[{i + 1}]</span>
          ))}
        </div>
      </Card>
      {cites.map((c, i) => (
        <div key={c.text} style={{
          position: 'absolute', left: S.x, top: 910 + i * 142, width: S.w, height: 124, boxSizing: 'border-box', borderRadius: 12,
          border: `3px solid ${link > 0.5 ? ACCENT_TEXT : CLAUDE.BORDER}`, background: CLAUDE.CARD, display: 'flex', alignItems: 'center', gap: 18,
          padding: '0 24px', opacity: cIn, whiteSpace: 'nowrap',
        }}>
          <span style={{ fontFamily: SANS, fontSize: PT.sans, color: ACCENT_TEXT }}>[{i + 1}]</span>
          <span style={{ fontFamily: SERIF, fontSize: PT.serif, color: CLAUDE.INK }}>{shortOf(c)}</span>
        </div>
      ))}
      <Pnote st={st} y={1210} a={link} text="illustrative · from [1][2]" />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
