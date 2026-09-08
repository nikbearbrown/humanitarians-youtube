/**
 * WeekGordy916.tsx — PORTRAIT (9:16) scenes for `yatra-this-week-gordy`.
 *
 * Re-banded vertically per the Shorts law's composition logic, NOT scaled
 * clones. Three of the landscape layouts are horizontal by nature and are
 * genuinely rebuilt here rather than squeezed:
 *
 *   · WkPipeline916    — the five stages run DOWN the frame with vertical
 *                        connectors; five boxes across 972px would be 170px
 *                        wide each, which cannot hold a label.
 *   · WkShip916        — made → destination becomes TOP → BOTTOM, so the route
 *                        is a vertical wire with the chip on it.
 *   · WkNotClaiming916 — the two columns STACK into two labelled groups; a
 *                        two-column ledger is unreadable at portrait width.
 *   · WkReview916      — slots stack, and the written → in review → Substack
 *                        track runs downward.
 *   · WkBluf916        — the state chip sits ABOVE its line instead of beside
 *                        it (no room for a 230px gutter).
 *   · WkTool916        — the coverage chips wrap across rows.
 *   · WkStatus916      — already row-based; the detail line moves BENEATH the
 *                        stage label instead of beside it.
 *
 * The same refusals hold, because they live in the shared types imported from
 * WeekGordy.tsx: `slots` carries a label and nothing else, so no article title
 * or content can render here either; `WkShip916` draws no artwork; `WkTool916`
 * requires a `source` and renders the description as a verbatim quote.
 *
 * KEEP-OUT: content stays above y≈1440 and left of x≈960 — the Shorts/Reels
 * chrome region — with the brand bug lower-left.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {SAFE916} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import type {
  BlufData, PipelineData, ToolData, StatusData, ShipData, ReviewData, NotClaimingData,
} from './WeekGordy';

const STAGE = '#F2F0E9';
const RULE = '#D8D4C8';
const MUTE = '#7A7265';
const BOX = {x: SAFE916.x, y: SAFE916.y, w: 972, bottom: 1440} as const;

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

const Head: React.FC<{meta: string; title: string}> = ({meta, title}) => (
  <>
    <div style={{position: 'absolute', left: BOX.x, top: BOX.y, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.16em', color: MUTE, fontWeight: 600}}>
      {meta.toUpperCase()}
    </div>
    <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 76, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 74, color: CLAUDE.INK, lineHeight: 1.06}}>
      {title}
    </div>
  </>
);

const Note: React.FC<{note: string; opacity: number; accent?: boolean}> = ({note, opacity, accent}) => (
  <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 88, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 38, color: accent ? CLAUDE.SPARK : CLAUDE.INK, lineHeight: 1.25, opacity}}>
    {note}
  </div>
);

const Chip: React.FC<{
  text: string; left: number; top: number; hot?: boolean; opacity: number; size?: number;
}> = ({text, left, top, hot, opacity, size = 21}) => (
  <div
    style={{
      position: 'absolute', left, top, opacity,
      fontFamily: CLAUDE_FONT.ui, fontSize: size, fontWeight: 600,
      letterSpacing: '.16em', textTransform: 'uppercase' as const,
      color: hot ? CLAUDE.SPARK : MUTE,
      border: `1px solid ${hot ? CLAUDE.SPARK : RULE}`,
      padding: '8px 14px', display: 'inline-block', whiteSpace: 'nowrap' as const,
    }}
  >
    {text}
  </div>
);

/* ── B01 — the week in one breath; chip ABOVE each line ──────────────────── */
export const WkBluf916: React.FC<{data: BlufData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 180;
  const STEP = 350;

  return (
    <Stage>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.16em', color: MUTE, fontWeight: 600, opacity: win(p, 0.02, 0.16)}}>
        {data.slideMeta.toUpperCase()}
      </div>
      {data.lines.map((ln, i) => {
        const g = win(p, 0.08 + i * 0.26, 0.3 + i * 0.26);
        const hot = i === data.lines.length - 1;
        const y = TOP + i * STEP;
        return (
          <React.Fragment key={i}>
            <Chip text={ln.chip} left={BOX.x} top={y} hot={hot} opacity={g} />
            <div
              style={{
                position: 'absolute', left: BOX.x, top: y + 72, width: BOX.w,
                fontFamily: CLAUDE_FONT.serif, fontSize: 62, lineHeight: 1.18,
                color: hot ? CLAUDE.SPARK : CLAUDE.INK, opacity: g,
                transform: `translateY(${(1 - g) * 14}px)`,
              }}
            >
              {ln.label}
            </div>
            <div style={{position: 'absolute', left: BOX.x, top: y + STEP - 54, width: BOX.w * g, height: 1, backgroundColor: RULE}} />
          </React.Fragment>
        );
      })}
      <Note note={data.closer} opacity={win(p, 0.86, 0.97)} />
    </Stage>
  );
};

/* ── B02 — five stages, running DOWN the frame ───────────────────────────── */
export const WkPipeline916: React.FC<{data: PipelineData}> = ({data}) => {
  const p = useP();
  const n = data.stages.length;
  const BOX_H = 140;
  const GAP = 38;
  const TOP = BOX.y + 300;

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.stages.map((s, i) => {
        const g = win(p, 0.1 + i * 0.14, 0.26 + i * 0.14);
        const hot = i === data.hotIndex ? win(p, 0.82, 0.94) : 0;
        const y = TOP + i * (BOX_H + GAP);
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w * g, height: BOX_H, border: `2px solid ${RULE}`, boxSizing: 'border-box'}} />
            <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w, height: BOX_H, border: `3px solid ${CLAUDE.SPARK}`, boxSizing: 'border-box', opacity: hot}} />
            <div style={{position: 'absolute', left: BOX.x + 26, top: y + 24, fontFamily: CLAUDE_FONT.ui, fontSize: 21, letterSpacing: '.16em', color: MUTE, opacity: g}}>
              {String(i + 1).padStart(2, '0')}
            </div>
            <div style={{position: 'absolute', left: BOX.x + 26, top: y + 58, width: 300, fontFamily: CLAUDE_FONT.serif, fontSize: 48, color: CLAUDE.INK, opacity: g, lineHeight: 1.1}}>
              {s.label}
            </div>
            <div style={{position: 'absolute', left: BOX.x + 360, top: y + 70, width: BOX.w - 390, fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE, opacity: g, lineHeight: 1.25}}>
              {s.sub}
            </div>
            {i < n - 1 && (
              <div style={{position: 'absolute', left: BOX.x + BOX.w / 2 - 1, top: y + BOX_H, width: 2, height: GAP * win(p, 0.16 + i * 0.14, 0.3 + i * 0.14), backgroundColor: RULE}} />
            )}
          </React.Fragment>
        );
      })}
      <Note note={data.note} opacity={win(p, 0.88, 0.97)} />
    </Stage>
  );
};

/* ── B03 — the tool, in its own words; chips wrap ────────────────────────── */
export const WkTool916: React.FC<{data: ToolData}> = ({data}) => {
  const p = useP();

  return (
    <Stage>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.16em', color: MUTE, fontWeight: 600, opacity: win(p, 0.02, 0.14)}}>
        {data.slideMeta.toUpperCase()}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 56, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 118, color: CLAUDE.INK, lineHeight: 1, opacity: win(p, 0.06, 0.24)}}>
        {data.name}
      </div>
      <div
        style={{
          position: 'absolute', left: BOX.x, top: BOX.y + 220, width: BOX.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 50, fontStyle: 'italic' as const,
          color: CLAUDE.INK, lineHeight: 1.28, opacity: win(p, 0.24, 0.46),
        }}
      >
        “{data.quote}”
      </div>

      <div
        style={{
          position: 'absolute', left: BOX.x, top: BOX.y + 560, width: BOX.w,
          display: 'flex', flexWrap: 'wrap' as const, gap: 12,
        }}
      >
        {data.chips.map((c, i) => (
          <span
            key={i}
            style={{
              fontFamily: CLAUDE_FONT.ui, fontSize: 20, fontWeight: 600,
              letterSpacing: '.14em', textTransform: 'uppercase' as const, color: MUTE,
              border: `1px solid ${RULE}`, padding: '8px 13px',
              opacity: win(p, 0.5 + i * 0.045, 0.62 + i * 0.045),
            }}
          >
            {c}
          </span>
        ))}
      </div>

      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 720, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 32, color: CLAUDE.INK, lineHeight: 1.3, opacity: win(p, 0.66, 0.8)}}>
        {data.audience}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 850, width: BOX.w, fontFamily: CLAUDE_FONT.mono, fontSize: 27, color: MUTE, opacity: win(p, 0.76, 0.88)}}>
        {data.url}
      </div>

      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 168, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 25, color: MUTE, lineHeight: 1.25, opacity: win(p, 0.82, 0.92)}}>
        Source: {data.source}
      </div>
      <Note note={data.note} opacity={win(p, 0.9, 0.99)} accent />
    </Stage>
  );
};

/* ── B05 — the status board; detail BENEATH the label ────────────────────── */
export const WkStatus916: React.FC<{data: StatusData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 280;
  const STEP = 190;
  const MARK = 28;

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.stages.map((s, i) => {
        const g = win(p, 0.06 + i * 0.13, 0.22 + i * 0.13);
        const open = s.state !== 'closed';
        const y = TOP + i * STEP;
        return (
          <React.Fragment key={i}>
            <div
              style={{
                position: 'absolute', left: BOX.x, top: y + 12,
                width: MARK, height: MARK,
                backgroundColor: open ? 'transparent' : CLAUDE.INK,
                border: open ? `3px solid ${CLAUDE.SPARK}` : 'none',
                boxSizing: 'border-box', opacity: g,
              }}
            />
            <div style={{position: 'absolute', left: BOX.x + 58, top: y, width: 420, fontFamily: CLAUDE_FONT.serif, fontSize: 46, color: open ? CLAUDE.SPARK : CLAUDE.INK, opacity: g, lineHeight: 1.1}}>
              {s.label}
            </div>
            <Chip text={open ? 'open' : 'closed'} left={BOX.x + BOX.w - 148} top={y + 6} hot={open} opacity={g} size={19} />
            <div style={{position: 'absolute', left: BOX.x + 58, top: y + 66, width: BOX.w - 58, fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: open ? CLAUDE.INK : MUTE, opacity: g, lineHeight: 1.26}}>
              {s.detail}
            </div>
            <div style={{position: 'absolute', left: BOX.x, top: y + STEP - 42, width: BOX.w * g, height: 1, backgroundColor: RULE}} />
          </React.Fragment>
        );
      })}
      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 148, fontFamily: CLAUDE_FONT.ui, fontSize: 28, letterSpacing: '.1em', textTransform: 'uppercase' as const, color: MUTE, opacity: win(p, 0.8, 0.9)}}>
        {data.tally}
      </div>
      <Note note={data.note} opacity={win(p, 0.88, 0.97)} />
    </Stage>
  );
};

/* ── B06 — made → destination, stacked vertically ────────────────────────── */
export const WkShip916: React.FC<{data: ShipData}> = ({data}) => {
  const p = useP();
  const NODE_H = 300;
  const TOP = BOX.y + 300;
  const WIRE_H = 130;
  const T2 = TOP + NODE_H + WIRE_H;
  const leftIn = win(p, 0.08, 0.3);
  const rightIn = win(p, 0.56, 0.76);
  const wireIn = win(p, 0.4, 0.6);
  const chipIn = win(p, 0.74, 0.88);

  const node = (y: number, d: {label: string; sub: string}, g: number) => (
    <>
      <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w, height: NODE_H, border: `2px solid ${RULE}`, boxSizing: 'border-box', opacity: g}} />
      <div style={{position: 'absolute', left: BOX.x + 30, top: y + 62, maxWidth: BOX.w - 60, fontFamily: CLAUDE_FONT.serif, fontSize: 56, color: CLAUDE.INK, opacity: g, lineHeight: 1.12}}>
        {d.label}
      </div>
      <div style={{position: 'absolute', left: BOX.x + 30, top: y + 200, maxWidth: BOX.w - 60, fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: MUTE, opacity: g, lineHeight: 1.3}}>
        {d.sub}
      </div>
    </>
  );

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {node(TOP, data.made, leftIn)}
      {node(T2, data.destination, rightIn)}
      <div style={{position: 'absolute', left: BOX.x + BOX.w / 2 - 1, top: TOP + NODE_H, width: 2, height: WIRE_H * wireIn, backgroundColor: MUTE, opacity: 0.7}} />
      <Chip text={data.chip} left={BOX.x + BOX.w / 2 - 58} top={TOP + NODE_H + WIRE_H / 2 - 22} hot opacity={chipIn} size={21} />
      <Note note={data.note} opacity={win(p, 0.88, 0.98)} />
    </Stage>
  );
};

/* ── B07 — two withheld slots, then the review track, running down ───────── */
export const WkReview916: React.FC<{data: ReviewData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 260;
  const SLOT_H = 150;
  const SLOT_GAP = 30;
  const BAND_Y = TOP + 2 * SLOT_H + SLOT_GAP + 26;
  const TRACK_Y = BAND_Y + 100;
  const n = data.stages.length;
  const NODE_H = 110;
  const NODE_GAP = 30;

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />

      {data.slots.map((s, i) => {
        const g = win(p, 0.06 + i * 0.1, 0.24 + i * 0.1);
        const y = TOP + i * (SLOT_H + SLOT_GAP);
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w, height: SLOT_H, border: `2px dashed ${RULE}`, boxSizing: 'border-box', opacity: g}} />
            <div style={{position: 'absolute', left: BOX.x, top: y + SLOT_H / 2 - 22, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 32, color: MUTE, textAlign: 'center' as const, opacity: g}}>
              {s.label}
            </div>
          </React.Fragment>
        );
      })}

      <div style={{position: 'absolute', left: BOX.x, top: BAND_Y, width: BOX.w, height: 76, border: `1px solid ${RULE}`, boxSizing: 'border-box', opacity: win(p, 0.3, 0.46)}} />
      <div style={{position: 'absolute', left: BOX.x + 16, top: BAND_Y + 16, width: BOX.w - 32, fontFamily: CLAUDE_FONT.ui, fontSize: 25, letterSpacing: '.06em', color: MUTE, textAlign: 'center' as const, opacity: win(p, 0.34, 0.5), lineHeight: 1.25}}>
        {data.withhold}
      </div>

      {data.stages.map((s, i) => {
        const g = win(p, 0.5 + i * 0.13, 0.66 + i * 0.13);
        const y = TRACK_Y + i * (NODE_H + NODE_GAP);
        const current = s.state === 'current';
        const done = s.state === 'done';
        return (
          <React.Fragment key={i}>
            <div
              style={{
                position: 'absolute', left: BOX.x, top: y, width: BOX.w, height: NODE_H,
                backgroundColor: done ? CLAUDE.INK : 'transparent',
                border: current ? `3px solid ${CLAUDE.SPARK}` : done ? 'none' : `2px dashed ${RULE}`,
                boxSizing: 'border-box', opacity: g,
              }}
            />
            <div
              style={{
                position: 'absolute', left: BOX.x + 16, top: y + NODE_H / 2 - 22, width: BOX.w - 32,
                fontFamily: CLAUDE_FONT.ui, fontSize: 32,
                color: done ? CLAUDE.PAGE : current ? CLAUDE.SPARK : MUTE,
                textAlign: 'center' as const, opacity: g, lineHeight: 1.2,
              }}
            >
              {s.label}
            </div>
            {i < n - 1 && (
              <div style={{position: 'absolute', left: BOX.x + BOX.w / 2 - 1, top: y + NODE_H, width: 2, height: NODE_GAP * g, backgroundColor: RULE}} />
            )}
          </React.Fragment>
        );
      })}

      <Note note={data.note} opacity={win(p, 0.9, 0.98)} />
    </Stage>
  );
};

/* ── B08 — the two sides, STACKED (a two-column ledger will not fit) ─────── */
export const WkNotClaiming916: React.FC<{data: NotClaimingData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 260;
  const STEP = 90;
  const GROUP2 = TOP + 84 + 3 * STEP + 60;

  const group = (
    y: number,
    side: {heading: string; items: string[]},
    hot: boolean,
    from: number,
  ) => (
    <>
      <div
        style={{
          position: 'absolute', left: BOX.x, top: y, width: BOX.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.14em', fontWeight: 600,
          textTransform: 'uppercase' as const, color: hot ? CLAUDE.SPARK : MUTE,
          opacity: win(p, from - 0.06, from),
        }}
      >
        {side.heading}
      </div>
      {side.items.map((it, i) => {
        const g = win(p, from + i * 0.1, from + 0.12 + i * 0.1);
        return (
          <React.Fragment key={i}>
            <div
              style={{
                position: 'absolute', left: BOX.x, top: y + 56 + i * STEP, width: BOX.w,
                fontFamily: CLAUDE_FONT.ui, fontSize: 33, lineHeight: 1.24,
                color: hot ? CLAUDE.SPARK : CLAUDE.INK, opacity: g,
                transform: `translateY(${(1 - g) * 10}px)`,
              }}
            >
              {it}
            </div>
            <div style={{position: 'absolute', left: BOX.x, top: y + 56 + i * STEP + STEP - 22, width: BOX.w * g, height: 1, backgroundColor: RULE}} />
          </React.Fragment>
        );
      })}
    </>
  );

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {group(TOP, data.claiming, false, 0.14)}
      {group(GROUP2, data.notClaiming, true, 0.5)}
      <Note note={data.note} opacity={win(p, 0.9, 0.98)} />
    </Stage>
  );
};
