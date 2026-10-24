import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { SAFE916 } from '../tokens/layout';
import { permissionGateSchema } from './PermissionGate';

/**
 * PermissionGate916 — native portrait (1080×1920), NOT a crop.
 *
 * Reflow R1 (rotate the axis): the landscape gate is a vertical boundary with
 * requests travelling left→right. Portrait turns the gate HORIZONTAL and the
 * requests fall downward into the protected zone, which reads naturally on a
 * phone. The allowed request lands inside the zone; the destructive one stops
 * on the line. Modes stack as a vertical list.
 */

export const permissionGate916Schema = permissionGateSchema;
export type PermissionGate916Props = z.infer<typeof permissionGate916Schema>;

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;
const MONO  = CLAUDE_FONT.mono;
const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const ramp = (p: number, a: number, b: number) =>
  clamp01(interpolate(p, [a, b], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));

const GATE_Y = 760;

const Chip: React.FC<{x:number;y:number;text:string;danger?:boolean}> = ({x,y,text,danger}) => (
  <div style={{
    position:'absolute', left:x, top:y, height:112, maxWidth:900,
    padding:'0 34px', borderRadius:12,
    border:`4px solid ${danger ? CLAUDE.SPARK : CLAUDE.INK}`, background:CLAUDE.CARD,
    display:'flex', alignItems:'center', justifyContent:'center',
    fontFamily:MONO, fontSize:50, color:CLAUDE.INK, whiteSpace:'nowrap',
  }}>{text}</div>
);

export const PermissionGate916: React.FC<PermissionGate916Props> = ({
  allowedExample, action, verdict, systemLabel, modes, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = clamp01(frame / Math.max(1, durationInFrames));

  const allowTravel = ramp(p, 0.08, 0.30);
  const blockTravel = ramp(p, 0.34, 0.50);
  const gateShut    = ramp(p, 0.48, 0.58);
  const verdictIn   = ramp(p, 0.58, 0.68);
  const modesIn     = ramp(p, 0.70, 0.86);

  const allowY = interpolate(allowTravel, [0,1], [180, 880]);   // crosses into the zone
  const blockY = interpolate(blockTravel, [0,1], [180, GATE_Y - 170]); // stops short

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      {/* protected zone below the gate */}
      <div style={{
        position:'absolute', left:SAFE916.x, top:GATE_Y, width:SAFE916.w, height:560,
        background:CLAUDE.FOOTER, opacity:0.75, borderRadius:14,
      }}/>
      <div style={{
        position:'absolute', left:SAFE916.x + 30, top:GATE_Y + 36,
        fontFamily:SANS, fontSize:52, letterSpacing:4, color:CLAUDE.INK_SOFT,
      }}>{systemLabel}</div>

      <svg width={1080} height={1920} style={{position:'absolute', inset:0}}>
        <line x1={SAFE916.x} y1={GATE_Y} x2={SAFE916.r} y2={GATE_Y}
              stroke={CLAUDE.INK_SOFT} strokeWidth={5} strokeDasharray="18 14"/>
        {/* the gate closes from both ends toward the middle */}
        <rect x={SAFE916.x} y={GATE_Y-11} width={gateShut*(SAFE916.w/2)} height={22}
              fill={CLAUDE.SPARK} opacity={gateShut}/>
        <rect x={SAFE916.r - gateShut*(SAFE916.w/2)} y={GATE_Y-11}
              width={gateShut*(SAFE916.w/2)} height={22}
              fill={CLAUDE.SPARK} opacity={gateShut}/>
      </svg>

      <Chip x={120} y={allowY} text={allowedExample}/>
      <Chip x={300} y={blockY} text={action} danger/>

      <div style={{
        position:'absolute', left:SAFE916.x, top:GATE_Y - 300, width:SAFE916.w,
        fontFamily:SANS, fontSize:54, letterSpacing:2, color:CLAUDE.INK,
        borderLeft:`8px solid ${CLAUDE.SPARK}`, paddingLeft:22,
        opacity:verdictIn,
      }}>{verdict}</div>

      {modes.map((m,i) => (
        <div key={m} style={{
          position:'absolute', left:170, top:1300 + i*124, width:740, height:104,
          borderRadius:52, border:`3px solid ${CLAUDE.BORDER}`, background:CLAUDE.FOOTER,
          display:'flex', alignItems:'center', justifyContent:'center',
          fontFamily:SANS, fontSize:54, color:CLAUDE.INK_SOFT,
          opacity: ramp(p, 0.70 + i*0.05, 0.82 + i*0.05),
          transform:`translateY(${(1-modesIn)*12}px)`,
        }}>{m}</div>
      ))}

      <div style={{
        position:'absolute', left:SAFE916.x, top:1680, width:SAFE916.w,
        display:'flex', alignItems:'center', gap:16,
        fontFamily:SERIF, fontSize:66, color:CLAUDE.INK,
        opacity: ramp(p, 0.04, 0.16),
      }}>
        <span style={{color:CLAUDE.SPARK, fontSize:70}}>✻</span>
        <span>{sparkLine}</span>
      </div>
    </AbsoluteFill>
  );
};
