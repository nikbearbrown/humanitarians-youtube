import React from 'react';
import {AbsoluteFill, Img, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {SAFE, SAFE916} from '../tokens/layout';

/**
 * SocialAiVisibility.tsx — concept illustrations (C3) for the ai-explainer reel
 * "Can AI Content Automation Pace Brand Visibility?" (@Shubh & @HumanitariansAI).
 *
 * Dual-aspect: every scene reads useVideoConfig() and lays out natively for
 * 1920×1080 (SAFE) or 1080×1920 (SAFE916). Root.tsx registers each as `<Name>`
 * and `<Name>916` (RENDER-TARGETS.md §3 — portrait is a layout, never a crop).
 * Pure functions of the beat clock: pass `durationSeconds` = the beat's measured
 * audio so reveals land on the spoken phrase (show events are beat fractions).
 *
 * Palette: claude C3 stage — cream #F2F0E9, warm ink, ONE terracotta accent per
 * beat. No invented figures: every chart here is labelled illustrative and has
 * no numeric axis.
 */

export const STAGE = '#F2F0E9';
export const INK = CLAUDE.INK;
export const SOFT = CLAUDE.INK_SOFT;
export const ACCENT = CLAUDE.SPARK;
export const SERIF = CLAUDE_FONT.serif;
export const SANS = CLAUDE_FONT.ui;

const clamp01 = (v: number) => Math.min(1, Math.max(0, v));

export const useBeat = (durationSeconds: number) => {
  const frame = useCurrentFrame();
  const {fps, width, height} = useVideoConfig();
  const portrait = height > width;
  const S = portrait ? SAFE916 : SAFE;
  const total = Math.max(1, durationSeconds * fps);
  const p = frame / total;
  /** spring that starts at beat fraction f */
  const pop = (f: number) =>
    clamp01(spring({frame: frame - f * total, fps, config: {damping: 22, stiffness: 150, mass: 0.7}}));
  /** linear 0→1 ramp starting at beat fraction f over d */
  const ramp = (f: number, d = 0.08) => clamp01((p - f) / d);
  return {frame, fps, width, height, portrait, S, p, pop, ramp};
};

const durationProp = {durationSeconds: z.number().default(16)};

export const Spark: React.FC<{size: number}> = ({size}) => (
  <svg width={size} height={size} viewBox="-50 -50 100 100" style={{flexShrink: 0}}>
    {[0, 45, 90, 135].map((a) => (
      <rect key={a} x={-7} y={-47} width={14} height={94} rx={7} fill={ACCENT} transform={`rotate(${a})`} />
    ))}
  </svg>
);

/** SPARK-LINE LAW — spark + one short serif line, pinned to the top of SAFE. */
const SparkLine: React.FC<{text: string; portrait: boolean; S: typeof SAFE | typeof SAFE916}> = ({text, portrait, S}) => {
  const size = portrait ? 56 : 52;
  return (
    <div style={{position: 'absolute', left: S.x, top: S.y, width: S.w, display: 'flex', alignItems: 'center',
      justifyContent: 'center', gap: size * 0.4}}>
      <Spark size={size * 0.9} />
      <span style={{fontFamily: SERIF, fontSize: size, color: INK, fontWeight: 600, lineHeight: 1.1}}>{text}</span>
    </div>
  );
};

/** LOGO LAW — HAI wordmark as a small low-opacity corner bug, inside SAFE. */
const LogoBug: React.FC<{S: typeof SAFE | typeof SAFE916; width: number; height: number}> = ({S, width, height}) => (
  <Img src={staticFile('hai-wordmark-outlined.svg')}
    style={{position: 'absolute', right: width - S.r, bottom: height - S.b, height: 34, opacity: 0.55}} />
);

export const Card: React.FC<{style?: React.CSSProperties; children: React.ReactNode}> = ({style, children}) => (
  <div style={{background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 22,
    boxShadow: '0 14px 44px rgba(61,57,41,0.12)', ...style}}>{children}</div>
);

const Caption: React.FC<{text: string; S: typeof SAFE | typeof SAFE916; bottomPad?: number}> = ({text, S, bottomPad = 40}) => (
  <div style={{position: 'absolute', left: S.x, width: S.w, top: S.b - bottomPad, textAlign: 'left',
    fontFamily: SANS, fontSize: 40, color: SOFT}}>{text}</div>
);

// ─────────────────────────────────────────────────────────────────────────────
// B02 — one idea fans out into many platform formats
// ─────────────────────────────────────────────────────────────────────────────
export const socialOneToManySchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('One idea, many formats.'),
  idea: z.string().default('A product launch'),
  ideaLabel: z.string().default('ONE IDEA'),
  outputs: z.array(z.object({label: z.string(), note: z.string()})).default([
    {label: 'Reel', note: 'vertical video'},
    {label: 'TikTok', note: 'short clip'},
    {label: 'LinkedIn post', note: 'professional take'},
    {label: 'Captions', note: 'per-platform copy'},
    {label: 'Carousel', note: 'swipe-through slides'},
    {label: 'Email', note: 'subscriber update'},
  ]),
  bottomLine: z.string().default('More quality content — without multiplying the workload.'),
  /** beat fraction where the first output card lands; the rest follow in order */
  outputsAt: z.number().default(0.18),
  outputsSpan: z.number().default(0.42),
  bottomAt: z.number().default(0.78),
  /** output-grid columns (landscape); 1 suits two or three outputs */
  cols: z.number().default(2),
});

export const SocialOneToMany: React.FC<z.infer<typeof socialOneToManySchema>> = (props) => {
  const {portrait, S, width, height, pop} = useBeat(props.durationSeconds);
  const n = props.outputs.length;
  const cols = Math.max(1, props.cols);
  const rows = Math.ceil(n / cols);

  // geometry — landscape: idea left, 2×3 grid right; portrait: idea top, grid below
  const top = S.y + (portrait ? 150 : 110);
  const bottomReserve = portrait ? 230 : 150;
  const areaH = S.b - bottomReserve - top;
  const idea = portrait
    ? {x: S.x + 110, y: top, w: S.w - 220, h: 250}
    : {x: S.x + 20, y: top + areaH / 2 - 150, w: 540, h: 300};
  const grid = portrait
    ? {x: S.x, y: top + 250 + 150, w: S.w, h: areaH - 250 - 150}
    : {x: S.x + 740, y: top, w: S.w - 760, h: areaH};
  const gap = portrait ? 28 : 30;
  const cw = (grid.w - gap * (cols - 1)) / cols;
  const ch = (grid.h - gap * (rows - 1)) / rows;
  const stagger = props.outputsSpan / Math.max(1, n - 1);

  const cells = props.outputs.map((o, i) => {
    const c = i % cols, r = Math.floor(i / cols);
    return {...o, x: grid.x + c * (cw + gap), y: grid.y + r * (ch + gap), t: pop(props.outputsAt + i * stagger)};
  });
  const ideaIn = pop(0.02);
  const src = portrait
    ? {x: idea.x + idea.w / 2, y: idea.y + idea.h}
    : {x: idea.x + idea.w, y: idea.y + idea.h / 2};
  const bottomIn = pop(props.bottomAt);

  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={portrait} S={S} />
      <svg width={width} height={height} style={{position: 'absolute', inset: 0}}>
        {cells.map((c, i) => {
          // branch into the near column only (landscape) / top row only (portrait) —
          // a line to a far card would show as stubs in the gaps between cards
          if (portrait ? i >= cols : i % cols !== 0) return null;
          const dst = portrait ? {x: c.x + cw / 2, y: c.y} : {x: c.x, y: c.y + ch / 2};
          const mid = portrait ? {x1: src.x, y1: (src.y + dst.y) / 2, x2: dst.x, y2: (src.y + dst.y) / 2}
                               : {x1: (src.x + dst.x) / 2, y1: src.y, x2: (src.x + dst.x) / 2, y2: dst.y};
          const d = `M ${src.x} ${src.y} C ${mid.x1} ${mid.y1}, ${mid.x2} ${mid.y2}, ${dst.x} ${dst.y}`;
          return <path key={i} d={d} fill="none" stroke={SOFT} strokeWidth={3} strokeDasharray="1400"
            strokeDashoffset={1400 * (1 - c.t)} opacity={0.7} />;
        })}
      </svg>
      <Card style={{position: 'absolute', left: idea.x, top: idea.y, width: idea.w, height: idea.h,
        display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center',
        opacity: ideaIn, transform: `scale(${0.9 + 0.1 * ideaIn})`, border: `3px solid ${CLAUDE.GHOST}`}}>
        <div style={{fontFamily: SANS, fontSize: 40, letterSpacing: '0.14em', color: SOFT, fontWeight: 700}}>{props.ideaLabel}</div>
        <div style={{fontFamily: SERIF, fontSize: portrait ? 64 : 60, color: INK, fontWeight: 700, marginTop: 14,
          textAlign: 'center', padding: '0 24px', lineHeight: 1.1}}>{props.idea}</div>
      </Card>
      {cells.map((c, i) => (
        <Card key={i} style={{position: 'absolute', left: c.x, top: c.y, width: cw, height: ch, opacity: c.t,
          transform: `translateY(${(1 - c.t) * 24}px)`, display: 'flex', flexDirection: 'column',
          justifyContent: 'center', padding: '0 34px', boxSizing: 'border-box'}}>
          <div style={{fontFamily: SERIF, fontSize: portrait ? 50 : 50, color: INK, fontWeight: 700, lineHeight: 1.05}}>{c.label}</div>
          <div style={{fontFamily: SANS, fontSize: portrait ? 40 : 40, color: SOFT, marginTop: 8}}>{c.note}</div>
        </Card>
      ))}
      <div style={{position: 'absolute', left: S.x, width: S.w, top: S.b - bottomReserve + (portrait ? 50 : 36),
        textAlign: 'center', fontFamily: SERIF, fontSize: portrait ? 52 : 50, color: INK, lineHeight: 1.15,
        opacity: bottomIn, transform: `translateY(${(1 - bottomIn) * 16}px)`}}>{props.bottomLine}</div>
      <LogoBug S={S} width={width} height={height} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B03 — one campaign keeps a consistent cadence across platforms
// ─────────────────────────────────────────────────────────────────────────────
export const socialCadenceGridSchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('Same campaign. Every platform.'),
  campaign: z.string().default('One campaign'),
  days: z.array(z.string()).default(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']),
  platforms: z.array(z.object({name: z.string(), format: z.string(), slots: z.array(z.number())})).default([
    {name: 'Instagram', format: 'Reel + carousel', slots: [0, 2, 4]},
    {name: 'LinkedIn', format: 'text post', slots: [1, 3]},
    {name: 'TikTok', format: 'short clip', slots: [0, 2, 3, 5]},
    {name: 'YouTube', format: 'Short', slots: [1, 4]},
    {name: 'X', format: 'thread', slots: [0, 1, 2, 3, 4]},
  ]),
  caption: z.string().default('Illustrative schedule'),
  rowsAt: z.number().default(0.14),
  rowsSpan: z.number().default(0.5),
});

export const SocialCadenceGrid: React.FC<z.infer<typeof socialCadenceGridSchema>> = (props) => {
  const {portrait, S, width, height, pop} = useBeat(props.durationSeconds);
  const top = S.y + (portrait ? 150 : 104);
  const campH = portrait ? 120 : 104;
  const gridTop = top + campH + (portrait ? 60 : 22);
  const gridBottom = S.b - (portrait ? 150 : 58);
  const labelW = portrait ? 300 : 440;
  const nDays = props.days.length;
  const headH = portrait ? 62 : 60;
  const rowGap = portrait ? 18 : 10;
  const nRows = props.platforms.length;
  const rowH = (gridBottom - gridTop - headH - rowGap * (nRows - 1)) / nRows;
  const cellW = (S.w - labelW) / nDays;
  const dot = Math.min(cellW, rowH) * 0.52;
  const campIn = pop(0.02);
  const rowStagger = props.rowsSpan / Math.max(1, nRows - 1);

  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={portrait} S={S} />
      <Card style={{position: 'absolute', left: S.x + S.w / 2 - (portrait ? 330 : 330), top, width: 660, height: campH,
        display: 'flex', alignItems: 'center', justifyContent: 'center', border: `3px solid ${CLAUDE.GHOST}`,
        opacity: campIn, transform: `scale(${0.9 + 0.1 * campIn})`}}>
        <span style={{fontFamily: SERIF, fontSize: portrait ? 58 : 56, fontWeight: 700, color: INK}}>{props.campaign}</span>
      </Card>
      {props.days.map((d, j) => (
        <div key={d} style={{position: 'absolute', left: S.x + labelW + j * cellW, width: cellW, top: gridTop,
          height: headH, textAlign: 'center', fontFamily: SANS, fontSize: portrait ? 44 : 44, color: SOFT,
          fontWeight: 600, opacity: campIn}}>{d}</div>
      ))}
      {props.platforms.map((pl, i) => {
        const rowIn = pop(props.rowsAt + i * rowStagger);
        const y = gridTop + headH + i * (rowH + rowGap);
        return (
          <React.Fragment key={pl.name}>
            <div style={{position: 'absolute', left: S.x, top: y, width: S.w, height: rowH, borderRadius: 16,
              background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, opacity: 0.35 + 0.65 * rowIn}} />
            <div style={{position: 'absolute', left: S.x + 28, top: y, height: rowH, width: labelW - 40,
              display: 'flex', flexDirection: 'column', justifyContent: 'center', opacity: rowIn,
              transform: `translateX(${(1 - rowIn) * -20}px)`}}>
              <div style={{fontFamily: SERIF, fontSize: portrait ? 50 : 50, fontWeight: 700, color: INK, lineHeight: 1.0}}>{pl.name}</div>
              <div style={{fontFamily: SANS, fontSize: portrait ? 48 : 48, color: SOFT, marginTop: 8, lineHeight: 1.0}}>{pl.format}</div>
            </div>
            {pl.slots.map((s, k) => {
              const t = pop(props.rowsAt + i * rowStagger + 0.02 + k * 0.012);
              const cx = S.x + labelW + s * cellW + cellW / 2;
              return <div key={k} style={{position: 'absolute', left: cx - dot / 2, top: y + rowH / 2 - dot / 2,
                width: dot, height: dot, borderRadius: dot / 2, background: INK,
                transform: `scale(${t})`, opacity: 0.85}} />;
            })}
          </React.Fragment>
        );
      })}
      <Caption text={props.caption} S={S} bottomPad={portrait ? 110 : 52} />
      <LogoBug S={S} width={width} height={height} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B04 — trend window: spotted early vs late (illustrative curve, no numbers)
// ─────────────────────────────────────────────────────────────────────────────
export const socialTrendWindowSchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('Early beats late.'),
  signals: z.array(z.string()).default(['trending topics', 'formats', 'keywords', 'conversations']),
  yLabel: z.string().default('attention on a trend'),
  xLabel: z.string().default('time'),
  earlyLabel: z.string().default('post on the way up'),
  lateLabel: z.string().default('post after the peak'),
  caption: z.string().default('Illustrative curve — not measured data'),
  signalsAt: z.number().default(0.1),
  curveAt: z.number().default(0.34),
  earlyAt: z.number().default(0.56),
  lateAt: z.number().default(0.7),
});

export const SocialTrendWindow: React.FC<z.infer<typeof socialTrendWindowSchema>> = (props) => {
  const {portrait, S, width, height, pop, ramp} = useBeat(props.durationSeconds);
  const top = S.y + (portrait ? 150 : 104);
  const chipH = portrait ? 76 : 70;
  const chipRows = portrait ? 2 : 1;
  const chipCols = portrait ? 2 : props.signals.length;
  const chipGap = 22;
  const chipW = (S.w - chipGap * (chipCols - 1)) / chipCols;
  const chartTop = top + chipRows * chipH + (chipRows - 1) * chipGap + (portrait ? 110 : 60);
  const chartBottom = S.b - (portrait ? 260 : 110);
  const chartL = S.x + 60, chartR = S.r - 20;
  const cw = chartR - chartL, chh = chartBottom - chartTop;

  // a smooth rise-peak-fade curve (gaussian-ish), sampled
  const N = 90;
  const curve = (u: number) => Math.exp(-Math.pow((u - 0.45) / 0.17, 2));
  const pts = Array.from({length: N + 1}, (_, i) => {
    const u = i / N;
    return {x: chartL + u * cw, y: chartBottom - curve(u) * chh * 0.86};
  });
  const drawn = ramp(props.curveAt, 0.18);
  const visible = pts.slice(0, Math.max(2, Math.round(drawn * N) + 1));
  const d = visible.map((q, i) => `${i ? 'L' : 'M'} ${q.x.toFixed(1)} ${q.y.toFixed(1)}`).join(' ');

  const uEarly = 0.3, uLate = 0.72;
  const early = {x: chartL + uEarly * cw, y: chartBottom - curve(uEarly) * chh * 0.86};
  const late = {x: chartL + uLate * cw, y: chartBottom - curve(uLate) * chh * 0.86};
  const eIn = pop(props.earlyAt), lIn = pop(props.lateAt);
  // shaded window under the curve from the early marker onward
  const win = pts.filter((q) => q.x >= early.x && q.x <= chartL + 0.62 * cw);
  const winD = win.length > 1
    ? `M ${win[0].x} ${chartBottom} ` + win.map((q) => `L ${q.x} ${q.y}`).join(' ') + ` L ${win[win.length - 1].x} ${chartBottom} Z`
    : '';
  // right-aligned labels are clamped to start at SAFE's left edge (portrait has little room left of the marker)
  const markerLabel = (x: number, y: number, text: string, t: number, accent: boolean, alignRight: boolean) => (
    <div style={{position: 'absolute', left: alignRight ? Math.max(chartL + 16, x - 26 - 520) : x + 26,
      width: alignRight ? x - 26 - Math.max(chartL + 16, x - 26 - 520) : undefined,
      top: y - (portrait ? 230 : 120), maxWidth: portrait ? 420 : 520, fontFamily: SERIF, fontSize: portrait ? 42 : 50,
      fontWeight: 700, color: accent ? INK : SOFT, opacity: t, lineHeight: 1.1,
      textAlign: alignRight ? 'right' : 'left'}}>{text}</div>
  );

  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={portrait} S={S} />
      {props.signals.map((s, i) => {
        const t = pop(props.signalsAt + i * 0.04);
        const c = i % chipCols, r = Math.floor(i / chipCols);
        return (
          <div key={s} style={{position: 'absolute', left: S.x + c * (chipW + chipGap), top: top + r * (chipH + chipGap),
            width: chipW, height: chipH, borderRadius: chipH / 2, background: CLAUDE.CARD,
            border: `2px solid ${CLAUDE.BORDER}`, display: 'flex', alignItems: 'center', justifyContent: 'center',
            fontFamily: SANS, fontSize: portrait ? 40 : 40, color: INK, fontWeight: 600, opacity: t,
            transform: `scale(${0.85 + 0.15 * t})`}}>{s}</div>
        );
      })}
      <svg width={width} height={height} style={{position: 'absolute', inset: 0}}>
        <line x1={chartL} y1={chartBottom} x2={chartR} y2={chartBottom} stroke={SOFT} strokeWidth={3} />
        <line x1={chartL} y1={chartTop} x2={chartL} y2={chartBottom} stroke={SOFT} strokeWidth={3} />
        {winD && <path d={winD} fill={ACCENT} opacity={0.14 * eIn} />}
        <path d={d} fill="none" stroke={INK} strokeWidth={6} strokeLinecap="round" strokeLinejoin="round" />
        <circle cx={early.x} cy={early.y} r={18 * eIn} fill={ACCENT} />
        <circle cx={late.x} cy={late.y} r={16 * lIn} fill={CLAUDE.GHOST} />
      </svg>
      {markerLabel(early.x, early.y, props.earlyLabel, eIn, true, true)}
      {markerLabel(late.x, late.y, props.lateLabel, lIn, false, false)}
      <div style={{position: 'absolute', left: chartL, top: chartBottom + 14, width: cw, textAlign: 'right',
        fontFamily: SANS, fontSize: 40, color: SOFT}}>{props.xLabel} →</div>
      <div style={{position: 'absolute', left: chartL + 18, top: chartTop - 6, fontFamily: SANS, fontSize: 40, color: SOFT}}>
        ↑ {props.yLabel}</div>
      <Caption text={props.caption} S={S} bottomPad={portrait ? 150 : 52} />
      <LogoBug S={S} width={width} height={height} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B05 — one product, different message per audience
// ─────────────────────────────────────────────────────────────────────────────
export const socialAudienceBranchSchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('Same product. Three angles.'),
  product: z.string().default('One product'),
  segments: z.array(z.object({audience: z.string(), angle: z.string(), sample: z.string()})).default([
    {audience: 'Gen Z', angle: 'playful · visual', sample: '“Your week, but make it aesthetic.”'},
    {audience: 'Professionals', angle: 'results · time saved', sample: '“Plan your whole quarter before lunch.”'},
    {audience: 'Existing customers', angle: 'what’s new for you', sample: '“New for you: shared team boards.”'},
  ]),
  caption: z.string().default('Example copy for a hypothetical planner app'),
  segmentsAt: z.array(z.number()).default([0.34, 0.5, 0.66]),
});

export const SocialAudienceBranch: React.FC<z.infer<typeof socialAudienceBranchSchema>> = (props) => {
  const {portrait, S, width, height, pop} = useBeat(props.durationSeconds);
  const top = S.y + (portrait ? 150 : 104);
  const prodH = portrait ? 150 : 130;
  const prodW = portrait ? 700 : 760;
  const prod = {x: S.x + (S.w - prodW) / 2, y: top, w: prodW, h: prodH};
  const n = props.segments.length;
  const segTop = top + prodH + (portrait ? 110 : 110);
  const segBottom = S.b - (portrait ? 150 : 70);
  const gap = portrait ? 34 : 34;
  const segs = props.segments.map((s, i) => {
    const w = portrait ? S.w - 90 : (S.w - gap * (n - 1)) / n;
    const h = portrait ? (segBottom - segTop - gap * (n - 1)) / n : segBottom - segTop;
    const x = portrait ? S.x + 90 : S.x + i * (w + gap);
    const y = portrait ? segTop + i * (h + gap) : segTop;
    return {...s, x, y, w, h, t: pop(props.segmentsAt[i] ?? 0.4 + i * 0.15)};
  });
  const prodIn = pop(0.03);
  const src = {x: prod.x + prod.w / 2, y: prod.y + prod.h};

  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={portrait} S={S} />
      <svg width={width} height={height} style={{position: 'absolute', inset: 0}}>
        {/* landscape: a branch into each card's top; portrait: one spine down the left
            margin with a tick into each stacked card (branches would run behind cards) */}
        {!portrait && segs.map((s, i) => {
          const dst = {x: s.x + s.w / 2, y: s.y};
          const d = `M ${src.x} ${src.y} C ${src.x} ${(src.y + dst.y) / 2}, ${dst.x} ${(src.y + dst.y) / 2}, ${dst.x} ${dst.y}`;
          return <path key={i} d={d} fill="none" stroke={SOFT} strokeWidth={3} strokeDasharray="1600"
            strokeDashoffset={1600 * (1 - s.t)} opacity={0.7} />;
        })}
        {portrait && (() => {
          const spineX = S.x + 44;
          const last = segs[segs.length - 1];
          const lastY = last.y + last.h / 2;
          const reach = Math.max(...segs.map((s) => s.t));
          return (
            <g opacity={0.7}>
              <path d={`M ${src.x} ${src.y} L ${src.x} ${src.y + 40} L ${spineX} ${src.y + 40} L ${spineX} ${lastY}`}
                fill="none" stroke={SOFT} strokeWidth={3} strokeDasharray="2400" strokeDashoffset={2400 * (1 - reach)} />
              {segs.map((s, i) => <circle key={i} cx={spineX} cy={s.y + s.h / 2} r={10 * s.t} fill={SOFT} />)}
            </g>
          );
        })()}
      </svg>
      <Card style={{position: 'absolute', left: prod.x, top: prod.y, width: prod.w, height: prod.h,
        display: 'flex', alignItems: 'center', justifyContent: 'center', border: `3px solid ${CLAUDE.GHOST}`,
        opacity: prodIn, transform: `scale(${0.9 + 0.1 * prodIn})`}}>
        <span style={{fontFamily: SERIF, fontSize: portrait ? 58 : 56, fontWeight: 700, color: INK}}>{props.product}</span>
      </Card>
      {segs.map((s, i) => (
        <Card key={i} style={{position: 'absolute', left: s.x, top: s.y, width: s.w, height: s.h, boxSizing: 'border-box',
          padding: portrait ? '0 40px' : '0 44px', display: 'flex', flexDirection: 'column',
          justifyContent: 'center', opacity: s.t, transform: `translateY(${(1 - s.t) * 24}px)`}}>
          <div style={{fontFamily: SERIF, fontSize: portrait ? 54 : 62, fontWeight: 700, color: INK, lineHeight: 1.05}}>{s.audience}</div>
          <div style={{fontFamily: SANS, fontSize: portrait ? 40 : 40, color: SOFT, marginTop: 12, letterSpacing: '0.02em'}}>{s.angle}</div>
          <div style={{fontFamily: SERIF, fontStyle: 'italic', fontSize: portrait ? 44 : 50, color: INK,
            marginTop: portrait ? 18 : 44, lineHeight: 1.2}}>{s.sample}</div>
        </Card>
      ))}
      <Caption text={props.caption} S={S} bottomPad={portrait ? 110 : 52} />
      <LogoBug S={S} width={width} height={height} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B07 — the create → publish → analyze → optimize → repeat loop
// ─────────────────────────────────────────────────────────────────────────────
export const socialLoopSchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('Every post teaches the next.'),
  stages: z.array(z.string()).default(['Create', 'Publish', 'Analyze', 'Optimize', 'Repeat']),
  signals: z.array(z.string()).default(['engagement', 'watch time', 'clicks', 'audience behavior']),
  /** index of the stage the signals feed into */
  signalsInto: z.number().default(2),
  /** optional caption over the signal chips (default: "signals → <stage>") */
  signalsLabel: z.string().optional(),
  center: z.string().default('Each round informs the next.'),
  stagesAt: z.number().default(0.4),
  stagesSpan: z.number().default(0.3),
  signalsAt: z.number().default(0.1),
});

export const SocialLoop: React.FC<z.infer<typeof socialLoopSchema>> = (props) => {
  const {portrait, S, width, height, pop, p} = useBeat(props.durationSeconds);
  const n = props.stages.length;
  const top = S.y + (portrait ? 150 : 104);
  // landscape: signals column left, ring right; portrait: ring top, signals below
  const ringBox = portrait
    ? {x: S.x, y: top, w: S.w, h: 1000}
    : {x: S.x + 560, y: top, w: S.w - 560, h: S.b - 60 - top};
  const cx = ringBox.x + ringBox.w / 2, cy = ringBox.y + ringBox.h / 2;
  const R = Math.min(ringBox.w, ringBox.h) / 2 - (portrait ? 110 : 70);
  const nodeW = portrait ? 260 : 290, nodeH = portrait ? 100 : 104;
  const pos = (i: number) => {
    const a = -Math.PI / 2 + (i / n) * Math.PI * 2;
    return {x: cx + R * Math.cos(a), y: cy + R * Math.sin(a)};
  };
  const stagger = props.stagesSpan / Math.max(1, n - 1);
  const active = Math.floor(clamp01((p - props.stagesAt) / props.stagesSpan) * (n - 0.001));
  const loopT = clamp01((p - props.stagesAt) / (1 - props.stagesAt));
  const travA = -Math.PI / 2 + loopT * Math.PI * 2 * 1.4;
  const trav = {x: cx + R * Math.cos(travA), y: cy + R * Math.sin(travA)};

  const sigArea = portrait
    ? {x: S.x, y: ringBox.y + ringBox.h + 40, w: S.w, h: S.b - 120 - (ringBox.y + ringBox.h + 40)}
    : {x: S.x, y: top + 40, w: 500, h: S.b - 80 - (top + 40)};
  const sigCols = portrait ? 2 : 1;
  const sigRows = Math.ceil(props.signals.length / sigCols);
  const sigGap = 24;
  const sigW = (sigArea.w - sigGap * (sigCols - 1)) / sigCols;
  const sigH = Math.min(portrait ? 110 : 120, (sigArea.h - sigGap * (sigRows - 1)) / sigRows);

  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={portrait} S={S} />
      <svg width={width} height={height} style={{position: 'absolute', inset: 0}}>
        <circle cx={cx} cy={cy} r={R} fill="none" stroke={SOFT} strokeWidth={4} opacity={0.55}
          strokeDasharray={2 * Math.PI * R} strokeDashoffset={2 * Math.PI * R * (1 - pop(0.04))} />
        {p > props.stagesAt && <circle cx={trav.x} cy={trav.y} r={16} fill={ACCENT} />}
      </svg>
      <div style={{position: 'absolute', left: cx - R * 0.8, width: R * 1.6, top: cy - 60, height: 120,
        display: 'flex', alignItems: 'center', justifyContent: 'center', textAlign: 'center',
        fontFamily: SERIF, fontSize: portrait ? 44 : 50, fontStyle: 'italic', color: INK, lineHeight: 1.15,
        opacity: pop(props.stagesAt + props.stagesSpan)}}>{props.center}</div>
      {props.stages.map((s, i) => {
        const q = pos(i);
        const t = pop(props.stagesAt + i * stagger);
        const on = i === active && p > props.stagesAt;
        return (
          <Card key={s} style={{position: 'absolute', left: q.x - nodeW / 2, top: q.y - nodeH / 2, width: nodeW,
            height: nodeH, display: 'flex', alignItems: 'center', justifyContent: 'center',
            border: on ? `5px solid ${CLAUDE.GHOST}` : `3px solid ${CLAUDE.BORDER}`, opacity: 0.4 + 0.6 * t,
            transform: `scale(${(0.9 + 0.1 * t) * (on ? 1.06 : 1)})`}}>
            <span style={{fontFamily: SERIF, fontSize: portrait ? 46 : 50, fontWeight: 700, color: INK}}>{s}</span>
          </Card>
        );
      })}
      {props.signals.map((s, i) => {
        const t = pop(props.signalsAt + i * 0.05);
        const c = i % sigCols, r = Math.floor(i / sigCols);
        return (
          <div key={s} style={{position: 'absolute', left: sigArea.x + c * (sigW + sigGap),
            top: sigArea.y + r * (sigH + sigGap), width: sigW, height: sigH, borderRadius: 18,
            background: CLAUDE.FOOTER, border: `2px solid ${CLAUDE.BORDER}`, display: 'flex',
            alignItems: 'center', justifyContent: 'center', fontFamily: SANS, fontSize: portrait ? 40 : 40,
            fontWeight: 600, color: INK, opacity: t, transform: `translateX(${(1 - t) * -24}px)`}}>{s}</div>
        );
      })}
      <div style={{position: 'absolute', left: sigArea.x, width: sigArea.w,
        top: portrait ? sigArea.y - 62 : sigArea.y - 56, fontFamily: SANS, fontSize: 40, color: SOFT,
        textAlign: portrait ? 'center' : 'left', opacity: pop(props.signalsAt)}}>
        {props.signalsLabel ?? `signals → ${props.stages[props.signalsInto]}`}</div>
      <LogoBug S={S} width={width} height={height} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B08 — the honest limit: what to automate vs what stays human
// ─────────────────────────────────────────────────────────────────────────────
export const socialHumanSplitSchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('Scale needs judgment.'),
  leftTitle: z.string().default('Let AI automate'),
  leftItems: z.array(z.string()).default(['First drafts & variations', 'Resizing for each platform', 'Scheduling & posting', 'Performance reports']),
  rightTitle: z.string().default('Keep human'),
  rightItems: z.array(z.string()).default(['Strategy & goals', 'Brand voice & taste', 'Fact-checking claims', 'Final approval']),
  verdict: z.string().default('Automation scales whatever you feed it.'),
  leftAt: z.number().default(0.2),
  rightAt: z.number().default(0.4),
  verdictAt: z.number().default(0.72),
});

export const SocialHumanSplit: React.FC<z.infer<typeof socialHumanSplitSchema>> = (props) => {
  const {portrait, S, width, height, pop} = useBeat(props.durationSeconds);
  const top = S.y + (portrait ? 150 : 104);
  const verdictH = portrait ? 200 : 130;
  const bottom = S.b - verdictH - (portrait ? 90 : 30);
  const gap = 40;
  const colW = portrait ? S.w : (S.w - gap) / 2;
  const colH = portrait ? (bottom - top - gap) / 2 : bottom - top;
  const cols = [
    {title: props.leftTitle, items: props.leftItems, at: props.leftAt, x: S.x, y: top, human: false},
    {title: props.rightTitle, items: props.rightItems, at: props.rightAt,
      x: portrait ? S.x : S.x + colW + gap, y: portrait ? top + colH + gap : top, human: true},
  ];
  const vIn = pop(props.verdictAt);

  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={portrait} S={S} />
      {cols.map((c, ci) => {
        const headIn = pop(c.at);
        const itemH = (colH - (portrait ? 120 : 130)) / c.items.length;
        return (
          <Card key={ci} style={{position: 'absolute', left: c.x, top: c.y, width: colW, height: colH,
            boxSizing: 'border-box', padding: portrait ? '26px 44px' : '34px 48px', opacity: 0.3 + 0.7 * headIn,
            background: c.human ? CLAUDE.CARD : CLAUDE.FOOTER}}>
            <div style={{fontFamily: SERIF, fontSize: portrait ? 54 : 54, fontWeight: 700, color: INK,
              height: portrait ? 80 : 90}}>{c.title}</div>
            {c.items.map((it, k) => {
              const t = pop(c.at + 0.03 + k * 0.035);
              return (
                <div key={k} style={{height: itemH, display: 'flex', alignItems: 'center', gap: 22, opacity: t,
                  transform: `translateX(${(1 - t) * 20}px)`}}>
                  <div style={{width: 16, height: 16, borderRadius: 8, background: c.human ? INK : SOFT, flexShrink: 0}} />
                  <span style={{fontFamily: SANS, fontSize: portrait ? 42 : 42, color: INK}}>{it}</span>
                </div>
              );
            })}
          </Card>
        );
      })}
      <div style={{position: 'absolute', left: S.x, width: S.w, top: S.b - verdictH - (portrait ? 60 : 0), height: verdictH,
        display: 'flex', alignItems: 'center', justifyContent: 'center', textAlign: 'center',
        fontFamily: SERIF, fontSize: portrait ? 60 : 58, fontWeight: 700, color: INK, lineHeight: 1.1,
        opacity: vIn, transform: `translateY(${(1 - vIn) * 16}px)`}}>{props.verdict}</div>
      {/* the beat's one accent moment: a terracotta rule under the verdict (accent never carries text — WCAG) */}
      <div style={{position: 'absolute', left: S.x + S.w / 2 - (portrait ? 220 : 300), width: (portrait ? 440 : 600) * vIn,
        top: S.b - (portrait ? 60 : 0) - (portrait ? 22 : 18), height: 8, borderRadius: 4, background: ACCENT}} />
      <LogoBug S={S} width={width} height={height} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// Outro — title restate + the reel's own handle (ClaudeTitleOutro is locked to
// @NikBearBrown per OUTRO-LOCK.md, so non-NBB channels carry their own card).
// ─────────────────────────────────────────────────────────────────────────────
export const handleTitleOutroSchema = z.object({
  ...durationProp,
  title: z.string().default('⚠ SET IN BEAT SHEET'),
  handle: z.string().default('@HumanitariansAI'),
  logo: z.string().default('hai-wordmark-outlined.svg'),
  /** landscape size multiplier for short titles that would underfill (default 1 = unchanged) */
  scale: z.number().default(1),
});

export const HandleTitleOutro: React.FC<z.infer<typeof handleTitleOutroSchema>> = (props) => {
  const {portrait, S, pop} = useBeat(props.durationSeconds);
  const m = props.title.match(/^([\s\S]*?)\s*([.?!…]+)\s*$/);
  const body = m ? m[1] : props.title;
  const punct = m ? m[2] : '.';
  const tIn = pop(0.0), hIn = pop(0.12), lIn = pop(0.22);
  const k = portrait ? 1 : props.scale;
  return (
    <AbsoluteFill style={{background: CLAUDE.PAGE, alignItems: 'center', justifyContent: 'center', flexDirection: 'column'}}>
      <div style={{marginBottom: portrait ? 110 : 50 * k, opacity: tIn}}><Spark size={portrait ? 160 : 110 * k} /></div>
      <div style={{fontFamily: SERIF, fontWeight: 700, fontSize: portrait ? 128 : 124 * k, color: INK, letterSpacing: '-0.02em',
        textAlign: 'center', lineHeight: 1.08, maxWidth: S.w - 40, opacity: tIn, whiteSpace: 'pre-line',
        transform: `translateY(${(1 - tIn) * 18}px)`}}>
        {body}<span style={{color: CLAUDE.SEND}}>{punct}</span>
      </div>
      <div style={{fontFamily: SERIF, fontSize: portrait ? 74 : 72 * k, color: INK, marginTop: portrait ? 110 : 48 * k,
        opacity: 0.9 * hIn, textAlign: 'center', maxWidth: S.w}}>{props.handle}</div>
      <Img src={staticFile(props.logo)} style={{height: portrait ? 100 : 96 * k, marginTop: portrait ? 150 : 70 * k, opacity: lIn,
        maxWidth: S.w}} />
    </AbsoluteFill>
  );
};
