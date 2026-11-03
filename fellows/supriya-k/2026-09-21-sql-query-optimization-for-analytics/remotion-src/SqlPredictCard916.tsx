/**
 * SqlPredictCard916 — portrait (9:16) variant of B05's predict card.
 *
 * No library `PredictCard916` exists (checked Root.tsx: absent), so this is a
 * reel-local portrait author, per shorts.py's ONDA CHECK: "If no 916
 * composition exists, the beat is flagged: add the composition to Root.tsx."
 *
 * RE-BAND (not a scale-down): the landscape card sits in the upper-middle of a
 * wide frame. Portrait stacks the three elements down the tall axis — spark at
 * top, question filling the middle third at a much larger size, rule + commit
 * beneath — so the frame is occupied rather than letterboxed.
 *
 * Registered 1080x1920; --scale=2 renders 2160x3840 native. Resolution-
 * independent via scW(W). Pure function of the audio clock.
 *
 * REEL-LOCAL. Register per remotion-src/REGISTER.md.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import { HandleChip } from './ClaudeCodeBeat';
import {clamp, remap, easeOutCubic, BG, INK, ACCENT, MUTE, scW, wrapText} from './sqlDeckKit';

export const sqlPredictCard916Schema = z.object({
  /** Lower-right author handle chip (e.g. "Supriya"). Omitted → no chip. */
  handle: z.string().optional(),
  sparkLine: z.string().default('Commit before the reveal.'),
  question: z.string(),
  commit: z.string().default('commit — the answer is one beat away'),
});
export type SqlPredictCard916Props = z.infer<typeof sqlPredictCard916Schema>;

const Spark: React.FC<{size: number}> = ({size}) => (
  <svg width={size} height={size} viewBox="0 0 24 24">
    {Array.from({length: 8}, (_, i) => (
      <line key={i} x1={12} y1={12}
        x2={12 + Math.cos((i * Math.PI) / 4) * 9}
        y2={12 + Math.sin((i * Math.PI) / 4) * 9}
        stroke={ACCENT} strokeWidth={2} strokeLinecap="round" />
    ))}
  </svg>
);

export const SqlPredictCard916: React.FC<SqlPredictCard916Props> = ({handle, sparkLine, question, commit}) => {
  const frame = useCurrentFrame();
  const {width: W, height: H, durationInFrames} = useVideoConfig();
  const p = clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);
  const S = scW(W);

  const SERIF = "'EB Garamond', Georgia, serif";
  const MONO = "'JetBrains Mono', ui-monospace, monospace";

  const sparkOp = clamp(remap(p, 0.02, 0.10, 0, 1), 0, 1);
  // Question reveals line by line, then the rule draws, then the commit line.
  const qLines = wrapText(question, 24);
  const ruleP = easeOutCubic(clamp(remap(p, 0.46, 0.60, 0, 1), 0, 1));
  const commitOp = clamp(remap(p, 0.60, 0.70, 0, 1), 0, 1);

  const qSize = 74 * S;
  const blockH = qLines.length * qSize * 1.22;
  const qTop = H * 0.30;

  return (
    <AbsoluteFill style={{backgroundColor: BG}}>
      {/* spark line — top band */}
      <div style={{
        position: 'absolute', left: 64 * S, top: 96 * S, right: 64 * S,
        display: 'flex', alignItems: 'center', gap: 16 * S, opacity: sparkOp,
      }}>
        <Spark size={30 * S} />
        <span style={{fontFamily: SERIF, fontSize: 44 * S, color: INK, lineHeight: 1.1}}>
          {sparkLine}
        </span>
      </div>

      {/* the question — the middle band, large */}
      <div style={{
        position: 'absolute', left: 64 * S, right: 64 * S, top: qTop,
        display: 'flex', flexDirection: 'column', gap: 0,
      }}>
        {qLines.map((ln, i) => {
          const st = 0.12 + i * 0.07;
          const op = clamp(remap(p, st, st + 0.09, 0, 1), 0, 1);
          const ty = (1 - op) * 14 * S;
          return (
            <div key={i} style={{
              fontFamily: SERIF, fontSize: qSize, lineHeight: 1.22, color: INK,
              opacity: op, transform: `translateY(${ty}px)`,
            }}>
              {ln}
            </div>
          );
        })}
      </div>

      {/* terracotta rule — draws on */}
      <div style={{
        position: 'absolute', left: 64 * S, top: qTop + blockH + 52 * S,
        width: (W - 128 * S) * 0.46 * ruleP, height: 7 * S,
        background: ACCENT, borderRadius: 4 * S,
      }} />

      {/* the commit instruction */}
      <div style={{
        position: 'absolute', left: 64 * S, right: 64 * S,
        top: qTop + blockH + 104 * S,
        fontFamily: MONO, fontSize: 32 * S, color: MUTE, opacity: commitOp,
      }}>
        {commit}
      </div>
      <HandleChip handle={handle} fontSize={H * (H > W ? 0.016 : 0.024)} right={W * 0.07}
        bottom={H * (H > W ? 0.06 : 0.055)} opacity={0.9} />
    </AbsoluteFill>
  );
};
