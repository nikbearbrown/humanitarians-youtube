import React from 'react';
import {AbsoluteFill} from 'remotion';
import {CLAUDE} from '../tokens/claude';
import {SAFE916} from '../tokens/layout';
import {ACCENT, Card, INK, SANS, SERIF, SOFT, STAGE, Spark, useBeat} from './SocialAiVisibility';
import {LogoBug} from './ContentRepurpose';
import {
  AtomSplitProps, Check, QualityGateProps, ReleaseRunwayProps, ReshapeNotCopyProps, TenFormatsProps, TenGlyph,
  atomFlight, gateState, litCount,
} from './OneIntoTen';

/**
 * OneIntoTen916.tsx — native 9:16 layouts for the OneIntoTen scenes.
 *
 * Registered as `<Name>916` with the same zod schemas. Portrait is re-composed
 * (one column, fewer words per frame) and type clears GATE T's portrait floor:
 * serif ≥ 92 and sans ≥ 78 CSS px. Long labels are shortened through the vertical
 * beat sheet's props, never by shrinking type.
 */

const S = SAFE916;
const SERIF_PX = 92;
const SANS_PX = 78;
const TOP = S.y + 260;
const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const ease = (t: number) => t * t * (3 - 2 * t);
const lerp = (a: number, b: number, t: number) => a + (b - a) * t;

const SparkLine916: React.FC<{text: string}> = ({text}) => (
  <div style={{position: 'absolute', left: S.x, top: S.y, width: S.w, height: 230, display: 'flex',
    alignItems: 'center', justifyContent: 'center', gap: 26}}>
    <Spark size={78} />
    <span style={{fontFamily: SERIF, fontSize: SERIF_PX, color: INK, fontWeight: 600, lineHeight: 1.05,
      textAlign: 'center', maxWidth: S.w - 110}}>{text}</span>
  </div>
);

const Text916: React.FC<{text: string; top: number; size?: number; font?: string; color?: string; weight?: number;
  italic?: boolean; align?: 'left' | 'center'; opacity?: number}> = (
  {text, top, size = SERIF_PX, font = SERIF, color = INK, weight = 400, italic = false, align = 'center', opacity = 1}) => (
  <div style={{position: 'absolute', left: S.x, width: S.w, top, fontFamily: font, fontSize: size, color, fontWeight: weight,
    fontStyle: italic ? 'italic' : 'normal', textAlign: align, lineHeight: 1.05, opacity}}>{text}</div>
);

const pad2 = (i: number) => String(i + 1).padStart(2, '0');

// ── B02 ──────────────────────────────────────────────────────────────────────
export const AtomSplit916: React.FC<AtomSplitProps> = (props) => {
  const {pop, ramp} = useBeat(props.durationSeconds);
  const card = {x: S.x, y: TOP, w: S.w, h: 380};
  const vIn = pop(props.videoAt);
  const split = ramp(props.splitAt, 0.06);
  const binW = (S.w - 24) / 2, binH = 380, binTop = card.y + card.h + 54, binGap = 24;
  const chipH = 110, chipGap = 16;
  const cellW = 190, cellH = 60, cellGx = 18, cellGy = 18;
  const gridX = card.x + (card.w - (4 * cellW + 3 * cellGx)) / 2, gridY = card.y + 124;
  let k = 0;
  const chips: {text: string; bin: number; j: number; x0: number; y0: number; x1: number; y1: number; w: number}[] = [];
  props.bins.forEach((b, i) => {
    const bx = S.x + (i % 2) * (binW + binGap), by = binTop + Math.floor(i / 2) * (binH + binGap);
    const n = b.chips.length;
    const w = (binW - 60 - (n - 1) * chipGap) / n;
    b.chips.forEach((text, j) => {
      chips.push({text, bin: i, j, w, x0: gridX + (k % 4) * (cellW + cellGx), y0: gridY + Math.floor(k / 4) * (cellH + cellGy),
        x1: bx + 30 + j * (w + chipGap), y1: by + 180});
      k++;
    });
  });
  const ringIn = pop(props.ringAt);
  const focus = chips.find((c) => c.bin === props.focusIndex && c.j === 0);
  const lineTop = binTop + 2 * binH + binGap + 40;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      <Card style={{position: 'absolute', left: card.x, top: card.y, width: card.w, height: card.h, boxSizing: 'border-box',
        opacity: vIn, border: split > 0 ? `4px dashed ${CLAUDE.GHOST}` : `2px solid ${CLAUDE.BORDER}`}}>
        <div style={{position: 'absolute', left: 0, right: 0, top: 22, textAlign: 'center', fontFamily: SERIF, fontSize: SERIF_PX,
          fontWeight: 700, color: INK, lineHeight: 1}}>{props.videoLabel}</div>
        <div style={{position: 'absolute', left: 0, right: 0, top: 140, display: 'flex', justifyContent: 'center',
          opacity: 1 - 0.8 * split}}>
          <TenGlyph kind="video" size={210} />
        </div>
      </Card>
      {props.bins.map((b, i) => {
        const bx = S.x + (i % 2) * (binW + binGap), by = binTop + Math.floor(i / 2) * (binH + binGap);
        const bIn = pop(props.splitAt + 0.03 + i * 0.015);
        return (
          <div key={i} style={{position: 'absolute', left: bx, top: by, width: binW, height: binH, borderRadius: 26,
            background: CLAUDE.FOOTER, border: `2px solid ${CLAUDE.BORDER}`, boxSizing: 'border-box', opacity: bIn}}>
            <div style={{position: 'absolute', left: 30, top: 36, fontFamily: SERIF, fontSize: SERIF_PX, fontWeight: 700, color: INK,
              lineHeight: 1, opacity: 0.5 + 0.5 * pop(b.at + 0.03)}}>{b.label}</div>
          </div>
        );
      })}
      {chips.map((c, i) => {
        const b = props.bins[c.bin];
        const appear = pop(props.splitAt + 0.02 + i * 0.008);
        const t = atomFlight(b.at, c.j, props, ramp);
        return (
          <div key={i} style={{position: 'absolute', left: lerp(c.x0, c.x1, t), top: lerp(c.y0, c.y1, t), width: c.w, height: chipH,
            transformOrigin: '0 0', transform: `scale(${lerp(cellW / c.w, 1, t)}, ${lerp(cellH / chipH, 1, t)})`, borderRadius: 20,
            background: CLAUDE.CARD, border: `4px solid ${t > 0.5 ? CLAUDE.BORDER : CLAUDE.GHOST}`, boxSizing: 'border-box', opacity: appear,
            boxShadow: t > 0.5 ? '0 8px 24px rgba(61,57,41,0.12)' : 'none',
            display: 'flex', alignItems: 'center', justifyContent: 'center', overflow: 'hidden'}}>
            <span style={{fontFamily: SANS, fontSize: SANS_PX, fontWeight: 700, color: INK, whiteSpace: 'nowrap',
              opacity: clamp01((t - 0.75) / 0.25)}}>{c.text}</span>
          </div>
        );
      })}
      {focus && (
        <div style={{position: 'absolute', left: focus.x1 - 14, top: focus.y1 - 14, width: focus.w + 28, height: chipH + 28,
          borderRadius: 30, border: `8px solid ${ACCENT}`, boxSizing: 'border-box', opacity: ringIn}} />
      )}
      <Text916 text={props.line} top={lineTop} weight={700} opacity={pop(props.lineAt)} />
      <LogoBug portrait />
    </AbsoluteFill>
  );
};

// ── B04 ──────────────────────────────────────────────────────────────────────
export const TenFormats916: React.FC<TenFormatsProps> = (props) => {
  const {pop, ramp, p} = useBeat(props.durationSeconds);
  const gapX = 24, gapY = 18;
  const tw = (S.w - gapX) / 2, th = 200;
  const n = litCount(props, p);
  const tenIn = ramp(props.tenAt, 0.05);
  const rows = Math.ceil(props.tiles.length / 2);
  const counterTop = TOP + rows * th + (rows - 1) * gapY + 32;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      {props.tiles.map((t, i) => {
        const x = S.x + (i % 2) * (tw + gapX), y = TOP + Math.floor(i / 2) * (th + gapY);
        const slot = pop(props.slotsAt + i * 0.006);
        const lit = pop(t.at);
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: x, top: y, width: tw, height: th, borderRadius: 24, boxSizing: 'border-box',
              border: `4px dashed ${CLAUDE.GHOST}`, opacity: slot * (1 - lit)}}>
              <div style={{position: 'absolute', left: 24, top: 18, fontFamily: SANS, fontSize: SANS_PX, fontWeight: 700, color: SOFT,
                opacity: 0.6, lineHeight: 1}}>{pad2(i)}</div>
            </div>
            <Card style={{position: 'absolute', left: x, top: y, width: tw, height: th, boxSizing: 'border-box', padding: '12px 24px',
              opacity: lit, transform: `scale(${0.9 + 0.1 * lit})`}}>
              <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start'}}>
                <span style={{fontFamily: SANS, fontSize: SANS_PX, fontWeight: 700, color: SOFT, lineHeight: 1}}>{pad2(i)}</span>
                <TenGlyph kind={t.glyph} size={84} />
              </div>
              <div style={{fontFamily: SERIF, fontSize: SERIF_PX, fontWeight: 700, color: INK, lineHeight: 1, marginTop: 8,
                whiteSpace: 'nowrap'}}>{t.label}</div>
            </Card>
          </React.Fragment>
        );
      })}
      <div style={{position: 'absolute', left: S.x, width: S.w, top: counterTop, height: 200, display: 'flex', alignItems: 'center',
        justifyContent: 'center', gap: 36, opacity: pop(props.slotsAt)}}>
        <span style={{fontFamily: SERIF, fontSize: 116, fontWeight: 700, color: INK}}>{props.sourceLabel}</span>
        <svg width={130} height={70} viewBox="0 0 120 60">
          <path d="M 6 30 L 104 30 M 84 12 L 106 30 L 84 48" fill="none" stroke={INK} strokeWidth={7} strokeLinecap="round" strokeLinejoin="round" />
        </svg>
        <span style={{position: 'relative', fontFamily: SERIF, fontSize: 190, fontWeight: 700, color: INK, lineHeight: 1,
          minWidth: 210, textAlign: 'center'}}>
          {Math.max(1, n)}
          <span style={{position: 'absolute', left: 0, right: 0, bottom: -20, height: 14, borderRadius: 7, background: ACCENT,
            transform: `scaleX(${tenIn})`}} />
        </span>
      </div>
      <Text916 text={props.countLabel} top={counterTop + 206} size={SANS_PX} font={SANS} weight={700} color={SOFT}
        opacity={pop(props.slotsAt)} />
      <LogoBug portrait />
    </AbsoluteFill>
  );
};

// ── B05 ──────────────────────────────────────────────────────────────────────
export const ReshapeNotCopy916: React.FC<ReshapeNotCopyProps> = (props) => {
  const {pop, ramp} = useBeat(props.durationSeconds);
  const rowH = 390, gap = 24;
  const copiesIn = pop(props.copiesAt);
  const strike = ramp(props.strikeAt, 0.05);
  const sameTop = TOP + 3 * rowH + 2 * gap + 30;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      {props.cols.map((c, i) => {
        const y = TOP + i * (rowH + gap);
        const re = pop(c.at);
        const out = Math.max(0, 1 - 2 * re), inn = Math.max(0, 2 * re - 1);
        const oIn = pop(c.openAt), eIn = pop(c.endAt);
        return (
          <Card key={i} style={{position: 'absolute', left: S.x, top: y, width: S.w, height: rowH, boxSizing: 'border-box',
            padding: '24px 36px', opacity: copiesIn}}>
            <div style={{display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', height: 96}}>
              <span style={{fontFamily: SERIF, fontSize: SERIF_PX, fontWeight: 700, color: INK, lineHeight: 1}}>{c.platform}</span>
              <span style={{position: 'relative', fontFamily: SANS, fontSize: SANS_PX, fontStyle: 'italic', color: SOFT, lineHeight: 1}}>
                <span style={{opacity: out}}>{props.pastedLabel}</span>
                <span style={{position: 'absolute', right: 0, top: 0, whiteSpace: 'nowrap', opacity: inn}}>{c.shape}</span>
              </span>
            </div>
            <div style={{position: 'absolute', left: 36, right: 36, top: 136, opacity: (1 - 0.55 * strike) * out}}>
              <div style={{position: 'relative', fontFamily: SERIF, fontSize: SERIF_PX, color: INK, lineHeight: 1.08}}>
                {props.pasted}
                <div style={{position: 'absolute', left: -8, top: '46%', height: 10, borderRadius: 5, background: ACCENT,
                  width: `calc(${strike * 100}% + 16px)`, opacity: strike > 0 ? 1 : 0}} />
              </div>
            </div>
            <div style={{position: 'absolute', left: 36, right: 36, top: 136, opacity: inn}}>
              <div style={{fontFamily: SERIF, fontSize: SERIF_PX, fontStyle: 'italic', color: INK, lineHeight: 1.05, whiteSpace: 'nowrap',
                opacity: oIn}}>{c.open}</div>
              <div style={{fontFamily: SANS, fontSize: SANS_PX, fontStyle: 'italic', color: SOFT, lineHeight: 1.05, marginTop: 30,
                whiteSpace: 'nowrap', opacity: eIn}}>{c.end}</div>
            </div>
          </Card>
        );
      })}
      <Text916 text={props.sameLine} top={sameTop} weight={700} opacity={pop(props.sameAt)} />
      <Text916 text={props.caption} top={sameTop + 124} size={SANS_PX} font={SANS} color={SOFT} align="left" opacity={copiesIn} />
      <LogoBug portrait />
    </AbsoluteFill>
  );
};

// ── B06 ──────────────────────────────────────────────────────────────────────
export const ReleaseRunway916: React.FC<ReleaseRunwayProps> = (props) => {
  const {pop, ramp} = useBeat(props.durationSeconds);
  const anchor = {y: TOP, h: 150};
  const capTop = anchor.y + anchor.h + 26;
  const runTop = capTop + 124, runBot = S.b - 130;
  const firstDay = 2;
  const dayH = (runBot - runTop) / (props.days - firstDay + 1);
  const dy = (d: number) => runTop + (d - firstDay + 0.5) * dayH;
  const lineX = S.x + 150, tile = 72;
  const drawn = ramp(props.runwayAt, 0.12);
  const aIn = pop(props.anchorAt), ringIn = pop(props.ringAt);
  const back = ramp(props.backAt, 0.08);
  const lastDay = Math.max(...props.pieces.map((q) => q.day));
  const backX = S.r - 34;
  const yLast = dy(lastDay), yTop = anchor.y + anchor.h + 16;
  const backLen = (backX - (lineX + 300)) + (yLast - yTop);
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      <svg width={1080} height={1920} style={{position: 'absolute', inset: 0}}>
        <line x1={lineX} y1={runTop} x2={lineX} y2={runTop + (runBot - runTop) * drawn} stroke={SOFT} strokeWidth={8}
          strokeLinecap="round" />
        {Array.from({length: props.days - firstDay + 1}, (_, i) => i + firstDay).map((d) => (
          <line key={d} x1={lineX - 16} y1={dy(d)} x2={lineX + 16} y2={dy(d)} stroke={SOFT} strokeWidth={5}
            opacity={drawn >= (d - firstDay + 0.5) / (props.days - firstDay + 1) ? 1 : 0} />
        ))}
        {back > 0 && (
          <path d={`M ${lineX + 300} ${yLast} L ${backX} ${yLast} L ${backX} ${yTop}`} fill="none" stroke={INK} strokeWidth={7}
            strokeLinecap="round" strokeLinejoin="round" strokeDasharray={backLen} strokeDashoffset={backLen * (1 - back)} />
        )}
        {back > 0.97 && <path d={`M ${backX - 20} ${yTop + 26} L ${backX} ${yTop} L ${backX + 20} ${yTop + 26}`}
          fill="none" stroke={INK} strokeWidth={7} strokeLinecap="round" strokeLinejoin="round" />}
      </svg>
      <Card style={{position: 'absolute', left: S.x, top: anchor.y, width: S.w, height: anchor.h, boxSizing: 'border-box',
        display: 'flex', alignItems: 'center', gap: 30, padding: '0 34px', background: CLAUDE.FOOTER, opacity: aIn,
        transform: `translateY(${(1 - aIn) * -40}px)`}}>
        <div style={{position: 'relative', width: 100, height: 100, flexShrink: 0}}>
          <TenGlyph kind="video" size={100} />
          <div style={{position: 'absolute', left: -12, top: -12, width: 124, height: 124, borderRadius: 26,
            border: `7px solid ${ACCENT}`, boxSizing: 'border-box', opacity: ringIn}} />
        </div>
        <span style={{fontFamily: SANS, fontSize: SANS_PX, fontWeight: 700, color: INK, whiteSpace: 'nowrap'}}>{props.anchorLabel}</span>
      </Card>
      <Text916 text={props.caption} top={capTop} size={SANS_PX} font={SANS} color={SOFT} align="left" opacity={drawn} />
      {Array.from({length: props.days - firstDay + 1}, (_, i) => i + firstDay).map((d) => (
        <div key={d} style={{position: 'absolute', left: S.x, width: 100, top: dy(d) - 39, textAlign: 'right', fontFamily: SANS,
          fontSize: SANS_PX, fontWeight: 600, color: SOFT, lineHeight: 1,
          opacity: drawn >= (d - firstDay + 0.5) / (props.days - firstDay + 1) ? 1 : 0}}>{d}</div>
      ))}
      {props.pieces.map((q, i) => {
        const t = pop(q.at);
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: lineX + 40, top: dy(q.day) - tile / 2, width: tile, height: tile, borderRadius: 16,
              background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, display: 'flex', alignItems: 'center',
              justifyContent: 'center', opacity: t, transform: `translateX(${(1 - t) * 60}px)`}}>
              <TenGlyph kind={q.glyph} size={58} />
            </div>
            <div style={{position: 'absolute', left: lineX + 140, top: dy(q.day) - 39, fontFamily: SANS, fontSize: SANS_PX,
              fontWeight: 700, color: INK, lineHeight: 1, whiteSpace: 'nowrap', opacity: t}}>{q.label}</div>
          </React.Fragment>
        );
      })}
      <Text916 text={props.backLine} top={runBot + 22} weight={700} align="left" opacity={pop(props.backAt + 0.03)} />
      <LogoBug portrait />
    </AbsoluteFill>
  );
};

// ── B07 ──────────────────────────────────────────────────────────────────────
export const QualityGate916: React.FC<QualityGateProps> = (props) => {
  const {pop, p} = useBeat(props.durationSeconds);
  const n = props.glyphs.length;
  const perRow = Math.ceil(n / 2);
  const gap = 18, tw = (S.w - gap * (perRow - 1)) / perRow, th = 190;
  const checkH = 130, checkGap = 20;
  const rowsTop = TOP + props.checks.length * (checkH + checkGap) + 50;
  const rowY = (r: number) => rowsTop + r * (th + 76);
  const {g} = gateState(props, p, 0, perRow);
  const gateVis = p >= props.gateAt ? 1 - clamp01((p - props.gateAt - props.gateSpan - 0.02) / 0.04) : 0;
  const gx = S.x + 9 + g * (S.w - 18);
  const shipTop = rowY(2) + 30;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      {props.checks.map((c, i) => {
        const t = pop(c.at);
        return (
          <Card key={i} style={{position: 'absolute', left: S.x, top: TOP + i * (checkH + checkGap), width: S.w, height: checkH,
            boxSizing: 'border-box', display: 'flex', alignItems: 'center', gap: 30, padding: '0 34px', opacity: t,
            border: `3px solid ${CLAUDE.BORDER}`}}>
            <span style={{fontFamily: SANS, fontSize: SANS_PX, fontWeight: 700, color: SOFT, lineHeight: 1}}>{i + 1}</span>
            <span style={{fontFamily: SERIF, fontSize: SERIF_PX, fontWeight: 700, color: INK, lineHeight: 1, whiteSpace: 'nowrap'}}>{c.label}</span>
          </Card>
        );
      })}
      {props.glyphs.map((gk, i) => {
        const col = i % perRow, row = Math.floor(i / perRow);
        const x = S.x + col * (tw + gap), y = rowY(row);
        const appear = pop(props.tilesAt + i * 0.01);
        const {passed} = gateState(props, p, col, perRow);
        const fail = props.fails.includes(i);
        const f = fail ? ease(passed) : 0;
        return (
          <React.Fragment key={i}>
            <Card style={{position: 'absolute', left: x, top: y, width: tw, height: th, boxSizing: 'border-box', display: 'flex',
              flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 10, opacity: appear * (1 - 0.55 * f),
              border: `3px solid ${CLAUDE.BORDER}`, background: fail && passed > 0.5 ? CLAUDE.FOOTER : CLAUDE.CARD}}>
              <span style={{fontFamily: SANS, fontSize: SANS_PX, fontWeight: 700, color: SOFT, lineHeight: 1}}>{pad2(i)}</span>
              <TenGlyph kind={gk} size={78} />
            </Card>
            {fail ? (
              <svg width={tw} height={th} viewBox={`0 0 ${tw} ${th}`} style={{position: 'absolute', left: x, top: y, opacity: f}}>
                <path d={`M ${tw * 0.18} ${th * 0.18} L ${tw * 0.82} ${th * 0.82} M ${tw * 0.82} ${th * 0.18} L ${tw * 0.18} ${th * 0.82}`}
                  stroke={INK} strokeWidth={10} strokeLinecap="round" />
              </svg>
            ) : (
              <div style={{position: 'absolute', left: x + (tw - 56) / 2, top: y + th + 8, opacity: passed}}><Check size={56} /></div>
            )}
          </React.Fragment>
        );
      })}
      <div style={{position: 'absolute', left: gx - 7, top: rowsTop - 40, width: 14, height: 2 * th + 76 + 80, borderRadius: 7,
        background: ACCENT, opacity: gateVis}} />
      <Text916 text={props.shipLine} top={shipTop} size={116} weight={700} opacity={pop(props.shipAt)} />
      <Text916 text={props.verdict} top={shipTop + 150} italic opacity={pop(props.verdictAt)} />
      <Text916 text={props.caption} top={S.b - 90} size={SANS_PX} font={SANS} color={SOFT} align="left" opacity={pop(props.tilesAt)} />
      <LogoBug portrait />
    </AbsoluteFill>
  );
};
