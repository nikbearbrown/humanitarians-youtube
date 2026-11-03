import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {z} from 'zod';
import {CLAUDE} from '../tokens/claude';
import {SAFE916} from '../tokens/layout';
import {
  ACCENT, Card, INK, SANS, SERIF, SOFT, STAGE, Spark, useBeat,
  socialAudienceBranchSchema, socialCadenceGridSchema, socialHumanSplitSchema, socialLoopSchema,
  socialOneToManySchema, socialTrendWindowSchema, handleTitleOutroSchema,
} from './SocialAiVisibility';

/**
 * SocialAiVisibility916.tsx — native 9:16 layouts for the SocialAiVisibility scenes.
 *
 * Registered as `<Name>916` (same zod schemas as the 16:9 scenes). Portrait is
 * re-composed, not squeezed: one column, fewer words per frame, and type sized
 * for GATE T's portrait floor (1.9% of 3840px ≈ 72px x-height at 2× render),
 * i.e. serif ≥ 90 and sans ≥ 76 CSS px. Long labels are shortened through the
 * vertical beat sheet's own props, never by shrinking type.
 */

const S = SAFE916;
const SERIF_PX = 92;   // body serif — clears the 72px portrait x-height floor
const SANS_PX = 78;    // body sans
const TOP = S.y + 260; // content starts under a (possibly two-line) spark line

const SparkLine916: React.FC<{text: string}> = ({text}) => (
  <div style={{position: 'absolute', left: S.x, top: S.y, width: S.w, height: 230, display: 'flex',
    alignItems: 'center', justifyContent: 'center', gap: 26}}>
    <Spark size={78} />
    <span style={{fontFamily: SERIF, fontSize: SERIF_PX, color: INK, fontWeight: 600, lineHeight: 1.05,
      textAlign: 'center', maxWidth: S.w - 110}}>{text}</span>
  </div>
);

const Bug916: React.FC = () => (
  <Img src={staticFile('hai-wordmark-outlined.svg')}
    style={{position: 'absolute', right: 1080 - S.r, bottom: 1920 - S.b, height: 54, opacity: 0.55}} />
);

const Line916: React.FC<{text: string; top: number; size?: number; color?: string; align?: 'left' | 'center';
  font?: string; weight?: number; italic?: boolean; opacity?: number}> = (
  {text, top, size = SANS_PX, color = SOFT, align = 'left', font = SANS, weight = 400, italic = false, opacity = 1}) => (
  <div style={{position: 'absolute', left: S.x, width: S.w, top, fontFamily: font, fontSize: size, color,
    textAlign: align, fontWeight: weight, fontStyle: italic ? 'italic' : 'normal', lineHeight: 1.08, opacity}}>{text}</div>
);

// ── B02 ──────────────────────────────────────────────────────────────────────
export const SocialOneToMany916: React.FC<z.infer<typeof socialOneToManySchema>> = (props) => {
  const {pop} = useBeat(props.durationSeconds);
  const n = props.outputs.length;
  const ideaH = 250, gap = 12, rowH = 108;
  const listTop = TOP + ideaH + 50;
  const stagger = props.outputsSpan / Math.max(1, n - 1);
  const spineX = S.x + 34;
  const lastY = listTop + (n - 1) * (rowH + gap) + rowH / 2;
  const reach = pop(props.outputsAt + props.outputsSpan);
  const ideaIn = pop(0.02), bottomIn = pop(props.bottomAt);
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      <Card style={{position: 'absolute', left: S.x, top: TOP, width: S.w, height: ideaH, display: 'flex',
        flexDirection: 'column', alignItems: 'center', justifyContent: 'center', border: `3px solid ${CLAUDE.GHOST}`,
        opacity: ideaIn, transform: `scale(${0.9 + 0.1 * ideaIn})`}}>
        <div style={{fontFamily: SANS, fontSize: SANS_PX, letterSpacing: '0.12em', color: SOFT, fontWeight: 700}}>{props.ideaLabel}</div>
        <div style={{fontFamily: SERIF, fontSize: 100, color: INK, fontWeight: 700, lineHeight: 1.05}}>{props.idea}</div>
      </Card>
      <svg width={1080} height={1920} style={{position: 'absolute', inset: 0}}>
        <path d={`M ${spineX} ${TOP + ideaH} L ${spineX} ${lastY}`} stroke={SOFT} strokeWidth={4} opacity={0.6}
          strokeDasharray={1600} strokeDashoffset={1600 * (1 - reach)} fill="none" />
      </svg>
      {props.outputs.map((o, i) => {
        const t = pop(props.outputsAt + i * stagger);
        const y = listTop + i * (rowH + gap);
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: spineX - 9, top: y + rowH / 2 - 9, width: 18, height: 18,
              borderRadius: 9, background: SOFT, opacity: t}} />
            <Card style={{position: 'absolute', left: S.x + 80, top: y, width: S.w - 80, height: rowH, display: 'flex',
              alignItems: 'center', padding: '0 40px', boxSizing: 'border-box', opacity: t,
              transform: `translateX(${(1 - t) * 30}px)`}}>
              <span style={{fontFamily: SERIF, fontSize: SERIF_PX, fontWeight: 700, color: INK, lineHeight: 1}}>{o.label}</span>
            </Card>
          </React.Fragment>
        );
      })}
      <Line916 text={props.bottomLine} top={listTop + n * (rowH + gap) + 30} size={SERIF_PX} font={SERIF}
        color={INK} align="center" opacity={bottomIn} />
      <Bug916 />
    </AbsoluteFill>
  );
};

// ── B03 ──────────────────────────────────────────────────────────────────────
export const SocialCadenceGrid916: React.FC<z.infer<typeof socialCadenceGridSchema>> = (props) => {
  const {pop} = useBeat(props.durationSeconds);
  const campH = 140, headH = 96, rowH = 170, rowGap = 12, labelW = 440;
  const nDays = props.days.length;
  const cellW = (S.w - labelW) / nDays;
  const headTop = TOP + campH + 40;
  const rowsTop = headTop + headH;
  const dot = 46;
  const nRows = props.platforms.length;
  const rowStagger = props.rowsSpan / Math.max(1, nRows - 1);
  const campIn = pop(0.02);
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      <Card style={{position: 'absolute', left: S.x + 90, top: TOP, width: S.w - 180, height: campH, display: 'flex',
        alignItems: 'center', justifyContent: 'center', border: `3px solid ${CLAUDE.GHOST}`, opacity: campIn}}>
        <span style={{fontFamily: SERIF, fontSize: 96, fontWeight: 700, color: INK}}>{props.campaign}</span>
      </Card>
      {props.days.map((d, j) => (
        <div key={j} style={{position: 'absolute', left: S.x + labelW + j * cellW, width: cellW, top: headTop,
          textAlign: 'center', fontFamily: SANS, fontSize: SANS_PX, fontWeight: 600, color: SOFT, opacity: campIn}}>{d}</div>
      ))}
      {props.platforms.map((pl, i) => {
        const rowIn = pop(props.rowsAt + i * rowStagger);
        const y = rowsTop + i * (rowH + rowGap);
        return (
          <React.Fragment key={pl.name}>
            <div style={{position: 'absolute', left: S.x, top: y, width: S.w, height: rowH, borderRadius: 18,
              background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, opacity: 0.35 + 0.65 * rowIn}} />
            <div style={{position: 'absolute', left: S.x + 26, top: y, height: rowH, width: labelW - 30, display: 'flex',
              flexDirection: 'column', justifyContent: 'center', gap: 8, opacity: rowIn}}>
              <div style={{fontFamily: SERIF, fontSize: SERIF_PX, fontWeight: 700, color: INK, lineHeight: 0.95}}>{pl.name}</div>
              <div style={{fontFamily: SANS, fontSize: SANS_PX, color: SOFT, lineHeight: 0.95}}>{pl.format}</div>
            </div>
            {pl.slots.map((sl, k) => {
              const t = pop(props.rowsAt + i * rowStagger + 0.02 + k * 0.012);
              const cx = S.x + labelW + sl * cellW + cellW / 2;
              return <div key={k} style={{position: 'absolute', left: cx - dot / 2, top: y + rowH / 2 - dot / 2,
                width: dot, height: dot, borderRadius: dot / 2, background: INK, opacity: 0.85, transform: `scale(${t})`}} />;
            })}
          </React.Fragment>
        );
      })}
      <Line916 text={props.caption} top={rowsTop + nRows * (rowH + rowGap) + 8} />
      <Bug916 />
    </AbsoluteFill>
  );
};

// ── B04 ──────────────────────────────────────────────────────────────────────
export const SocialTrendWindow916: React.FC<z.infer<typeof socialTrendWindowSchema>> = (props) => {
  const {pop, ramp} = useBeat(props.durationSeconds);
  const chipH = 86, chipGap = 12;
  const chipsH = props.signals.length * chipH + (props.signals.length - 1) * chipGap;
  const yLabelTop = TOP + chipsH + 34;
  const chartTop = yLabelTop + 100, chartBottom = chartTop + 400;
  const chartL = S.x + 30, chartR = S.r - 10, cw = chartR - chartL, chh = chartBottom - chartTop;
  const curve = (u: number) => Math.exp(-Math.pow((u - 0.45) / 0.17, 2));
  const N = 90;
  const pts = Array.from({length: N + 1}, (_, i) => ({x: chartL + (i / N) * cw, y: chartBottom - curve(i / N) * chh * 0.9}));
  const drawn = ramp(props.curveAt, 0.18);
  const vis = pts.slice(0, Math.max(2, Math.round(drawn * N) + 1));
  const d = vis.map((q, i) => `${i ? 'L' : 'M'} ${q.x.toFixed(1)} ${q.y.toFixed(1)}`).join(' ');
  const at = (u: number) => ({x: chartL + u * cw, y: chartBottom - curve(u) * chh * 0.9});
  const early = at(0.3), late = at(0.72);
  const eIn = pop(props.earlyAt), lIn = pop(props.lateAt);
  const win = pts.filter((q) => q.x >= early.x && q.x <= chartL + 0.62 * cw);
  const winD = `M ${win[0].x} ${chartBottom} ` + win.map((q) => `L ${q.x} ${q.y}`).join(' ') + ` L ${win[win.length - 1].x} ${chartBottom} Z`;
  const legendTop = chartBottom + 50;
  const legend = [
    {text: props.earlyLabel, color: ACCENT, t: eIn},
    {text: props.lateLabel, color: CLAUDE.GHOST, t: lIn},
  ];
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      {props.signals.map((s, i) => {
        const t = pop(props.signalsAt + i * 0.04);
        return (
          <div key={s} style={{position: 'absolute', left: S.x, top: TOP + i * (chipH + chipGap), width: S.w, height: chipH,
            borderRadius: chipH / 2, background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, display: 'flex',
            alignItems: 'center', justifyContent: 'center', fontFamily: SANS, fontSize: SANS_PX, fontWeight: 600,
            color: INK, opacity: t, transform: `scale(${0.9 + 0.1 * t})`}}>{s}</div>
        );
      })}
      <Line916 text={`↑ ${props.yLabel}`} top={yLabelTop} />
      <svg width={1080} height={1920} style={{position: 'absolute', inset: 0}}>
        <line x1={chartL} y1={chartBottom} x2={chartR} y2={chartBottom} stroke={SOFT} strokeWidth={4} />
        <line x1={chartL} y1={chartTop} x2={chartL} y2={chartBottom} stroke={SOFT} strokeWidth={4} />
        <path d={winD} fill={ACCENT} opacity={0.14 * eIn} />
        <path d={d} fill="none" stroke={INK} strokeWidth={7} strokeLinecap="round" strokeLinejoin="round" />
        <circle cx={early.x} cy={early.y} r={22 * eIn} fill={ACCENT} />
        <circle cx={late.x} cy={late.y} r={20 * lIn} fill={CLAUDE.GHOST} />
      </svg>
      {legend.map((l, i) => (
        <div key={i} style={{position: 'absolute', left: S.x, top: legendTop + i * 104, width: S.w, display: 'flex',
          alignItems: 'center', gap: 28, opacity: l.t}}>
          <div style={{width: 40, height: 40, borderRadius: 20, background: l.color, flexShrink: 0}} />
          <span style={{fontFamily: SERIF, fontSize: SERIF_PX, color: INK, lineHeight: 1}}>{l.text}</span>
        </div>
      ))}
      <Line916 text={props.caption} top={legendTop + 2 * 104 + 20} />
      <Bug916 />
    </AbsoluteFill>
  );
};

// ── B05 ──────────────────────────────────────────────────────────────────────
export const SocialAudienceBranch916: React.FC<z.infer<typeof socialAudienceBranchSchema>> = (props) => {
  const {pop} = useBeat(props.durationSeconds);
  const prodH = 160, cardH = 250, gap = 34;
  const cardsTop = TOP + prodH + 70;
  const spineX = S.x + 34;
  const segs = props.segments.map((s, i) => ({...s, y: cardsTop + i * (cardH + gap), t: pop(props.segmentsAt[i] ?? 0.4 + i * 0.15)}));
  const lastY = segs[segs.length - 1].y + cardH / 2;
  const reach = Math.max(...segs.map((s) => s.t));
  const prodIn = pop(0.03);
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      <Card style={{position: 'absolute', left: S.x + 110, top: TOP, width: S.w - 220, height: prodH, display: 'flex',
        alignItems: 'center', justifyContent: 'center', border: `3px solid ${CLAUDE.GHOST}`, opacity: prodIn}}>
        <span style={{fontFamily: SERIF, fontSize: 100, fontWeight: 700, color: INK}}>{props.product}</span>
      </Card>
      <svg width={1080} height={1920} style={{position: 'absolute', inset: 0}}>
        <path d={`M ${S.x + S.w / 2} ${TOP + prodH} L ${S.x + S.w / 2} ${TOP + prodH + 34} L ${spineX} ${TOP + prodH + 34} L ${spineX} ${lastY}`}
          fill="none" stroke={SOFT} strokeWidth={4} opacity={0.6} strokeDasharray={2400} strokeDashoffset={2400 * (1 - reach)} />
        {segs.map((s, i) => <circle key={i} cx={spineX} cy={s.y + cardH / 2} r={11 * s.t} fill={SOFT} />)}
      </svg>
      {segs.map((s, i) => (
        <Card key={i} style={{position: 'absolute', left: S.x + 80, top: s.y, width: S.w - 80, height: cardH,
          boxSizing: 'border-box', padding: '0 40px', display: 'flex', flexDirection: 'column', justifyContent: 'center',
          gap: 14, opacity: s.t, transform: `translateX(${(1 - s.t) * 30}px)`}}>
          <div style={{fontFamily: SERIF, fontSize: SERIF_PX, fontWeight: 700, color: INK, lineHeight: 1}}>{s.audience}</div>
          <div style={{fontFamily: SANS, fontSize: SANS_PX, color: SOFT, lineHeight: 1}}>{s.angle}</div>
        </Card>
      ))}
      <Line916 text={props.caption} top={cardsTop + segs.length * (cardH + gap) + 10} />
      <Bug916 />
    </AbsoluteFill>
  );
};

// ── B07 ──────────────────────────────────────────────────────────────────────
export const SocialLoop916: React.FC<z.infer<typeof socialLoopSchema>> = (props) => {
  const {pop, p} = useBeat(props.durationSeconds);
  const n = props.stages.length;
  const chipH = 96, chipGap = 16, chipW = (S.w - chipGap) / 2;
  const chipsTop = TOP + 100;
  const chainTop = chipsTop + 2 * chipH + chipGap + 60;
  const nodeH = 108, nodeGap = 22, nodeW = 560, nodeX = S.x + (S.w - nodeW) / 2 - 60;
  const nodeY = (i: number) => chainTop + i * (nodeH + nodeGap);
  const stagger = props.stagesSpan / Math.max(1, n - 1);
  const active = Math.floor(Math.min(1, Math.max(0, (p - props.stagesAt) / props.stagesSpan)) * (n - 0.001));
  // loop-back path: down the chain centre, out to the right margin, back up to Create
  const cx = nodeX + nodeW / 2, rx = S.r - 70;
  const topY = nodeY(0) + nodeH / 2, botY = nodeY(n - 1) + nodeH / 2;
  const loopD = `M ${cx} ${topY} L ${cx} ${botY} L ${rx} ${botY} L ${rx} ${topY} L ${nodeX + nodeW} ${topY}`;
  const loopLen = (botY - topY) * 2 + (rx - cx) * 2;
  const tLoop = Math.min(1, Math.max(0, (p - props.stagesAt) / (1 - props.stagesAt)));
  const along = (tLoop * 1.4) % 1;
  const seg = (u: number) => {
    const L1 = botY - topY, L2 = rx - cx, L3 = botY - topY;
    let dist = u * (L1 + L2 + L3 + (rx - (nodeX + nodeW)));
    if (dist < L1) return {x: cx, y: topY + dist}; dist -= L1;
    if (dist < L2) return {x: cx + dist, y: botY}; dist -= L2;
    if (dist < L3) return {x: rx, y: botY - dist}; dist -= L3;
    return {x: rx - dist, y: topY};
  };
  const dotP = seg(along);
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      {/* words, not "→": a thin arrow glyph measures as a sub-floor text run in GATE T */}
      <Line916 text={props.signalsLabel ?? `signals feed ${props.stages[props.signalsInto]}`} top={TOP} align="center" opacity={pop(props.signalsAt)} />
      {props.signals.map((s, i) => {
        const t = pop(props.signalsAt + i * 0.05);
        return (
          <div key={s} style={{position: 'absolute', left: S.x + (i % 2) * (chipW + chipGap),
            top: chipsTop + Math.floor(i / 2) * (chipH + chipGap), width: chipW, height: chipH, borderRadius: 18,
            background: CLAUDE.FOOTER, border: `2px solid ${CLAUDE.BORDER}`, display: 'flex', alignItems: 'center',
            justifyContent: 'center', fontFamily: SANS, fontSize: SANS_PX, fontWeight: 600, color: INK, opacity: t}}>{s}</div>
        );
      })}
      <svg width={1080} height={1920} style={{position: 'absolute', inset: 0}}>
        <path d={loopD} fill="none" stroke={SOFT} strokeWidth={4} opacity={0.55} strokeDasharray={loopLen}
          strokeDashoffset={loopLen * (1 - pop(props.stagesAt))} />
        {p > props.stagesAt && <circle cx={dotP.x} cy={dotP.y} r={18} fill={ACCENT} />}
      </svg>
      {props.stages.map((s, i) => {
        const t = pop(props.stagesAt + i * stagger);
        const on = i === active && p > props.stagesAt;
        return (
          <Card key={s} style={{position: 'absolute', left: nodeX, top: nodeY(i), width: nodeW, height: nodeH, display: 'flex',
            alignItems: 'center', justifyContent: 'center', border: on ? `5px solid ${CLAUDE.GHOST}` : `3px solid ${CLAUDE.BORDER}`,
            opacity: 0.4 + 0.6 * t, transform: `scale(${on ? 1.06 : 1})`}}>
            <span style={{fontFamily: SERIF, fontSize: SERIF_PX, fontWeight: 700, color: INK, lineHeight: 1}}>{s}</span>
          </Card>
        );
      })}
      <Line916 text={props.center} top={nodeY(n - 1) + nodeH + 50} size={SERIF_PX} font={SERIF} color={INK}
        align="center" italic opacity={pop(props.stagesAt + props.stagesSpan)} />
      <Bug916 />
    </AbsoluteFill>
  );
};

// ── B08 ──────────────────────────────────────────────────────────────────────
export const SocialHumanSplit916: React.FC<z.infer<typeof socialHumanSplitSchema>> = (props) => {
  const {pop} = useBeat(props.durationSeconds);
  const itemH = 84, titleH = 100, pad = 26;
  const colH = (items: number) => titleH + items * itemH + pad * 2;
  const cols = [
    {title: props.leftTitle, items: props.leftItems, at: props.leftAt, human: false, y: TOP},
    {title: props.rightTitle, items: props.rightItems, at: props.rightAt, human: true,
      y: TOP + colH(props.leftItems.length) + 30},
  ];
  const verdictTop = cols[1].y + colH(props.rightItems.length) + 40;
  const vIn = pop(props.verdictAt);
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      {cols.map((c, ci) => (
        <Card key={ci} style={{position: 'absolute', left: S.x, top: c.y, width: S.w, height: colH(c.items.length),
          boxSizing: 'border-box', padding: `${pad}px 40px`, opacity: 0.3 + 0.7 * pop(c.at),
          background: c.human ? CLAUDE.CARD : CLAUDE.FOOTER}}>
          <div style={{fontFamily: SERIF, fontSize: SERIF_PX, fontWeight: 700, color: INK, height: titleH, lineHeight: 1}}>{c.title}</div>
          {c.items.map((it, k) => {
            const t = pop(c.at + 0.03 + k * 0.035);
            return (
              <div key={k} style={{height: itemH, display: 'flex', alignItems: 'center', gap: 24, opacity: t}}>
                <div style={{width: 18, height: 18, borderRadius: 9, background: c.human ? INK : SOFT, flexShrink: 0}} />
                <span style={{fontFamily: SANS, fontSize: SANS_PX, color: INK, lineHeight: 1}}>{it}</span>
              </div>
            );
          })}
        </Card>
      ))}
      <Line916 text={props.verdict} top={verdictTop} size={SERIF_PX} font={SERIF} color={INK} weight={700}
        align="center" opacity={vIn} />
      <div style={{position: 'absolute', left: S.x + S.w / 2 - 230, width: 460 * vIn, top: verdictTop + 220, height: 9,
        borderRadius: 5, background: ACCENT}} />
      <Bug916 />
    </AbsoluteFill>
  );
};

// ── Outro ────────────────────────────────────────────────────────────────────
export const HandleTitleOutro916: React.FC<z.infer<typeof handleTitleOutroSchema>> = (props) => {
  const {pop} = useBeat(props.durationSeconds);
  const m = props.title.match(/^([\s\S]*?)\s*([.?!…]+)\s*$/);
  const body = m ? m[1] : props.title;
  const punct = m ? m[2] : '.';
  const tIn = pop(0.0), hIn = pop(0.12), lIn = pop(0.22);
  return (
    <AbsoluteFill style={{background: CLAUDE.PAGE, alignItems: 'center', justifyContent: 'center', flexDirection: 'column'}}>
      <div style={{marginBottom: 150, opacity: tIn}}><Spark size={190} /></div>
      <div style={{fontFamily: SERIF, fontWeight: 700, fontSize: 132 * props.scale, color: INK, letterSpacing: '-0.02em',
        textAlign: 'center', lineHeight: 1.06, maxWidth: S.w, opacity: tIn, whiteSpace: 'pre-line'}}>
        {body}<span style={{color: CLAUDE.SEND}}>{punct}</span>
      </div>
      <div style={{fontFamily: SERIF, fontSize: 96, color: INK, marginTop: 150, textAlign: 'center', maxWidth: S.w,
        lineHeight: 1.1, opacity: 0.9 * hIn}}>{props.handle}</div>
      <Img src={staticFile(props.logo)} style={{height: 130, marginTop: 200, maxWidth: S.w, opacity: lIn}} />
    </AbsoluteFill>
  );
};
