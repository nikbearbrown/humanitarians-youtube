/**
 * LbScenes.tsx — Remotion components for "Learning Brutalist" (Humanitarians AI
 * fellow progress update, Tanishaa). Registered in Root.tsx under the folder
 * "LearningBrutalist".
 *
 * Same look as RagScenes.tsx: Claude fidelity cream #FAF9F5, ink #3D3929,
 * terracotta #D97757 as the one accent (#AF4B2D when it carries words).
 * 1920x1080, 30 fps. Every reveal time is a prop (fraction of the beat, cued to
 * the measured spoken word), so re-timing is a beat-sheet change.
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
const OK = '#3F6B4A';
const SERIF = '"EB Garamond", Georgia, "Times New Roman", serif';
const SANS = '-apple-system, "SF Pro Text", "Segoe UI", "Helvetica Neue", sans-serif';
const MONO = 'ui-monospace, "SF Mono", Menlo, monospace';

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

const Logo: React.FC<{ name: string; h: number; style?: React.CSSProperties }> = ({ name, h, style }) => (
  <Img src={staticFile(`logos/${name}/${name}-01.svg`)} style={{ height: h, width: 'auto', ...style }} />
);

/** Drawn waveform for Kokoro (no logo in icons/logos). */
const Wave: React.FC<{ h: number; t: number }> = ({ h, t }) => {
  const bars = [0.35, 0.7, 1, 0.55, 0.85, 0.4, 0.75, 0.5, 0.3];
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: h * 0.08, height: h }}>
      {bars.map((b, i) => (
        <div key={i} style={{ width: h * 0.09, borderRadius: h, background: ACC_TEXT,
          height: h * b * (0.75 + 0.25 * Math.sin(t * 60 + i * 1.3)) }} />
      ))}
    </div>
  );
};

const dur = { durationSeconds: z.number().optional() };

// ===========================================================================
// LbPipeline — five steps in a row light up on their words. The clock step
// (audio) gets the one accent and a ticking clock hand: it sets every timing.
// ===========================================================================
export const lbPipelineSchema = z.object({
  spark: z.string().default(''),
  steps: z.array(z.object({ name: z.string(), sub: z.string() })),
  stepAt: z.array(z.number()),
  clockIndex: z.number().default(1),
  clockAt: z.number().default(0.6),
  ...dur,
});
export const LbPipeline: React.FC<z.infer<typeof lbPipelineSchema>> = (p) => {
  const t = useT();
  const n = p.steps.length, GAP = 56, W = (CW - 2 * SX - (n - 1) * GAP) / n, TOP = 330, H = 420;
  const clock = rise(t, p.clockAt);
  return (
    <AbsoluteFill style={{ background: BG }}>
      <Spark line={p.spark} o={rise(t, 0)} />
      {p.steps.map((s, i) => {
        const o = rise(t, p.stepAt[i] ?? 0);
        const isClock = i === p.clockIndex;
        const x = SX + i * (W + GAP);
        return (
          <React.Fragment key={i}>
            <div style={{ position: 'absolute', left: x, top: TOP, width: W, height: H, boxSizing: 'border-box',
              background: CARD, borderRadius: 20, padding: '30px 26px', opacity: 0.25 + 0.75 * o,
              border: `${isClock && clock > 0.5 ? 5 : 2}px solid ${isClock && clock > 0.5 ? ACC : o > 0.5 ? INK : BORDER}`,
              transform: `translateY(${(1 - o) * 20}px)` }}>
              <div style={{ fontFamily: SANS, fontSize: 28, letterSpacing: 2, color: SOFT }}>{`STEP ${i + 1}`}</div>
              <div style={{ fontFamily: SERIF, fontSize: 60, lineHeight: 1.05, color: INK, marginTop: 10 }}>{s.name}</div>
              <div style={{ fontFamily: SERIF, fontSize: 38, lineHeight: 1.2, color: isClock && clock > 0.5 ? ACC_TEXT : SOFT, marginTop: 16 }}>{s.sub}</div>
              {isClock ? (
                <svg width={120} height={120} style={{ position: 'absolute', left: W / 2 - 60, bottom: 30, opacity: clock }}>
                  <circle cx={60} cy={60} r={52} fill="none" stroke={ACC} strokeWidth={6} />
                  <line x1={60} y1={60} x2={60 + 38 * Math.sin(t * 12)} y2={60 - 38 * Math.cos(t * 12)} stroke={ACC_TEXT} strokeWidth={6} strokeLinecap="round" />
                  <circle cx={60} cy={60} r={6} fill={ACC_TEXT} />
                </svg>
              ) : null}
            </div>
            {i < n - 1 ? (
              <div style={{ position: 'absolute', left: x + W, top: TOP + H / 2 - 40, width: GAP, textAlign: 'center',
                fontFamily: SANS, fontSize: 54, color: rise(t, p.stepAt[i + 1] ?? 1) > 0.5 ? INK : GHOST }}>→</div>
            ) : null}
          </React.Fragment>
        );
      })}
      {/* the audio clock drives every later step: a terracotta rule under steps 2..n */}
      <div style={{ position: 'absolute', top: TOP + H + 50, left: SX + p.clockIndex * (W + GAP) + W / 2,
        width: (n - 1 - p.clockIndex) * (W + GAP) * clock, height: 6, borderRadius: 3, background: ACC }} />
      <div style={{ position: 'absolute', top: TOP + H + 80, left: SX + p.clockIndex * (W + GAP) + W / 2, fontFamily: SERIF,
        fontSize: 40, color: ACC_TEXT, opacity: clock }}>everything after the audio is timed to it</div>
      <HaiBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// LbChecklist — a setup check: each row ticks on its word; one row fails with
// an honest note. Logos per LOGO LAW where the toolkit has one.
// ===========================================================================
export const lbChecklistSchema = z.object({
  spark: z.string().default(''),
  title: z.string(),
  items: z.array(z.object({ label: z.string(), logo: z.string().default(''), ok: z.boolean(),
    note: z.string().default(''), short: z.string().default(''), noteShort: z.string().default(''), at: z.number() })),
  footnote: z.string().default(''),
  footnoteShort: z.string().default(''),
  footnoteAt: z.number().default(0.3),
  ...dur,
});
export const LbChecklist: React.FC<z.infer<typeof lbChecklistSchema>> = (p) => {
  const t = useT();
  const TOP = 170, W = 1160, X = (CW - W) / 2, ROW = 128;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <Spark line={p.spark} o={rise(t, 0)} />
      <div style={{ position: 'absolute', left: X, top: TOP, width: W, height: 140 + p.items.length * ROW, boxSizing: 'border-box',
        background: CARD, border: `2px solid ${BORDER}`, borderRadius: 22, padding: '28px 48px', opacity: rise(t, 0.02) }}>
        <div style={{ fontFamily: MONO, fontSize: 40, color: SOFT }}>$ {p.title}</div>
        {p.items.map((it, i) => {
          const o = rise(t, it.at);
          return (
            <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 30, height: ROW, borderTop: i ? `1px solid ${BORDER}` : 'none',
              marginTop: i ? 0 : 18, opacity: 0.3 + 0.7 * o }}>
              <div style={{ width: 70, height: 70, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                {it.logo ? <Logo name={it.logo} h={62} /> : <Wave h={56} t={t} />}
              </div>
              <div style={{ fontFamily: SERIF, fontSize: 58, color: INK, flex: 1 }}>
                {it.label}
                {it.note ? <span style={{ fontSize: 40, color: SOFT, marginLeft: 22, fontStyle: 'italic', opacity: o }}>{it.note}</span> : null}
              </div>
              <div style={{ fontFamily: SANS, fontSize: 60, fontWeight: 800, width: 70, textAlign: 'center',
                color: it.ok ? OK : ACC_TEXT, opacity: o, transform: `scale(${1.5 - 0.5 * o})` }}>{it.ok ? '✓' : '✕'}</div>
            </div>
          );
        })}
      </div>
      <Footnote text={p.footnote} o={rise(t, p.footnoteAt)} />
      <HaiBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// LbToolCards — four tool cards, each arriving on its name.
// ===========================================================================
export const lbToolCardsSchema = z.object({
  spark: z.string().default(''),
  cards: z.array(z.object({ name: z.string(), role: z.string(), logos: z.array(z.string()).default([]),
    glyph: z.string().default(''), at: z.number() })),
  ...dur,
});
export const LbToolCards: React.FC<z.infer<typeof lbToolCardsSchema>> = (p) => {
  const t = useT();
  const n = p.cards.length, GAP = 40, W = (CW - 2 * SX - (n - 1) * GAP) / n, TOP = 230, H = 640;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <Spark line={p.spark} o={rise(t, 0)} />
      {p.cards.map((c, i) => {
        const o = rise(t, c.at);
        return (
          <div key={i} style={{ position: 'absolute', left: SX + i * (W + GAP), top: TOP, width: W, height: H, boxSizing: 'border-box',
            background: CARD, border: `2px solid ${o > 0.5 ? INK : BORDER}`, borderRadius: 22, padding: '50px 34px',
            display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center',
            opacity: o, transform: `translateY(${(1 - o) * 40}px)` }}>
            <div style={{ height: 180, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 24 }}>
              {c.logos.map((l) => <Logo key={l} name={l} h={150} />)}
              {c.glyph === 'wave' ? <Wave h={140} t={t} /> : null}
            </div>
            <div style={{ fontFamily: SERIF, fontSize: 66, lineHeight: 1.05, color: INK, marginTop: 60 }}>{c.name}</div>
            <div style={{ fontFamily: SERIF, fontSize: 44, lineHeight: 1.2, color: SOFT, marginTop: 24 }}>{c.role}</div>
          </div>
        );
      })}
      <HaiBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// LbGates — two gate cards; each stamps its result on its word.
// ===========================================================================
export const lbGatesSchema = z.object({
  spark: z.string().default(''),
  gates: z.array(z.object({ name: z.string(), desc: z.string(), result: z.string(), at: z.number() })),
  footnote: z.string().default(''),
  footnoteShort: z.string().default(''),
  ...dur,
});
export const LbGates: React.FC<z.infer<typeof lbGatesSchema>> = (p) => {
  const t = useT();
  const W = 790, GAP = CW - 2 * SX - 2 * W, TOP = 250, H = 560;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <Spark line={p.spark} o={rise(t, 0)} />
      {p.gates.map((g, i) => {
        const o = rise(t, g.at);
        const stamp = rise(t, g.at + 0.08);
        return (
          <div key={i} style={{ position: 'absolute', left: SX + i * (W + GAP), top: TOP, width: W, height: H, boxSizing: 'border-box',
            background: CARD, border: `2px solid ${BORDER}`, borderRadius: 22, padding: '44px 50px', opacity: 0.25 + 0.75 * o }}>
            <div style={{ fontFamily: MONO, fontSize: 52, color: INK, fontWeight: 700 }}>{g.name}</div>
            <div style={{ fontFamily: SERIF, fontSize: 58, lineHeight: 1.2, color: INK, marginTop: 26 }}>{g.desc}</div>
            <div style={{ position: 'absolute', left: 50, bottom: 50, border: `6px solid ${OK}`, color: OK, fontFamily: SANS,
              fontWeight: 800, fontSize: 64, letterSpacing: 3, padding: '10px 30px', borderRadius: 12, opacity: stamp,
              transform: `rotate(-4deg) scale(${1.5 - 0.5 * stamp})`, transformOrigin: 'left center' }}>{g.result}</div>
          </div>
        );
      })}
      <Footnote text={p.footnote} o={rise(t, 0.05)} />
      <HaiBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// LbTwoFrames — real frames from an earlier video: landscape and vertical,
// each tagged with its pixel size; the callout says why vertical isn't a crop.
// ===========================================================================
export const lbTwoFramesSchema = z.object({
  spark: z.string().default(''),
  landscape: z.string(),
  vertical: z.string(),
  landTag: z.string(),
  vertTag: z.string(),
  landAt: z.number().default(0.05),
  vertAt: z.number().default(0.4),
  callout: z.string(),
  calloutShort: z.string().default(''),
  calloutAt: z.number().default(0.6),
  footnote: z.string().default(''),
  footnoteShort: z.string().default(''),
  ...dur,
});
export const LbTwoFrames: React.FC<z.infer<typeof lbTwoFramesSchema>> = (p) => {
  const t = useT();
  const lo = rise(t, p.landAt), vo = rise(t, p.vertAt), co = rise(t, p.calloutAt);
  const LW = 1040, LH = LW * 9 / 16, VH = 760, VW = VH * 9 / 16, TOP = 170;
  const tag = (s: string): React.CSSProperties => ({ fontFamily: MONO, fontSize: 36, color: INK, marginTop: 16 });
  return (
    <AbsoluteFill style={{ background: BG }}>
      <Spark line={p.spark} o={rise(t, 0)} />
      <div style={{ position: 'absolute', left: SX, top: TOP + 60, opacity: lo, transform: `translateY(${(1 - lo) * 30}px)` }}>
        <Img src={staticFile(p.landscape)} style={{ width: LW, height: LH, borderRadius: 14, border: `2px solid ${BORDER}`, display: 'block' }} />
        <div style={tag(p.landTag)}>{p.landTag} · landscape</div>
      </div>
      <div style={{ position: 'absolute', left: SX + LW + 120, top: TOP, opacity: vo, transform: `translateY(${(1 - vo) * 30}px)` }}>
        <Img src={staticFile(p.vertical)} style={{ width: VW, height: VH, borderRadius: 14, border: `3px solid ${co > 0.5 ? ACC_TEXT : BORDER}`, display: 'block' }} />
        <div style={tag(p.vertTag)}>{p.vertTag} · vertical</div>
      </div>
      <div style={{ position: 'absolute', left: SX, top: TOP + 60 + LH + 80, width: LW, fontFamily: SERIF, fontSize: 54,
        color: ACC_TEXT, opacity: co, transform: `translateX(${(1 - co) * -30}px)` }}>{p.callout}</div>
      <HaiBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// LbSyncFix — the bug the checks missed. Two tracks: when Bella says each item,
// and when it appears on screen. Before the fix the on-screen marks trail the
// words; on the fix they slide back to line up.
// ===========================================================================
export const lbSyncFixSchema = z.object({
  spark: z.string().default(''),
  frame: z.string(),
  badge: z.string(),
  badgeAt: z.number().default(0.05),
  words: z.array(z.string()),
  lagAt: z.number().default(0.3),
  fixAt: z.number().default(0.7),
  caption: z.string(),
  captionAt: z.number().default(0.5),
  spokenLabel: z.string().default('Bella says'),
  shownLabel: z.string().default('On screen'),
  ...dur,
});
export const LbSyncFix: React.FC<z.infer<typeof lbSyncFixSchema>> = (p) => {
  const t = useT();
  const bo = rise(t, p.badgeAt), lag = rise(t, p.lagAt), fix = rise(t, p.fixAt, FADE * 2), cap = rise(t, p.captionAt);
  const IW = 640, IH = IW * 9 / 16;
  const TX = SX + IW + 90, TW = CW - SX - TX, ROW1 = 300, ROW2 = 520, LABEL = 230;
  const n = p.words.length, step = (TW - LABEL - 60) / n;
  const wx = (i: number) => TX + LABEL + 30 + i * step;
  const offset = 150 * (1 - fix);
  return (
    <AbsoluteFill style={{ background: BG }}>
      <Spark line={p.spark} o={rise(t, 0)} />
      <div style={{ position: 'absolute', left: SX, top: 220 }}>
        <Img src={staticFile(p.frame)} style={{ width: IW, height: IH, borderRadius: 12, border: `2px solid ${BORDER}`, display: 'block' }} />
        <div style={{ marginTop: 26, display: 'inline-block', border: `5px solid ${OK}`, color: OK, fontFamily: SANS, fontWeight: 800,
          fontSize: 44, padding: '6px 22px', borderRadius: 10, opacity: bo }}>{p.badge}</div>
      </div>
      {/* tracks */}
      {[ROW1, ROW2].map((y, r) => (
        <React.Fragment key={r}>
          <div style={{ position: 'absolute', left: TX, top: y - 30, width: LABEL, fontFamily: SANS, fontSize: 34, color: SOFT, opacity: lag }}>
            {r === 0 ? p.spokenLabel : p.shownLabel}</div>
          <div style={{ position: 'absolute', left: TX + LABEL, top: y, width: TW - LABEL, height: 4, background: BORDER, opacity: lag }} />
        </React.Fragment>
      ))}
      {p.words.map((w, i) => {
        const x = wx(i);
        const sx = x + offset;
        return (
          <React.Fragment key={i}>
            <div style={{ position: 'absolute', left: x - 10, top: ROW1 - 10, width: 24, height: 24, borderRadius: 12, background: INK, opacity: lag }} />
            <div style={{ position: 'absolute', left: x - 130, width: 260, top: ROW1 - 90, textAlign: 'center', fontFamily: SERIF,
              fontSize: 40, color: INK, opacity: lag }}>“{w}”</div>
            <div style={{ position: 'absolute', left: sx - 12, top: ROW2 - 30, width: 28, height: 64, borderRadius: 6,
              background: fix > 0.5 ? OK : ACC, opacity: lag }} />
            <svg width={CW} height={1080} style={{ position: 'absolute', left: 0, top: 0, opacity: lag * (1 - fix) }}>
              <line x1={x} y1={ROW1 + 20} x2={sx} y2={ROW2 - 34} stroke={ACC} strokeWidth={3} strokeDasharray="10 8" />
            </svg>
          </React.Fragment>
        );
      })}
      <div style={{ position: 'absolute', left: TX + LABEL, top: ROW2 + 60, fontFamily: SERIF, fontSize: 42,
        color: fix > 0.5 ? OK : ACC_TEXT, opacity: lag }}>
        {fix > 0.5 ? 'fixed: each reveal cued to its measured word' : 'each item appears after its word'}</div>
      <div style={{ position: 'absolute', left: SX, right: SX, top: 840, textAlign: 'center', fontFamily: SERIF, fontSize: 74,
        color: INK, opacity: cap, transform: `translateY(${(1 - cap) * 20}px)` }}>{p.caption}</div>
      <HaiBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// PORTRAIT (9:16) VARIANTS — native 1080×1920, registered as <Name>916. Same
// schemas and cue props as landscape. Phone-size type (GATE T floor = 1.9% of
// 3840): serif >= 92, sans >= 72 design px. SHOW LESS: no spark lines or
// sub-labels (the narration says them); `short` fields replace long labels.
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

export const LbPipeline916: React.FC<z.infer<typeof lbPipelineSchema>> = (p) => {
  const t = useT();
  const n = p.steps.length, GAP = 60, TOP = PY + 40, H = (1700 - TOP - (n - 1) * GAP) / n;
  const clock = rise(t, p.clockAt);
  return (
    <AbsoluteFill style={{ background: BG }}>
      {p.steps.map((s, i) => {
        const o = rise(t, p.stepAt[i] ?? 0);
        const isClock = i === p.clockIndex;
        const y = TOP + i * (H + GAP);
        const hot = isClock && clock > 0.5;
        return (
          <React.Fragment key={i}>
            <div style={{ position: 'absolute', left: PX, top: y, width: PIW, height: H, boxSizing: 'border-box', background: CARD,
              borderRadius: 22, border: `${hot ? 6 : 2}px solid ${hot ? ACC : o > 0.5 ? INK : BORDER}`, opacity: 0.25 + 0.75 * o,
              display: 'flex', alignItems: 'center', padding: '0 44px', gap: 36 }}>
              <span style={{ fontFamily: SANS, fontSize: PSANS, color: SOFT, width: 60 }}>{i + 1}</span>
              <span style={{ fontFamily: SERIF, fontSize: PSERIF + 8, color: INK, flex: 1 }}>{s.name}</span>
              {isClock ? (
                <svg width={110} height={110} style={{ opacity: clock }}>
                  <circle cx={55} cy={55} r={48} fill="none" stroke={ACC} strokeWidth={7} />
                  <line x1={55} y1={55} x2={55 + 35 * Math.sin(t * 12)} y2={55 - 35 * Math.cos(t * 12)} stroke={ACC_TEXT} strokeWidth={7} strokeLinecap="round" />
                </svg>
              ) : null}
            </div>
            {i < n - 1 ? (
              <div style={{ position: 'absolute', left: 0, right: 0, top: y + H - 6, height: GAP, textAlign: 'center', fontFamily: SANS,
                fontSize: 64, lineHeight: `${GAP}px`, color: rise(t, p.stepAt[i + 1] ?? 1) > 0.5 ? (i >= p.clockIndex && clock > 0.5 ? ACC_TEXT : INK) : GHOST }}>↓</div>
            ) : null}
          </React.Fragment>
        );
      })}
      <div style={{ position: 'absolute', left: PX, right: PX, top: 1730, fontFamily: SERIF, fontSize: PSERIF, lineHeight: 1,
        color: ACC_TEXT, opacity: clock }}>audio sets the clock</div>
      <PBug />
    </AbsoluteFill>
  );
};

export const LbChecklist916: React.FC<z.infer<typeof lbChecklistSchema>> = (p) => {
  const t = useT();
  const TOP = PY + 20, ROW = 230;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: PX, top: TOP, fontFamily: MONO, fontSize: PSANS, color: SOFT, opacity: rise(t, 0.02) }}>$ {p.title}</div>
      {p.items.map((it, i) => {
        const o = rise(t, it.at);
        const label = (it as any).short || it.label;
        const note = (it as any).noteShort || '';
        return (
          <div key={i} style={{ position: 'absolute', left: PX, width: PIW, top: TOP + 150 + i * ROW, height: ROW - 30, boxSizing: 'border-box',
            background: CARD, border: `2px solid ${BORDER}`, borderRadius: 20, padding: '0 36px', display: 'flex', alignItems: 'center', gap: 30,
            opacity: 0.3 + 0.7 * o }}>
            <div style={{ width: 110, display: 'flex', justifyContent: 'center' }}>
              {it.logo ? <Logo name={it.logo} h={100} /> : <Wave h={90} t={t} />}
            </div>
            <div style={{ flex: 1 }}>
              <div style={{ fontFamily: SERIF, fontSize: PSERIF, lineHeight: 1, color: INK }}>{label}</div>
              {note ? <div style={{ fontFamily: SANS, fontSize: PSANS, lineHeight: 1.1, color: SOFT, marginTop: 6, opacity: o }}>{note}</div> : null}
            </div>
            <div style={{ fontFamily: SANS, fontSize: 96, fontWeight: 800, color: it.ok ? OK : ACC_TEXT, opacity: o,
              transform: `scale(${1.5 - 0.5 * o})` }}>{it.ok ? '✓' : '✕'}</div>
          </div>
        );
      })}
      <PFoot text={p.footnoteShort || p.footnote} o={rise(t, p.footnoteAt)} />
      <PBug />
    </AbsoluteFill>
  );
};

export const LbToolCards916: React.FC<z.infer<typeof lbToolCardsSchema>> = (p) => {
  const t = useT();
  const n = p.cards.length, GAP = 44, TOP = PY + 20, H = (1780 - TOP - (n - 1) * GAP) / n;
  return (
    <AbsoluteFill style={{ background: BG }}>
      {p.cards.map((c, i) => {
        const o = rise(t, c.at);
        return (
          <div key={i} style={{ position: 'absolute', left: PX, top: TOP + i * (H + GAP), width: PIW, height: H, boxSizing: 'border-box',
            background: CARD, border: `2px solid ${o > 0.5 ? INK : BORDER}`, borderRadius: 22, padding: '0 44px',
            display: 'flex', alignItems: 'center', gap: 44, opacity: o, transform: `translateX(${(1 - o) * -40}px)` }}>
            <div style={{ width: 180, display: 'flex', justifyContent: 'center' }}>
              {c.logos.map((l) => <Logo key={l} name={l} h={160} />)}
              {c.glyph === 'wave' ? <Wave h={150} t={t} /> : null}
            </div>
            <div style={{ fontFamily: SERIF, fontSize: PSERIF + 4, lineHeight: 1.02, color: INK }}>{c.name}</div>
          </div>
        );
      })}
      <PBug />
    </AbsoluteFill>
  );
};

export const LbGates916: React.FC<z.infer<typeof lbGatesSchema>> = (p) => {
  const t = useT();
  const TOP = PY + 20, H = 760, GAP = 60;
  return (
    <AbsoluteFill style={{ background: BG }}>
      {p.gates.map((g, i) => {
        const o = rise(t, g.at), stamp = rise(t, g.at + 0.08);
        return (
          <div key={i} style={{ position: 'absolute', left: PX, top: TOP + i * (H + GAP), width: PIW, height: H, boxSizing: 'border-box',
            background: CARD, border: `2px solid ${BORDER}`, borderRadius: 22, padding: '44px 50px', opacity: 0.25 + 0.75 * o }}>
            <div style={{ fontFamily: MONO, fontSize: PSANS + 8, color: INK, fontWeight: 700 }}>{g.name}</div>
            <div style={{ fontFamily: SERIF, fontSize: PSERIF, lineHeight: 1.1, color: INK, marginTop: 30 }}>{g.desc}</div>
            <div style={{ position: 'absolute', left: 50, bottom: 50, border: `7px solid ${OK}`, color: OK, fontFamily: SANS, fontWeight: 800,
              fontSize: 96, letterSpacing: 3, padding: '8px 34px', borderRadius: 14, opacity: stamp,
              transform: `rotate(-4deg) scale(${1.5 - 0.5 * stamp})`, transformOrigin: 'left center' }}>{g.result}</div>
          </div>
        );
      })}
      <PBug />
    </AbsoluteFill>
  );
};

export const LbTwoFrames916: React.FC<z.infer<typeof lbTwoFramesSchema>> = (p) => {
  const t = useT();
  const lo = rise(t, p.landAt), vo = rise(t, p.vertAt), co = rise(t, p.calloutAt);
  const LH = PIW * 9 / 16, VH = 880, VW = VH * 9 / 16, VY = PY + LH + 150;
  const callout = (p as any).calloutShort || p.callout;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: PX, top: PY, opacity: lo }}>
        <Img src={staticFile(p.landscape)} style={{ width: PIW, height: LH, borderRadius: 14, border: `2px solid ${BORDER}`, display: 'block' }} />
        <div style={{ fontFamily: MONO, fontSize: PSANS, color: INK, marginTop: 14 }}>{p.landTag}</div>
      </div>
      <div style={{ position: 'absolute', left: PX, top: VY, opacity: vo }}>
        <Img src={staticFile(p.vertical)} style={{ width: VW, height: VH, borderRadius: 14, border: `4px solid ${co > 0.5 ? ACC_TEXT : BORDER}`, display: 'block' }} />
      </div>
      <div style={{ position: 'absolute', left: PX + VW + 40, right: PX, top: VY, opacity: vo, fontFamily: MONO, fontSize: PSANS, lineHeight: 1.1, color: INK }}>
        {p.vertTag.replace('×', '×\n').split('\n').map((s, i) => <div key={i}>{s}</div>)}
      </div>
      <div style={{ position: 'absolute', left: PX + VW + 40, right: PX, top: VY + 300, fontFamily: SERIF, fontSize: PSERIF, lineHeight: 1.05,
        color: ACC_TEXT, opacity: co }}>{callout}</div>
      <PBug />
    </AbsoluteFill>
  );
};

export const LbSyncFix916: React.FC<z.infer<typeof lbSyncFixSchema>> = (p) => {
  const t = useT();
  const bo = rise(t, p.badgeAt), lag = rise(t, p.lagAt), fix = rise(t, p.fixAt, FADE * 2), cap = rise(t, p.captionAt);
  const IH = PIW * 9 / 16, R1 = 1000, R2 = 1220, LX = PX + 300, TW = PW - PX - LX;
  const n = p.words.length, step = TW / n, off = 110 * (1 - fix);
  const wx = (i: number) => LX + step * (i + 0.3);
  return (
    <AbsoluteFill style={{ background: BG }}>
      <Img src={staticFile(p.frame)} style={{ position: 'absolute', left: PX, top: PY, width: PIW, height: IH, borderRadius: 14, border: `2px solid ${BORDER}` }} />
      <div style={{ position: 'absolute', left: PX, top: PY + IH + 30, border: `6px solid ${OK}`, color: OK, fontFamily: SANS, fontWeight: 800,
        fontSize: PSANS, padding: '4px 24px', borderRadius: 12, opacity: bo }}>{p.badge}</div>
      {[R1, R2].map((y, r) => (
        <React.Fragment key={r}>
          <div style={{ position: 'absolute', left: PX, top: y - 45, fontFamily: SANS, fontSize: PSANS, color: SOFT, opacity: lag }}>{r ? 'Screen' : 'Bella'}</div>
          <div style={{ position: 'absolute', left: LX, top: y, width: TW, height: 5, background: BORDER, opacity: lag }} />
        </React.Fragment>
      ))}
      {p.words.map((_, i) => {
        const x = wx(i), sx = x + off;
        return (
          <React.Fragment key={i}>
            <div style={{ position: 'absolute', left: x - 18, top: R1 - 16, width: 36, height: 36, borderRadius: 18, background: INK, opacity: lag }} />
            <div style={{ position: 'absolute', left: sx - 18, top: R2 - 50, width: 36, height: 100, borderRadius: 8, background: fix > 0.5 ? OK : ACC_TEXT, opacity: lag }} />
            <svg width={PW} height={1920} style={{ position: 'absolute', left: 0, top: 0, opacity: lag * (1 - fix) }}>
              <line x1={x} y1={R1 + 24} x2={sx} y2={R2 - 54} stroke={ACC_TEXT} strokeWidth={5} strokeDasharray="14 10" />
            </svg>
          </React.Fragment>
        );
      })}
      <div style={{ position: 'absolute', left: PX, right: PX, top: R2 + 100, fontFamily: SERIF, fontSize: PSERIF, lineHeight: 1,
        color: fix > 0.5 ? OK : ACC_TEXT, opacity: lag }}>{fix > 0.5 ? 'fixed: on the word' : 'late: after the word'}</div>
      <div style={{ position: 'absolute', left: PX, right: PX, top: 1500, fontFamily: SERIF, fontSize: PSERIF + 8, lineHeight: 1.08,
        color: INK, opacity: cap }}>{p.caption}</div>
      <PBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// LbTakeaway916 — portrait takeaway: heading + numbered lines at phone size,
// each on its spoken words. Replaces ClaudeVerdictArtifact916 in the vertical
// sheet, whose lines render at ~40 design px (unreadable on a phone).
// ===========================================================================
export const lbTakeawaySchema = z.object({
  artifactTitle: z.string().default(''),
  artifactHeading: z.string(),
  artifactLines: z.array(z.string()),
  lineAt: z.array(z.number()).default([]),
  ...dur,
});
export const LbTakeaway916: React.FC<z.infer<typeof lbTakeawaySchema>> = (p) => {
  const t = useT();
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: PX, right: PX, top: PY + 40, fontFamily: SERIF, fontSize: PSERIF + 16, lineHeight: 1.05,
        color: INK, opacity: rise(t, 0), borderBottom: `4px solid ${INK}`, paddingBottom: 40 }}>{p.artifactHeading}</div>
      {p.artifactLines.map((l, i) => {
        const o = rise(t, p.lineAt[i] ?? 0.1 + i * 0.25);
        const text = l.replace(/^\d+\.\s*/, '');
        return (
          <div key={i} style={{ position: 'absolute', left: PX, right: PX, top: 520 + i * 400, display: 'flex', gap: 30,
            opacity: o, transform: `translateY(${(1 - o) * 30}px)` }}>
            <span style={{ fontFamily: SERIF, fontSize: PSERIF + 30, color: ACC_TEXT, lineHeight: 1, width: 80 }}>{i + 1}</span>
            <span style={{ fontFamily: SERIF, fontSize: PSERIF, color: INK, lineHeight: 1.08 }}>{text}</span>
          </div>
        );
      })}
      <PBug />
    </AbsoluteFill>
  );
};
