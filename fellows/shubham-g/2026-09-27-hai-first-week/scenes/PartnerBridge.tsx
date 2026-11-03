import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {z} from 'zod';
import {CLAUDE} from '../tokens/claude';
import {SAFE, SAFE916} from '../tokens/layout';
import {ACCENT, Card, INK, SANS, SERIF, SOFT, STAGE, Spark, useBeat} from './SocialAiVisibility';

/**
 * PartnerBridge — two partner cards join into one shared-goal card (C3, claude stage).
 * For "who works with whom, toward what" beats: a partnership, a collaboration, two
 * teams and their common aim. Names and roles are props — say only what the source says.
 *
 * Dual-aspect: `PartnerBridge` (1920×1080) and `PartnerBridge916` (1080×1920, stacked,
 * type sized for GATE T's portrait floor: serif ≥ 90, sans ≥ 76 CSS px).
 * First used by the reel hai-first-week (@HumanitariansAI).
 */

export const partnerBridgeSchema = z.object({
  durationSeconds: z.number().default(14),
  sparkLine: z.string().default('Two teams, one goal.'),
  left: z.object({name: z.string(), role: z.string()}).default({name: 'Partner A', role: 'what they bring'}),
  right: z.object({name: z.string(), role: z.string()}).default({name: 'Partner B', role: 'what they bring'}),
  goalLabel: z.string().default('SHARED GOAL'),
  goal: z.string().default('The goal they share'),
  leftAt: z.number().default(0.1),
  rightAt: z.number().default(0.25),
  goalAt: z.number().default(0.5),
});
type Props = z.infer<typeof partnerBridgeSchema>;

const Bug: React.FC<{S: typeof SAFE | typeof SAFE916; w: number; h: number; size: number}> = ({S, w, h, size}) => (
  <Img src={staticFile('hai-wordmark-outlined.svg')}
    style={{position: 'absolute', right: w - S.r, bottom: h - S.b, height: size, opacity: 0.55}} />
);

export const PartnerBridge: React.FC<Props> = (props) => {
  const {pop, width, height} = useBeat(props.durationSeconds);
  const S = SAFE;
  const top = S.y + 130;
  const cardW = 760, cardH = 250, gap = S.w - 2 * cardW;
  const goalW = 1500, goalH = 300, goalY = top + cardH + 150;
  const lIn = pop(props.leftAt), rIn = pop(props.rightAt), gIn = pop(props.goalAt);
  const L = {x: S.x, y: top}, R = {x: S.x + cardW + gap, y: top};
  const G = {x: S.x + (S.w - goalW) / 2, y: goalY};
  const join = (from: {x: number; y: number}, t: number) => {
    const sx = from.x + cardW / 2, sy = from.y + cardH, ex = G.x + goalW / 2, ey = G.y;
    return <path d={`M ${sx} ${sy} C ${sx} ${(sy + ey) / 2}, ${ex} ${(sy + ey) / 2}, ${ex} ${ey}`} fill="none"
      stroke={SOFT} strokeWidth={4} opacity={0.7} strokeDasharray={900} strokeDashoffset={900 * (1 - t)} />;
  };
  const partner = (p: {name: string; role: string}, at: {x: number; y: number}, t: number) => (
    <Card style={{position: 'absolute', left: at.x, top: at.y, width: cardW, height: cardH, display: 'flex',
      flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 14, opacity: t,
      transform: `translateY(${(1 - t) * 24}px)`}}>
      <div style={{fontFamily: SERIF, fontSize: 72, fontWeight: 700, color: INK, lineHeight: 1}}>{p.name}</div>
      <div style={{fontFamily: SANS, fontSize: 44, color: SOFT, lineHeight: 1.1, textAlign: 'center', padding: '0 30px'}}>{p.role}</div>
    </Card>
  );
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <div style={{position: 'absolute', left: S.x, top: S.y, width: S.w, display: 'flex', alignItems: 'center',
        justifyContent: 'center', gap: 20}}>
        <Spark size={48} />
        <span style={{fontFamily: SERIF, fontSize: 56, fontWeight: 600, color: INK}}>{props.sparkLine}</span>
      </div>
      <svg width={width} height={height} style={{position: 'absolute', inset: 0}}>
        {join(L, Math.min(lIn, gIn))}
        {join(R, Math.min(rIn, gIn))}
        {/* the beat's one accent: the meeting point */}
        <circle cx={G.x + goalW / 2} cy={G.y} r={16 * gIn} fill={ACCENT} />
      </svg>
      {partner(props.left, L, lIn)}
      {partner(props.right, R, rIn)}
      <Card style={{position: 'absolute', left: G.x, top: G.y, width: goalW, height: goalH, display: 'flex',
        flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 16,
        border: `3px solid ${CLAUDE.GHOST}`, opacity: gIn, transform: `scale(${0.92 + 0.08 * gIn})`}}>
        <div style={{fontFamily: SANS, fontSize: 44, letterSpacing: '0.12em', fontWeight: 700, color: SOFT}}>{props.goalLabel}</div>
        <div style={{fontFamily: SERIF, fontSize: 66, fontWeight: 700, color: INK, lineHeight: 1.1, textAlign: 'center',
          padding: '0 50px'}}>{props.goal}</div>
      </Card>
      <Bug S={S} w={width} h={height} size={34} />
    </AbsoluteFill>
  );
};

export const PartnerBridge916: React.FC<Props> = (props) => {
  const {pop} = useBeat(props.durationSeconds);
  const S = SAFE916;
  const TOP = S.y + 260;
  const cardH = 300, plusH = 80, goalH = 440;
  const lY = TOP, rY = TOP + cardH + plusH, gY = rY + cardH + 70;
  const lIn = pop(props.leftAt), rIn = pop(props.rightAt), gIn = pop(props.goalAt);
  const partner = (p: {name: string; role: string}, y: number, t: number) => (
    <Card style={{position: 'absolute', left: S.x, top: y, width: S.w, height: cardH, display: 'flex',
      flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 14, opacity: t,
      transform: `translateY(${(1 - t) * 30}px)`}}>
      <div style={{fontFamily: SERIF, fontSize: 96, fontWeight: 700, color: INK, lineHeight: 1}}>{p.name}</div>
      <div style={{fontFamily: SANS, fontSize: 78, color: SOFT, lineHeight: 1.05, textAlign: 'center', padding: '0 30px'}}>{p.role}</div>
    </Card>
  );
  const cx = S.x + S.w / 2;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <div style={{position: 'absolute', left: S.x, top: S.y, width: S.w, height: 230, display: 'flex', alignItems: 'center',
        justifyContent: 'center', gap: 26}}>
        <Spark size={78} />
        <span style={{fontFamily: SERIF, fontSize: 92, fontWeight: 600, color: INK, lineHeight: 1.05, textAlign: 'center',
          maxWidth: S.w - 110}}>{props.sparkLine}</span>
      </div>
      {partner(props.left, lY, lIn)}
      <svg width={1080} height={1920} style={{position: 'absolute', inset: 0}}>
        {/* a drawn plus between the partners (a "+" glyph would read as a sub-floor text run) */}
        <g opacity={rIn} stroke={SOFT} strokeWidth={8} strokeLinecap="round">
          <line x1={cx - 26} y1={lY + cardH + plusH / 2} x2={cx + 26} y2={lY + cardH + plusH / 2} />
          <line x1={cx} y1={lY + cardH + plusH / 2 - 26} x2={cx} y2={lY + cardH + plusH / 2 + 26} />
        </g>
        <line x1={cx} y1={rY + cardH} x2={cx} y2={rY + cardH + 70 * gIn} stroke={SOFT} strokeWidth={4} opacity={0.7} />
        <circle cx={cx} cy={gY} r={14 * gIn} fill={SOFT} />
      </svg>
      {partner(props.right, rY, rIn)}
      <Card style={{position: 'absolute', left: S.x, top: gY, width: S.w, height: goalH, display: 'flex',
        flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 18,
        border: `3px solid ${CLAUDE.GHOST}`, opacity: gIn}}>
        <div style={{fontFamily: SANS, fontSize: 78, letterSpacing: '0.1em', fontWeight: 700, color: SOFT}}>{props.goalLabel}</div>
        <div style={{fontFamily: SERIF, fontSize: 92, fontWeight: 700, color: INK, lineHeight: 1.05, textAlign: 'center',
          padding: '0 40px'}}>{props.goal}</div>
      </Card>
      <Bug S={S} w={1080} h={1920} size={54} />
    </AbsoluteFill>
  );
};
