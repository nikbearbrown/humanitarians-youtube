import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { SAFE916 } from '../tokens/layout';
import { agentRuntimeFrameSchema } from './AgentRuntimeFrame';

/**
 * AgentRuntimeFrame916 — native portrait (1080×1920), NOT a crop.
 *
 * Reflow R1 (rotate the axis): landscape runs model → runtime → executor
 * left-to-right; portrait runs it TOP-TO-BOTTOM, which is the natural reading
 * direction on a phone. Ports stack as a vertical list instead of a row.
 * Type is sized for the portrait floor (1.9% of 3840 = 73px ink).
 */

export const agentRuntimeFrame916Schema = agentRuntimeFrameSchema;
export type AgentRuntimeFrame916Props = z.infer<typeof agentRuntimeFrame916Schema>;

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;
const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const ramp = (p: number, a: number, b: number) =>
  clamp01(interpolate(p, [a, b], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));

const Box: React.FC<{x:number;y:number;w:number;h:number;label:string;opacity?:number;fs?:number}> =
({ x, y, w, h, label, opacity = 1, fs = 64 }) => (
  <div style={{
    position:'absolute', left:x, top:y, width:w, height:h,
    border:`4px solid ${CLAUDE.INK}`, borderRadius:14, background:CLAUDE.CARD,
    display:'flex', alignItems:'center', justifyContent:'center',
    fontFamily:SANS, fontSize:fs, letterSpacing:2, color:CLAUDE.INK,
    textAlign:'center', padding:14, boxSizing:'border-box', opacity,
  }}>{label}</div>
);

export const AgentRuntimeFrame916: React.FC<AgentRuntimeFrame916Props> = ({
  phase, modelLabel, frameLabel, inLabel, outLabel, executorLabel, ports, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = clamp01(frame / Math.max(1, durationInFrames));

  const spark = (
    <div style={{
      position:'absolute', left:SAFE916.x, top:1700, width:SAFE916.w,
      display:'flex', alignItems:'center', gap:16,
      fontFamily:SERIF, fontSize:68, color:CLAUDE.INK,
      opacity: ramp(p, 0.04, 0.16),
    }}>
      <span style={{color:CLAUDE.SPARK, fontSize:72}}>✻</span>
      <span>{sparkLine}</span>
    </div>
  );

  if (phase === 'wrap') {
    const seal    = ramp(p, 0.18, 0.30);
    const frameIn = ramp(p, 0.40, 0.58);
    const portsIn = ramp(p, 0.62, 0.80);

    const FX = 80,  FY = 300, FW = 920, FH = 760;    // runtime frame
    const MX = 190, MY = 540, MW = 700, MH = 300;    // model box
    const cx = MX + MW / 2;

    // arrows run vertically in portrait
    const inFrom = interpolate(seal, [0,1], [200, 470]);
    const outTo  = interpolate(seal, [0,1], [1180, 910]);

    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
        <svg width={1080} height={1920} style={{position:'absolute', inset:0}}>
          <line x1={cx} y1={inFrom} x2={cx} y2={MY - 18} stroke={CLAUDE.INK} strokeWidth={5}/>
          <polygon points={`${cx},${MY-14} ${cx-18},${MY-48} ${cx+18},${MY-48}`} fill={CLAUDE.INK}/>
          <line x1={cx} y1={MY+MH+18} x2={cx} y2={outTo} stroke={CLAUDE.INK} strokeWidth={5}/>
          <polygon points={`${cx},${outTo} ${cx-18},${outTo-34} ${cx+18},${outTo-34}`} fill={CLAUDE.INK}/>
          <rect x={FX} y={FY} width={FW} height={FH} rx={18} fill="none"
                stroke={CLAUDE.SPARK} strokeWidth={7}
                strokeDasharray={2*(FW+FH)} strokeDashoffset={(1-frameIn)*2*(FW+FH)}/>
        </svg>

        <Box x={MX} y={MY} w={MW} h={MH} label={modelLabel} fs={64}/>

        <div style={{position:'absolute', left:SAFE916.x, top:200, width:SAFE916.w,
          textAlign:'center', fontFamily:SANS, fontSize:56, color:CLAUDE.INK_SOFT,
          opacity: 1 - seal*0.55}}>{inLabel}</div>
        <div style={{position:'absolute', left:SAFE916.x, top:1185, width:SAFE916.w,
          textAlign:'center', fontFamily:SANS, fontSize:56, color:CLAUDE.INK_SOFT,
          opacity: 1 - seal*0.55}}>{outLabel}</div>

        <div style={{position:'absolute', left:FX+28, top:FY-78,
          fontFamily:SANS, fontSize:58, letterSpacing:4, color:CLAUDE.INK,
          opacity:frameIn}}>{frameLabel}</div>

        {/* ports stack vertically — a row would not fit the portrait width */}
        {ports.slice(0,3).map((t,i) => (
          <div key={t} style={{
            position:'absolute', left:270, top:1320 + i*120, width:540, height:100,
            borderRadius:50, border:`3px solid ${CLAUDE.BORDER}`, background:CLAUDE.FOOTER,
            display:'flex', alignItems:'center', justifyContent:'center',
            fontFamily:SANS, fontSize:58, color:CLAUDE.INK_SOFT,
            opacity: ramp(p, 0.62 + i*0.05, 0.76 + i*0.05),
            transform:`translateY(${(1-portsIn)*14}px)`,
          }}>{t}</div>
        ))}
        {spark}
      </AbsoluteFill>
    );
  }

  // ── blind: vertical stack, model top → runtime → executor bottom ─────────
  const directIn = ramp(p, 0.04, 0.14);
  const strike   = ramp(p, 0.16, 0.30);
  const legal    = ramp(p, 0.36, 0.68);
  const dim      = ramp(p, 0.62, 0.80);

  const BX = 180, BW = 720;
  const MY = 260, RY = 700, EY = 1140, BH = 260;
  const cx = BX + BW / 2;
  const leg = (i:number) => clamp01((legal - i*0.25)/0.25);

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <svg width={1080} height={1920} style={{position:'absolute', inset:0}}>
        {/* the direct route the model does not have — down the left gutter */}
        <path d={`M ${BX} ${MY+BH/2} Q 70 ${(MY+EY)/2} ${BX} ${EY+BH/2}`}
              fill="none" stroke={CLAUDE.GHOST} strokeWidth={5} strokeDasharray="16 14"
              opacity={directIn*(1-strike*0.45)}/>
        {strike > 0 && (
          <line x1={60} y1={(MY+EY)/2 + 120} x2={210} y2={(MY+EY)/2 - 40}
                stroke={CLAUDE.SPARK} strokeWidth={10}
                strokeDasharray={230} strokeDashoffset={(1-strike)*230}/>
        )}
        {/* legal path down the right side and back */}
        <line x1={cx+140} y1={MY+BH} x2={cx+140} y2={MY+BH + (RY-MY-BH)*leg(0)}
              stroke={CLAUDE.INK} strokeWidth={6} opacity={leg(0)}/>
        <line x1={cx+140} y1={RY+BH} x2={cx+140} y2={RY+BH + (EY-RY-BH)*leg(1)}
              stroke={CLAUDE.INK} strokeWidth={6} opacity={leg(1)}/>
        <line x1={cx-140} y1={EY} x2={cx-140} y2={EY - (EY-RY-BH)*leg(2)}
              stroke={CLAUDE.INK} strokeWidth={6} opacity={leg(2)}/>
        <line x1={cx-140} y1={RY} x2={cx-140} y2={RY - (RY-MY-BH)*leg(3)}
              stroke={CLAUDE.INK} strokeWidth={6} opacity={leg(3)}/>
      </svg>

      <Box x={BX} y={MY} w={BW} h={BH} label={modelLabel}   fs={58} opacity={1-dim*0.62}/>
      <Box x={BX} y={RY} w={BW} h={BH} label={frameLabel}   fs={58}/>
      <Box x={BX} y={EY} w={BW} h={BH} label={executorLabel} fs={58}/>

      <div style={{position:'absolute', left:BX, top:MY+BH+18, width:BW, textAlign:'center',
        fontFamily:SANS, fontSize:52, letterSpacing:2, color:CLAUDE.GHOST, opacity:dim}}>
        never observed
      </div>
      {spark}
    </AbsoluteFill>
  );
};
