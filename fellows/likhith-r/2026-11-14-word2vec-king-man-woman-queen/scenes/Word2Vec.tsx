/**
 * Word2Vec.tsx — reel-local, DUAL-ASPECT Remotion components for
 * claude-hai-word2vec ("Word2Vec: How a Computer Learned That King − Man + Woman ≈ Queen", @HumanitariansAI).
 *
 * Same contract as Grokking.tsx (stage helpers from JevExplainer.tsx): each component lays out natively
 * for 16:9 (<Name>) and 9:16 (<Name>916) — never a crop — and every motion is a pure function of
 * progress, conformed via `durationSeconds`. Every number on screen comes from ./word2vecData.ts,
 * which is GENERATED from the reel's evidence/w2v_toy.json (seeded numpy skip-gram).
 *
 *   WvHook    — king − man + woman = ? → queen; nothing was ever labelled
 *   WvIds     — words as ID numbers: one-hot rows, every pair equally unrelated (cosine 0)
 *   WvCompany — Firth 1957; real toy sentences; how many neighbours cat and kitten share
 *   WvTrain   — Mikolov et al. 2013 skip-gram: a sliding window predicts neighbours; king = 300 numbers
 *   WvMap     — similar words land close (PCA map); relationships become directions (two panels)
 *   WvCatch   — the ranking with the inputs left in (king wins), then excluded (queen); Bolukbasi et al. 2016
 *   WvToday   — tokens → vectors → the model (ChatGPT, Claude)
 *   WvClose   — zero definitions, 30,000 sentences; the sum returns
 */
import React from 'react';
import { AbsoluteFill, Img, staticFile } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from './tokens/claude';
import { SERIF, SANS, ACC_TEXT, ramp, ease, useStage, durMeta, Bug, Title, Spark, Card } from './JevExplainer';
import { WV } from './word2vecData';

const W = (P: boolean) => (P ? 1080 : 1920);
const H = (P: boolean) => (P ? 1920 : 1080);
const lerp = (a: number, b: number, p: number) => a + (b - a) * p;
const fmtInt = (n: number) => Math.round(n).toLocaleString('en-US');
const f2 = (v: number) => v.toFixed(2);
const f3 = (v: number) => v.toFixed(3);

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

// drawn arrow between two points (SVG), grows with p; head drawn only once the shaft is long enough
const ArrowLine: React.FC<{ x1: number; y1: number; x2: number; y2: number; p: number; color: string; w?: number; head?: number }> = ({ x1, y1, x2, y2, p, color, w = 7, head = 26 }) => {
  if (p <= 0) return null;
  const ex = lerp(x1, x2, p), ey = lerp(y1, y2, p);
  const ang = Math.atan2(ey - y1, ex - x1);
  const hx = (k: number) => ex - head * Math.cos(ang + k), hy = (k: number) => ey - head * Math.sin(ang + k);
  return (
    <g>
      <line x1={x1} y1={y1} x2={ex - Math.cos(ang) * w * 0.6} y2={ey - Math.sin(ang) * w * 0.6} stroke={color} strokeWidth={w} strokeLinecap="round" />
      <path d={`M${hx(0.45)} ${hy(0.45)}L${ex} ${ey}L${hx(-0.45)} ${hy(-0.45)}`} fill="none" stroke={color} strokeWidth={w} strokeLinecap="round" strokeLinejoin="round" />
    </g>
  );
};

const get = (pairs: ReadonlyArray<ReadonlyArray<string | number>>, i: number) => pairs[i] as unknown as [string, number];

// ===========================================================================
// WvHook — king − man + woman = ? → queen
// ===========================================================================
export const wvHookSchema = z.object({
  title: z.string().default('A sum of words'),
  note: z.string().default('our toy model · nearest other word · similarity'),
  pills: z.array(z.string()).default(['royalty: never labeled', 'gender: never labeled']),
  sparkLine: z.string().default('Nobody told it.'),
  durationSeconds: z.number().optional(),
});
export const wvHookMeta = durMeta(4.7);
export const WvHook: React.FC<z.infer<typeof wvHookSchema>> = ({ title, note, pills, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const tok = [
    { text: 'king', a: ease(ramp(t, 0.0, 0.05)) },
    { text: '− man', a: ease(ramp(t, 0.05, 0.1)) },
    { text: '+ woman', a: ease(ramp(t, 0.15, 0.2)) },
  ];
  const eqA = ease(ramp(t, 0.24, 0.3));
  const flip = ease(ramp(t, 0.42, 0.48));
  const nIn = ease(ramp(t, 0.48, 0.56));
  const pIn = (i: number) => ease(ramp(t, 0.6 + i * 0.08, 0.66 + i * 0.08));
  const score = get(WV.kingExcluded, 0)[1];
  const fs = P ? 150 : 124;
  const answer = (
    <span style={{ position: 'relative', display: 'inline-block', width: P ? 420 : 380, textAlign: 'left' }}>
      <span style={{ position: 'absolute', left: 0, opacity: eqA * (1 - flip) }}>?</span>
      <span style={{ color: ACC_TEXT, opacity: flip, display: 'inline-block', transform: `translateY(${(1 - flip) * 30}px)` }}>{get(WV.kingExcluded, 0)[0]}</span>
    </span>
  );
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {P ? (
        <div style={{ position: 'absolute', left: S.x, width: S.w, top: 330, display: 'flex', flexDirection: 'column', alignItems: 'center', fontFamily: SERIF, fontSize: fs, lineHeight: 1.12, color: CLAUDE.INK }}>
          {tok.map((k) => <span key={k.text} style={{ opacity: k.a }}>{k.text}</span>)}
          <span style={{ whiteSpace: 'nowrap' }}><span style={{ opacity: eqA }}>= </span>{answer}</span>
        </div>
      ) : (
        <div style={{ position: 'absolute', left: S.x, width: S.w, top: 360, display: 'flex', justifyContent: 'center', alignItems: 'baseline', gap: 40, fontFamily: SERIF, fontSize: fs, lineHeight: 1, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>
          {tok.map((k) => <span key={k.text} style={{ opacity: k.a }}>{k.text}</span>)}
          <span style={{ opacity: eqA }}>=</span>
          {answer}
        </div>
      )}
      <div style={{ position: 'absolute', left: S.x, width: S.w, top: P ? 1050 : 560, textAlign: 'center', opacity: nIn }}>
        <span style={{ fontFamily: SANS, fontSize: P ? 40 : 42, color: CLAUDE.INK_SOFT }}>{note} </span>
        <span style={{ fontFamily: SERIF, fontSize: P ? 64 : 64, color: CLAUDE.INK }}>{f3(score)}</span>
      </div>
      <div style={{ position: 'absolute', left: S.x, width: S.w, top: P ? 1160 : 720, display: 'flex', flexDirection: P ? 'column' : 'row', alignItems: 'center', justifyContent: 'center', gap: P ? 20 : 40 }}>
        {pills.map((p, i) => <Pill key={p} text={p} size={P ? 46 : 50} a={pIn(i)} />)}
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// WvIds — words as ID numbers (one-hot)
// ===========================================================================
export const wvIdsSchema = z.object({
  title: z.string().default('Words as ID numbers'),
  words: z.array(z.string()).default(['cat', 'kitten', 'carburetor']),
  stripLabel: z.string().default('one-hot row: one slot per word, a single 1'),
  simLabel: z.string().default('similarity'),
  sparkLine: z.string().default('Just numbers.'),
  durationSeconds: z.number().optional(),
});
export const wvIdsMeta = durMeta(4.7);
export const WvIds: React.FC<z.infer<typeof wvIdsSchema>> = ({ title, words, stripLabel, simLabel, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const V = WV.vocab as number;
  const ids = WV.ids as unknown as Record<string, number>;
  const oh = WV.onehot as unknown as Record<string, number>;
  const rIn = (i: number) => ease(ramp(t, 0.04 + i * 0.06, 0.1 + i * 0.06));
  const sIn = (i: number) => ease(ramp(t, 0.26 + i * 0.05, 0.34 + i * 0.05));
  const lIn = ease(ramp(t, 0.3, 0.38));
  const kIn = ease(ramp(t, 0.46, 0.54)), cIn = ease(ramp(t, 0.8, 0.88));
  const rowY = (i: number) => (P ? 300 + i * 240 : 230 + i * 170);
  const sx = P ? S.x : S.x + 640, sw = P ? S.w : S.r - (S.x + 640);
  const sh = P ? 60 : 76;
  const cell = sw / V;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {words.map((w, i) => {
        const y = rowY(i);
        const stripY = P ? y + 116 : y + 20;
        return (
          <React.Fragment key={w}>
            <div style={{ position: 'absolute', left: S.x, top: y, display: 'flex', alignItems: 'center', gap: 26, opacity: rIn(i) }}>
              <span style={{ fontFamily: SERIF, fontSize: P ? 84 : 84, lineHeight: 1, color: CLAUDE.INK, width: P ? undefined : 400 }}>{w}</span>
              <Pill text={`ID ${ids[w]}`} size={P ? 46 : 48} />
            </div>
            <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0, opacity: sIn(i) }}>
              {/* outlined, not a pale fill: GATE V averages every non-background pixel, and big pale strips read as low contrast */}
              <rect x={sx + 2} y={stripY + 2} width={sw - 4} height={sh - 4} rx={8} fill="none" stroke={CLAUDE.INK_SOFT} strokeWidth={4} />
              <rect x={sx + ids[w] * cell} y={stripY} width={Math.max(7, cell)} height={sh} fill={CLAUDE.INK} />
            </svg>
          </React.Fragment>
        );
      })}
      <Label text={stripLabel.replace('one slot per word', `${V} slots, one per word`)} size={P ? 38 : 38} color={CLAUDE.INK_SOFT}
        style={{ left: sx, width: sw, top: P ? rowY(2) + 196 : rowY(2) + 120, opacity: lIn }} />
      <div style={{ position: 'absolute', left: S.x, width: S.w, top: P ? 1110 : 830, display: 'flex', flexDirection: P ? 'column' : 'row', gap: P ? 22 : 40, alignItems: P ? 'flex-start' : 'center' }}>
        <Pill text={`${simLabel} cat · kitten = ${oh.cat_kitten}`} size={P ? 46 : 50} a={kIn} />
        <Pill text={`${simLabel} cat · carburetor = ${oh.cat_carburetor}`} size={P ? 46 : 50} a={cIn} accent />
      </div>
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// WvCompany — Firth 1957; the company cat, kitten and carburetor keep
// ===========================================================================
export const wvCompanySchema = z.object({
  title: z.string().default('The company it keeps'),
  quote: z.string().default('“You shall know a word by the company it keeps.”'),
  who: z.string().default('J. R. Firth, linguist, 1957'),
  corpusLabel: z.string().default('from our toy corpus'),
  shareLabel: z.string().default('neighbors shared with cat'),
  sparkLine: z.string().default('Similar places, similar meaning.'),
  durationSeconds: z.number().optional(),
});
export const wvCompanyMeta = durMeta(4.4);
export const WvCompany: React.FC<z.infer<typeof wvCompanySchema>> = ({ title, quote, who, corpusLabel, shareLabel, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const ex = WV.examples as unknown as Record<string, string[]>;
  const share = WV.share as unknown as Record<string, number>;
  const qIn = ease(ramp(t, 0.03, 0.12));
  const sIn = (i: number) => ease(ramp(t, 0.3 + i * 0.06, 0.36 + i * 0.06));
  const bIn = ease(ramp(t, 0.52, 0.66));
  const sents = [
    { w: 'cat', s: ex.cat.find((x) => x.endsWith('purrs')) ?? ex.cat[0] },
    { w: 'kitten', s: ex.kitten.find((x) => x.endsWith('purrs')) ?? ex.kitten[0] },
    { w: 'carburetor', s: ex.carburetor[1] },
  ];
  const qx = S.x, qy = P ? 290 : 220, qw = P ? S.w : 760, qh = P ? 380 : 600;
  const rx = P ? S.x : S.x + 830, rw = P ? S.w : S.r - (S.x + 830);
  const ry = P ? 720 : 220;
  const fs = P ? 52 : 56;
  const bars = [
    { label: `kitten: ${Math.round(share.kitten_in_cat * 100)}%`, v: share.kitten_in_cat, accent: true },
    { label: `carburetor: ${Math.round(share.carburetor_in_cat * 100)}%`, v: share.carburetor_in_cat, accent: false },
  ];
  const by = P ? 1000 : 560;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: qx, top: qy, width: qw, height: qh, borderRadius: 16, background: CLAUDE.INK, opacity: qIn, boxSizing: 'border-box',
        padding: P ? '44px 44px' : '64px 56px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', transform: `translateY(${(1 - qIn) * 20}px)` }}>
        <div style={{ fontFamily: SERIF, fontSize: P ? 66 : 72, lineHeight: 1.15, color: CLAUDE.CARD }}>{quote}</div>
        <div style={{ fontFamily: SANS, fontSize: P ? 40 : 42, color: CLAUDE.CARD }}>{who}</div>
      </div>
      <Label text={corpusLabel} size={P ? 38 : 38} color={CLAUDE.INK_SOFT} style={{ left: rx, top: ry - (P ? 0 : 0), opacity: sIn(0) }} />
      <div style={{ position: 'absolute', left: rx, top: ry + 56, width: rw, display: 'flex', flexDirection: 'column', gap: P ? 10 : 14 }}>
        {sents.map(({ w, s }, i) => (
          <div key={w} style={{ fontFamily: SERIF, fontSize: fs, lineHeight: 1.2, color: CLAUDE.INK, opacity: sIn(i), whiteSpace: 'nowrap' }}>
            {s.split(' ').map((tok, k) => (
              <React.Fragment key={k}><span style={tok === w ? { background: CLAUDE.INK, color: CLAUDE.CARD, padding: '0 12px', borderRadius: 8 } : undefined}>{tok}</span>{' '}</React.Fragment>
            ))}
          </div>
        ))}
      </div>
      <Label text={shareLabel} size={P ? 40 : 40} style={{ left: rx, top: by, opacity: bIn }} />
      {bars.map((b, i) => (
        <div key={b.label} style={{ position: 'absolute', left: rx, top: by + 64 + i * (P ? 120 : 120), width: rw, opacity: bIn }}>
          <div style={{ fontFamily: SANS, fontSize: P ? 40 : 40, color: b.accent ? ACC_TEXT : CLAUDE.INK }}>{b.label}</div>
          <div style={{ marginTop: 6, width: rw * b.v * bIn, height: P ? 40 : 44, borderRadius: 8, background: b.accent ? ACC_TEXT : CLAUDE.INK }} />
        </div>
      ))}
      <Spark st={st} text={sparkLine} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// WvTrain — skip-gram: the window slides; the centre word predicts its neighbours; king = 300 numbers
// ===========================================================================
export const wvTrainSchema = z.object({
  title: z.string().default('Predict the neighbors'),
  source: z.string().default('Mikolov et al., Google, 2013 · the skip-gram model'),
  windowLabel: z.string().default('the middle word learns to predict the words around it'),
  googleLabel: z.string().default('Google: billions of words of news'),
  vecLabel: z.string().default('our toy model’s real vector for “king”'),
  sparkLine: z.string().default('A vector per word.'),
  durationSeconds: z.number().optional(),
});
export const wvTrainMeta = durMeta(8.1);
export const WvTrain: React.FC<z.infer<typeof wvTrainSchema>> = ({ title, source, windowLabel, googleLabel, vecLabel, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const sIn = ease(ramp(t, 0.02, 0.1));
  const rowIn = ease(ramp(t, 0.12, 0.2));
  const words = (WV.windowSentence as string).split(' ');
  const slide = ramp(t, 0.3, 0.6);
  const ci = Math.min(words.length - 1, Math.floor(slide * words.length));
  const winA = ease(ramp(t, 0.28, 0.32));
  const cIn = ease(ramp(t, 0.52, 0.58)), oIn = ease(ramp(t, 0.6, 0.66));
  const vIn = ease(ramp(t, 0.7, 0.76));
  const grow = ramp(t, 0.76, 0.86);
  // word boxes, laid out from character counts (sans, ~0.56 em per char)
  const fs = P ? 40 : 56, pad = P ? 16 : 24, gap = P ? 10 : 16;
  const wOf = (w: string) => w.length * fs * 0.56 + 2 * pad;
  const total = words.reduce((s, w) => s + wOf(w), 0) + gap * (words.length - 1);
  let x = S.x + (S.w - total) / 2;
  const boxes = words.map((w) => { const b = { w, x, cw: wOf(w) }; x += wOf(w) + gap; return b; });
  const by = P ? 520 : 395, bh = fs * 1.7;
  const vec = WV.kingVector as unknown as number[];
  const vmax = Math.max(...vec.map(Math.abs));
  const n = Math.floor(vec.length * grow);
  const vx = S.x, vw = S.w, base = P ? 1130 : 865, amp = P ? 90 : 75;
  const bw = vw / vec.length;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <div style={{ position: 'absolute', left: S.x, top: P ? 290 : 190, width: S.w, display: 'flex', alignItems: 'center', gap: 22, opacity: sIn }}>
        <Img src={staticFile('logos/google/google-01.svg')} style={{ width: 70, height: 70 }} />
        <span style={{ fontFamily: SANS, fontSize: P ? 40 : 44, color: CLAUDE.INK, lineHeight: 1.2 }}>{source}</span>
      </div>
      {/* window arcs: centre → each neighbour */}
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0, opacity: winA }}>
        {boxes.map((b, i) => {
          if (i === ci || Math.abs(i - ci) > (WV.window as number)) return null;
          const c = boxes[ci];
          const x1 = c.x + c.cw / 2, x2 = b.x + b.cw / 2, y = by - 14;
          const h = 46 + Math.abs(i - ci) * 26;
          return <path key={i} d={`M${x1} ${y} Q${(x1 + x2) / 2} ${y - h * 2} ${x2} ${y}`} fill="none" stroke={CLAUDE.INK} strokeWidth={5} />;
        })}
      </svg>
      {boxes.map((b, i) => {
        const inWin = winA > 0 && Math.abs(i - ci) <= (WV.window as number);
        const centre = winA > 0 && i === ci;
        return (
          <div key={i} style={{ position: 'absolute', left: b.x, top: by, width: b.cw, height: bh, borderRadius: 12, opacity: rowIn,
            background: centre ? ACC_TEXT : inWin ? CLAUDE.INK : CLAUDE.CARD, border: `3px solid ${centre || inWin ? 'transparent' : CLAUDE.BORDER}`, boxSizing: 'border-box',
            display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SANS, fontSize: fs, color: centre || inWin ? CLAUDE.CARD : CLAUDE.INK }}>{b.w}</div>
        );
      })}
      <Label text={windowLabel} size={P ? 38 : 40} color={CLAUDE.INK_SOFT} style={{ left: S.x, width: S.w, textAlign: 'center', top: by + bh + 26, opacity: winA }} />
      <div style={{ position: 'absolute', left: S.x, width: S.w, top: P ? 710 : 585, display: 'flex', flexDirection: P ? 'column' : 'row', gap: P ? 18 : 30, justifyContent: 'center', alignItems: 'center' }}>
        <Pill text={googleLabel} size={P ? 42 : 46} a={cIn} />
        <Pill text={`our toy: ${fmtInt(WV.tokens as number)} words`} size={P ? 42 : 46} a={oIn} fill={CLAUDE.INK_SOFT} />
      </div>
      <div style={{ position: 'absolute', left: S.x, width: S.w, top: base - amp - (P ? 140 : 115), display: 'flex', alignItems: 'baseline', gap: 26, opacity: vIn, flexWrap: 'wrap' }}>
        <span style={{ fontFamily: SERIF, fontSize: P ? 80 : 80, lineHeight: 1, color: CLAUDE.INK }}>king =</span>
        <span style={{ fontFamily: SERIF, fontSize: P ? 80 : 80, lineHeight: 1, color: ACC_TEXT }}>{vec.length} numbers</span>
        {!P && <span style={{ fontFamily: SANS, fontSize: 38, color: CLAUDE.INK_SOFT }}>{vecLabel}</span>}
      </div>
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0, opacity: vIn }}>
        <line x1={vx} y1={base} x2={vx + vw} y2={base} stroke={CLAUDE.BORDER} strokeWidth={3} />
        {vec.slice(0, n).map((v, i) => {
          const h = (v / vmax) * amp;
          return <rect key={i} x={vx + i * bw + bw * 0.15} y={h > 0 ? base - h : base} width={bw * 0.7} height={Math.max(2, Math.abs(h))} fill={CLAUDE.INK} />;
        })}
      </svg>
      {P && <Label text={vecLabel} size={38} color={CLAUDE.INK_SOFT} style={{ left: S.x, width: S.w, top: base + amp + 20, opacity: vIn }} />}
      <Spark st={st} text={sparkLine} at={0.86} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// WvMap — similar words land close; relationships become directions
// ===========================================================================
export const wvMapSchema = z.object({
  title: z.string().default('Meaning becomes geometry'),
  mapLabel: z.string().default('our toy: 300 numbers squeezed to 2 (PCA)'),
  matchLabel: z.string().default('direction match'),
  sparkLine: z.string().default('Relationships are directions.'),
  durationSeconds: z.number().optional(),
});
export const wvMapMeta = durMeta(7.1);

type Panel = { words: readonly string[]; xy: readonly (readonly number[])[] };
const PanelArt: React.FC<{ g: Panel; box: { x: number; y: number; w: number; h: number }; pairs: [number, number, number][]; P: boolean; fs: number }> = ({ g, box, pairs, fs }) => {
  // pairs: [from, to, progress]; positions scaled into the box with a margin for labels
  const xs = g.xy.map((p) => p[0]), ys = g.xy.map((p) => p[1]);
  const mx = 90, my = 60;
  const sx = (v: number) => box.x + mx + ((v - Math.min(...xs)) / (Math.max(...xs) - Math.min(...xs) || 1)) * (box.w - 2 * mx);
  const sy = (v: number) => box.y + my + ((Math.max(...ys) - v) / (Math.max(...ys) - Math.min(...ys) || 1)) * (box.h - 2 * my);
  const pt = (i: number) => [sx(g.xy[i][0]), sy(g.xy[i][1])];
  return (
    <>
      <svg width={4000} height={4000} style={{ position: 'absolute', left: 0, top: 0, overflow: 'visible' }}>
        {pairs.map(([a, b, p], k) => {
          const [x1, y1] = pt(a), [x2, y2] = pt(b);
          const d = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / d, uy = (y2 - y1) / d;
          return <ArrowLine key={k} x1={x1 + ux * 22} y1={y1 + uy * 22} x2={x2 - ux * 22} y2={y2 - uy * 22} p={p} color={k === 0 ? CLAUDE.INK : CLAUDE.SPARK} w={7} head={24} />;
        })}
        {g.words.map((w, i) => { const [x, y] = pt(i); return <circle key={w} cx={x} cy={y} r={13} fill={CLAUDE.INK} />; })}
      </svg>
      {g.words.map((w, i) => {
        const [x, y] = pt(i);
        const below = g.xy[i][1] < (Math.max(...ys) + Math.min(...ys)) / 2;
        return <Label key={w} text={w} size={fs} style={{ left: x - 150, width: 300, textAlign: 'center', top: below ? y + 22 : y - 22 - fs * 1.15 }} />;
      })}
    </>
  );
};

export const WvMap: React.FC<z.infer<typeof wvMapSchema>> = ({ title, mapLabel, matchLabel, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const words = WV.mapWords as unknown as string[];
  const xy = WV.mapXY as unknown as number[][];
  const cos = WV.cos as unknown as Record<string, number>;
  const off = WV.offset as unknown as Record<string, number>;
  const mIn = ease(ramp(t, 0.02, 0.1));
  const cIn = ease(ramp(t, 0.1, 0.18));
  const panIn = ease(ramp(t, 0.3, 0.38));
  const a1 = ease(ramp(t, 0.43, 0.5)), a2 = ease(ramp(t, 0.6, 0.67)), a3 = ease(ramp(t, 0.72, 0.78)), a4 = ease(ramp(t, 0.84, 0.9));
  const v1 = ease(ramp(t, 0.66, 0.72)), v2 = ease(ramp(t, 0.9, 0.95));
  // the map
  const mb = P ? { x: S.x, y: 290, w: S.w, h: 430 } : { x: S.x, y: 220, w: 800, h: 560 };
  const xs = xy.map((p) => p[0]), ys = xy.map((p) => p[1]);
  const m = 60, mTop = 40, mBot = 80; // bottom margin keeps the caption clear of the dots
  const px = (v: number) => mb.x + m + ((v - Math.min(...xs)) / (Math.max(...xs) - Math.min(...xs))) * (mb.w - 2 * m);
  const py = (v: number) => mb.y + mTop + ((Math.max(...ys) - v) / (Math.max(...ys) - Math.min(...ys))) * (mb.h - mTop - mBot);
  // label side per cluster, chosen from where the empty space is on this map
  const groups = [
    { label: 'king · queen · man · woman', ws: ['king', 'queen', 'man', 'woman'], below: true },
    { label: 'paris · france · tokyo · japan', ws: ['paris', 'france', 'tokyo', 'japan'], below: false },
    { label: 'cat · kitten', ws: ['cat', 'kitten'], below: false },
    { label: 'carburetor', ws: ['carburetor'], below: false, right: true },
  ];
  const centre = (ws: string[]) => {
    const pts = ws.map((w) => xy[words.indexOf(w)]);
    return [pts.reduce((s, p) => s + p[0], 0) / pts.length, pts.reduce((s, p) => s + p[1], 0) / pts.length];
  };
  const gfs = P ? 36 : 36;
  // the two direction panels
  const pw = P ? (S.w - 30) / 2 : S.r - (S.x + 860), ph = P ? 490 : 350;
  const panels = P
    ? [{ x: S.x, y: 820 }, { x: S.x + pw + 30, y: 820 }]
    : [{ x: S.x + 860, y: 220 }, { x: S.x + 860, y: 600 }];
  const people = WV.people as unknown as Panel, places = WV.places as unknown as Panel;
  const artH = P ? 290 : ph - 20;
  const artW = P ? pw : pw - 300;
  const matches = [
    { v: off.man_woman__king_queen, word: 'roughly', a: v1 },
    { v: off.france_paris__japan_tokyo, word: 'closely', a: v2 },
  ];
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: mb.x, top: mb.y, width: mb.w, height: mb.h, opacity: mIn }} />
      <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0, opacity: mIn }}>
        {/* card-coloured ring: near-coincident dots (cat, kitten) stay separate shapes instead of one wide blob GATE T reads as a text run */}
        {words.map((w, i) => <circle key={w} cx={px(xy[i][0])} cy={py(xy[i][1])} r={P ? 12 : 13} fill={CLAUDE.INK} stroke={CLAUDE.CARD} strokeWidth={3} />)}
      </svg>
      {groups.map((g) => {
        const [cx] = centre(g.ws);
        const gy = g.ws.map((w) => py(xy[words.indexOf(w)][1]));
        const x = Math.min(Math.max(px(cx) - 230, mb.x + 16), mb.x + mb.w - 476);
        if ((g as { right?: boolean }).right) return <Label key={g.label} text={g.label} size={gfs} style={{ left: px(cx) + 26, top: gy[0] - gfs * 0.62, opacity: mIn, whiteSpace: 'nowrap' }} />;
        return <Label key={g.label} text={g.label} size={gfs} style={{ left: x, width: 460, textAlign: 'center', top: g.below ? Math.max(...gy) + 24 : Math.min(...gy) - 26 - gfs * 1.2, opacity: mIn }} />;
      })}
      <Label text={mapLabel} size={P ? 34 : 34} color={CLAUDE.INK_SOFT} style={{ left: mb.x + 24, top: mb.y + mb.h - 54, opacity: mIn }} />
      <div style={{ position: 'absolute', left: mb.x, top: mb.y + mb.h + (P ? 22 : 24), width: mb.w, display: 'flex', gap: P ? 16 : 24, flexWrap: 'wrap' }}>
        <Pill text={`cat · kitten ${f2(cos.cat_kitten)}`} size={P ? 40 : 42} a={cIn} />
        <Pill text={`cat · carburetor ${f2(cos.cat_carburetor)}`} size={P ? 40 : 42} a={cIn} fill={CLAUDE.INK_SOFT} />
      </div>
      {[people, places].map((g, k) => {
        const pos = panels[k];
        const art = { x: pos.x, y: pos.y + (P ? 0 : 10), w: artW, h: artH };
        const pairs: [number, number, number][] = k === 0 ? [[0, 1, a1], [2, 3, a2]] : [[0, 1, a3], [2, 3, a4]];
        const mt = matches[k];
        return (
          <React.Fragment key={k}>
            <Card style={{ left: pos.x, top: pos.y, width: pw, height: ph, opacity: panIn }} />
            <div style={{ opacity: panIn }}><PanelArt g={g} box={art} pairs={pairs} P={P} fs={P ? 38 : 38} /></div>
            <div style={{ position: 'absolute', opacity: mt.a, ...(P ? { left: pos.x, width: pw, top: pos.y + artH + 20, textAlign: 'center' } : { left: pos.x + artW, width: 280, top: pos.y + 80 }) }}>
              <div style={{ fontFamily: SANS, fontSize: P ? 36 : 38, color: CLAUDE.INK }}>{matchLabel}</div>
              <div style={{ fontFamily: SERIF, fontSize: P ? 80 : 96, lineHeight: 1.05, color: k === 1 ? ACC_TEXT : CLAUDE.INK }}>{f3(mt.v)}</div>
              <div style={{ fontFamily: SANS, fontSize: P ? 36 : 38, color: CLAUDE.INK_SOFT }}>{mt.word}</div>
            </div>
          </React.Fragment>
        );
      })}
      <Spark st={st} text={sparkLine} at={0.9} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// WvCatch — inputs included vs excluded; Bolukbasi et al. 2016
// ===========================================================================
export const wvCatchSchema = z.object({
  title: z.string().default('The catch'),
  rankLabel: z.string().default('nearest to king − man + woman · our toy'),
  excludedLabel: z.string().default('inputs excluded: queen is #1'),
  paperWho: z.string().default('Bolukbasi et al., 2016'),
  paperTitle: z.string().default('Man is to Computer Programmer as Woman is to Homemaker?'),
  paperSub: z.string().default('analogies found in Google’s Word2Vec news vectors'),
  pairs: z.array(z.string()).default(['man : computer programmer', 'woman : homemaker']),
  sparkLine: z.string().default('It learns our biases too.'),
  durationSeconds: z.number().optional(),
});
export const wvCatchMeta = durMeta(7.4);
export const WvCatch: React.FC<z.infer<typeof wvCatchSchema>> = ({ title, rankLabel, excludedLabel, paperWho, paperTitle, paperSub, pairs, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const rows = WV.kingIncluded as unknown as [string, number][];
  const inputs = new Set(['king', 'man', 'woman']);
  const rIn = ease(ramp(t, 0.02, 0.08));
  const strike = ease(ramp(t, 0.13, 0.2));
  const promo = ease(ramp(t, 0.2, 0.27));
  const pIn = ease(ramp(t, 0.36, 0.44));
  const q1 = ease(ramp(t, 0.66, 0.72)), q2 = ease(ramp(t, 0.86, 0.91));
  const cx = S.x, cy = P ? 290 : 220, cw = P ? S.w : 800, ch = P ? 560 : 640;
  const rowH = P ? 92 : 105, fs = P ? 62 : 66;
  // ranks after exclusion
  let k = 0;
  const newRank = rows.map(([w]) => (inputs.has(w) ? null : ++k));
  const px = P ? S.x : S.x + 870, pw = P ? S.w : S.r - px;
  const py = P ? 880 : 220, ph = P ? 290 : 460;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: cx, top: cy, width: cw, height: ch, opacity: rIn }} />
      <Label text={rankLabel} size={P ? 38 : 38} color={CLAUDE.INK_SOFT} style={{ left: cx + 40, top: cy + 34, width: cw - 80, opacity: rIn }} />
      {rows.map(([w, v], i) => {
        const y = cy + (P ? 100 : 105) + i * rowH;
        const isIn = inputs.has(w);
        const isQueen = newRank[i] === 1;
        const rankOld = i + 1, rankNew = newRank[i];
        const dim = isIn ? lerp(1, 0.5, strike) : 1;
        const textW = (w.length + 1) * fs * 0.48;
        return (
          <React.Fragment key={w}>
            {/* strike line drawn BEHIND the text */}
            <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0, opacity: rIn }}>
              {isIn && strike > 0 && <line x1={cx + 140} y1={y + fs * 0.62} x2={cx + 140 + (textW + 40) * strike} y2={y + fs * 0.62} stroke={ACC_TEXT} strokeWidth={7} strokeLinecap="round" />}
            </svg>
            <div style={{ position: 'absolute', left: cx + 40, top: y, width: cw - 80, display: 'flex', alignItems: 'baseline', opacity: rIn * dim }}>
              <span style={{ fontFamily: SERIF, fontSize: fs, width: 100, color: isQueen && promo > 0.5 ? ACC_TEXT : CLAUDE.INK }}>
                {promo > 0.5 ? (isIn ? '–' : rankNew) : rankOld}
              </span>
              <span style={{ fontFamily: SERIF, fontSize: fs, flex: 1, color: isQueen && promo > 0.5 ? ACC_TEXT : CLAUDE.INK }}>{w}</span>
              <span style={{ fontFamily: SANS, fontSize: P ? 46 : 50, color: CLAUDE.INK }}>{f3(v)}</span>
            </div>
          </React.Fragment>
        );
      })}
      <div style={{ position: 'absolute', left: cx + 40, top: cy + ch - (P ? 84 : 96), opacity: promo }}>
        <Pill text={excludedLabel} size={P ? 40 : 44} accent />
      </div>
      <div style={{ position: 'absolute', left: px, top: py, width: pw, height: ph, borderRadius: 16, background: CLAUDE.INK, opacity: pIn, boxSizing: 'border-box',
        padding: P ? '34px 40px' : '48px 50px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', transform: `translateY(${(1 - pIn) * 20}px)` }}>
        <div style={{ fontFamily: SANS, fontSize: P ? 38 : 42, color: CLAUDE.CARD }}>{paperWho}</div>
        <div style={{ fontFamily: SERIF, fontSize: P ? 54 : 62, lineHeight: 1.12, color: CLAUDE.CARD }}>{paperTitle}</div>
        <div style={{ fontFamily: SANS, fontSize: P ? 34 : 36, color: CLAUDE.CARD }}>{paperSub}</div>
      </div>
      <div style={{ position: 'absolute', left: px, top: py + ph + (P ? 20 : 36), width: pw, display: 'flex', flexDirection: P ? 'row' : 'column', flexWrap: 'wrap', gap: P ? 12 : 20 }}>
        <div><Pill text={pairs[0]} size={P ? 40 : 50} a={q1} /></div>
        <div><Pill text={pairs[1]} size={P ? 40 : 50} a={q2} /></div>
      </div>
      <Spark st={st} text={sparkLine} at={0.9} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// WvToday — tokens → vectors → the model
// ===========================================================================
export const wvTodaySchema = z.object({
  title: z.string().default('Still step one'),
  modelLabel: z.string().default('ChatGPT · Claude · every modern model'),
  chip: z.string().default('Word2Vec, 2013: made the idea famous'),
  note: z.string().default('today’s models learn their own vectors, for word pieces'),
  vecNote: z.string().default('our toy’s vectors, first 48 of 300 numbers'),
  sparkLine: z.string().default('Words in, vectors first.'),
  durationSeconds: z.number().optional(),
});
export const wvTodayMeta = durMeta(4.5);
export const WvToday: React.FC<z.infer<typeof wvTodaySchema>> = ({ title, modelLabel, chip, note, vecNote, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const tv = WV.tokenVectors as unknown as Record<string, number[]>;
  const toks = ['the', 'cat', 'purrs'];
  const lg1 = ease(ramp(t, 0.0, 0.06)), lg2 = ease(ramp(t, 0.12, 0.18));
  const tIn = (i: number) => ease(ramp(t, 0.28 + i * 0.05, 0.34 + i * 0.05));
  const vIn = (i: number) => ease(ramp(t, 0.5 + i * 0.05, 0.58 + i * 0.05));
  const flow = ease(ramp(t, 0.66, 0.76));
  const chIn = ease(ramp(t, 0.74, 0.82));
  // model card
  const mx = P ? S.x : S.x + 1060, my = P ? 290 : 220, mw = P ? S.w : S.r - (S.x + 1060), mh = P ? 300 : 460;
  const logo = P ? 120 : 150;
  const rowY = (i: number) => (P ? 690 + i * 130 : 240 + i * 150);
  const chipW = P ? 220 : 220;
  const vx = S.x + chipW + 40, vw = P ? S.r - vx : 620, vh = P ? 80 : 90;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      <Card style={{ left: mx, top: my, width: mw, height: mh, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: P ? 20 : 34 }}>
        <div style={{ display: 'flex', gap: P ? 60 : 70 }}>
          <Img src={staticFile('logos/chatgpt/chatgpt-01.svg')} style={{ width: logo, height: logo, opacity: lg1 }} />
          <Img src={staticFile('logos/claude/claude-01.svg')} style={{ width: logo, height: logo, opacity: lg2 }} />
        </div>
        <div style={{ fontFamily: SANS, fontSize: P ? 40 : 40, color: CLAUDE.INK, textAlign: 'center', padding: '0 24px', opacity: lg2 }}>{modelLabel}</div>
      </Card>
      {toks.map((w, i) => {
        const v = tv[w]; const vmax = Math.max(...v.map(Math.abs));
        const y = rowY(i), base = y + vh / 2, bw = vw / v.length;
        return (
          <React.Fragment key={w}>
            <div style={{ position: 'absolute', left: S.x, top: y + (vh - (P ? 70 : 78)) / 2, width: chipW, height: P ? 70 : 78, borderRadius: 12, background: CLAUDE.INK, opacity: tIn(i),
              display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SANS, fontSize: P ? 44 : 48, color: CLAUDE.CARD }}>{w}</div>
            <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0, opacity: vIn(i) }}>
              <line x1={vx} y1={base} x2={vx + vw} y2={base} stroke={CLAUDE.BORDER} strokeWidth={3} />
              {v.map((x, k) => { const h = (x / vmax) * (vh / 2); return <rect key={k} x={vx + k * bw + bw * 0.18} y={h > 0 ? base - h : base} width={bw * 0.64} height={Math.max(2, Math.abs(h))} fill={CLAUDE.INK} />; })}
              {!P && <ArrowLine x1={vx + vw + 30} y1={base} x2={mx - 30} y2={my + mh / 2} p={flow} color={CLAUDE.INK} w={6} head={22} />}
            </svg>
          </React.Fragment>
        );
      })}
      {P && (
        <svg width={W(P)} height={H(P)} style={{ position: 'absolute', left: 0, top: 0 }}>
          <ArrowLine x1={S.x + S.w / 2} y1={rowY(0) - 30} x2={S.x + S.w / 2} y2={my + mh + 30} p={flow} color={CLAUDE.INK} w={6} head={22} />
        </svg>
      )}
      <Label text={vecNote} size={P ? 34 : 34} color={CLAUDE.INK_SOFT} style={{ left: vx, top: rowY(2) + vh + 14, width: vw, opacity: vIn(2) }} />
      <div style={{ position: 'absolute', left: S.x, top: P ? 1130 : 760, width: S.w, opacity: chIn, display: 'flex', flexDirection: 'column', gap: 16, alignItems: 'flex-start' }}>
        <Pill text={chip} size={P ? 42 : 48} accent />
        <span style={{ fontFamily: SANS, fontSize: P ? 34 : 36, color: CLAUDE.INK_SOFT }}>{note}</span>
      </div>
      <Spark st={st} text={sparkLine} at={0.86} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};

// ===========================================================================
// WvClose — zero definitions; the sum returns
// ===========================================================================
export const wvCloseSchema = z.object({
  title: z.string().default('No definitions needed'),
  defLabel: z.string().default('definitions given'),
  sentLabel: z.string().default('sentences read · our toy'),
  sparkLine: z.string().default('The company words keep.'),
  durationSeconds: z.number().optional(),
});
export const wvCloseMeta = durMeta(3.4);
export const WvClose: React.FC<z.infer<typeof wvCloseSchema>> = ({ title, defLabel, sentLabel, sparkLine }) => {
  const st = useStage(); const { t, P, S } = st;
  const c1 = ease(ramp(t, 0.02, 0.1)), c2 = ease(ramp(t, 0.1, 0.18));
  const eIn = ease(ramp(t, 0.3, 0.42));
  const qIn = ease(ramp(t, 0.45, 0.55));
  const cw = P ? S.w : (S.w - 60) / 2, chh = P ? 230 : 270;
  const cards = [
    { label: defLabel, v: '0', a: c1 },
    { label: sentLabel, v: fmtInt(WV.sentences as number), a: c2 },
  ];
  const answer = get(WV.kingExcluded, 0)[0];
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title st={st} text={title} />
      {cards.map((c, i) => (
        <Card key={c.label} style={{ left: P ? S.x : S.x + i * (cw + 60), top: P ? 300 + i * (chh + 30) : 230, width: cw, height: chh, opacity: c.a,
          display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 6 }}>
          <span style={{ fontFamily: SANS, fontSize: P ? 42 : 44, color: CLAUDE.INK }}>{c.label}</span>
          <span style={{ fontFamily: SERIF, fontSize: P ? 130 : 150, lineHeight: 1, color: CLAUDE.INK }}>{c.v}</span>
        </Card>
      ))}
      <div style={{ position: 'absolute', left: S.x, width: S.w, top: P ? 880 : 610, display: 'flex', flexDirection: P ? 'column' : 'row', justifyContent: 'center', alignItems: 'center', gap: P ? 0 : 36,
        fontFamily: SERIF, fontSize: P ? 108 : 110, lineHeight: 1.15, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>
        <span style={{ opacity: eIn }}>king − man + woman</span>
        <span><span style={{ opacity: eIn }}>≈ </span><span style={{ color: ACC_TEXT, opacity: qIn }}>{answer}</span></span>
      </div>
      <Spark st={st} text={sparkLine} at={0.72} />
      <Bug st={st} />
    </AbsoluteFill>
  );
};
