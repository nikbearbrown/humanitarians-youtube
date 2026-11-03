import React from 'react';
import { CLAUDE } from '../../tokens/claude';
import { HAI_TYPE, SPARK_TEXT } from '../../lib/cueKit';
import { VOICE } from './voiceData';

export { Chip, listening } from '../pitch/pitchKit';
export { PhoneBaseline, LandBaseline, Stat } from '../shazam/shzKit';
export { Caps } from '../tempo/tmpKit';
export { VOICE, SPARK_TEXT };

/**
 * voiceKit — shared drawing for "How AI Voices Read a Script."
 *
 * Everything drawn here is a column of `voiceData.ts`, GENERATED from a real run of voice.py: the narrator's own
 * G2P step (espeak-ng via kokoro-onnx), run on heteronyms, numbers and our own past mispronunciations. IPA is
 * shown exactly as the step produced it.
 */

/** IPA in a monospace-free serif, on a soft plate so it reads as "sounds", not text. */
export const Ipa: React.FC<{ ipa: string; size: number; color?: string; plate?: boolean; style?: React.CSSProperties }> = ({ ipa, size, color = CLAUDE.INK, plate = true, style }) => (
  <span style={{ fontFamily: HAI_TYPE.serif, fontSize: size, color, background: plate ? CLAUDE.CARD : 'transparent',
    border: plate ? `1.5px solid ${CLAUDE.BORDER}` : 'none', borderRadius: size * 0.2, padding: plate ? `${size * 0.08}px ${size * 0.3}px` : 0,
    whiteSpace: 'nowrap', display: 'inline-block', ...style }}>/{ipa.replace(/\.$/, '')}/</span>
);

/** A small right / wrong mark drawn as a shape (no glyphs: thin check glyphs fail GATE T on the phone). */
export const Mark: React.FC<{ ok: boolean; size: number; opacity?: number }> = ({ ok, size, opacity = 1 }) => (
  <svg width={size} height={size} style={{ display: 'inline-block', verticalAlign: 'middle', opacity, flexShrink: 0 }}>
    <circle cx={size / 2} cy={size / 2} r={size / 2 - 2} fill={ok ? CLAUDE.INK : SPARK_TEXT} />
    {ok ? <path d={`M ${size * 0.28} ${size * 0.52} L ${size * 0.44} ${size * 0.68} L ${size * 0.74} ${size * 0.34}`} fill="none" stroke={CLAUDE.CARD} strokeWidth={size * 0.12} strokeLinecap="round" strokeLinejoin="round" />
      : <path d={`M ${size * 0.32} ${size * 0.32} L ${size * 0.68} ${size * 0.68} M ${size * 0.68} ${size * 0.32} L ${size * 0.32} ${size * 0.68}`} fill="none" stroke={CLAUDE.CARD} strokeWidth={size * 0.12} strokeLinecap="round" />}
  </svg>
);
