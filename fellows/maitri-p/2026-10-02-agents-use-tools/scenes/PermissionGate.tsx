import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { SAFE } from '../tokens/layout';

/**
 * PermissionGate — tool access is not handed over whole.
 *
 * A benign request crosses the boundary untouched; a destructive one travels
 * the same lane, hits the gate, and stops dead with APPROVAL REQUIRED. The
 * three containment modes (scoped / sandboxed / human approval) stack beneath.
 *
 * The blocked request is the single terracotta moment — the allowed one is
 * deliberately unremarkable, because "nothing happened" is the point.
 * Motion is a pure function of progress; every cue lands by ~86%.
 */

export const permissionGateSchema = z.object({
  allowedExample: z.string().default('read ./runtime/scripts'),
  action:         z.string().default('rm -rf /'),
  verdict:        z.string().default('BLOCKED — approval required'),
  systemLabel:    z.string().default('YOUR SYSTEM'),
  modes:          z.array(z.string()).default(['scoped', 'sandboxed', 'human approval']),
  sparkLine:      z.string().default('Never handed over whole.'),
  durationSeconds: z.number().optional(),
});
export type PermissionGateProps = z.infer<typeof permissionGateSchema>;

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;
const MONO  = CLAUDE_FONT.mono;

const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const ramp = (p: number, a: number, b: number) =>
  clamp01(interpolate(p, [a, b], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));

const GATE_X = 1080;
const LANE_A = 250;   // allowed lane
const LANE_B = 500;   // blocked lane

const Chip: React.FC<{ x: number; y: number; text: string; danger?: boolean; opacity: number }> =
({ x, y, text, danger, opacity }) => (
  <div style={{
    position: 'absolute', left: x, top: y, height: 92,
    padding: '0 34px', borderRadius: 10,
    border: `3px solid ${danger ? CLAUDE.SPARK : CLAUDE.INK}`,
    background: CLAUDE.CARD,
    display: 'flex', alignItems: 'center',
    fontFamily: MONO, fontSize: 44,
    color: CLAUDE.INK,
    whiteSpace: 'nowrap', opacity,
  }}>{text}</div>
);

export const PermissionGate: React.FC<PermissionGateProps> = ({
  allowedExample, action, verdict, systemLabel, modes, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = clamp01(frame / Math.max(1, durationInFrames));

  const allowTravel = ramp(p, 0.08, 0.30);   // benign request crosses
  const blockTravel = ramp(p, 0.34, 0.50);   // destructive approaches
  const gateShut    = ramp(p, 0.48, 0.58);   // gate closes
  const verdictIn   = ramp(p, 0.58, 0.68);   // APPROVAL REQUIRED
  const modesIn     = ramp(p, 0.70, 0.86);   // containment modes

  // allowed chip travels past the gate; blocked chip stops short of it
  const allowX = interpolate(allowTravel, [0, 1], [150, 1120]);
  const blockX = interpolate(blockTravel, [0, 1], [150, GATE_X - 430]);

  const gateTop = 150, gateBot = 770;
  const gateMid = (gateTop + gateBot) / 2;

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <svg width={1920} height={1080} style={{ position: 'absolute', inset: 0 }}>
        {/* the boundary */}
        <line x1={GATE_X} y1={gateTop} x2={GATE_X} y2={gateBot}
              stroke={CLAUDE.INK_SOFT} strokeWidth={3} strokeDasharray="14 12" />

        {/* the gate leaves closing across the blocked lane */}
        <rect x={GATE_X - 9} y={gateMid - 10} width={18}
              height={gateShut * (gateBot - gateMid + 10)}
              fill={CLAUDE.SPARK} opacity={gateShut} />
        <rect x={GATE_X - 9} y={gateMid + 10 - gateShut * (gateMid - gateTop + 10)} width={18}
              height={gateShut * (gateMid - gateTop + 10)}
              fill={CLAUDE.SPARK} opacity={gateShut} />

        {/* lane guides */}
        <line x1={120} y1={LANE_A + 39} x2={GATE_X - 20} y2={LANE_A + 39}
              stroke={CLAUDE.BORDER} strokeWidth={2} />
        <line x1={120} y1={LANE_B + 39} x2={GATE_X - 20} y2={LANE_B + 39}
              stroke={CLAUDE.BORDER} strokeWidth={2} />

        {/* the stop mark where the blocked request dies */}
        {gateShut > 0.2 && (
          <g opacity={gateShut}>
            <line x1={GATE_X - 42} y1={LANE_B + 14} x2={GATE_X - 42} y2={LANE_B + 64}
                  stroke={CLAUDE.SPARK} strokeWidth={6} />
          </g>
        )}
      </svg>

      {/* the two requests */}
      <Chip x={allowX} y={LANE_A} text={allowedExample} opacity={allowTravel > 0 ? 1 : 0} />
      <Chip x={blockX} y={LANE_B} text={action} danger opacity={blockTravel > 0 ? 1 : 0} />

      {/* what sits behind the boundary — a tinted zone, not an opaque card,
           so a request that legitimately crosses stays visible inside it */}
      <div style={{
        position: 'absolute', left: GATE_X, top: 150, width: 1788 - GATE_X, height: 620,
        background: CLAUDE.FOOTER, opacity: 0.75, borderRadius: 12,
      }} />
      <div style={{
        position: 'absolute', left: GATE_X + 40, top: 176,
        fontFamily: SANS, fontSize: 44, letterSpacing: 3, color: CLAUDE.INK_SOFT,
      }}>{systemLabel}</div>

      {/* verdict on the blocked request */}
      <div style={{
        position: 'absolute', left: 150, top: LANE_B + 110,
        fontFamily: SANS, fontSize: 38, letterSpacing: 2, color: CLAUDE.INK,
        borderLeft: `6px solid ${CLAUDE.SPARK}`, paddingLeft: 18,
        opacity: verdictIn,
      }}>{verdict}</div>

      {/* containment modes */}
      {modes.map((m, i) => (
        <div key={m} style={{
          position: 'absolute', left: 150 + i * 428, top: 806,
          width: 390, height: 98, borderRadius: 49,
          border: `2px solid ${CLAUDE.BORDER}`, background: CLAUDE.FOOTER,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          fontFamily: SANS, fontSize: 44, color: CLAUDE.INK_SOFT,
          opacity: ramp(p, 0.70 + i * 0.04, 0.82 + i * 0.04),
          transform: `translateY(${(1 - modesIn) * 12}px)`,
        }}>{m}</div>
      ))}

      <div style={{
        position: 'absolute', left: SAFE.x, top: 940, width: SAFE.w,
        display: 'flex', alignItems: 'center', gap: 14,
        fontFamily: SERIF, fontSize: 54, color: CLAUDE.INK,
        opacity: ramp(p, 0.04, 0.16),
      }}>
        <span style={{ color: CLAUDE.SPARK, fontSize: 46 }}>✻</span>
        <span>{sparkLine}</span>
      </div>
    </AbsoluteFill>
  );
};
