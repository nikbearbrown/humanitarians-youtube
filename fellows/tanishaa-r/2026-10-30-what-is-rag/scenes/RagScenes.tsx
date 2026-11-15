/**
 * RagScenes.tsx — Remotion components for "What Is RAG?" (Humanitarians AI
 * fellow explainer, Tanishaa). Registered in Root.tsx under the folder "Rag".
 *
 * Palette: Claude fidelity cream #FAF9F5, ink #3D3929, terracotta #D97757 as the
 * ONE accent (shapes); #AF4B2D when the accent carries words (WCAG 4.5:1).
 * 1920x1080, 30 fps. Every component is a pure function of beat progress
 * t = frame / durationInFrames, and every reveal time arrives as a prop
 * (fractions of the beat, set from where the word lands in the narration), so
 * re-timing is a beat-sheet change, never a code change.
 *
 * SOURCE CARE: nothing here hardcodes a number. Retrieval scores come from
 * demo/rag_demo.py output via the beat sheet.
 */
import React from 'react';
import { AbsoluteFill, Img, staticFile, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';

const BG = '#FAF9F5';
const INK = '#3D3929';
const SOFT = '#6C6959';
const GHOST = '#B0AD9A';
const CARD = '#FFFFFF';
const BORDER = '#E5E2D9';
const ACC = '#D97757';
const ACC_TEXT = '#AF4B2D';
const SERIF = '"EB Garamond", Georgia, "Times New Roman", serif';
const SANS = '-apple-system, "SF Pro Text", "Segoe UI", "Helvetica Neue", sans-serif';
const MONO = 'ui-monospace, "SF Mono", Menlo, monospace';

const SX = 96;   // SAFE.x
const SY = 54;   // SAFE.y
const CW = 1920;
const CH = 1080;

const cl = (v: number, a = 0, b = 1) => Math.min(b, Math.max(a, v));
/** 0→1 eased over [a, a+len] of normalized beat time. */
/** Fade length for word-cued reveals: 0.35 s expressed as a fraction of the beat. */
let FADE = 0.03;
const rise = (t: number, a: number, len = FADE) => {
  const p = cl(interpolate(t, [a, a + len], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));
  return 1 - Math.pow(1 - p, 3);
};

const useT = () => {
  const frame = useCurrentFrame();
  const { durationInFrames, fps } = useVideoConfig();
  FADE = (0.35 * fps) / Math.max(1, durationInFrames);
  return frame / Math.max(1, durationInFrames - 1);
};

/** SPARK-LINE LAW: spark + one short serif line, top-left inside SAFE. */
const Spark: React.FC<{ line: string; o: number }> = ({ line, o }) =>
  line ? (
    <div style={{ position: 'absolute', left: SX, top: SY + 6, display: 'flex', alignItems: 'baseline', gap: 16, opacity: o }}>
      <span style={{ fontFamily: SERIF, fontSize: 58, color: ACC_TEXT, lineHeight: 1 }}>*</span>
      <span style={{ fontFamily: SERIF, fontSize: 50, color: SOFT, lineHeight: 1 }}>{line}</span>
    </div>
  ) : null;

/** LOGO LAW: the Humanitarians AI mark, small and low-opacity, lower-right inside SAFE. */
export const HaiBug: React.FC<{ size?: number }> = ({ size = 54 }) => (
  <Img src={staticFile('logos/humanitarians/humanitarians-logo-1.svg')}
    style={{ position: 'absolute', right: SX, bottom: SY, height: size, opacity: 0.32 }} />
);

/** Small honest caption (e.g. "Example syllabus, made up for this demo"). */
const Footnote: React.FC<{ text: string; o: number }> = ({ text, o }) =>
  text ? (
    <div style={{ position: 'absolute', left: SX, bottom: SY + 8, right: SX + 120, fontFamily: SANS,
      fontSize: 26, color: SOFT, opacity: o }}>{text}</div>
  ) : null;

const dur = { durationSeconds: z.number().optional() };

// ===========================================================================
// RagTwoAnswers — the same question, answered twice. Left: from memory, typed
// out confidently, then stamped "no source". Right: empty until retrieval
// exists (B02) — or filled with the sourced answer (B05 reuses the right card).
// ===========================================================================
export const ragTwoAnswersSchema = z.object({
  question: z.string(),
  spark: z.string().default(''),
  leftLabel: z.string().default('From memory'),
  leftAnswer: z.string(),
  stamp: z.string().default('no source'),
  stampAt: z.number().default(0.62),
  rightLabel: z.string().default('With retrieval'),
  rightAnswer: z.string().default(''),
  rightCitation: z.string().default(''),
  footnote: z.string().default(''),
  footnoteShort: z.string().default(''),
  ...dur,
});
export const RagTwoAnswers: React.FC<z.infer<typeof ragTwoAnswersSchema>> = (p) => {
  const t = useT();
  const qIn = rise(t, 0.0);
  const lIn = rise(t, 0.05);
  const rIn = rise(t, 0.10);
  const typed = Math.floor(p.leftAnswer.length * cl(interpolate(t, [0.12, 0.5], [0, 1])));
  const st = rise(t, p.stampAt);
  const CARD_W = 780, TOP = 330, H = 560;
  const box = (x: number, o: number, dashed: boolean): React.CSSProperties => ({
    position: 'absolute', left: x, top: TOP, width: CARD_W, height: H, background: dashed ? 'transparent' : CARD,
    border: dashed ? `3px dashed ${GHOST}` : `2px solid ${BORDER}`, borderRadius: 18, padding: '40px 48px',
    boxSizing: 'border-box', opacity: o, transform: `translateY(${(1 - o) * 24}px)`,
  });
  const label: React.CSSProperties = { fontFamily: SANS, fontSize: 30, letterSpacing: 2, textTransform: 'uppercase', color: SOFT, marginBottom: 24 };
  const hasRight = !!p.rightAnswer;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <Spark line={p.spark} o={qIn} />
      <div style={{ position: 'absolute', top: 170, left: SX, right: SX, textAlign: 'center', fontFamily: SERIF,
        fontSize: 84, color: INK, opacity: qIn }}>“{p.question}”</div>
      <div style={box(SX + 20, lIn, false)}>
        <div style={label}>{p.leftLabel}</div>
        <div style={{ fontFamily: SERIF, fontSize: 52, lineHeight: 1.3, color: INK }}>
          {p.leftAnswer.slice(0, typed)}<span style={{ opacity: typed < p.leftAnswer.length ? 1 : 0, color: ACC }}>|</span>
        </div>
        <div style={{ position: 'absolute', right: 40, bottom: 40, border: `5px solid ${ACC}`, color: ACC_TEXT,
          fontFamily: SANS, fontWeight: 800, fontSize: 44, letterSpacing: 3, textTransform: 'uppercase',
          padding: '10px 26px', borderRadius: 10, opacity: st, transform: `rotate(-6deg) scale(${1.6 - 0.6 * st})` }}>{p.stamp}</div>
      </div>
      <div style={box(CW - SX - 20 - CARD_W, rIn, !hasRight)}>
        <div style={label}>{p.rightLabel}</div>
        {hasRight ? (
          <>
            <div style={{ fontFamily: SERIF, fontSize: 50, lineHeight: 1.3, color: INK }}>{p.rightAnswer}</div>
            <div style={{ marginTop: 26, fontFamily: SANS, fontSize: 32, color: ACC_TEXT }}>{p.rightCitation}</div>
          </>
        ) : (
          <div style={{ fontFamily: SERIF, fontSize: 200, color: GHOST, textAlign: 'center', marginTop: 40 }}>?</div>
        )}
      </div>
      <Footnote text={p.footnote} o={rIn} />
      <HaiBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RagPipeline — Retrieve → Augment → Generate. Each stage lights on its spoken
// word (stageAt), and performs itself: three chunks leave the stack, slide into
// the prompt, and the answer writes with numbered citations.
// ===========================================================================
export const ragPipelineSchema = z.object({
  spark: z.string().default(''),
  stages: z.array(z.object({ name: z.string(), detail: z.string() })).length(3),
  stageAt: z.array(z.number()).length(3),
  ...dur,
});
export const RagPipeline: React.FC<z.infer<typeof ragPipelineSchema>> = (p) => {
  const t = useT();
  const COL_W = 470, GAP = (CW - 2 * SX - 3 * COL_W) / 2, TOP = 220;
  const on = p.stageAt.map((a) => rise(t, a));
  const colX = (i: number) => SX + i * (COL_W + GAP);
  const pull = rise(t, p.stageAt[0] + 0.05, 0.08);     // chunks leave the stack
  const slide = rise(t, p.stageAt[1] + 0.02, 0.08);    // chunks enter the prompt
  const write = cl(interpolate(t, [p.stageAt[2] + 0.02, p.stageAt[2] + 0.18], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));
  const PICK = [1, 3, 4];
  const stage = (i: number) => {
    const active = on[i];
    return (
      <div key={i} style={{ position: 'absolute', left: colX(i), top: TOP, width: COL_W, height: 740,
        background: CARD, border: `2px solid ${active > 0.5 ? ACC : BORDER}`, borderRadius: 20,
        opacity: 0.4 + 0.6 * active, boxSizing: 'border-box', padding: '34px 36px' }}>
        <div style={{ fontFamily: SANS, fontSize: 28, color: SOFT, letterSpacing: 2 }}>{`STEP ${i + 1}`}</div>
        <div style={{ fontFamily: SERIF, fontSize: 76, color: INK, lineHeight: 1.05, marginTop: 6 }}>{p.stages[i].name}</div>
        <div style={{ fontFamily: SERIF, fontSize: 36, color: SOFT, lineHeight: 1.3, marginTop: 14, minHeight: 140 }}>{p.stages[i].detail}</div>
      </div>
    );
  };
  // chunk bars
  const chunkW = 300, chunkH = 34;
  const stackX = colX(0) + 85, stackY = TOP + 420;
  const promptX = colX(1) + 85, promptY = TOP + 470;
  const bars = [0, 1, 2, 3, 4, 5].map((k) => {
    const pickIdx = PICK.indexOf(k);
    const picked = pickIdx >= 0;
    const x0 = stackX, y0 = stackY + k * (chunkH + 10);
    let x = x0, y = y0;
    if (picked) {
      const x1 = x0 + 40, y1 = y0;
      const x2 = promptX, y2 = promptY + pickIdx * (chunkH + 12);
      x = x0 + (x1 - x0) * pull + (x2 - x1) * slide;
      y = y0 + (y2 - y1) * slide;
    }
    return (
      <div key={k} style={{ position: 'absolute', left: x, top: y, width: chunkW, height: chunkH, borderRadius: 6,
        background: picked && pull > 0.3 ? ACC : '#E9E6DC', opacity: picked ? 1 : 1 - 0.4 * pull }} />
    );
  });
  const ansX = colX(2) + 36, ansY = TOP + 420;
  const lines = [0.92, 0.8, 0.88, 0.6];
  return (
    <AbsoluteFill style={{ background: BG }}>
      <Spark line={p.spark} o={rise(t, 0)} />
      {[0, 1, 2].map(stage)}
      {[0, 1].map((i) => (
        <div key={i} style={{ position: 'absolute', left: colX(i) + COL_W + 8, top: TOP + 340, width: GAP - 16,
          textAlign: 'center', fontFamily: SANS, fontSize: 60, color: on[i + 1] > 0.5 ? ACC_TEXT : GHOST }}>→</div>
      ))}
      {/* the prompt frame inside Augment */}
      <div style={{ position: 'absolute', left: promptX - 18, top: promptY - 60, width: chunkW + 36, height: 3 * (chunkH + 12) + 76,
        border: `2px dashed ${GHOST}`, borderRadius: 10, opacity: on[1] }}>
        <div style={{ fontFamily: MONO, fontSize: 24, color: SOFT, padding: '8px 12px' }}>prompt + question</div>
      </div>
      {bars}
      {lines.map((w, i) => {
        const fill = cl(write * lines.length - i);
        return (
          <div key={i} style={{ position: 'absolute', left: ansX, top: ansY + i * 64, display: 'flex', alignItems: 'center', gap: 12 }}>
            <div style={{ width: (COL_W - 140) * w * fill, height: 18, borderRadius: 9, background: '#CFCBBE' }} />
            {i < 3 && fill > 0.95 ? (
              <span style={{ fontFamily: SANS, fontSize: 26, fontWeight: 700, color: ACC_TEXT, border: `2px solid ${ACC}`, borderRadius: 6, padding: '0 8px' }}>{i + 1}</span>
            ) : null}
          </div>
        );
      })}
      <HaiBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RagEmbeddingMap — a document is cut into chunks; each chunk becomes a dot on
// a meaning map; the question lands as a dot and its nearest neighbours light
// up. One neighbour shares no keyword with the question — that link is the
// single terracotta moment. Positions are schematic and captioned as such.
// ===========================================================================
export const ragEmbeddingMapSchema = z.object({
  spark: z.string().default(''),
  chunks: z.array(z.object({ label: z.string(), x: z.number(), y: z.number() })),
  question: z.object({ label: z.string(), x: z.number(), y: z.number() }),
  /** Portrait-only dot positions (phone-size labels need one label per row). */
  chunks916: z.array(z.object({ label: z.string(), x: z.number(), y: z.number() })).optional(),
  question916: z.object({ x: z.number(), y: z.number() }).optional(),
  nearest: z.array(z.string()),
  highlight: z.string(),
  cutAt: z.number().default(0.1),
  flyAt: z.number().default(0.3),
  questionAt: z.number().default(0.55),
  linkAt: z.number().default(0.72),
  footnote: z.string().default(''),
  footnoteShort: z.string().default(''),
  ...dur,
});
export const RagEmbeddingMap: React.FC<z.infer<typeof ragEmbeddingMapSchema>> = (p) => {
  const t = useT();
  const cut = rise(t, p.cutAt, 0.08);
  const fly = rise(t, p.flyAt, 0.12);
  const qIn = rise(t, p.questionAt);
  const MAP = { x: SX + 40, y: 300, w: CW - 2 * SX - 80, h: 620 };
  const n = p.chunks.length;
  const stripW = CW - 2 * SX - 80, pieceW = stripW / n;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <Spark line={p.spark} o={rise(t, 0)} />
      {/* map frame */}
      <div style={{ position: 'absolute', left: MAP.x, top: MAP.y, width: MAP.w, height: MAP.h, border: `2px solid ${BORDER}`,
        borderRadius: 20, background: CARD, opacity: fly }}>
        <div style={{ position: 'absolute', left: 24, top: 16, fontFamily: SANS, fontSize: 26, color: SOFT, letterSpacing: 2 }}>MEANING MAP</div>
      </div>
      {/* links from question to nearest */}
      <svg width={CW} height={CH} style={{ position: 'absolute', left: 0, top: 0 }}>
        {p.nearest.map((lab, i) => {
          const c = p.chunks.find((k) => k.label === lab);
          if (!c) return null;
          const o = rise(t, p.linkAt + i * 0.04);
          const qx = MAP.x + p.question.x * MAP.w, qy = MAP.y + p.question.y * MAP.h;
          const cx = MAP.x + c.x * MAP.w, cy = MAP.y + c.y * MAP.h;
          const hi = lab === p.highlight;
          return <line key={lab} x1={qx} y1={qy} x2={qx + (cx - qx) * o} y2={qy + (cy - qy) * o}
            stroke={hi ? ACC : INK} strokeWidth={hi ? 6 : 4} opacity={hi ? 1 : 0.7} />;
        })}
      </svg>
      {p.chunks.map((c, i) => {
        // strip position (the cut document) → map position (the embedding)
        const sx = SX + 40 + i * pieceW, sy = 170;
        const mx = MAP.x + c.x * MAP.w, my = MAP.y + c.y * MAP.h;
        const near = p.nearest.includes(c.label);
        const lit = near ? rise(t, p.linkAt + p.nearest.indexOf(c.label) * 0.04 + 0.04) : 0;
        const hi = c.label === p.highlight;
        const gap = 10 * cut;
        // piece rectangle morphs into a dot
        const w = (pieceW - gap) * (1 - fly) + 30 * fly;
        const h = 80 * (1 - fly) + 30 * fly;
        const x = sx + gap / 2 + (mx - 15 - sx - gap / 2) * fly;
        const y = sy + (my - 15 - sy) * fly;
        return (
          <React.Fragment key={c.label}>
            <div style={{ position: 'absolute', left: x, top: y, width: w, height: h, borderRadius: 6 + 9 * fly,
              background: hi && lit > 0.5 ? ACC : near && lit > 0.5 ? INK : '#CFCBBE' }} />
            <div style={{ position: 'absolute', left: fly > 0.5 ? mx + 26 : sx + 14, top: fly > 0.5 ? my - 22 : sy + 18,
              fontFamily: SANS, fontSize: fly > 0.5 ? 34 : 26, color: hi && lit > 0.5 ? ACC_TEXT : near && lit > 0.5 ? INK : SOFT,
              fontWeight: lit > 0.5 ? 700 : 400, whiteSpace: 'nowrap' }}>{c.label}</div>
          </React.Fragment>
        );
      })}
      {/* the question */}
      <div style={{ position: 'absolute', left: MAP.x + p.question.x * MAP.w - 22, top: MAP.y + p.question.y * MAP.h - 22,
        width: 44, height: 44, transform: `rotate(45deg) scale(${qIn})`, background: INK }} />
      <div style={{ position: 'absolute', left: MAP.x + p.question.x * MAP.w - 260, top: MAP.y + p.question.y * MAP.h - 100,
        width: 520, textAlign: 'center', fontFamily: SERIF, fontSize: 42, fontStyle: 'italic', color: INK, opacity: qIn }}>“{p.question.label}”</div>
      <Footnote text={p.footnote} o={fly} />
      <HaiBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RagRetrievalDemo — the real output of demo/rag_demo.py. Ranked passages
// arrive with score bars that grow to their measured value; the top passage
// is the one terracotta moment; then the sourced answer fills in.
// ===========================================================================
export const ragRetrievalDemoSchema = z.object({
  spark: z.string().default(''),
  question: z.string(),
  method: z.string(),
  results: z.array(z.object({ section: z.string(), text: z.string(), score: z.number() })),
  resultsAt: z.number().default(0.12),
  answer: z.string(),
  citation: z.string(),
  answerAt: z.number().default(0.6),
  footnote: z.string().default(''),
  footnoteShort: z.string().default(''),
  ...dur,
});
export const RagRetrievalDemo: React.FC<z.infer<typeof ragRetrievalDemoSchema>> = (p) => {
  const t = useT();
  const max = Math.max(...p.results.map((r) => r.score), 1e-6);
  const LW = 1040, RX = SX + LW + 48, RW = CW - SX - RX;
  const aIn = rise(t, p.answerAt);
  return (
    <AbsoluteFill style={{ background: BG }}>
      <Spark line={p.spark} o={rise(t, 0)} />
      <div style={{ position: 'absolute', left: SX, top: 150, width: LW, fontFamily: MONO, fontSize: 30, color: SOFT, opacity: rise(t, 0.02) }}>
        $ python3 rag_demo.py<br />
        <span style={{ color: INK }}>query: “{p.question}”</span>
      </div>
      {p.results.map((r, i) => {
        const o = rise(t, p.resultsAt + i * 0.07);
        const top = i === 0;
        return (
          <div key={r.section} style={{ position: 'absolute', left: SX, top: 280 + i * 220, width: LW, height: 200, boxSizing: 'border-box',
            background: CARD, border: `${top ? 4 : 2}px solid ${top && o > 0.5 ? ACC_TEXT : BORDER}`, borderRadius: 16,
            padding: '20px 28px', opacity: o, transform: `translateX(${(1 - o) * -40}px)` }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 18 }}>
              <span style={{ fontFamily: SANS, fontSize: 30, fontWeight: 700, color: INK }}>{`#${i + 1}  ${r.section}`}</span>
              <div style={{ flex: 1 }} />
              <div style={{ width: 220 * (r.score / max) * o, height: 20, borderRadius: 10, background: top ? ACC_TEXT : '#CFCBBE' }} />
              <span style={{ fontFamily: MONO, fontSize: 30, color: top ? ACC_TEXT : SOFT, width: 100, textAlign: 'right' }}>{(r.score * o).toFixed(3)}</span>
            </div>
            <div style={{ fontFamily: SERIF, fontSize: 34, lineHeight: 1.28, color: top ? INK : SOFT, marginTop: 12 }}>{r.text}</div>
          </div>
        );
      })}
      <div style={{ position: 'absolute', left: RX, top: 280, width: RW, height: 640, boxSizing: 'border-box', background: CARD,
        border: `2px solid ${BORDER}`, borderRadius: 18, padding: '34px 36px', opacity: aIn, transform: `translateY(${(1 - aIn) * 24}px)` }}>
        <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 2, color: SOFT }}>WITH RETRIEVAL</div>
        <div style={{ fontFamily: SERIF, fontSize: 46, lineHeight: 1.3, color: INK, marginTop: 20 }}>{p.answer}</div>
        <div style={{ fontFamily: SANS, fontSize: 30, color: ACC_TEXT, marginTop: 24 }}>{p.citation}</div>
      </div>
      <div style={{ position: 'absolute', left: RX, top: 150, width: RW, fontFamily: SANS, fontSize: 26, color: SOFT, opacity: rise(t, 0.02) }}>{p.method}</div>
      <Footnote text={p.footnote} o={rise(t, 0.05)} />
      <HaiBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RagWhenToUse — items sort into two columns on their spoken words; the warning
// card drops in last and takes the one accent.
// ===========================================================================
export const ragWhenToUseSchema = z.object({
  spark: z.string().default(''),
  useHeader: z.string(),
  useItems: z.array(z.object({ text: z.string(), at: z.number() })),
  skipHeader: z.string(),
  skipItems: z.array(z.object({ text: z.string(), at: z.number() })),
  warning: z.string(),
  warningAt: z.number(),
  useHeaderAt: z.number().optional(),
  skipHeaderAt: z.number().optional(),
  ...dur,
});
export const RagWhenToUse: React.FC<z.infer<typeof ragWhenToUseSchema>> = (p) => {
  const t = useT();
  const COL_W = 820, TOP = 120;
  const col = (x: number, header: string, items: { text: string; at: number }[], mark: string, delay: number) => (
    <div style={{ position: 'absolute', left: x, top: TOP, width: COL_W }}>
      <div style={{ fontFamily: SERIF, fontSize: 84, color: INK, opacity: rise(t, delay), borderBottom: `3px solid ${INK}`, paddingBottom: 12 }}>{header}</div>
      {items.map((it, i) => {
        const o = rise(t, it.at);
        return (
          <div key={i} style={{ display: 'flex', gap: 22, alignItems: 'baseline', marginTop: 40, opacity: o,
            transform: `translateY(${(1 - o) * 30}px)` }}>
            <span style={{ fontFamily: SANS, fontSize: 54, color: INK, width: 50 }}>{mark}</span>
            <span style={{ fontFamily: SERIF, fontSize: 60, color: INK, lineHeight: 1.18 }}>{it.text}</span>
          </div>
        );
      })}
    </div>
  );
  const w = rise(t, p.warningAt);
  return (
    <AbsoluteFill style={{ background: BG }}>
      {col(SX, p.useHeader, p.useItems, '✓', p.useHeaderAt ?? p.useItems[0]?.at ?? 0)}
      {col(CW - SX - COL_W, p.skipHeader, p.skipItems, '✕', p.skipHeaderAt ?? p.skipItems[0]?.at ?? 0.5)}
      <div style={{ position: 'absolute', left: SX + 100, right: SX + 100, top: 790, background: CARD, border: `4px solid ${ACC}`,
        borderRadius: 18, padding: '30px 40px', textAlign: 'center', fontFamily: SERIF, fontSize: 64, color: ACC_TEXT,
        opacity: w, transform: `translateY(${(1 - w) * -60}px)` }}>{p.warning}</div>
      <HaiBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// HaiTitleOutro — the Humanitarians AI outro: the HAI mark full-size, the
// episode title restated with the terracotta period, the handle beneath.
// ===========================================================================
export const haiTitleOutroSchema = z.object({
  title: z.string(),
  handle: z.string().default('@HumanitariansAI'),
  ...dur,
});
export const HaiTitleOutro: React.FC<z.infer<typeof haiTitleOutroSchema>> = (p) => {
  const t = useT();
  const a = rise(t, 0.0, 0.15), b = rise(t, 0.12, 0.15), c = rise(t, 0.25, 0.15);
  const title = p.title.replace(/[.?!]$/, '');
  return (
    <AbsoluteFill style={{ background: BG, alignItems: 'center', justifyContent: 'center' }}>
      <Img src={staticFile('logos/humanitarians/humanitarians-logo-1.svg')} style={{ height: 360, opacity: a, marginBottom: 70 }} />
      <div style={{ fontFamily: SERIF, fontSize: 245, color: INK, opacity: b, lineHeight: 1 }}>
        {title}<span style={{ color: ACC }}>.</span>
      </div>
      <div style={{ fontFamily: SANS, fontSize: 72, color: SOFT, marginTop: 60, opacity: c }}>{p.handle}</div>
    </AbsoluteFill>
  );
};

// ===========================================================================
// HaiBugOverlay — transparent LOGO-LAW bug, composited over library scenes
// that do not draw one themselves (composer, hesitant writer, verdict page).
// ===========================================================================
export const haiBugOverlaySchema = z.object({ ...dur });
export const HaiBugOverlay: React.FC = () => (
  <AbsoluteFill><HaiBug /></AbsoluteFill>
);

// ===========================================================================
// PORTRAIT (9:16) VARIANTS — native 1080×1920 layouts, registered as <Name>916.
// Same schemas and cue props as landscape. GATE T measures glyph height against
// 1.9% of the 3840 px frame, so portrait type is phone-size: serif >= 92, sans >= 72
// (design px). SHOW LESS: portrait carries fewer words, never smaller ones —
// no spark lines or stage details (the narration says them), short footnotes,
// first sentences only. Safe area: x 54–1026, y 96–1824.
// ===========================================================================
const PW = 1080, PH = 1920, PX = 54, PY = 96;
const PSERIF = 92, PSANS = 72, PCAPS = 52;

const PBug: React.FC = () => (
  <Img src={staticFile('logos/humanitarians/humanitarians-logo-1.svg')}
    style={{ position: 'absolute', right: PX, bottom: PY, height: 60, opacity: 0.32 }} />
);

const PFootnote: React.FC<{ text: string; o: number }> = ({ text, o }) =>
  text ? (
    <div style={{ position: 'absolute', left: PX, bottom: PY, right: PX + 80, fontFamily: SANS,
      fontSize: PSANS, lineHeight: 1.15, color: SOFT, opacity: o }}>{text}</div>
  ) : null;

const firstSentence = (s: string) => {
  const m = s.match(/^.*?[.!?](\s|$)/);
  return (m ? m[0] : s).trim();
};

export const RagTwoAnswers916: React.FC<z.infer<typeof ragTwoAnswersSchema>> = (p) => {
  const t = useT();
  const qIn = rise(t, 0.0), lIn = rise(t, 0.05), rIn = rise(t, 0.10);
  const typed = Math.floor(p.leftAnswer.length * cl(interpolate(t, [0.12, 0.5], [0, 1])));
  const st = rise(t, p.stampAt);
  const W = PW - 2 * PX, H = 540;
  const box = (top: number, o: number, dashed: boolean): React.CSSProperties => ({
    position: 'absolute', left: PX, top, width: W, height: H, background: dashed ? 'transparent' : CARD,
    border: dashed ? `4px dashed ${GHOST}` : `2px solid ${BORDER}`, borderRadius: 20, padding: '30px 40px',
    boxSizing: 'border-box', opacity: o, transform: `translateY(${(1 - o) * 24}px)`,
  });
  const label: React.CSSProperties = { fontFamily: SANS, fontSize: PCAPS, letterSpacing: 3, textTransform: 'uppercase', color: SOFT, marginBottom: 14 };
  const hasRight = !!p.rightAnswer;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', top: PY + 10, left: PX, right: PX, textAlign: 'center', fontFamily: SERIF,
        fontSize: PSERIF, lineHeight: 1.08, color: INK, opacity: qIn }}>“{p.question}”</div>
      <div style={box(330, lIn, false)}>
        <div style={label}>{p.leftLabel}</div>
        <div style={{ fontFamily: SERIF, fontSize: PSERIF, lineHeight: 1.08, color: INK }}>
          {p.leftAnswer.slice(0, typed)}<span style={{ opacity: typed < p.leftAnswer.length ? 1 : 0, color: ACC }}>|</span>
        </div>
      </div>
      <div style={{ position: 'absolute', left: PX + 360, top: 330 + H - 70, border: `6px solid ${ACC}`, color: ACC_TEXT,
        fontFamily: SANS, fontWeight: 800, fontSize: 64, letterSpacing: 3, textTransform: 'uppercase', background: CARD,
        padding: '8px 26px', borderRadius: 12, opacity: st, transform: `rotate(-6deg) scale(${1.6 - 0.6 * st})` }}>{p.stamp}</div>
      <div style={box(950, rIn, !hasRight)}>
        <div style={label}>{p.rightLabel}</div>
        {hasRight ? (
          <div style={{ fontFamily: SERIF, fontSize: PSERIF, lineHeight: 1.08, color: INK }}>{firstSentence(p.rightAnswer)}</div>
        ) : (
          <div style={{ fontFamily: SERIF, fontSize: 260, color: GHOST, textAlign: 'center', lineHeight: 1.2 }}>?</div>
        )}
      </div>
      <PFootnote text={p.footnoteShort || p.footnote} o={rIn} />
      <PBug />
    </AbsoluteFill>
  );
};

export const RagPipeline916: React.FC<z.infer<typeof ragPipelineSchema>> = (p) => {
  const t = useT();
  const on = p.stageAt.map((a) => rise(t, a));
  const pull = rise(t, p.stageAt[0] + 0.05, 0.08);
  const slide = rise(t, p.stageAt[1] + 0.02, 0.08);
  const write = cl(interpolate(t, [p.stageAt[2] + 0.02, p.stageAt[2] + 0.18], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));
  const W = PW - 2 * PX, ROW_H = 470, GAP = 110, TOP = PY + 40;
  const rowY = (i: number) => TOP + i * (ROW_H + GAP);
  const GX = PX + 470, chunkW = 420, chunkH = 40;
  const stage = (i: number) => (
    <div key={i} style={{ position: 'absolute', left: PX, top: rowY(i), width: W, height: ROW_H, boxSizing: 'border-box',
      background: CARD, border: `2px solid ${on[i] > 0.5 ? ACC : BORDER}`, borderRadius: 22, padding: '36px 40px',
      opacity: 0.4 + 0.6 * on[i] }}>
      <div style={{ fontFamily: SANS, fontSize: PCAPS, color: SOFT, letterSpacing: 3 }}>{`STEP ${i + 1}`}</div>
      <div style={{ fontFamily: SERIF, fontSize: 104, color: INK, lineHeight: 1.05, marginTop: 10 }}>{p.stages[i].name}</div>
    </div>
  );
  const PICK = [1, 3, 4];
  const stackY = rowY(0) + 60, promptY = rowY(1) + 170;
  const bars = [0, 1, 2, 3, 4, 5].map((k) => {
    const pi = PICK.indexOf(k), picked = pi >= 0;
    const x0 = GX, y0 = stackY + k * (chunkH + 22);
    let x = x0, y = y0;
    if (picked) {
      x = x0 + 30 * pull * (1 - slide);
      y = y0 + (promptY + pi * (chunkH + 20) - y0) * slide;
    }
    return <div key={k} style={{ position: 'absolute', left: x, top: y, width: chunkW, height: chunkH, borderRadius: 8,
      background: picked && pull > 0.3 ? ACC_TEXT : '#E9E6DC', opacity: picked ? 1 : 1 - 0.4 * pull }} />;
  });
  const lines = [0.92, 0.8, 0.88, 0.6];
  return (
    <AbsoluteFill style={{ background: BG }}>
      {[0, 1, 2].map(stage)}
      {[0, 1].map((i) => (
        <div key={i} style={{ position: 'absolute', left: 0, right: 0, top: rowY(i) + ROW_H + 2, textAlign: 'center',
          fontFamily: SANS, fontSize: 92, lineHeight: 1.1, color: on[i + 1] > 0.5 ? ACC_TEXT : GHOST }}>↓</div>
      ))}
      <div style={{ position: 'absolute', left: GX - 20, top: promptY - 110, width: chunkW + 40, height: 3 * (chunkH + 20) + 130,
        border: `3px dashed ${GHOST}`, borderRadius: 12, opacity: on[1] }}>
        <div style={{ fontFamily: MONO, fontSize: PSANS, color: SOFT, padding: '0 16px', lineHeight: 1.3 }}>prompt</div>
      </div>
      {bars}
      {lines.map((w, i) => {
        const fill = cl(write * lines.length - i);
        return (
          <div key={i} style={{ position: 'absolute', left: GX - 20, top: rowY(2) + 50 + i * 96, display: 'flex', alignItems: 'center', gap: 14 }}>
            <div style={{ width: 330 * w * fill, height: 22, borderRadius: 11, background: '#CFCBBE' }} />
            {i < 3 && fill > 0.95 ? (
              <span style={{ fontFamily: SANS, fontSize: 64, fontWeight: 700, color: ACC_TEXT, border: `3px solid ${ACC_TEXT}`, borderRadius: 10, padding: '0 14px', lineHeight: 1.1 }}>{i + 1}</span>
            ) : null}
          </div>
        );
      })}
      <PBug />
    </AbsoluteFill>
  );
};

export const RagEmbeddingMap916: React.FC<z.infer<typeof ragEmbeddingMapSchema>> = (p) => {
  const t = useT();
  const cut = rise(t, p.cutAt, 0.08), fly = rise(t, p.flyAt, 0.12), qIn = rise(t, p.questionAt);
  const MAP = { x: PX, y: PY + 290, w: PW - 2 * PX, h: 1060 };
  const n = (p.chunks916 ?? p.chunks).length, perRow = Math.ceil(n / 3);
  const pieceW = (PW - 2 * PX) / perRow, pieceH = 70;
  // labels need room beside the dot: pull dots into the map's inner band
  const ix = (x: number) => MAP.x + 60 + x * (MAP.w - 120);
  const iy = (y: number) => MAP.y + 150 + y * (MAP.h - 220);
  const chunks = p.chunks916 ?? p.chunks;
  const qpos = p.question916 ?? p.question;
  const qx = ix(qpos.x), qy = iy(qpos.y);
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: PX, right: PX, top: PY + 10, textAlign: 'center', fontFamily: SERIF,
        fontSize: PSERIF, lineHeight: 1.08, color: INK, opacity: rise(t, 0) }}>Close in meaning, close on the map</div>
      <div style={{ position: 'absolute', left: MAP.x, top: MAP.y, width: MAP.w, height: MAP.h, border: `2px solid ${BORDER}`,
        borderRadius: 22, background: CARD, opacity: fly }}>
        <div style={{ position: 'absolute', left: 28, top: 18, fontFamily: SANS, fontSize: PCAPS, color: SOFT, letterSpacing: 3 }}>MEANING MAP</div>
      </div>
      <svg width={PW} height={PH} style={{ position: 'absolute', left: 0, top: 0 }}>
        {p.nearest.map((lab, i) => {
          const c = chunks.find((k) => k.label === lab);
          if (!c) return null;
          const o = rise(t, p.linkAt + i * 0.04);
          const cx = ix(c.x), cy = iy(c.y), hi = lab === p.highlight;
          return <line key={lab} x1={qx} y1={qy} x2={qx + (cx - qx) * o} y2={qy + (cy - qy) * o}
            stroke={hi ? ACC : INK} strokeWidth={hi ? 9 : 6} opacity={hi ? 1 : 0.7} />;
        })}
      </svg>
      {chunks.map((c, i) => {
        const row = Math.floor(i / perRow), col = i % perRow;
        const sx = PX + col * pieceW, sy = MAP.y + 110 + row * (pieceH + 30);
        const mx = ix(c.x), my = iy(c.y);
        const near = p.nearest.includes(c.label);
        const lit = near ? rise(t, p.linkAt + p.nearest.indexOf(c.label) * 0.04 + 0.04) : 0;
        const hi = c.label === p.highlight, gap = 14 * cut;
        const w = (pieceW - gap) * (1 - fly) + 40 * fly, h = pieceH * (1 - fly) + 40 * fly;
        const x = sx + gap / 2 + (mx - 20 - sx - gap / 2) * fly, y = sy + (my - 20 - sy) * fly;
        const leftSide = c.x > 0.5;
        return (
          <React.Fragment key={c.label}>
            <div style={{ position: 'absolute', left: x, top: y, width: w, height: h, borderRadius: 8 + 12 * fly,
              background: hi && lit > 0.5 ? ACC : near && lit > 0.5 ? INK : '#CFCBBE' }} />
            <div style={{ position: 'absolute', top: my - 44, opacity: fly,
              ...(leftSide ? { right: PW - mx + 34 } : { left: mx + 34 }),
              fontFamily: SANS, fontSize: PSANS, lineHeight: 1.2, color: hi && lit > 0.5 ? ACC_TEXT : near && lit > 0.5 ? INK : SOFT,
              fontWeight: lit > 0.5 ? 700 : 400, whiteSpace: 'nowrap' }}>{c.label}</div>
          </React.Fragment>
        );
      })}
      <div style={{ position: 'absolute', left: qx - 30, top: qy - 30, width: 60, height: 60,
        transform: `rotate(45deg) scale(${qIn})`, background: INK }} />
      <div style={{ position: 'absolute', left: PX, right: PX, top: MAP.y + MAP.h + 24, textAlign: 'center',
        fontFamily: SERIF, fontSize: PSERIF, lineHeight: 1.05, fontStyle: 'italic', color: INK, opacity: qIn }}>◆ “{p.question.label}”</div>
      <PFootnote text={p.footnoteShort || p.footnote} o={fly} />
      <PBug />
    </AbsoluteFill>
  );
};

export const RagRetrievalDemo916: React.FC<z.infer<typeof ragRetrievalDemoSchema>> = (p) => {
  const t = useT();
  const max = Math.max(...p.results.map((r) => r.score), 1e-6);
  const W = PW - 2 * PX, aIn = rise(t, p.answerAt);
  const head = (r: { section: string; score: number }, i: number, o: number) => (
    <div style={{ display: 'flex', alignItems: 'center', gap: 18 }}>
      <span style={{ fontFamily: SANS, fontSize: PSANS, fontWeight: 700, color: INK, whiteSpace: 'nowrap' }}>{`#${i + 1} ${r.section}`}</span>
      <div style={{ flex: 1 }} />
      <span style={{ fontFamily: MONO, fontSize: PSANS, color: i === 0 ? ACC_TEXT : SOFT }}>{(r.score * o).toFixed(3)}</span>
    </div>
  );
  const top = p.results[0];
  const o0 = rise(t, p.resultsAt);
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: PX, right: PX, top: PY + 10, fontFamily: MONO, fontSize: PSANS, lineHeight: 1.2,
        color: SOFT, opacity: rise(t, 0.02), whiteSpace: 'nowrap' }}>$ python3 rag_demo.py</div>
      <div style={{ position: 'absolute', left: PX, top: 230, width: W, boxSizing: 'border-box', background: CARD,
        border: `5px solid ${o0 > 0.5 ? ACC_TEXT : BORDER}`, borderRadius: 20, padding: '24px 34px', opacity: o0,
        transform: `translateX(${(1 - o0) * -40}px)` }}>
        {head(top, 0, o0)}
        <div style={{ width: (W - 80) * (top.score / max) * o0, height: 18, borderRadius: 9, background: ACC_TEXT, margin: '14px 0 16px' }} />
        <div style={{ fontFamily: SERIF, fontSize: PSERIF, lineHeight: 1.06, color: INK }}>“{firstSentence(top.text)}”</div>
      </div>
      {p.results.slice(1).map((r, j) => {
        const i = j + 1, o = rise(t, p.resultsAt + i * 0.07) * (1 - aIn);
        return (
          <div key={r.section} style={{ position: 'absolute', left: PX, top: 920 + j * 150, width: W, height: 130, boxSizing: 'border-box',
            background: CARD, border: `2px solid ${BORDER}`, borderRadius: 18, padding: '22px 34px', opacity: o }}>
            {head(r, i, o)}
          </div>
        );
      })}
      <div style={{ position: 'absolute', left: PX, top: 920, width: W, boxSizing: 'border-box', background: CARD,
        border: `2px solid ${BORDER}`, borderRadius: 20, padding: '24px 34px', opacity: aIn, transform: `translateY(${(1 - aIn) * 30}px)` }}>
        <div style={{ fontFamily: SANS, fontSize: PCAPS, letterSpacing: 3, color: SOFT }}>WITH RETRIEVAL</div>
        <div style={{ fontFamily: SERIF, fontSize: PSERIF, lineHeight: 1.06, color: INK, marginTop: 10 }}>{firstSentence(p.answer)}</div>
        <div style={{ fontFamily: SANS, fontSize: PSANS, lineHeight: 1.15, color: ACC_TEXT, marginTop: 16 }}>{top.section}</div>
      </div>
      <PFootnote text={p.footnoteShort || p.footnote} o={rise(t, 0.05)} />
      <PBug />
    </AbsoluteFill>
  );
};

export const RagWhenToUse916: React.FC<z.infer<typeof ragWhenToUseSchema>> = (p) => {
  const t = useT();
  const sec = (top: number, header: string, items: { text: string; at: number }[], mark: string, at: number) => (
    <div style={{ position: 'absolute', left: PX, right: PX, top }}>
      <div style={{ fontFamily: SERIF, fontSize: 100, lineHeight: 1.05, color: INK, opacity: rise(t, at), borderBottom: `3px solid ${INK}`, paddingBottom: 30 }}>{header}</div>
      {items.map((it, i) => {
        const o = rise(t, it.at);
        return (
          <div key={i} style={{ display: 'flex', gap: 20, alignItems: 'baseline', marginTop: 22, opacity: o, transform: `translateY(${(1 - o) * 30}px)` }}>
            <span style={{ fontFamily: SANS, fontSize: 84, fontWeight: 700, color: INK, width: 74, lineHeight: 1 }}>{mark}</span>
            <span style={{ fontFamily: SERIF, fontSize: PSERIF, color: INK, lineHeight: 1.0 }}>{it.text}</span>
          </div>
        );
      })}
    </div>
  );
  const w = rise(t, p.warningAt);
  return (
    <AbsoluteFill style={{ background: BG }}>
      {sec(PY, p.useHeader, p.useItems, '✓', p.useHeaderAt ?? p.useItems[0]?.at ?? 0)}
      {sec(PY + 690, p.skipHeader, p.skipItems, '✕', p.skipHeaderAt ?? p.skipItems[0]?.at ?? 0.5)}
      <div style={{ position: 'absolute', left: PX, right: PX, bottom: PY + 70, background: CARD, border: `5px solid ${ACC}`,
        borderRadius: 20, padding: '24px 34px', textAlign: 'center', fontFamily: SERIF, fontSize: PSERIF, lineHeight: 1.02, color: ACC_TEXT,
        opacity: w, transform: `translateY(${(1 - w) * -60}px)` }}>{p.warning}</div>
      <PBug />
    </AbsoluteFill>
  );
};

export const HaiTitleOutro916: React.FC<z.infer<typeof haiTitleOutroSchema>> = (p) => {
  const t = useT();
  const a = rise(t, 0.0, 0.15), b = rise(t, 0.12, 0.15), c = rise(t, 0.25, 0.15);
  const title = p.title.replace(/[.?!]$/, '');
  return (
    <AbsoluteFill style={{ background: BG, alignItems: 'center', justifyContent: 'center', padding: `0 ${PX}px` }}>
      <Img src={staticFile('logos/humanitarians/humanitarians-logo-1.svg')} style={{ height: 640, opacity: a, marginBottom: 100 }} />
      <div style={{ fontFamily: SERIF, fontSize: 190, color: INK, opacity: b, lineHeight: 1.05, textAlign: 'center' }}>
        {title}<span style={{ color: ACC }}>.</span>
      </div>
      <div style={{ fontFamily: SANS, fontSize: 104, color: SOFT, marginTop: 80, opacity: c }}>{p.handle}</div>
    </AbsoluteFill>
  );
};
