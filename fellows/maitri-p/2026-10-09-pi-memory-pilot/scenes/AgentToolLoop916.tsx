import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { SAFE916 } from '../tokens/layout';
import { agentToolLoopSchema } from './AgentToolLoop';

/**
 * AgentToolLoop916 — native portrait (1080×1920), NOT a crop.
 *
 * Reflow R4 (serialize): the landscape version runs the four stages across a
 * row with a loop arc beneath. Portrait stacks them vertically and returns the
 * loop up the LEFT gutter, so the cycle still reads as a cycle on a phone.
 * Ports become a 2-column grid rather than a six-wide row.
 */

export const agentToolLoop916Schema = agentToolLoopSchema;
export type AgentToolLoop916Props = z.infer<typeof agentToolLoop916Schema>;

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;
const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const ramp = (p: number, a: number, b: number) =>
  clamp01(interpolate(p, [a, b], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));

export const AgentToolLoop916: React.FC<AgentToolLoop916Props> = ({
  stages, executeIndex, loopBack, ports, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = clamp01(frame / Math.max(1, durationInFrames));

  const NX = 250, NW = 700, NH = 165, TOP = 210, GAP = 52;
  const n = stages.length;
  const nodeY = (i: number) => TOP + i * (NH + GAP);
  const cx = NX + NW / 2;

  const lit     = (i: number) => ramp(p, 0.04 + i * 0.14, 0.14 + i * 0.14);
  const arcIn   = ramp(p, 0.58, 0.72);
  const portsIn = ramp(p, 0.72, 0.86);

  const pulseT = clamp01((p - (0.04 + executeIndex * 0.14)) / 0.12);
  const pulse  = Math.sin(pulseT * Math.PI) * (pulseT > 0 ? 1 : 0);

  const lastBottom = nodeY(n - 1) + NH;
  const gutterX = 140;

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <svg width={1080} height={1920} style={{ position: 'absolute', inset: 0 }}>
        {stages.slice(0, -1).map((_, i) => {
          const y1 = nodeY(i) + NH, y2 = nodeY(i + 1);
          const a = lit(i + 1);
          return (
            <g key={i} opacity={a}>
              <line x1={cx} y1={y1 + 6} x2={cx} y2={y1 + 6 + (y2 - y1 - 26) * a}
                    stroke={CLAUDE.INK} strokeWidth={5} />
              <polygon points={`${cx},${y2 - 4} ${cx - 16},${y2 - 30} ${cx + 16},${y2 - 30}`}
                       fill={CLAUDE.INK} opacity={a} />
            </g>
          );
        })}

        {loopBack && (
          <g opacity={arcIn}>
            <path d={`M ${NX} ${lastBottom - NH / 2}
                      L ${gutterX} ${lastBottom - NH / 2}
                      L ${gutterX} ${nodeY(1) + NH / 2}
                      L ${NX - 6} ${nodeY(1) + NH / 2}`}
                  fill="none" stroke={CLAUDE.INK_SOFT} strokeWidth={5}
                  strokeDasharray={2200} strokeDashoffset={(1 - arcIn) * 2200} />
            <polygon points={`${NX - 2},${nodeY(1) + NH / 2}
                              ${NX - 28},${nodeY(1) + NH / 2 - 16}
                              ${NX - 28},${nodeY(1) + NH / 2 + 16}`}
                     fill={CLAUDE.INK_SOFT} opacity={arcIn > 0.9 ? 1 : 0} />
          </g>
        )}
      </svg>

      {stages.map((s, i) => {
        const a = lit(i);
        const isExec = i === executeIndex;
        return (
          <div key={s} style={{
            position: 'absolute', left: NX, top: nodeY(i), width: NW, height: NH,
            border: `${isExec ? 6 : 4}px solid ${isExec && a > 0.5 ? CLAUDE.SPARK : CLAUDE.INK}`,
            borderRadius: 14, background: CLAUDE.CARD,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            fontFamily: SANS, fontSize: 62, letterSpacing: 2, color: CLAUDE.INK,
            opacity: 0.22 + a * 0.78,
            transform: `scale(${isExec ? 1 + pulse * 0.04 : 1})`,
            textAlign: 'center', padding: 12, boxSizing: 'border-box',
          }}>{s}</div>
        );
      })}

      {/* ports as a 2-column grid — six across will not fit 1080 wide */}
      {ports.slice(0, 6).map((t, i) => {
        const col = i % 2, row = Math.floor(i / 2);
        return (
          <div key={t} style={{
            position: 'absolute', left: 70 + col * 480, top: 1280 + row * 118,
            width: 440, height: 98, borderRadius: 49,
            border: `3px solid ${CLAUDE.BORDER}`, background: CLAUDE.FOOTER,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            fontFamily: SANS, fontSize: 54, color: CLAUDE.INK_SOFT,
            opacity: ramp(p, 0.72 + i * 0.015, 0.84 + i * 0.015),
            transform: `translateY(${(1 - portsIn) * 12}px)`,
          }}>{t}</div>
        );
      })}

      <div style={{
        position: 'absolute', left: SAFE916.x, top: 1700, width: SAFE916.w,
        display: 'flex', alignItems: 'center', gap: 16,
        fontFamily: SERIF, fontSize: 68, color: CLAUDE.INK,
        opacity: ramp(p, 0.04, 0.16),
      }}>
        <span style={{ color: CLAUDE.SPARK, fontSize: 72 }}>✻</span>
        <span>{sparkLine}</span>
      </div>
    </AbsoluteFill>
  );
};
