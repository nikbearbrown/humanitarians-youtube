import React from 'react';
import { Img, staticFile } from 'remotion';
import { CLAUDE } from '../../tokens/claude';
import { HAI_TYPE, SPARK_TEXT } from '../../lib/cueKit';
import { RECS } from './recsData';

export { Chip } from '../pitch/pitchKit';
export { PhoneBaseline, LandBaseline, Stat } from '../shazam/shzKit';
export { Caps } from '../tempo/tmpKit';
export { RECS, SPARK_TEXT };

/**
 * recsKit — shared drawing for "How Spotify Picks Songs."
 *
 * Every number drawn is a column of `recsData.ts`, GENERATED from a real run of recs.py: a made-up music service
 * (1,600 songs in 8 Western genres, 3,000 listeners) and an implicit-feedback ALS recommender. Nothing here is
 * Spotify's data. The taste map is every song's learned vector projected to two dimensions.
 */

/** One muted hue per genre, readable on the cream page. */
export const GENRE_COL: Record<string, string> = {
  pop: '#C0563A', rock: '#7A5C3E', indie: '#A08A2E', 'hip-hop': '#6B4E9B',
  jazz: '#2F6F8F', country: '#B5793A', electronic: '#3E8E7E', classical: '#8E4A63',
};

/** LOGO LAW: Spotify's mark beside its name. */
export const SpotifyTag: React.FC<{ size: number; label?: string }> = ({ size, label = 'SPOTIFY' }) => (
  <span style={{ display: 'inline-flex', alignItems: 'center', gap: size * 0.45 }}>
    <Img src={staticFile('recs/spotify-01.svg')} style={{ height: size * 1.7, width: size * 1.7 }} />
    <span style={{ fontFamily: HAI_TYPE.sans, fontWeight: 800, fontSize: size, letterSpacing: 1.2, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>{label}</span>
  </span>
);

/** A big number with a caps label at an explicit size (the shared Stat's label is too small on the phone). */
export const BigStat: React.FC<{ value: string; label: string; size: number; lbl: number; accent?: boolean; opacity?: number }> = ({ value, label, size, lbl, accent, opacity = 1 }) => (
  <div style={{ opacity }}>
    <div style={{ fontFamily: HAI_TYPE.serif, fontSize: size, fontWeight: 700, lineHeight: 1.0, color: accent ? SPARK_TEXT : CLAUDE.INK }}>{value}</div>
    <div style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.INK_SOFT, marginTop: size * 0.12, whiteSpace: 'nowrap' }}>{label}</div>
  </div>
);

/** A row of song tiles (squares), optionally some dashed (hidden) or accented. */
export const Tiles: React.FC<{ n: number; size: number; gap: number; hidden?: number[]; accent?: number[]; opacity?: number[] }> = ({ n, size, gap, hidden = [], accent = [], opacity }) => (
  <div style={{ display: 'flex', gap }}>
    {Array.from({ length: n }, (_, i) => (
      <div key={i} style={{ width: size, height: size, borderRadius: size * 0.18, opacity: opacity ? opacity[i] : 1,
        background: hidden.includes(i) ? 'transparent' : accent.includes(i) ? SPARK_TEXT : CLAUDE.INK,
        border: hidden.includes(i) ? `${Math.max(2, size * 0.06)}px dashed ${CLAUDE.INK_SOFT}` : 'none', boxSizing: 'border-box' }} />
    ))}
  </div>
);
