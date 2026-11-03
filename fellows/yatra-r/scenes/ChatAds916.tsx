/**
 * ChatAds916.tsx — PORTRAIT (9:16) scenes for `yatra-ads-in-the-picture`.
 *
 * Re-banded vertically, NOT scaled clones:
 *
 *   · AdpBluf916     — the rails still enter from opposite sides, one above the other,
 *                      and bend into a meeting point lower in the frame.
 *   · AdpCanvas916   — the ad panel sits BELOW the user's image instead of beside it;
 *                      the bracketed gap becomes vertical.
 *   · AdpRoom916     — the conversation sits on top, the reframe lines beneath it.
 *   · AdpDots916     — the dot and its computer share a top row; the app field is a
 *                      10-wide grid under them.
 *   · AdpConverge916 — the two cards stack and slide together vertically; the seam is
 *                      horizontal.
 *   · AdpChannel916  — the channel sequence runs top-to-bottom.
 *
 * Every refusal holds because the types are imported from ChatAds.tsx rather than
 * redeclared: `source` is still required wherever an announced fact appears, `value`
 * is still printed verbatim and never counted, `tileNote` and `caption` are still
 * required on the two illustrative scenes.
 *
 * KEEP-OUT: content stays above y≈1440 and left of x≈960 — the Shorts/Reels chrome
 * region — with the brand bug lower-left.
 */
import React from 'react';
import {AbsoluteFill} from 'remotion';
import {SAFE916} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {useP, typed, GeneratedArt, AdPlaceholder, AlwaysOnDot, CheckBox} from './ChatAds';
import type {
  BlufData, RolloutData, CanvasData, RoomData, DotsData, ConvergeData, ChannelData, LimitsData,
} from './ChatAds';

const STAGE = '#F2F0E9';
const RULE = '#D8D4C8';
const MUTE = '#7A7265';
const BOX = {x: SAFE916.x, y: SAFE916.y, w: 906, bottom: 1440} as const;
const BOX_R = BOX.x + BOX.w;
const MID = BOX.x + BOX.w / 2;

const ease = (t: number) => 1 - Math.pow(1 - Math.min(1, Math.max(0, t)), 3);
const win = (p: number, a: number, b: number) => ease((p - a) / (b - a));

const Stage: React.FC<{children: React.ReactNode}> = ({children}) => (
  <AbsoluteFill style={{backgroundColor: STAGE}}>
    {children}
    <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom + 40, fontFamily: CLAUDE_FONT.serif, fontSize: 30, color: CLAUDE.INK, opacity: 0.3, letterSpacing: '.04em'}}>
      @Yatra
    </div>
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
    <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 70, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 72, color: CLAUDE.INK, lineHeight: 1.06}}>
      {title}
    </div>
  </>
);

const Note: React.FC<{note: string; opacity: number}> = ({note, opacity}) => (
  <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 96, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 40, color: CLAUDE.INK, lineHeight: 1.22, opacity}}>
    {note}
  </div>
);

const SourceLine: React.FC<{source: string; opacity: number; top?: number}> = ({source, opacity, top}) => (
  <div style={{position: 'absolute', left: BOX.x, top: top ?? BOX.bottom - 166, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE, opacity, lineHeight: 1.3}}>
    Source: {source}
  </div>
);

const chipStyle = (hot: boolean | undefined, size: number): React.CSSProperties => ({
  fontFamily: CLAUDE_FONT.ui, fontSize: size, fontWeight: 600,
  letterSpacing: '.14em', textTransform: 'uppercase',
  color: hot ? CLAUDE.SPARK : MUTE,
  border: `${hot ? 2 : 1}px solid ${hot ? CLAUDE.SPARK : RULE}`,
  padding: '9px 15px', display: 'inline-block', whiteSpace: 'nowrap',
  backgroundColor: hot ? '#FFFFFF' : 'transparent',
});

/* ── B01 — two rails, stacked, bending into one point ── */
export const AdpBluf916: React.FC<{data: BlufData}> = ({data}) => {
  const p = useP();
  const yT = BOX.y + 400;
  const yB = BOX.y + 480;
  const yM = BOX.y + 720;
  const g1 = win(p, 0.06, 0.24);
  const g2 = win(p, 0.28, 0.46);
  const m = win(p, 0.52, 0.64);

  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 110, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 76, lineHeight: 1.1, color: CLAUDE.INK, opacity: g1}}>
        {data.top}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 230, width: BOX.w, textAlign: 'right', fontFamily: CLAUDE_FONT.serif, fontSize: 76, lineHeight: 1.1, color: CLAUDE.INK, opacity: g2}}>
        {data.bottom}
      </div>
      <svg width={1080} height={1920} style={{position: 'absolute', left: 0, top: 0}}>
        <line x1={BOX.x} y1={yT} x2={BOX.x + (MID - 90 - BOX.x) * g1} y2={yT} stroke={CLAUDE.INK} strokeWidth={4} />
        <line x1={BOX_R} y1={yB} x2={BOX_R - (BOX_R - (MID + 90)) * g2} y2={yB} stroke={CLAUDE.INK} strokeWidth={4} />
        <path d={`M ${MID - 90} ${yT} Q ${MID} ${yT} ${MID} ${yM}`} fill="none" stroke={CLAUDE.INK} strokeWidth={4} pathLength={1} strokeDasharray={1} strokeDashoffset={1 - m} />
        <path d={`M ${MID + 90} ${yB} Q ${MID} ${yB} ${MID} ${yM}`} fill="none" stroke={CLAUDE.INK} strokeWidth={4} pathLength={1} strokeDasharray={1} strokeDashoffset={1 - m} />
        <circle cx={MID} cy={yM} r={16 * win(p, 0.6, 0.66)} fill={CLAUDE.SPARK} />
      </svg>
      <div style={{position: 'absolute', left: BOX.x, top: yM + 40, width: BOX.w, textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: 76, lineHeight: 1.12, color: CLAUDE.SPARK, opacity: win(p, 0.64, 0.76)}}>
        {data.meet}
      </div>
      <Note note={data.closer} opacity={win(p, 0.86, 0.97)} />
    </Stage>
  );
};

/* ── B02 — the spec sheet; key above value so the rows fit the narrow column ── */
export const AdpRollout916: React.FC<{data: RolloutData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 300;
  const STEP = 148;
  const st = win(p, 0.1, 0.18);
  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 196, ...chipStyle(true, 30), opacity: st, transform: `scale(${1.35 - 0.35 * st})`, transformOrigin: 'left center'}}>
        {data.stamp}
      </div>
      {data.rows.map((r, i) => {
        const g = win(p, 0.16 + i * 0.1, 0.26 + i * 0.1);
        const y = TOP + i * STEP;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 24, letterSpacing: '.16em', fontWeight: 600, color: MUTE, opacity: g}}>
              {r.key.toUpperCase()}
            </div>
            <div style={{position: 'absolute', left: BOX.x, top: y + 38, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 58, lineHeight: 1.1, color: CLAUDE.INK, opacity: g}}>
              {r.value}
            </div>
            <div style={{position: 'absolute', left: BOX.x, top: y + 124, width: BOX.w * g, height: 1, backgroundColor: RULE}} />
          </React.Fragment>
        );
      })}
      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} top={BOX.bottom - 60} />
    </Stage>
  );
};

/* ── B04 — the ad panel sits BELOW the image; the gap is bracketed vertically ── */
export const AdpCanvas916: React.FC<{data: CanvasData}> = ({data}) => {
  const p = useP();
  const WIN_Y = BOX.y + 262;
  const IMG_X = BOX.x + 28;
  const IMG_W = BOX.w - 56;
  const IMG_Y = WIN_Y + 92;
  const IMG_H = 380;
  const GAP = 120;
  const AD_Y = IMG_Y + IMG_H + GAP;
  const AD_H = 230;
  const WIN_H = AD_Y + AD_H + 28 - WIN_Y;

  const draw = win(p, 0.04, 0.14);
  const gen = win(p, 0.12, 0.38);
  const ad = win(p, 0.36, 0.5);
  const gap = win(p, 0.54, 0.66);

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      <div style={{position: 'absolute', left: BOX.x, top: WIN_Y, width: BOX.w, height: WIN_H, backgroundColor: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 18, opacity: draw}} />
      <div style={{position: 'absolute', left: BOX.x + 28, top: WIN_Y + 22, width: BOX.w - 56, height: 44, borderRadius: 22, backgroundColor: CLAUDE.PILL, opacity: draw}}>
        <div style={{position: 'absolute', left: 26, top: 17, width: 420, height: 10, borderRadius: 5, backgroundColor: CLAUDE.INK, opacity: 0.2}} />
      </div>
      <div style={{position: 'absolute', left: IMG_X, top: IMG_Y, width: IMG_W, height: IMG_H, borderRadius: 10, overflow: 'hidden', border: `1px solid ${RULE}`, opacity: draw}}>
        <GeneratedArt w={IMG_W} h={IMG_H} reveal={gen} />
      </div>

      {/* the vertical gap, bracketed and named */}
      <svg width={1080} height={1920} style={{position: 'absolute', left: 0, top: 0, opacity: gap}}>
        <line x1={IMG_X + 30} y1={IMG_Y + IMG_H + 10} x2={IMG_X + 30} y2={IMG_Y + IMG_H + 10 + (GAP - 20) * gap} stroke={CLAUDE.INK} strokeWidth={3} />
        <line x1={IMG_X + 18} y1={IMG_Y + IMG_H + 10} x2={IMG_X + 42} y2={IMG_Y + IMG_H + 10} stroke={CLAUDE.INK} strokeWidth={3} />
        <line x1={IMG_X + 18} y1={AD_Y - 10} x2={IMG_X + 42} y2={AD_Y - 10} stroke={CLAUDE.INK} strokeWidth={3} />
      </svg>
      <div style={{position: 'absolute', left: IMG_X + 66, top: IMG_Y + IMG_H + GAP / 2 - 18, fontFamily: CLAUDE_FONT.ui, fontSize: 28, fontWeight: 600, color: CLAUDE.INK, opacity: gap}}>
        {data.gapLabel}
      </div>

      <div style={{position: 'absolute', left: IMG_X, top: AD_Y, width: IMG_W, height: AD_H, boxSizing: 'border-box', border: `2px dashed ${CLAUDE.INK_SOFT}`, borderRadius: 10, padding: 24, opacity: ad}}>
        <div style={{...chipStyle(true, 26)}}>{data.adTag}</div>
        <div style={{position: 'absolute', left: 200, top: 24}}>
          <AdPlaceholder w={IMG_W - 240} h={AD_H - 48} />
        </div>
      </div>

      <div style={{position: 'absolute', left: BOX.x, top: WIN_Y + WIN_H + 20, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: CLAUDE.INK, opacity: win(p, 0.68, 0.8)}}>
        {data.imageLabel}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: WIN_Y + WIN_H + 64, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: CLAUDE.SPARK, opacity: win(p, 0.72, 0.84)}}>
        {data.adLabel}
      </div>
      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} top={BOX.bottom - 120} />
      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 82, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 24, lineHeight: 1.3, color: MUTE, opacity: win(p, 0.86, 0.96)}}>
        {data.caption}
      </div>
    </Stage>
  );
};

/* ── B05 — the conversation on top, the reframe beneath ── */
export const AdpRoom916: React.FC<{data: RoomData}> = ({data}) => {
  const p = useP();
  const COL_Y = BOX.y + 70;
  const COL_H = 480;
  const frameIn = win(p, 0.6, 0.74);
  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />
      <div style={{position: 'absolute', left: BOX.x, top: COL_Y, width: BOX.w, height: COL_H, border: `3px dashed ${CLAUDE.SPARK}`, borderRadius: 22, opacity: frameIn * 0.8}} />
      <div style={{position: 'absolute', left: BOX.x + 36, top: COL_Y + 50, width: BOX.w - 72, display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: 40}}>
        {data.bubbles.map((b, i) => {
          const g = win(p, 0.12 + i * 0.09, 0.22 + i * 0.09);
          return (
            <div key={i} style={{maxWidth: 720, backgroundColor: CLAUDE.PILL, borderRadius: 30, padding: '24px 34px', fontFamily: CLAUDE_FONT.ui, fontSize: 36, lineHeight: 1.25, color: CLAUDE.INK, opacity: g}}>
              {b}
            </div>
          );
        })}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: COL_Y + COL_H + 14, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 24, color: MUTE, opacity: win(p, 0.3, 0.4)}}>
        {data.caption}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: COL_Y + COL_H + 120, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 100, lineHeight: 1.08, color: CLAUDE.INK, opacity: win(p, 0.4, 0.52)}}>
        {data.before}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: COL_Y + COL_H + 260, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 100, lineHeight: 1.08, color: CLAUDE.SPARK}}>
        {typed(data.after, win(p, 0.58, 0.74))}
      </div>
      <Note note={data.note} opacity={win(p, 0.86, 0.96)} />
    </Stage>
  );
};

/* ── B06 — dot + computer on one row, the app field beneath ── */
export const AdpDots916: React.FC<{data: DotsData}> = ({data}) => {
  const p = useP();
  const DX = BOX.x + 70;
  const DY = BOX.y + 290;
  const COLS = 10;
  const ROWS = 5;
  const T = 66;
  const G = 22;
  const GX = BOX.x + (BOX.w - (COLS * (T + G) - G)) / 2;
  const GY = BOX.y + 520;
  const CX = BOX_R - 270;

  const appear = win(p, 0.06, 0.14);
  const box = win(p, 0.22, 0.34);
  const targets = [[0, 0], [0, 2], [0, 4], [2, 1], [3, 3], [5, 0], [6, 4], [8, 2], [9, 0]];

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      <svg width={1080} height={1920} style={{position: 'absolute', left: 0, top: 0}}>
        {targets.map(([c, r], i) => {
          const g = win(p, 0.4 + i * 0.015, 0.54 + i * 0.015);
          return (
            <line key={i} x1={DX} y1={DY} x2={DX + (GX + c * (T + G) + T / 2 - DX) * g} y2={DY + (GY + r * (T + G) + T / 2 - DY) * g} stroke={CLAUDE.INK} strokeWidth={2} opacity={0.35} />
          );
        })}
        <line x1={DX + 60} y1={DY} x2={DX + 60 + (CX - DX - 60) * box} y2={DY} stroke={CLAUDE.INK} strokeWidth={3} opacity={0.6} />
      </svg>
      {Array.from({length: COLS * ROWS}).map((_, k) => {
        const c = k % COLS;
        const r = Math.floor(k / COLS);
        const shown = win(p, 0.3 + c * 0.006, 0.4 + c * 0.006);
        const lit = win(p, 0.42 + c * 0.018, 0.5 + c * 0.018);
        return (
          <div key={k} style={{position: 'absolute', left: GX + c * (T + G), top: GY + r * (T + G), width: T, height: T, borderRadius: 12, boxSizing: 'border-box', border: `2px solid ${CLAUDE.INK_SOFT}`, backgroundColor: `rgba(61, 57, 41, ${0.06 + 0.3 * lit})`, opacity: shown}} />
        );
      })}
      <AlwaysOnDot cx={DX} cy={DY} r={48} appear={appear} />
      <div style={{position: 'absolute', left: DX + 70, top: DY - 56, width: 300, fontFamily: CLAUDE_FONT.ui, fontSize: 28, fontWeight: 600, color: CLAUDE.INK, opacity: win(p, 0.1, 0.2)}}>
        {data.dotLabel}
      </div>
      <div style={{position: 'absolute', left: CX, top: DY - 75, opacity: box}}>
        <div style={{width: 230, height: 130, border: `3px solid ${CLAUDE.INK}`, borderRadius: 12, backgroundColor: CLAUDE.CARD, position: 'relative'}}>
          {[0, 1, 2].map((k) => (
            <div key={k} style={{position: 'absolute', left: 22, top: 24 + k * 30, width: k === 2 ? 100 : 180, height: 11, borderRadius: 6, backgroundColor: CLAUDE.INK, opacity: 0.22}} />
          ))}
        </div>
        <div style={{width: 70, height: 16, margin: '0 auto', backgroundColor: CLAUDE.INK, opacity: 0.5}} />
        <div style={{width: 270, marginLeft: -20, marginTop: 10, textAlign: 'center', fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: CLAUDE.INK}}>
          {data.computerLabel}
        </div>
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: GY + ROWS * (T + G) + 16, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 130, lineHeight: 1, color: CLAUDE.INK, opacity: win(p, 0.56, 0.68), whiteSpace: 'nowrap'}}>
        {data.value}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: GY + ROWS * (T + G) + 160, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 34, color: CLAUDE.INK, opacity: win(p, 0.62, 0.74)}}>
        {data.valueLabel}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 104, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 24, color: MUTE, opacity: win(p, 0.8, 0.9)}}>
        {data.tileNote}
      </div>
      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} top={BOX.bottom - 64} />
    </Stage>
  );
};

/* ── B07 — the cards stack and slide together; the seam runs across ── */
export const AdpConverge916: React.FC<{data: ConvergeData}> = ({data}) => {
  const p = useP();
  const CARD_H = 330;
  const SPREAD = 140;
  const TOP = BOX.y + 90;
  const slide = win(p, 0.5, 0.66);
  const shift = (SPREAD / 2) * slide;
  const seamY = TOP + CARD_H + SPREAD / 2;
  const seam = win(p, 0.6, 0.72);

  const card = (y: number, c: {tag: string; label: string}, g: number) => (
    <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w, height: CARD_H, boxSizing: 'border-box', padding: '40px 44px', backgroundColor: CLAUDE.CARD, border: `2px solid ${CLAUDE.INK}`, borderRadius: 16, opacity: g}}>
      <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 28, letterSpacing: '.18em', fontWeight: 600, color: MUTE}}>{c.tag.toUpperCase()}</div>
      <div style={{marginTop: 24, fontFamily: CLAUDE_FONT.serif, fontSize: 62, lineHeight: 1.12, color: CLAUDE.INK}}>{c.label}</div>
    </div>
  );

  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />
      {card(TOP + shift, data.left, win(p, 0.06, 0.2))}
      {card(TOP + CARD_H + SPREAD - shift, data.right, win(p, 0.28, 0.42))}
      <div style={{position: 'absolute', left: BOX.x - 10, top: seamY - 4, width: (BOX.w + 20) * seam, height: 8, backgroundColor: CLAUDE.SPARK}} />
      <div style={{position: 'absolute', left: BOX.x, top: TOP + 2 * CARD_H + SPREAD + 40, width: BOX.w, textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: 50, color: CLAUDE.SPARK, opacity: win(p, 0.66, 0.76)}}>
        {data.seam}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: TOP + 2 * CARD_H + SPREAD + 130, width: BOX.w, textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: 62, lineHeight: 1.12, color: CLAUDE.INK, opacity: win(p, 0.78, 0.9)}}>
        {data.verdict}
      </div>
      <Note note={data.note} opacity={win(p, 0.9, 0.99)} />
    </Stage>
  );
};

/* ── B08 — the channel sequence runs top-to-bottom ── */
export const AdpChannel916: React.FC<{data: ChannelData}> = ({data}) => {
  const p = useP();
  const N = data.steps.length;
  const ARROW = 90;
  const SLOT_H = 230;
  const TOP = BOX.y + 210;
  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.steps.map((s, i) => {
        const open = i === N - 1;
        const g = win(p, 0.06 + i * 0.18, 0.18 + i * 0.18);
        const y = TOP + i * (SLOT_H + ARROW);
        const arrow = i < N - 1 ? win(p, 0.2 + i * 0.18, 0.28 + i * 0.18) : 0;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w, height: SLOT_H, boxSizing: 'border-box', borderRadius: 16, border: open ? `4px dashed ${CLAUDE.SPARK}` : `2px solid ${CLAUDE.INK}`, backgroundColor: open ? 'transparent' : CLAUDE.CARD, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 24, opacity: g}}>
              <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: 60, color: CLAUDE.INK}}>{s.label}</div>
              <div style={chipStyle(open, 24)}>{s.chip}</div>
            </div>
            {open && (
              <div style={{position: 'absolute', left: BOX_R - 70, top: y + 4, fontFamily: CLAUDE_FONT.serif, fontSize: 84, color: CLAUDE.SPARK, opacity: g}}>?</div>
            )}
            {i < N - 1 && (
              <svg width={40} height={ARROW} style={{position: 'absolute', left: MID - 20, top: y + SLOT_H}}>
                <line x1={20} y1={12} x2={20} y2={12 + (ARROW - 36) * arrow} stroke={CLAUDE.INK} strokeWidth={4} />
                <polyline points={`8,${ARROW - 30} 20,${ARROW - 16} 32,${ARROW - 30}`} fill="none" stroke={CLAUDE.INK} strokeWidth={4} opacity={arrow > 0.95 ? 1 : 0} />
              </svg>
            )}
          </React.Fragment>
        );
      })}
      <div style={{position: 'absolute', left: BOX.x, top: TOP + N * SLOT_H + (N - 1) * ARROW + 40, width: BOX.w, textAlign: 'center', fontFamily: CLAUDE_FONT.ui, fontSize: 34, lineHeight: 1.3, color: CLAUDE.INK, opacity: win(p, 0.62, 0.74)}}>
        {data.status}
      </div>
      <Note note={data.note} opacity={win(p, 0.88, 0.97)} />
    </Stage>
  );
};

/* ── B09 — the two lists stack ── */
export const AdpLimits916: React.FC<{data: LimitsData}> = ({data}) => {
  const p = useP();
  const STEP = 84;
  const list = (top: number, h: {heading: string; items: string[]}, startAt: number, hot: boolean) => (
    <>
      <div style={{position: 'absolute', left: BOX.x, top, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 28, letterSpacing: '.16em', fontWeight: 600, color: hot ? CLAUDE.SPARK : MUTE, opacity: win(p, startAt, startAt + 0.08)}}>
        {h.heading.toUpperCase()}
      </div>
      {h.items.map((it, i) => {
        const g = win(p, startAt + 0.04 + i * 0.07, startAt + 0.14 + i * 0.07);
        return (
          <div key={i} style={{position: 'absolute', left: BOX.x, top: top + 62 + i * STEP, width: BOX.w, display: 'flex', alignItems: 'center', gap: 22, opacity: g}}>
            <CheckBox size={42} hot={hot} tick={win(p, startAt + 0.1 + i * 0.07, startAt + 0.18 + i * 0.07)} opacity={1} />
            <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 34, lineHeight: 1.2, color: CLAUDE.INK}}>{it}</div>
          </div>
        );
      })}
    </>
  );
  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {list(BOX.y + 290, data.announced, 0.06, false)}
      {list(BOX.y + 290 + 62 + data.announced.items.length * STEP + 60, data.open, 0.44, true)}
      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 190, width: BOX.w * win(p, 0.76, 0.86), height: 1, backgroundColor: RULE}} />
      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 172, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 25, lineHeight: 1.3, color: MUTE, opacity: win(p, 0.78, 0.88)}}>
        {data.provenance}
      </div>
      <Note note={data.falsifier} opacity={win(p, 0.88, 0.97)} />
    </Stage>
  );
};
