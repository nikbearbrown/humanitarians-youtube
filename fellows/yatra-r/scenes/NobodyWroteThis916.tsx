/**
 * NobodyWroteThis916.tsx — PORTRAIT (9:16) scenes for `yatra-nobody-wrote-this`.
 *
 * Re-banded vertically per the Shorts law's composition logic, NOT scaled clones:
 * a centre-crop of the landscape set would chop the citation lines and the value
 * labels that sit at the end of each bar, and the citations are the point of this
 * reel.
 *
 *   · LnkBluf916          — the statement gets the top half; the struck line and its
 *                           replacement stack beneath with more air.
 *   · LnkFrame916         — three bins as full-width bands, taller, more gap.
 *   · LnkStat916          — hero figure in the upper band, label/rank/citation below.
 *   · LnkLadder916        — the platform name moves ABOVE its bar (a 300px left
 *                           gutter leaves no usable track at portrait width), and
 *                           the value prints beneath the bar rather than after it.
 *   · LnkDisproportion916 — two tracks stack with the dashed proportional reference
 *                           carried down between them.
 *   · LnkAllOrNothing916  — same three bands; the 4.3% sliver stays a sliver.
 *   · LnkContradiction916 — the two blocks stop being side-by-side and become
 *                           TOP and BOTTOM, so the drives collide vertically.
 *   · LnkPressure916      — the two pressure blocks stack; the date axis runs
 *                           beneath both, as in landscape.
 *
 * KEEP-OUT: content stays above y≈1440 and left of x≈960 — the Shorts/Reels chrome
 * region — and the brand bug sits lower-left. Citation discipline is identical to
 * the landscape set: every figure-bearing component REQUIRES a `source`, values
 * render verbatim as strings, `bar` stays separate from `value`, and there is still
 * no remainder-bar prop on LnkAllOrNothing916.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {SAFE916} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {JdgStakes916} from './JudgmentIsTheJob916';
import type {
  BlufData, FrameData, StatData, LadderData, DispData, AllOrNothingData,
  ContraData, PressureData,
} from './NobodyWroteThis';

/** B09 reuses the generic portrait stakes shape, as it does in landscape. */
export const LnkFalsify916 = JdgStakes916;

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
    <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 76, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 76, color: CLAUDE.INK, lineHeight: 1.06}}>
      {title}
    </div>
  </>
);

const Source: React.FC<{source: string; opacity: number}> = ({source, opacity}) => (
  <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 152, width: BOX.w, opacity, fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE, lineHeight: 1.25}}>
    Source: {source}
  </div>
);

const Note: React.FC<{note: string; opacity: number}> = ({note, opacity}) => (
  <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 88, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 38, color: CLAUDE.INK, lineHeight: 1.25, opacity}}>
    {note}
  </div>
);

/* ── B01 — the BLUF, stacked ─────────────────────────────────────────────── */
export const LnkBluf916: React.FC<{data: BlufData}> = ({data}) => {
  const p = useP();
  const leadIn = win(p, 0.04, 0.22);
  const hotIn = win(p, 0.26, 0.46);
  const struckIn = win(p, 0.5, 0.62);
  const strikeIn = win(p, 0.66, 0.76);
  const replaceIn = win(p, 0.76, 0.88);

  return (
    <Stage>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.16em', color: MUTE, fontWeight: 600, opacity: leadIn}}>
        {data.slideMeta.toUpperCase()}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 110, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 84, lineHeight: 1.16, color: CLAUDE.INK}}>
        <span style={{opacity: leadIn}}>{data.lead} </span>
        <span style={{color: CLAUDE.SPARK, opacity: hotIn}}>{data.hot}</span>
      </div>

      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 720, width: BOX.w}}>
        <span style={{position: 'relative', display: 'inline-block', fontFamily: CLAUDE_FONT.ui, fontSize: 52, color: MUTE, opacity: struckIn}}>
          {data.struck}
          <span style={{position: 'absolute', left: 0, top: '54%', height: 4, width: `${100 * strikeIn}%`, backgroundColor: MUTE}} />
        </span>
      </div>
      <div
        style={{
          position: 'absolute', left: BOX.x, top: BOX.y + 830, width: BOX.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 80, color: CLAUDE.INK, lineHeight: 1.1,
          opacity: replaceIn, transform: `translateY(${(1 - replaceIn) * 18}px)`,
        }}
      >
        {data.replacement}
      </div>

      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 118, width: BOX.w * 0.5 * win(p, 0.9, 0.99), height: 3, backgroundColor: RULE}} />
      <Note note={data.closer} opacity={win(p, 0.9, 0.99)} />
    </Stage>
  );
};

/* ── B02 — three empty bins ──────────────────────────────────────────────── */
export const LnkFrame916: React.FC<{data: FrameData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 300;
  const BAND = 210;
  const GAP = 54;

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.bins.map((b, i) => {
        const draw = win(p, 0.08 + i * 0.18, 0.24 + i * 0.18);
        const text = win(p, 0.16 + i * 0.18, 0.3 + i * 0.18);
        const hot = i === data.hotIndex ? win(p, 0.8, 0.92) : 0;
        const y = TOP + i * (BAND + GAP);
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w * draw, height: BAND, border: `2px solid ${RULE}`, boxSizing: 'border-box'}} />
            <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w, height: BAND, border: `3px solid ${CLAUDE.SPARK}`, boxSizing: 'border-box', opacity: hot}} />
            <div style={{position: 'absolute', left: BOX.x + 30, top: y + 40, maxWidth: BOX.w - 60, fontFamily: CLAUDE_FONT.ui, fontSize: 44, color: CLAUDE.INK, opacity: text, lineHeight: 1.15}}>
              {b.label}
            </div>
            <div style={{position: 'absolute', left: BOX.x + 30, top: y + 140, maxWidth: BOX.w - 60, fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: MUTE, opacity: text}}>
              {b.sub}
            </div>
          </React.Fragment>
        );
      })}
      <Source source={data.source} opacity={win(p, 0.86, 0.95)} />
      <Note note={data.note} opacity={win(p, 0.88, 0.97)} />
    </Stage>
  );
};

/* ── B03 — the hero figure ───────────────────────────────────────────────── */
export const LnkStat916: React.FC<{data: StatData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 330;
  const figIn = win(p, 0.1, 0.36);

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      <div style={{position: 'absolute', left: BOX.x, top: TOP, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 290, lineHeight: 1, color: CLAUDE.SPARK, opacity: figIn}}>
        {data.value}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: TOP + 322, width: BOX.w * 0.6 * win(p, 0.4, 0.6), height: 5, backgroundColor: CLAUDE.SPARK}} />
      <div style={{position: 'absolute', left: BOX.x, top: TOP + 366, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 44, color: CLAUDE.INK, lineHeight: 1.28, opacity: win(p, 0.44, 0.64)}}>
        {data.label}
      </div>
      <div
        style={{
          position: 'absolute', left: BOX.x, top: TOP + 540,
          fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: MUTE, letterSpacing: '.1em',
          textTransform: 'uppercase' as const, opacity: win(p, 0.62, 0.78),
          border: `1px solid ${RULE}`, padding: '12px 20px', display: 'inline-block',
        }}
      >
        {data.rank}
      </div>
      <Source source={data.source} opacity={win(p, 0.78, 0.9)} />
      <Note note={data.note} opacity={win(p, 0.86, 0.96)} />
    </Stage>
  );
};

/* ── B05 — the ladder: name above the bar, value beneath it ──────────────── */
export const LnkLadder916: React.FC<{data: LadderData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 290;
  const ROW = 168;
  const BAR_H = 56;
  const maxBar = Math.max(...data.items.map((i) => i.bar), data.baseline.bar) * 1.06;
  const baseX = BOX.x + BOX.w * (data.baseline.bar / maxBar);
  const baseIn = win(p, 0.74, 0.88);

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.items.map((it, i) => {
        const g = win(p, 0.08 + i * 0.12, 0.26 + i * 0.12);
        const w = BOX.w * (it.bar / maxBar) * g;
        const c = it.hot ? CLAUDE.SPARK : CLAUDE.INK;
        const y = TOP + i * ROW;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w * 0.6, fontFamily: CLAUDE_FONT.ui, fontSize: 36, color: CLAUDE.INK, opacity: 0.35 + 0.65 * g}}>
              {it.label}
            </div>
            <div style={{position: 'absolute', left: BOX.x, top: y + 54, width: BOX.w, height: 1, backgroundColor: RULE}} />
            <div style={{position: 'absolute', left: BOX.x, top: y + 54, width: w, height: BAR_H, backgroundColor: c}} />
            <div
              style={{
                position: 'absolute', left: BOX.x, top: y - 6, width: BOX.w,
                fontFamily: CLAUDE_FONT.serif, fontSize: 54, color: c, opacity: g,
                lineHeight: 1, textAlign: 'right' as const, whiteSpace: 'nowrap' as const,
              }}
            >
              {it.value}
            </div>
          </React.Fragment>
        );
      })}

      <div
        style={{
          position: 'absolute', left: baseX, top: TOP + 40,
          width: 0, height: (data.items.length * ROW - 40) * baseIn,
          borderLeft: `3px dashed ${MUTE}`, opacity: 0.85 * baseIn,
        }}
      />
      <div
        style={{
          position: 'absolute', left: BOX.x, top: TOP + data.items.length * ROW + 6, width: BOX.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: MUTE, opacity: baseIn,
        }}
      >
        {data.baseline.label}
      </div>

      <Source source={data.source} opacity={win(p, 0.84, 0.94)} />
      <Note note={data.note} opacity={win(p, 0.88, 0.97)} />
    </Stage>
  );
};

/* ── B06 — the disproportion ─────────────────────────────────────────────── */
export const LnkDisproportion916: React.FC<{data: DispData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 320;
  const BAND = 130;
  const T2 = TOP + 380;
  const topIn = win(p, 0.1, 0.36);
  const botIn = win(p, 0.42, 0.68);
  const refIn = win(p, 0.7, 0.84);
  const topW = BOX.w * (data.top.bar / 100) * topIn;
  const botW = BOX.w * (data.bottom.bar / 100) * botIn;
  const refX = BOX.x + BOX.w * (data.top.bar / 100);

  const row = (y: number, d: {label: string; value: string}, w: number, accent: boolean, g: number) => (
    <>
      <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w, height: BAND, border: `1px solid ${RULE}`, boxSizing: 'border-box'}} />
      <div style={{position: 'absolute', left: BOX.x, top: y, width: w, height: BAND, backgroundColor: accent ? CLAUDE.SPARK : CLAUDE.INK, opacity: accent ? 1 : 0.85}} />
      <div style={{position: 'absolute', left: BOX.x, top: y + BAND + 16, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: accent ? CLAUDE.SPARK : CLAUDE.INK, opacity: g, lineHeight: 1.25}}>
        {d.label}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: y + BAND + 92, fontFamily: CLAUDE_FONT.serif, fontSize: 68, color: accent ? CLAUDE.SPARK : CLAUDE.INK, opacity: g, lineHeight: 1}}>
        {d.value}
      </div>
    </>
  );

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {row(TOP, data.top, topW, false, topIn)}
      {row(T2, data.bottom, botW, true, botIn)}
      {/* Two segments, one per band — same fix as landscape: a continuous rule
          ran straight through the first track's label and value in the gap. */}
      <div
        style={{
          position: 'absolute', left: refX, top: TOP,
          width: 0, height: BAND * refIn,
          borderLeft: `3px dashed ${MUTE}`, opacity: 0.9 * refIn,
        }}
      />
      <div
        style={{
          position: 'absolute', left: refX, top: T2,
          width: 0, height: BAND * refIn,
          borderLeft: `3px dashed ${MUTE}`, opacity: 0.9 * refIn,
        }}
      />
      <div style={{position: 'absolute', left: BOX.x, top: T2 + BAND + 170, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 27, color: MUTE, opacity: refIn}}>
        proportional would stop at the dashed line
      </div>
      <Source source={data.source} opacity={win(p, 0.84, 0.94)} />
      <Note note={data.note} opacity={win(p, 0.88, 0.97)} />
    </Stage>
  );
};

/* ── B07 — all or nothing (still no remainder bar) ───────────────────────── */
export const LnkAllOrNothing916: React.FC<{data: AllOrNothingData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 300;
  const BAND = 140;
  const STEP = 250;

  const filled = (y: number, d: {label: string; value: string; bar: number}, accent: boolean, g: number) => (
    <>
      <div style={{position: 'absolute', left: BOX.x, top: y - 46, maxWidth: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 32, color: CLAUDE.INK, opacity: g}}>
        {d.label}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w, height: BAND, border: `2px solid ${RULE}`, boxSizing: 'border-box'}} />
      <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w * (d.bar / 100) * g, height: BAND, backgroundColor: accent ? CLAUDE.SPARK : CLAUDE.INK, opacity: accent ? 1 : 0.88}} />
      <div style={{position: 'absolute', left: BOX.x, top: y + 34, width: BOX.w - 24, fontFamily: CLAUDE_FONT.serif, fontSize: 70, color: accent ? CLAUDE.SPARK : CLAUDE.INK, opacity: g, lineHeight: 1, textAlign: 'right' as const}}>
        {d.value}
      </div>
    </>
  );

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {filled(TOP + 46, data.assisted, true, win(p, 0.16, 0.4))}
      {filled(TOP + 46 + STEP, data.generated, false, win(p, 0.44, 0.66))}
      <div style={{position: 'absolute', left: BOX.x, top: TOP + 46 + 2 * STEP, width: BOX.w, height: BAND, border: `2px dashed ${RULE}`, boxSizing: 'border-box', opacity: win(p, 0.66, 0.82)}} />
      <div style={{position: 'absolute', left: BOX.x + 26, top: TOP + 46 + 2 * STEP + 44, maxWidth: BOX.w - 52, fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE, opacity: win(p, 0.7, 0.86), lineHeight: 1.25}}>
        {data.remainderLabel}
      </div>
      <Source source={data.source} opacity={win(p, 0.84, 0.94)} />
      <Note note={data.note} opacity={win(p, 0.88, 0.97)} />
    </Stage>
  );
};

/* ── B08 — the contradiction, collided VERTICALLY ────────────────────────── */
export const LnkContradiction916: React.FC<{data: ContraData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 290;
  const BOX_H = 300;
  const LANE_TOP = TOP + BOX_H;
  const LANE_H = 210;
  const MIDY = LANE_TOP + LANE_H / 2;
  const B2 = LANE_TOP + LANE_H;
  const leftIn = win(p, 0.08, 0.3);
  const rightIn = win(p, 0.34, 0.56);
  const driveIn = win(p, 0.56, 0.76);
  const hitIn = win(p, 0.76, 0.9);

  const block = (y: number, d: {heading: string; label: string; sub: string}, g: number) => (
    <>
      <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w, height: BOX_H, border: `2px solid ${RULE}`, boxSizing: 'border-box', opacity: g}} />
      <div style={{position: 'absolute', left: BOX.x + 28, top: y + 26, fontFamily: CLAUDE_FONT.ui, fontSize: 24, letterSpacing: '.18em', color: MUTE, fontWeight: 600, opacity: g}}>
        {d.heading.toUpperCase()}
      </div>
      <div style={{position: 'absolute', left: BOX.x + 28, top: y + 72, maxWidth: BOX.w - 56, fontFamily: CLAUDE_FONT.serif, fontSize: 60, color: CLAUDE.INK, opacity: g, lineHeight: 1.1}}>
        {d.label}
      </div>
      <div style={{position: 'absolute', left: BOX.x + 28, top: y + 190, maxWidth: BOX.w - 56, fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: MUTE, opacity: g, lineHeight: 1.3}}>
        {d.sub}
      </div>
    </>
  );

  const reach = (LANE_H / 2 - 10) * driveIn;

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {block(TOP, data.left, leftIn)}
      {block(B2, data.right, rightIn)}

      {/* the drives run down and up the centre column */}
      <div style={{position: 'absolute', left: BOX.x + BOX.w / 2 - 6, top: LANE_TOP + 6, width: 12, height: reach, backgroundColor: CLAUDE.INK, opacity: 0.75 * driveIn}} />
      <div style={{position: 'absolute', left: BOX.x + BOX.w / 2 - 6, top: B2 - 6 - reach, width: 12, height: reach, backgroundColor: CLAUDE.INK, opacity: 0.75 * driveIn}} />
      <div style={{position: 'absolute', left: BOX.x + BOX.w / 2 - 26, top: MIDY - 13, width: 52, height: 26, backgroundColor: CLAUDE.SPARK, opacity: hitIn}} />
      <div
        style={{
          position: 'absolute', left: BOX.x, top: MIDY + 28, width: BOX.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 46, color: CLAUDE.SPARK,
          opacity: hitIn, textAlign: 'center' as const,
        }}
      >
        {data.collision}
      </div>

      <Source source={data.source} opacity={win(p, 0.86, 0.95)} />
      <Note note={data.note} opacity={win(p, 0.9, 0.98)} />
    </Stage>
  );
};

/* ── B10 — the two pressures, stacked, over one date axis ────────────────── */
export const LnkPressure916: React.FC<{data: PressureData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 270;
  const BOX_H = 330;
  const GAP = 46;
  const AXIS = TOP + 2 * BOX_H + GAP + 96;
  const markX = BOX.x + BOX.w * 0.5;

  const block = (y: number, d: {tag: string; label: string; sub: string; cite: string}, g: number, accent: boolean) => (
    <>
      <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w, height: BOX_H, border: `2px solid ${RULE}`, boxSizing: 'border-box', opacity: g}} />
      <div
        style={{
          position: 'absolute', left: BOX.x + 26, top: y + 24,
          fontFamily: CLAUDE_FONT.ui, fontSize: 21, letterSpacing: '.2em', fontWeight: 600,
          color: accent ? CLAUDE.SPARK : MUTE, border: `1px solid ${accent ? CLAUDE.SPARK : RULE}`,
          padding: '8px 14px', display: 'inline-block', opacity: g,
        }}
      >
        {d.tag}
      </div>
      <div style={{position: 'absolute', left: BOX.x + 26, top: y + 90, maxWidth: BOX.w - 52, fontFamily: CLAUDE_FONT.serif, fontSize: 58, color: CLAUDE.INK, opacity: g, lineHeight: 1.08}}>
        {d.label}
      </div>
      <div style={{position: 'absolute', left: BOX.x + 26, top: y + 166, maxWidth: BOX.w - 52, fontFamily: CLAUDE_FONT.ui, fontSize: 29, color: CLAUDE.INK, opacity: g * 0.9, lineHeight: 1.3}}>
        {d.sub}
      </div>
      <div style={{position: 'absolute', left: BOX.x + 26, top: y + BOX_H - 50, maxWidth: BOX.w - 52, fontFamily: CLAUDE_FONT.ui, fontSize: 24, color: MUTE, opacity: g}}>
        {d.cite}
      </div>
    </>
  );

  const axisIn = win(p, 0.6, 0.78);
  const markIn = win(p, 0.78, 0.92);

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {block(TOP, data.left, win(p, 0.08, 0.32), false)}
      {block(TOP + BOX_H + GAP, data.right, win(p, 0.36, 0.6), true)}

      <div style={{position: 'absolute', left: BOX.x, top: AXIS, width: BOX.w * axisIn, height: 2, backgroundColor: RULE}} />
      <div style={{position: 'absolute', left: markX, top: AXIS - 24, width: 4, height: 50 * markIn, backgroundColor: CLAUDE.SPARK}} />
      <div style={{position: 'absolute', left: BOX.x, top: AXIS + 40, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 46, color: CLAUDE.SPARK, opacity: markIn}}>
        {data.marker}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: AXIS + 100, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 27, color: MUTE, opacity: markIn, lineHeight: 1.25}}>
        {data.axisLabel}
      </div>

      <Note note={data.note} opacity={win(p, 0.9, 0.98)} />
    </Stage>
  );
};
