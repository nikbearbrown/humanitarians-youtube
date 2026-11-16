/**
 * RLHF.tsx — reel-local, DUAL-ASPECT Remotion components for
 * claude-hai-rlhf ("RLHF: How Chatbots Learned to Help", @HumanitariansAI).
 *
 * Same contract as Quantization.tsx (stage helpers from JevExplainer.tsx): each component lays
 * out natively for 16:9 (<Name>) and 9:16 (<Name>916) — never a crop — and every motion is a pure
 * function of progress, conformed via `durationSeconds`. Every number on screen is a default copied
 * from the reel's evidence/rlhf_toy.out.txt (seeded numpy run + echoed paper constants).
 *
 *   RlHook     — "How do I bake bread?" → a raw model continues with more questions (illustrative)
 *   RlPretrain — web text streams into the model: 300B tokens (GPT-3); continues anything, judges nothing
 *   RlSft      — step 1: a person writes the answer, the model learns to imitate it (~13,000 prompts)
 *   RlRank     — step 2: four answers ranked → 6 comparisons → a reward model (toy: 50 → 77.7 %)
 *   RlLoop     — step 3: score → nudge, on a KL leash; the score histogram slides right (toy)
 *   RlScale    — InstructGPT 2022: 1.3B RLHF preferred over 175B GPT-3 (more than 100× smaller)
 *   RlHack     — push harder: learned reward climbs, true substance peaks then falls (toy)
 *   RlNow      — RLHF · DPO · RLAIF (Constitutional AI): all learn from preferences
 */
import React from 'react';
import { AbsoluteFill, Img, staticFile } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from './tokens/claude';
import { SERIF, SANS, MONO, ACC_TEXT, ramp, ease, useStage, durMeta, Bug, Title, Spark, Card } from './JevExplainer';
import type { Stage } from './JevExplainer';

const W = (P: boolean) => (P ? 1080 : 1920);
const H = (P: boolean) => (P ? 1920 : 1080);
const lerp = (a: number, b: number, p: number) => a + (b - a) * p;

// filled pill (GATE T reads outlined pills as overlapping text — always filled)
const Pill: React.FC<{ text: string; size: number; a?: number; accent?: boolean; fill?: string; style?: React.CSSProperties }> = ({ text, size, a = 1, accent, fill, style }) => (
  <span style={{
    display: 'inline-block', padding: `${size * 0.16}px ${size * 0.42}px`, borderRadius: size, boxSizing: 'border-box',
    background: fill ?? (accent ? ACC_TEXT : CLAUDE.INK),
    fontFamily: SANS, fontSize: size, lineHeight: 1.1, color: CLAUDE.CARD, opacity: a, whiteSpace: 'nowrap', ...style,
  }}>{text}</span>
);

const Label: React.FC<{ text: string; size: number; style?: React.CSSProperties; color?: string; serif?: boolean }> = ({ text, size, style, color, serif }) => (
  <div style={{ position: 'absolute', fontFamily: serif ? SERIF : SANS, fontSize: size, lineHeight: 1.15, color: color ?? CLAUDE.INK, ...style }}>{text}</div>
);

const fmtInt = (n: number) => Math.round(n).toLocaleString('en-US');

// the three-step tracker shared by B04–B06 (the lit step is the accent)
const Steps: React.FC<{ st: Stage; on: number }> = ({ st, on }) => {
  const { t, P, S } = st;
  const names = ['1 · imitate', '2 · rank', '3 · reinforce'];
  return (
    <div style={{ position: 'absolute', left: S.x, top: P ? 300 : 196, display: 'flex', gap: P ? 14 : 18, opacity: ease(ramp(t, 0.02, 0.08)) }}>
      {names.map((n, i) => <Pill key={n} text={n} size={P ? 44 : 40} accent={i === on} fill={i === on ? undefined : CLAUDE.INK_SOFT} a={i === on ? 1 : 0.85} />)}
    </div>
  );
};

// ===========================================================================
// RlHook — a raw model asked how to bake bread continues with more questions
// ===========================================================================
export const rlHookSchema = z.object({
  title: z.string().default('Ask a raw model'),
  prompt: z.string().default('How do I bake bread?'),
  continuation: z.array(z.string()).default(['How do I make pizza dough?', 'How long should dough rise?', 'Why is my loaf so dense?']),
  wanted: z.array(z.string()).default(['Mix flour, water, yeast and salt.', 'Knead, then let it rise.', 'Bake until golden.']),
  rawLabel: z.string().default('raw model: predicts the next word'),
  wantLabel: z.string().default('what we wanted'),
  note: z.string().default('illustrative: the raw model continues the pattern of a question list'),
  sparkLine: z.string().default("Predicts, doesn't help."),
  durationSeconds: z.number().optional(),
});
export const rlHookMeta = durMeta(5);
export const RlHook: React.FC<z.infer<typeof rlHookSchema>> = ({ title, prompt, continuation, wanted, rawLabel, wantLabel, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const pIn = ease(ramp(t, 0.03, 0.1));
  const line = (i: number) => ease(ramp(t, 0.16 + i * 0.12, 0.24 + i * 0.12));
  const wIn = ease(ramp(t, 0.58, 0.68));
  const colW = P ? S.w : (S.w - 60) / 2;
  const rawX = S.x, rawY = P ? 430 : 360;
  const rawH = P ? 360 : 500;
  const wX = P ? S.x : S.x + colW + 60, wY = P ? rawY + rawH + 90 : rawY;
  const wH = P ? 300 : 500;
  const fs = P ? 50 : 46;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {/* the prompt, as a user bubble */}
      <div style={{ position: 'absolute', left: S.x, top: P ? 290 : 200, opacity: pIn, transform: `translateY(${(1 - pIn) * 14}px)` }}>
        <span style={{ display: 'inline-block', background: CLAUDE.INK, borderRadius: 24, padding: P ? '20px 34px' : '18px 32px', fontFamily: SERIF, fontSize: P ? 66 : 62, color: CLAUDE.CARD }}>{prompt}</span>
      </div>
      <Card style={{ left: rawX, top: rawY, width: colW, height: rawH, padding: P ? '84px 36px 0' : '90px 40px 0', opacity: pIn }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: P ? 26 : 50 }}>
          {continuation.map((c, i) => (
            <div key={c} style={{ fontFamily: MONO, fontSize: fs, color: CLAUDE.INK, opacity: line(i), lineHeight: 1.15 }}>{c}</div>
          ))}
        </div>
      </Card>
      <div style={{ position: 'absolute', left: rawX + 30, top: rawY - 30, opacity: pIn }}><Pill text={rawLabel} size={P ? 42 : 38} /></div>
      <Card style={{ left: wX, top: wY, width: colW, height: wH, padding: P ? '80px 36px 0' : '90px 40px 0', opacity: wIn }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: P ? 22 : 50 }}>
          {wanted.map((c, i) => (
            <div key={c} style={{ display: 'flex', gap: 18, fontFamily: SERIF, fontSize: P ? 50 : 56, color: CLAUDE.INK, lineHeight: 1.15 }}>
              <span style={{ color: ACC_TEXT }}>{i + 1}</span><span>{c}</span>
            </div>
          ))}
        </div>
      </Card>
      <div style={{ position: 'absolute', left: wX + 30, top: wY - 30, opacity: wIn }}><Pill text={wantLabel} size={P ? 42 : 38} accent /></div>
      <Label text={note} size={P ? 38 : 34} color={CLAUDE.INK_SOFT}
        style={{ left: S.x, top: P ? wY + wH + 24 : rawY + rawH + 24, width: S.w, opacity: ease(ramp(t, 0.4, 0.5)) }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RlPretrain — web text streams in; 300B tokens; continues anything, judges nothing
// ===========================================================================
export const rlPretrainSchema = z.object({
  title: z.string().default('Pretraining'),
  snippets: z.array(z.string()).default(['…preheat the oven and', 'Q: What is the capital of', 'def add(a, b): return', 'Re: my sourdough won’t rise', 'Chapter 1. It was a cold', '10 quiz questions about']),
  tokens: z.number().default(300e9),
  tokensNote: z.string().default('tokens of text read by GPT-3 (2020)'),
  model: z.string().default('language model'),
  can: z.string().default('continue any text'),
  cannot: z.string().default('know a good answer'),
  sparkLine: z.string().default('Fluent, not helpful.'),
  durationSeconds: z.number().optional(),
});
export const rlPretrainMeta = durMeta(5);
export const RlPretrain: React.FC<z.infer<typeof rlPretrainSchema>> = ({ title, snippets, tokens, tokensNote, model, can, cannot, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const cnt = ease(ramp(t, 0.06, 0.4));
  const canIn = ease(ramp(t, 0.5, 0.58));
  const noIn = ease(ramp(t, 0.62, 0.7));
  const strike = ease(ramp(t, 0.7, 0.78));
  // counter
  const cY = P ? 290 : 196;
  // stream column + model box
  const sx = S.x, sy = P ? 520 : 330, sw = P ? S.w : 700;
  const rows = P ? 3 : 5;
  const rowH = P ? 80 : 92;
  const mx = P ? S.x : S.x + sw + 90, my = P ? sy + rows * rowH + 40 : sy;
  const mw = P ? S.w : S.r - (S.x + sw + 90), mh = P ? 150 : 220;
  // results
  const rx = P ? S.x : mx, ry = P ? my + mh + 60 : my + mh + 60;
  const rw = P ? S.w : S.r - rx;
  const flow = t * 2.2; // snippets drift toward the model
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top: cY, display: 'flex', flexDirection: P ? 'column' : 'row', alignItems: P ? 'flex-start' : 'baseline', gap: P ? 4 : 26, opacity: ease(ramp(t, 0.03, 0.09)) }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 104 : 100, lineHeight: 1, color: CLAUDE.INK }}>{fmtInt(tokens * cnt)}</span>
        <span style={{ fontFamily: SANS, fontSize: P ? 46 : 44, color: CLAUDE.INK }}>{tokensNote}</span>
      </div>
      {/* the stream: rows of text cards sliding toward the model */}
      <div style={{ position: 'absolute', left: sx, top: sy, width: sw, height: rows * rowH, overflow: 'hidden' }}>
        {Array.from({ length: rows }, (_, r) => {
          const s = snippets[(r * 2 + Math.floor(flow + r * 0.5)) % snippets.length];
          const off = ((flow + r * 0.5) % 1);
          const a = ease(ramp(t, 0.02 + r * 0.03, 0.08 + r * 0.03));
          return (
            <div key={r} style={{ position: 'absolute', top: r * rowH, left: P ? 0 : lerp(0, 50, off), opacity: a * (P ? 1 : lerp(1, 0.35, off)),
              background: CLAUDE.CARD, border: `3px solid ${CLAUDE.BORDER}`, borderRadius: 14, padding: P ? '10px 22px' : '12px 24px', boxSizing: 'border-box',
              fontFamily: MONO, fontSize: P ? 40 : 36, color: CLAUDE.INK, whiteSpace: 'nowrap', transform: P ? `translateY(${lerp(0, 18, off)}px)` : undefined }}>{s}</div>
          );
        })}
      </div>
      {!P && (
        <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0 }}>
          <line x1={sx + sw + 8} y1={my + mh / 2} x2={mx - 14} y2={my + mh / 2} stroke={CLAUDE.INK} strokeWidth={5} opacity={ease(ramp(t, 0.1, 0.16))} />
          <polygon points={`${mx - 10},${my + mh / 2} ${mx - 30},${my + mh / 2 - 12} ${mx - 30},${my + mh / 2 + 12}`} fill={CLAUDE.INK} opacity={ease(ramp(t, 0.1, 0.16))} />
        </svg>
      )}
      <div style={{ position: 'absolute', left: mx, top: my, width: mw, height: mh, borderRadius: 20, background: CLAUDE.INK, display: 'flex', alignItems: 'center', justifyContent: 'center',
        opacity: ease(ramp(t, 0.08, 0.14)) }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 64 : 60, color: CLAUDE.PAGE, textAlign: 'center', lineHeight: 1.1 }}>{model}</span>
      </div>
      <div style={{ position: 'absolute', left: rx, top: ry, width: rw, display: 'flex', flexDirection: 'column', gap: P ? 26 : 40 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 20, opacity: canIn }}>
          <span style={{ fontFamily: SANS, fontSize: P ? 64 : 64, color: CLAUDE.INK, lineHeight: 1 }}>✓</span>
          <Pill text={can} size={P ? 50 : 54} />
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 20, opacity: noIn }}>
          <span style={{ fontFamily: SANS, fontSize: P ? 64 : 64, color: ACC_TEXT, lineHeight: 1 }}>✗</span>
          <span style={{ position: 'relative', display: 'inline-block' }}>
            {/* strike line drawn BEHIND the pill's text layer (GATE T) */}
            <span style={{ position: 'absolute', left: -8, right: -8, top: '50%', height: 6, marginTop: -3, background: CLAUDE.INK, transform: `scaleX(${strike})`, transformOrigin: 'left', zIndex: 0 }} />
            <Pill text={cannot} size={P ? 50 : 54} accent style={{ position: 'relative', zIndex: 1 }} />
          </span>
        </div>
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RlSft — step 1: a person writes the answer; the model learns to imitate it
// ===========================================================================
export const rlSftSchema = z.object({
  title: z.string().default('Step one: show it'),
  prompt: z.string().default('How do I bake bread?'),
  answer: z.string().default('Mix flour, water, yeast and salt. Knead, let it rise, then bake until golden.'),
  humanLabel: z.string().default('written by a person'),
  modelLabel: z.string().default('the model, trained to imitate'),
  count: z.number().default(13000),
  countNote: z.string().default('example prompts (InstructGPT, about)'),
  sparkLine: z.string().default('Imitate the examples.'),
  durationSeconds: z.number().optional(),
});
export const rlSftMeta = durMeta(4.5);
export const RlSft: React.FC<z.infer<typeof rlSftSchema>> = ({ title, prompt, answer, humanLabel, modelLabel, count, countNote, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const hIn = ease(ramp(t, 0.1, 0.2));
  const words = answer.split(' ');
  const typed = ramp(t, 0.32, 0.7) * words.length;
  const cIn = ease(ramp(t, 0.7, 0.8));
  const colW = P ? S.w : (S.w - 120) / 2;
  const top = P ? 420 : 420;
  const ch = P ? 300 : 360;
  const hx = S.x, mx = P ? S.x : S.x + colW + 120, my = P ? top + ch + 90 : top;
  const fs = P ? 48 : 48;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Steps st={st} on={0} />
      {!P && <Label text={`“${prompt}”`} size={52} serif style={{ left: S.x, top: 280, opacity: hIn }} />}
      <Card style={{ left: hx, top, width: colW, height: ch, padding: P ? '70px 34px 0' : '80px 40px 0', opacity: hIn, fontFamily: SERIF, fontSize: fs, lineHeight: 1.3, background: CLAUDE.INK, border: 'none', color: CLAUDE.CARD }}>
        {answer}
      </Card>
      <div style={{ position: 'absolute', left: hx + 30, top: top - 30, opacity: hIn }}><Pill text={humanLabel} size={42} fill={CLAUDE.INK_SOFT} /></div>
      {!P && (
        <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0 }}>
          <line x1={hx + colW + 18} y1={top + ch / 2} x2={mx - 30} y2={top + ch / 2} stroke={ACC_TEXT} strokeWidth={6} opacity={ease(ramp(t, 0.24, 0.3))} />
          <polygon points={`${mx - 16},${top + ch / 2} ${mx - 38},${top + ch / 2 - 14} ${mx - 38},${top + ch / 2 + 14}`} fill={ACC_TEXT} opacity={ease(ramp(t, 0.24, 0.3))} />
        </svg>
      )}
      <Card style={{ left: mx, top: my, width: colW, height: ch, padding: P ? '70px 34px 0' : '80px 40px 0', opacity: ease(ramp(t, 0.24, 0.32)), fontFamily: SERIF, fontSize: fs, lineHeight: 1.3, background: ACC_TEXT, border: 'none', color: CLAUDE.CARD }}>
        {words.map((w, i) => (
          <span key={i} style={{ opacity: i < Math.floor(typed) ? 1 : i < typed ? typed - i : 0 }}>{w} </span>
        ))}
      </Card>
      <div style={{ position: 'absolute', left: mx + 30, top: my - 30, opacity: ease(ramp(t, 0.24, 0.32)) }}><Pill text={modelLabel} size={42} /></div>
      <div style={{ position: 'absolute', left: S.x, top: P ? my + ch + 50 : top + ch + 60, display: 'flex', alignItems: 'baseline', gap: 22, flexWrap: 'wrap', width: S.w, opacity: cIn }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 92 : 88, lineHeight: 1, color: ACC_TEXT }}>~{fmtInt(count * cIn)}</span>
        <span style={{ fontFamily: SANS, fontSize: P ? 44 : 44, color: CLAUDE.INK }}>{countNote}</span>
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RlRank — step 2: four answers ranked → 6 comparisons → a reward model
// ===========================================================================
export const rlRankSchema = z.object({
  title: z.string().default('Step two: rank them'),
  answers: z.array(z.object({ id: z.string(), text: z.string() })).default([
    { id: 'A', text: 'Mix, knead, rise, bake.' },
    { id: 'B', text: 'Try a local bakery.' },
    { id: 'C', text: 'How do I make pizza?' },
    { id: 'D', text: 'Bread is a staple food…' },
  ]),
  order: z.array(z.number()).default([0, 3, 1, 2]), // best → worst
  pairsLabel: z.string().default('4 answers → 6 comparisons'),
  curve: z.array(z.array(z.number())).default([[0, 50.0], [5, 77.4], [10, 77.6], [20, 77.8], [40, 77.7], [80, 77.7], [120, 77.7], [200, 77.7]]),
  acc: z.number().default(77.7),
  rmLabel: z.string().default('reward model: agrees with held-out rankings'),
  note: z.string().default('toy: 3,000 ranked sets of 4 · Bradley–Terry model'),
  sparkLine: z.string().default('Learn the taste.'),
  durationSeconds: z.number().optional(),
});
export const rlRankMeta = durMeta(5);
export const RlRank: React.FC<z.infer<typeof rlRankSchema>> = ({ title, answers, order, pairsLabel, curve, acc, rmLabel, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const sort = ease(ramp(t, 0.2, 0.36));
  const pIn = (i: number) => ease(ramp(t, 0.4 + i * 0.03, 0.46 + i * 0.03));
  const cIn = ease(ramp(t, 0.58, 0.8));
  // answer cards
  const cx = S.x, cy = P ? 390 : 300, cw = P ? S.w : 720, chh = P ? 80 : 96, cg = P ? 12 : 20;
  const rankOf = (i: number) => order.indexOf(i);
  // pairs (from the ranking: every better-over-worse pair)
  const pairs: string[] = [];
  for (let a = 0; a < order.length; a++) for (let b = a + 1; b < order.length; b++) pairs.push(`${answers[order[a]].id} > ${answers[order[b]].id}`);
  const px = P ? S.x : cx + cw + 70, py = P ? cy + 4 * (chh + cg) + 30 : 300, pw = P ? S.w : S.r - px;
  // curve panel
  const gx = px, gy = P ? py + 280 : py + 290, gw = pw, gh = P ? 180 : 270;
  const maxStep = curve[curve.length - 1][0];
  const GX = (s: number) => gx + 10 + (Math.sqrt(s) / Math.sqrt(maxStep)) * (gw - 260);
  const GY = (v: number) => gy + gh - 20 - ((v - 40) / 50) * (gh - 70);
  const shown = cIn * (curve.length - 1);
  const pts = curve.filter((_, i) => i <= shown).map(([s, v]) => `${GX(s)},${GY(v)}`);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Steps st={st} on={1} />
      {answers.map((a, i) => {
        const y0 = cy + i * (chh + cg), y1 = cy + rankOf(i) * (chh + cg);
        const appear = ease(ramp(t, 0.04 + i * 0.03, 0.1 + i * 0.03));
        const best = rankOf(i) === 0 && sort > 0.9;
        return (
          <Card key={a.id} style={{ border: `3px solid ${best ? ACC_TEXT : CLAUDE.BORDER}`, left: cx, top: lerp(y0, y1, sort), width: cw, height: chh, opacity: appear, display: 'flex', alignItems: 'center', gap: 22, padding: '0 24px' }}>
            <span style={{ fontFamily: SERIF, fontSize: P ? 54 : 52, color: ACC_TEXT, width: 46, opacity: sort }}>{rankOf(i) + 1}</span>
            <Pill text={a.id} size={P ? 40 : 38} />
            <span style={{ fontFamily: SANS, fontSize: P ? 42 : 40, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>{a.text}</span>
          </Card>
        );
      })}
      <div style={{ position: 'absolute', left: px, top: py, width: pw, opacity: pIn(0) }}>
        <Pill text={pairsLabel} size={P ? 46 : 42} accent />
      </div>
      <div style={{ position: 'absolute', left: px, top: py + (P ? 86 : 84), width: pw, display: 'flex', flexWrap: 'wrap', gap: P ? 12 : 16 }}>
        {pairs.map((p, i) => <Pill key={p} text={p} size={P ? 36 : 40} a={pIn(i + 1)} style={{ fontFamily: MONO }} />)}
      </div>
      {/* the reward model's learning curve */}
      <Label text={rmLabel} size={P ? 40 : 38} style={{ left: gx, top: gy - (P ? 50 : 52), width: gw, opacity: ease(ramp(t, 0.56, 0.62)) }} />
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0 }}>
        <line x1={gx + 10} y1={gy + gh - 20} x2={gx + gw - 240} y2={gy + gh - 20} stroke={CLAUDE.INK} strokeWidth={4} opacity={ease(ramp(t, 0.56, 0.62))} />
        <line x1={gx + 10} y1={GY(50)} x2={gx + gw - 240} y2={GY(50)} stroke={CLAUDE.INK_SOFT} strokeWidth={3} strokeDasharray="10 10" opacity={ease(ramp(t, 0.56, 0.62))} />
        {pts.length > 1 && <polyline points={pts.join(' ')} fill="none" stroke={ACC_TEXT} strokeWidth={7} strokeLinejoin="round" />}
      </svg>
      <Label text="coin flip 50 %" size={P ? 34 : 32} color={CLAUDE.INK_SOFT} style={{ left: gx + 24, top: GY(50) + 8, opacity: ease(ramp(t, 0.56, 0.62)) }} />
      <span style={{ position: 'absolute', left: gx + gw - 220, top: GY(acc) - (P ? 46 : 44), fontFamily: SERIF, fontSize: P ? 84 : 80, lineHeight: 1, color: ACC_TEXT, opacity: cIn > 0 ? 1 : 0 }}>
        {lerp(50, acc, cIn).toFixed(1)}%
      </span>
      <Label text={note} size={P ? 34 : 32} color={CLAUDE.INK_SOFT} style={{ left: gx, top: gy + gh + 4, width: gw, opacity: ease(ramp(t, 0.62, 0.7)) }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RlLoop — step 3: score → nudge, on a leash; the score histogram slides right
// ===========================================================================
export const rlLoopSchema = z.object({
  title: z.string().default('Step three: reinforce'),
  edges: z.array(z.number()).default([-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]),
  before: z.array(z.number()).default([1.6, 6.0, 15.5, 25.3, 26.0, 16.2, 6.7, 1.9, 0.3, 0.0, 0.0, 0.0]),
  after: z.array(z.number()).default([0.0, 0.2, 1.2, 5.1, 13.8, 22.5, 24.5, 18.4, 8.3, 4.5, 1.5, 0.0]),
  r0: z.number().default(0.05),
  r1: z.number().default(2.34),
  kl: z.number().default(1.18),
  note: z.string().default('toy: 20,000 answers, scored by the toy reward model'),
  sparkLine: z.string().default('Nudged, on a leash.'),
  durationSeconds: z.number().optional(),
});
export const rlLoopMeta = durMeta(5);
export const RlLoop: React.FC<z.infer<typeof rlLoopSchema>> = ({ title, edges, before, after, r0, r1, kl, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const n = (i: number) => ease(ramp(t, 0.04 + i * 0.05, 0.1 + i * 0.05));
  const shift = ease(ramp(t, 0.36, 0.6));
  const leash = ease(ramp(t, 0.6, 0.7));
  // loop diagram
  const dx = S.x, dy = P ? 410 : 300, dw = P ? S.w : 760;
  const nodeH = P ? 96 : 100;
  const nodes = ['assistant', 'reward model'];
  const nW = P ? 400 : 330;
  const n2x = dx + dw - nW;
  // histogram
  const hx = P ? S.x : S.x + dw + 100, hy = P ? dy + 420 : 300, hw = P ? S.w : S.r - hx, hh = P ? 360 : 460;
  const maxV = 30;
  const bw = hw / before.length;
  const H_ = (v: number) => (v / maxV) * (hh - 40);
  const meanX = (r: number) => hx + ((r - edges[0]) / (edges[edges.length - 1] - edges[0])) * hw;
  const mNow = lerp(r0, r1, shift);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Steps st={st} on={2} />
      {nodes.map((nm, i) => (
        <div key={nm} style={{ position: 'absolute', left: i ? n2x : dx, top: dy, width: nW, height: nodeH, borderRadius: 18, background: i ? CLAUDE.INK_SOFT : CLAUDE.INK,
          display: 'flex', alignItems: 'center', justifyContent: 'center', opacity: n(i * 2) }}>
          <span style={{ fontFamily: SERIF, fontSize: P ? 54 : 50, color: CLAUDE.PAGE }}>{nm}</span>
        </div>
      ))}
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0 }}>
        {/* answer → (top arrow), score → nudge (return arrow underneath) */}
        <line x1={dx + nW + 14} y1={dy + nodeH * 0.5} x2={n2x - 30} y2={dy + nodeH * 0.5} stroke={CLAUDE.INK} strokeWidth={5} opacity={n(1)} />
        <polygon points={`${n2x - 14},${dy + nodeH * 0.5} ${n2x - 40},${dy + nodeH * 0.5 - 21} ${n2x - 40},${dy + nodeH * 0.5 + 21}`} fill={CLAUDE.INK} opacity={n(1)} />
        <path d={`M ${n2x + nW / 2} ${dy + nodeH + 12} L ${n2x + nW / 2} ${dy + nodeH + (P ? 120 : 130)} L ${dx + nW / 2} ${dy + nodeH + (P ? 120 : 130)} L ${dx + nW / 2} ${dy + nodeH + 30}`}
          fill="none" stroke={ACC_TEXT} strokeWidth={6} opacity={n(3)} />
        <polygon points={`${dx + nW / 2},${dy + nodeH + 14} ${dx + nW / 2 - 14},${dy + nodeH + 38} ${dx + nW / 2 + 14},${dy + nodeH + 38}`} fill={ACC_TEXT} opacity={n(3)} />
      </svg>
      <Label text="reply" size={P ? 40 : 38} style={{ left: dx + nW + 30, width: n2x - dx - nW - 60, textAlign: 'center', top: dy - (P ? 52 : 52), opacity: n(1) }} />
      <div style={{ position: 'absolute', left: dx + nW / 2 + 30, top: dy + nodeH + (P ? 140 : 150), opacity: n(3) }}>
        <Pill text="score → nudge toward higher" size={P ? 42 : 38} accent />
      </div>
      <div style={{ position: 'absolute', left: dx, top: dy + nodeH + (P ? 230 : 250), width: dw, opacity: leash }}>
        <Pill text={`drift penalty: stays close (KL ${kl.toFixed(2)})`} size={P ? 42 : 38} />
      </div>
      {/* score histogram: the old one stays as a ghost */}
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0 }}>
        {before.map((v, i) => {
          const hNow = H_(lerp(v, after[i], shift));
          const hOld = H_(v);
          return (
            <g key={i}>
              <rect x={hx + i * bw + 4} y={hy + hh - hOld} width={bw - 8} height={hOld} rx={5} fill={CLAUDE.BORDER} opacity={leash > 0 ? 1 : 0} />
              <rect x={hx + i * bw + 10} y={hy + hh - hNow} width={bw - 20} height={hNow} rx={5} fill={CLAUDE.INK} opacity={n(4)} />
            </g>
          );
        })}
        <line x1={hx} y1={hy + hh} x2={hx + hw} y2={hy + hh} stroke={CLAUDE.INK} strokeWidth={4} opacity={n(4)} />
        <line x1={meanX(mNow)} y1={hy + 20} x2={meanX(mNow)} y2={hy + hh} stroke={ACC_TEXT} strokeWidth={6} opacity={n(4)} />
      </svg>
      <Label text="reward-model score →" size={P ? 38 : 36} color={CLAUDE.INK_SOFT} style={{ left: hx, top: hy + hh + 12, opacity: n(4) }} />
      <div style={{ position: 'absolute', left: Math.min(meanX(mNow) + 16, hx + hw - (P ? 380 : 360)), top: hy - (P ? 30 : 30), opacity: n(4) }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 60 : 56, color: ACC_TEXT, whiteSpace: 'nowrap' }}>mean {mNow >= 0 ? '+' : ''}{mNow.toFixed(2)}</span>
      </div>
      <Label text={note} size={P ? 34 : 32} color={CLAUDE.INK_SOFT} style={{ left: hx, top: hy + hh + (P ? 60 : 58), width: hw, opacity: ease(ramp(t, 0.5, 0.58)) }} />
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RlScale — InstructGPT 2022: the 1.3B RLHF model preferred over 175B GPT-3
// ===========================================================================
export const rlScaleSchema = z.object({
  title: z.string().default('Smaller, and preferred'),
  source: z.string().default('InstructGPT · Ouyang et al., OpenAI, 2022'),
  bigLabel: z.string().default('GPT-3 · 175B parameters'),
  smallLabel: z.string().default('InstructGPT with RLHF · 1.3B'),
  big: z.number().default(175),
  small: z.number().default(1.3),
  ratio: z.number().default(134.6),
  preferred: z.string().default('people preferred its answers'),
  sparkLine: z.string().default('Smaller, but preferred.'),
  durationSeconds: z.number().optional(),
});
export const rlScaleMeta = durMeta(7);
export const RlScale: React.FC<z.infer<typeof rlScaleSchema>> = ({ title, source, bigLabel, smallLabel, big, small, ratio, preferred, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const lIn = ease(ramp(t, 0.03, 0.1));
  const b1 = ease(ramp(t, 0.14, 0.32));
  const b2 = ease(ramp(t, 0.34, 0.42));
  const pr = ease(ramp(t, 0.46, 0.54));
  const rIn = ease(ramp(t, 0.6, 0.7));
  const barH = P ? 120 : 110;
  const y1 = P ? 600 : 420, y2 = P ? 900 : 650;
  const logo = P ? 120 : 110;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top: P ? 300 : 200, display: 'flex', alignItems: 'center', gap: 28, opacity: lIn, width: S.w }}>
        <Img src={staticFile('logos/openai/openai-01.svg')} style={{ width: logo, height: logo }} />
        <span style={{ fontFamily: SANS, fontSize: P ? 44 : 46, color: CLAUDE.INK, lineHeight: 1.2 }}>{source}</span>
      </div>
      <Label text={bigLabel} size={P ? 52 : 50} style={{ left: S.x, top: y1 - (P ? 74 : 70), opacity: b1 > 0 ? 1 : 0 }} />
      <div style={{ position: 'absolute', left: S.x, top: y1, width: S.w * b1, height: barH, borderRadius: 14, background: CLAUDE.INK_SOFT }} />
      <Label text={smallLabel} size={P ? 52 : 50} style={{ left: S.x, top: y2 - (P ? 74 : 70), opacity: b2 > 0 ? 1 : 0 }} />
      <div style={{ position: 'absolute', left: S.x, top: y2, width: Math.max(16, S.w * (small / big)) * b2, height: barH, borderRadius: 6, background: ACC_TEXT }} />
      <div style={{ position: 'absolute', left: S.x + 60, top: y2 + (barH - (P ? 76 : 70)) / 2, opacity: pr, transform: `translateX(${(1 - pr) * 30}px)` }}>
        <Pill text={`← ${preferred}`} size={P ? 50 : 48} accent />
      </div>
      <div style={{ position: 'absolute', left: S.x, top: y2 + barH + (P ? 70 : 60), width: S.w, display: 'flex', flexDirection: P ? 'column' : 'row', alignItems: P ? 'flex-start' : 'baseline', gap: P ? 8 : 34, opacity: rIn }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 76 : 72, color: CLAUDE.INK, lineHeight: 1.1 }}>{big} ÷ {small} ≈ {Math.round(ratio)}</span>
        <span style={{ fontFamily: SERIF, fontSize: P ? 76 : 72, color: ACC_TEXT, lineHeight: 1.1 }}>more than 100× smaller</span>
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RlHack — push harder: learned reward climbs, true substance peaks then falls
// ===========================================================================
export const rlHackSchema = z.object({
  title: z.string().default('Pleasing the judge'),
  sweep: z.array(z.array(z.number())).default([
    [0.0, 0.05, -0.14], [0.07, 0.59, 0.06], [0.27, 1.14, 0.23], [0.5, 1.52, 0.32], [0.8, 1.92, 0.38], [1.18, 2.34, 0.41], [1.94, 3.01, 0.38],
    [3.56, 4.13, 0.11], [4.88, 4.85, -0.2], [6.31, 5.5, -0.59], [7.39, 5.88, -0.92], [8.05, 6.05, -1.13], [8.81, 6.16, -1.3], [9.19, 6.19, -1.32],
  ]),
  peakKL: z.number().default(1.18),
  pleaser0: z.number().default(6.3),
  pleaser1: z.number().default(99.9),
  rewardLabel: z.string().default('reward-model score'),
  truthLabel: z.string().default('actual substance'),
  xLabel: z.string().default('push harder: drift from the original (KL) →'),
  chips: z.array(z.string()).default(['agrees with you', 'sounds sure']),
  note: z.string().default('toy: raters reward agreement as well as substance'),
  sparkLine: z.string().default("Pleasing isn't right."),
  durationSeconds: z.number().optional(),
});
export const rlHackMeta = durMeta(5.5);
export const RlHack: React.FC<z.infer<typeof rlHackSchema>> = ({ title, sweep, peakKL, pleaser0, pleaser1, rewardLabel, truthLabel, xLabel, chips, note, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const ax = ease(ramp(t, 0.03, 0.1));
  const d1 = ease(ramp(t, 0.12, 0.42));
  const d2 = ease(ramp(t, 0.3, 0.6));
  const pk = ease(ramp(t, 0.4, 0.48));
  const plz = ease(ramp(t, 0.56, 0.68));
  const chip = (i: number) => ease(ramp(t, 0.66 + i * 0.05, 0.72 + i * 0.05));
  const cx = S.x + 10, cw = P ? S.w - 20 : 1060;
  const top1 = P ? 330 : 210, chH = P ? 250 : 300, gap = P ? 80 : 80;
  const top2 = top1 + chH + gap;
  const kMax = sweep[sweep.length - 1][0];
  const X = (k: number) => cx + (k / kMax) * cw;
  const Y1 = (r: number) => top1 + chH - (r / 6.5) * chH;
  const Y2 = (s: number) => top2 + chH / 2 - (s / 1.5) * (chH / 2);
  const partial = (col: number, Y: (v: number) => number, d: number) => {
    const xs = sweep.map((p) => p[0]); const lim = d * kMax;
    const pts: string[] = [];
    for (let i = 0; i < sweep.length; i++) {
      if (xs[i] <= lim) pts.push(`${X(xs[i])},${Y(sweep[i][col])}`);
      else if (i > 0 && xs[i - 1] < lim) {
        const f = (lim - xs[i - 1]) / (xs[i] - xs[i - 1]);
        pts.push(`${X(lim)},${Y(lerp(sweep[i - 1][col], sweep[i][col], f))}`);
      }
    }
    return pts.join(' ');
  };
  const peak = sweep.reduce((a, b) => (b[2] > a[2] ? b : a));
  const rx = P ? S.x : cx + cw + 80, rw = P ? S.w : S.r - rx;
  const ry = P ? top2 + chH + 80 : top1 + 10;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0 }}>
        <g opacity={ax}>
          <line x1={cx} y1={top1 + chH} x2={cx + cw} y2={top1 + chH} stroke={CLAUDE.INK} strokeWidth={4} />
          <line x1={cx} y1={top1} x2={cx} y2={top1 + chH} stroke={CLAUDE.INK} strokeWidth={4} />
          <line x1={cx} y1={top2 + chH / 2} x2={cx + cw} y2={top2 + chH / 2} stroke={CLAUDE.INK} strokeWidth={4} />
          <line x1={cx} y1={top2} x2={cx} y2={top2 + chH} stroke={CLAUDE.INK} strokeWidth={4} />
        </g>
        <polyline points={partial(1, Y1, d1)} fill="none" stroke={CLAUDE.INK} strokeWidth={7} strokeLinejoin="round" />
        <polyline points={partial(2, Y2, d2)} fill="none" stroke={ACC_TEXT} strokeWidth={7} strokeLinejoin="round" />
        <line x1={X(peakKL)} y1={top1} x2={X(peakKL)} y2={top2 + chH} stroke={ACC_TEXT} strokeWidth={4} strokeDasharray="12 10" opacity={pk} />
        <circle cx={X(peak[0])} cy={Y2(peak[2])} r={14} fill={ACC_TEXT} opacity={pk} />
      </svg>
      <Label text={rewardLabel} size={P ? 42 : 38} style={{ left: cx + 24, top: top1 - 6, opacity: ax }} />
      <Label text={truthLabel} size={P ? 42 : 38} color={ACC_TEXT} style={{ left: X(peakKL) + 24, top: top2 - 6, opacity: ax }} />
      <Label text={xLabel} size={P ? 36 : 34} color={CLAUDE.INK_SOFT} style={{ left: cx, top: top2 + chH + 10, width: cw, opacity: ax }} />
      <div style={{ position: 'absolute', left: X(peakKL) + 18, top: top1 + chH - (P ? 76 : 70), opacity: pk }}>
        <Pill text={`best at KL ${peakKL.toFixed(2)}`} size={P ? 38 : 36} accent />
      </div>
      <div style={{ position: 'absolute', left: rx, top: ry, width: rw, display: 'flex', flexDirection: 'column', gap: P ? 18 : 26 }}>
        <span style={{ fontFamily: SANS, fontSize: P ? 44 : 42, color: CLAUDE.INK, opacity: plz }}>people-pleasing answers</span>
        <span style={{ fontFamily: SERIF, fontSize: P ? 88 : 84, color: ACC_TEXT, lineHeight: 1, opacity: plz }}>{pleaser0}% → {lerp(pleaser0, pleaser1, plz).toFixed(1)}%</span>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 16, marginTop: P ? 8 : 18 }}>
          {chips.map((c, i) => <Pill key={c} text={c} size={P ? 46 : 44} a={chip(i)} />)}
        </div>
        <span style={{ fontFamily: SANS, fontSize: P ? 34 : 32, color: CLAUDE.INK_SOFT, opacity: chip(1), marginTop: 8 }}>{note}</span>
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// RlNow — RLHF · DPO · RLAIF: all three learn from preferences
// ===========================================================================
export const rlNowSchema = z.object({
  title: z.string().default('Cheaper ways, same idea'),
  lanes: z.array(z.object({ name: z.string(), steps: z.array(z.string()), note: z.string(), logo: z.string() })).default([
    { name: 'RLHF', steps: ['people rank', 'reward model', 'RL'], note: '', logo: '' },
    { name: 'DPO', steps: ['people rank', 'train directly'], note: 'no reward model, no RL loop', logo: '' },
    { name: 'RLAIF', steps: ['an AI ranks', 'reward model', 'RL'], note: 'Constitutional AI', logo: 'logos/anthropic/anthropic-01.svg' },
  ]),
  verdict: z.string().default('All three learn from preferences.'),
  sparkLine: z.string().default('Still taught by preference.'),
  durationSeconds: z.number().optional(),
});
export const rlNowMeta = durMeta(7);
export const RlNow: React.FC<z.infer<typeof rlNowSchema>> = ({ title, lanes, verdict, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const lane = (i: number) => ease(ramp(t, 0.04 + i * 0.2, 0.14 + i * 0.2));
  const vIn = ease(ramp(t, 0.66, 0.74));
  const ly = P ? 300 : 210, lh = P ? 290 : 190;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {lanes.map((l, i) => {
        const a = lane(i);
        const y = ly + i * lh;
        return (
          <Card key={l.name} style={{ left: S.x, top: y, width: S.w, height: lh - (P ? 24 : 26), opacity: a, transform: `translateY(${(1 - a) * 16}px)`,
            display: 'flex', flexDirection: P ? 'column' : 'row', alignItems: P ? 'flex-start' : 'center', justifyContent: P ? 'center' : 'flex-start', gap: P ? 16 : 30, padding: P ? '0 28px' : '0 34px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 20, width: P ? undefined : 300 }}>
              <span style={{ fontFamily: SERIF, fontSize: P ? 66 : 62, color: i === 0 ? CLAUDE.INK : ACC_TEXT, lineHeight: 1 }}>{l.name}</span>
              {P && l.logo && <Img src={staticFile(l.logo)} style={{ height: 56 }} />}
              {P && l.note && <span style={{ fontFamily: SANS, fontSize: 38, color: CLAUDE.INK }}>{l.note}</span>}
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: P ? 10 : 14, flexWrap: 'nowrap' }}>
              {l.steps.map((s, j) => (
                <React.Fragment key={s}>
                  {j > 0 && <span style={{ fontFamily: SANS, fontSize: P ? 40 : 44, color: CLAUDE.INK_SOFT }}>→</span>}
                  <Pill text={s} size={P ? 40 : 42} accent={i > 0 && j === 0} />
                </React.Fragment>
              ))}
            </div>
            {!P && (l.note || l.logo) && (
              <div style={{ display: 'flex', alignItems: 'center', gap: 18, marginLeft: 'auto' }}>
                {l.logo && <Img src={staticFile(l.logo)} style={{ height: 60 }} />}
                <span style={{ fontFamily: SANS, fontSize: 40, color: CLAUDE.INK }}>{l.note}</span>
              </div>
            )}
          </Card>
        );
      })}
      <div style={{ position: 'absolute', left: S.x, top: ly + 3 * lh + (P ? 10 : 10), width: S.w, opacity: vIn, transform: `translateY(${(1 - vIn) * 14}px)` }}>
        <span style={{ display: 'inline-block', background: CLAUDE.INK, borderRadius: 16, padding: P ? '20px 30px' : '20px 36px', fontFamily: SERIF, fontSize: P ? 58 : 60, color: CLAUDE.PAGE, lineHeight: 1.15 }}>{verdict}</span>
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
