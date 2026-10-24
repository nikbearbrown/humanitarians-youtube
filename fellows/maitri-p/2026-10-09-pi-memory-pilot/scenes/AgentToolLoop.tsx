import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { SAFE } from '../tokens/layout';

/**
 * AgentToolLoop — the agent's four-move cycle, lit in narration order.
 *
 *   GOAL → DECIDE → TOOL RUNS → OBSERVE ──┐
 *            ↑                            │
 *            └────────────────────────────┘
 *
 * Only TOOL RUNS executes anything; it is the single node that pulses, and
 * the only terracotta moment in the frame. An optional row of port chips
 * fans out beneath to show the tool slot is interchangeable.
 *
 * Motion is a pure function of progress through durationInFrames, so the
 * scene conforms to the measured audio clock. Every cue lands by ~85% —
 * a reveal scheduled later than that is effectively invisible.
 */

export const agentToolLoopSchema = z.object({
  stages:    z.array(z.string()).default(['GOAL', 'DECIDE', 'TOOL RUNS', 'OBSERVE']),
  /** index of the stage that actually executes — gets the accent + pulse */
  executeIndex: z.number().default(2),
  loopBack:  z.boolean().default(true),
  ports:     z.array(z.string()).default([]),
  sparkLine: z.string().default('Four moves, repeated.'),
  durationSeconds: z.number().optional(),
});
export type AgentToolLoopProps = z.infer<typeof agentToolLoopSchema>;

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;

const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const ramp = (p: number, a: number, b: number) =>
  clamp01(interpolate(p, [a, b], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));

export const AgentToolLoop: React.FC<AgentToolLoopProps> = ({
  stages, executeIndex, loopBack, ports, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = clamp01(frame / Math.max(1, durationInFrames));

  // A bare row (no ports, no loop arc) sits at the vertical centre instead of the top.
  const bare = ports.length === 0 && !loopBack;
  const NODE_H = bare ? 230 : 170, NODE_Y = bare ? 350 : 250;
  const GAP = 48;
  const n = stages.length;
  // Four stages fit at 360px; more stages shrink so the row stays inside SAFE (1728px).
  const NODE_W = Math.min(360, Math.floor((1728 - (n - 1) * GAP) / Math.max(1, n)));
  const totalW = n * NODE_W + (n - 1) * GAP;
  const startX = (1920 - totalW) / 2;
  const nodeX = (i: number) => startX + i * (NODE_W + GAP);
  const midY = NODE_Y + NODE_H / 2;

  // each stage lights in narration order, all four done by 0.56
  const lit = (i: number) => ramp(p, 0.04 + i * 0.14, 0.14 + i * 0.14);
  const arcIn   = ramp(p, 0.58, 0.72);
  const portsIn = ramp(p, 0.72, 0.86);

  // the executing node pulses once as it lights
  const pulseT = clamp01((p - (0.04 + executeIndex * 0.14)) / 0.12);
  const pulse  = Math.sin(pulseT * Math.PI) * (pulseT > 0 ? 1 : 0);

  const arcBottom = NODE_Y + NODE_H + 110;

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <svg width={1920} height={1080} style={{ position: 'absolute', inset: 0 }}>
        {/* connectors between stages */}
        {stages.slice(0, -1).map((_, i) => {
          const x1 = nodeX(i) + NODE_W, x2 = nodeX(i + 1);
          const a = lit(i + 1);
          return (
            <g key={i} opacity={a}>
              <line x1={x1 + 6} y1={midY} x2={x1 + 6 + (x2 - x1 - 24) * a} y2={midY}
                    stroke={CLAUDE.INK} strokeWidth={3} />
              <polygon points={`${x2 - 2},${midY} ${x2 - 30},${midY - 14} ${x2 - 30},${midY + 14}`}
                       fill={CLAUDE.INK} opacity={a} />
            </g>
          );
        })}

        {/* loop arc: last stage back to stage 1 (DECIDE) */}
        {loopBack && (
          <g opacity={arcIn}>
            <path
              d={`M ${nodeX(n - 1) + NODE_W / 2} ${NODE_Y + NODE_H}
                  L ${nodeX(n - 1) + NODE_W / 2} ${arcBottom}
                  L ${nodeX(1) + NODE_W / 2} ${arcBottom}
                  L ${nodeX(1) + NODE_W / 2} ${NODE_Y + NODE_H + 6}`}
              fill="none" stroke={CLAUDE.INK_SOFT} strokeWidth={3}
              strokeDasharray={2400} strokeDashoffset={(1 - arcIn) * 2400} />
            <polygon
              points={`${nodeX(1) + NODE_W / 2},${NODE_Y + NODE_H + 4}
                       ${nodeX(1) + NODE_W / 2 - 9},${NODE_Y + NODE_H + 24}
                       ${nodeX(1) + NODE_W / 2 + 9},${NODE_Y + NODE_H + 24}`}
              fill={CLAUDE.INK_SOFT} opacity={arcIn > 0.9 ? 1 : 0} />
          </g>
        )}

        </svg>

      {/* stage nodes */}
      {stages.map((s, i) => {
        const a = lit(i);
        const isExec = i === executeIndex;
        const scale = isExec ? 1 + pulse * 0.045 : 1;
        return (
          <div key={s} style={{
            position: 'absolute', left: nodeX(i), top: NODE_Y,
            width: NODE_W, height: NODE_H,
            border: `${isExec ? 4 : 3}px solid ${isExec && a > 0.5 ? CLAUDE.SPARK : CLAUDE.INK}`,
            borderRadius: 12,
            background: CLAUDE.CARD,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            fontFamily: SANS, fontSize: 38, letterSpacing: 2,
            color: CLAUDE.INK,
            opacity: 0.22 + a * 0.78,
            transform: `scale(${scale})`,
            textAlign: 'center', padding: 10, boxSizing: 'border-box',
          }}>{s}</div>
        );
      })}

      {/* interchangeable ports */}
      {ports.map((t, i) => {
        const cx = 1920 / 2 + (i - (ports.length - 1) / 2) * 268;
        return (
          <div key={t} style={{
            position: 'absolute', left: cx - 134, top: 700,
            width: 268, height: 96, borderRadius: 48,
            border: `2px solid ${CLAUDE.BORDER}`, background: CLAUDE.FOOTER,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            fontFamily: SANS, fontSize: 44, color: CLAUDE.INK_SOFT,
            opacity: ramp(p, 0.72 + i * 0.02, 0.84 + i * 0.02),
            transform: `translateY(${(1 - portsIn) * 12}px)`,
          }}>{t}</div>
        );
      })}

      <div style={{
        position: 'absolute', left: SAFE.x, top: 930, width: SAFE.w,
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
