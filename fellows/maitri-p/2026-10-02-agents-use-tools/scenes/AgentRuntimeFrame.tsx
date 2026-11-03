import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { SAFE } from '../tokens/layout';

/**
 * AgentRuntimeFrame — the model/runtime relationship, in two phases.
 *
 *   phase "wrap"  — a model alone is a closed box (text in, text out); the
 *                   agent runtime then draws AROUND it and grows tool ports.
 *   phase "blind" — the model never reaches the executor directly: that path
 *                   is struck through, and the legal round trip
 *                   (model → runtime → executor → runtime → model) animates
 *                   while the model dims to show it never observed anything.
 *
 * All motion is a pure function of progress through durationInFrames, so the
 * scene conforms to whatever the measured audio clock turns out to be.
 * Per ILLUSTRATE LAW this is a concept illustration, never UI wallpaper.
 * One terracotta accent per phase (FRAME in "wrap", the STRIKE in "blind").
 */

export const agentRuntimeFrameSchema = z.object({
  phase:         z.enum(['wrap', 'blind']).default('wrap'),
  modelLabel:    z.string().default('LANGUAGE MODEL'),
  frameLabel:    z.string().default('AGENT RUNTIME'),
  inLabel:       z.string().default('text in'),
  outLabel:      z.string().default('text out'),
  executorLabel: z.string().default('FILESYSTEM'),
  ports:         z.array(z.string()).default(['shell', 'files', 'web']),
  sparkLine:     z.string().default('A box, then a frame.'),
  durationSeconds: z.number().optional(),
});
export type AgentRuntimeFrameProps = z.infer<typeof agentRuntimeFrameSchema>;

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;

const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
/** eased 0→1 ramp between two progress fractions */
const ramp = (p: number, a: number, b: number) =>
  clamp01(interpolate(p, [a, b], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));

const Box: React.FC<{
  x: number; y: number; w: number; h: number;
  label: string; opacity?: number; solid?: boolean; fontSize?: number;
}> = ({ x, y, w, h, label, opacity = 1, solid = true, fontSize = 34 }) => (
  <div style={{
    position: 'absolute', left: x, top: y, width: w, height: h,
    border: `${solid ? 3 : 2}px solid ${CLAUDE.INK}`,
    borderRadius: 10,
    background: solid ? CLAUDE.CARD : 'transparent',
    display: 'flex', alignItems: 'center', justifyContent: 'center',
    fontFamily: SANS, fontSize, letterSpacing: 1.5, color: CLAUDE.INK,
    textAlign: 'center', padding: 12, boxSizing: 'border-box',
    opacity,
  }}>{label}</div>
);

export const AgentRuntimeFrame: React.FC<AgentRuntimeFrameProps> = ({
  phase, modelLabel, frameLabel, inLabel, outLabel, executorLabel, ports, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const p = clamp01(frame / Math.max(1, durationInFrames));

  const spark = (
    <div style={{
      position: 'absolute', left: SAFE.x, top: 930, width: SAFE.w,
      display: 'flex', alignItems: 'center', gap: 14,
      fontFamily: SERIF, fontSize: 54, color: CLAUDE.INK,
      opacity: ramp(p, 0.04, 0.16),
    }}>
      <span style={{ color: CLAUDE.SPARK, fontSize: 46 }}>✻</span>
      <span>{sparkLine}</span>
    </div>
  );

  if (phase === 'wrap') {
    // model centred; runtime frame draws around it; ports grow beneath
    const seal    = ramp(p, 0.18, 0.30);   // arrows retract to the box edge
    const frameIn = ramp(p, 0.40, 0.58);   // runtime rectangle draws
    const portsIn = ramp(p, 0.62, 0.80);   // tool ports appear — on the spoken "tools"

    const FX = 260, FY = 150, FW = 1400, FH = 600;      // runtime frame
    const MX = 650, MY = 300, MW = 620, MH = 300;       // model box
    const midY = MY + MH / 2;

    // arrows retract from the wide canvas edges to the model's own edge
    const inFrom  = interpolate(seal, [0, 1], [150, 560]);
    const outTo   = interpolate(seal, [0, 1], [1770, 1360]);

    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
        <svg width={1920} height={1080} style={{ position: 'absolute', inset: 0 }}>
          {/* text in → */}
          <line x1={inFrom} y1={midY} x2={MX - 16} y2={midY}
                stroke={CLAUDE.INK} strokeWidth={4} />
          <polygon points={`${MX - 14},${midY} ${MX - 42},${midY - 14} ${MX - 42},${midY + 14}`}
                   fill={CLAUDE.INK} />
          {/* → text out */}
          <line x1={MX + MW + 16} y1={midY} x2={outTo} y2={midY}
                stroke={CLAUDE.INK} strokeWidth={4} />
          <polygon points={`${outTo},${midY} ${outTo - 28},${midY - 14} ${outTo - 28},${midY + 14}`}
                   fill={CLAUDE.INK} />

          {/* the runtime frame, drawn as a stroke that wipes in */}
          <rect x={FX} y={FY} width={FW} height={FH} rx={16}
                fill="none" stroke={CLAUDE.SPARK} strokeWidth={5}
                strokeDasharray={2 * (FW + FH)}
                strokeDashoffset={(1 - frameIn) * 2 * (FW + FH)} />

          {/* connectors down to the tool ports */}
          {ports.map((_, i) => {
            const cx = 660 + i * 300;
            return (
              <line key={i} x1={cx} y1={FY + FH} x2={cx} y2={800}
                    stroke={CLAUDE.INK_SOFT} strokeWidth={2}
                    opacity={ramp(p, 0.62 + i * 0.04, 0.76 + i * 0.04)} />
            );
          })}
        </svg>

        <Box x={MX} y={MY} w={MW} h={MH} label={modelLabel} fontSize={44} />

        {/* in / out captions */}
        <div style={{
          position: 'absolute', left: 470, top: midY - 86, width: 180, textAlign: 'center' as const,
          fontFamily: SANS, fontSize: 44, color: CLAUDE.INK_SOFT, letterSpacing: 1,
          opacity: 1 - seal * 0.55,
        }}>{inLabel}</div>
        <div style={{
          position: 'absolute', left: 1272, top: midY - 86, width: 180,
          fontFamily: SANS, fontSize: 44, color: CLAUDE.INK_SOFT, letterSpacing: 1,
          textAlign: 'center', opacity: 1 - seal * 0.55,
        }}>{outLabel}</div>

        {/* runtime frame label */}
        <div style={{
          position: 'absolute', left: FX + 24, top: FY - 52,
          fontFamily: SANS, fontSize: 46, letterSpacing: 3,
          color: CLAUDE.INK, opacity: frameIn,
        }}>{frameLabel}</div>

        {/* tool ports */}
        {ports.map((t, i) => (
          <div key={t} style={{
            position: 'absolute', left: 660 + i * 300 - 140, top: 800,
            width: 300, height: 100, borderRadius: 50,
            border: `2px solid ${CLAUDE.BORDER}`, background: CLAUDE.FOOTER,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            fontFamily: SANS, fontSize: 44, color: CLAUDE.INK_SOFT,
            opacity: ramp(p, 0.62 + i * 0.04, 0.76 + i * 0.04),
            transform: `translateY(${(1 - portsIn) * 14}px)`,
          }}>{t}</div>
        ))}

        {spark}
      </AbsoluteFill>
    );
  }

  // ── phase "blind" ──────────────────────────────────────────────────────
  const directIn = ramp(p, 0.04, 0.14);   // the tempting direct line
  const strike   = ramp(p, 0.16, 0.30);   // struck through
  const legal    = ramp(p, 0.36, 0.68);   // the real round trip
  const dim      = ramp(p, 0.62, 0.80);   // the model goes blind

  const MX = 150, MY = 300, MW = 420, MH = 240;     // model
  const RX = 740, RY = 270, RW = 440, RH = 300;     // runtime
  const EX = 1350, EY = 300, EW = 420, EH = 240;    // executor
  const midY = 370;
  const arcY = 600;

  // four legs of the round trip, each taking a quarter of `legal`
  const leg = (i: number) => clamp01((legal - i * 0.25) / 0.25);

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <svg width={1920} height={1080} style={{ position: 'absolute', inset: 0 }}>
        {/* the direct path the model does NOT have */}
        <path d={`M ${MX + MW / 2} ${MY + MH} Q 960 ${arcY + 160} ${EX + EW / 2} ${EY + EH}`}
              fill="none" stroke={CLAUDE.GHOST} strokeWidth={3} strokeDasharray="12 10"
              opacity={directIn * (1 - strike * 0.45)} />
        {strike > 0 && (
          <line x1={862} y1={arcY + 148} x2={1058} y2={arcY + 58}
                stroke={CLAUDE.SPARK} strokeWidth={7}
                strokeDasharray={220} strokeDashoffset={(1 - strike) * 220} />
        )}

        {/* legal round trip: model → runtime → executor → runtime → model */}
        {/* leg 1: model → runtime */}
        <line x1={MX + MW} y1={midY} x2={MX + MW + (RX - MX - MW) * leg(0)} y2={midY}
              stroke={CLAUDE.INK} strokeWidth={4} opacity={leg(0)} />
        {/* leg 2: runtime → executor */}
        <line x1={RX + RW} y1={midY} x2={RX + RW + (EX - RX - RW) * leg(1)} y2={midY}
              stroke={CLAUDE.INK} strokeWidth={4} opacity={leg(1)} />
        {/* leg 3: executor → runtime (return, lower) */}
        <line x1={EX} y1={midY + 120} x2={EX - (EX - RX - RW) * leg(2)} y2={midY + 120}
              stroke={CLAUDE.INK} strokeWidth={4} opacity={leg(2)} />
        {/* leg 4: runtime → model (return, lower) */}
        <line x1={RX} y1={midY + 120} x2={RX - (RX - MX - MW) * leg(3)} y2={midY + 120}
              stroke={CLAUDE.INK} strokeWidth={4} opacity={leg(3)} />
      </svg>

      <Box x={MX} y={MY} w={MW} h={MH} label={modelLabel} fontSize={34}
           opacity={1 - dim * 0.62} />
      <Box x={RX} y={RY} w={RW} h={RH} label={frameLabel} fontSize={34} />
      <Box x={EX} y={EY} w={EW} h={EH} label={executorLabel} fontSize={34} />

      {/* the runtime stays solid while the model fades — the blindness, shown */}
      <div style={{
        position: 'absolute', left: MX, top: MY + MH + 22, width: MW,
        textAlign: 'center', fontFamily: SANS, fontSize: 44, letterSpacing: 1.5,
        color: CLAUDE.GHOST, opacity: dim,
      }}>never observed</div>

      {spark}
    </AbsoluteFill>
  );
};
