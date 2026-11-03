import React from 'react';
import {AbsoluteFill} from 'remotion';
import {z} from 'zod';
import {CLAUDE} from '../tokens/claude';
import {SAFE, SAFE916} from '../tokens/layout';
import {ACCENT, Card, INK, SANS, SERIF, SOFT, STAGE, Spark, useBeat} from './SocialAiVisibility';
import {LogoBug} from './ContentRepurpose';
import {Check} from './OneIntoTen';

/**
 * ContentPerformance.tsx — concept illustrations (C3) for the ai-explainer reel
 * "Why Great Content Doesn't Always Perform?" (@Shubh & @HumanitariansAI).
 *
 * Eight scenes: the reach chain (framework) → audience fit → distribution → timing →
 * format → the algorithm's signal loop → paid reach → diagnose (where the content
 * itself is the problem).
 *
 * Dual-aspect: every scene reads useVideoConfig() and lays out natively for 1920×1080
 * (SAFE) or 1080×1920 (SAFE916); Root.tsx registers each as `<Name>` and `<Name>916`
 * (portrait is a layout, never a crop). Portrait type clears GATE T's floor (serif ≥ 92,
 * sans ≥ 78); long copy is shortened through the vertical beat sheet's props.
 *
 * HONESTY: no statistics. Every chart and audience here is illustrative — no numeric
 * axis, no real data, captioned as such. `durationSeconds` = the beat's measured audio;
 * every `*At` prop is a beat fraction placed on the spoken word (faster-whisper
 * timestamps in the reel's _words.json). One terracotta accent per beat.
 */

type Safe = typeof SAFE | typeof SAFE916;
const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const dur = {durationSeconds: z.number().default(14)};
const PALE = CLAUDE.INK_SOFT;

/** type scale — landscape vs portrait (portrait floors: serif 92, sans 78) */
export const ty = (portrait: boolean) => portrait
  ? {serif: 92, sans: 78, head: 96}
  : {serif: 54, sans: 44, head: 60};

export const SparkLine: React.FC<{text: string; portrait: boolean; S: Safe}> = ({text, portrait, S}) => {
  const fs = portrait ? 92 : 52;
  return (
    <div style={{position: 'absolute', left: S.x, top: S.y, width: S.w, height: portrait ? 230 : 70, display: 'flex',
      alignItems: 'center', justifyContent: 'center', gap: fs * 0.4}}>
      <Spark size={fs * 0.9} />
      <span style={{fontFamily: SERIF, fontSize: fs, color: INK, fontWeight: 600, lineHeight: 1.05, textAlign: 'center',
        maxWidth: S.w - fs * 1.4}}>{text}</span>
    </div>
  );
};

export const Caption: React.FC<{text: string; S: Safe; portrait: boolean; opacity?: number}> = ({text, S, portrait, opacity = 1}) =>
  text ? (
    <div style={{position: 'absolute', left: S.x, top: S.b - (portrait ? 84 : 42), fontFamily: SANS, fontSize: portrait ? 78 : 40,
      lineHeight: 1, color: SOFT, opacity, whiteSpace: 'nowrap'}}>{text}</div>
  ) : null;

/** A person: head + shoulders, centred on (x, y), s = height. SVG. */
/** `joined` overlaps head and shoulders into one silhouette (portrait: GATE T reads a lone small head as a text run). */
export const Person: React.FC<{x: number; y: number; s: number; fill: string; opacity?: number; joined?: boolean}> = (
  {x, y, s, fill, opacity = 1, joined = false}) => (
  <g transform={`translate(${x} ${y})`} opacity={opacity}>
    <circle cx={0} cy={joined ? -s * 0.16 : -s * 0.24} r={s * 0.22} fill={fill} />
    <path d={`M ${-s * 0.36} ${s * 0.46} Q ${-s * 0.36} ${s * 0.02} 0 ${s * 0.02} Q ${s * 0.36} ${s * 0.02} ${s * 0.36} ${s * 0.46} Z`} fill={fill} />
  </g>
);

/** Line-drawn document glyph (the post). */
export const PostGlyph: React.FC<{size: number}> = ({size}) => (
  <svg width={size} height={size} viewBox="0 0 100 100" style={{flexShrink: 0}}>
    <path d="M 22 8 L 64 8 L 80 24 L 80 92 L 22 92 Z" fill="none" stroke={INK} strokeWidth={6} strokeLinejoin="round" />
    {[38, 54, 70].map((y, i) => <line key={y} x1={32} y1={y} x2={i === 2 ? 56 : 70} y2={y} stroke={INK} strokeWidth={6} strokeLinecap="round" />)}
  </svg>
);

const PostCard: React.FC<{left: number; top: number; w: number; h: number; title: string; tag?: string; px: number;
  tagPx: number; opacity: number}> = ({left, top, w, h, title, tag, px, tagPx, opacity}) => (
  <Card style={{position: 'absolute', left, top, width: w, height: h, boxSizing: 'border-box', padding: `0 ${px * 0.55}px`,
    display: 'flex', alignItems: 'center', gap: px * 0.45, opacity, transform: `translateY(${(1 - opacity) * 18}px)`}}>
    <PostGlyph size={px * 1.6} />
    <div>
      {tag && <div style={{fontFamily: SANS, fontSize: tagPx, fontWeight: 700, letterSpacing: '0.08em', color: SOFT, lineHeight: 1}}>{tag}</div>}
      <div style={{fontFamily: SERIF, fontSize: px, fontWeight: 700, color: INK, lineHeight: 1.05, marginTop: tag ? px * 0.2 : 0}}>{title}</div>
    </div>
  </Card>
);

// ─────────────────────────────────────────────────────────────────────────────
// B02 — framework: performance is a chain; one weak link stalls the post
// ─────────────────────────────────────────────────────────────────────────────
export const reachChainSchema = z.object({
  ...dur,
  sparkLine: z.string().default('Quality is one link.'),
  links: z.array(z.object({label: z.string(), at: z.number()})).default([
    {label: 'Quality', at: 0.19},
    {label: 'Audience fit', at: 0.35},
    {label: 'Distribution', at: 0.42},
    {label: 'Timing', at: 0.51},
    {label: 'Format', at: 0.56},
    {label: 'Algorithm', at: 0.62},
    {label: 'Paid reach', at: 0.68},
  ]),
  breakIndex: z.number().default(3),
  breakAt: z.number().default(0.8),
  panelTitle: z.string().default('WHO SEES IT'),
  stallLine: z.string().default('One weak link — it stalls.'),
  stallAt: z.number().default(0.88),
  caption: z.string().default('A mental model — not a formula'),
});
export type ReachChainProps = z.infer<typeof reachChainSchema>;

export const ReachChain: React.FC<ReachChainProps> = (props) => {
  const {portrait, S, pop, ramp, width, height} = useBeat(props.durationSeconds);
  const T = ty(portrait);
  const n = props.links.length;
  const top = portrait ? S.y + 260 : 160;
  const rowH = portrait ? 104 : 106, gap = portrait ? 12 : 12;
  const colW = portrait ? S.w : 640;
  const brk = ramp(props.breakAt, 0.05);
  const panel = portrait
    ? {x: S.x, y: top + n * (rowH + gap) + 28, w: S.w, h: 0}
    : {x: S.x + 720, y: top, w: S.w - 720, h: n * (rowH + gap) - gap};
  if (portrait) panel.h = S.b - 110 - panel.y;
  // people grid in the panel
  const cols = portrait ? 8 : 12, rows = portrait ? 2 : 6;
  const titleH = portrait ? 120 : 90, stallH = portrait ? 130 : 110, pad = portrait ? 34 : 48;
  const gw = panel.w - 2 * pad, gh = panel.h - titleH - stallH - pad;
  const cell = Math.min(gw / cols, gh / rows);
  const gx = panel.x + pad + (gw - cell * cols) / 2, gy = panel.y + titleH + (gh - cell * rows) / 2;
  const total = cols * rows;
  const lit = props.links.reduce((a, l) => a + pop(l.at), 0);
  const reachFull = (lit / n) * total;
  const reachAtBreak = (props.breakIndex / n) * total;
  const reach = reachFull + (Math.min(reachFull, reachAtBreak) - reachFull) * brk;
  const stallIn = pop(props.stallAt);
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={portrait} S={S} />
      {props.links.map((l, i) => {
        const t = pop(l.at);
        const isBreak = i === props.breakIndex;
        const after = i > props.breakIndex;
        const y = top + i * (rowH + gap);
        const dim = after ? 1 - 0.5 * brk : 1;
        return (
          <React.Fragment key={i}>
            {i > 0 && (
              <div style={{position: 'absolute', left: S.x + (portrait ? 70 : 64) - 9, top: y - gap - 8, width: 18, height: gap + 16,
                borderRadius: 9, background: isBreak ? (brk > 0 ? 'transparent' : INK) : INK, opacity: (0.45 + 0.55 * t) * dim}} />
            )}
            <div style={{position: 'absolute', left: S.x + (isBreak && !portrait ? brk * 30 : 0), top: y, width: colW, height: rowH,
              borderRadius: rowH / 2, boxSizing: 'border-box', display: 'flex', alignItems: 'center', gap: 22,
              padding: `0 ${portrait ? 40 : 34}px`,
              background: t > 0.5 ? CLAUDE.CARD : CLAUDE.FOOTER,
              border: `${isBreak && brk > 0 ? 7 : 4}px solid ${isBreak && brk > 0 ? ACCENT : t > 0.5 ? INK : CLAUDE.BORDER}`,
              opacity: (0.45 + 0.55 * t) * dim}}>
              <div style={{width: portrait ? 60 : 56, height: portrait ? 60 : 56, borderRadius: 30, flexShrink: 0,
                border: `4px solid ${INK}`, boxSizing: 'border-box', display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                {t > 0.5 && !(isBreak && brk > 0) && <Check size={portrait ? 40 : 38} />}
              </div>
              <span style={{fontFamily: SERIF, fontSize: T.serif, fontWeight: 700, color: INK, lineHeight: 1, whiteSpace: 'nowrap'}}>{l.label}</span>
            </div>
            {isBreak && brk > 0 && (
              <svg width={width} height={height} style={{position: 'absolute', left: 0, top: 0}}>
                <path d={`M ${S.x + colW - 170 + (portrait ? 0 : brk * 30)} ${y - 6} l 26 ${rowH * 0.3} l -30 ${rowH * 0.22} l 26 ${rowH * 0.3} l -18 ${rowH * 0.3}`}
                  fill="none" stroke={ACCENT} strokeWidth={7} strokeLinecap="round" strokeLinejoin="round" opacity={brk} />
              </svg>
            )}
          </React.Fragment>
        );
      })}
      <Card style={{position: 'absolute', left: panel.x, top: panel.y, width: panel.w, height: panel.h, boxSizing: 'border-box',
        padding: `${portrait ? 30 : 34}px ${pad}px`, opacity: pop(0.03)}}>
        <div style={{fontFamily: SANS, fontSize: T.sans, fontWeight: 700, letterSpacing: '0.1em', color: SOFT, lineHeight: 1}}>{props.panelTitle}</div>
      </Card>
      <svg width={width} height={height} style={{position: 'absolute', left: 0, top: 0}}>
        {Array.from({length: total}, (_, k) => {
          const c = k % cols, r = Math.floor(k / cols);
          const on = clamp01(reach - k);
          return <Person key={k} x={gx + (c + 0.5) * cell} y={gy + (r + 0.5) * cell} s={cell * 0.78}
            fill={on > 0.5 ? INK : PALE} opacity={(0.5 + 0.5 * on) * pop(0.03)} />;
        })}
      </svg>
      <div style={{position: 'absolute', left: panel.x, width: panel.w, top: panel.y + panel.h - stallH + (portrait ? 10 : 18),
        textAlign: 'center', fontFamily: SERIF, fontSize: portrait ? T.serif : 58, fontWeight: 700, color: INK, lineHeight: 1,
        opacity: stallIn}}>{props.stallLine}</div>
      <Caption text={props.caption} S={S} portrait={portrait} opacity={pop(0.03)} />
      <LogoBug portrait={portrait} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B03 — audience fit: the same post in two rooms
// ─────────────────────────────────────────────────────────────────────────────
const room = z.object({label: z.string(), verdict: z.string(), at: z.number()});
export const audienceFitSchema = z.object({
  ...dur,
  sparkLine: z.string().default('Right post, wrong room.'),
  post: z.string().default('A guide to budgeting'),
  postTag: z.string().default('THE SAME POST'),
  postAt: z.number().default(0.1),
  roomsAt: z.number().default(0.22),
  left: room.default({label: 'Scrolling for jokes', verdict: 'Skipped', at: 0.42}),
  right: room.default({label: 'Planning a first budget', verdict: 'Saved & shared', at: 0.66}),
  line: z.string().default('Same post. Different room.'),
  lineAt: z.number().default(0.86),
  caption: z.string().default('Illustration'),
});
export type AudienceFitProps = z.infer<typeof audienceFitSchema>;

export const AudienceFit: React.FC<AudienceFitProps> = (props) => {
  const {portrait, S, pop, ramp, width, height} = useBeat(props.durationSeconds);
  const T = ty(portrait);
  const postIn = pop(props.postAt), roomsIn = pop(props.roomsAt);
  const lIn = ramp(props.left.at, 0.06), rIn = ramp(props.right.at, 0.1);
  const post = portrait ? {x: S.x, y: S.y + 260, w: S.w, h: 220} : {x: S.x + (S.w - 820) / 2, y: 150, w: 820, h: 160};
  const rooms = portrait
    ? [{x: S.x, y: post.y + post.h + 50, w: S.w, h: 460}, {x: S.x, y: post.y + post.h + 50 + 490, w: S.w, h: 460}]
    : [{x: S.x, y: 380, w: (S.w - 60) / 2, h: 500}, {x: S.x + (S.w - 60) / 2 + 60, y: 380, w: (S.w - 60) / 2, h: 500}];
  const cols = 6, rowsN = portrait ? 2 : 3;
  const specs = [props.left, props.right];
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={portrait} S={S} />
      <svg width={width} height={height} style={{position: 'absolute', left: 0, top: 0}}>
        {!portrait && rooms.map((r, i) => (
          <line key={i} x1={post.x + post.w / 2} y1={post.y + post.h} x2={r.x + r.w / 2} y2={r.y} stroke={SOFT} strokeWidth={5}
            strokeDasharray="14 12" opacity={roomsIn} />
        ))}
      </svg>
      <PostCard left={post.x} top={post.y} w={post.w} h={post.h} title={props.post} tag={props.postTag}
        px={portrait ? T.serif : 60} tagPx={portrait ? T.sans : 40} opacity={postIn} />
      {rooms.map((r, i) => {
        const spec = specs[i];
        const good = i === 1;
        const t = good ? rIn : lIn;
        const labelH = portrait ? 120 : 84, verdictH = portrait ? 120 : 86;
        const gw = r.w - 80, gh = r.h - labelH - verdictH - 40;
        const cell = Math.min(gw / cols, gh / rowsN);
        const gx = r.x + 40 + (gw - cell * cols) / 2, gy = r.y + labelH + 20 + (gh - cell * rowsN) / 2;
        return (
          <React.Fragment key={i}>
            <Card style={{position: 'absolute', left: r.x, top: r.y, width: r.w, height: r.h, boxSizing: 'border-box',
              padding: `${portrait ? 30 : 28}px 36px`, opacity: roomsIn,
              border: good && t > 0 ? `${3 + 4 * t}px solid ${ACCENT}` : `2px solid ${CLAUDE.BORDER}`}}>
              <div style={{fontFamily: SANS, fontSize: T.sans, fontWeight: 700, color: SOFT, lineHeight: 1, whiteSpace: 'nowrap'}}>{spec.label}</div>
            </Card>
            <svg width={width} height={height} style={{position: 'absolute', left: 0, top: 0}}>
              {Array.from({length: cols * rowsN}, (_, k) => {
                const c = k % cols, rr = Math.floor(k / cols);
                const stagger = clamp01(t * 1.6 - (k / (cols * rowsN)) * 0.6);
                const drift = good ? 0 : -stagger * cell * 0.18;
                const cx = gx + (c + 0.5) * cell, cy = gy + (rr + 0.5) * cell + drift;
                return (
                  <React.Fragment key={k}>
                    <Person x={cx} y={cy} s={cell * 0.72} fill={good ? (stagger > 0.5 ? INK : PALE) : PALE}
                      opacity={roomsIn * (good ? 0.55 + 0.45 * stagger : 1 - 0.45 * stagger)} />
                    {good && k % 3 === 0 && stagger > 0.5 && (
                      <path d={`M ${cx + cell * 0.2} ${cy - cell * 0.44} h ${cell * 0.2} v ${cell * 0.28} l ${-cell * 0.1} ${-cell * 0.08} l ${-cell * 0.1} ${cell * 0.08} Z`}
                        fill={INK} />
                    )}
                  </React.Fragment>
                );
              })}
            </svg>
            <div style={{position: 'absolute', left: r.x, width: r.w, top: r.y + r.h - verdictH, textAlign: 'center',
              fontFamily: SERIF, fontSize: portrait ? T.serif : 58, fontWeight: 700, lineHeight: 1,
              color: good ? INK : SOFT, opacity: t}}>{spec.verdict}</div>
          </React.Fragment>
        );
      })}
      {props.line && (
        <div style={{position: 'absolute', left: S.x, width: S.w, top: portrait ? rooms[1].y + rooms[1].h + 34 : 912, textAlign: 'center',
          fontFamily: SERIF, fontSize: portrait ? T.serif : 60, fontWeight: 700, fontStyle: 'italic', color: INK, lineHeight: 1,
          opacity: pop(props.lineAt)}}>{props.line}</div>
      )}
      {!portrait && <Caption text={props.caption} S={S} portrait={portrait} opacity={roomsIn} />}
      <LogoBug portrait={portrait} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B04 — distribution: publishing reaches some followers; the paths after reach more
// ─────────────────────────────────────────────────────────────────────────────
export const distributionPathsSchema = z.object({
  ...dur,
  sparkLine: z.string().default("Posting isn't distributing."),
  post: z.string().default('Your post'),
  postAt: z.number().default(0.03),
  rows: z.array(z.object({label: z.string(), note: z.string(), lit: z.number(), at: z.number()})).default([
    {label: 'Publish', note: 'some of your followers', lit: 4, at: 0.18},
    {label: 'Newsletter', note: 'subscribers', lit: 10, at: 0.6},
    {label: 'Community', note: 'members', lit: 10, at: 0.71},
    {label: 'Creator partner', note: 'their audience', lit: 10, at: 0.83},
  ]),
  afterLabel: z.string().default('What you do after'),
  afterAt: z.number().default(0.44),
  caption: z.string().default('Illustration — not real data'),
});
export type DistributionPathsProps = z.infer<typeof distributionPathsSchema>;

export const DistributionPaths: React.FC<DistributionPathsProps> = (props) => {
  const {portrait, S, pop, ramp, width, height} = useBeat(props.durationSeconds);
  const T = ty(portrait);
  const n = props.rows.length;
  const post = portrait ? {x: S.x + 120, y: S.y + 260, w: S.w - 240, h: 190} : {x: S.x, y: 410, w: 400, h: 200};
  const rowsTop = portrait ? post.y + post.h + 70 : 160;
  const rowH = portrait ? 250 : 170, gap = portrait ? 34 : 30;
  const rx = portrait ? S.x + 70 : S.x + 580, rw = S.r - rx;
  const perRow = 10;
  const afterIn = pop(props.afterAt);
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={portrait} S={S} />
      <svg width={width} height={height} style={{position: 'absolute', left: 0, top: 0}}>
        {props.rows.map((r, i) => {
          const cy = rowsTop + i * (rowH + gap) + rowH / 2;
          const d = portrait
            ? `M ${S.x + 22} ${post.y + post.h} L ${S.x + 22} ${cy} L ${rx} ${cy}`
            : `M ${post.x + post.w} ${post.y + post.h / 2} C ${post.x + post.w + 110} ${post.y + post.h / 2} ${rx - 110} ${cy} ${rx} ${cy}`;
          const len = portrait ? cy - post.y - post.h + rx - S.x : 700;
          const t = ramp(r.at - 0.03, 0.05);
          return <path key={i} d={d} fill="none" stroke={INK} strokeWidth={6} strokeLinecap="round"
            strokeDasharray={len} strokeDashoffset={len * (1 - t)} opacity={t > 0 ? 1 : 0} />;
        })}
      </svg>
      <PostCard left={post.x} top={post.y} w={post.w} h={post.h} title={props.post} px={portrait ? T.serif : 60} tagPx={40}
        opacity={pop(props.postAt)} />
      {!portrait && (
        <div style={{position: 'absolute', left: post.x, top: post.y + post.h + 40, width: post.w, boxSizing: 'border-box',
          padding: '34px 24px 18px', borderRadius: 20, border: `3px solid ${INK}`, background: CLAUDE.CARD, fontFamily: SERIF,
          backgroundImage: `linear-gradient(${ACCENT}, ${ACCENT})`, backgroundSize: '100% 16px', backgroundRepeat: 'no-repeat',
          fontSize: T.serif, fontWeight: 700, color: INK, lineHeight: 1.05, textAlign: 'center', opacity: afterIn,
          transform: `scale(${1.08 - 0.08 * afterIn})`}}>{props.afterLabel}</div>
      )}
      {props.rows.map((r, i) => {
        const y = rowsTop + i * (rowH + gap);
        const t = pop(r.at);
        const labelW = portrait ? rw : 520;
        const px0 = portrait ? rx + 30 : rx + labelW + 10;
        const pw = S.r - 30 - px0;
        const cell = pw / perRow;
        const pyc = portrait ? y + rowH - 70 : y + rowH / 2;
        return (
          <React.Fragment key={i}>
            <Card style={{position: 'absolute', left: rx, top: y, width: rw, height: rowH, boxSizing: 'border-box',
              padding: portrait ? '22px 30px' : '0 30px', display: 'flex', flexDirection: 'column', justifyContent: portrait ? 'flex-start' : 'center',
              opacity: 0.45 + 0.55 * t, border: portrait && i > 0 ? `4px solid ${afterIn > 0 && t > 0 ? ACCENT : CLAUDE.BORDER}` : undefined}}>
              <div style={{display: 'flex', alignItems: 'baseline', gap: 18}}>
                <span style={{fontFamily: SERIF, fontSize: T.serif, fontWeight: 700, color: INK, lineHeight: 1, whiteSpace: 'nowrap'}}>{r.label}</span>
              </div>
              {!portrait && <div style={{fontFamily: SANS, fontSize: 46, fontStyle: 'italic', color: SOFT, marginTop: 10, lineHeight: 1}}>{r.note}</div>}
            </Card>
            <svg width={width} height={height} style={{position: 'absolute', left: 0, top: 0}}>
              {Array.from({length: perRow}, (_, k) => {
                const on = k < r.lit ? clamp01(t * 1.5 - (k / perRow) * 0.5) : 0;
                return <Person key={k} joined={portrait} x={px0 + (k + 0.5) * cell} y={pyc} s={Math.min(cell * 0.86, portrait ? 110 : 96)}
                  fill={on > 0.5 ? INK : PALE} opacity={0.5 + 0.5 * Math.max(on, 0)} />;
              })}
            </svg>
          </React.Fragment>
        );
      })}
      <Caption text={props.caption} S={S} portrait={portrait} opacity={pop(props.postAt)} />
      <LogoBug portrait={portrait} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B06 — timing: the same post at 3 AM vs the evening peak
// ─────────────────────────────────────────────────────────────────────────────
export const timingWindowSchema = z.object({
  ...dur,
  sparkLine: z.string().default('Same post, different hour.'),
  curveAt: z.number().default(0.03),
  chartLabel: z.string().default('WHEN YOUR AUDIENCE IS ONLINE'),
  axis: z.array(z.object({h: z.number(), label: z.string()})).default([
    {h: 0, label: '12 AM'}, {h: 6, label: '6 AM'}, {h: 12, label: '12 PM'}, {h: 18, label: '6 PM'}, {h: 24, label: '12 AM'},
  ]),
  posts: z.array(z.object({label: z.string(), hour: z.number(), bar: z.number(), at: z.number()})).default([
    {label: 'Posted at 3 AM', hour: 3, bar: 0.14, at: 0.28},
    {label: 'Posted at 7 PM', hour: 19, bar: 0.86, at: 0.59},
  ]),
  barsTitle: z.string().default('FIRST-HOUR REACTIONS'),
  moreLabel: z.string().default('→ shown to more people'),
  moreAt: z.number().default(0.84),
  caption: z.string().default('Illustrative curve — check your own analytics'),
});
export type TimingWindowProps = z.infer<typeof timingWindowSchema>;

/** illustrative audience-activity curve over 24 h (no data; shape only) */
const activity = (h: number) => {
  const g = (mu: number, s: number, a: number) => a * Math.exp(-((h - mu) ** 2) / (2 * s * s));
  return 0.06 + g(8, 1.6, 0.42) + g(12.5, 1.8, 0.55) + g(20, 2.2, 0.92) + g(-4, 2.2, 0.5) + g(44, 2.2, 0.92);
};

export const TimingWindow: React.FC<TimingWindowProps> = (props) => {
  const {portrait, S, pop, ramp, width, height} = useBeat(props.durationSeconds);
  const T = ty(portrait);
  const chart = portrait ? {x: S.x, y: S.y + 260, w: S.w, h: 640} : {x: S.x, y: 150, w: S.w, h: 420};
  const padL = 40, padR = 40, padT = portrait ? 120 : 84, padB = portrait ? 110 : 70;
  const px = (h: number) => chart.x + padL + (h / 24) * (chart.w - padL - padR);
  const base = chart.y + chart.h - padB, plotH = chart.h - padT - padB;
  const py = (h: number) => base - (activity(h) / 1.05) * plotH;
  const pts = Array.from({length: 97}, (_, i) => i / 4);
  const line = pts.map((h, i) => `${i ? 'L' : 'M'} ${px(h).toFixed(1)} ${py(h).toFixed(1)}`).join(' ');
  const draw = ramp(props.curveAt, 0.14);
  const barsTop = portrait ? chart.y + chart.h + 60 : chart.y + chart.h + 40;
  const rowH = portrait ? 150 : 110, rowGap = portrait ? 30 : 22;
  const labelW = portrait ? 290 : 470;
  const trackX = S.x + labelW + 30, trackW = S.r - trackX - (portrait ? 0 : 560);
  const moreIn = pop(props.moreAt);
  const titleH = portrait ? 100 : 60;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={portrait} S={S} />
      <Card style={{position: 'absolute', left: chart.x, top: chart.y, width: chart.w, height: chart.h, boxSizing: 'border-box',
        padding: `${portrait ? 28 : 24}px ${padL}px`, opacity: pop(props.curveAt)}}>
        <div style={{fontFamily: SANS, fontSize: T.sans, fontWeight: 700, letterSpacing: '0.08em', color: SOFT, lineHeight: 1,
          whiteSpace: 'nowrap'}}>{props.chartLabel}</div>
      </Card>
      <svg width={width} height={height} style={{position: 'absolute', left: 0, top: 0}}>
        <defs>
          <clipPath id="tw-draw"><rect x={chart.x} y={chart.y} width={(chart.w) * draw} height={chart.h} /></clipPath>
        </defs>
        <g clipPath="url(#tw-draw)">
          <path d={`${line} L ${px(24)} ${base} L ${px(0)} ${base} Z`} fill={CLAUDE.FOOTER} />
          <path d={line} fill="none" stroke={INK} strokeWidth={6} strokeLinejoin="round" />
        </g>
        <line x1={px(0)} y1={base} x2={px(24)} y2={base} stroke={SOFT} strokeWidth={3} opacity={pop(props.curveAt)} />
        {props.posts.map((p, i) => {
          const t = pop(p.at);
          return (
            <g key={i} opacity={t}>
              <line x1={px(p.hour)} y1={base} x2={px(p.hour)} y2={py(p.hour) - 40} stroke={INK} strokeWidth={5} strokeDasharray="10 8" />
              <circle cx={px(p.hour)} cy={py(p.hour)} r={portrait ? 20 : 16} fill={INK} />
            </g>
          );
        })}
      </svg>
      {props.axis.map((a, i) => (
        <div key={i} style={{position: 'absolute', left: px(a.h) - 150, width: 300, top: base + (portrait ? 18 : 12), textAlign: 'center',
          fontFamily: SANS, fontSize: portrait ? T.sans : 40, color: SOFT, lineHeight: 1, opacity: pop(props.curveAt),
          transform: i === 0 ? 'translateX(110px)' : i === props.axis.length - 1 ? 'translateX(-125px)' : undefined}}>{a.label}</div>
      ))}
      <div style={{position: 'absolute', left: S.x, top: barsTop, fontFamily: SANS, fontSize: T.sans, fontWeight: 700,
        letterSpacing: '0.08em', color: SOFT, lineHeight: 1, opacity: pop(props.posts[0]?.at ?? 0.3)}}>{props.barsTitle}</div>
      {props.posts.map((p, i) => {
        const y = barsTop + titleH + i * (rowH + rowGap);
        const t = pop(p.at);
        const grow = ramp(p.at + 0.03, 0.12);
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: S.x, top: y, width: labelW, height: rowH, display: 'flex', alignItems: 'center',
              fontFamily: SERIF, fontSize: T.serif, fontWeight: 700, color: INK, lineHeight: 1, opacity: t, whiteSpace: 'nowrap'}}>{p.label}</div>
            <div style={{position: 'absolute', left: trackX, top: y + rowH * 0.2, width: trackW, height: rowH * 0.6, borderRadius: rowH * 0.3,
              background: CLAUDE.PILL, opacity: 0.45 + 0.55 * t}} />
            <div style={{position: 'absolute', left: trackX, top: y + rowH * 0.2, width: Math.max(rowH * 0.6, trackW * p.bar * grow),
              height: rowH * 0.6, borderRadius: rowH * 0.3, background: INK, opacity: t}} />
          </React.Fragment>
        );
      })}
      <div style={{position: 'absolute', right: width - S.r,
        top: portrait ? barsTop + titleH + 2 * (rowH + rowGap) + 20 : barsTop + titleH + (rowH + rowGap) + rowH / 2 - 40,
        padding: portrait ? '20px 34px' : '12px 28px', borderRadius: 20, border: `5px solid ${ACCENT}`, background: CLAUDE.CARD,
        fontFamily: SERIF, fontSize: T.serif, fontWeight: 700, color: INK, lineHeight: 1, whiteSpace: 'nowrap', opacity: moreIn,
        transform: `translateX(${-(1 - moreIn) * 30 - 8}px)`}}>{props.moreLabel}</div>
      <Caption text={props.caption} S={S} portrait={portrait} opacity={pop(props.curveAt)} />
      <LogoBug portrait={portrait} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B07 — format: a wall of text vs a short vertical video with the point first
// ─────────────────────────────────────────────────────────────────────────────
const side = z.object({title: z.string(), verdict: z.string(), at: z.number(), verdictAt: z.number()});
export const formatFitSchema = z.object({
  ...dur,
  sparkLine: z.string().default('Hook first.'),
  feedLabel: z.string().default('ON A VIDEO-FIRST FEED'),
  left: side.default({title: 'A wall of text', verdict: 'Scrolled past', at: 0.2, verdictAt: 0.4}),
  right: side.default({title: 'A short vertical video', verdict: 'Watched', at: 0.55, verdictAt: 0.92}),
  hookLabel: z.string().default('The point, in the first seconds'),
  hookAt: z.number().default(0.78),
});
export type FormatFitProps = z.infer<typeof formatFitSchema>;

const Phone: React.FC<{left: number; top: number; w: number; h: number; opacity: number; children: React.ReactNode}> = (
  {left, top, w, h, opacity, children}) => (
  <div style={{position: 'absolute', left, top, width: w, height: h, borderRadius: w * 0.12, background: INK, padding: w * 0.035,
    boxSizing: 'border-box', opacity, boxShadow: '0 18px 50px rgba(61,57,41,0.22)'}}>
    <div style={{position: 'relative', width: '100%', height: '100%', borderRadius: w * 0.09, background: CLAUDE.PAGE, overflow: 'hidden'}}>
      {children}
    </div>
  </div>
);

export const FormatFit: React.FC<FormatFitProps> = (props) => {
  const {portrait, S, pop, ramp, p} = useBeat(props.durationSeconds);
  const T = ty(portrait);
  const lIn = pop(props.left.at), rIn = pop(props.right.at);
  const scroll = ramp(props.left.verdictAt - 0.04, 0.16);
  const hookIn = ramp(props.hookAt, 0.06);
  const phoneW = portrait ? 440 : 420, phoneH = portrait ? 800 : 780;
  const top = portrait ? S.y + 260 + 90 : 200;
  const half = portrait ? S.w / 2 : S.w / 2;
  const phones = portrait
    ? [{x: S.x + (half - phoneW) / 2, y: top}, {x: S.x + half + (half - phoneW) / 2, y: top}]
    : [{x: S.x, y: top}, {x: S.x + half, y: top}];
  const textX = (i: number) => portrait ? S.x + i * half : phones[i].x + phoneW + 50;
  const textW = portrait ? half : half - phoneW - 60;
  const textY = portrait ? top + phoneH + 40 : top + 90;
  // right phone: playhead
  const play = clamp01((p - props.right.at) / Math.max(0.05, 1 - props.right.at));
  const inner = {w: phoneW * 0.93, h: phoneH * 0.93};
  const barY = inner.h - (portrait ? 70 : 56), barX = 26, barW = inner.w - 52;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={portrait} S={S} />
      <div style={{position: 'absolute', left: S.x, width: S.w, top: portrait ? S.y + 250 : 136, textAlign: 'center', fontFamily: SANS,
        fontSize: portrait ? T.sans : 40, fontWeight: 700, letterSpacing: '0.08em', color: SOFT, lineHeight: 1,
        opacity: lIn}}>{props.feedLabel}</div>
      <Phone left={phones[0].x} top={phones[0].y} w={phoneW} h={phoneH} opacity={0.45 + 0.55 * lIn}>
        <div style={{position: 'absolute', left: 0, top: -scroll * inner.h * 0.9, width: '100%', padding: 26, boxSizing: 'border-box'}}>
          {Array.from({length: 26}, (_, i) => (
            <div key={i} style={{height: portrait ? 16 : 13, borderRadius: 8, background: CLAUDE.GHOST, opacity: 0.7,
              width: `${i % 5 === 4 ? 58 : 92 - (i * 7) % 14}%`, marginBottom: portrait ? 18 : 15}} />
          ))}
        </div>
        <svg width={inner.w} height={inner.h} style={{position: 'absolute', left: 0, top: 0, opacity: scroll > 0 ? 1 : 0}}>
          <path d={`M ${inner.w / 2} ${inner.h * 0.72} L ${inner.w / 2} ${inner.h * 0.3} M ${inner.w / 2 - 44} ${inner.h * 0.3 + 44} L ${inner.w / 2} ${inner.h * 0.3} L ${inner.w / 2 + 44} ${inner.h * 0.3 + 44}`}
            fill="none" stroke={INK} strokeWidth={10} strokeLinecap="round" strokeLinejoin="round" opacity={clamp01(scroll * 3)} />
        </svg>
      </Phone>
      <Phone left={phones[1].x} top={phones[1].y} w={phoneW} h={phoneH} opacity={0.45 + 0.55 * rIn}>
        <svg width={inner.w} height={inner.h} style={{position: 'absolute', left: 0, top: 0}}>
          <rect x={0} y={0} width={inner.w} height={inner.h} fill={CLAUDE.FOOTER} />
          <circle cx={inner.w * 0.5} cy={inner.h * 0.3} r={inner.w * 0.2} fill={CLAUDE.PILL} stroke={INK} strokeWidth={5} />
          <rect x={inner.w * 0.18} y={inner.h * 0.5} width={inner.w * 0.64} height={inner.h * 0.06} rx={10} fill={INK} opacity={0.85} />
          <rect x={inner.w * 0.26} y={inner.h * 0.59} width={inner.w * 0.48} height={inner.h * 0.045} rx={10} fill={SOFT} opacity={0.7} />
          <path d={`M ${inner.w * 0.44} ${inner.h * 0.24} L ${inner.w * 0.6} ${inner.h * 0.3} L ${inner.w * 0.44} ${inner.h * 0.36} Z`} fill={INK}
            opacity={1 - clamp01(play * 8)} />
          <rect x={barX} y={barY} width={barW} height={14} rx={7} fill={CLAUDE.BORDER} />
          <rect x={barX} y={barY} width={barW * play} height={14} rx={7} fill={INK} />
          <rect x={barX} y={barY - 5} width={barW * 0.16 * hookIn} height={24} rx={12} fill={ACCENT} />
          <circle cx={barX + barW * play} cy={barY + 7} r={15} fill={INK} opacity={rIn} />
        </svg>
      </Phone>
      {[props.left, props.right].map((s, i) => {
        const t = i === 0 ? lIn : rIn;
        const v = pop(s.verdictAt);
        return (
          <div key={i} style={{position: 'absolute', left: textX(i), top: textY, width: textW, textAlign: portrait ? 'center' : 'left'}}>
            <div style={{fontFamily: SERIF, fontSize: portrait ? T.serif : 60, fontWeight: 700, color: INK, lineHeight: 1.05, opacity: t}}>{s.title}</div>
            <div style={{fontFamily: SERIF, fontSize: portrait ? T.serif : 60, fontStyle: 'italic', color: i === 0 ? SOFT : INK,
              lineHeight: 1.05, marginTop: portrait ? 26 : 30, opacity: v, display: 'flex', alignItems: 'center', gap: 14,
              justifyContent: portrait ? 'center' : 'flex-start'}}>
              {i === 1 && <Check size={portrait ? 80 : 58} />}{s.verdict}
            </div>
          </div>
        );
      })}
      {!portrait && (
        <div style={{position: 'absolute', left: textX(1), top: textY + 360, width: textW, fontFamily: SANS, fontSize: T.sans,
          fontWeight: 700, color: INK, lineHeight: 1.12, opacity: hookIn}}>
          <span style={{display: 'inline-block', width: 60, height: 20, borderRadius: 10, background: ACCENT, marginRight: 16}} />
          {props.hookLabel}
        </div>
      )}
      {portrait && (
        <div style={{position: 'absolute', left: S.x, width: S.w, top: textY + 290, textAlign: 'center', fontFamily: SANS,
          fontSize: T.sans, fontWeight: 700, color: INK, lineHeight: 1.1, opacity: hookIn}}>
          <span style={{display: 'inline-block', width: 80, height: 26, borderRadius: 13, background: ACCENT, marginRight: 20}} />
          {props.hookLabel}
        </div>
      )}
      <LogoBug portrait={portrait} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B08 — the algorithm: small test group → signals → bigger audience (the loop)
// ─────────────────────────────────────────────────────────────────────────────
export const signalLoopSchema = z.object({
  ...dur,
  sparkLine: z.string().default('The algorithm reads signals.'),
  testLabel: z.string().default('Small test group'),
  testAt: z.number().default(0.17),
  signalsTitle: z.string().default('SIGNALS'),
  signals: z.array(z.object({label: z.string(), at: z.number()})).default([
    {label: 'Watch time', at: 0.41}, {label: 'Saves', at: 0.44}, {label: 'Shares', at: 0.47}, {label: 'Comments', at: 0.53},
  ]),
  growAt: z.number().default(0.64),
  grow2At: z.number().default(0.79),
  strongLabel: z.string().default('Strong → bigger audience, and repeat'),
  weakLabel: z.string().default('Weak → it stops'),
  weakAt: z.number().default(0.89),
  caption: z.string().default('Simplified — every platform ranks differently'),
});
export type SignalLoopProps = z.infer<typeof signalLoopSchema>;

export const SignalLoop: React.FC<SignalLoopProps> = (props) => {
  const {portrait, S, pop, ramp, width, height} = useBeat(props.durationSeconds);
  const T = ty(portrait);
  const c = portrait ? {x: S.x + S.w / 2, y: S.y + 260 + 360} : {x: S.x + 410, y: 555};
  const radii = portrait ? [120, 235, 350] : [120, 250, 370];
  const counts = [6, 12, 18];
  const ringIn = [pop(props.testAt), pop(props.growAt), pop(props.grow2At)];
  const loop = ramp(props.growAt - 0.02, 0.2);
  const col = portrait
    ? {x: S.x, y: c.y + radii[2] + 70, w: S.w}
    : {x: S.x + 900, y: 170, w: S.w - 900};
  const chipGap = portrait ? 22 : 22;
  const chipW = (col.w - chipGap) / 2, chipH = portrait ? 130 : 112;
  const listTop = col.y + (portrait ? 0 : 76);
  const afterChips = listTop + 2 * (chipH + chipGap) + (portrait ? 20 : 26);
  const ps = portrait ? 76 : 58;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={portrait} S={S} />
      <svg width={width} height={height} style={{position: 'absolute', left: 0, top: 0}}>
        {radii.map((r, i) => (
          <circle key={i} cx={c.x} cy={c.y} r={r * (0.85 + 0.15 * ringIn[i])} fill="none" stroke={CLAUDE.BORDER} strokeWidth={4}
            strokeDasharray={i === 0 ? undefined : '12 12'} opacity={ringIn[i]} />
        ))}
        {radii.map((r, i) => Array.from({length: counts[i]}, (_, k) => {
          const a = (k / counts[i]) * Math.PI * 2 + i * 0.3 - Math.PI / 2;
          return <Person key={`${i}-${k}`} x={c.x + Math.cos(a) * r * (0.85 + 0.15 * ringIn[i])} y={c.y + Math.sin(a) * r * (0.85 + 0.15 * ringIn[i])}
            s={ps} joined={portrait} fill={INK} opacity={ringIn[i]} />;
        }))}
        {/* the loop: accent arc sweeping around the middle ring */}
        <path d={`M ${c.x} ${c.y - radii[1] - 40} A ${radii[1] + 40} ${radii[1] + 40} 0 1 1 ${c.x - (radii[1] + 40) * Math.sin(0.6)} ${c.y - (radii[1] + 40) * Math.cos(0.6)}`}
          fill="none" stroke={ACCENT} strokeWidth={9} strokeLinecap="round" pathLength={1} strokeDasharray={1} strokeDashoffset={1 - loop}
          opacity={loop > 0 ? 1 : 0} />
      </svg>
      <div style={{position: 'absolute', left: c.x - 90, top: c.y - 90, width: 180, height: 180, borderRadius: 30, background: CLAUDE.CARD,
        border: `3px solid ${INK}`, display: 'flex', alignItems: 'center', justifyContent: 'center', opacity: pop(0.03)}}>
        <PostGlyph size={120} />
      </div>
      <div style={{position: 'absolute', left: c.x - 300, width: 600, top: c.y + radii[0] + (portrait ? -8 : 50), textAlign: 'center',
        fontFamily: SANS, fontSize: portrait ? T.sans : 46, fontWeight: 700, color: SOFT, lineHeight: 1, opacity: ringIn[0] * (1 - ringIn[1]),
        display: portrait ? 'none' : 'block'}}>{props.testLabel}</div>
      {!portrait && (
        <div style={{position: 'absolute', left: col.x, top: col.y, fontFamily: SANS, fontSize: T.sans, fontWeight: 700,
          letterSpacing: '0.1em', color: SOFT, lineHeight: 1, opacity: pop(props.signals[0]?.at ?? 0.4)}}>{props.signalsTitle}</div>
      )}
      {props.signals.map((s, i) => {
        const t = pop(s.at);
        return (
          <Card key={i} style={{position: 'absolute', left: col.x + (i % 2) * (chipW + chipGap), top: listTop + Math.floor(i / 2) * (chipH + chipGap),
            width: chipW, height: chipH, boxSizing: 'border-box', display: 'flex', alignItems: 'center', justifyContent: 'center',
            fontFamily: SERIF, fontSize: T.serif, fontWeight: 700, color: INK, lineHeight: 1, opacity: 0.45 + 0.55 * t,
            transform: `translateY(${(1 - t) * 20}px)`, whiteSpace: 'nowrap'}}>{s.label}</Card>
        );
      })}
      <div style={{position: 'absolute', left: col.x, width: col.w, top: afterChips, fontFamily: SERIF, fontSize: T.serif, fontWeight: 700,
        color: INK, lineHeight: 1.08, opacity: pop(props.growAt), textAlign: portrait ? 'center' : 'left'}}>{props.strongLabel}</div>
      <div style={{position: 'absolute', left: col.x, width: col.w, top: afterChips + (portrait ? 140 : 150), fontFamily: SERIF,
        fontSize: T.serif, fontStyle: 'italic', color: SOFT, lineHeight: 1.08, opacity: pop(props.weakAt), display: 'flex', alignItems: 'center',
        gap: 20, justifyContent: portrait ? 'center' : 'flex-start'}}>
        <span style={{display: 'inline-block', width: portrait ? 60 : 46, height: portrait ? 60 : 46, borderRadius: 8, background: SOFT}} />
        {props.weakLabel}
      </div>
      <Caption text={props.caption} S={S} portrait={portrait} opacity={pop(0.03)} />
      <LogoBug portrait={portrait} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B09 — paid reach: a boost to the wrong audience vs the right one
// ─────────────────────────────────────────────────────────────────────────────
const lane = z.object({label: z.string(), views: z.number(), results: z.number(), at: z.number(), resAt: z.number()});
export const paidReachSchema = z.object({
  ...dur,
  sparkLine: z.string().default('Paid buys reach, not fit.'),
  boostLabel: z.string().default('Boost post'),
  boostAt: z.number().default(0.02),
  metricA: z.string().default('Views'),
  metricB: z.string().default('Follows & sales'),
  lanes: z.array(lane).default([
    {label: 'Boost → wrong audience', views: 0.9, results: 0.07, at: 0.26, resAt: 0.5},
    {label: 'Boost → right audience', views: 0.72, results: 0.64, at: 0.73, resAt: 0.84},
  ]),
  line: z.string().default('Paid amplifies what already fits.'),
  lineAt: z.number().default(0.9),
  caption: z.string().default('Illustrative — no real data'),
});
export type PaidReachProps = z.infer<typeof paidReachSchema>;

export const PaidReach: React.FC<PaidReachProps> = (props) => {
  const {portrait, S, pop, ramp} = useBeat(props.durationSeconds);
  const T = ty(portrait);
  const bIn = pop(props.boostAt);
  const top = portrait ? S.y + 260 : 150;
  const boostH = portrait ? 130 : 96;
  const laneTop = top + boostH + (portrait ? 50 : 34);
  const laneH = portrait ? 520 : 280, laneGap = portrait ? 40 : 30;
  const labelW = portrait ? 0 : 420;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={portrait} S={S} />
      <div style={{position: 'absolute', left: S.x, top, height: boostH, padding: `0 ${portrait ? 44 : 36}px`, borderRadius: boostH / 2,
        background: INK, color: CLAUDE.PAGE, display: 'flex', alignItems: 'center', gap: 20, fontFamily: SANS,
        fontSize: T.sans, fontWeight: 700, lineHeight: 1, opacity: bIn, transform: `scale(${1.1 - 0.1 * bIn})`, transformOrigin: 'left center'}}>
        <svg width={T.sans} height={T.sans} viewBox="0 0 100 100"><path d="M 50 8 L 88 58 L 62 58 L 62 92 L 38 92 L 38 58 L 12 58 Z" fill={CLAUDE.PAGE} /></svg>
        {props.boostLabel}
      </div>
      {props.lanes.map((ln, i) => {
        const y = laneTop + i * (laneH + laneGap);
        const t = pop(ln.at);
        const good = i === props.lanes.length - 1;
        const vGrow = ramp(ln.at + 0.02, 0.14), rGrow = ramp(ln.resAt, 0.1);
        const rows: [string, number, number, boolean][] = [[props.metricA, ln.views, vGrow, false], [props.metricB, ln.results, rGrow, good]];
        const trackX = S.x + 40 + labelW, trackW = S.r - 40 - trackX;
        return (
          <Card key={i} style={{position: 'absolute', left: S.x, top: y, width: S.w, height: laneH, boxSizing: 'border-box',
            padding: `${portrait ? 30 : 26}px 40px`, opacity: 0.45 + 0.55 * t}}>
            <div style={{fontFamily: SERIF, fontSize: portrait ? T.serif : 58, fontWeight: 700, color: INK, lineHeight: 1, whiteSpace: 'nowrap'}}>{ln.label}</div>
            {rows.map(([lab, v, g, accent], k) => {
              const ry = portrait ? 150 + k * 175 : 100 + k * 84;
              const barH = portrait ? 56 : 50;
              return (
                <React.Fragment key={k}>
                  <div style={{position: 'absolute', left: 40, top: portrait ? ry : ry + barH / 2 - 22, fontFamily: SANS, fontSize: T.sans,
                    fontWeight: 700, color: SOFT, lineHeight: 1, whiteSpace: 'nowrap'}}>{lab}</div>
                  <div style={{position: 'absolute', left: trackX - S.x, top: portrait ? ry + 92 : ry, width: trackW, height: barH,
                    borderRadius: barH / 2, background: CLAUDE.PILL}} />
                  <div style={{position: 'absolute', left: trackX - S.x, top: portrait ? ry + 92 : ry, width: Math.max(barH, trackW * v * g),
                    height: barH, borderRadius: barH / 2, background: accent ? ACCENT : INK, opacity: g > 0 ? 1 : 0.35}} />
                </React.Fragment>
              );
            })}
          </Card>
        );
      })}
      <div style={{position: 'absolute', left: S.x, width: S.w, top: laneTop + 2 * laneH + laneGap + (portrait ? 40 : 30), textAlign: 'center',
        fontFamily: SERIF, fontSize: portrait ? T.serif : 60, fontWeight: 700, fontStyle: 'italic', color: INK, lineHeight: 1,
        opacity: pop(props.lineAt)}}>{props.line}</div>
      {!portrait && <Caption text={props.caption} S={S} portrait={portrait} opacity={bIn} />}
      <LogoBug portrait={portrait} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B10 — falsifiability: diagnose before you blame (sometimes it IS the content)
// ─────────────────────────────────────────────────────────────────────────────
export const diagnoseFlowSchema = z.object({
  ...dur,
  sparkLine: z.string().default('Diagnose before you blame.'),
  headline: z.string().default('Sometimes it is the content.'),
  headAt: z.number().default(0.06),
  noLabel: z.string().default('No'),
  steps: z.array(z.object({q: z.string(), fix: z.string(), at: z.number(), fixAt: z.number()})).default([
    {q: 'Did the right people see it?', fix: 'Fix fit & distribution', at: 0.33, fixAt: 0.45},
    {q: 'Did they stop?', fix: 'Fix format & the hook', at: 0.59, fixAt: 0.67},
    {q: 'Did they act?', fix: 'Rework the content', at: 0.81, fixAt: 0.88},
  ]),
});
export type DiagnoseFlowProps = z.infer<typeof diagnoseFlowSchema>;

export const DiagnoseFlow: React.FC<DiagnoseFlowProps> = (props) => {
  const {portrait, S, pop, width, height} = useBeat(props.durationSeconds);
  const T = ty(portrait);
  const headTop = portrait ? S.y + 250 : 136;
  const rowsTop = portrait ? headTop + 250 : 250;
  const n = props.steps.length;
  const rowH = portrait ? 370 : 230, gap = portrait ? 30 : 28;
  const qW = portrait ? S.w : 900, fixX = portrait ? S.x + 110 : S.x + 1150, fixW = portrait ? S.w - 110 : S.r - (S.x + 1150);
  const qH = portrait ? 200 : rowH, fixH = portrait ? 140 : 150;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={portrait} S={S} />
      <div style={{position: 'absolute', left: S.x, width: S.w, top: headTop, textAlign: 'center', fontFamily: SERIF,
        fontSize: portrait ? T.serif : 62, fontStyle: 'italic', color: INK, lineHeight: 1.05, opacity: pop(props.headAt)}}>{props.headline}</div>
      <svg width={width} height={height} style={{position: 'absolute', left: 0, top: 0}}>
        {props.steps.map((s, i) => {
          const y = rowsTop + i * (rowH + gap);
          const t = pop(s.fixAt);
          const d = portrait
            ? `M ${S.x + 70} ${y + qH} L ${S.x + 70} ${y + qH + 20 + fixH / 2} L ${fixX - 30} ${y + qH + 20 + fixH / 2}`
            : `M ${S.x + qW + 20} ${y + rowH / 2} L ${fixX - 30} ${y + rowH / 2}`;
          const hx = portrait ? fixX - 30 : fixX - 30, hy = portrait ? y + qH + 20 + fixH / 2 : y + rowH / 2;
          return (
            <g key={i} opacity={t}>
              <path d={d} fill="none" stroke={INK} strokeWidth={6} strokeLinecap="round" strokeLinejoin="round" />
              <path d={`M ${hx - 22} ${hy - 18} L ${hx} ${hy} L ${hx - 22} ${hy + 18}`} fill="none" stroke={INK} strokeWidth={6}
                strokeLinecap="round" strokeLinejoin="round" />
            </g>
          );
        })}
      </svg>
      {props.steps.map((s, i) => {
        const y = rowsTop + i * (rowH + gap);
        const qIn = pop(s.at), fIn = pop(s.fixAt);
        const last = i === n - 1;
        return (
          <React.Fragment key={i}>
            <Card style={{position: 'absolute', left: S.x, top: y, width: qW, height: qH, boxSizing: 'border-box', padding: '0 40px',
              display: 'flex', alignItems: 'center', gap: 28, opacity: 0.45 + 0.55 * qIn}}>
              {portrait
                ? <span style={{fontFamily: SERIF, fontSize: T.serif, fontWeight: 700, color: SOFT, lineHeight: 1.05, marginRight: -10}}>{`${i + 1}.`}</span>
                : <div style={{width: 84, height: 84, borderRadius: 50, flexShrink: 0, background: INK, color: CLAUDE.PAGE,
                  display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SANS, fontSize: 48,
                  fontWeight: 700}}>{i + 1}</div>}
              <span style={{fontFamily: SERIF, fontSize: portrait ? T.serif : 60, fontWeight: 700, color: INK, lineHeight: 1.05}}>{s.q}</span>
            </Card>
            {!portrait && (
              <div style={{position: 'absolute', left: S.x + qW + 30, width: fixX - 30 - (S.x + qW + 30), top: y + rowH / 2 - 62, textAlign: 'center',
                fontFamily: SANS, fontSize: T.sans, fontWeight: 700, color: SOFT, lineHeight: 1, opacity: fIn}}>{props.noLabel}</div>
            )}
            <div style={{position: 'absolute', left: fixX, top: portrait ? y + qH + 20 : y + (rowH - fixH) / 2, width: fixW, height: fixH,
              boxSizing: 'border-box', padding: '0 30px', borderRadius: 22, background: CLAUDE.CARD,
              border: last ? `6px solid ${ACCENT}` : portrait ? `3px solid ${CLAUDE.BORDER}` : `3px solid ${INK}`, display: 'flex', alignItems: 'center',
              fontFamily: SERIF, fontSize: portrait ? T.serif : 54, fontWeight: 700, color: INK, lineHeight: 1.05, opacity: fIn,
              transform: `translateX(${(1 - fIn) * 24}px)`}}>{s.fix}</div>
          </React.Fragment>
        );
      })}
      <LogoBug portrait={portrait} />
    </AbsoluteFill>
  );
};
