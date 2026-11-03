/**
 * JevExplainer.tsx — reel-local, DUAL-ASPECT Remotion components for
 * claude-hai-system-one-jev ("System One Models and Jev", @HumanitariansAI).
 *
 * Every component reads the frame shape at render time and lays out natively for
 * 16:9 (registered as <Name>, 1920×1080 → 3840×2160 at --scale=2) or 9:16
 * (registered as <Name>916, 1080×1920 → 2160×3840). Nothing is a crop.
 * Motion is a pure function of progress (frame / duration), so each scene
 * conforms to its beat's measured audio via the `durationSeconds` prop.
 * Palette: Claude fidelity — cream, warm ink, ONE terracotta accent.
 * Corner bug: the Humanitarians AI mark (LOGO LAW).
 *
 * Claims on screen come from TypeSafe's launch post + docs (see the reel's SOURCES.md).
 * Decision values and confidences are illustrative toy values, labelled as such.
 *
 *   JevHook        — chat bubbles vs. an automation pipeline with an empty slot
 *   JevSequential  — an LLM string, typed token by token, then parsed
 *   JevParallel    — one state, typed answers filling in parallel, one pass
 *   JevTypeCheck   — free-form value fails a type check; typed value passes
 *   JevLatency     — TypeSafe's reported 70–500 ms band vs. a multi-second LLM call
 *   JevFit         — built for (classify/route/score/extract) vs. not for (chat/coding)
 *   JevConfidence  — calibrated confidences against a threshold: automate vs. escalate
 *   (The outro is the shared default HaiOutro.tsx.)
 */
import React from 'react';
import { AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from './tokens/claude';
import { SAFE, SAFE916 } from './tokens/layout';

export const SERIF = CLAUDE_FONT.serif;
export const SANS = CLAUDE_FONT.ui;
export const MONO = CLAUDE_FONT.mono;
// Accent for TEXT: the darker terracotta passes WCAG 4.5:1 on cream (5.5:1); CLAUDE.SPARK
// (2.96:1) stays for fills, borders, bars and the spark glyph (GATE T §8.3).
export const ACC_TEXT = '#A44A32';
const HAI_LOGO = 'logo-outro/humanitarians/humanitarians-logo-1.svg';

export const ramp = (t: number, a: number, b: number) =>
  interpolate(t, [a, b], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
export const ease = (x: number) => 1 - Math.pow(1 - x, 3);

export type Stage = { t: number; P: boolean; S: { x: number; y: number; w: number; h: number; r: number; b: number } };
export const useStage = (): Stage => {
  const frame = useCurrentFrame();
  const { durationInFrames, width, height } = useVideoConfig();
  const P = height > width;
  return { t: frame / Math.max(1, durationInFrames - 1), P, S: P ? SAFE916 : SAFE };
};

export const durMeta = (fallback: number) =>
  ({ props }: { props: Record<string, unknown> }) =>
    ({ durationInFrames: Math.max(30, Math.ceil(((props.durationSeconds as number) ?? fallback) * 30)) });

export const Bug: React.FC<{ st: Stage }> = ({ st }) => (
  <Img src={staticFile(HAI_LOGO)} style={{
    position: 'absolute', right: (st.P ? 1080 : 1920) - st.S.r, bottom: (st.P ? 1920 : 1080) - st.S.b,
    height: st.P ? 70 : 60, opacity: 0.45,
  }} />
);

export const Title: React.FC<{ st: Stage; text: string }> = ({ st, text }) => {
  const a = ease(ramp(st.t, 0, 0.12));
  return (
    <div style={{
      position: 'absolute', left: st.S.x, top: st.S.y + (st.P ? 60 : 30), width: st.S.w,
      fontFamily: SERIF, fontSize: st.P ? 88 : 80, color: CLAUDE.INK, lineHeight: 1.1,
      opacity: a, transform: `translateY(${(1 - a) * 18}px)`,
    }}>{text}</div>
  );
};

// the one-line spark summary; portrait keeps it above the Shorts UI band (y < 1440)
export const Spark: React.FC<{ st: Stage; text: string; at?: number }> = ({ st, text, at = 0.8 }) => {
  const a = ease(ramp(st.t, at, at + 0.1));
  if (!text) return null;
  return (
    <div style={{
      position: 'absolute', left: st.S.x, width: st.S.w - (st.P ? 0 : 300),
      ...(st.P ? { top: 1330 } : { bottom: 1080 - st.S.b + 6 }),
      display: 'flex', alignItems: 'center', gap: 18, opacity: a,
    }}>
      <span style={{ fontFamily: SERIF, fontSize: 60, color: CLAUDE.SPARK, lineHeight: 1 }}>✻</span>
      <span style={{ fontFamily: SERIF, fontSize: st.P ? 56 : 50, color: CLAUDE.INK, fontStyle: 'italic' }}>{text}</span>
    </div>
  );
};

export const Card: React.FC<{ style?: React.CSSProperties; accent?: boolean; children?: React.ReactNode }> = ({ style, accent, children }) => (
  <div style={{
    position: 'absolute', background: CLAUDE.CARD, borderRadius: 16, boxSizing: 'border-box',
    border: `3px solid ${accent ? CLAUDE.SPARK : CLAUDE.BORDER}`, ...style,
  }}>{children}</div>
);

// ===========================================================================
// JevHook — "most AI talk is chat" (bubbles) vs. the pipeline with an empty slot
// ===========================================================================
export const jevHookSchema = z.object({
  title: z.string().default('Most AI talk is chat.'),
  bubbles: z.array(z.string()).default(['Write me a poem', 'Explain this code', 'Plan my trip']),
  pipeline: z.array(z.string()).default(['ticket', '?', 'queue']),
  sparkLine: z.string().default('Where is the automation?'),
  durationSeconds: z.number().optional(),
});
export const jevHookMeta = durMeta(5);
export const JevHook: React.FC<z.infer<typeof jevHookSchema>> = ({ title, bubbles, pipeline, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const colW = P ? S.w : (S.w - 80) / 2;
  const top = P ? 330 : 280;
  const pipeTop = P ? 830 : top;
  const pipeX = P ? S.x : S.x + colW + 80;
  const slot = ease(ramp(t, 0.5, 0.62));
  const pulse = 0.5 + 0.5 * Math.sin(t * 40);
  const n = pipeline.length;
  const bw = (colW - 50 * (n - 1)) / n;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {bubbles.map((b, i) => {
        const a = ease(ramp(t, 0.08 + i * 0.08, 0.18 + i * 0.08));
        return (
          <Card key={b} style={{
            left: S.x + (i % 2 ? 90 : 0), top: top + i * (P ? 150 : 170), width: colW - 90,
            padding: '26px 34px', opacity: a, transform: `translateY(${(1 - a) * 20}px)`,
            fontFamily: SANS, fontSize: P ? 46 : 44, color: CLAUDE.INK,
          }}>{b}</Card>
        );
      })}
      {pipeline.map((p, i) => {
        const a = ease(ramp(t, 0.36 + i * 0.05, 0.46 + i * 0.05));
        const empty = p === '?';
        return (
          <React.Fragment key={i}>
            <Card accent={empty} style={{
              left: pipeX + i * (bw + 50), top: pipeTop + (P ? 0 : 150), width: bw, height: 200,
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              fontFamily: empty ? SERIF : SANS, fontSize: empty ? 110 : 46,
              color: empty ? ACC_TEXT : CLAUDE.INK, opacity: a * (empty ? 0.55 + 0.45 * (slot * pulse + (1 - slot)) : 1),
              borderStyle: empty ? 'dashed' : 'solid',
            }}>{p}</Card>
            {i < n - 1 && (
              <div style={{
                position: 'absolute', left: pipeX + i * (bw + 50) + bw + 8, top: pipeTop + (P ? 0 : 150) + 97,
                width: 34, height: 6, background: CLAUDE.INK_SOFT, opacity: a,
              }} />
            )}
          </React.Fragment>
        );
      })}
      <div style={{
        position: 'absolute', left: pipeX, top: pipeTop + (P ? 230 : 380), width: colW, textAlign: 'center',
        fontFamily: SANS, fontSize: 40, color: CLAUDE.INK_SOFT, opacity: ease(ramp(t, 0.5, 0.6)),
      }}>inside real software</div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// JevSequential — an LLM string, one token at a time, then it must be parsed
// ===========================================================================
export const jevSequentialSchema = z.object({
  title: z.string().default('An LLM writes a string'),
  tokens: z.array(z.string()).default(['{', '"route"', ':', ' "billing"', ',', ' "urgent"', ':', ' true', ' }']),
  sparkLine: z.string().default('Then your code parses it.'),
  durationSeconds: z.number().optional(),
});
export const jevSequentialMeta = durMeta(5);
export const JevSequential: React.FC<z.infer<typeof jevSequentialSchema>> = ({ title, tokens, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const typeT = ramp(t, 0.08, 0.66);
  const shown = Math.floor(typeT * tokens.length + 1e-4);
  const parseIn = ease(ramp(t, 0.7, 0.8));
  const top = P ? 360 : 290;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top, fontFamily: SANS, fontSize: 40, color: CLAUDE.INK_SOFT }}>
        token {Math.min(shown, tokens.length)} of {tokens.length} · one at a time
      </div>
      <Card style={{
        left: S.x, top: top + 80, width: S.w, minHeight: P ? 420 : 200, padding: P ? '40px 36px' : '0 44px',
        display: 'flex', flexWrap: 'wrap', alignItems: 'center', alignContent: 'center',
        fontFamily: MONO, fontSize: P ? 60 : 62, color: CLAUDE.INK, whiteSpace: 'pre',
      }}>
        {tokens.slice(0, shown).map((tok, i) => (
          <span key={i} style={{ borderBottom: `4px solid ${i === shown - 1 ? CLAUDE.SPARK : CLAUDE.BORDER}`, marginRight: 8, marginBottom: 10 }}>{tok}</span>
        ))}
        {shown < tokens.length && <span style={{ width: 6, height: 66, background: CLAUDE.INK, opacity: Math.floor(t * 40) % 2 ? 1 : 0.2 }} />}
      </Card>
      <div style={{
        position: 'absolute', left: S.x, top: top + (P ? 560 : 330), width: S.w,
        display: 'flex', alignItems: 'center', gap: 28, opacity: parseIn,
        fontFamily: MONO, fontSize: P ? 46 : 50, color: CLAUDE.INK,
      }}>
        <span style={{ color: ACC_TEXT }}>→</span> json.loads(text)
      </div>
      <Spark st={st} text={sparkLine} at={0.82} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// JevParallel — one state; every typed question answered at once, one pass
// ===========================================================================
export const jevParallelSchema = z.object({
  title: z.string().default('Jev answers in parallel'),
  state: z.string().default('"Charged twice this month. Fix it today!"'),
  questions: z.array(z.object({ kind: z.string(), name: z.string(), value: z.string() })).default([
    { kind: 'Choice', name: 'route', value: 'billing' },
    { kind: 'Score', name: 'urgency', value: '0.82' },
    { kind: 'Choice', name: 'language', value: 'en' },
  ]),
  sparkLine: z.string().default('Typed values, one pass.'),
  durationSeconds: z.number().optional(),
});
export const jevParallelMeta = durMeta(5);
export const JevParallel: React.FC<z.infer<typeof jevParallelSchema>> = ({ title, state, questions, sparkLine }) => {
  const st0 = useStage();
  const IN = 16;   // card borders sat exactly on the SAFE edge and read as bleed
  const st = { ...st0, S: { ...st0.S, x: st0.S.x + IN, w: st0.S.w - IN * 2, r: st0.S.r - IN } };
  const { t, P, S } = st;
  const stateIn = ease(ramp(t, 0.06, 0.16));
  const qIn = ease(ramp(t, 0.2, 0.3));
  const fill = ease(ramp(t, 0.5, 0.56));           // all answers land on the SAME frame
  const top = P ? 330 : 260;
  const n = questions.length;
  const qTop = top + (P ? 370 : 200);
  const qW = P ? S.w : (S.w - 40 * (n - 1)) / n;
  const qH = P ? 170 : 250;
  const qGap = P ? 24 : 40;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{
        left: S.x, top, width: S.w, padding: P ? '30px 36px' : '26px 40px', opacity: stateIn,
        // portrait: sans at 70 — at 4K glyphs don't touch, so x-height clusters must clear the 9:16 GATE T floor
        fontFamily: P ? SANS : SERIF, fontSize: P ? 70 : 54, lineHeight: 1.2, color: CLAUDE.INK, background: CLAUDE.FOOTER,
      }}>
        <div style={{ fontFamily: SANS, fontSize: 36, color: CLAUDE.INK_SOFT, fontStyle: 'normal', marginBottom: 8 }}>state</div>
        {state}
      </Card>
      {questions.map((q, i) => (
        <Card key={q.name} accent={fill > 0.5} style={{
          left: S.x + (P ? 0 : i * (qW + 40)), top: qTop + (P ? i * (qH + qGap) : 0), width: qW, height: qH,
          padding: '0 34px', display: 'flex', flexDirection: P ? 'row' : 'column',
          justifyContent: P ? 'space-between' : 'center', alignItems: P ? 'center' : 'flex-start', gap: 10,
          opacity: qIn, transform: `translateY(${(1 - qIn) * 20}px)`,
        }}>
          <div style={{ fontFamily: SANS, fontSize: 40, color: CLAUDE.INK_SOFT }}>{q.kind} · {q.name}</div>
          <div style={{
            fontFamily: MONO, fontSize: P ? 60 : 66, color: ACC_TEXT,
            opacity: fill, transform: `scale(${0.85 + 0.15 * fill})`, transformOrigin: 'left center',
          }}>{q.value}</div>
        </Card>
      ))}
      <div style={{
        position: 'absolute', left: S.x, top: qTop + (P ? n * (qH + qGap) + 10 : qH + 36), width: S.w,
        fontFamily: SANS, fontSize: 38, color: CLAUDE.INK_SOFT, opacity: ease(ramp(t, 0.6, 0.7)),
      }}>illustrative values</div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// JevTypeCheck — a free-form value fails the type check; a typed value can't
// ===========================================================================
export const jevTypeCheckSchema = z.object({
  title: z.string().default('No type errors'),
  field: z.string().default('urgent: bool'),
  llmValue: z.string().default('"urgent": "yes-ish"'),
  jevValue: z.string().default('urgent = true'),
  caveat: z.string().default('Typed is not the same as right.'),
  sparkLine: z.string().default(''),
  durationSeconds: z.number().optional(),
});
export const jevTypeCheckMeta = durMeta(5);
export const JevTypeCheck: React.FC<z.infer<typeof jevTypeCheckSchema>> = ({ title, field, llmValue, jevValue, caveat, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 330 : 280;
  const colW = P ? S.w : (S.w - 60) / 2;
  const colH = P ? 380 : 420;
  const verdict = ease(ramp(t, 0.42, 0.54));
  const cav = ease(ramp(t, 0.68, 0.78));
  const cols = [
    { head: 'LLM · free text', value: llmValue, ok: false },
    { head: 'Jev · typed', value: jevValue, ok: true },
  ];
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top, fontFamily: MONO, fontSize: 44, color: CLAUDE.INK_SOFT }}>schema → {field}</div>
      {cols.map((c, i) => {
        const a = ease(ramp(t, 0.1 + i * 0.1, 0.2 + i * 0.1));
        return (
          <Card key={c.head} accent={c.ok && verdict > 0.5} style={{
            left: S.x + (P ? 0 : i * (colW + 60)), top: top + 90 + (P ? i * (colH + 30) : 0), width: colW, height: colH,
            padding: '34px 40px', opacity: a,
          }}>
            <div style={{ fontFamily: SANS, fontSize: 42, color: CLAUDE.INK_SOFT }}>{c.head}</div>
            <div style={{ fontFamily: MONO, fontSize: P ? 54 : 56, color: CLAUDE.INK, marginTop: 30 }}>{c.value}</div>
            <div style={{
              fontFamily: SANS, fontSize: 52, marginTop: 36, opacity: verdict,
              color: c.ok ? ACC_TEXT : CLAUDE.INK_SOFT,
            }}>{c.ok ? '✓ bool, by construction' : '✕ not a bool'}</div>
          </Card>
        );
      })}
      <div style={{
        position: 'absolute', left: S.x, top: top + 90 + (P ? 2 * (colH + 30) + 10 : colH + 40), width: S.w,
        fontFamily: SERIF, fontSize: P ? 50 : 50, color: CLAUDE.INK, fontStyle: 'italic', opacity: cav,
      }}>{caveat}</div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// JevLatency — TypeSafe's reported 70–500 ms band vs. a multi-second LLM call
// ===========================================================================
export const jevLatencySchema = z.object({
  title: z.string().default('Milliseconds, not seconds'),
  jevLabel: z.string().default('Jev · 70–500 ms'),
  llmLabel: z.string().default('LLM call · often seconds'),
  source: z.string().default('Jev range as reported by TypeSafe'),
  sparkLine: z.string().default(''),
  durationSeconds: z.number().optional(),
});
export const jevLatencyMeta = durMeta(5);
export const JevLatency: React.FC<z.infer<typeof jevLatencySchema>> = ({ title, jevLabel, llmLabel, source, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const axisMs = 3000;
  const top = P ? 420 : 330;
  const W = S.w;
  const x = (ms: number) => S.x + (ms / axisMs) * W;
  const jevIn = ease(ramp(t, 0.12, 0.28));
  const llmGrow = ease(ramp(t, 0.36, 0.72));
  const rowGap = P ? 300 : 230;
  const ticks = P ? [0, 1000, 2000, 3000] : [0, 500, 1000, 2000, 3000];
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {/* Jev: the reported band, 70 → 500 ms */}
      <div style={{ position: 'absolute', left: S.x, top, fontFamily: SANS, fontSize: 46, color: ACC_TEXT }}>{jevLabel}</div>
      <div style={{
        position: 'absolute', left: x(70), top: top + 80, height: 70, borderRadius: 10,
        width: (x(500) - x(70)) * jevIn, background: ACC_TEXT,
      }} />
      {/* LLM: grows past the Jev band, fading out — "seconds", no invented figure */}
      <div style={{ position: 'absolute', left: S.x, top: top + rowGap, fontFamily: SANS, fontSize: 46, color: CLAUDE.INK }}>{llmLabel}</div>
      <div style={{
        position: 'absolute', left: S.x, top: top + rowGap + 80, height: 70, borderRadius: 10,
        width: W * llmGrow, background: `linear-gradient(90deg, ${CLAUDE.INK_SOFT} 60%, rgba(115,112,95,0.25))`,
      }} />
      {/* axis */}
      <div style={{ position: 'absolute', left: S.x, top: top + rowGap + 190, width: W, height: 3, background: CLAUDE.BORDER }} />
      {ticks.map((ms) => (
        <div key={ms} style={{
          position: 'absolute', top: top + rowGap + 206, left: Math.min(x(ms), S.r - 110) - (ms === 0 ? 0 : 20),
          fontFamily: SANS, fontSize: 38, color: CLAUDE.INK_SOFT,
        }}>{ms < 1000 ? `${ms} ms` : `${ms / 1000} s`}</div>
      ))}
      <div style={{
        position: 'absolute', left: S.x, top: top + rowGap + 290, width: S.w,
        fontFamily: SANS, fontSize: 36, color: CLAUDE.INK_SOFT, opacity: ease(ramp(t, 0.3, 0.4)),
      }}>{source}</div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// JevFit — built for high-volume structured jobs; not for chat or coding
// ===========================================================================
export const jevFitSchema = z.object({
  title: z.string().default('Built for pipelines'),
  forLabel: z.string().default('built for'),
  forItems: z.array(z.string()).default(['classify', 'route', 'score', 'extract']),
  notLabel: z.string().default('not for'),
  notItems: z.array(z.string()).default(['open-ended chat', 'coding']),
  sparkLine: z.string().default('High volume, small decisions.'),
  durationSeconds: z.number().optional(),
});
export const jevFitMeta = durMeta(5);
export const JevFit: React.FC<z.infer<typeof jevFitSchema>> = ({ title, forLabel, forItems, notLabel, notItems, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 330 : 280;
  const gap = 30;
  const perRow = P ? 2 : 4;
  const chipW = (S.w - gap * (perRow - 1)) / perRow;
  const chipH = P ? 160 : 170;
  const forRows = Math.ceil(forItems.length / perRow);
  const notTop = top + 80 + forRows * (chipH + gap) + (P ? 60 : 50);
  const notIn = ease(ramp(t, 0.5, 0.62));
  const chip = (label: string, i: number, y0: number, on: boolean, a: number) => (
    <Card key={label} accent={on} style={{
      left: S.x + (i % perRow) * (chipW + gap), top: y0 + Math.floor(i / perRow) * (chipH + gap),
      width: chipW, height: chipH, display: 'flex', alignItems: 'center', justifyContent: 'center',
      background: on ? ACC_TEXT : CLAUDE.CARD, border: `3px solid ${on ? ACC_TEXT : CLAUDE.BORDER}`, fontFamily: SERIF, fontSize: P ? 54 : 56,
      color: on ? CLAUDE.CARD : CLAUDE.INK_SOFT, opacity: a, transform: `translateY(${(1 - a) * 18}px)`,
    }}>{label}</Card>
  );
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top, fontFamily: SANS, fontSize: 42, color: ACC_TEXT }}>✓ {forLabel}</div>
      {forItems.map((f, i) => chip(f, i, top + 80, true, ease(ramp(t, 0.1 + i * 0.06, 0.2 + i * 0.06))))}
      <div style={{ position: 'absolute', left: S.x, top: notTop, fontFamily: SANS, fontSize: 42, color: CLAUDE.INK_SOFT, opacity: notIn }}>✕ {notLabel}</div>
      {notItems.map((f, i) => chip(f, i, notTop + 80, false, notIn * 0.7))}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// JevConfidence — calibrated confidences vs. a threshold: automate or escalate
// ===========================================================================
export const jevConfidenceSchema = z.object({
  title: z.string().default('Every answer has a confidence'),
  rows: z.array(z.object({ label: z.string(), p: z.number() })).default([
    { label: 'billing', p: 0.94 }, { label: 'refund', p: 0.88 }, { label: 'fraud?', p: 0.41 },
  ]),
  threshold: z.number().default(0.8),
  method: z.string().default('trained with RLCD'),
  sparkLine: z.string().default('Automate the sure ones.'),
  durationSeconds: z.number().optional(),
});
export const jevConfidenceMeta = durMeta(5);
export const JevConfidence: React.FC<z.infer<typeof jevConfidenceSchema>> = ({ title, rows, threshold, method, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const top = P ? 440 : 270;   // portrait title wraps to two lines
  const labelW = P ? 260 : 300;
  const tagW = P ? 0 : 330;
  const barX = S.x + labelW;
  const barW = S.w - labelW - tagW - (P ? 0 : 30);
  const rowH = P ? 220 : 140;
  const grow = ease(ramp(t, 0.12, 0.42));
  const lineIn = ease(ramp(t, 0.46, 0.56));
  const tagIn = ease(ramp(t, 0.6, 0.7));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{
        position: 'absolute', left: S.x, top, padding: '8px 22px', borderRadius: 999,
        border: `3px solid ${ACC_TEXT}`, fontFamily: SANS, fontSize: 38, color: ACC_TEXT,
        opacity: ease(ramp(t, 0.06, 0.14)),
      }}>{method}</div>
      {rows.map((r, i) => {
        const y = top + 110 + i * rowH;
        const sure = r.p >= threshold;
        return (
          <React.Fragment key={r.label}>
            <div style={{ position: 'absolute', left: S.x, top: y + 6, width: labelW, fontFamily: MONO, fontSize: 46, color: CLAUDE.INK }}>{r.label}</div>
            <div style={{ position: 'absolute', left: barX, top: y, width: barW, height: 64, background: CLAUDE.FOOTER, borderRadius: 8 }} />
            <div style={{
              position: 'absolute', left: barX, top: y, height: 64, borderRadius: 8,
              width: barW * r.p * grow, background: sure && tagIn > 0.5 ? ACC_TEXT : CLAUDE.GHOST,
            }} />
            <div style={{ position: 'absolute', left: barX + 16, top: y + 8, fontFamily: SANS, fontSize: 40, color: CLAUDE.CARD, opacity: grow }}>
              {Math.round(r.p * grow * 100)}%
            </div>
            <div style={{
              position: 'absolute', opacity: tagIn, fontFamily: SANS, fontSize: 42,
              color: sure ? ACC_TEXT : CLAUDE.INK,
              ...(P ? { left: barX, top: y + 84 } : { left: S.r - tagW, top: y + 6 }),
            }}>{sure ? '→ automate' : '→ ask a human'}</div>
          </React.Fragment>
        );
      })}
      {/* the threshold line */}
      <div style={{
        position: 'absolute', left: barX + barW * threshold - 3, top: top + 90, width: 6,
        height: rows.length * rowH, background: CLAUDE.INK, opacity: lineIn,
      }} />
      <div style={{
        position: 'absolute', left: Math.min(barX + barW * threshold - 70, S.r - 300), top: top + 100 + rows.length * rowH,
        fontFamily: SANS, fontSize: 38, color: CLAUDE.INK, opacity: lineIn,
      }}>threshold {Math.round(threshold * 100)}%</div>
      <div style={{
        position: 'absolute', left: S.x, top: top + 170 + rows.length * rowH, fontFamily: SANS, fontSize: 36,
        color: CLAUDE.INK_SOFT, opacity: lineIn,
      }}>illustrative values</div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
