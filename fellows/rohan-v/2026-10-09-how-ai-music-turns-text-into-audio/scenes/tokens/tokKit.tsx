import React from 'react';
import { CLAUDE } from '../../tokens/claude';
import { HAI_TYPE, SPARK_TEXT, clamp, op } from '../../lib/cueKit';
import { TOK } from './tokData';

export { Chip, listening } from '../pitch/pitchKit';
export { Stat, PhoneBaseline } from '../shazam/shzKit';
export { TOK };

/**
 * tokKit — shared drawing for "How AI Music Generators Turn Text Into Audio."
 *
 * Everything drawn here is a field of `tokData.ts`, GENERATED from a real run of codec.py
 * (MDCT frames, residual vector quantization with 12 k-means codebooks of 1,024 entries, a
 * trigram next-token model) on synthetic music. Spectral shapes are the run's own frame and
 * codebook vectors (log magnitude, pooled to 64 bands); token numbers are the run's tokens.
 *
 * Colour: data lines and small marks are SPARK_TEXT, never SPARK (GATE T §8.3).
 */

export const fmt = (n: number) => n.toLocaleString('en-US');

/** A 64-band log-magnitude shape as an SVG path (filled or line), over [lo, hi] in log10 units. */
export const shapePath = (v: number[], w: number, h: number, lo: number, hi: number, fill = false, reveal = 1) => {
  const n = v.length;
  const m = Math.max(1, Math.round(n * clamp(reveal, 0, 1)));
  let d = '';
  for (let i = 0; i < m; i++) {
    const x = (i / (n - 1)) * w;
    const y = h - clamp((v[i] - lo) / (hi - lo), 0, 1) * h;
    d += `${i === 0 ? 'M' : 'L'} ${x.toFixed(1)} ${y.toFixed(1)} `;
  }
  if (fill) d += `L ${((m - 1) / (n - 1)) * w} ${h} L 0 ${h} Z`;
  return d;
};

/** The shape range used by every spectral panel, so frames, entries and stages compare directly. */
export const SHAPE_LO = Math.min(...TOK.frame.orig) - 0.2;
export const SHAPE_HI = Math.max(...TOK.frame.orig) + 0.15;

/** A token: its number in a monospace box. */
export const TokenBox: React.FC<{ n: number | string; size: number; accent?: boolean; ghost?: boolean; opacity?: number }> = ({ n, size, accent, ghost, opacity = 1 }) => (
  <span style={{ display: 'inline-flex', alignItems: 'center', justifyContent: 'center', minWidth: size * 2.6, height: size * 1.7,
    boxSizing: 'border-box', borderRadius: size * 0.3, fontFamily: HAI_TYPE.mono, fontSize: size, fontWeight: 700,
    color: ghost ? CLAUDE.INK_SOFT : accent ? CLAUDE.CARD : CLAUDE.INK, background: accent ? SPARK_TEXT : CLAUDE.CARD,
    border: `2px ${ghost ? 'dashed' : 'solid'} ${accent ? SPARK_TEXT : ghost ? CLAUDE.GHOST : CLAUDE.INK}`, opacity, padding: `0 ${size * 0.25}px` }}>{n}</span>
);

export const Label: React.FC<{ text: string; size: number; color?: string; opacity?: number; style?: React.CSSProperties }> = ({ text, size, color, opacity = 1, style }) => (
  <div style={{ fontFamily: HAI_TYPE.sans, fontSize: size, fontWeight: 800, letterSpacing: 1.2, color: color ?? CLAUDE.INK_SOFT, opacity: op(opacity), whiteSpace: 'nowrap', ...style }}>{text}</div>
);
