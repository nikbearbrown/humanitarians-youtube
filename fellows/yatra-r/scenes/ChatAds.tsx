/**
 * ChatAds.tsx — reel-local scenes for `yatra-ads-in-the-picture`
 * ("Ads in the Picture." — ChatGPT testing visual ads in image generation, the same
 * week it introduces always-on agents).
 *
 * ── WHY THESE ARE NEW COMPONENTS ─────────────────────────────────────────────
 * The human asked for a video that is not a variation of any previous one. Nothing from
 * the `Tbl*`, `Msk*`, `Itm*`, `Wk*`, `Lnk*` or `Jdg*` families is reused. The shapes come
 * from this reel's argument: two rails that converge on one question, a spec sheet that
 * stamps in line by line, a generation screen with the ad held apart from the work, a
 * private space that becomes an audience, an always-on dot wired to a field of apps, two
 * cards that slide into one product, and a channel sequence whose last slot is open.
 *
 * ── THE SOURCING CONSTRAINT ──────────────────────────────────────────────────
 * Three points were supplied, all from one source (Jumpfly, October 2026), with the
 * instruction to add no detail or number beyond them. So:
 *
 *   · Every scene that states an announced fact REQUIRES a `source` string.
 *   · The ONLY figure in the reel is "over 4,000" (apps). `AdpDots` prints `value`
 *     verbatim and draws NO count from it — the tile field is decorative, and the scene
 *     REQUIRES a `tileNote` that says so on screen.
 *   · `AdpCanvas` is a redraw from a written description, not a screenshot: no product
 *     chrome, no logo, no real ad. It REQUIRES a `caption` saying so.
 *
 * ── ACCENT SEMANTICS ─────────────────────────────────────────────────────────
 * Terracotta is the ONE accent per beat and it always marks THE NEW THING ENTERING THE
 * SPACE — the testing stamp, the ad tag, the always-on dot, the seam where ads and agents
 * meet, the open last slot. The user's own work, and every citation, stays in ink.
 */
import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {CANVAS, SAFE} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {PlainStage, Head, RULE, MUTE, win} from './claudeStage';

export const useP = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));
};

/** characters of `text` revealed at progress g — typing, for the one reframe beat */
export const typed = (text: string, g: number) => text.slice(0, Math.round(text.length * g));

const NoteLine: React.FC<{note: string; opacity: number; accent?: boolean}> = ({note, opacity, accent}) => (
  <div
    style={{
      position: 'absolute', left: SAFE.x, top: SAFE.b - 62, width: SAFE.w,
      fontFamily: CLAUDE_FONT.serif, fontSize: 40,
      color: accent ? CLAUDE.SPARK : CLAUDE.INK, opacity, lineHeight: 1.2,
    }}
  >
    {note}
  </div>
);

/** Provenance. Always MUTE, never the accent. */
const SourceLine: React.FC<{source: string; opacity: number; top?: number; left?: number; width?: number}> =
({source, opacity, top, left, width}) => (
  <div
    style={{
      position: 'absolute', left: left ?? SAFE.x, top: top ?? SAFE.b - 128,
      width: width ?? SAFE.w,
      fontFamily: CLAUDE_FONT.ui, fontSize: 25, color: MUTE, opacity, lineHeight: 1.3,
    }}
  >
    Source: {source}
  </div>
);

const Eyebrow: React.FC<{text: string; opacity?: number}> = ({text, opacity = 1}) => (
  <div
    style={{
      position: 'absolute', left: SAFE.x, top: SAFE.y + 6, width: SAFE.w,
      fontFamily: CLAUDE_FONT.ui, fontSize: 22, letterSpacing: '.18em',
      color: MUTE, fontWeight: 600, opacity,
    }}
  >
    {text.toUpperCase()}
  </div>
);

const chipStyle = (hot: boolean | undefined, size: number): React.CSSProperties => ({
  fontFamily: CLAUDE_FONT.ui, fontSize: size, fontWeight: 600,
  letterSpacing: '.16em', textTransform: 'uppercase',
  color: hot ? CLAUDE.SPARK : MUTE,
  border: `${hot ? 2 : 1}px solid ${hot ? CLAUDE.SPARK : RULE}`,
  padding: '9px 16px', display: 'inline-block', whiteSpace: 'nowrap',
  backgroundColor: hot ? '#FFFFFF' : 'transparent',
});

/* ═══════════════════════════════════════════════════════════════════════════
   B01 — AdpBluf: two rails, one meeting point.

   EXECUTIVE-SUMMARY LAW. Ads arrive on one rail, agents on the other; the rails bend
   into a single point and the question sets there — the reel's whole shape, before any
   specific. No numbers on this type.
   ═══════════════════════════════════════════════════════════════════════════ */
export type BlufData = {
  slideMeta: string;
  top: string;
  bottom: string;
  meet: string;
  closer: string;
};

export const AdpBluf: React.FC<{data: BlufData}> = ({data}) => {
  const p = useP();
  const yT = SAFE.y + 250;
  const yB = SAFE.y + 450;
  const yM = SAFE.y + 600;
  const MX = CANVAS.w / 2;
  const g1 = win(p, 0.06, 0.24);
  const g2 = win(p, 0.28, 0.46);
  const m = win(p, 0.52, 0.64);

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />

      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.y + 130, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 76, lineHeight: 1.1, color: CLAUDE.INK,
          opacity: g1, transform: `translateX(${(1 - g1) * -40}px)`,
        }}
      >
        {data.top}
      </div>
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.y + 330, width: SAFE.w,
          textAlign: 'right',
          fontFamily: CLAUDE_FONT.serif, fontSize: 76, lineHeight: 1.1, color: CLAUDE.INK,
          opacity: g2, transform: `translateX(${(1 - g2) * 40}px)`,
        }}
      >
        {data.bottom}
      </div>

      <svg width={CANVAS.w} height={CANVAS.h} style={{position: 'absolute', left: 0, top: 0}}>
        {/* the two straight rails */}
        <line x1={SAFE.x} y1={yT} x2={SAFE.x + (MX - 120 - SAFE.x) * g1} y2={yT} stroke={CLAUDE.INK} strokeWidth={4} />
        <line x1={SAFE.r} y1={yB} x2={SAFE.r - (SAFE.r - (MX + 120)) * g2} y2={yB} stroke={CLAUDE.INK} strokeWidth={4} />
        {/* the bends into one point */}
        <path
          d={`M ${MX - 120} ${yT} Q ${MX} ${yT} ${MX} ${yM}`}
          fill="none" stroke={CLAUDE.INK} strokeWidth={4}
          pathLength={1} strokeDasharray={1} strokeDashoffset={1 - m}
        />
        <path
          d={`M ${MX + 120} ${yB} Q ${MX} ${yB} ${MX} ${yM}`}
          fill="none" stroke={CLAUDE.INK} strokeWidth={4}
          pathLength={1} strokeDasharray={1} strokeDashoffset={1 - m}
        />
        <circle cx={MX} cy={yM} r={16 * win(p, 0.6, 0.66)} fill={CLAUDE.SPARK} />
      </svg>

      <div
        style={{
          position: 'absolute', left: SAFE.x, top: yM + 44, width: SAFE.w, textAlign: 'center',
          fontFamily: CLAUDE_FONT.serif, fontSize: 80, lineHeight: 1.12, color: CLAUDE.SPARK,
          opacity: win(p, 0.64, 0.76),
        }}
      >
        {data.meet}
      </div>
      <NoteLine note={data.closer} opacity={win(p, 0.86, 0.97)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B02 — AdpRollout: the announcement as a spec sheet, one row per spoken fact.

   REQUIRES a `source`. Rows are printed verbatim from the beat sheet — every one of them
   is a supplied fact, and the type has no slot for anything else (no price, no count, no
   advertiser names). The `stamp` takes the accent because "testing" is the qualifier
   that governs every row beneath it.
   ═══════════════════════════════════════════════════════════════════════════ */
export type RolloutData = {
  slideMeta: string;
  title: string;
  stamp: string;
  rows: {key: string; value: string}[];
  /** REQUIRED */
  source: string;
};

export const AdpRollout: React.FC<{data: RolloutData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 214;
  const STEP = 104;
  const st = win(p, 0.1, 0.18);

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      <div
        style={{
          position: 'absolute', right: CANVAS.w - SAFE.r, top: SAFE.y + 78,
          ...chipStyle(true, 34), opacity: st,
          transform: `scale(${1.35 - 0.35 * st})`, transformOrigin: 'center',
        }}
      >
        {data.stamp}
      </div>

      {data.rows.map((r, i) => {
        const g = win(p, 0.16 + i * 0.1, 0.26 + i * 0.1);
        const y = TOP + i * STEP;
        return (
          <React.Fragment key={i}>
            <div
              style={{
                position: 'absolute', left: SAFE.x, top: y + 22, width: 330,
                fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.16em', fontWeight: 600,
                color: MUTE, opacity: g,
              }}
            >
              {r.key.toUpperCase()}
            </div>
            <div
              style={{
                position: 'absolute', left: SAFE.x + 360, top: y, width: SAFE.w - 360,
                fontFamily: CLAUDE_FONT.serif, fontSize: 62, lineHeight: 1.1, color: CLAUDE.INK,
                opacity: g, transform: `translateY(${(1 - g) * 14}px)`,
              }}
            >
              {r.value}
            </div>
            <div
              style={{
                position: 'absolute', left: SAFE.x, top: y + 88,
                width: SAFE.w * g, height: 1, backgroundColor: RULE,
              }}
            />
          </React.Fragment>
        );
      })}

      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} top={SAFE.b - 70} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B04 — AdpCanvas: the user's image, and the ad held apart from it.

   The ask→result pair's RESULT. A REDRAW of a written description — the window has no
   product chrome, no logo and no real ad, and the type REQUIRES a `caption` that says so
   on screen. The user's image generates (top-down wipe) in plain ink; only the ad's tag
   and label take the accent. The gap between the two is bracketed and named, because
   "kept visually separate" is the claim.
   ═══════════════════════════════════════════════════════════════════════════ */
export type CanvasData = {
  slideMeta: string;
  title: string;
  imageLabel: string;
  adTag: string;
  adLabel: string;
  gapLabel: string;
  /** REQUIRED — this is a redraw, and the frame says so */
  caption: string;
  /** REQUIRED */
  source: string;
};

/** The abstract "generated image" — sun and hills, in ink tints only. */
export const GeneratedArt: React.FC<{w: number; h: number; reveal: number}> = ({w, h, reveal}) => (
  <div style={{position: 'absolute', inset: 0, clipPath: `inset(0 0 ${(1 - reveal) * 100}% 0)`}}>
    <svg width={w} height={h} viewBox={`0 0 ${w} ${h}`}>
      <rect x={0} y={0} width={w} height={h} fill={CLAUDE.PILL} />
      <circle cx={w * 0.7} cy={h * 0.34} r={Math.min(w, h) * 0.16} fill={CLAUDE.INK} opacity={0.5} />
      <path d={`M0 ${h * 0.72} Q ${w * 0.25} ${h * 0.5} ${w * 0.5} ${h * 0.68} T ${w} ${h * 0.6} V ${h} H 0 Z`} fill={CLAUDE.INK} opacity={0.28} />
      <path d={`M0 ${h * 0.86} Q ${w * 0.3} ${h * 0.7} ${w * 0.6} ${h * 0.84} T ${w} ${h * 0.8} V ${h} H 0 Z`} fill={CLAUDE.INK} opacity={0.55} />
    </svg>
    {/* the generation edge */}
    {reveal < 1 && (
      <div style={{position: 'absolute', left: 0, top: `${reveal * 100}%`, width: '100%', height: 3, backgroundColor: CLAUDE.INK, opacity: 0.4}} />
    )}
  </div>
);

/** placeholder bars standing in for an ad's content — never a real product */
export const AdPlaceholder: React.FC<{w: number; h: number}> = ({w, h}) => (
  <svg width={w} height={h} viewBox={`0 0 ${w} ${h}`}>
    <rect x={0} y={0} width={w} height={h * 0.58} rx={10} fill={CLAUDE.INK} opacity={0.14} />
    <rect x={0} y={h * 0.68} width={w * 0.82} height={h * 0.09} rx={5} fill={CLAUDE.INK} opacity={0.22} />
    <rect x={0} y={h * 0.84} width={w * 0.56} height={h * 0.09} rx={5} fill={CLAUDE.INK} opacity={0.16} />
  </svg>
);

export const AdpCanvas: React.FC<{data: CanvasData}> = ({data}) => {
  const p = useP();
  const WIN_Y = SAFE.y + 186;
  const WIN_H = 520;
  const IMG_X = SAFE.x + 40;
  const IMG_Y = WIN_Y + 96;
  const IMG_W = 1060;
  const IMG_H = 384;
  const AD_X = IMG_X + IMG_W + 130;
  const AD_W = SAFE.r - 40 - AD_X;

  const draw = win(p, 0.04, 0.14);
  const gen = win(p, 0.12, 0.38);
  const ad = win(p, 0.36, 0.5);
  const gap = win(p, 0.54, 0.66);

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />

      {/* a generic window: no product chrome, no logo */}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: WIN_Y, width: SAFE.w, height: WIN_H,
          backgroundColor: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 18,
          opacity: draw,
        }}
      />
      <div
        style={{
          position: 'absolute', left: SAFE.x + 28, top: WIN_Y + 22, width: 900, height: 44,
          borderRadius: 22, backgroundColor: CLAUDE.PILL, opacity: draw,
        }}
      >
        <div style={{position: 'absolute', left: 26, top: 17, width: 520, height: 10, borderRadius: 5, backgroundColor: CLAUDE.INK, opacity: 0.2}} />
      </div>

      {/* the user's image — the work */}
      <div
        style={{
          position: 'absolute', left: IMG_X, top: IMG_Y, width: IMG_W, height: IMG_H,
          borderRadius: 10, overflow: 'hidden', opacity: draw,
          border: `1px solid ${RULE}`,
        }}
      >
        <GeneratedArt w={IMG_W} h={IMG_H} reveal={gen} />
      </div>

      {/* the ad — labeled, held apart */}
      <div
        style={{
          position: 'absolute', left: AD_X, top: IMG_Y, width: AD_W, height: IMG_H,
          boxSizing: 'border-box', border: `2px dashed ${CLAUDE.INK_SOFT}`, borderRadius: 10,
          opacity: ad, padding: 28,
        }}
      >
        <div style={{...chipStyle(true, 26)}}>{data.adTag}</div>
        <div style={{position: 'absolute', left: 28, top: 104}}>
          <AdPlaceholder w={AD_W - 56} h={IMG_H - 140} />
        </div>
      </div>

      {/* the separation, bracketed and named */}
      <svg width={CANVAS.w} height={CANVAS.h} style={{position: 'absolute', left: 0, top: 0, opacity: gap}}>
        <line x1={IMG_X + IMG_W + 8} y1={IMG_Y - 14} x2={IMG_X + IMG_W + 8 + (AD_X - IMG_X - IMG_W - 16) * gap} y2={IMG_Y - 14} stroke={CLAUDE.INK} strokeWidth={3} />
        <line x1={IMG_X + IMG_W + 8} y1={IMG_Y - 26} x2={IMG_X + IMG_W + 8} y2={IMG_Y - 2} stroke={CLAUDE.INK} strokeWidth={3} />
        <line x1={AD_X - 8} y1={IMG_Y - 26} x2={AD_X - 8} y2={IMG_Y - 2} stroke={CLAUDE.INK} strokeWidth={3} />
      </svg>
      <div
        style={{
          position: 'absolute', left: IMG_X + IMG_W - 140, top: WIN_Y + 26, width: 410,
          textAlign: 'center', fontFamily: CLAUDE_FONT.ui, fontSize: 26, fontWeight: 600,
          color: CLAUDE.INK, opacity: gap,
        }}
      >
        {data.gapLabel}
      </div>

      <div
        style={{
          position: 'absolute', left: IMG_X, top: WIN_Y + WIN_H + 22, width: IMG_W,
          fontFamily: CLAUDE_FONT.ui, fontSize: 34, color: CLAUDE.INK, opacity: win(p, 0.68, 0.8),
        }}
      >
        {data.imageLabel}
      </div>
      <div
        style={{
          position: 'absolute', left: AD_X - 60, top: WIN_Y + WIN_H + 22, width: AD_W + 60,
          fontFamily: CLAUDE_FONT.ui, fontSize: 34, lineHeight: 1.2, color: CLAUDE.SPARK,
          opacity: win(p, 0.72, 0.84),
        }}
      >
        {data.adLabel}
      </div>

      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} top={SAFE.b - 118} />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 80, width: SAFE.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 25, color: MUTE, opacity: win(p, 0.86, 0.96),
        }}
      >
        {data.caption}
      </div>
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B05 — AdpRoom: the private space that becomes an audience.

   The reframe beat. The bubbles are ILLUSTRATIVE (the type requires a `caption` saying
   so) — no user quote, no usage figure. The old line stays; the new line TYPES in beside
   it on the spoken word, because the claim is "also", not "instead".
   ═══════════════════════════════════════════════════════════════════════════ */
export type RoomData = {
  slideMeta: string;
  bubbles: string[];
  before: string;
  after: string;
  /** REQUIRED — the messages are illustrative */
  caption: string;
  note: string;
};

export const AdpRoom: React.FC<{data: RoomData}> = ({data}) => {
  const p = useP();
  const COL_X = SAFE.x;
  const COL_W = 780;
  const COL_Y = SAFE.y + 96;
  const COL_H = 690;
  const R_X = SAFE.x + 900;
  const R_W = SAFE.w - 900;
  const frameIn = win(p, 0.6, 0.74);

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />

      {/* the room around the conversation — drawn when it becomes an audience */}
      <div
        style={{
          position: 'absolute', left: COL_X, top: COL_Y, width: COL_W, height: COL_H,
          border: `3px dashed ${CLAUDE.SPARK}`, borderRadius: 22, opacity: frameIn * 0.8,
        }}
      />
      <div
        style={{
          position: 'absolute', left: COL_X + 40, top: COL_Y + 70, width: COL_W - 80,
          display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: 56,
        }}
      >
        {data.bubbles.map((b, i) => {
          const g = win(p, 0.12 + i * 0.09, 0.22 + i * 0.09);
          return (
            <div
              key={i}
              style={{
                maxWidth: 700, backgroundColor: CLAUDE.PILL, borderRadius: 30,
                padding: '26px 36px', fontFamily: CLAUDE_FONT.ui, fontSize: 38, lineHeight: 1.25,
                color: CLAUDE.INK, opacity: g, transform: `translateY(${(1 - g) * 16}px)`,
              }}
            >
              {b}
            </div>
          );
        })}
      </div>
      <div
        style={{
          position: 'absolute', left: COL_X, top: COL_Y + COL_H + 16, width: COL_W,
          fontFamily: CLAUDE_FONT.ui, fontSize: 24, color: MUTE, opacity: win(p, 0.3, 0.4),
        }}
      >
        {data.caption}
      </div>

      <div
        style={{
          position: 'absolute', left: R_X, top: SAFE.y + 190, width: R_W,
          fontFamily: CLAUDE_FONT.serif, fontSize: 96, lineHeight: 1.08, color: CLAUDE.INK,
          opacity: win(p, 0.4, 0.52),
        }}
      >
        {data.before}
      </div>
      <div
        style={{
          position: 'absolute', left: R_X, top: SAFE.y + 360, width: R_W,
          fontFamily: CLAUDE_FONT.serif, fontSize: 96, lineHeight: 1.08, color: CLAUDE.SPARK,
        }}
      >
        {typed(data.after, win(p, 0.58, 0.74))}
      </div>

      <NoteLine note={data.note} opacity={win(p, 0.86, 0.96)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B06 — AdpDots: one always-on agent, its own computer, a field of apps.

   REQUIRES `source` AND `tileNote`. "over 4,000" is the reel's ONLY figure and it is
   printed verbatim; the tile field is not a count of anything and the frame says so.
   The dot is the accent and never stops pulsing — "always on" is the motion.
   ═══════════════════════════════════════════════════════════════════════════ */
export type DotsData = {
  slideMeta: string;
  title: string;
  dotLabel: string;
  computerLabel: string;
  /** printed VERBATIM — never parsed, never counted */
  value: string;
  valueLabel: string;
  /** REQUIRED — the tiles are decorative */
  tileNote: string;
  /** REQUIRED */
  source: string;
};

/** Pulsing always-on dot with an expanding ring. */
export const AlwaysOnDot: React.FC<{cx: number; cy: number; r: number; appear: number}> = ({cx, cy, r, appear}) => {
  const frame = useCurrentFrame();
  const pulse = 1 + 0.07 * Math.sin(frame / 7);
  const ring = (frame % 45) / 45;
  return (
    <svg width={CANVAS.w * 2} height={CANVAS.h * 2} style={{position: 'absolute', left: 0, top: 0, overflow: 'visible'}}>
      <circle cx={cx} cy={cy} r={r * (1 + ring * 0.9)} fill="none" stroke={CLAUDE.SPARK} strokeWidth={3} opacity={(1 - ring) * 0.6 * appear} />
      <circle cx={cx} cy={cy} r={r * pulse * appear} fill={CLAUDE.SPARK} />
    </svg>
  );
};

export const AdpDots: React.FC<{data: DotsData}> = ({data}) => {
  const p = useP();
  const DX = SAFE.x + 170;
  const DY = SAFE.y + 400;
  const COLS = 16;
  const ROWS = 6;
  const T = 54;
  const G = 20;
  const GX = SAFE.x + 540;
  const GY = SAFE.y + 200;

  const appear = win(p, 0.06, 0.14);
  const box = win(p, 0.22, 0.34);
  const wire = win(p, 0.4, 0.56);
  const targets = [[0, 0], [0, 2], [0, 4], [0, 5], [2, 1], [3, 3], [5, 0], [6, 5], [9, 2]];

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />

      {/* wires from the dot out to the apps */}
      <svg width={CANVAS.w} height={CANVAS.h} style={{position: 'absolute', left: 0, top: 0}}>
        {targets.map(([c, r], i) => (
          <line
            key={i}
            x1={DX} y1={DY}
            x2={DX + (GX + c * (T + G) + T / 2 - DX) * win(p, 0.4 + i * 0.015, 0.54 + i * 0.015)}
            y2={DY + (GY + r * (T + G) + T / 2 - DY) * win(p, 0.4 + i * 0.015, 0.54 + i * 0.015)}
            stroke={CLAUDE.INK} strokeWidth={2} opacity={0.35}
          />
        ))}
        {/* dot → its own computer */}
        <line x1={DX} y1={DY} x2={DX} y2={DY + 200 * box} stroke={CLAUDE.INK} strokeWidth={3} opacity={0.6} />
      </svg>

      {/* the field of apps — decorative, not a count */}
      {Array.from({length: COLS * ROWS}).map((_, k) => {
        const c = k % COLS;
        const r = Math.floor(k / COLS);
        const shown = win(p, 0.3 + c * 0.004, 0.4 + c * 0.004);
        const lit = win(p, 0.42 + c * 0.012, 0.5 + c * 0.012);
        return (
          <div
            key={k}
            style={{
              position: 'absolute', left: GX + c * (T + G), top: GY + r * (T + G),
              width: T, height: T, borderRadius: 12, boxSizing: 'border-box',
              border: `2px solid ${CLAUDE.INK_SOFT}`,
              /* an app "connects" by filling with ink tint — ink, never the accent */
              backgroundColor: `rgba(61, 57, 41, ${0.06 + 0.3 * lit})`,
              opacity: shown,
            }}
          />
        );
      })}

      <AlwaysOnDot cx={DX} cy={DY} r={52} appear={appear} />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: DY - 150, width: 360, textAlign: 'left',
          fontFamily: CLAUDE_FONT.ui, fontSize: 30, fontWeight: 600, color: CLAUDE.INK, opacity: win(p, 0.1, 0.2),
          paddingLeft: 0,
        }}
      >
        {data.dotLabel}
      </div>

      {/* its own cloud computer */}
      <div style={{position: 'absolute', left: DX - 130, top: DY + 200, opacity: box}}>
        <div style={{width: 260, height: 150, border: `3px solid ${CLAUDE.INK}`, borderRadius: 12, backgroundColor: CLAUDE.CARD, position: 'relative'}}>
          {[0, 1, 2].map((k) => (
            <div key={k} style={{position: 'absolute', left: 24, top: 28 + k * 34, width: k === 2 ? 120 : 200, height: 12, borderRadius: 6, backgroundColor: CLAUDE.INK, opacity: 0.22}} />
          ))}
        </div>
        <div style={{width: 80, height: 18, margin: '0 auto', backgroundColor: CLAUDE.INK, opacity: 0.5}} />
        <div style={{width: 360, marginLeft: -50, marginTop: 14, textAlign: 'center', fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: CLAUDE.INK}}>
          {data.computerLabel}
        </div>
      </div>

      <div
        style={{
          position: 'absolute', left: GX, top: GY + ROWS * (T + G) + 20, width: 700,
          fontFamily: CLAUDE_FONT.serif, fontSize: 140, lineHeight: 1, color: CLAUDE.INK,
          opacity: win(p, 0.56, 0.68), whiteSpace: 'nowrap',
        }}
      >
        {data.value}
      </div>
      <div
        style={{
          position: 'absolute', left: GX + 720, top: GY + ROWS * (T + G) + 44, width: SAFE.r - GX - 720,
          fontFamily: CLAUDE_FONT.ui, fontSize: 36, lineHeight: 1.25, color: CLAUDE.INK,
          opacity: win(p, 0.62, 0.74),
        }}
      >
        {data.valueLabel}
      </div>

      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} top={SAFE.b - 80} left={GX} width={SAFE.r - GX} />
      <div
        style={{
          position: 'absolute', left: GX, top: SAFE.b - 120, width: SAFE.r - GX,
          fontFamily: CLAUDE_FONT.ui, fontSize: 25, color: MUTE, opacity: win(p, 0.8, 0.9),
        }}
      >
        {data.tileNote}
      </div>
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B07 — AdpConverge: two cards slide into one product.

   No numbers on this type. The cards stay distinct after they meet — the seam between
   them is what takes the accent, labelled as the thing they share. Nothing on screen
   says the two announcements are one plan; `note` says only that they share a week.
   ═══════════════════════════════════════════════════════════════════════════ */
export type ConvergeData = {
  slideMeta: string;
  left: {tag: string; label: string};
  right: {tag: string; label: string};
  seam: string;
  verdict: string;
  note: string;
};

export const AdpConverge: React.FC<{data: ConvergeData}> = ({data}) => {
  const p = useP();
  const CARD_W = 780;
  const CARD_H = 400;
  const TOP = SAFE.y + 120;
  const slide = win(p, 0.5, 0.66);
  const shift = ((SAFE.w - 2 * CARD_W) / 2) * slide;
  const seam = win(p, 0.6, 0.72);

  const card = (x: number, c: {tag: string; label: string}, g: number) => (
    <div
      style={{
        position: 'absolute', left: x, top: TOP, width: CARD_W, height: CARD_H,
        boxSizing: 'border-box', padding: '46px 52px',
        backgroundColor: CLAUDE.CARD, border: `2px solid ${CLAUDE.INK}`, borderRadius: 16,
        opacity: g,
      }}
    >
      <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 30, letterSpacing: '.18em', fontWeight: 600, color: MUTE}}>
        {c.tag.toUpperCase()}
      </div>
      <div style={{marginTop: 30, fontFamily: CLAUDE_FONT.serif, fontSize: 64, lineHeight: 1.12, color: CLAUDE.INK}}>
        {c.label}
      </div>
    </div>
  );

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />
      {card(SAFE.x + shift, data.left, win(p, 0.06, 0.2))}
      {card(SAFE.r - CARD_W - shift, data.right, win(p, 0.28, 0.42))}

      <div
        style={{
          position: 'absolute', left: CANVAS.w / 2 - 4, top: TOP - 20,
          width: 8, height: (CARD_H + 40) * seam, backgroundColor: CLAUDE.SPARK,
        }}
      />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP + CARD_H + 44, width: SAFE.w, textAlign: 'center',
          fontFamily: CLAUDE_FONT.serif, fontSize: 52, color: CLAUDE.SPARK, opacity: win(p, 0.66, 0.76),
        }}
      >
        {data.seam}
      </div>
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP + CARD_H + 150, width: SAFE.w, textAlign: 'center',
          fontFamily: CLAUDE_FONT.serif, fontSize: 70, lineHeight: 1.12, color: CLAUDE.INK, opacity: win(p, 0.78, 0.9),
        }}
      >
        {data.verdict}
      </div>
      <NoteLine note={data.note} opacity={win(p, 0.9, 0.99)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B08 — AdpChannel: two channels that happened, and one slot still open.

   No dates and no figures on this type — the history is ordinal ("became an ad
   channel"), not quantified. The third slot draws dashed and takes the accent, because
   the reel does not claim it IS a channel, only that it is being tested.
   ═══════════════════════════════════════════════════════════════════════════ */
export type ChannelData = {
  slideMeta: string;
  title: string;
  steps: {label: string; chip: string}[];
  status: string;
  note: string;
};

export const AdpChannel: React.FC<{data: ChannelData}> = ({data}) => {
  const p = useP();
  const N = data.steps.length;
  const ARROW = 130;
  const SLOT_W = (SAFE.w - (N - 1) * ARROW) / N;
  const SLOT_H = 390;
  const TOP = SAFE.y + 236;

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.steps.map((s, i) => {
        const open = i === N - 1;
        const g = win(p, 0.06 + i * 0.18, 0.18 + i * 0.18);
        const x = SAFE.x + i * (SLOT_W + ARROW);
        const arrow = i < N - 1 ? win(p, 0.2 + i * 0.18, 0.28 + i * 0.18) : 0;
        return (
          <React.Fragment key={i}>
            <div
              style={{
                position: 'absolute', left: x, top: TOP, width: SLOT_W, height: SLOT_H,
                boxSizing: 'border-box', borderRadius: 16,
                border: open ? `4px dashed ${CLAUDE.SPARK}` : `2px solid ${CLAUDE.INK}`,
                backgroundColor: open ? 'transparent' : CLAUDE.CARD,
                display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 34,
                opacity: g, transform: `translateY(${(1 - g) * 16}px)`,
              }}
            >
              <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: 60, color: CLAUDE.INK, textAlign: 'center', lineHeight: 1.1, padding: '0 20px'}}>
                {s.label}
              </div>
              <div style={chipStyle(open, 26)}>{s.chip}</div>
            </div>
            {open && (
              <div style={{position: 'absolute', left: x + SLOT_W - 66, top: TOP - 4, fontFamily: CLAUDE_FONT.serif, fontSize: 76, color: CLAUDE.SPARK, opacity: g}}>
                ?
              </div>
            )}
            {i < N - 1 && (
              <svg width={ARROW} height={40} style={{position: 'absolute', left: x + SLOT_W, top: TOP + SLOT_H / 2 - 20}}>
                <line x1={18} y1={20} x2={18 + (ARROW - 50) * arrow} y2={20} stroke={CLAUDE.INK} strokeWidth={4} />
                <polyline points={`${ARROW - 42},8 ${ARROW - 26},20 ${ARROW - 42},32`} fill="none" stroke={CLAUDE.INK} strokeWidth={4} opacity={arrow > 0.95 ? 1 : 0} />
              </svg>
            )}
          </React.Fragment>
        );
      })}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP + SLOT_H + 56, width: SAFE.w, textAlign: 'center',
          fontFamily: CLAUDE_FONT.ui, fontSize: 38, color: CLAUDE.INK, opacity: win(p, 0.62, 0.74),
        }}
      >
        {data.status}
      </div>
      <NoteLine note={data.note} opacity={win(p, 0.88, 0.97)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B09 — AdpLimits: what was announced, ticked; what isn't covered, left open.

   The FALSIFIABILITY beat. `provenance` and `falsifier` are REQUIRED. The open boxes are
   never ticked by any prop — there is no `answer` field, because none was supplied.
   ═══════════════════════════════════════════════════════════════════════════ */
export type LimitsData = {
  slideMeta: string;
  title: string;
  announced: {heading: string; items: string[]};
  open: {heading: string; items: string[]};
  /** REQUIRED */
  provenance: string;
  /** REQUIRED */
  falsifier: string;
};

export const CheckBox: React.FC<{size: number; hot?: boolean; tick: number; opacity: number}> = ({size, hot, tick, opacity}) => (
  <svg width={size} height={size} viewBox="0 0 36 36" style={{opacity, flexShrink: 0}}>
    <rect x={2} y={2} width={32} height={32} rx={6} fill="none" stroke={hot ? CLAUDE.SPARK : CLAUDE.INK} strokeWidth={3} />
    {!hot && (
      <path d="M9 19 L16 26 L28 11" fill="none" stroke={CLAUDE.INK} strokeWidth={4} strokeLinecap="round"
        pathLength={1} strokeDasharray={1} strokeDashoffset={1 - tick} />
    )}
  </svg>
);

export const AdpLimits: React.FC<{data: LimitsData}> = ({data}) => {
  const p = useP();
  const COL_W = 806;
  const HEAD_Y = SAFE.y + 226;
  const ITEM_Y = SAFE.y + 300;
  const STEP = 108;

  const list = (x: number, h: {heading: string; items: string[]}, startAt: number, hot: boolean) => (
    <>
      <div
        style={{
          position: 'absolute', left: x, top: HEAD_Y, width: COL_W,
          fontFamily: CLAUDE_FONT.ui, fontSize: 28, letterSpacing: '.16em', fontWeight: 600,
          color: hot ? CLAUDE.SPARK : MUTE, opacity: win(p, startAt, startAt + 0.08),
        }}
      >
        {h.heading.toUpperCase()}
      </div>
      {h.items.map((it, i) => {
        const g = win(p, startAt + 0.04 + i * 0.07, startAt + 0.14 + i * 0.07);
        return (
          <div
            key={i}
            style={{
              position: 'absolute', left: x, top: ITEM_Y + i * STEP, width: COL_W,
              display: 'flex', alignItems: 'center', gap: 26, opacity: g,
            }}
          >
            <CheckBox size={46} hot={hot} tick={win(p, startAt + 0.1 + i * 0.07, startAt + 0.18 + i * 0.07)} opacity={1} />
            <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 36, lineHeight: 1.25, color: CLAUDE.INK}}>{it}</div>
          </div>
        );
      })}
    </>
  );

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {list(SAFE.x, data.announced, 0.06, false)}
      {list(SAFE.x + 922, data.open, 0.44, true)}

      <div style={{position: 'absolute', left: SAFE.x, top: SAFE.b - 150, width: SAFE.w * win(p, 0.76, 0.86), height: 1, backgroundColor: RULE}} />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 130, width: SAFE.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 25, color: MUTE, opacity: win(p, 0.78, 0.88),
        }}
      >
        {data.provenance}
      </div>
      <NoteLine note={data.falsifier} opacity={win(p, 0.88, 0.97)} />
    </PlainStage>
  );
};
