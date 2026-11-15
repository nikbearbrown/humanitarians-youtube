/**
 * TtvScenes.tsx — Remotion components for "How a Computer Turns Text into a Voice"
 * (Humanitarians AI fellow explainer, Tanishaa). Registered in Root.tsx under the
 * folder "TextToVoice".
 *
 * Same look as RagScenes.tsx / LbScenes.tsx: Claude fidelity cream #FAF9F5, ink
 * #3D3929, terracotta #D97757 as the one accent (#AF4B2D when it carries words).
 * 1920x1080 (and native 1080x1920 <Name>916), 30 fps. Every reveal time is a prop
 * (fraction of the beat, cued to the measured spoken word). Waveforms, samples,
 * style numbers and phonemes are real Kokoro output (youtube/text-to-voice/demo).
 */
import React from 'react';
import { AbsoluteFill, Img, staticFile, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { HaiBug } from './RagScenes';

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
// IPA needs stress (ˈ) and length (ː) marks, which the mono fonts draw as ' and :
const IPA = '-apple-system, "SF Pro Text", "Helvetica Neue", "Lucida Grande", sans-serif';

const SX = 96;
const SY = 54;
const CW = 1920;

const cl = (v: number, a = 0, b = 1) => Math.min(b, Math.max(a, v));
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

const Spark: React.FC<{ line: string; o: number }> = ({ line, o }) =>
  line ? (
    <div style={{ position: 'absolute', left: SX, top: SY + 6, display: 'flex', alignItems: 'baseline', gap: 16, opacity: o }}>
      <span style={{ fontFamily: SERIF, fontSize: 58, color: ACC_TEXT, lineHeight: 1 }}>*</span>
      <span style={{ fontFamily: SERIF, fontSize: 50, color: SOFT, lineHeight: 1 }}>{line}</span>
    </div>
  ) : null;

const Footnote: React.FC<{ text: string; o: number }> = ({ text, o }) =>
  text ? (
    <div style={{ position: 'absolute', left: SX, bottom: SY + 8, right: SX + 120, fontFamily: SANS,
      fontSize: 28, color: SOFT, opacity: o }}>{text}</div>
  ) : null;

/** Mirrored bar waveform from a real amplitude envelope. `reveal` sweeps it in left to right. */
const Waveform: React.FC<{ env: number[]; w: number; h: number; color?: string; reveal?: number; style?: React.CSSProperties }> =
  ({ env, w, h, color = INK, reveal = 1, style }) => {
    const n = env.length, peak = Math.max(0.001, ...env), bw = w / n;
    return (
      <svg width={w} height={h} style={style}>
        <line x1={0} y1={h / 2} x2={w} y2={h / 2} stroke={BORDER} strokeWidth={2} />
        {env.map((v, i) => {
          if (i / n > reveal) return null;
          const bh = Math.max(3, (v / peak) * (h - 6));
          return <rect key={i} x={i * bw + bw * 0.15} y={(h - bh) / 2} width={Math.max(1.5, bw * 0.7)} height={bh} rx={bw * 0.35} fill={color} />;
        })}
      </svg>
    );
  };

const dur = { durationSeconds: z.number().optional() };

/** Text split into parts; the parts listed in `hot` are drawn in the accent and underlined. */
const HotText: React.FC<{ parts: string[]; hot: number[]; size: number; o?: number }> = ({ parts, hot, size, o = 1 }) => (
  <span style={{ fontFamily: SERIF, fontSize: size, color: INK, whiteSpace: 'pre' }}>
    {parts.map((s, i) => hot.includes(i)
      ? <span key={i} style={{ color: o > 0.5 ? ACC_TEXT : INK, textDecoration: o > 0.5 ? 'underline' : 'none',
          textDecorationThickness: Math.max(3, size * 0.06), textUnderlineOffset: size * 0.14 }}>{s}</span>
      : <span key={i}>{s}</span>)}
  </span>
);

// ===========================================================================
// TtvTrickyLines — three lines where writing and speech disagree. Each line
// arrives on its cue; its tricky parts turn terracotta with a short question.
// ===========================================================================
export const ttvTrickyLinesSchema = z.object({
  spark: z.string().default(''),
  lines: z.array(z.object({ parts: z.array(z.string()), hot: z.array(z.number()), note: z.string(), at: z.number() })),
  ...dur,
});
export const TtvTrickyLines: React.FC<z.infer<typeof ttvTrickyLinesSchema>> = (p) => {
  const t = useT();
  const TOP = 220, ROW = 270;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <Spark line={p.spark} o={rise(t, 0)} />
      {p.lines.map((l, i) => {
        const o = rise(t, l.at), hot = rise(t, l.at + FADE * 1.5);
        return (
          <div key={i} style={{ position: 'absolute', left: SX + 40, top: TOP + i * ROW, opacity: o,
            transform: `translateY(${(1 - o) * 24}px)` }}>
            <HotText parts={l.parts} hot={l.hot} size={76} o={hot} />
            <div style={{ fontFamily: SERIF, fontStyle: 'italic', fontSize: 50, color: ACC_TEXT, marginTop: 14, opacity: hot }}>{l.note}</div>
          </div>
        );
      })}
      <HaiBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// TtvPipeline — four steps, each lighting on its name, each with a tiny worked
// example of what that step makes ($5 → words → phonemes → timing → wave).
// ===========================================================================
export const ttvPipelineSchema = z.object({
  spark: z.string().default(''),
  steps: z.array(z.object({ name: z.string(), detail: z.string(), example: z.string() })),
  stepAt: z.array(z.number()),
  envelope: z.array(z.number()).default([]),
  ...dur,
});
const TimingBars: React.FC<{ w: number; h: number; o: number }> = ({ w, h, o }) => {
  // schematic: one bar per sound of "five dollars", width = length, height = pitch
  const s = [{ l: 'f', w: 0.8, p: 0.5 }, { l: 'aɪ', w: 1.6, p: 0.85 }, { l: 'v', w: 0.7, p: 0.55 },
    { l: 'd', w: 0.6, p: 0.6 }, { l: 'ɑː', w: 1.4, p: 0.7 }, { l: 'l', w: 0.7, p: 0.5 }, { l: 'ɚ', w: 1.0, p: 0.4 }, { l: 'z', w: 0.9, p: 0.3 }];
  const total = s.reduce((a, b) => a + b.w, 0), gap = 6, usable = w - gap * (s.length - 1);
  let x = 0;
  return (
    <svg width={w} height={h}>
      {s.map((b, i) => {
        const bw = (b.w / total) * usable, bh = b.p * (h - 10) * o;
        const r = <rect key={i} x={x} y={h - bh} width={bw} height={bh} rx={4} fill={i === 1 ? ACC : INK} opacity={0.85} />;
        x += bw + gap;
        return r;
      })}
    </svg>
  );
};
export const TtvPipeline: React.FC<z.infer<typeof ttvPipelineSchema>> = (p) => {
  const t = useT();
  const n = p.steps.length, GAP = 48, W = (CW - 2 * SX - (n - 1) * GAP) / n, TOP = 210, H = 690;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <Spark line={p.spark} o={rise(t, 0)} />
      {p.steps.map((s, i) => {
        const o = rise(t, p.stepAt[i] ?? 0), x = SX + i * (W + GAP);
        const ex = s.example;
        return (
          <React.Fragment key={i}>
            <div style={{ position: 'absolute', left: x, top: TOP, width: W, height: H, boxSizing: 'border-box', background: CARD,
              borderRadius: 20, padding: '32px 28px', border: `2px solid ${o > 0.5 ? INK : BORDER}`, opacity: 0.25 + 0.75 * o,
              transform: `translateY(${(1 - o) * 20}px)` }}>
              <div style={{ fontFamily: SANS, fontSize: 36, letterSpacing: 2, color: SOFT }}>{`STEP ${i + 1}`}</div>
              <div style={{ fontFamily: SERIF, fontSize: 62, lineHeight: 1.02, color: INK, marginTop: 10, height: 130 }}>{s.name}</div>
              <div style={{ fontFamily: SERIF, fontSize: 40, lineHeight: 1.18, color: SOFT, marginTop: 8 }}>{s.detail}</div>
              <div style={{ position: 'absolute', left: 28, right: 28, bottom: 36, height: 170, borderTop: `2px solid ${BORDER}`,
                paddingTop: 26, opacity: o }}>
                {ex === 'bars' ? <TimingBars w={W - 56} h={130} o={o} />
                  : ex === 'wave' ? <Waveform env={p.envelope} w={W - 56} h={130} color={ACC_TEXT} reveal={o} />
                  : <div style={{ fontFamily: i === 1 ? IPA : SERIF, fontSize: i === 1 ? 44 : 46, color: ACC_TEXT, lineHeight: 1.2 }}>{ex}</div>}
              </div>
            </div>
            {i < n - 1 ? (
              <div style={{ position: 'absolute', left: x + W, top: TOP + H / 2 - 44, width: GAP, textAlign: 'center',
                fontFamily: SANS, fontSize: 64, color: rise(t, p.stepAt[i + 1] ?? 1) > 0.5 ? INK : GHOST }}>→</div>
            ) : null}
          </React.Fragment>
        );
      })}
      <HaiBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// TtvWave — a real waveform of Bella's voice; zoom into raw sample numbers;
// 24,000 per second; then the voice itself as a list of style numbers, and the
// swap to another voice redraws the same sentence's wave.
// ===========================================================================
export const ttvWaveSchema = z.object({
  envelope: z.array(z.number()),
  otherEnvelope: z.array(z.number()),
  samples: z.array(z.number()),
  sampleRate: z.number(),
  styleSize: z.number(),
  bellaStyle: z.array(z.number()),
  otherStyle: z.array(z.number()),
  bellaLabel: z.string().default('Bella'),
  otherLabel: z.string().default('Michael'),
  waveAt: z.number().default(0.02),
  zoomAt: z.number().default(0.15),
  rateAt: z.number().default(0.3),
  netAt: z.number().default(0.45),
  styleAt: z.number().default(0.6),
  swapAt: z.number().default(0.8),
  footnote: z.string().default(''),
  footnoteShort: z.string().default(''),
  ...dur,
});
const fmt = (v: number) => (Math.abs(v) < 0.0005 ? ' ' : v > 0 ? '+' : '−') + Math.abs(v).toFixed(3);
export const TtvWave: React.FC<z.infer<typeof ttvWaveSchema>> = (p) => {
  const t = useT();
  const wave = rise(t, p.waveAt, FADE * 3), zoom = rise(t, p.zoomAt), rate = rise(t, p.rateAt), net = rise(t, p.netAt);
  const style = rise(t, p.styleAt), swap = rise(t, p.swapAt);
  const WW = CW - 2 * SX, WH = 250, WTOP = 110;
  const ZX = SX + WW * 0.12, ZW = WW * 0.05;          // the window that gets "zoomed"
  const chipW = 134, chipGap = 10, CTOP = 440;
  const sty = swap > 0.5 ? p.otherStyle : p.bellaStyle;
  const who = swap > 0.5 ? p.otherLabel : p.bellaLabel;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: SX, top: WTOP, opacity: wave }}>
        <div style={{ position: 'absolute', left: 0, top: 0, opacity: 1 - swap }}>
          <Waveform env={p.envelope} w={WW} h={WH} color={INK} reveal={wave} />
        </div>
        <div style={{ position: 'absolute', left: 0, top: 0, opacity: swap }}>
          <Waveform env={p.otherEnvelope} w={WW} h={WH} color={ACC_TEXT} />
        </div>
      </div>
      {/* zoom window + leader lines down to the sample chips */}
      <div style={{ position: 'absolute', left: ZX, top: WTOP - 10, width: ZW, height: WH + 20, border: `4px solid ${ACC}`,
        borderRadius: 8, opacity: zoom * (1 - style * 0.6) }} />
      <svg width={CW} height={1080} style={{ position: 'absolute', left: 0, top: 0, opacity: zoom * (1 - style * 0.6) }}>
        <line x1={ZX} y1={WTOP + WH + 10} x2={SX} y2={CTOP - 10} stroke={ACC} strokeWidth={3} strokeDasharray="10 8" />
        <line x1={ZX + ZW} y1={WTOP + WH + 10} x2={SX + p.samples.length * (chipW + chipGap) - chipGap} y2={CTOP - 10}
          stroke={ACC} strokeWidth={3} strokeDasharray="10 8" />
      </svg>
      <div style={{ position: 'absolute', left: SX, top: CTOP, display: 'flex', gap: chipGap }}>
        {p.samples.map((v, i) => {
          const o = rise(t, p.zoomAt + i * 0.006);
          return (
            <div key={i} style={{ width: chipW, height: 74, boxSizing: 'border-box', background: CARD, border: `2px solid ${BORDER}`,
              borderRadius: 10, display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: MONO, fontSize: 35,
              color: INK, opacity: o }}>{fmt(v)}</div>
          );
        })}
      </div>
      <div style={{ position: 'absolute', left: SX, top: CTOP + 110, fontFamily: SERIF, fontSize: 62, color: ACC_TEXT, opacity: rate }}>
        {p.sampleRate.toLocaleString('en-US')} numbers every second</div>
      <div style={{ position: 'absolute', right: SX, top: CTOP + 116, fontFamily: SERIF, fontSize: 56, color: SOFT, opacity: net }}>
        a neural network predicts each one</div>
      {/* the voice = a style list */}
      <div style={{ position: 'absolute', left: SX, top: 720, width: WW, height: 190, boxSizing: 'border-box', background: CARD,
        border: `${swap > 0.5 ? 4 : 2}px solid ${swap > 0.5 ? ACC : INK}`, borderRadius: 20, padding: '26px 36px', opacity: style,
        transform: `translateY(${(1 - style) * 24}px)` }}>
        <div style={{ fontFamily: SERIF, fontSize: 52, color: INK }}>
          {who}’s voice = <span style={{ color: SOFT }}>a list of {p.styleSize} numbers</span></div>
        <div style={{ display: 'flex', gap: 16, marginTop: 18, fontFamily: MONO, fontSize: 34, color: swap > 0.5 ? ACC_TEXT : INK }}>
          {sty.map((v, i) => <span key={`${who}${i}`}>{fmt(v)}</span>)}<span style={{ color: SOFT }}>…</span>
        </div>
      </div>
      <Footnote text={p.footnote} o={rise(t, p.zoomAt)} />
      <HaiBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// TtvDemo — real Kokoro output on the tricky lines: text → phonemes, the wrong
// part marked, what it said. Then Bella's and another voice's waveforms with
// one chip: different voice, same mistakes.
// ===========================================================================
export const ttvDemoSchema = z.object({
  spark: z.string().default(''),
  rows: z.array(z.object({ text: z.string(), hot: z.string(), phonemes: z.string(), bad: z.string(), badShort: z.string().default(''), said: z.string(), at: z.number() })),
  bellaEnvelope: z.array(z.number()),
  otherEnvelope: z.array(z.number()),
  bellaLabel: z.string().default('Bella'),
  otherLabel: z.string().default('Michael'),
  chip: z.string(),
  voicesAt: z.number().default(0.7),
  footnote: z.string().default(''),
  footnoteShort: z.string().default(''),
  ...dur,
});
const splitOn = (s: string, k: string) => {
  const i = s.indexOf(k);
  return i < 0 ? [s, '', ''] : [s.slice(0, i), k, s.slice(i + k.length)];
};
export const TtvDemo: React.FC<z.infer<typeof ttvDemoSchema>> = (p) => {
  const t = useT();
  const TOP = 140, ROW = 160, vo = rise(t, p.voicesAt), VW = 780;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <Spark line={p.spark} o={rise(t, 0)} />
      {p.rows.map((r, i) => {
        const o = rise(t, r.at), x = rise(t, r.at + FADE * 1.5);
        const [a, b, c] = splitOn(r.text, r.hot);
        const [pa, pb, pc] = splitOn(r.phonemes, r.bad);
        return (
          <div key={i} style={{ position: 'absolute', left: SX, top: TOP + i * ROW, width: CW - 2 * SX, height: ROW - 18, boxSizing: 'border-box',
            background: CARD, border: `2px solid ${BORDER}`, borderRadius: 18, display: 'flex', alignItems: 'center', padding: '0 36px',
            opacity: 0.2 + 0.8 * o }}>
            <div style={{ flex: 1 }}>
              <HotText parts={[a, b, c]} hot={[1]} size={52} o={x} />
              <div style={{ fontFamily: IPA, fontSize: 34, color: SOFT, marginTop: 6, whiteSpace: 'nowrap' }}>
                {pa}<span style={{ color: x > 0.5 ? ACC_TEXT : SOFT, fontWeight: 600, background: x > 0.5 ? '#F6E3DB' : 'none',
                  borderRadius: 6, padding: '0 6px' }}>{pb}</span>{pc}
              </div>
            </div>
            <div style={{ fontFamily: SERIF, fontSize: 50, color: ACC_TEXT, textAlign: 'right', whiteSpace: 'nowrap', opacity: x }}>
              <span style={{ fontFamily: SANS, fontWeight: 800, marginRight: 16 }}>✕</span>{r.said}</div>
          </div>
        );
      })}
      {[{ env: p.bellaEnvelope, lab: p.bellaLabel, x: SX, c: INK }, { env: p.otherEnvelope, lab: p.otherLabel, x: CW - SX - VW, c: ACC_TEXT }].map((v, i) => (
        <div key={i} style={{ position: 'absolute', left: v.x, top: 650, opacity: rise(t, p.voicesAt + i * 0.03) }}>
          <div style={{ fontFamily: SERIF, fontSize: 46, color: INK, marginBottom: 8 }}>{v.lab} <span style={{ color: SOFT, fontSize: 36 }}>· “I read it yesterday.”</span></div>
          <Waveform env={v.env} w={VW} h={130} color={v.c} />
        </div>
      ))}
      <div style={{ position: 'absolute', left: 0, right: 0, top: 870, display: 'flex', justifyContent: 'center', opacity: rise(t, p.voicesAt + 0.08) }}>
        <div style={{ border: `5px solid ${ACC_TEXT}`, color: ACC_TEXT, fontFamily: SERIF, fontSize: 52, padding: '6px 34px', borderRadius: 14 }}>{p.chip}</div>
      </div>
      <Footnote text={p.footnote} o={rise(t, 0.05) * (1 - vo * 0)} />
      <HaiBug />
    </AbsoluteFill>
  );
};


// ===========================================================================
// TtvSpokenLines — the narration itself, word for word: each word fades in on
// its MEASURED start time (faster-whisper), so what's on screen is exactly what
// Bella says, when she says it. Accent words carry the one terracotta.
// ===========================================================================
export const ttvSpokenLinesSchema = z.object({
  lines: z.array(z.array(z.object({ w: z.string(), at: z.number(), accent: z.boolean().default(false) }))),
  fontSize: z.number().default(70),
  ...dur,
});
const SpokenWords: React.FC<{ lines: z.infer<typeof ttvSpokenLinesSchema>['lines']; t: number; size: number; lead: number; align: 'left' | 'center' }> =
  ({ lines, t, size, lead, align }) => (
    <div style={{ textAlign: align }}>
      {lines.map((ln, i) => (
        <div key={i} style={{ fontFamily: SERIF, fontSize: size, lineHeight: lead, color: INK }}>
          {ln.map((w, j) => {
            const o = rise(t, w.at, FADE * 0.6);
            return (
              <span key={j} style={{ opacity: 0.12 + 0.88 * o, color: w.accent && o > 0.5 ? ACC_TEXT : INK }}>
                {w.w}{j < ln.length - 1 ? ' ' : ''}</span>
            );
          })}
        </div>
      ))}
    </div>
  );
export const TtvSpokenLines: React.FC<z.infer<typeof ttvSpokenLinesSchema>> = (p) => {
  const t = useT();
  return (
    <AbsoluteFill style={{ background: BG, justifyContent: 'center', padding: `0 ${SX + 40}px` }}>
      <SpokenWords lines={p.lines} t={t} size={p.fontSize} lead={1.45} align="left" />
      <HaiBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// PORTRAIT (9:16) VARIANTS — native 1080×1920, registered as <Name>916. Same
// schemas and cue props. Phone-size type: serif >= 92, sans/mono >= 72 design px.
// SHOW LESS: no spark lines; phoneme rows show only the wrong part.
// Safe area x 54–1026, y 96–1824.
// ===========================================================================
const PW = 1080, PX = 54, PY = 96, PSERIF = 92, PSANS = 72;
const PIW = PW - 2 * PX;

const PBug: React.FC = () => (
  <Img src={staticFile('logos/humanitarians/humanitarians-logo-1.svg')}
    style={{ position: 'absolute', right: PX, bottom: PY, height: 60, opacity: 0.32 }} />
);
const PFoot: React.FC<{ text: string; o: number }> = ({ text, o }) =>
  text ? (
    <div style={{ position: 'absolute', left: PX, right: PX + 90, bottom: PY, fontFamily: SANS, fontSize: PSANS,
      lineHeight: 1.12, color: SOFT, opacity: o }}>{text}</div>
  ) : null;

export const TtvTrickyLines916: React.FC<z.infer<typeof ttvTrickyLinesSchema>> = (p) => {
  const t = useT();
  const TOP = PY + 60, ROW = 560;
  return (
    <AbsoluteFill style={{ background: BG }}>
      {p.lines.map((l, i) => {
        const o = rise(t, l.at), hot = rise(t, l.at + FADE * 1.5);
        return (
          <div key={i} style={{ position: 'absolute', left: PX, width: PIW, top: TOP + i * ROW, opacity: o, whiteSpace: 'normal' }}>
            <div style={{ fontFamily: SERIF, fontSize: PSERIF + 4, lineHeight: 1.12, color: INK }}>
              {l.parts.map((s, j) => l.hot.includes(j)
                ? <span key={j} style={{ color: hot > 0.5 ? ACC_TEXT : INK, textDecoration: hot > 0.5 ? 'underline' : 'none',
                    textDecorationThickness: 6, textUnderlineOffset: 12 }}>{s}</span>
                : <span key={j}>{s}</span>)}
            </div>
            <div style={{ fontFamily: SERIF, fontStyle: 'italic', fontSize: PSERIF, color: ACC_TEXT, marginTop: 18, opacity: hot }}>{l.note}</div>
          </div>
        );
      })}
      <PBug />
    </AbsoluteFill>
  );
};

export const TtvPipeline916: React.FC<z.infer<typeof ttvPipelineSchema>> = (p) => {
  const t = useT();
  const n = p.steps.length, GAP = 56, TOP = PY + 20, H = (1780 - TOP - (n - 1) * GAP) / n;
  return (
    <AbsoluteFill style={{ background: BG }}>
      {p.steps.map((s, i) => {
        const o = rise(t, p.stepAt[i] ?? 0), y = TOP + i * (H + GAP);
        const ex = s.example;
        return (
          <React.Fragment key={i}>
            <div style={{ position: 'absolute', left: PX, top: y, width: PIW, height: H, boxSizing: 'border-box', background: CARD,
              borderRadius: 22, border: `2px solid ${o > 0.5 ? INK : BORDER}`, opacity: 0.25 + 0.75 * o, padding: '30px 40px' }}>
              <div style={{ display: 'flex', alignItems: 'baseline', gap: 28 }}>
                <span style={{ fontFamily: SANS, fontSize: PSANS, color: SOFT }}>{i + 1}</span>
                <span style={{ fontFamily: SERIF, fontSize: PSERIF + 8, color: INK, lineHeight: 1 }}>{s.name}</span>
              </div>
              <div style={{ position: 'absolute', left: 40, right: 40, bottom: 30, height: 120, opacity: o }}>
                {ex === 'bars' ? <TimingBars w={PIW - 80} h={110} o={o} />
                  : ex === 'wave' ? <Waveform env={p.envelope} w={PIW - 80} h={110} color={ACC_TEXT} reveal={o} />
                  : <div style={{ fontFamily: i === 1 ? IPA : SERIF, fontSize: i === 1 ? PSANS : PSERIF, color: ACC_TEXT, lineHeight: 1.1 }}>{ex}</div>}
              </div>
            </div>
            {i < n - 1 ? (
              <div style={{ position: 'absolute', left: 0, right: 0, top: y + H - 4, height: GAP, textAlign: 'center', fontFamily: SANS,
                fontSize: 56, lineHeight: `${GAP}px`, color: rise(t, p.stepAt[i + 1] ?? 1) > 0.5 ? INK : GHOST }}>↓</div>
            ) : null}
          </React.Fragment>
        );
      })}
      <PBug />
    </AbsoluteFill>
  );
};

export const TtvWave916: React.FC<z.infer<typeof ttvWaveSchema>> = (p) => {
  const t = useT();
  const wave = rise(t, p.waveAt, FADE * 3), zoom = rise(t, p.zoomAt), rate = rise(t, p.rateAt), net = rise(t, p.netAt);
  const style = rise(t, p.styleAt), swap = rise(t, p.swapAt);
  const WH = 300, WTOP = PY + 20;
  const sty = (swap > 0.5 ? p.otherStyle : p.bellaStyle).slice(0, 4);
  const who = swap > 0.5 ? p.otherLabel : p.bellaLabel;
  const samples = p.samples.slice(0, 4);
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: PX, top: WTOP, opacity: wave }}>
        <div style={{ position: 'absolute', opacity: 1 - swap }}><Waveform env={p.envelope} w={PIW} h={WH} color={INK} reveal={wave} /></div>
        <div style={{ position: 'absolute', opacity: swap }}><Waveform env={p.otherEnvelope} w={PIW} h={WH} color={ACC_TEXT} /></div>
      </div>
      <div style={{ position: 'absolute', left: PX, top: WTOP + WH + 50, width: PIW, display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 20 }}>
        {samples.map((v, i) => (
          <div key={i} style={{ height: 110, boxSizing: 'border-box', background: CARD, border: `2px solid ${BORDER}`, borderRadius: 12,
            display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: MONO, fontSize: PSANS, color: INK,
            opacity: rise(t, p.zoomAt + i * 0.01) * (1 - style * 0.5) }}>{fmt(v)}</div>
        ))}
      </div>
      <div style={{ position: 'absolute', left: PX, right: PX, top: 830, fontFamily: SERIF, fontSize: PSERIF + 8, lineHeight: 1.02,
        color: ACC_TEXT, opacity: rate * (1 - style * 0.5) }}>{p.sampleRate.toLocaleString('en-US')} per second</div>
      <div style={{ position: 'absolute', left: PX, right: PX, top: 960, fontFamily: SERIF, fontSize: PSERIF, lineHeight: 1.05,
        color: SOFT, opacity: net * (1 - style * 0.5) }}>a neural network predicts each one</div>
      <div style={{ position: 'absolute', left: PX, top: 1230, width: PIW, boxSizing: 'border-box', background: CARD,
        border: `${swap > 0.5 ? 6 : 2}px solid ${swap > 0.5 ? ACC : INK}`, borderRadius: 22, padding: '34px 40px', opacity: style }}>
        <div style={{ fontFamily: SERIF, fontSize: PSERIF, lineHeight: 1.05, color: INK }}>{who}’s voice =</div>
        <div style={{ fontFamily: SERIF, fontSize: PSERIF, lineHeight: 1.05, color: SOFT }}>{p.styleSize} numbers</div>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '6px 20px', marginTop: 20, fontFamily: MONO, fontSize: PSANS,
          color: swap > 0.5 ? ACC_TEXT : INK }}>
          {sty.map((v, i) => <span key={`${who}${i}`}>{fmt(v)}</span>)}
        </div>
      </div>
      <PBug />
    </AbsoluteFill>
  );
};

export const TtvDemo916: React.FC<z.infer<typeof ttvDemoSchema>> = (p) => {
  const t = useT();
  const TOP = PY + 10, ROW = 330;
  return (
    <AbsoluteFill style={{ background: BG }}>
      {p.rows.map((r, i) => {
        const o = rise(t, r.at), x = rise(t, r.at + FADE * 1.5);
        const [a, b, c] = splitOn(r.text, r.hot);
        return (
          <div key={i} style={{ position: 'absolute', left: PX, top: TOP + i * ROW, width: PIW, height: ROW - 30, boxSizing: 'border-box',
            background: CARD, border: `2px solid ${BORDER}`, borderRadius: 20, padding: '24px 36px', opacity: 0.2 + 0.8 * o }}>
            <div style={{ fontFamily: SERIF, fontSize: PSERIF - 4, lineHeight: 1.05, color: INK, whiteSpace: 'nowrap' }}>
              {a}<span style={{ color: x > 0.5 ? ACC_TEXT : INK, textDecoration: x > 0.5 ? 'underline' : 'none', textDecorationThickness: 6,
                textUnderlineOffset: 10 }}>{b}</span>{c}</div>
            <div style={{ display: 'flex', alignItems: 'baseline', gap: 24, marginTop: 26, opacity: x, whiteSpace: 'nowrap' }}>
              <span style={{ fontFamily: IPA, fontSize: PSANS, color: ACC_TEXT, fontWeight: 600 }}>{r.badShort || r.bad}</span>
              <span style={{ fontFamily: SERIF, fontSize: PSERIF - 4, color: ACC_TEXT }}>✕ {r.said.replace(/^said /, '')}</span>
            </div>
          </div>
        );
      })}
      {[{ env: p.bellaEnvelope, lab: p.bellaLabel, c: INK }, { env: p.otherEnvelope, lab: p.otherLabel, c: ACC_TEXT }].map((v, i) => (
        <div key={i} style={{ position: 'absolute', left: PX, top: 1130 + i * 230, opacity: rise(t, p.voicesAt + i * 0.03) }}>
          <div style={{ fontFamily: SERIF, fontSize: PSERIF - 4, color: INK, lineHeight: 1 }}>{v.lab}</div>
          <Waveform env={v.env} w={PIW} h={120} color={v.c} style={{ marginTop: 10 }} />
        </div>
      ))}
      <div style={{ position: 'absolute', left: PX, right: PX + 90, top: 1600, fontFamily: SERIF, fontSize: PSERIF, lineHeight: 1.04,
        color: ACC_TEXT, opacity: rise(t, p.voicesAt + 0.08) }}>{p.chip}</div>
      <PBug />
    </AbsoluteFill>
  );
};

export const TtvSpokenLines916: React.FC<z.infer<typeof ttvSpokenLinesSchema>> = (p) => {
  const t = useT();
  return (
    <AbsoluteFill style={{ background: BG, justifyContent: 'center', padding: `0 ${PX}px` }}>
      <SpokenWords lines={p.lines} t={t} size={PSERIF + 4} lead={1.22} align="left" />
      <PBug />
    </AbsoluteFill>
  );
};
