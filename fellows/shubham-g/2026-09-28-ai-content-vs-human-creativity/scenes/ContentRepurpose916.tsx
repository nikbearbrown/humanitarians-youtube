import React from 'react';
import {AbsoluteFill} from 'remotion';
import {z} from 'zod';
import {CLAUDE} from '../tokens/claude';
import {SAFE916} from '../tokens/layout';
import {ACCENT, Card, INK, SANS, SERIF, SOFT, STAGE, Spark, useBeat} from './SocialAiVisibility';
import {
  DraftBody, Glyph, LogoBug, Phone,
  creativityBalanceSchema, repurposeCascadeSchema, repurposeClipsSchema, repurposeSourceSchema, repurposeVoiceCheckSchema,
} from './ContentRepurpose';

/**
 * ContentRepurpose916.tsx — native 9:16 layouts for the ContentRepurpose scenes.
 *
 * Registered as `<Name>916` with the same zod schemas. Portrait is re-composed
 * (one column, fewer words per frame), and type clears GATE T's portrait floor:
 * serif ≥ 90 and sans ≥ 76 CSS px. Long labels are shortened through the vertical
 * beat sheet's props, never by shrinking type.
 */

const S = SAFE916;
const SERIF_PX = 92;
const SANS_PX = 78;
const TOP = S.y + 260;
const clamp01 = (v: number) => Math.min(1, Math.max(0, v));

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
    fontStyle: italic ? 'italic' : 'normal', textAlign: align, lineHeight: 1.08, opacity}}>{text}</div>
);

// ── B02 ──────────────────────────────────────────────────────────────────────
export const RepurposeSource916: React.FC<z.infer<typeof repurposeSourceSchema>> = (props) => {
  const {pop, ramp, p} = useBeat(props.durationSeconds);
  const bar = {x: S.x, y: 600, w: S.w, h: 360};
  const drawn = ramp(props.barAt, 0.14);
  const n = props.chapters.length;
  const segW = bar.w / n;
  const scanT = clamp01((p - props.scanAt) / props.scanSpan);
  const scanVis = p > props.scanAt ? 1 - ramp(props.scanAt + props.scanSpan + 0.01, 0.04) : 0;
  const headX = bar.x + 34 + scanT * (bar.w - 68);
  const hlW = segW - 28;
  const cardW = (S.w - 2 * 20) / 3, cardH = 170, cardTop = bar.y + bar.h + 70;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      <Text916 text={props.videoLabel} top={TOP} size={SANS_PX} font={SANS} weight={700} opacity={pop(props.barAt)} />
      <Text916 text={props.videoNote} top={TOP + 100} italic color={SOFT} opacity={pop(props.barAt)} />
      <div style={{position: 'absolute', left: bar.x, top: bar.y, width: bar.w * drawn, height: bar.h, overflow: 'hidden', borderRadius: 30}}>
        <div style={{position: 'absolute', inset: 0, width: bar.w, background: CLAUDE.CARD, border: `3px solid ${CLAUDE.BORDER}`,
          borderRadius: 30, boxSizing: 'border-box'}} />
        {props.chapters.map((c, i) => {
          const t = pop(c.at);
          return (
            <div key={i} style={{position: 'absolute', left: i * segW + 8, top: 56, width: segW - 16, height: bar.h - 112,
              borderRadius: 16, background: CLAUDE.FOOTER, border: `2px solid ${CLAUDE.BORDER}`, boxSizing: 'border-box',
              display: 'flex', alignItems: 'center', justifyContent: 'center', opacity: 0.4 + 0.6 * t}}>
              <span style={{fontFamily: SERIF, fontSize: SERIF_PX, fontWeight: 700, color: INK, opacity: t}}>{c.label}</span>
            </div>
          );
        })}
        {Array.from({length: 12}, (_, i) => 30 + i * ((bar.w - 60) / 11)).map((x, i) => (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: x - 12, top: 16, width: 24, height: 22, borderRadius: 5, background: CLAUDE.BORDER}} />
            <div style={{position: 'absolute', left: x - 12, top: bar.h - 38, width: 24, height: 22, borderRadius: 5, background: CLAUDE.BORDER}} />
          </React.Fragment>
        ))}
        {props.moments.map((m, i) => (
          <div key={i} style={{position: 'absolute', left: (i + 0.5) * segW - hlW / 2, top: 46, width: hlW, height: bar.h - 92,
            borderRadius: 16, border: `6px solid ${INK}`, boxSizing: 'border-box', opacity: pop(m.at)}} />
        ))}
      </div>
      <div style={{position: 'absolute', left: headX - 5, top: bar.y - 40, width: 10, height: bar.h + 80, borderRadius: 5,
        background: ACCENT, opacity: scanVis}} />
      <div style={{position: 'absolute', left: headX - 22, top: bar.y - 62, width: 44, height: 44, borderRadius: 22,
        background: ACCENT, opacity: scanVis}} />
      {props.moments.map((m, i) => {
        const t = pop(m.at);
        const x = S.x + i * (cardW + 20);
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: x + cardW / 2 - 4, top: bar.y + bar.h, width: 8, height: 70 * t, background: INK}} />
            <Card style={{position: 'absolute', left: x, top: cardTop, width: cardW, height: cardH, display: 'flex',
              alignItems: 'center', justifyContent: 'center', opacity: t, transform: `translateY(${(1 - t) * -24}px)`}}>
              <span style={{fontFamily: SERIF, fontSize: SERIF_PX, fontWeight: 700, color: INK}}>{m.label}</span>
            </Card>
          </React.Fragment>
        );
      })}
      <Text916 text={props.jobLine} top={cardTop + cardH + 110} opacity={pop(props.jobAt)} />
      <LogoBug portrait />
    </AbsoluteFill>
  );
};

// ── B04 ──────────────────────────────────────────────────────────────────────
export const RepurposeClips916: React.FC<z.infer<typeof repurposeClipsSchema>> = (props) => {
  const {pop} = useBeat(props.durationSeconds);
  const bar = {x: S.x, y: TOP, w: S.w, h: 84};
  const n = props.clips.length;
  const colW = S.w / n;
  const phoneW = 280, phoneH = 498, phoneTop = TOP + 260;
  const segW = bar.w * 0.12;
  const pickIn = pop(props.pickAt);
  const pcx = S.x + colW * (props.pickIndex + 0.5);
  const pad = 16;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      <div style={{position: 'absolute', left: bar.x, top: bar.y, width: bar.w, height: bar.h, borderRadius: 20,
        background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, opacity: pop(0.02)}} />
      {props.clips.map((c, i) => {
        const t = pop(c.at);
        const cx = S.x + colW * (i + 0.5);
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: bar.x + c.pos * bar.w - segW / 2, top: bar.y + 10, width: segW,
              height: bar.h - 20, borderRadius: 12, background: INK, opacity: 0.3 + 0.55 * pop(0.04)}} />
            <div style={{position: 'absolute', left: cx - colW / 2, width: colW, top: phoneTop - 120, textAlign: 'center',
              fontFamily: SANS, fontSize: SANS_PX, fontWeight: 700, color: SOFT, opacity: t}}>{c.platform}</div>
            <Phone w={phoneW} h={phoneH} moment={c.moment} momentPx={SERIF_PX} barsIn={pop(props.captionsAt + i * 0.03)}
              style={{left: cx - phoneW / 2, top: phoneTop, opacity: t, transform: `translateY(${(1 - t) * -90}px) scale(${0.7 + 0.3 * t})`}} />
          </React.Fragment>
        );
      })}
      <div style={{position: 'absolute', left: pcx - phoneW / 2 - pad, top: phoneTop - pad, width: phoneW + pad * 2,
        height: phoneH + pad * 2, borderRadius: phoneW * 0.14 + pad, border: `8px solid ${ACCENT}`, boxSizing: 'border-box',
        opacity: pickIn}} />
      <div style={{position: 'absolute', left: pcx - 220, width: 440, top: phoneTop + phoneH - 20, height: 110, borderRadius: 55,
        background: CLAUDE.CARD, border: `4px solid ${ACCENT}`, display: 'flex', alignItems: 'center', justifyContent: 'center',
        fontFamily: SANS, fontSize: SANS_PX, fontWeight: 700, color: INK, opacity: pickIn}}>{props.pickLabel}</div>
      <Text916 text={props.aiLine} top={phoneTop + phoneH + 150} opacity={pop(props.aiAt)} />
      <Text916 text={props.youLine} top={phoneTop + phoneH + 470} weight={700} opacity={pickIn} />
      <LogoBug portrait />
    </AbsoluteFill>
  );
};

// ── B05 ──────────────────────────────────────────────────────────────────────
export const RepurposeCascade916: React.FC<z.infer<typeof repurposeCascadeSchema>> = (props) => {
  const {pop, ramp} = useBeat(props.durationSeconds);
  const all = [...props.nodes, ...props.leaves];
  const nodeX = S.x + 90, nodeW = S.w - 90 - 80;
  const rowH = 140, rowGap = 34;
  const rowY = (i: number) => TOP + i * (rowH + rowGap);
  const spineX = S.x + 36;
  const traceX = S.r - 34;
  const firstLeaf = props.nodes.length;
  const traceT = ramp(props.traceAt, 0.1);
  const yLast = rowY(all.length - 1) + rowH / 2, yFirst = rowY(0) + rowH / 2;
  const traceD = `M ${nodeX + nodeW + 6} ${yLast} L ${traceX} ${yLast} L ${traceX} ${yFirst} L ${nodeX + nodeW + 14} ${yFirst}`;
  const traceLen = (traceX - nodeX - nodeW) * 2 + (yLast - yFirst);
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      <svg width={1080} height={1920} style={{position: 'absolute', inset: 0}}>
        {all.slice(1).map((nd, j) => {
          const i = j + 1;
          const t = ramp(nd.at - 0.03, 0.04);
          // leaves branch from the last chain node down a left spine; the chain runs row to row
          const fromY = rowY(Math.min(i - 1, firstLeaf - 1)) + rowH / 2;
          const toY = rowY(i) + rowH / 2;
          const d = `M ${nodeX} ${fromY} L ${spineX} ${fromY} L ${spineX} ${fromY + (toY - fromY) * t} ${t > 0.98 ? `L ${nodeX - 8} ${toY}` : ''}`;
          return t > 0 ? <path key={i} d={d} fill="none" stroke={SOFT} strokeWidth={5} /> : null;
        })}
        {traceT > 0 && <path d={traceD} fill="none" stroke={ACCENT} strokeWidth={10} strokeLinecap="round" strokeLinejoin="round"
          strokeDasharray={traceLen} strokeDashoffset={traceLen * (1 - traceT)} />}
      </svg>
      {all.map((nd, i) => {
        const t = pop(nd.at);
        return (
          <Card key={i} style={{position: 'absolute', left: nodeX, top: rowY(i), width: nodeW, height: rowH, boxSizing: 'border-box',
            display: 'flex', alignItems: 'center', gap: 28, padding: '0 28px', opacity: t,
            transform: `translateX(${(1 - t) * 30}px)`, background: i >= firstLeaf ? CLAUDE.FOOTER : CLAUDE.CARD}}>
            <Glyph kind={nd.glyph} size={96} />
            <span style={{fontFamily: SERIF, fontSize: SERIF_PX, fontWeight: 700, color: INK, lineHeight: 1}}>{nd.label}</span>
          </Card>
        );
      })}
      <Text916 text={props.weekLine} top={rowY(all.length) + 30} weight={700} opacity={pop(props.weekAt + 0.03)} />
      <LogoBug portrait />
    </AbsoluteFill>
  );
};

// ── B06 ──────────────────────────────────────────────────────────────────────
export const RepurposeVoiceCheck916: React.FC<z.infer<typeof repurposeVoiceCheckSchema>> = (props) => {
  const {pop, ramp} = useBeat(props.durationSeconds);
  const gIn = pop(props.guideAt), dIn = pop(props.draftAt);
  const guideTop = TOP, guideH = 520;
  const draftTop = guideTop + guideH + 36;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      <Card style={{position: 'absolute', left: S.x, top: guideTop, width: S.w, height: guideH, boxSizing: 'border-box',
        padding: '30px 40px', background: CLAUDE.FOOTER, opacity: gIn}}>
        <div style={{fontFamily: SERIF, fontSize: SERIF_PX, fontWeight: 700, color: INK, marginBottom: 20, lineHeight: 1}}>{props.guideTitle}</div>
        {props.rules.map((r, i) => {
          const t = pop(r.at);
          return (
            <div key={i} style={{display: 'flex', alignItems: 'baseline', gap: 30, height: 112, opacity: t}}>
              <span style={{fontFamily: SANS, fontSize: SANS_PX, fontWeight: 700, color: SOFT, width: 290, flexShrink: 0}}>{r.k}</span>
              <span style={{fontFamily: SERIF, fontSize: SERIF_PX, color: INK, lineHeight: 1}}>{r.v}</span>
            </div>
          );
        })}
      </Card>
      <Card style={{position: 'absolute', left: S.x, top: draftTop, width: S.w, height: S.b - 230 - draftTop, boxSizing: 'border-box',
        padding: '30px 40px', opacity: dIn}}>
        <div style={{fontFamily: SANS, fontSize: SANS_PX, fontWeight: 700, color: SOFT, marginBottom: 26, lineHeight: 1}}>{props.draftTitle}</div>
        <DraftBody props={props} px={SERIF_PX} pillPx={SANS_PX} gap={26} pop={pop} ramp={ramp} nowrap={false} />
      </Card>
      <Text916 text={props.caption} top={S.b - 200} size={SANS_PX} font={SANS} color={SOFT} align="left" opacity={gIn} />
      <LogoBug portrait />
    </AbsoluteFill>
  );
};

// ── B07 ──────────────────────────────────────────────────────────────────────
export const CreativityBalance916: React.FC<z.infer<typeof creativityBalanceSchema>> = (props) => {
  const {pop, ramp} = useBeat(props.durationSeconds);
  const cx = S.x + S.w / 2;
  const pIn = pop(props.polesAt);
  const halfW = S.w / 2 - 16;
  const rowsTop = TOP + 390, rowH = 112, rowGap = 22, chipW = 470;
  const vIn = pop(props.verdictAt);
  const verdictTop = rowsTop + props.rows.length * (rowH + rowGap) + 50;
  const pole = (side: 'L' | 'R') => (
    <div style={{position: 'absolute', top: TOP, width: halfW, left: side === 'L' ? S.x : S.r - halfW,
      textAlign: side === 'L' ? 'left' : 'right', opacity: pIn}}>
      <div style={{fontFamily: SERIF, fontSize: 116, fontWeight: 700, color: INK, lineHeight: 1}}>
        {side === 'L' ? props.leftPole : props.rightPole}</div>
      <div style={{fontFamily: SANS, fontSize: SANS_PX, color: SOFT, fontStyle: 'italic', lineHeight: 1.05, marginTop: 20,
        opacity: pop(side === 'L' ? props.leftNoteAt : props.rightNoteAt)}}>{side === 'L' ? props.leftNote : props.rightNote}</div>
    </div>
  );
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      {pole('L')}
      {pole('R')}
      <div style={{position: 'absolute', left: cx - 2, top: rowsTop - 24, width: 4, height: props.rows.length * (rowH + rowGap) + 24,
        background: CLAUDE.GHOST, opacity: 0.6 * pIn}} />
      {props.rows.map((r, i) => {
        const y = rowsTop + i * (rowH + rowGap);
        const appear = pop(r.at);
        const slide = ramp(r.at + 0.012, 0.05);
        const e = slide * slide * (3 - 2 * slide);
        const startX = cx - chipW / 2;
        const endX = r.side === 'L' ? S.x : S.r - chipW;
        return (
          <Card key={i} style={{position: 'absolute', left: startX + (endX - startX) * e, top: y, width: chipW, height: rowH,
            display: 'flex', alignItems: 'center', justifyContent: 'center', opacity: appear,
            background: r.side === 'L' ? CLAUDE.FOOTER : CLAUDE.CARD, border: `3px solid ${CLAUDE.BORDER}`}}>
            <span style={{fontFamily: SERIF, fontSize: SERIF_PX, fontWeight: 700, color: INK, lineHeight: 1}}>{r.label}</span>
          </Card>
        );
      })}
      <Text916 text={props.verdict} top={verdictTop} weight={700} opacity={vIn} />
      <div style={{position: 'absolute', left: cx - 230, width: 460 * vIn, top: verdictTop + 130, height: 10, borderRadius: 5,
        background: ACCENT}} />
      <LogoBug portrait />
    </AbsoluteFill>
  );
};
