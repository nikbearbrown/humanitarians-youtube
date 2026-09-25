import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { claudeCodeBeatSchema } from './ClaudeCodeBeat';

/**
 * ClaudeCodeBeat916 — portrait 9:16 (1080×1920) version of ClaudeCodeBeat.
 *
 * The 916 family had no code beat, so `./art vertical` had nothing to rewire a
 * code beat to and would have fallen back to the landscape composition. The
 * landscape one sizes its type from height (`height * 0.022` = 42px at 1920
 * tall) while the card is only ~930px wide in portrait, so a 40-column source
 * line overflows. Here the type is sized from WIDTH, which is the axis that
 * actually constrains a code block, and the card fills the tall frame.
 *
 * Same schema as ClaudeCodeBeat (shorts.py standing rule #4: a 916 composition
 * must accept the landscape props unchanged).
 */

export const claudeCodeBeat916Schema = claudeCodeBeatSchema;
export type ClaudeCodeBeat916Props = z.infer<typeof claudeCodeBeat916Schema>;

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;
const MONO  = CLAUDE_FONT.mono;
const COMMENT_CLR = '#8B8878';
const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));

export const ClaudeCodeBeat916: React.FC<ClaudeCodeBeat916Props> = ({
  title, code, sparkLine, language,
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();

  const cardIn  = spring({ frame,            fps, config: { damping: 28, stiffness: 140, mass: 0.8 } });
  const sparkIn = spring({ frame: frame - 8, fps, config: { damping: 28, stiffness: 140, mass: 0.8 } });

  const lines = code.split('\n');
  const REVEAL_START = 12;
  const LINE_STRIDE  = 3;

  const filename = title.includes(' — ') ? title.split(' — ')[0].trim() : title;

  // Fit the widest source line to the card, so nothing clips in portrait.
  const pad = 30;
  const cardW = width - width * 0.06 * 2;
  const longest = lines.reduce((m, l) => Math.max(m, l.length), 1);
  const fitted = (cardW - pad * 2) / (longest * 0.6);
  const codeSize = clamp(fitted, 20, 38);

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>
      <div style={{
        position: 'absolute',
        left: width * 0.06,
        right: width * 0.06,
        top: height * 0.14,
        bottom: height * 0.16,
        background: CLAUDE.CARD,
        border: `1px solid ${CLAUDE.BORDER}`,
        borderRadius: 18,
        boxShadow: '0 8px 32px rgba(61,57,41,0.10)',
        overflow: 'hidden',
        transform: `translateY(${(1 - clamp(cardIn, 0, 1)) * 18}px)`,
        opacity: clamp(cardIn, 0, 1),
      }}>
        <div style={{
          display: 'flex',
          alignItems: 'center',
          gap: 10,
          padding: '20px 26px',
          background: CLAUDE.PAGE,
          borderBottom: `1px solid ${CLAUDE.BORDER}`,
        }}>
          {[CLAUDE.SPARK, CLAUDE.BORDER, CLAUDE.BORDER].map((c, i) => (
            <div key={i} style={{ width: 15, height: 15, borderRadius: '50%', background: c }} />
          ))}
          <span style={{
            marginLeft: 12, fontFamily: MONO, fontSize: 24,
            color: CLAUDE.INK_SOFT, letterSpacing: '0.02em',
          }}>
            {filename}
          </span>
          <span style={{
            marginLeft: 'auto', fontFamily: SANS, fontSize: 18, fontWeight: 600,
            color: CLAUDE.SPARK, letterSpacing: 2, textTransform: 'uppercase' as const,
          }}>
            {language}
          </span>
        </div>

        <pre style={{
          margin: 0,
          padding: `34px ${pad}px`,
          fontFamily: MONO,
          fontSize: codeSize,
          lineHeight: 1.8,
          textAlign: 'left',
          overflow: 'hidden',
        }}>
          {lines.map((line, i) => {
            const start = REVEAL_START + i * LINE_STRIDE;
            const op = clamp(interpolate(frame, [start, start + 5], [0, 1]), 0, 1);
            const ty = interpolate(frame, [start, start + 7], [6, 0], {
              extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
            });
            const isComment = line.trimStart().startsWith('#');
            return (
              <div key={i} style={{
                opacity: op,
                transform: `translateY(${ty}px)`,
                whiteSpace: 'pre' as const,
                color: isComment ? COMMENT_CLR : CLAUDE.INK,
              }}>
                {line || '​'}
              </div>
            );
          })}
        </pre>
      </div>

      <div style={{
        position: 'absolute',
        left: width * 0.06,
        right: width * 0.06,
        bottom: height * 0.07,
        display: 'flex',
        alignItems: 'center',
        opacity: clamp(sparkIn, 0, 1),
        transform: `translateY(${(1 - clamp(sparkIn, 0, 1)) * 8}px)`,
      }}>
        <span style={{
          flex: 1, fontFamily: SERIF, fontSize: 36, fontStyle: 'italic', color: CLAUDE.INK,
        }}>
          {sparkLine}
        </span>
      </div>
    </AbsoluteFill>
  );
};
