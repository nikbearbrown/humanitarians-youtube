/**
 * CustomerTrust916.tsx — PORTRAIT (9:16) scenes for `yatra-no-default-winner`.
 *
 * Re-banded vertically, NOT scaled clones:
 *
 *   · CtrBluf916       — the struck sentence and its replacement wrap to the column.
 *   · CtrUse916        — label above each bar; figure beside the bar's end.
 *   · CtrContradict916 — the two answer bubbles STACK with the ≠ between them.
 *   · CtrScale916      — a narrower beam; pans and labels fit the 906px column.
 *   · CtrTiebreak916   — BEFORE above NOW instead of side by side.
 *   · CtrCall916       — the three parties stack down the left, the shared line runs
 *                        vertically beside them.
 *
 * Types are imported from CustomerTrust.tsx, so every refusal holds: `source` still
 * required, `value` still verbatim with a separate `bar`, CtrScale916 still has no
 * numeric prop, captions and the interpretation note still required.
 *
 * KEEP-OUT: content above y≈1440 and left of x≈960; brand bug lower-left.
 */
import React from 'react';
import {AbsoluteFill} from 'remotion';
import {SAFE916} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {useP, typed, beamAngle, chipStyle, Bubble, ScaleSvg, Block, SharpBubble, Person, Agent, Marker} from './CustomerTrust';
import type {
  BlufData, UseData, ContradictData, ScaleData, TiebreakData, SharpenData, CallData, LimitsData,
} from './CustomerTrust';

const STAGE = '#F2F0E9';
const RULE = '#D8D4C8';
const MUTE = '#7A7265';
const BOX = {x: SAFE916.x, y: SAFE916.y, w: 906, bottom: 1440} as const;
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

const Small: React.FC<{text: string; opacity: number; top: number}> = ({text, opacity, top}) => (
  <div style={{position: 'absolute', left: BOX.x, top, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 25, lineHeight: 1.3, color: MUTE, opacity}}>
    {text}
  </div>
);

/* ── B01 ── */
export const CtrBluf916: React.FC<{data: BlufData}> = ({data}) => {
  const p = useP();
  const i = data.old.indexOf(data.struck);
  const head = i >= 0 ? data.old.slice(0, i) : data.old;
  const tail = i >= 0 ? data.old.slice(i + data.struck.length) : '';
  const strike = win(p, 0.4, 0.52);
  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 180, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 104, lineHeight: 1.12, color: CLAUDE.INK, opacity: win(p, 0.06, 0.2) * (1 - 0.35 * strike)}}>
        {head}
        <span style={{position: 'relative', display: 'inline-block'}}>
          {data.struck}
          <span style={{position: 'absolute', left: 0, top: '56%', height: 8, width: `${strike * 100}%`, backgroundColor: CLAUDE.SPARK}} />
        </span>
        {tail}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 560, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 104, lineHeight: 1.12, color: CLAUDE.INK, opacity: win(p, 0.52, 0.58)}}>
        {head}
        <span style={{color: CLAUDE.SPARK}}>{typed(data.replacement, win(p, 0.56, 0.74))}</span>
      </div>
      <Note note={data.closer} opacity={win(p, 0.86, 0.97)} />
    </Stage>
  );
};

/* ── B02 — label above each bar ── */
export const CtrUse916: React.FC<{data: UseData}> = ({data}) => {
  const p = useP();
  const TRACK_W = BOX.w - 260;
  const TOP = BOX.y + 300;
  const STEP = 340;
  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.rows.map((r, i) => {
        const at = 0.08 + i * 0.44;
        const fill = win(p, at + 0.04, at + 0.22);
        const y = TOP + i * STEP;
        const color = r.hot ? CLAUDE.SPARK : CLAUDE.INK;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 56, color: CLAUDE.INK, opacity: win(p, at, at + 0.1)}}>{r.label}</div>
            <div style={{position: 'absolute', left: BOX.x, top: y + 100, width: TRACK_W, height: 90, border: `1px solid ${RULE}`, boxSizing: 'border-box', opacity: win(p, at, at + 0.08)}} />
            <div style={{position: 'absolute', left: BOX.x + 1, top: y + 101, width: (TRACK_W - 2) * (r.bar / 100) * fill, height: 88, backgroundColor: color, opacity: 0.88}} />
            <div style={{position: 'absolute', left: BOX.x + TRACK_W + 24, top: y + 84, width: 236, fontFamily: CLAUDE_FONT.serif, fontSize: 108, lineHeight: 1, color, opacity: win(p, at + 0.12, at + 0.24)}}>{r.value}</div>
          </React.Fragment>
        );
      })}
      <Small text={`Source: ${data.source}`} opacity={win(p, 0.84, 0.94)} top={BOX.bottom - 166} />
      <Note note={data.note} opacity={win(p, 0.88, 0.98)} />
    </Stage>
  );
};

/* ── B03 — the answers stack, ≠ between ── */
export const CtrContradict916: React.FC<{data: ContradictData}> = ({data}) => {
  const p = useP();
  const BH = 250;
  const neq = win(p, 0.42, 0.52);
  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />
      <Bubble x={BOX.x} y={BOX.y + 80} w={BOX.w} h={BH} label={data.left} g={win(p, 0.06, 0.2)} />
      <div style={{position: 'absolute', left: MID - 100, top: BOX.y + 80 + BH + 10, width: 200, textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: 140, lineHeight: 1, color: CLAUDE.SPARK, opacity: neq}}>≠</div>
      <Bubble x={BOX.x} y={BOX.y + 80 + BH + 170} w={BOX.w} h={BH} label={data.right} g={win(p, 0.24, 0.38)} dashed />
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 790, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 180, lineHeight: 1, color: CLAUDE.INK, opacity: win(p, 0.56, 0.7)}}>{data.value}</div>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 990, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 36, lineHeight: 1.3, color: CLAUDE.INK, opacity: win(p, 0.62, 0.76)}}>{data.label}</div>
      <Small text={data.caption} opacity={win(p, 0.8, 0.9)} top={BOX.bottom - 104} />
      <Small text={`Source: ${data.source}`} opacity={win(p, 0.84, 0.94)} top={BOX.bottom - 64} />
    </Stage>
  );
};

/* ── B05 — narrower scale ── */
export const CtrScale916: React.FC<{data: ScaleData}> = ({data}) => {
  const p = useP();
  const PIVOT = BOX.y + 260;
  const HALF = 320;
  const HANG = 190;
  const angle = beamAngle(Math.max(0, p - 0.26) / 0.74, 0.4);
  const a = (angle * Math.PI) / 180;
  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />
      <ScaleSvg cx={MID} pivotY={PIVOT} half={HALF} hang={HANG} baseY={BOX.y + 700} angle={angle} draw={win(p, 0.04, 0.16)} level={win(p, 0.56, 0.62)} dish={260} />
      {[
        {t: data.left, x: MID - HALF * Math.cos(a), y: PIVOT - HALF * Math.sin(a), at: 0.12},
        {t: data.right, x: MID + HALF * Math.cos(a), y: PIVOT + HALF * Math.sin(a), at: 0.2},
      ].map((l, i) => (
        <div key={i} style={{position: 'absolute', left: l.x - 150, top: l.y + HANG + 60, width: 300, textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: 44, lineHeight: 1.1, color: CLAUDE.INK, opacity: win(p, l.at, l.at + 0.1)}}>{l.t}</div>
      ))}
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 800, width: BOX.w, textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: 72, lineHeight: 1.12, color: CLAUDE.SPARK, opacity: win(p, 0.66, 0.78)}}>{data.verdict}</div>
      <Small text={`Source: ${data.source}`} opacity={win(p, 0.84, 0.94)} top={BOX.bottom - 166} />
      <Note note={data.note} opacity={win(p, 0.88, 0.98)} />
    </Stage>
  );
};

/* ── B06 — BEFORE above NOW ── */
export const CtrTiebreak916: React.FC<{data: TiebreakData}> = ({data}) => {
  const p = useP();
  const PH = 520;
  const T1 = BOX.y + 80;
  const T2 = T1 + PH + 50;
  const slide = win(p, 0.42, 0.58);
  const panel = (y: number, head: string, g: number) => (
    <>
      <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w, height: PH, borderRadius: 20, border: `1px solid ${RULE}`, opacity: g}} />
      <div style={{position: 'absolute', left: BOX.x + 36, top: y + 30, fontFamily: CLAUDE_FONT.ui, fontSize: 28, letterSpacing: '.18em', fontWeight: 600, color: MUTE, opacity: g}}>{head.toUpperCase()}</div>
    </>
  );
  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />
      {panel(T1, data.beforeHead, win(p, 0.04, 0.14))}
      <div style={{position: 'absolute', left: BOX.x + 36, top: T1 + 100, ...chipStyle(false, 26), color: CLAUDE.INK, border: `2px solid ${CLAUDE.INK}`, opacity: win(p, 0.14, 0.24)}}>{data.beforeLabel}</div>
      <Block x={BOX.x + 36} y={T1 + 200} w={BOX.w - 72} h={270} label={data.brand} g={win(p, 0.08, 0.2)} />
      {panel(T2, data.afterHead, win(p, 0.36, 0.44))}
      <div style={{position: 'absolute', left: BOX.x + 36, top: T2 + 100, ...chipStyle(true, 26), opacity: win(p, 0.64, 0.74)}}>{data.afterLabel}</div>
      <Block x={BOX.x + 36} y={T2 + 200} w={400} h={270} label={data.brand} g={win(p, 0.4, 0.5)} />
      <Block x={BOX.x + 470 + (1 - slide) * 200} y={T2 + 200} w={400} h={270} label={data.ai} g={slide} hot />
      <Small text={data.note} opacity={win(p, 0.84, 0.94)} top={BOX.bottom - 64} />
    </Stage>
  );
};

/* ── B07 ── */
export const CtrSharpen916: React.FC<{data: SharpenData}> = ({data}) => {
  const p = useP();
  const s = win(p, 0.3, 0.5);
  const CY = BOX.y + 300;
  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />
      <SharpBubble cx={MID} cy={CY} s={s} g={win(p, 0.06, 0.18)} wide={BOX.w} narrow={560} />
      <div style={{position: 'absolute', left: BOX.x, top: CY + 180, width: BOX.w, textAlign: 'center', fontFamily: CLAUDE_FONT.ui, fontSize: 34, color: MUTE, opacity: win(p, 0.1, 0.2) * (1 - s)}}>{data.vague}</div>
      <div style={{position: 'absolute', left: BOX.x, top: CY + 180, width: BOX.w, textAlign: 'center', fontFamily: CLAUDE_FONT.ui, fontSize: 34, fontWeight: 600, color: CLAUDE.SPARK, opacity: s}}>{data.specific}</div>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 640, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 220, lineHeight: 1, color: CLAUDE.INK, opacity: win(p, 0.54, 0.66)}}>{data.value}</div>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 880, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 40, lineHeight: 1.3, color: CLAUDE.INK, opacity: win(p, 0.6, 0.74)}}>{data.label}</div>
      <Small text={data.caption} opacity={win(p, 0.8, 0.9)} top={BOX.bottom - 104} />
      <Small text={`Source: ${data.source}`} opacity={win(p, 0.84, 0.94)} top={BOX.bottom - 64} />
    </Stage>
  );
};

/* ── B08 — parties down the left, the shared line vertical beside them ── */
export const CtrCall916: React.FC<{data: CallData}> = ({data}) => {
  const p = useP();
  const R = 66;
  const NX = BOX.x + 90;
  const LINE_X = BOX.x + 560;
  const Y = [BOX.y + 140, BOX.y + 340, BOX.y + 540];
  const connect = win(p, 0.24, 0.4);
  const join = win(p, 0.46, 0.6);
  const lbl = (y: number, t: string, at: number) => (
    <div style={{position: 'absolute', left: NX + R + 26, top: y - 22, width: 320, fontFamily: CLAUDE_FONT.ui, fontSize: 32, color: CLAUDE.INK, opacity: win(p, at, at + 0.1)}}>{t}</div>
  );
  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />
      <svg width={1080} height={1920} style={{position: 'absolute', left: 0, top: 0}}>
        <path d={`M ${NX + R} ${Y[1]} Q ${NX + 260} ${(Y[1] + Y[2]) / 2} ${NX + R} ${Y[2]}`} fill="none" stroke={CLAUDE.INK} strokeWidth={3} strokeDasharray="10 10" opacity={0.7 * connect} />
        <line x1={LINE_X} y1={Y[0]} x2={LINE_X} y2={Y[0] + (Y[2] - Y[0]) * connect} stroke={CLAUDE.INK} strokeWidth={6} />
        <line x1={NX + 420} y1={Y[0]} x2={NX + 420 + (LINE_X - NX - 420) * connect} y2={Y[0]} stroke={CLAUDE.INK} strokeWidth={4} />
        <line x1={NX + 420} y1={Y[2]} x2={NX + 420 + (LINE_X - NX - 420) * connect} y2={Y[2]} stroke={CLAUDE.INK} strokeWidth={4} />
        <line x1={NX + 420} y1={Y[1]} x2={NX + 420 + (LINE_X - NX - 420) * join} y2={Y[1]} stroke={CLAUDE.SPARK} strokeWidth={6} />
        <circle cx={LINE_X} cy={Y[1]} r={14 * win(p, 0.56, 0.62)} fill={CLAUDE.SPARK} />
      </svg>
      <div style={{position: 'absolute', left: LINE_X + 30, top: (Y[1] + Y[2]) / 2 - 20, width: 300, fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: CLAUDE.INK, opacity: connect}}>{data.steps[0]}</div>
      <div style={{position: 'absolute', left: LINE_X + 30, top: Y[1] - 20, width: 300, fontFamily: CLAUDE_FONT.ui, fontSize: 30, fontWeight: 600, color: CLAUDE.SPARK, opacity: win(p, 0.56, 0.66)}}>{data.steps[1]}</div>
      <Person cx={NX} cy={Y[0]} r={R} g={win(p, 0.06, 0.16)} />
      <Agent cx={NX} cy={Y[1]} r={R} g={win(p, 0.1, 0.2)} hot={join} />
      <Person cx={NX} cy={Y[2]} r={R} g={win(p, 0.14, 0.24)} />
      {lbl(Y[0], data.customer, 0.06)}
      {lbl(Y[1], data.agent, 0.1)}
      {lbl(Y[2], data.rep, 0.14)}
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 700, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 200, lineHeight: 1, color: CLAUDE.INK, opacity: win(p, 0.64, 0.76)}}>{data.value}</div>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 920, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 38, lineHeight: 1.3, color: CLAUDE.INK, opacity: win(p, 0.7, 0.82)}}>{data.label}</div>
      <Small text={`Source: ${data.source}`} opacity={win(p, 0.84, 0.94)} top={BOX.bottom - 64} />
    </Stage>
  );
};

/* ── B09 — the two lists stack ── */
export const CtrLimits916: React.FC<{data: LimitsData}> = ({data}) => {
  const p = useP();
  const STEP = 84;
  const list = (top: number, h: {heading: string; items: string[]}, at: number, hot: boolean) => (
    <>
      <div style={{position: 'absolute', left: BOX.x, top, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 28, letterSpacing: '.16em', fontWeight: 600, color: hot ? CLAUDE.SPARK : MUTE, opacity: win(p, at, at + 0.08)}}>{h.heading.toUpperCase()}</div>
      {h.items.map((it, i) => (
        <div key={i} style={{position: 'absolute', left: BOX.x, top: top + 62 + i * STEP, width: BOX.w, display: 'flex', alignItems: 'center', gap: 22, opacity: win(p, at + 0.04 + i * 0.07, at + 0.14 + i * 0.07)}}>
          <Marker hot={hot} size={hot ? 40 : 18} />
          <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 33, lineHeight: 1.2, color: CLAUDE.INK}}>{it}</div>
        </div>
      ))}
    </>
  );
  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {list(BOX.y + 260, data.found, 0.06, false)}
      {list(BOX.y + 260 + 62 + data.found.items.length * STEP + 60, data.notFound, 0.44, true)}
      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 200, width: BOX.w * win(p, 0.76, 0.86), height: 1, backgroundColor: RULE}} />
      <Small text={data.provenance} opacity={win(p, 0.78, 0.88)} top={BOX.bottom - 182} />
      <Note note={data.falsifier} opacity={win(p, 0.88, 0.97)} />
    </Stage>
  );
};
