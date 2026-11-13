/**
 * MaskSlips916.tsx — PORTRAIT (9:16) scenes for `yatra-the-mask-slips`.
 *
 * Re-banded vertically per the Shorts law's composition logic, NOT scaled clones.
 * Five of the landscape layouts are horizontal by nature and are genuinely rebuilt:
 *
 *   · MskBluf916   — the two phases STACK, and the divider becomes a horizontal rule
 *                    between them rather than a vertical one beside them.
 *   · MskSpike916  — the lead figure sits above its two scale figures instead of
 *                    beside them; three figures will not fit across 972px.
 *   · MskArc916    — the curve is re-plotted into a TALLER, NARROWER box with its
 *                    labels stacked beneath rather than flanking the peak.
 *   · MskReveal916 — the audience→person wire runs DOWN the frame, so the far node
 *                    sits below rather than to the right.
 *   · MskDrop916   — each case's bar gets its own row with the figure BELOW it, since
 *                    a 980px track plus a 600px figure column cannot coexist here.
 *
 * Every refusal holds, because the types are imported from MaskSlips.tsx rather than
 * redeclared: `source` is still required on every figure-bearing scene, values are still
 * strings printed verbatim, `MskMoney916` still requires its `stamp`, `MskArc916` still
 * requires its `axisNote`, and there is still no `name` prop by which either account
 * could be identified.
 *
 * KEEP-OUT: content stays above y≈1440 and left of x≈960 — the Shorts/Reels chrome
 * region — with the brand bug lower-left.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {SAFE916} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import type {
  BlufData, SpikeData, MoneyData, ArcData, RevealData, DropData, TurnData, LimitsData,
} from './MaskSlips';

const STAGE = '#F2F0E9';
const RULE = '#D8D4C8';
const MUTE = '#7A7265';
/** working box: full safe width, but critical content is kept left of x≈960 */
const BOX = {x: SAFE916.x, y: SAFE916.y, w: 972, keep: 960, bottom: 1440} as const;

const ease = (t: number) => 1 - Math.pow(1 - Math.min(1, Math.max(0, t)), 3);
const win = (p: number, a: number, b: number) => ease((p - a) / (b - a));

const useP = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));
};

const LogoBug916: React.FC = () => (
  <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom + 40, fontFamily: CLAUDE_FONT.serif, fontSize: 30, color: CLAUDE.INK, opacity: 0.3, letterSpacing: '.04em'}}>
    @Yatra
  </div>
);

const Stage: React.FC<{children: React.ReactNode}> = ({children}) => (
  <AbsoluteFill style={{backgroundColor: STAGE}}>
    {children}
    <LogoBug916 />
  </AbsoluteFill>
);

const Eyebrow: React.FC<{text: string; opacity?: number}> = ({text, opacity = 1}) => (
  <div style={{position: 'absolute', left: BOX.x, top: BOX.y, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.16em', color: MUTE, fontWeight: 600, opacity}}>
    {text.toUpperCase()}
  </div>
);

const Head: React.FC<{meta: string; title: string}> = ({meta, title}) => (
  <>
    <Eyebrow text={meta} />
    <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 76, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 72, color: CLAUDE.INK, lineHeight: 1.06}}>
      {title}
    </div>
  </>
);

const Note: React.FC<{note: string; opacity: number; accent?: boolean}> = ({note, opacity, accent}) => (
  <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 96, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 38, color: accent ? CLAUDE.SPARK : CLAUDE.INK, lineHeight: 1.25, opacity}}>
    {note}
  </div>
);

/** Provenance. Always MUTE — a citation is not emphasis. */
const SourceLine: React.FC<{source: string; opacity: number; top?: number}> = ({source, opacity, top}) => (
  <div style={{position: 'absolute', left: BOX.x, top: top ?? BOX.bottom - 166, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE, opacity, lineHeight: 1.25}}>
    Source: {source}
  </div>
);

const Chip: React.FC<{
  text: string; left: number; top: number; hot?: boolean; opacity: number; size?: number;
}> = ({text, left, top, hot, opacity, size = 24}) => (
  <div
    style={{
      position: 'absolute', left, top, opacity,
      fontFamily: CLAUDE_FONT.ui, fontSize: size, fontWeight: 600,
      letterSpacing: '.14em', textTransform: 'uppercase' as const,
      color: hot ? CLAUDE.SPARK : MUTE,
      border: `1px solid ${hot ? CLAUDE.SPARK : RULE}`,
      padding: '9px 15px', display: 'inline-block', whiteSpace: 'nowrap' as const,
    }}
  >
    {text}
  </div>
);

/* ── B01 — the two phases STACK; the divider becomes a horizontal rule ───── */
export const MskBluf916: React.FC<{data: BlufData}> = ({data}) => {
  const p = useP();
  const TOP_A = BOX.y + 170;
  const TOP_B = BOX.y + 760;
  const divide = win(p, 0.36, 0.56);

  const phase = (y: number, head: string, lines: string[], at: number, hot: boolean) => (
    <>
      <Chip text={head} left={BOX.x} top={y} hot={hot} opacity={win(p, at, at + 0.1)} size={26} />
      {lines.map((ln, i) => {
        const g = win(p, at + 0.08 + i * 0.1, at + 0.26 + i * 0.1);
        return (
          <div
            key={i}
            style={{
              position: 'absolute', left: BOX.x, top: y + 90 + i * 190, width: BOX.w,
              fontFamily: CLAUDE_FONT.serif, fontSize: 70, lineHeight: 1.18,
              color: hot ? CLAUDE.SPARK : CLAUDE.INK,
              opacity: g, transform: `translateY(${(1 - g) * 18}px)`,
            }}
          >
            {ln}
          </div>
        );
      })}
    </>
  );

  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.16)} />
      {phase(TOP_A, data.firstHead, data.firstLines, 0.08, false)}
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 690, width: BOX.w * divide, height: 2, backgroundColor: RULE}} />
      {phase(TOP_B, data.secondHead, data.secondLines, 0.52, true)}
      <Note note={data.closer} opacity={win(p, 0.86, 0.97)} />
    </Stage>
  );
};

/* ── B02 — the lead figure sits ABOVE its two scale figures ──────────────── */
export const MskSpike916: React.FC<{data: SpikeData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 250;
  const lead = win(p, 0.06, 0.26);

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />

      <div
        style={{
          position: 'absolute', left: BOX.x, top: TOP, width: BOX.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 180, lineHeight: 1,
          color: CLAUDE.INK, opacity: lead, transform: `translateY(${(1 - lead) * 20}px)`,
        }}
      >
        {data.lead.value}
      </div>
      <div
        style={{
          position: 'absolute', left: BOX.x, top: TOP + 200, width: BOX.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 32, color: MUTE, lineHeight: 1.3,
          opacity: win(p, 0.18, 0.34),
        }}
      >
        {data.lead.label}
      </div>

      {data.figures.map((f, i) => {
        const g = win(p, 0.34 + i * 0.22, 0.54 + i * 0.22);
        const y = TOP + 320 + i * 220;
        return (
          <React.Fragment key={i}>
            <div
              style={{
                position: 'absolute', left: BOX.x, top: y, width: BOX.w,
                fontFamily: CLAUDE_FONT.serif, fontSize: 108, lineHeight: 1,
                color: CLAUDE.INK, opacity: g, transform: `translateY(${(1 - g) * 16}px)`,
              }}
            >
              {f.value}
            </div>
            <div
              style={{
                position: 'absolute', left: BOX.x, top: y + 122, width: BOX.w,
                fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE,
                opacity: win(p, 0.4 + i * 0.22, 0.6 + i * 0.22),
              }}
            >
              {f.label}
            </div>
          </React.Fragment>
        );
      })}

      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 232, width: BOX.w * win(p, 0.76, 0.9), height: 2, backgroundColor: RULE}} />
      <div style={{position: 'absolute', left: BOX.x + 54, top: BOX.bottom - 256, width: 6, height: 50 * win(p, 0.86, 0.96), backgroundColor: CLAUDE.SPARK}} />

      <SourceLine source={data.source} opacity={win(p, 0.78, 0.9)} />
      <Note note={data.note} opacity={win(p, 0.9, 0.99)} />
    </Stage>
  );
};

/* ── B03 — one figure, sized for portrait ────────────────────────────────── */
export const MskMoney916: React.FC<{data: MoneyData}> = ({data}) => {
  const p = useP();
  const set = win(p, 0.08, 0.3);
  const TOP = BOX.y + 330;

  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.16)} />

      <div
        style={{
          position: 'absolute', left: BOX.x, top: TOP, width: BOX.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 210, lineHeight: 1,
          color: CLAUDE.INK, opacity: set, transform: `translateY(${(1 - set) * 24}px)`,
        }}
      >
        {data.value}
      </div>
      <div
        style={{
          position: 'absolute', left: BOX.x, top: TOP + 250, width: BOX.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 62, color: CLAUDE.INK, lineHeight: 1.2,
          opacity: win(p, 0.3, 0.48),
        }}
      >
        {data.qualifier}
      </div>
      <Chip text={data.stamp} left={BOX.x} top={TOP + 350} opacity={win(p, 0.48, 0.64)} size={26} />

      <SourceLine source={data.source} opacity={win(p, 0.7, 0.84)} />
      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 116, width: BOX.w * 0.6 * win(p, 0.84, 0.95), height: 5, backgroundColor: CLAUDE.SPARK}} />
      <Note note={data.note} opacity={win(p, 0.86, 0.97)} />
    </Stage>
  );
};

/* ── B05 — the curve re-plotted taller and narrower; labels stack beneath ── */
export const MskArc916: React.FC<{data: ArcData}> = ({data}) => {
  const p = useP();
  const rise = win(p, 0.06, 0.38);
  const mark = win(p, 0.52, 0.66);
  const fall = win(p, 0.66, 0.9);

  const X0 = BOX.x + 20;
  const Y0 = BOX.y + 900;
  const PEAK_X = BOX.x + 470;
  const PEAK_Y = BOX.y + 330;
  const END_X = BOX.x + 930;
  const END_Y = Y0 - 150;

  const risePath = `M ${X0} ${Y0} C ${X0 + 150} ${Y0} ${PEAK_X - 110} ${PEAK_Y + 50} ${PEAK_X} ${PEAK_Y}`;
  const fallPath = `M ${PEAK_X} ${PEAK_Y} C ${PEAK_X + 130} ${PEAK_Y + 80} ${END_X - 150} ${END_Y - 50} ${END_X} ${END_Y}`;

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />

      <svg width={1080} height={1920} style={{position: 'absolute', left: 0, top: 0}} viewBox="0 0 1080 1920">
        <line x1={X0} y1={Y0} x2={END_X} y2={Y0} stroke={RULE} strokeWidth={2} />
        <path d={risePath} fill="none" stroke={CLAUDE.INK} strokeWidth={8} strokeLinecap="round" pathLength={1} strokeDasharray={1} strokeDashoffset={1 - rise} />
        <path d={fallPath} fill="none" stroke={CLAUDE.INK} strokeWidth={8} strokeLinecap="round" opacity={0.55} pathLength={1} strokeDasharray={1} strokeDashoffset={1 - fall} />
        <line x1={PEAK_X} y1={PEAK_Y - 50} x2={PEAK_X} y2={PEAK_Y + 140 * mark} stroke={CLAUDE.SPARK} strokeWidth={5} opacity={mark} />
        <circle cx={PEAK_X} cy={PEAK_Y} r={17 * mark} fill={CLAUDE.SPARK} />
      </svg>

      <div style={{position: 'absolute', left: BOX.x, top: Y0 + 28, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE, opacity: win(p, 0.2, 0.36)}}>
        {data.riseLabel}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: Y0 + 78, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 40, fontWeight: 600, color: CLAUDE.SPARK, opacity: mark, lineHeight: 1.2}}>
        {data.markerLabel}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: Y0 + 136, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE, opacity: win(p, 0.82, 0.94)}}>
        {data.fallLabel}
      </div>

      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 162, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE, lineHeight: 1.3, opacity: win(p, 0.86, 0.96)}}>
        {data.axisNote}
      </div>
      <Note note={data.note} opacity={win(p, 0.9, 0.99)} />
    </Stage>
  );
};

/* ── B06 — the wire runs DOWN the frame ──────────────────────────────────── */
export const MskReveal916: React.FC<{data: RevealData}> = ({data}) => {
  const p = useP();
  const draw = win(p, 0.06, 0.26);
  const strike = win(p, 0.5, 0.64);
  const after = win(p, 0.58, 0.72);
  const dash = win(p, 0.68, 0.84);

  const TOP_Y = BOX.y + 260;
  const BOT_Y = BOX.y + 760;
  const NODE_H = 170;

  const node = (y: number, label: string, g: number, struck: boolean, hot: boolean) => (
    <div
      style={{
        position: 'absolute', left: BOX.x, top: y, width: BOX.w, minHeight: NODE_H,
        boxSizing: 'border-box', border: `2px solid ${hot ? CLAUDE.SPARK : CLAUDE.INK}`,
        borderRadius: 14, backgroundColor: '#FFFFFF',
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        padding: '18px 24px', textAlign: 'center',
        fontFamily: CLAUDE_FONT.serif, fontSize: 58, lineHeight: 1.15,
        color: hot ? CLAUDE.SPARK : CLAUDE.INK, opacity: g,
      }}
    >
      <span style={{position: 'relative', display: 'inline-block'}}>
        {label}
        {struck ? (
          <span style={{position: 'absolute', left: 0, top: '52%', width: `${100 * strike}%`, height: 5, backgroundColor: CLAUDE.INK}} />
        ) : null}
      </span>
    </div>
  );

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />

      {/* the wire, vertical */}
      <div
        style={{
          position: 'absolute', left: BOX.x + BOX.w / 2 - 3, top: TOP_Y + NODE_H,
          width: 6, height: (BOT_Y - TOP_Y - NODE_H) * draw,
          backgroundColor: dash > 0.02 ? 'transparent' : CLAUDE.INK,
          backgroundImage: dash > 0.02
            ? `repeating-linear-gradient(180deg, ${CLAUDE.SPARK} 0 22px, transparent 22px 44px)`
            : 'none',
        }}
      />
      <div
        style={{
          position: 'absolute', left: BOX.x + BOX.w / 2 + 28, top: TOP_Y + NODE_H + 60,
          width: 420, fontFamily: CLAUDE_FONT.ui, fontSize: 30,
          color: dash > 0.5 ? CLAUDE.SPARK : MUTE, opacity: win(p, 0.26, 0.4),
        }}
      >
        {data.wireLabel}
      </div>

      {node(TOP_Y, data.leftLabel, draw, false, false)}
      {after < 0.5 ? node(BOT_Y, data.rightBefore, draw, strike > 0.02, false)
                   : node(BOT_Y, data.rightAfter, after, false, true)}

      <div
        style={{
          position: 'absolute', left: BOX.x, top: BOX.bottom - 200, width: BOX.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 58, color: CLAUDE.SPARK, lineHeight: 1.2,
          opacity: win(p, 0.84, 0.94),
        }}
      >
        {data.verdict}
      </div>
      <Note note={data.note} opacity={win(p, 0.9, 0.99)} />
    </Stage>
  );
};

/* ── B07 — each case gets its own row, figure BELOW the bar ──────────────── */
export const MskDrop916: React.FC<{data: DropData}> = ({data}) => {
  const p = useP();
  const TRACK_W = BOX.w;
  const TOP = BOX.y + 250;
  const ROW = 400;

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />

      {data.cases.map((c, i) => {
        const at = 0.1 + i * 0.3;
        const grow = win(p, at, at + 0.12);
        const halve = win(p, at + 0.16, at + 0.3);
        const y = TOP + i * ROW;
        return (
          <React.Fragment key={i}>
            <div
              style={{
                position: 'absolute', left: BOX.x, top: y, width: BOX.w,
                fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: CLAUDE.INK,
                opacity: grow, lineHeight: 1.28,
              }}
            >
              {c.label}
            </div>
            <div style={{position: 'absolute', left: BOX.x, top: y + 106, width: TRACK_W * grow, height: 66, border: `2px dashed ${RULE}`, boxSizing: 'border-box'}} />
            <div
              style={{
                position: 'absolute', left: BOX.x, top: y + 106,
                width: TRACK_W * grow * (1 - 0.5 * halve), height: 66,
                backgroundColor: halve > 0.5 ? CLAUDE.SPARK : CLAUDE.INK,
                opacity: halve > 0.5 ? 0.9 : 0.82,
              }}
            />
            <div
              style={{
                position: 'absolute', left: BOX.x, top: y + 192, width: BOX.w,
                fontFamily: CLAUDE_FONT.serif, fontSize: 64, color: CLAUDE.SPARK,
                opacity: win(p, at + 0.22, at + 0.34), lineHeight: 1.1,
              }}
            >
              {c.value}
            </div>
            <div
              style={{
                position: 'absolute', left: BOX.x, top: y + 268, width: BOX.w,
                fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: MUTE,
                opacity: win(p, at + 0.26, at + 0.38), lineHeight: 1.28,
              }}
            >
              {c.detail}
            </div>
          </React.Fragment>
        );
      })}

      <div
        style={{
          position: 'absolute', left: BOX.x, top: TOP + data.cases.length * ROW - 60,
          width: TRACK_W, display: 'flex', justifyContent: 'space-between',
          fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE,
          opacity: win(p, 0.72, 0.84),
        }}
      >
        <span>{data.beforeLabel}</span>
        <span>{data.afterLabel}</span>
      </div>

      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} />
      <Note note={data.note} opacity={win(p, 0.9, 0.99)} />
    </Stage>
  );
};

/* ── B08 — already vertical; re-spaced for portrait ──────────────────────── */
export const MskTurn916: React.FC<{data: TurnData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 170;
  const STEP = 150;

  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />

      {data.ruledOut.map((r, i) => {
        const at = 0.08 + i * 0.2;
        const set = win(p, at, at + 0.08);
        const rule = win(p, at + 0.1, at + 0.2);
        return (
          <div key={i} style={{position: 'absolute', left: BOX.x, top: TOP + i * STEP, width: BOX.w}}>
            <div style={{position: 'relative', display: 'inline-block'}}>
              <span style={{fontFamily: CLAUDE_FONT.serif, fontSize: 62, color: CLAUDE.INK, opacity: set * (1 - 0.5 * rule)}}>
                {r}
              </span>
              <span style={{position: 'absolute', left: 0, top: 42, width: `${100 * rule}%`, height: 4, backgroundColor: CLAUDE.INK, opacity: 0.6}} />
            </div>
          </div>
        );
      })}

      <div
        style={{
          position: 'absolute', left: BOX.x, top: TOP + data.ruledOut.length * STEP + 90,
          width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 150, lineHeight: 1.05,
          color: CLAUDE.SPARK, opacity: win(p, 0.68, 0.82),
          transform: `translateY(${(1 - win(p, 0.68, 0.82)) * 22}px)`,
        }}
      >
        {data.survivor}
      </div>
      <div
        style={{
          position: 'absolute', left: BOX.x, top: BOX.bottom - 190, width: BOX.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 38, color: CLAUDE.INK, lineHeight: 1.28,
          opacity: win(p, 0.84, 0.94),
        }}
      >
        {data.closer}
      </div>
      <Note note={data.note} opacity={win(p, 0.92, 1.0)} />
    </Stage>
  );
};

/* ── B09 — the two ledgers STACK into two labelled groups ────────────────── */
export const MskLimits916: React.FC<{data: LimitsData}> = ({data}) => {
  const p = useP();
  const G1_Y = BOX.y + 250;
  const G2_Y = BOX.y + 720;
  const STEP = 122;

  const ledger = (y: number, heading: string, items: string[], startAt: number, hot: boolean) => (
    <>
      <div
        style={{
          position: 'absolute', left: BOX.x, top: y, width: BOX.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 27, letterSpacing: '.16em', fontWeight: 600,
          color: hot ? CLAUDE.SPARK : MUTE, opacity: win(p, startAt, startAt + 0.08),
        }}
      >
        {heading.toUpperCase()}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: y + 42, width: BOX.w * win(p, startAt, startAt + 0.12), height: 2, backgroundColor: hot ? CLAUDE.SPARK : RULE}} />
      {items.map((it, i) => {
        const g = win(p, startAt + 0.05 + i * 0.07, startAt + 0.2 + i * 0.07);
        return (
          <div
            key={i}
            style={{
              position: 'absolute', left: BOX.x, top: y + 74 + i * STEP, width: BOX.w,
              fontFamily: CLAUDE_FONT.ui, fontSize: 33, lineHeight: 1.3,
              color: hot ? CLAUDE.SPARK : CLAUDE.INK,
              opacity: g, transform: `translateY(${(1 - g) * 12}px)`,
            }}
          >
            · {it}
          </div>
        );
      })}
    </>
  );

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {ledger(G1_Y, data.claims.heading, data.claims.items, 0.08, false)}
      {ledger(G2_Y, data.refusals.heading, data.refusals.items, 0.44, true)}

      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 220, width: BOX.w * win(p, 0.78, 0.88), height: 1, backgroundColor: RULE}} />
      <div
        style={{
          position: 'absolute', left: BOX.x, top: BOX.bottom - 200, width: BOX.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 27, color: MUTE, lineHeight: 1.3,
          opacity: win(p, 0.8, 0.9),
        }}
      >
        {data.provenance}
      </div>
      <Note note={data.falsifier} opacity={win(p, 0.9, 0.99)} />
    </Stage>
  );
};
