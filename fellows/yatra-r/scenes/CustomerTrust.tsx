/**
 * CustomerTrust.tsx — reel-local scenes for `yatra-no-default-winner`
 * ("No Default Winner." — when an AI tool and a human customer service rep disagree,
 * customers no longer automatically trust the human).
 *
 * ── WHY THESE ARE NEW COMPONENTS ─────────────────────────────────────────────
 * The human asked for a video that is not a variation of any previous one. Nothing from
 * the `Adp*`, `Tbl*`, `Msk*` or earlier families is reused. The shapes come from this
 * reel's argument: an old assumption struck through, two answers that don't match, a
 * balance scale that rocks and settles level, a tiebreaker that becomes one voice of two,
 * a question that sharpens, and a call with a third party on the line.
 *
 * ── THE SOURCING CONSTRAINT, ENFORCED BY THE TYPES ───────────────────────────
 * Five figures were supplied, all from Capacity (October 2026), with the instruction to
 * add nothing. So:
 *
 *   · Every figure-bearing scene REQUIRES a `source` string.
 *   · `value` is a verbatim STRING; `bar` is a separate number that drives drawing.
 *     Nothing parses a displayed string.
 *   · `CtrScale` has NO numeric prop at all. "Equally likely to trust either" was
 *     supplied without a figure, so the scale settles level and the frame prints no
 *     percentage. 50/50 would be an invented number.
 *   · No remainder is ever captioned (100 − 44 is arithmetic, not a finding).
 *   · `CtrContradict` and `CtrSharpen` draw placeholder lines, never an invented
 *     exchange, and REQUIRE a `caption` that says so.
 *   · `CtrTiebreak` is interpretation, and REQUIRES a `note` that says so on screen.
 *
 * ── ACCENT SEMANTICS ─────────────────────────────────────────────────────────
 * Terracotta is the ONE accent per beat and it always marks WHERE THE HUMAN DEFAULT
 * BREAKS — the strike, the younger cohort, the mismatch, the level pivot, the second
 * voice, the agent joining the call. Citations stay muted ink.
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

export const typed = (text: string, g: number) => text.slice(0, Math.round(text.length * g));

/** Beam angle (degrees) for the scale: rocks with decaying amplitude, then holds level. */
export const beamAngle = (p: number, settleAt: number) => {
  if (p >= settleAt) return 0;
  const t = p / settleAt;
  return 7 * (1 - t) * Math.sin(t * Math.PI * 4);
};

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

const Caption: React.FC<{text: string; opacity: number; top: number}> = ({text, opacity, top}) => (
  <div style={{position: 'absolute', left: SAFE.x, top, width: SAFE.w, fontFamily: CLAUDE_FONT.ui, fontSize: 25, color: MUTE, opacity}}>
    {text}
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

export const chipStyle = (hot: boolean | undefined, size: number): React.CSSProperties => ({
  fontFamily: CLAUDE_FONT.ui, fontSize: size, fontWeight: 600,
  letterSpacing: '.16em', textTransform: 'uppercase',
  color: hot ? CLAUDE.SPARK : MUTE,
  border: `${hot ? 2 : 1}px solid ${hot ? CLAUDE.SPARK : RULE}`,
  padding: '9px 16px', display: 'inline-block', whiteSpace: 'nowrap',
  backgroundColor: hot ? '#FFFFFF' : 'transparent',
});

/** Placeholder answer lines — never real text. */
export const AnswerLines: React.FC<{w: number; n?: number; g: number}> = ({w, n = 3, g}) => (
  <div style={{display: 'flex', flexDirection: 'column', gap: 22}}>
    {Array.from({length: n}).map((_, i) => (
      <div key={i} style={{width: w * (i === n - 1 ? 0.6 : 1) * g, height: 14, borderRadius: 7, backgroundColor: CLAUDE.INK, opacity: 0.2}} />
    ))}
  </div>
);

/* ═══════════════════════════════════════════════════════════════════════════
   B01 — CtrBluf: the old assumption, struck through and replaced.

   EXECUTIVE-SUMMARY LAW. The assumption stays readable under its strike (never faded
   below the legibility floor) because the beat is about it being REPLACED, not erased.
   ═══════════════════════════════════════════════════════════════════════════ */
export type BlufData = {
  slideMeta: string;
  /** the whole old sentence; must contain `struck` */
  old: string;
  struck: string;
  replacement: string;
  closer: string;
};

export const CtrBluf: React.FC<{data: BlufData}> = ({data}) => {
  const p = useP();
  const i = data.old.indexOf(data.struck);
  const head = i >= 0 ? data.old.slice(0, i) : data.old;
  const tail = i >= 0 ? data.old.slice(i + data.struck.length) : '';
  const set = win(p, 0.06, 0.2);
  const strike = win(p, 0.4, 0.52);

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.y + 210, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 116, lineHeight: 1.1, color: CLAUDE.INK,
          opacity: set * (1 - 0.35 * strike),
        }}
      >
        {head}
        <span style={{position: 'relative', display: 'inline-block'}}>
          {data.struck}
          <span
            style={{
              position: 'absolute', left: 0, top: '56%', height: 9,
              width: `${strike * 100}%`, backgroundColor: CLAUDE.SPARK,
            }}
          />
        </span>
        {tail}
      </div>
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.y + 440, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 116, lineHeight: 1.1, color: CLAUDE.INK,
          opacity: win(p, 0.52, 0.58),
        }}
      >
        {head}
        <span style={{color: CLAUDE.SPARK}}>{typed(data.replacement, win(p, 0.56, 0.74))}</span>
      </div>
      <NoteLine note={data.closer} opacity={win(p, 0.86, 0.97)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B02 — CtrUse: two cohorts, two bars.

   REQUIRES a `source`. The two figures are NOT a comparison of two studies — they are
   one finding and its subgroup, from the same source, so they share one citation. The
   subgroup takes the accent. Unfilled track is never labelled.
   ═══════════════════════════════════════════════════════════════════════════ */
export type UseRow = {label: string; value: string; bar: number; hot: boolean};
export type UseData = {
  slideMeta: string;
  title: string;
  rows: UseRow[];
  note: string;
  /** REQUIRED */
  source: string;
};

export const CtrUse: React.FC<{data: UseData}> = ({data}) => {
  const p = useP();
  const TRACK_X = SAFE.x + 600;
  const TRACK_W = SAFE.w - 600 - 300;
  const TOP = SAFE.y + 300;
  const STEP = 300;

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.rows.map((r, i) => {
        const at = 0.08 + i * 0.44;
        const fill = win(p, at + 0.04, at + 0.22);
        const y = TOP + i * STEP;
        const color = r.hot ? CLAUDE.SPARK : CLAUDE.INK;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: SAFE.x, top: y + 4, width: 560, fontFamily: CLAUDE_FONT.serif, fontSize: 56, lineHeight: 1.1, color: CLAUDE.INK, opacity: win(p, at, at + 0.1)}}>
              {r.label}
            </div>
            <div style={{position: 'absolute', left: TRACK_X, top: y, width: TRACK_W, height: 86, border: `1px solid ${RULE}`, boxSizing: 'border-box', opacity: win(p, at, at + 0.08)}} />
            <div style={{position: 'absolute', left: TRACK_X + 1, top: y + 1, width: (TRACK_W - 2) * (r.bar / 100) * fill, height: 84, backgroundColor: color, opacity: 0.88}} />
            <div style={{position: 'absolute', left: TRACK_X + TRACK_W + 40, top: y - 24, width: 260, fontFamily: CLAUDE_FONT.serif, fontSize: 124, lineHeight: 1, color, opacity: win(p, at + 0.12, at + 0.24)}}>
              {r.value}
            </div>
          </React.Fragment>
        );
      })}
      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} />
      <NoteLine note={data.note} opacity={win(p, 0.88, 0.98)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B03 — CtrContradict: two answers that don't match.

   REQUIRES `source` AND `caption`. The bubbles carry placeholder lines only — the survey
   reports THAT a contradiction happened, not what was said, so no exchange is invented.
   ═══════════════════════════════════════════════════════════════════════════ */
export type ContradictData = {
  slideMeta: string;
  left: string;
  right: string;
  value: string;
  label: string;
  /** REQUIRED — the answers are placeholders */
  caption: string;
  /** REQUIRED */
  source: string;
};

export const Bubble: React.FC<{x: number; y: number; w: number; h: number; label: string; g: number; dashed?: boolean}> =
({x, y, w, h, label, g, dashed}) => (
  <div
    style={{
      position: 'absolute', left: x, top: y, width: w, height: h, boxSizing: 'border-box',
      padding: '34px 40px', borderRadius: 26, backgroundColor: CLAUDE.CARD,
      border: `2px ${dashed ? 'dashed' : 'solid'} ${CLAUDE.INK}`,
      opacity: g, transform: `translateY(${(1 - g) * 16}px)`,
    }}
  >
    <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 30, fontWeight: 600, color: CLAUDE.INK, marginBottom: 30}}>{label}</div>
    <AnswerLines w={w - 80} g={g} />
  </div>
);

export const CtrContradict: React.FC<{data: ContradictData}> = ({data}) => {
  const p = useP();
  const BW = 760;
  const BY = SAFE.y + 100;
  const BH = 290;
  const neq = win(p, 0.42, 0.52);

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />
      <Bubble x={SAFE.x} y={BY} w={BW} h={BH} label={data.left} g={win(p, 0.06, 0.2)} />
      <Bubble x={SAFE.r - BW} y={BY} w={BW} h={BH} label={data.right} g={win(p, 0.24, 0.38)} dashed />
      <div
        style={{
          position: 'absolute', left: CANVAS.w / 2 - 100, top: BY + BH / 2 - 100, width: 200, textAlign: 'center',
          fontFamily: CLAUDE_FONT.serif, fontSize: 170, lineHeight: 1, color: CLAUDE.SPARK,
          opacity: neq, transform: `scale(${1.3 - 0.3 * neq})`,
        }}
      >
        ≠
      </div>
      <div style={{position: 'absolute', left: SAFE.x, top: SAFE.y + 460, width: 520, fontFamily: CLAUDE_FONT.serif, fontSize: 200, lineHeight: 1, color: CLAUDE.INK, opacity: win(p, 0.56, 0.7)}}>
        {data.value}
      </div>
      <div style={{position: 'absolute', left: SAFE.x + 540, top: SAFE.y + 500, width: SAFE.w - 540, fontFamily: CLAUDE_FONT.ui, fontSize: 40, lineHeight: 1.3, color: CLAUDE.INK, opacity: win(p, 0.62, 0.76)}}>
        {data.label}
      </div>
      <Caption text={data.caption} opacity={win(p, 0.8, 0.9)} top={SAFE.b - 120} />
      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} top={SAFE.b - 80} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B05 — CtrScale: the scale that doesn't tip.

   The ask→result pair's RESULT. There is deliberately NO numeric prop on this type: the
   finding is "equally likely", supplied without a figure, so the beam settles LEVEL and
   no percentage is ever printed. The beam rotates (it is an SVG line, not pixel art);
   the pans stay vertical because they hang from the rotated endpoints.
   ═══════════════════════════════════════════════════════════════════════════ */
export type ScaleData = {
  slideMeta: string;
  left: string;
  right: string;
  verdict: string;
  note: string;
  /** REQUIRED */
  source: string;
};

export const ScaleSvg: React.FC<{
  cx: number; pivotY: number; half: number; hang: number; baseY: number;
  angle: number; draw: number; level: number; dish: number;
}> = ({cx, pivotY, half, hang, baseY, angle, draw, level, dish}) => {
  const a = (angle * Math.PI) / 180;
  const lx = cx - half * Math.cos(a);
  const ly = pivotY - half * Math.sin(a);
  const rx = cx + half * Math.cos(a);
  const ry = pivotY + half * Math.sin(a);
  const pan = (x: number, y: number) => (
    <g>
      <line x1={x} y1={y} x2={x - dish / 2 + 20} y2={y + hang} stroke={CLAUDE.INK} strokeWidth={3} />
      <line x1={x} y1={y} x2={x + dish / 2 - 20} y2={y + hang} stroke={CLAUDE.INK} strokeWidth={3} />
      <path d={`M ${x - dish / 2} ${y + hang} Q ${x} ${y + hang + 70} ${x + dish / 2} ${y + hang} Z`} fill={CLAUDE.CARD} stroke={CLAUDE.INK} strokeWidth={4} />
    </g>
  );
  return (
    <svg width={CANVAS.w * 2} height={CANVAS.h * 2} style={{position: 'absolute', left: 0, top: 0, overflow: 'visible', opacity: draw}}>
      <line x1={cx} y1={pivotY} x2={cx} y2={baseY} stroke={CLAUDE.INK} strokeWidth={10} />
      <path d={`M ${cx - 150} ${baseY + 30} L ${cx - 60} ${baseY} L ${cx + 60} ${baseY} L ${cx + 150} ${baseY + 30} Z`} fill={CLAUDE.INK} />
      <line x1={lx} y1={ly} x2={rx} y2={ry} stroke={CLAUDE.INK} strokeWidth={10} strokeLinecap="round" />
      {pan(lx, ly)}
      {pan(rx, ry)}
      <circle cx={cx} cy={pivotY} r={22} fill={level > 0.5 ? CLAUDE.SPARK : CLAUDE.INK} />
    </svg>
  );
};

export const CtrScale: React.FC<{data: ScaleData}> = ({data}) => {
  const p = useP();
  const CX = CANVAS.w / 2;
  const PIVOT = SAFE.y + 200;
  const HALF = 560;
  const HANG = 190;
  const angle = beamAngle(Math.max(0, p - 0.26) / 0.74, 0.4);
  const level = win(p, 0.56, 0.62);
  const a = (angle * Math.PI) / 180;
  const labelY = (y: number) => y + HANG + 66;

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />
      <ScaleSvg cx={CX} pivotY={PIVOT} half={HALF} hang={HANG} baseY={SAFE.y + 600} angle={angle} draw={win(p, 0.04, 0.16)} level={level} dish={380} />
      {[
        {t: data.left, x: CX - HALF * Math.cos(a), y: PIVOT - HALF * Math.sin(a), at: 0.12},
        {t: data.right, x: CX + HALF * Math.cos(a), y: PIVOT + HALF * Math.sin(a), at: 0.2},
      ].map((l, i) => (
        <div key={i} style={{position: 'absolute', left: l.x - 240, top: labelY(l.y), width: 480, textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: 52, color: CLAUDE.INK, opacity: win(p, l.at, l.at + 0.1)}}>
          {l.t}
        </div>
      ))}
      <div style={{position: 'absolute', left: SAFE.x, top: SAFE.y + 676, width: SAFE.w, textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: 72, color: CLAUDE.SPARK, opacity: win(p, 0.66, 0.78)}}>
        {data.verdict}
      </div>
      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} />
      <NoteLine note={data.note} opacity={win(p, 0.88, 0.98)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B06 — CtrTiebreak: the final word becomes one answer of two.

   Interpretation, not data — so `note` is REQUIRED and says so on screen. No numeric
   prop. The two NOW blocks are drawn the same size on purpose: "same weight".
   ═══════════════════════════════════════════════════════════════════════════ */
export type TiebreakData = {
  slideMeta: string;
  beforeHead: string;
  afterHead: string;
  brand: string;
  ai: string;
  beforeLabel: string;
  afterLabel: string;
  /** REQUIRED — this beat is a reading of the finding */
  note: string;
};

export const Block: React.FC<{x: number; y: number; w: number; h: number; label: string; g: number; hot?: boolean}> =
({x, y, w, h, label, g, hot}) => (
  <div
    style={{
      position: 'absolute', left: x, top: y, width: w, height: h, boxSizing: 'border-box',
      display: 'flex', alignItems: 'center', justifyContent: 'center', textAlign: 'center', padding: 20,
      borderRadius: 16, backgroundColor: CLAUDE.CARD,
      border: hot ? `3px dashed ${CLAUDE.SPARK}` : `2px solid ${CLAUDE.INK}`,
      fontFamily: CLAUDE_FONT.serif, fontSize: 46, lineHeight: 1.12, color: CLAUDE.INK, opacity: g,
    }}
  >
    {label}
  </div>
);

export const CtrTiebreak: React.FC<{data: TiebreakData}> = ({data}) => {
  const p = useP();
  const PW = 800;
  const LX = SAFE.x;
  const RX = SAFE.r - PW;
  const TOP = SAFE.y + 90;
  const BY = TOP + 250;
  const slide = win(p, 0.42, 0.58);
  const relabel = win(p, 0.64, 0.74);

  const panel = (x: number, head: string, g: number) => (
    <>
      <div style={{position: 'absolute', left: x, top: TOP, width: PW, height: 620, borderRadius: 20, border: `1px solid ${RULE}`, opacity: g}} />
      <div style={{position: 'absolute', left: x + 40, top: TOP + 32, fontFamily: CLAUDE_FONT.ui, fontSize: 28, letterSpacing: '.18em', fontWeight: 600, color: MUTE, opacity: g}}>
        {head.toUpperCase()}
      </div>
    </>
  );

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />
      {panel(LX, data.beforeHead, win(p, 0.04, 0.14))}
      {panel(RX, data.afterHead, win(p, 0.36, 0.44))}

      {/* before: one answer, crowned */}
      <div style={{position: 'absolute', left: LX + 140, top: TOP + 120, ...chipStyle(false, 28), color: CLAUDE.INK, border: `2px solid ${CLAUDE.INK}`, opacity: win(p, 0.14, 0.24)}}>
        {data.beforeLabel}
      </div>
      <Block x={LX + 140} y={BY} w={520} h={240} label={data.brand} g={win(p, 0.08, 0.2)} />

      {/* now: two answers, equal size */}
      <div style={{position: 'absolute', left: RX + 40, top: TOP + 120, ...chipStyle(true, 28), opacity: relabel}}>
        {data.afterLabel}
      </div>
      <Block x={RX + 40} y={BY} w={340} h={240} label={data.brand} g={win(p, 0.4, 0.5)} />
      <Block x={RX + 420 + (1 - slide) * 260} y={BY} w={340} h={240} label={data.ai} g={slide} hot />

      <Caption text={data.note} opacity={win(p, 0.84, 0.94)} top={SAFE.b - 80} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B07 — CtrSharpen: a broad question narrows into a specific one.

   REQUIRES `source` AND `caption` — the bubble holds placeholder lines, no invented
   question text. The morph is the claim: wide and soft → narrow and crisp.
   ═══════════════════════════════════════════════════════════════════════════ */
export type SharpenData = {
  slideMeta: string;
  value: string;
  label: string;
  vague: string;
  specific: string;
  /** REQUIRED */
  caption: string;
  /** REQUIRED */
  source: string;
};

export const SharpBubble: React.FC<{cx: number; cy: number; s: number; g: number; wide: number; narrow: number}> =
({cx, cy, s, g, wide, narrow}) => {
  const w = wide + (narrow - wide) * s;
  const h = 300 - 120 * s;
  return (
    <div
      style={{
        position: 'absolute', left: cx - w / 2, top: cy - h / 2, width: w, height: h, boxSizing: 'border-box',
        borderRadius: 150 - 126 * s, backgroundColor: CLAUDE.CARD,
        border: `${2 + 2 * s}px ${s < 0.5 ? 'dashed' : 'solid'} ${s < 0.5 ? CLAUDE.INK_SOFT : CLAUDE.INK}`,
        display: 'flex', flexDirection: 'column', justifyContent: 'center', gap: 20 - 6 * s, padding: '0 50px',
        opacity: g,
      }}
    >
      {[1, 0.8, 0.55].map((f, i) => (
        <div key={i} style={{width: `${f * 100}%`, height: 14, borderRadius: 7, backgroundColor: CLAUDE.INK, opacity: (0.12 + 0.18 * s) * (i < 3 - s ? 1 : 0)}} />
      ))}
    </div>
  );
};

export const CtrSharpen: React.FC<{data: SharpenData}> = ({data}) => {
  const p = useP();
  const s = win(p, 0.3, 0.5);
  const CX = SAFE.x + 480;
  const CY = SAFE.y + 370;

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />
      <SharpBubble cx={CX} cy={CY} s={s} g={win(p, 0.06, 0.18)} wide={900} narrow={640} />
      <div style={{position: 'absolute', left: CX - 450, top: CY + 190, width: 900, textAlign: 'center', fontFamily: CLAUDE_FONT.ui, fontSize: 34, color: MUTE, opacity: win(p, 0.1, 0.2) * (1 - s)}}>
        {data.vague}
      </div>
      <div style={{position: 'absolute', left: CX - 450, top: CY + 190, width: 900, textAlign: 'center', fontFamily: CLAUDE_FONT.ui, fontSize: 34, fontWeight: 600, color: CLAUDE.SPARK, opacity: s}}>
        {data.specific}
      </div>
      <div style={{position: 'absolute', left: SAFE.x + 1060, top: SAFE.y + 170, width: 668, fontFamily: CLAUDE_FONT.serif, fontSize: 220, lineHeight: 1, color: CLAUDE.INK, opacity: win(p, 0.54, 0.66)}}>
        {data.value}
      </div>
      <div style={{position: 'absolute', left: SAFE.x + 1060, top: SAFE.y + 420, width: 668, fontFamily: CLAUDE_FONT.ui, fontSize: 40, lineHeight: 1.3, color: CLAUDE.INK, opacity: win(p, 0.6, 0.74)}}>
        {data.label}
      </div>
      <Caption text={data.caption} opacity={win(p, 0.8, 0.9)} top={SAFE.b - 120} />
      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} top={SAFE.b - 80} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B08 — CtrCall: the customer's AI connects the call, then stays on it.

   REQUIRES a `source`. Two steps, in narration order: the agent CONNECTS customer and
   rep (ink), then JOINS the shared line itself (the accent).
   ═══════════════════════════════════════════════════════════════════════════ */
export type CallData = {
  slideMeta: string;
  customer: string;
  agent: string;
  rep: string;
  /** [connect label, join label] */
  steps: string[];
  value: string;
  label: string;
  /** REQUIRED */
  source: string;
};

export const Person: React.FC<{cx: number; cy: number; r: number; g: number}> = ({cx, cy, r, g}) => (
  <svg width={CANVAS.w * 2} height={CANVAS.h * 2} style={{position: 'absolute', left: 0, top: 0, overflow: 'visible', opacity: g}}>
    <circle cx={cx} cy={cy} r={r} fill={CLAUDE.CARD} stroke={CLAUDE.INK} strokeWidth={3} />
    {/* filled head-and-shoulders silhouette — neutral, never a face */}
    <circle cx={cx} cy={cy - r * 0.24} r={r * 0.27} fill={CLAUDE.INK} opacity={0.7} />
    <path d={`M ${cx - r * 0.56} ${cy + r * 0.62} Q ${cx - r * 0.56} ${cy + r * 0.1} ${cx} ${cy + r * 0.1} Q ${cx + r * 0.56} ${cy + r * 0.1} ${cx + r * 0.56} ${cy + r * 0.62} Z`} fill={CLAUDE.INK} opacity={0.7} />
  </svg>
);

export const Agent: React.FC<{cx: number; cy: number; r: number; g: number; hot: number}> = ({cx, cy, r, g, hot}) => (
  <svg width={CANVAS.w * 2} height={CANVAS.h * 2} style={{position: 'absolute', left: 0, top: 0, overflow: 'visible', opacity: g}}>
    <rect x={cx - r} y={cy - r} width={r * 2} height={r * 2} rx={r * 0.3} fill={CLAUDE.CARD} stroke={hot > 0.5 ? CLAUDE.SPARK : CLAUDE.INK} strokeWidth={hot > 0.5 ? 5 : 3} />
    <circle cx={cx - r * 0.32} cy={cy - r * 0.1} r={r * 0.12} fill={CLAUDE.INK} opacity={0.7} />
    <circle cx={cx + r * 0.32} cy={cy - r * 0.1} r={r * 0.12} fill={CLAUDE.INK} opacity={0.7} />
    <rect x={cx - r * 0.4} y={cy + r * 0.3} width={r * 0.8} height={r * 0.12} rx={r * 0.06} fill={CLAUDE.INK} opacity={0.7} />
  </svg>
);

export const CtrCall: React.FC<{data: CallData}> = ({data}) => {
  const p = useP();
  const R = 78;
  const NY = SAFE.y + 210;
  const CUST = SAFE.x + 220;
  const REP = SAFE.r - 220;
  const AG = CANVAS.w / 2;
  const LINE_Y = SAFE.y + 470;
  const connect = win(p, 0.24, 0.4);
  const join = win(p, 0.46, 0.6);

  const label = (x: number, t: string, at: number) => (
    <div style={{position: 'absolute', left: x - 220, top: NY + R + 18, width: 440, textAlign: 'center', fontFamily: CLAUDE_FONT.ui, fontSize: 32, color: CLAUDE.INK, opacity: win(p, at, at + 0.1)}}>{t}</div>
  );

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />
      <svg width={CANVAS.w} height={CANVAS.h} style={{position: 'absolute', left: 0, top: 0}}>
        {/* the agent places the call */}
        <path d={`M ${AG + R} ${NY} Q ${(AG + REP) / 2} ${NY - 90} ${REP - R} ${NY}`} fill="none" stroke={CLAUDE.INK} strokeWidth={3} strokeDasharray="10 10" opacity={0.7 * connect} />
        {/* the shared line, and the two humans on it */}
        <line x1={CUST} y1={LINE_Y} x2={CUST + (REP - CUST) * connect} y2={LINE_Y} stroke={CLAUDE.INK} strokeWidth={6} />
        <line x1={CUST} y1={NY + R + 70} x2={CUST} y2={NY + R + 70 + (LINE_Y - NY - R - 70) * connect} stroke={CLAUDE.INK} strokeWidth={4} />
        <line x1={REP} y1={NY + R + 70} x2={REP} y2={NY + R + 70 + (LINE_Y - NY - R - 70) * connect} stroke={CLAUDE.INK} strokeWidth={4} />
        {/* and the agent joins it */}
        <line x1={AG} y1={NY + R + 70} x2={AG} y2={NY + R + 70 + (LINE_Y - NY - R - 70) * join} stroke={CLAUDE.SPARK} strokeWidth={6} />
        <circle cx={AG} cy={LINE_Y} r={14 * win(p, 0.56, 0.62)} fill={CLAUDE.SPARK} />
      </svg>
      <div style={{position: 'absolute', left: (AG + REP) / 2 - 200, top: NY - 150, width: 400, textAlign: 'center', fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: CLAUDE.INK, opacity: connect}}>{data.steps[0]}</div>
      <div style={{position: 'absolute', left: AG + 26, top: LINE_Y - 64, fontFamily: CLAUDE_FONT.ui, fontSize: 30, fontWeight: 600, color: CLAUDE.SPARK, opacity: win(p, 0.56, 0.66)}}>{data.steps[1]}</div>

      <Person cx={CUST} cy={NY} r={R} g={win(p, 0.06, 0.16)} />
      <Agent cx={AG} cy={NY} r={R} g={win(p, 0.1, 0.2)} hot={join} />
      <Person cx={REP} cy={NY} r={R} g={win(p, 0.14, 0.24)} />
      {label(CUST, data.customer, 0.06)}
      {label(AG, data.agent, 0.1)}
      {label(REP, data.rep, 0.14)}

      <div style={{position: 'absolute', left: SAFE.x, top: SAFE.y + 540, width: 460, fontFamily: CLAUDE_FONT.serif, fontSize: 190, lineHeight: 1, color: CLAUDE.INK, opacity: win(p, 0.64, 0.76)}}>
        {data.value}
      </div>
      <div style={{position: 'absolute', left: SAFE.x + 480, top: SAFE.y + 580, width: SAFE.w - 480, fontFamily: CLAUDE_FONT.ui, fontSize: 38, lineHeight: 1.3, color: CLAUDE.INK, opacity: win(p, 0.7, 0.82)}}>
        {data.label}
      </div>
      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} top={SAFE.b - 80} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B09 — CtrLimits: what consumers reported, and what the survey doesn't say.

   The FALSIFIABILITY beat. `provenance` and `falsifier` REQUIRED. The falsifier names the
   reel's own interpretive claim ("companies haven't caught up") as interpretation.
   ═══════════════════════════════════════════════════════════════════════════ */
export type LimitsData = {
  slideMeta: string;
  title: string;
  found: {heading: string; items: string[]};
  notFound: {heading: string; items: string[]};
  /** REQUIRED */
  provenance: string;
  /** REQUIRED */
  falsifier: string;
};

export const Marker: React.FC<{hot?: boolean; size: number}> = ({hot, size}) => (
  <div
    style={{
      width: size, height: size, flexShrink: 0, borderRadius: size / 2, boxSizing: 'border-box',
      border: `3px solid ${hot ? CLAUDE.SPARK : CLAUDE.INK}`,
      backgroundColor: hot ? 'transparent' : CLAUDE.INK,
      display: 'flex', alignItems: 'center', justifyContent: 'center',
      fontFamily: CLAUDE_FONT.serif, fontSize: size * 0.7, lineHeight: 1, color: CLAUDE.SPARK,
    }}
  >
    {hot ? '?' : ''}
  </div>
);

export const CtrLimits: React.FC<{data: LimitsData}> = ({data}) => {
  const p = useP();
  const COL_W = 820;
  const HEAD_Y = SAFE.y + 226;
  const ITEM_Y = SAFE.y + 296;
  const STEP = 104;

  const col = (x: number, h: {heading: string; items: string[]}, at: number, hot: boolean) => (
    <>
      <div style={{position: 'absolute', left: x, top: HEAD_Y, width: COL_W, fontFamily: CLAUDE_FONT.ui, fontSize: 28, letterSpacing: '.16em', fontWeight: 600, color: hot ? CLAUDE.SPARK : MUTE, opacity: win(p, at, at + 0.08)}}>
        {h.heading.toUpperCase()}
      </div>
      {h.items.map((it, i) => {
        const g = win(p, at + 0.04 + i * 0.07, at + 0.14 + i * 0.07);
        return (
          <div key={i} style={{position: 'absolute', left: x, top: ITEM_Y + i * STEP, width: COL_W, display: 'flex', alignItems: 'center', gap: 24, opacity: g, transform: `translateX(${(1 - g) * -14}px)`}}>
            <Marker hot={hot} size={hot ? 44 : 20} />
            <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 35, lineHeight: 1.25, color: CLAUDE.INK}}>{it}</div>
          </div>
        );
      })}
    </>
  );

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {col(SAFE.x, data.found, 0.06, false)}
      {col(SAFE.x + 908, data.notFound, 0.44, true)}
      <div style={{position: 'absolute', left: SAFE.x, top: SAFE.b - 150, width: SAFE.w * win(p, 0.76, 0.86), height: 1, backgroundColor: RULE}} />
      <div style={{position: 'absolute', left: SAFE.x, top: SAFE.b - 130, width: SAFE.w, fontFamily: CLAUDE_FONT.ui, fontSize: 25, color: MUTE, opacity: win(p, 0.78, 0.88)}}>
        {data.provenance}
      </div>
      <NoteLine note={data.falsifier} opacity={win(p, 0.88, 0.97)} />
    </PlainStage>
  );
};
