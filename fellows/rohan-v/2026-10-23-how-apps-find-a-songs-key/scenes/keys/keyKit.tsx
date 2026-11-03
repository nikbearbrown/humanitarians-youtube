import React from 'react';
import { CLAUDE } from '../../tokens/claude';
import { HAI_TYPE, SPARK_TEXT, clamp } from '../../lib/cueKit';
import { KEY } from './keyData';

export { Chip, listening } from '../pitch/pitchKit';
export { PhoneBaseline, Stat } from '../shazam/shzKit';
export { Caps } from '../tempo/tmpKit';
export { KEY };

/**
 * keyKit — shared drawing for "How Apps Find a Song's Key."
 *
 * Everything drawn here is a column of `keyData.ts`, GENERATED from a real run of key.py (STFT chroma,
 * Krumhansl–Kessler profiles, correlation over 24 keys) on 60 synthetic Western songs. The worked example is
 * the test set's own C major pop song; the minor example is its own A minor ballad.
 *
 * Colour: small marks that carry meaning (the winning key, home notes) are SPARK_TEXT, never SPARK.
 */

export const NOTES = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B'];
export const BLACK = [1, 3, 6, 8, 10];
export const keyName = (i: number) => `${NOTES[i % 12]} ${i < 12 ? 'major' : 'minor'}`;

/** Vertical bars for a 12-value profile, with note names under them. */
export const ProfileBars: React.FC<{
  values: number[]; w: number; h: number; size: number; grow?: number; hot?: number[]; color?: string; opacity?: number; labels?: boolean;
}> = ({ values, w, h, size, grow = 1, hot = [], color = CLAUDE.INK_SOFT, opacity = 1, labels = true }) => {
  const max = Math.max(...values);
  const bw = w / values.length;
  return (
    <svg width={w} height={h + (labels ? size * 1.6 : 0)} style={{ overflow: 'visible', display: 'block', opacity }}>
      <line x1={0} x2={w} y1={h} y2={h} stroke={CLAUDE.INK_SOFT} strokeWidth={2} />
      {values.map((v, i) => {
        const bh = (v / max) * h * clamp(grow, 0, 1);
        const isHot = hot.includes(i);
        return (
          <g key={i}>
            <rect x={i * bw + bw * 0.14} y={h - bh} width={bw * 0.72} height={bh} fill={isHot ? SPARK_TEXT : color} />
            {labels ? <text x={i * bw + bw / 2} y={h + size * 1.3} textAnchor="middle" fontFamily={HAI_TYPE.sans} fontWeight={800}
              fontSize={size} fill={isHot ? SPARK_TEXT : CLAUDE.INK_SOFT}>{NOTES[i]}</text> : null}
          </g>
        );
      })}
    </svg>
  );
};

export { SPARK_TEXT };
