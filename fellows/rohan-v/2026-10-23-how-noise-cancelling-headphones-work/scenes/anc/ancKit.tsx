import React from 'react';
import { CLAUDE } from '../../tokens/claude';
import { clamp } from '../../lib/cueKit';
import { ANC } from './ancData';

export { Chip, listening } from '../pitch/pitchKit';
export { PhoneBaseline, Stat } from '../shazam/shzKit';
export { Caps } from '../tempo/tmpKit';
export { ANC };

/**
 * ancKit — shared drawing for "How Noise-Cancelling Headphones Work."
 *
 * Everything drawn here is a column of `ancData.ts`, GENERATED from a real run of anc.py: a simulated
 * feedforward headphone (48 kHz; outside mic, 83 µs acoustic lead, 125 µs electronic latency, 128-tap
 * filtered-x LMS, in-ear error mic) on synthetic noise.
 */

/** A waveform as an SVG polyline across w x h, values roughly -1..1, centred. */
export const wavePath = (ys: number[], w: number, h: number, reveal = 1, gain = 1) => {
  const n = Math.max(2, Math.round(ys.length * clamp(reveal, 0, 1)));
  return 'M' + ys.slice(0, n).map((v, i) => `${((i / (ys.length - 1)) * w).toFixed(1)},${(h / 2 - clamp(v * gain, -1, 1) * h * 0.46).toFixed(1)}`).join(' L');
};

/** A labelled waveform strip on a card. */
export const WaveStrip: React.FC<{ ys: number[]; w: number; h: number; color: string; reveal?: number; stroke?: number; opacity?: number; gain?: number }> = ({ ys, w, h, color, reveal = 1, stroke = 4, opacity = 1, gain = 1 }) => (
  <svg width={w} height={h} style={{ display: 'block', overflow: 'visible', opacity }}>
    <rect x={0} y={0} width={w} height={h} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={1.5} />
    <line x1={0} x2={w} y1={h / 2} y2={h / 2} stroke={CLAUDE.BORDER} strokeWidth={2} />
    <path d={wavePath(ys, w, h, reveal, gain)} fill="none" stroke={color} strokeWidth={stroke} />
  </svg>
);
