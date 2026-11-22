import React from 'react';
import { AbsoluteFill, Img, useCurrentFrame, useVideoConfig, spring, interpolate, staticFile } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { CC_FONT } from '../tokens/claudecode';

/**
 * Trust in LLMs — concept beats for "Can You Trust Your AI? How We Test Large Language Models"
 * (ai-explainer, claude-hai). Every component lays itself out for 16:9 (1920x1080) or 9:16 (1080x1920)
 * from useVideoConfig, so the same component backs the landscape id and its *916 id.
 *
 *   TrustHallucination   a question, a confident wrong answer, the HALLUCINATION stamp, the truth
 *   TrustThreeProblems   three icon cards (hallucination · bias · black box) + one analogy line
 *   TrustToolbox         the evaluation toolbox: N tool tiles, each lit on its spoken name
 *   TrustOverlap         a word-overlap score (ROUGE-1) for two answers against one reference
 *   TrustBenchAB         benchmark (same test, every model) beside A/B (two versions, same prompts)
 *   TrustCounterfactual  swap one detail in a prompt, compare the two answers
 *   TrustEmbedding       real 2-D embedding points, clusters, a query word and its nearest neighbour
 *   TrustReasoning       an explanation's steps, the faulty step flagged, black box → glass box
 *   TrustCredit          the source-paper credit card
 *
 * Reveals are driven by `cues` (seconds from the start of the beat), authored from the narration.
 * Palette: the Claude fidelity palette; terracotta is the one accent. Brand: handle / logo props.
 */

const brand = {
  handle: z.string().default('@HumanitariansAI'),
  logo: z.string().optional(),
};
const BrandCtx = React.createContext<{ handle: string; logo?: string }>({ handle: '@HumanitariansAI' });

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const MONO = CC_FONT.mono;
const WARN = '#A44A32';

function useClock() {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const portrait = height > width;
  const reveal = (at: number | undefined, soft = false) =>
    at === undefined ? 1 : Math.min(1, spring({ frame: frame - Math.round(at * fps), fps,
      config: soft ? { damping: 30, stiffness: 80, mass: 1 } : { damping: 22, stiffness: 140, mass: 0.7 } }));
  return { frame, fps, width, height, portrait, t: frame / fps, reveal };
}

// Portrait design constants: GATE T's portrait floor is ~68 px type on the 1080x1920 canvas, and the
// bottom 14% is platform UI, so portrait content stays inside y 160-1650.
const P = { title: 86, big: 80, body: 68, x0: 54, x1: 1026, top: 160, bottom: 1650 };

const Bug: React.FC = () => {
  const { handle, logo } = React.useContext(BrandCtx);
  const { width, height, portrait } = useClock();
  if (portrait) {
    return logo
      ? <Img src={staticFile(logo)} style={{ position: 'absolute', right: 64, top: 104, height: 30, opacity: 0.45 }} />
      : <div style={{ position: 'absolute', right: 64, top: 104, fontFamily: SANS, fontSize: 30, color: CLAUDE.INK_SOFT, opacity: 0.4 }}>{handle}</div>;
  }
  return logo
    ? <Img src={staticFile(logo)} style={{ position: 'absolute', right: width * 0.05, bottom: height * 0.05, height: 34, opacity: 0.45 }} />
    : <div style={{ position: 'absolute', right: width * 0.05, bottom: height * 0.05, fontFamily: SANS, fontSize: 26,
        fontWeight: 600, color: CLAUDE.INK_SOFT, opacity: 0.35 }}>{handle}</div>;
};

const Card: React.FC<{ style?: React.CSSProperties; children?: React.ReactNode }> = ({ style, children }) => (
  <div style={{ background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 22,
    boxShadow: '0 8px 24px rgba(61,57,41,0.08)', boxSizing: 'border-box', ...style }}>{children}</div>
);

const Title: React.FC<{ text: string }> = ({ text }) => {
  const { width, height, portrait } = useClock();
  return portrait
    ? <div style={{ position: 'absolute', left: P.x0, right: 1080 - P.x1, top: P.top + 40, fontFamily: SERIF, fontSize: P.title,
        color: CLAUDE.INK, lineHeight: 1.08, textAlign: 'center' }}>{text}</div>
    : <div style={{ position: 'absolute', left: width * 0.06, right: width * 0.06, top: height * 0.075, fontFamily: SERIF,
        fontSize: 64, color: CLAUDE.INK, lineHeight: 1.1 }}>{text}</div>;
};

const Note: React.FC<{ text?: string; top?: number }> = ({ text, top }) => {
  const { width, height, portrait } = useClock();
  if (!text) return null;
  return portrait
    ? <div style={{ position: 'absolute', left: P.x0, right: 1080 - P.x1, top: top ?? 1560, fontFamily: SANS, fontSize: 40,
        color: CLAUDE.INK_SOFT, textAlign: 'center', lineHeight: 1.2 }}>{text}</div>
    : <div style={{ position: 'absolute', left: width * 0.06, bottom: height * 0.05, maxWidth: width * 0.62, fontFamily: SANS,
        fontSize: 26, color: CLAUDE.INK_SOFT, lineHeight: 1.25 }}>{text}</div>;
};

const Quote: React.FC<{ text: string; source: string; o: number; style?: React.CSSProperties; portrait: boolean }> = ({ text, source, o, style, portrait }) => (
  <Card style={{ opacity: o, transform: `translateY(${(1 - o) * 20}px)`, borderLeft: `10px solid ${CLAUDE.SPARK}`,
    padding: portrait ? '26px 32px' : '22px 30px', ...style }}>
    <div style={{ fontFamily: SERIF, fontSize: portrait ? 64 : 40, color: CLAUDE.INK, lineHeight: 1.15 }}>“{text}”</div>
    <div style={{ fontFamily: SANS, fontSize: portrait ? 40 : 24, color: CLAUDE.INK_SOFT, marginTop: 10 }}>{source}</div>
  </Card>
);

const withBrand = <T extends { handle?: string; logo?: string }>(Inner: React.FC<T>): React.FC<T> => (props) => (
  <BrandCtx.Provider value={{ handle: props.handle ?? '@HumanitariansAI', logo: props.logo }}>
    <Inner {...props} />
  </BrandCtx.Provider>
);

const cueAt = (cues: number[], i: number) => (cues[i] ?? 0);

const pick = <T,>(L: React.FC<T>, Pv: React.FC<T>): React.FC<T> => (props) => {
  const { width, height } = useVideoConfig();
  return height > width ? <Pv {...(props as any)} /> : <L {...(props as any)} />;
};

// ─────────────────────────────────────────────────────────────────────────────
// 1. TrustHallucination — cues: [question, answer, stamp, truth]

export const trustHallucinationSchema = z.object({
  question: z.string().default('What temperature does water boil at on top of Mount Everest?'),
  answer: z.string().default('Water boils at 100 °C, the same as at sea level.'),
  stamp: z.string().default('HALLUCINATION'),
  truth: z.string().default('About 70 °C: the air is thinner, so water boils sooner.'),
  note: z.string().default(''),
  noteShort: z.string().default(''),
  cues: z.array(z.number()).default([0.5, 2, 5, 7]),
  durationSeconds: z.number().optional(),
  ...brand,
});

const HallucinationInner: React.FC<z.infer<typeof trustHallucinationSchema>> = ({ question, answer, stamp, truth, note, cues }) => {
  const { t, portrait, width, reveal } = useClock();
  const qIn = reveal(cueAt(cues, 0));
  const typed = interpolate(t, [cueAt(cues, 1), cueAt(cues, 1) + Math.max(1.2, answer.length / 28)], [0, answer.length],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const stampIn = reveal(cueAt(cues, 2));
  const truthIn = reveal(cueAt(cues, 3));
  const L = portrait
    ? { q: { left: 140, right: 54, top: 260, fs: 64 }, a: { left: 54, right: 54, top: 640, h: 520, fs: 80 }, tr: { top: 1220, fs: 64 }, stampFs: 96 }
    : { q: { left: width * 0.3, right: width * 0.06, top: 110, fs: 50 }, a: { left: width * 0.06, right: width * 0.14, top: 300, h: 470, fs: 72 }, tr: { top: 830, fs: 58 }, stampFs: 110 };
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <div style={{ position: 'absolute', left: L.q.left, right: L.q.right, top: L.q.top, opacity: qIn, display: 'flex', justifyContent: 'flex-end' }}>
        <div style={{ background: CLAUDE.PILL, borderRadius: 26, padding: portrait ? '24px 34px' : '18px 28px', fontFamily: SANS,
          fontSize: L.q.fs, color: CLAUDE.INK, lineHeight: 1.2 }}>{question}</div>
      </div>
      <Card style={{ position: 'absolute', left: L.a.left, right: L.a.right, top: L.a.top, height: L.a.h, padding: portrait ? '34px 40px' : '30px 40px',
        opacity: typed > 0 ? 1 : 0 }}>
        <div style={{ display: 'flex', gap: 18, alignItems: 'flex-start' }}>
          <span style={{ color: CLAUDE.SPARK, fontSize: portrait ? 70 : 48, lineHeight: 1 }}>✻</span>
          <div style={{ fontFamily: SERIF, fontSize: L.a.fs, color: CLAUDE.INK, lineHeight: 1.2 }}>{answer.slice(0, Math.round(typed))}</div>
        </div>
        <div style={{ position: 'absolute', left: '50%', top: portrait ? '62%' : '70%', transform: `translate(-50%,-50%) rotate(-8deg) scale(${1.6 - 0.6 * stampIn})`,
          opacity: stampIn, border: `10px solid ${WARN}`, borderRadius: 14, padding: '6px 26px', fontFamily: SANS, fontWeight: 800,
          fontSize: L.stampFs, letterSpacing: 6, color: WARN, background: 'rgba(250,249,245,0.82)', whiteSpace: 'nowrap' }}>{stamp}</div>
      </Card>
      <div style={{ position: 'absolute', left: portrait ? P.x0 : width * 0.06, right: portrait ? 1080 - P.x1 : width * 0.14, top: L.tr.top,
        opacity: truthIn, transform: `translateY(${(1 - truthIn) * 20}px)`, display: 'flex', gap: 18, alignItems: 'baseline' }}>
        <span style={{ fontFamily: SANS, fontWeight: 800, fontSize: L.tr.fs, color: CLAUDE.INK }}>✓</span>
        <span style={{ fontFamily: SANS, fontSize: L.tr.fs, color: CLAUDE.INK, lineHeight: 1.2 }}>{truth}</span>
      </div>
      <Note text={note} />
      <Bug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// 2. TrustThreeProblems — cues: [item0, item1, item2, analogy]

const Icon: React.FC<{ kind: string; size: number; on: boolean }> = ({ kind, size, on }) => {
  const ink = CLAUDE.INK, soft = CLAUDE.INK_SOFT, acc = on ? CLAUDE.SPARK : soft;
  return (
    <svg width={size} height={size} viewBox="0 0 100 100">
      {kind === 'hallucination' && (<>
        <path d="M14 22 h72 a8 8 0 0 1 8 8 v34 a8 8 0 0 1 -8 8 h-40 l-18 16 v-16 h-14 a8 8 0 0 1 -8 -8 v-34 a8 8 0 0 1 8 -8z" fill={CLAUDE.CARD} stroke={ink} strokeWidth={5} />
        <text x="50" y="58" textAnchor="middle" fontFamily={SERIF} fontSize="34" fill={acc}>?!</text>
      </>)}
      {kind === 'bias' && (<>
        <line x1="50" y1="14" x2="50" y2="84" stroke={ink} strokeWidth={5} />
        <line x1="20" y1="30" x2="80" y2="42" stroke={ink} strokeWidth={5} />
        <path d="M8 56 l12 -26 l12 26 z" fill={CLAUDE.CARD} stroke={ink} strokeWidth={4} />
        <path d="M68 68 l12 -26 l12 26 z" fill={acc} stroke={ink} strokeWidth={4} />
        <line x1="30" y1="86" x2="70" y2="86" stroke={ink} strokeWidth={6} />
      </>)}
      {kind === 'blackbox' && (<>
        <path d="M18 34 l32 -16 l32 16 v40 l-32 16 l-32 -16z" fill={ink} />
        <path d="M18 34 l32 16 l32 -16 M50 50 v40" stroke={CLAUDE.INK_SOFT} strokeWidth={3} fill="none" />
        <text x="50" y="44" textAnchor="middle" fontFamily={SERIF} fontSize="22" fill={acc}>?</text>
      </>)}
    </svg>
  );
};

export const trustThreeProblemsSchema = z.object({
  title: z.string().default('Why We Can’t Just Trust It'),
  items: z.array(z.object({ label: z.string(), detail: z.string(), icon: z.string() })).default([]),
  analogy: z.string().default(''),
  cues: z.array(z.number()).default([]),
  durationSeconds: z.number().optional(),
  ...brand,
});

const ThreeProblemsInner: React.FC<z.infer<typeof trustThreeProblemsSchema>> = ({ title, items, analogy, cues }) => {
  const { t, portrait, width, height, reveal } = useClock();
  const n = items.length;
  const active = cues.slice(0, n).reduce((k, c, i) => (t >= c ? i : k), -1);
  const anIn = reveal(cues[n]);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title text={title} />
      {items.map((it, i) => {
        const o = reveal(cues[i]);
        const on = i === active && t < (cues[n] ?? 1e9);
        const box = portrait
          ? { left: P.x0, width: P.x1 - P.x0, top: 360 + i * 330, height: 300 }
          : { left: width * 0.06 + i * (width * 0.88 + 36) / n, width: (width * 0.88 - 36 * (n - 1)) / n, top: height * 0.2, height: height * 0.54 };
        return (
          <Card key={it.label} style={{ position: 'absolute', ...box, opacity: 0.25 + 0.75 * o, transform: `translateY(${(1 - o) * 30}px)`,
            border: `3px solid ${on ? CLAUDE.INK : CLAUDE.BORDER}`, borderBottom: `${on ? 12 : 3}px solid ${on ? CLAUDE.SPARK : CLAUDE.BORDER}`,
            display: 'flex', flexDirection: portrait ? 'row' : 'column', alignItems: 'center', justifyContent: 'center', gap: portrait ? 30 : 22,
            padding: portrait ? '0 34px' : '34px 30px', textAlign: portrait ? 'left' : 'center' }}>
            <Icon kind={it.icon} size={portrait ? 190 : 230} on={on} />
            <div>
              <div style={{ fontFamily: SERIF, fontSize: portrait ? P.big : 64, color: CLAUDE.INK, lineHeight: 1.05 }}>{it.label}</div>
              <div style={{ fontFamily: SANS, fontSize: portrait ? 48 : 38, color: CLAUDE.INK_SOFT, marginTop: 10, lineHeight: 1.2 }}>{it.detail}</div>
            </div>
          </Card>
        );
      })}
      <div style={{ position: 'absolute', left: portrait ? P.x0 : width * 0.06, right: portrait ? 1080 - P.x1 : width * 0.06,
        top: portrait ? 1390 : height * 0.8, opacity: anIn, transform: `translateY(${(1 - anIn) * 16}px)`, display: 'flex',
        justifyContent: 'center', alignItems: 'center', gap: 16 }}>
        <span style={{ color: CLAUDE.SPARK, fontSize: portrait ? 60 : 44 }}>✻</span>
        <span style={{ fontFamily: SERIF, fontSize: portrait ? 64 : 56, color: CLAUDE.INK, textAlign: 'center', lineHeight: 1.15 }}>{analogy}</span>
      </div>
      <Bug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// 3. TrustToolbox — cues: one per tool, then [all]

export const trustToolboxSchema = z.object({
  title: z.string().default('The Evaluation Toolbox'),
  tools: z.array(z.object({ label: z.string(), detail: z.string(), tag: z.string().optional() })).default([]),
  footnote: z.string().default(''),
  cues: z.array(z.number()).default([]),
  durationSeconds: z.number().optional(),
  ...brand,
});

const ToolboxInner: React.FC<z.infer<typeof trustToolboxSchema>> = ({ title, tools, footnote, cues }) => {
  const { t, portrait, width, height, reveal } = useClock();
  const n = tools.length;
  const all = t >= (cues[n] ?? 1e9);
  const active = all ? -1 : cues.slice(0, n).reduce((k, c, i) => (t >= c ? i : k), -1);
  const cols = portrait ? 2 : 3;
  const rows = Math.ceil(n / cols);
  const g = portrait ? 28 : 28;
  const area = portrait ? { x: P.x0, y: 380, w: P.x1 - P.x0, h: 1140 } : { x: width * 0.06, y: height * 0.21, w: width * 0.88, h: height * 0.6 };
  const cw = (area.w - g * (cols - 1)) / cols, ch = (area.h - g * (rows - 1)) / rows;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title text={title} />
      {tools.map((tool, i) => {
        const o = reveal(cues[i]);
        const on = i === active;
        const c = i % cols, r = Math.floor(i / cols);
        return (
          <Card key={tool.label} style={{ position: 'absolute', left: area.x + c * (cw + g), top: area.y + r * (ch + g), width: cw, height: ch,
            opacity: 0.25 + 0.75 * o, transform: `scale(${0.96 + 0.04 * o})`, padding: portrait ? '26px 26px' : '24px 30px',
            border: `3px solid ${on || (all && o > 0.5) ? CLAUDE.INK : CLAUDE.BORDER}`,
            borderBottom: `${on ? 12 : 3}px solid ${on ? CLAUDE.SPARK : (all ? CLAUDE.INK : CLAUDE.BORDER)}`,
            display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
            <div style={{ fontFamily: SANS, fontSize: portrait ? 44 : 26, color: CLAUDE.INK_SOFT, fontWeight: 700, letterSpacing: 2 }}>{String(i + 1).padStart(2, '0')}</div>
            <div style={{ fontFamily: SERIF, fontSize: portrait ? 68 : 52, color: CLAUDE.INK, lineHeight: 1.05, marginTop: 6 }}>{tool.label}</div>
            {!portrait && <div style={{ fontFamily: SANS, fontSize: 30, color: CLAUDE.INK_SOFT, marginTop: 10, lineHeight: 1.2 }}>{tool.detail}</div>}
            {tool.tag && <div style={{ fontFamily: SANS, fontSize: portrait ? 40 : 24, color: CLAUDE.INK_SOFT, marginTop: 8, fontStyle: 'italic' }}>{tool.tag}</div>}
          </Card>
        );
      })}
      <Note text={footnote} />
      <Bug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// 4. TrustOverlap — cues: [reference, row0, score0, row1, score1, lesson]

export const trustOverlapSchema = z.object({
  title: z.string().default('Scoring Against a Reference'),
  metric: z.string().default('ROUGE-1 · shared words'),
  reference: z.array(z.string()).default([]),
  rows: z.array(z.object({ label: z.string(), tokens: z.array(z.string()), matched: z.array(z.string()), score: z.number(),
    verdict: z.enum(['wrong', 'right']) })).default([]),
  lesson: z.string().default(''),
  quote: z.string().default(''),
  quoteSource: z.string().default(''),
  note: z.string().default(''),
  noteShort: z.string().default(''),
  cues: z.array(z.number()).default([]),
  durationSeconds: z.number().optional(),
  ...brand,
});

const Chips: React.FC<{ tokens: string[]; matched: string[]; fs: number; showMatch: number }> = ({ tokens, matched, fs, showMatch }) => {
  const pool = [...matched];
  return (
    <div style={{ display: 'flex', flexWrap: 'wrap', gap: fs * 0.25 }}>
      {tokens.map((w, i) => {
        const k = pool.indexOf(w);
        const hit = k >= 0;
        if (hit) pool.splice(k, 1);
        const on = hit && showMatch > 0.5;
        return (
          <span key={i} style={{ fontFamily: MONO, fontSize: fs, padding: `${fs * 0.08}px ${fs * 0.3}px`, borderRadius: fs * 0.25,
            color: on ? CLAUDE.PAGE : CLAUDE.INK, background: on ? CLAUDE.INK : CLAUDE.PILL }}>{w}</span>
        );
      })}
    </div>
  );
};

const OverlapInner: React.FC<z.infer<typeof trustOverlapSchema>> = ({ title, metric, reference, rows, lesson, quote, quoteSource, note, cues }) => {
  const { t, portrait, width, height, reveal } = useClock();
  const refIn = reveal(cues[0]);
  const lessonIn = reveal(cues[5]);
  const fs = portrait ? 46 : 30;
  const bar = (score: number, at: number) => {
    const p = interpolate(t, [at, at + 1.2], [0, score], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
    return p;
  };
  const X0 = portrait ? P.x0 : width * 0.06, W = portrait ? P.x1 - P.x0 : width * 0.88;
  const y0 = portrait ? 350 : height * 0.185;
  const rowH = portrait ? 440 : 225;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title text={title} />
      <div style={{ position: 'absolute', left: X0, width: W, top: y0, opacity: refIn }}>
        <div style={{ fontFamily: SANS, fontSize: portrait ? 44 : 26, color: CLAUDE.INK_SOFT, marginBottom: 10 }}>Reference answer · {metric}</div>
        <Chips tokens={reference} matched={[]} fs={fs} showMatch={0} />
      </div>
      {rows.map((r, i) => {
        const o = reveal(cues[1 + 2 * i]);
        const sAt = cues[2 + 2 * i] ?? 1e9;
        const p = bar(r.score, sAt);
        const shown = t >= sAt;
        const top = y0 + (portrait ? 300 : 150) + i * rowH;
        return (
          <Card key={r.label} style={{ position: 'absolute', left: X0, width: W, top, height: rowH - (portrait ? 30 : 22), opacity: o,
            padding: portrait ? '20px 28px' : '16px 26px', transform: `translateY(${(1 - o) * 20}px)` }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline' }}>
              <div style={{ fontFamily: SERIF, fontSize: portrait ? 60 : 38, color: CLAUDE.INK }}>{r.label}</div>
              <div style={{ fontFamily: SANS, fontWeight: 800, fontSize: portrait ? 52 : 34, opacity: shown ? 1 : 0,
                color: r.verdict === 'wrong' ? WARN : CLAUDE.INK }}>{r.verdict === 'wrong' ? '✕ wrong' : '✓ right'}</div>
            </div>
            <div style={{ marginTop: 10 }}><Chips tokens={r.tokens} matched={r.matched} fs={fs} showMatch={shown ? 1 : 0} /></div>
            <div style={{ display: 'flex', alignItems: 'center', gap: 20, marginTop: portrait ? 18 : 12 }}>
              <div style={{ flex: 1, height: portrait ? 34 : 24, background: CLAUDE.PILL, borderRadius: 20, overflow: 'hidden' }}>
                <div style={{ width: `${p * 100}%`, height: '100%', background: i === 0 ? CLAUDE.SPARK : CLAUDE.INK_SOFT }} />
              </div>
              <div style={{ fontFamily: MONO, fontWeight: 700, fontSize: portrait ? 64 : 42, color: CLAUDE.INK, width: portrait ? 190 : 120, textAlign: 'right' }}>{p.toFixed(2)}</div>
            </div>
          </Card>
        );
      })}
      {portrait ? (
        <div style={{ position: 'absolute', left: P.x0, right: 1080 - P.x1, top: 1440, opacity: lessonIn, fontFamily: SERIF, fontSize: 64,
          color: CLAUDE.INK, textAlign: 'center', lineHeight: 1.15 }}><span style={{ color: CLAUDE.SPARK }}>✻ </span>{lesson}</div>
      ) : (
        <div style={{ position: 'absolute', left: X0, width: W - 230, top: y0 + 150 + 2 * rowH + 4, display: 'flex', gap: 30, alignItems: 'stretch', opacity: lessonIn }}>
          <div style={{ flex: '0 0 38%', fontFamily: SERIF, fontSize: 44, color: CLAUDE.INK, lineHeight: 1.15, alignSelf: 'center' }}>
            <span style={{ color: CLAUDE.SPARK }}>✻ </span>{lesson}</div>
          {quote && <Quote text={quote} source={quoteSource} o={lessonIn} portrait={false} style={{ flex: 1 }} />}
        </div>
      )}
      {!portrait && <Note text={note} />}
      <Bug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// 5. TrustBenchAB — cues: [bench, models, leaderboard, ab, prefer, warning]

export const trustBenchABSchema = z.object({
  title: z.string().default('Same Test, Fair Comparison'),
  benchLabel: z.string().default('Benchmark'),
  benchDetail: z.string().default('same questions · same scoring · every model'),
  models: z.array(z.string()).default(['Model A', 'Model B', 'Model C']),
  abLabel: z.string().default('A/B test'),
  abDetail: z.string().default('two versions · same prompts · side by side'),
  prompts: z.number().default(5),
  prefer: z.array(z.enum(['A', 'B'])).default(['B', 'A', 'B', 'B', 'A']),
  quote: z.string().default(''),
  quoteSource: z.string().default(''),
  note: z.string().default(''),
  noteShort: z.string().default(''),
  cues: z.array(z.number()).default([]),
  durationSeconds: z.number().optional(),
  ...brand,
});

const BenchABInner: React.FC<z.infer<typeof trustBenchABSchema>> = ({ title, benchLabel, benchDetail, models, abLabel, abDetail, prompts, prefer, quote, quoteSource, note, cues }) => {
  const { t, portrait, width, height, reveal } = useClock();
  const [cBench, cModels, cBoard, cAB, cPrefer, cWarn] = cues;
  const benchIn = reveal(cBench), modelsIn = reveal(cModels), boardIn = reveal(cBoard), abIn = reveal(cAB), warnIn = reveal(cWarn);
  const panel = portrait
    ? { a: { left: P.x0, top: 330, width: P.x1 - P.x0, height: 560 }, b: { left: P.x0, top: 920, width: P.x1 - P.x0, height: 500 } }
    : { a: { left: width * 0.06, top: height * 0.2, width: width * 0.42, height: height * 0.5 }, b: { left: width * 0.52, top: height * 0.2, width: width * 0.42, height: height * 0.5 } };
  const big = portrait ? 72 : 58, body = portrait ? 46 : 38;
  const nPref = prefer.filter((_, i) => t >= (cPrefer ?? 1e9) + i * 0.5).length;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title text={title} />
      <Card style={{ position: 'absolute', ...panel.a, opacity: 0.25 + 0.75 * benchIn, padding: portrait ? '24px 30px' : '24px 30px' }}>
        <div style={{ fontFamily: SERIF, fontSize: big, color: CLAUDE.INK }}>{benchLabel}</div>
        <div style={{ fontFamily: SANS, fontSize: body, color: CLAUDE.INK_SOFT, marginTop: 4 }}>{benchDetail}</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 16 : 12, marginTop: portrait ? 24 : 22 }}>
          {models.map((m, i) => {
            const o = Math.min(1, Math.max(0, (t - (cModels ?? 1e9)) / 0.4 - i * 0.6));
            const w = [0.72, 0.58, 0.81][i % 3];
            const rank = [2, 3, 1][i % 3];
            return (
              <div key={m} style={{ display: 'flex', alignItems: 'center', gap: 16, marginTop: portrait ? 0 : 14, opacity: 0.2 + 0.8 * Math.min(1, o) * modelsIn }}>
                <div style={{ fontFamily: SANS, fontSize: body, color: CLAUDE.INK, width: portrait ? 240 : 150 }}>{m}</div>
                <div style={{ flex: 1, height: 24, background: CLAUDE.PILL, borderRadius: 20, overflow: 'hidden' }}>
                  <div style={{ width: `${w * Math.min(1, o) * 100}%`, height: '100%', background: rank === 1 && boardIn > 0.5 ? CLAUDE.SPARK : CLAUDE.INK_SOFT }} />
                </div>
                <div style={{ fontFamily: SANS, fontWeight: 800, fontSize: body, color: CLAUDE.INK, width: portrait ? 80 : 54, opacity: boardIn }}>#{rank}</div>
              </div>
            );
          })}
        </div>
      </Card>
      <Card style={{ position: 'absolute', ...panel.b, opacity: 0.25 + 0.75 * abIn, padding: '24px 30px' }}>
        <div style={{ fontFamily: SERIF, fontSize: big, color: CLAUDE.INK }}>{abLabel}</div>
        <div style={{ fontFamily: SANS, fontSize: body, color: CLAUDE.INK_SOFT, marginTop: 4 }}>{abDetail}</div>
        <div style={{ display: 'flex', gap: portrait ? 14 : 12, marginTop: portrait ? 26 : 26, flexWrap: 'wrap' }}>
          {Array.from({ length: prompts }).map((_, i) => {
            const decided = i < nPref;
            return (
              <div key={i} style={{ width: portrait ? 172 : 136, height: portrait ? 172 : 190, borderRadius: 16, border: `3px solid ${CLAUDE.BORDER}`,
                background: CLAUDE.FOOTER, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                <div style={{ fontFamily: SANS, fontSize: portrait ? 40 : 28, color: CLAUDE.INK_SOFT }}>prompt {i + 1}</div>
                <div style={{ fontFamily: SANS, fontWeight: 800, fontSize: portrait ? 64 : 64, color: CLAUDE.INK, opacity: decided ? 1 : 0.2 }}>{decided ? prefer[i] : 'A|B'}</div>
              </div>
            );
          })}
        </div>
      </Card>
      {quote && (
        <div style={{ position: 'absolute', left: portrait ? P.x0 : width * 0.06, right: portrait ? 1080 - P.x1 : width * 0.06,
          top: portrait ? 1440 : height * 0.74 }}>
          <Quote text={quote} source={quoteSource} o={warnIn} portrait={portrait} />
        </div>
      )}
      {!portrait && <Note text={note} />}
      <Bug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// 6. TrustCounterfactual — cues: [template, swap, answers, compare, verdict]

export const trustCounterfactualSchema = z.object({
  title: z.string().default('Swap One Detail'),
  before: z.string().default('Write a reference letter for '),
  after: z.string().default(', a nurse.'),
  names: z.array(z.string()).default(['Emily', 'Jamal']),
  checks: z.array(z.object({ label: z.string(), a: z.string(), b: z.string(), same: z.boolean() })).default([]),
  verdict: z.string().default(''),
  source: z.string().default(''),
  note: z.string().default(''),
  noteShort: z.string().default(''),
  cues: z.array(z.number()).default([]),
  durationSeconds: z.number().optional(),
  ...brand,
});

const CounterfactualInner: React.FC<z.infer<typeof trustCounterfactualSchema>> = ({ title, before, after, names, checks, verdict, source, note, cues }) => {
  const { t, portrait, width, height, reveal } = useClock();
  const [cTpl, cSwap, cAns, cCmp, cVerdict] = cues;
  const tplIn = reveal(cTpl), ansIn = reveal(cAns), vIn = reveal(cVerdict);
  const swapped = t >= (cSwap ?? 1e9);
  const flip = interpolate(t, [cSwap ?? 1e9, (cSwap ?? 1e9) + 0.5], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const big = portrait ? 64 : 62, body = portrait ? 50 : 42;
  const X0 = portrait ? P.x0 : width * 0.06, W = portrait ? P.x1 - P.x0 : width * 0.88;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title text={title} />
      <Card style={{ position: 'absolute', left: X0, width: W, top: portrait ? 340 : height * 0.2, padding: portrait ? '26px 30px' : '22px 34px', opacity: tplIn }}>
        <div style={{ fontFamily: SANS, fontSize: portrait ? 40 : 24, color: CLAUDE.INK_SOFT }}>Same prompt, one detail changed</div>
        <div style={{ fontFamily: SERIF, fontSize: big, color: CLAUDE.INK, marginTop: 6, lineHeight: 1.2 }}>
          {before}
          <span style={{ display: 'inline-block', borderBottom: `6px solid ${CLAUDE.SPARK}`, padding: '0 6px' }}>
            {swapped ? `${names[0]} → ${names[1]}` : names[0]}
          </span>{after}
        </div>
      </Card>
      {[0, 1].map((k) => {
        const box = portrait
          ? { left: P.x0, width: (P.x1 - P.x0 - 24) / 2, top: 640 + 0, height: 160 }
          : { left: width * 0.06 + k * (width * 0.44 + 0), width: width * 0.42, top: height * 0.4, height: 110 };
        const left = portrait ? P.x0 + k * ((P.x1 - P.x0 + 24) / 2) : box.left;
        const o = k === 0 ? ansIn : ansIn * flip;
        return (
          <Card key={k} style={{ position: 'absolute', left, width: box.width, top: box.top, height: box.height, opacity: 0.15 + 0.85 * o,
            display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SERIF, fontSize: big, color: CLAUDE.INK }}>
            Letter for {names[k]}
          </Card>
        );
      })}
      <div style={{ position: 'absolute', left: X0, width: W, top: portrait ? 830 : height * 0.55 }}>
        {checks.map((c, i) => {
          const o = Math.min(1, Math.max(0, (t - (cCmp ?? 1e9)) / 0.4 - i * 0.7));
          return (
            <div key={c.label} style={{ display: 'grid', gridTemplateColumns: portrait ? '1fr' : '0.9fr 1fr 1fr 0.3fr', gap: portrait ? 4 : 16,
              alignItems: 'center', padding: portrait ? '12px 0' : '8px 0', borderBottom: `2px solid ${CLAUDE.BORDER}`, opacity: o }}>
              <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: body, color: CLAUDE.INK }}>{c.label}{portrait ? (c.same ? '  ✓' : '  ✕') : ''}</div>
              <div style={{ fontFamily: SANS, fontSize: body, color: CLAUDE.INK_SOFT }}>{portrait ? `${c.a}  ·  ${c.b}` : c.a}</div>
              {!portrait && <div style={{ fontFamily: SANS, fontSize: body, color: c.same ? CLAUDE.INK_SOFT : WARN }}>{c.b}</div>}
              {!portrait && <div style={{ fontFamily: SANS, fontWeight: 800, fontSize: body, color: c.same ? CLAUDE.INK : WARN }}>{c.same ? '✓' : '✕'}</div>}
            </div>
          );
        })}
      </div>
      <div style={{ position: 'absolute', left: X0, width: W, top: portrait ? 1390 : height * 0.8, opacity: vIn, display: 'flex', gap: 16,
        alignItems: 'baseline', justifyContent: portrait ? 'center' : 'flex-start' }}>
        <span style={{ color: CLAUDE.SPARK, fontSize: portrait ? 60 : 42 }}>✻</span>
        <span style={{ fontFamily: SERIF, fontSize: portrait ? 62 : 54, color: CLAUDE.INK, lineHeight: 1.15, textAlign: portrait ? 'center' : 'left' }}>{verdict}</span>
      </div>
      {!portrait && source && <div style={{ position: 'absolute', right: width * 0.06, top: height * 0.075 + 20, fontFamily: SANS, fontSize: 26, color: CLAUDE.INK_SOFT }}>{source}</div>}
      <Note text={note} />
      <Bug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// 7. TrustEmbedding — cues: [points, clusters, query, neighbour]

export const trustEmbeddingSchema = z.object({
  title: z.string().default('Words as Points in Space'),
  points: z.array(z.object({ word: z.string(), group: z.string(), x: z.number(), y: z.number() })).default([]),
  labelSide: z.record(z.string(), z.enum(['left', 'right', 'above', 'below'])).default({}),
  groupLabels: z.record(z.string(), z.string()).default({}),
  groupBelow: z.array(z.string()).default([]),
  query: z.string().default('kitten'),
  neighbour: z.object({ word: z.string(), cosine: z.number() }).default({ word: 'cat', cosine: 0.79 }),
  far: z.object({ word: z.string(), cosine: z.number() }).default({ word: 'guitar', cosine: 0.25 }),
  note: z.string().default(''),
  noteShort: z.string().default(''),
  cues: z.array(z.number()).default([]),
  durationSeconds: z.number().optional(),
  ...brand,
});

const EmbeddingInner: React.FC<z.infer<typeof trustEmbeddingSchema>> = ({ title, points, labelSide, groupLabels, query, neighbour, far, note, cues }) => {
  const { t, portrait, width, height, reveal } = useClock();
  const [cPts, cClu, cQ, cN] = cues;
  const cluIn = reveal(cClu), qIn = reveal(cQ), nIn = reveal(cN);
  const area = portrait ? { x: 90, y: 360, w: 900, h: 880 } : { x: width * 0.06, y: height * 0.19, w: width * 0.58, h: height * 0.7 };
  const xs = points.map((p) => p.x), ys = points.map((p) => p.y);
  const [minX, maxX, minY, maxY] = [Math.min(...xs), Math.max(...xs), Math.min(...ys), Math.max(...ys)];
  const pad = 0.1;
  const sx = (x: number) => area.x + area.w * (pad + (1 - 2 * pad) * (x - minX) / Math.max(1e-6, maxX - minX));
  const sy = (y: number) => area.y + area.h * (pad + (1 - 2 * pad) * (1 - (y - minY) / Math.max(1e-6, maxY - minY)));
  const groups = Array.from(new Set(points.filter((p) => p.group !== 'query').map((p) => p.group)));
  const fs = portrait ? 46 : 30;
  const q = points.find((p) => p.group === 'query');
  const nb = points.find((p) => p.word === neighbour.word);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title text={title} />
      <Card style={{ position: 'absolute', left: area.x - 20, top: area.y - 20, width: area.w + 40, height: area.h + 40, background: CLAUDE.CARD }} />
      <svg width={width} height={height} style={{ position: 'absolute', inset: 0 }}>
        {groups.map((g) => {
          const gp = points.filter((p) => p.group === g);
          const cx = gp.reduce((s, p) => s + sx(p.x), 0) / gp.length, cy = gp.reduce((s, p) => s + sy(p.y), 0) / gp.length;
          const rx = Math.max(...gp.map((p) => Math.abs(sx(p.x) - cx))) + (portrait ? 120 : 110);
          const ry = Math.max(...gp.map((p) => Math.abs(sy(p.y) - cy))) + (portrait ? 70 : 50);
          return <ellipse key={g} cx={cx} cy={cy} rx={rx} ry={ry} fill={CLAUDE.FOOTER} stroke={CLAUDE.INK_SOFT} strokeWidth={3}
            strokeDasharray="10 8" opacity={cluIn} />;
        })}
        {q && nb && <line x1={sx(q.x)} y1={sy(q.y)} x2={sx(nb.x)} y2={sy(nb.y)} stroke={CLAUDE.SPARK} strokeWidth={6} opacity={nIn} />}
      </svg>
      {groups.map((g) => {
        const gp = points.filter((p) => p.group === g);
        const cx = gp.reduce((s, p) => s + sx(p.x), 0) / gp.length;
        const top = Math.min(...gp.map((p) => sy(p.y))) - (portrait ? 120 : 90);
        return <div key={g} style={{ position: 'absolute', left: cx, top, transform: 'translateX(-50%)', fontFamily: SERIF,
          fontSize: portrait ? 50 : 36, color: CLAUDE.INK, opacity: cluIn, whiteSpace: 'nowrap' }}>{groupLabels[g] ?? g}</div>;
      })}
      {points.map((p, i) => {
        const isQ = p.group === 'query';
        const o = isQ ? qIn : Math.min(1, Math.max(0, (t - (cPts ?? 0)) / 0.25 - i * 0.12));
        return (
          <React.Fragment key={p.word}>
            <div style={{ position: 'absolute', left: sx(p.x), top: sy(p.y), width: isQ ? 26 : 18, height: isQ ? 26 : 18, borderRadius: '50%',
              transform: `translate(-50%,-50%) scale(${0.6 + 0.4 * o})`, opacity: o, background: isQ ? CLAUDE.SPARK : CLAUDE.INK }} />
            {(() => {
              const side = labelSide[p.word] ?? 'right';
              const d = isQ ? 22 : 16;
              const tr = { right: `translate(${d}px,-50%)`, left: `translate(calc(-100% - ${d}px),-50%)`,
                above: `translate(-50%,calc(-100% - ${d - 6}px))`, below: `translate(-50%,${d - 6}px)` }[side];
              return <span style={{ position: 'absolute', left: sx(p.x), top: sy(p.y), transform: tr, opacity: o, whiteSpace: 'nowrap',
                fontFamily: MONO, fontSize: isQ ? fs * 1.1 : fs * 0.85, fontWeight: isQ ? 700 : 400, color: CLAUDE.INK,
                background: isQ ? CLAUDE.CARD : 'transparent', padding: isQ ? '0 8px' : 0, borderRadius: 8 }}>{p.word}</span>;
            })()}
          </React.Fragment>
        );
      })}
      <div style={{ position: 'absolute', left: portrait ? P.x0 : width * 0.66, right: portrait ? 1080 - P.x1 : width * 0.06,
        top: portrait ? 1290 : height * 0.24, display: 'flex', flexDirection: 'column', gap: portrait ? 14 : 22 }}>
        {[{ w: neighbour.word, c: neighbour.cosine, on: true }, { w: far.word, c: far.cosine, on: false }].map((r) => (
          <Card key={r.w} style={{ padding: portrait ? '14px 26px' : '20px 26px', opacity: nIn, borderLeft: `10px solid ${r.on ? CLAUDE.SPARK : CLAUDE.BORDER}` }}>
            <div style={{ fontFamily: MONO, fontSize: portrait ? 50 : 34, color: CLAUDE.INK }}>{query} ~ {r.w}</div>
            <div style={{ fontFamily: SANS, fontSize: portrait ? 44 : 30, color: CLAUDE.INK_SOFT, marginTop: 4 }}>similarity {r.c.toFixed(2)}</div>
          </Card>
        ))}
      </div>
      <Note text={note} />
      <Bug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// 8. TrustReasoning — cues: one per step, then [flag, glass, caution]

export const trustReasoningSchema = z.object({
  title: z.string().default('Ask It to Show Its Work'),
  steps: z.array(z.object({ text: z.string(), bad: z.boolean().default(false), fix: z.string().optional() })).default([]),
  glassLabel: z.string().default('black box → glass box'),
  quote: z.string().default(''),
  quoteSource: z.string().default(''),
  note: z.string().default(''),
  noteShort: z.string().default(''),
  cues: z.array(z.number()).default([]),
  durationSeconds: z.number().optional(),
  ...brand,
});

const ReasoningInner: React.FC<z.infer<typeof trustReasoningSchema>> = ({ title, steps, glassLabel, quote, quoteSource, note, cues }) => {
  const { t, portrait, width, height, reveal } = useClock();
  const n = steps.length;
  const cFlag = cues[n], cGlass = cues[n + 1], cCaution = cues[n + 2];
  const flagged = t >= (cFlag ?? 1e9);
  const glass = interpolate(t, [cGlass ?? 1e9, (cGlass ?? 1e9) + 1.4], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const cauIn = reveal(cCaution);
  const X0 = portrait ? P.x0 : width * 0.06, W = portrait ? P.x1 - P.x0 : width * 0.56;
  const stepH = portrait ? 200 : 160;
  const box = portrait ? { x: 540, y: 1180, s: 230 } : { x: width * 0.8, y: height * 0.4, s: 330 };
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Title text={title} />
      {steps.map((s, i) => {
        const o = reveal(cues[i]);
        const bad = s.bad && flagged;
        return (
          <Card key={i} style={{ position: 'absolute', left: X0, width: W, top: (portrait ? 330 : height * 0.2) + i * (stepH + (portrait ? 18 : 16)),
            height: stepH, opacity: 0.2 + 0.8 * o, padding: portrait ? '16px 26px' : '14px 26px', display: 'flex', alignItems: 'center', gap: 20,
            border: `3px solid ${bad ? WARN : CLAUDE.BORDER}` }}>
            <div style={{ fontFamily: SANS, fontWeight: 800, fontSize: portrait ? 56 : 36, color: bad ? WARN : CLAUDE.INK_SOFT, width: portrait ? 60 : 40 }}>{i + 1}</div>
            <div style={{ flex: 1 }}>
              <div style={{ fontFamily: SANS, fontSize: portrait ? 50 : 46, color: CLAUDE.INK, lineHeight: 1.18,
                textDecoration: bad ? `line-through ${WARN} 4px` : 'none' }}>{s.text}</div>
              {bad && s.fix && <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: portrait ? 46 : 44, color: CLAUDE.INK, marginTop: 4 }}>✓ {s.fix}</div>}
            </div>
          </Card>
        );
      })}
      <div style={{ position: 'absolute', left: box.x, top: box.y, transform: 'translate(-50%,-50%)', opacity: portrait ? (glass > 0 ? 1 : 0) : 1 }}>
        <svg width={box.s} height={box.s} viewBox="0 0 100 100">
          <path d="M14 30 l36 -18 l36 18 v44 l-36 18 l-36 -18z" fill={CLAUDE.INK} fillOpacity={1 - 0.88 * glass} stroke={CLAUDE.INK} strokeWidth={3} />
          <path d="M14 30 l36 18 l36 -18 M50 48 v44" stroke={glass > 0.5 ? CLAUDE.INK : CLAUDE.INK_SOFT} strokeWidth={2} fill="none" />
          {[0, 1, 2].map((k) => (
            <circle key={k} cx={34 + k * 16} cy={58 + (k % 2) * 8} r={5} fill={CLAUDE.SPARK} opacity={glass} />
          ))}
          <path d="M34 58 L50 66 L66 58" stroke={CLAUDE.SPARK} strokeWidth={2} fill="none" opacity={glass} />
        </svg>
        <div style={{ fontFamily: SERIF, fontSize: portrait ? 56 : 46, color: CLAUDE.INK, textAlign: 'center', marginTop: 8, whiteSpace: 'nowrap' }}>{glassLabel}</div>
      </div>
      {quote && (
        <div style={{ position: 'absolute', left: portrait ? P.x0 : width * 0.06, right: portrait ? 1080 - P.x1 : width * 0.06,
          top: portrait ? 1420 : height * 0.75 }}>
          <Quote text={quote} source={quoteSource} o={cauIn} portrait={portrait} />
        </div>
      )}
      {!portrait && <Note text={note} />}
      <Bug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// 9. TrustCredit — cues: [paper, author, id, kind]

export const trustCreditSchema = z.object({
  kicker: z.string().default('Based on'),
  paper: z.string().default('Enhancing Trust in LLMs: Algorithms for Comparing and Interpreting LLMs'),
  author: z.string().default('Nik Bear Brown'),
  id: z.string().default('arXiv 2406.01943 · 2024'),
  kind: z.string().default('A survey of evaluation techniques. The examples in this video are ours.'),
  cues: z.array(z.number()).default([]),
  durationSeconds: z.number().optional(),
  ...brand,
});

const CreditInner: React.FC<z.infer<typeof trustCreditSchema>> = ({ kicker, paper, author, id, kind, cues }) => {
  const { portrait, width, reveal } = useClock();
  const [c0, c1, c2, c3] = cues;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Card style={{ position: 'absolute', left: '50%', top: portrait ? 860 : '50%', transform: 'translate(-50%,-50%)', width: portrait ? P.x1 - P.x0 : width * 0.84, padding: portrait ? '60px 50px' : '70px 90px', borderTop: `12px solid ${CLAUDE.SPARK}` }}>
        <div style={{ fontFamily: SANS, fontSize: portrait ? 48 : 30, color: CLAUDE.INK_SOFT, letterSpacing: 2, opacity: reveal(c0) }}>{kicker}</div>
        <div style={{ fontFamily: SERIF, fontSize: portrait ? 80 : 76, color: CLAUDE.INK, lineHeight: 1.12, marginTop: 14, opacity: reveal(c0) }}>{paper}</div>
        <div style={{ fontFamily: SERIF, fontSize: portrait ? 72 : 64, color: CLAUDE.INK, marginTop: 30, opacity: reveal(c1) }}>{author}</div>
        <div style={{ fontFamily: MONO, fontSize: portrait ? 54 : 46, color: CLAUDE.INK, marginTop: 14, opacity: reveal(c2) }}>{id}</div>
        <div style={{ fontFamily: SANS, fontSize: portrait ? 48 : 38, color: CLAUDE.INK_SOFT, marginTop: 30, lineHeight: 1.25, opacity: reveal(c3) }}>{kind}</div>
      </Card>
      <Bug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// Portrait (9:16) views. GATE T measures each word's ink height, so a lowercase-only word reads at its
// x-height: on the 1080x1920 canvas serif text needs ~90 px and sans ~72 px to clear the 72 px (3840) floor.
// Each view keeps the beat's single idea at that size; secondary detail stays in the 16:9 cut and the voice.

const Q = { serif: 92, sans: 72, mono: 70 };
const sec = (src: string) => { const m = src.match(/§\s*\d+/); return m ? `survey ${m[0]}` : src; };

const PT: React.FC<{ text: string }> = ({ text }) => (
  <div style={{ position: 'absolute', left: P.x0, right: 1080 - P.x1, top: P.top + 30, fontFamily: SERIF, fontSize: Q.serif,
    color: CLAUDE.INK, lineHeight: 1.05, textAlign: 'center' }}>{text}</div>
);
const PNote: React.FC<{ text?: string; top?: number }> = ({ text, top = 1560 }) => text
  ? <div style={{ position: 'absolute', left: P.x0, right: 1080 - P.x1, top, fontFamily: SANS, fontSize: Q.sans, color: CLAUDE.INK_SOFT, textAlign: 'center' }}>{text}</div>
  : null;
const PQuote: React.FC<{ text: string; source: string; o: number; top: number }> = ({ text, source, o, top }) => (
  <Card style={{ position: 'absolute', left: P.x0, width: P.x1 - P.x0, top, opacity: o, borderLeft: `12px solid ${CLAUDE.SPARK}`, padding: '24px 30px' }}>
    <div style={{ fontFamily: SERIF, fontSize: Q.serif, color: CLAUDE.INK, lineHeight: 1.08 }}>“{text}”</div>
    <div style={{ fontFamily: SANS, fontSize: Q.sans, color: CLAUDE.INK_SOFT, marginTop: 8 }}>{sec(source)}</div>
  </Card>
);

const HallucinationP: React.FC<z.infer<typeof trustHallucinationSchema>> = ({ question, answer, stamp, truth, note, noteShort, cues }) => {
  const { t, reveal } = useClock();
  const typed = interpolate(t, [cueAt(cues, 1), cueAt(cues, 1) + Math.max(1.2, answer.length / 28)], [0, answer.length], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const stampIn = reveal(cueAt(cues, 2)), truthIn = reveal(cueAt(cues, 3));
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <div style={{ position: 'absolute', left: 120, right: P.x0, top: 230, opacity: reveal(cueAt(cues, 0)), background: CLAUDE.PILL, borderRadius: 30,
        padding: '22px 32px', fontFamily: SANS, fontSize: Q.sans, color: CLAUDE.INK, lineHeight: 1.15 }}>{question}</div>
      <Card style={{ position: 'absolute', left: P.x0, width: P.x1 - P.x0, top: 650, height: 640, padding: '30px 36px', opacity: typed > 0 ? 1 : 0 }}>
        <div style={{ fontFamily: SERIF, fontSize: Q.serif, color: CLAUDE.INK, lineHeight: 1.12 }}><span style={{ color: CLAUDE.SPARK }}>✻ </span>{answer.slice(0, Math.round(typed))}</div>
        <div style={{ position: 'absolute', left: '50%', bottom: 50, transform: `translateX(-50%) rotate(-6deg) scale(${1.6 - 0.6 * stampIn})`, opacity: stampIn,
          border: `10px solid ${WARN}`, borderRadius: 14, padding: '4px 22px', fontFamily: SANS, fontWeight: 800, fontSize: 84, letterSpacing: 4, color: WARN, whiteSpace: 'nowrap' }}>{stamp}</div>
      </Card>
      <div style={{ position: 'absolute', left: P.x0, right: 1080 - P.x1, top: 1330, opacity: truthIn, fontFamily: SANS, fontSize: Q.sans, color: CLAUDE.INK, lineHeight: 1.15 }}>✓ {truth}</div>
      <PNote text={noteShort || note} />
      <Bug />
    </AbsoluteFill>
  );
};

const ThreeProblemsP: React.FC<z.infer<typeof trustThreeProblemsSchema>> = ({ title, items, analogy, cues }) => {
  const { t, reveal } = useClock();
  const n = items.length;
  const active = cues.slice(0, n).reduce((k, c, i) => (t >= c ? i : k), -1);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <PT text={title} />
      {items.map((it, i) => {
        const o = reveal(cues[i]); const on = i === active && t < (cues[n] ?? 1e9);
        return (
          <Card key={it.label} style={{ position: 'absolute', left: P.x0, width: P.x1 - P.x0, top: 290 + i * 340, height: 325, opacity: 0.25 + 0.75 * o,
            display: 'flex', alignItems: 'center', gap: 26, padding: '0 30px', border: `3px solid ${on ? CLAUDE.INK : CLAUDE.BORDER}`,
            borderBottom: `${on ? 12 : 3}px solid ${on ? CLAUDE.SPARK : CLAUDE.BORDER}` }}>
            <Icon kind={it.icon} size={170} on={on} />
            <div>
              <div style={{ fontFamily: SERIF, fontSize: Q.serif, color: CLAUDE.INK, lineHeight: 1 }}>{it.label}</div>
              <div style={{ fontFamily: SANS, fontSize: Q.sans, color: CLAUDE.INK_SOFT, lineHeight: 1.1, marginTop: 6 }}>{it.detail}</div>
            </div>
          </Card>
        );
      })}
      <div style={{ position: 'absolute', left: P.x0, right: 1080 - P.x1, top: 1340, opacity: reveal(cues[n]), fontFamily: SERIF, fontSize: Q.serif,
        color: CLAUDE.INK, textAlign: 'center', lineHeight: 1.08 }}><span style={{ color: CLAUDE.SPARK }}>✻ </span>{analogy}</div>
      <Bug />
    </AbsoluteFill>
  );
};

const ToolboxP: React.FC<z.infer<typeof trustToolboxSchema>> = ({ title, tools, cues }) => {
  const { t, reveal } = useClock();
  const n = tools.length; const all = t >= (cues[n] ?? 1e9);
  const active = all ? -1 : cues.slice(0, n).reduce((k, c, i) => (t >= c ? i : k), -1);
  const h = 190, g = 18;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <PT text={title} />
      {tools.map((tool, i) => {
        const o = reveal(cues[i]); const on = i === active;
        return (
          <Card key={tool.label} style={{ position: 'absolute', left: P.x0, width: P.x1 - P.x0, top: 330 + i * (h + g), height: h, opacity: 0.25 + 0.75 * o,
            display: 'flex', alignItems: 'center', gap: 30, padding: '0 34px', border: `3px solid ${on || (all && o > 0.5) ? CLAUDE.INK : CLAUDE.BORDER}`,
            borderBottom: `${on ? 12 : 3}px solid ${on ? CLAUDE.SPARK : (all ? CLAUDE.INK : CLAUDE.BORDER)}` }}>
            <div style={{ fontFamily: SANS, fontWeight: 800, fontSize: Q.sans, color: CLAUDE.INK_SOFT, width: 110 }}>{String(i + 1).padStart(2, '0')}</div>
            <div style={{ fontFamily: SERIF, fontSize: Q.serif, color: CLAUDE.INK }}>{tool.label}{tool.label.startsWith('A/B') ? ' *' : ''}</div>
          </Card>
        );
      })}
      <PNote text={tools.some((x) => x.label.startsWith('A/B')) ? '* industry practice' : ''} top={1580} />
      <Bug />
    </AbsoluteFill>
  );
};

const OverlapP: React.FC<z.infer<typeof trustOverlapSchema>> = ({ rows, lesson, cues }) => {
  const { t, reveal } = useClock();
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      {rows.map((r, i) => {
        const o = reveal(cues[1 + 2 * i]); const sAt = cues[2 + 2 * i] ?? 1e9; const shown = t >= sAt;
        const p = interpolate(t, [sAt, sAt + 1.2], [0, r.score], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
        return (
          <Card key={r.label} style={{ position: 'absolute', left: P.x0, width: P.x1 - P.x0, top: 190 + i * 590, height: 560, opacity: 0.25 + 0.75 * o, padding: '18px 26px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline' }}>
              <div style={{ fontFamily: SERIF, fontSize: Q.serif, color: CLAUDE.INK }}>{r.verdict === 'wrong' ? '✕ Wrong' : '✓ Right'}</div>
              <div style={{ fontFamily: MONO, fontWeight: 700, fontSize: 92, color: r.verdict === 'wrong' ? WARN : CLAUDE.INK }}>{p.toFixed(2)}</div>
            </div>
            <div style={{ height: 30, background: CLAUDE.PILL, borderRadius: 15, overflow: 'hidden', margin: '8px 0 18px' }}>
              <div style={{ width: `${p * 100}%`, height: '100%', background: i === 0 ? CLAUDE.SPARK : CLAUDE.INK_SOFT }} />
            </div>
            <Chips tokens={r.tokens} matched={r.matched} fs={Q.mono} showMatch={shown ? 1 : 0} />
          </Card>
        );
      })}
      <div style={{ position: 'absolute', left: P.x0, right: 1080 - P.x1, top: 1390, opacity: reveal(cues[5]), fontFamily: SERIF, fontSize: Q.serif,
        color: CLAUDE.INK, textAlign: 'center', lineHeight: 1.05 }}><span style={{ color: CLAUDE.SPARK }}>✻ </span>{lesson}</div>
      <Bug />
    </AbsoluteFill>
  );
};

const BenchABP: React.FC<z.infer<typeof trustBenchABSchema>> = ({ benchLabel, models, abLabel, prompts, prefer, quote, quoteSource, noteShort, cues }) => {
  const { t, reveal } = useClock();
  const [cBench, cModels, cBoard, cAB, cPrefer, cWarn] = cues;
  const boardIn = reveal(cBoard);
  const nPref = prefer.filter((_, i) => t >= (cPrefer ?? 1e9) + i * 0.5).length;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Card style={{ position: 'absolute', left: P.x0, width: P.x1 - P.x0, top: 200, height: 470, opacity: 0.25 + 0.75 * reveal(cBench), padding: '22px 30px' }}>
        <div style={{ fontFamily: SERIF, fontSize: Q.serif, color: CLAUDE.INK }}>{benchLabel}</div>
        {models.map((m, i) => {
          const o = Math.min(1, Math.max(0, (t - (cModels ?? 1e9)) / 0.4 - i * 0.6));
          const w = [0.72, 0.58, 0.81][i % 3], rank = [2, 3, 1][i % 3];
          return (
            <div key={m} style={{ display: 'flex', alignItems: 'center', gap: 18, marginTop: 18, opacity: 0.2 + 0.8 * o }}>
              <div style={{ fontFamily: SANS, fontSize: Q.sans, color: CLAUDE.INK, width: 120 }}>{m.replace('Model ', '')}</div>
              <div style={{ flex: 1, height: 52, background: CLAUDE.PILL, borderRadius: 26, overflow: 'hidden', border: `4px solid ${rank === 1 && boardIn > 0.5 ? CLAUDE.INK : CLAUDE.PILL}` }}>
                <div style={{ width: `${w * o * 100}%`, height: '100%', background: rank === 1 && boardIn > 0.5 ? CLAUDE.INK : CLAUDE.INK_SOFT }} />
              </div>
              <div style={{ fontFamily: SANS, fontWeight: 800, fontSize: Q.sans, color: CLAUDE.INK, width: 100, opacity: boardIn }}>#{rank}</div>
            </div>
          );
        })}
      </Card>
      <Card style={{ position: 'absolute', left: P.x0, width: P.x1 - P.x0, top: 700, height: 360, opacity: 0.25 + 0.75 * reveal(cAB), padding: '22px 30px' }}>
        <div style={{ fontFamily: SERIF, fontSize: Q.serif, color: CLAUDE.INK }}>{abLabel}</div>
        <div style={{ display: 'flex', gap: 16, marginTop: 20 }}>
          {Array.from({ length: prompts }).map((_, i) => (
            <div key={i} style={{ flex: 1, height: 150, borderRadius: 16, border: `3px solid ${CLAUDE.BORDER}`, background: CLAUDE.FOOTER, display: 'flex',
              alignItems: 'center', justifyContent: 'center', fontFamily: SANS, fontWeight: 800, fontSize: 92, color: CLAUDE.INK, opacity: i < nPref ? 1 : 0.15 }}>{i < nPref ? prefer[i] : '?'}</div>
          ))}
        </div>
      </Card>
      {quote && <PQuote text={quote} source={quoteSource} o={reveal(cWarn)} top={1090} />}
      <PNote text={noteShort} top={1570} />
      <Bug />
    </AbsoluteFill>
  );
};

const CounterfactualP: React.FC<z.infer<typeof trustCounterfactualSchema>> = ({ before, after, names, checks, verdict, noteShort, note, cues }) => {
  const { t, reveal } = useClock();
  const [cTpl, cSwap, cAns, cCmp, cVerdict] = cues;
  const swapped = t >= (cSwap ?? 1e9);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Card style={{ position: 'absolute', left: P.x0, width: P.x1 - P.x0, top: 200, padding: '24px 30px', opacity: reveal(cTpl) }}>
        <div style={{ fontFamily: SERIF, fontSize: Q.serif, color: CLAUDE.INK, lineHeight: 1.1 }}>{before}
          <span style={{ borderBottom: `8px solid ${CLAUDE.SPARK}` }}>{swapped ? names[1] : names[0]}</span>{after}</div>
      </Card>
      <div style={{ position: 'absolute', left: P.x0, right: 1080 - P.x1, top: 690, display: 'flex', gap: 24, opacity: reveal(cAns) }}>
        {names.map((n2, k) => (
          <Card key={n2} style={{ flex: 1, height: 150, display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SERIF, fontSize: Q.serif,
            color: CLAUDE.INK, opacity: k === 0 || swapped ? 1 : 0.2 }}>{n2}</Card>
        ))}
      </div>
      <div style={{ position: 'absolute', left: P.x0 + 10, right: 1080 - P.x1 + 24, top: 880 }}>
        {checks.map((c, i) => {
          const o = Math.min(1, Math.max(0, (t - (cCmp ?? 1e9)) / 0.4 - i * 0.7));
          return (
            <div key={c.label} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '14px 0',
              borderBottom: `3px solid ${CLAUDE.BORDER}`, opacity: o }}>
              <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: Q.sans, color: c.same ? CLAUDE.INK : WARN }}>{c.label}</div>
              <div style={{ fontFamily: SANS, fontWeight: 800, fontSize: Q.sans, color: c.same ? CLAUDE.INK : WARN }}>{c.same ? 'same ✓' : 'differs ✕'}</div>
            </div>
          );
        })}
      </div>
      <div style={{ position: 'absolute', left: P.x0, right: 1080 - P.x1, top: 1260, opacity: reveal(cVerdict), fontFamily: SERIF, fontSize: Q.serif,
        color: CLAUDE.INK, textAlign: 'center', lineHeight: 1.05 }}><span style={{ color: CLAUDE.SPARK }}>✻ </span>{verdict}</div>
      <PNote text={noteShort || note} top={1570} />
      <Bug />
    </AbsoluteFill>
  );
};

const EmbeddingP: React.FC<z.infer<typeof trustEmbeddingSchema>> = ({ title, points, groupLabels, groupBelow, query, neighbour, far, noteShort, cues }) => {
  const { t, reveal } = useClock();
  const [cPts, cClu, cQ, cN] = cues;
  const cluIn = reveal(cClu), qIn = reveal(cQ), nIn = reveal(cN);
  const area = { x: 150, y: 430, w: 780, h: 700 };
  const xs = points.map((p) => p.x), ys = points.map((p) => p.y);
  const [minX, maxX, minY, maxY] = [Math.min(...xs), Math.max(...xs), Math.min(...ys), Math.max(...ys)];
  const sx = (x: number) => area.x + area.w * (0.12 + 0.76 * (x - minX) / Math.max(1e-6, maxX - minX));
  const sy = (y: number) => area.y + area.h * (0.12 + 0.76 * (1 - (y - minY) / Math.max(1e-6, maxY - minY)));
  const groups = Array.from(new Set(points.filter((p) => p.group !== 'query').map((p) => p.group)));
  const q = points.find((p) => p.group === 'query'); const nb = points.find((p) => p.word === neighbour.word);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <PT text={title} />
      <Card style={{ position: 'absolute', left: area.x - 56, top: area.y - 40, width: area.w + 112, height: area.h + 80 }} />
      <svg width={1080} height={1920} style={{ position: 'absolute', inset: 0 }}>
        {groups.map((g) => {
          const gp = points.filter((p) => p.group === g);
          const cx = gp.reduce((a, p) => a + sx(p.x), 0) / gp.length, cy = gp.reduce((a, p) => a + sy(p.y), 0) / gp.length;
          const rx = Math.max(...gp.map((p) => Math.abs(sx(p.x) - cx))) + 50, ry = Math.max(...gp.map((p) => Math.abs(sy(p.y) - cy))) + 50;
          return <ellipse key={g} cx={cx} cy={cy} rx={rx} ry={ry} fill={CLAUDE.FOOTER} stroke={CLAUDE.INK_SOFT} strokeWidth={4} strokeDasharray="12 10" opacity={cluIn} />;
        })}
        {q && nb && <line x1={sx(q.x)} y1={sy(q.y)} x2={sx(nb.x)} y2={sy(nb.y)} stroke={CLAUDE.SPARK} strokeWidth={8} opacity={nIn} />}
        {points.map((p, i) => {
          const isQ = p.group === 'query';
          const o = isQ ? qIn : Math.min(1, Math.max(0, (t - (cPts ?? 0)) / 0.25 - i * 0.12));
          return <circle key={p.word} cx={sx(p.x)} cy={sy(p.y)} r={isQ ? 24 : 20} fill={isQ ? CLAUDE.SPARK : CLAUDE.INK} opacity={o} />;
        })}
      </svg>
      {groups.map((g) => {
        const gp = points.filter((p) => p.group === g);
        const cx = gp.reduce((a, p) => a + sx(p.x), 0) / gp.length, cy = gp.reduce((a, p) => a + sy(p.y), 0) / gp.length;
        const below = groupBelow.includes(g);
        const top = below ? Math.max(...gp.map((p) => sy(p.y))) + 50 : Math.min(...gp.map((p) => sy(p.y))) - 50;
        return <div key={g} style={{ position: 'absolute', left: cx, top, transform: below ? 'translate(-50%,0)' : 'translate(-50%,-100%)', fontFamily: SERIF, fontSize: 96,
          color: CLAUDE.INK, opacity: cluIn, whiteSpace: 'nowrap', lineHeight: 1 }}>{groupLabels[g] ?? g}</div>;
      })}
      {q && <div style={{ position: 'absolute', left: sx(q.x) + 30, top: sy(q.y) + 24, opacity: qIn, fontFamily: MONO, fontWeight: 700,
        fontSize: Q.mono, color: CLAUDE.INK, background: CLAUDE.CARD, padding: '0 10px', borderRadius: 10 }}>{query}</div>}
      <div style={{ position: 'absolute', left: P.x0, right: 1080 - P.x1, top: 1210, display: 'flex', flexDirection: 'column', gap: 16, opacity: nIn }}>
        {[{ w: neighbour.word, c: neighbour.cosine, on: true }, { w: far.word, c: far.cosine, on: false }].map((r) => (
          <Card key={r.w} style={{ padding: '10px 26px', display: 'flex', justifyContent: 'space-between', borderLeft: `12px solid ${r.on ? CLAUDE.SPARK : CLAUDE.BORDER}` }}>
            <span style={{ fontFamily: MONO, fontSize: Q.mono, color: CLAUDE.INK }}>~ {r.w}</span>
            <span style={{ fontFamily: MONO, fontWeight: 700, fontSize: Q.mono, color: CLAUDE.INK }}>{r.c.toFixed(2)}</span>
          </Card>
        ))}
      </div>
      <PNote text={noteShort} top={1540} />
      <Bug />
    </AbsoluteFill>
  );
};

const ReasoningP: React.FC<z.infer<typeof trustReasoningSchema>> = ({ steps, glassLabel, quote, quoteSource, noteShort, cues }) => {
  const { t, reveal } = useClock();
  const n = steps.length; const cFlag = cues[n], cGlass = cues[n + 1], cCaution = cues[n + 2];
  const flagged = t >= (cFlag ?? 1e9);
  const glass = interpolate(t, [cGlass ?? 1e9, (cGlass ?? 1e9) + 1.4], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const cau = reveal(cCaution);
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <div style={{ position: 'absolute', left: P.x0, width: P.x1 - P.x0, top: 200, display: 'flex', flexDirection: 'column', gap: 18 }}>
      {steps.map((s2, i) => {
        const bad = s2.bad && flagged;
        return (
          <Card key={i} style={{ opacity: 0.2 + 0.8 * reveal(cues[i]), padding: '14px 26px', border: `4px solid ${bad ? WARN : CLAUDE.BORDER}` }}>
            <div style={{ fontFamily: SANS, fontSize: Q.sans, color: bad ? WARN : CLAUDE.INK, lineHeight: 1.08 }}>{bad ? '✕' : `${i + 1}.`} {s2.text}</div>
            {bad && s2.fix && <div style={{ fontFamily: SANS, fontWeight: 700, fontSize: Q.sans, color: CLAUDE.INK, lineHeight: 1.08, marginTop: 6 }}>✓ {s2.fix}</div>}
          </Card>
        );
      })}
      </div>
      <div style={{ position: 'absolute', left: 540, top: 1270, transform: 'translate(-50%,-50%)', opacity: glass * (1 - cau) }}>
        <svg width={260} height={260} viewBox="0 0 100 100" style={{ display: 'block', margin: '0 auto' }}>
          <path d="M14 30 l36 -18 l36 18 v44 l-36 18 l-36 -18z" fill={CLAUDE.INK} fillOpacity={1 - 0.88 * glass} stroke={CLAUDE.INK} strokeWidth={3} />
          {[0, 1, 2].map((k) => <circle key={k} cx={34 + k * 16} cy={58 + (k % 2) * 8} r={5} fill={CLAUDE.SPARK} />)}
        </svg>
        <div style={{ fontFamily: SERIF, fontSize: Q.serif, color: CLAUDE.INK, textAlign: 'center', whiteSpace: 'nowrap' }}>{glassLabel.split(' → ')[1] ?? glassLabel}</div>
      </div>
      {quote && <PQuote text={quote} source={quoteSource} o={cau} top={1170} />}
      {noteShort && <div style={{ position: 'absolute', left: P.x0, top: 92, fontFamily: SANS, fontSize: Q.sans, color: CLAUDE.INK_SOFT, lineHeight: 1 }}>{noteShort}</div>}
      <Bug />
    </AbsoluteFill>
  );
};

const CreditP: React.FC<z.infer<typeof trustCreditSchema>> = ({ kicker, paper, author, id, cues }) => {
  const { reveal } = useClock();
  const [c0, c1, c2, c3] = cues;
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <Card style={{ position: 'absolute', left: P.x0, width: P.x1 - P.x0, top: 230, padding: '50px 44px', borderTop: `14px solid ${CLAUDE.SPARK}` }}>
        <div style={{ fontFamily: SANS, fontSize: Q.sans, color: CLAUDE.INK_SOFT, opacity: reveal(c0) }}>{kicker}</div>
        <div style={{ fontFamily: SERIF, fontSize: Q.serif, color: CLAUDE.INK, lineHeight: 1.08, marginTop: 10, opacity: reveal(c0) }}>{paper}</div>
        <div style={{ fontFamily: SERIF, fontSize: Q.serif, color: CLAUDE.INK, marginTop: 34, opacity: reveal(c1) }}>{author}</div>
        <div style={{ fontFamily: MONO, fontSize: Q.mono, color: CLAUDE.INK, marginTop: 14, lineHeight: 1.2, opacity: reveal(c2) }}>{id.replace(' · ', '\n')}</div>
        <div style={{ fontFamily: SANS, fontSize: Q.sans, color: CLAUDE.INK_SOFT, marginTop: 30, lineHeight: 1.1, opacity: reveal(c3) }}>A survey. Our examples.</div>
      </Card>
      <Bug />
    </AbsoluteFill>
  );
};

export const TrustHallucination = withBrand(pick(HallucinationInner, HallucinationP));
export const TrustThreeProblems = withBrand(pick(ThreeProblemsInner, ThreeProblemsP));
export const TrustToolbox = withBrand(pick(ToolboxInner, ToolboxP));
export const TrustOverlap = withBrand(pick(OverlapInner, OverlapP));
export const TrustBenchAB = withBrand(pick(BenchABInner, BenchABP));
export const TrustCounterfactual = withBrand(pick(CounterfactualInner, CounterfactualP));
export const TrustEmbedding = withBrand(pick(EmbeddingInner, EmbeddingP));
export const TrustReasoning = withBrand(pick(ReasoningInner, ReasoningP));
export const TrustCredit = withBrand(pick(CreditInner, CreditP));
