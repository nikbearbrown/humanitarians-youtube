/**
 * VqaKit.tsx — shared primitives for the "Visual Question Answering, Blind?" reel.
 *
 * WHY A LOCAL KIT: illustrations/kit.tsx is landscape-only (its SparkLine sits at
 * top:44, which is OUTSIDE the 9:16 title-safe inset of y=96 and would trip GATE V's
 * edge-bleed BLOCKER on a portrait render). This reel ships in BOTH orientations from
 * one component set, so the stage has to be orientation-aware.
 *
 * THE ONE GEOMETRY FACT THIS KIT IS BUILT ON:
 *   landscape SAFE   = 1728 x 972   (long axis horizontal)
 *   portrait  SAFE916 =  972 x 1728 (long axis vertical)
 * The SHORT axis is 972 in both. So a px type scale chosen once reads identically
 * in both orientations, and only the LAYOUT DIRECTION has to flip. Every scene here
 * therefore keeps one set of font sizes and switches `flexDirection` on `portrait`.
 *
 * Time: exactly one clock, useP() -> p in [0,1] across the beat. No wall-clock, no
 * state, no CSS transitions — seeking to any frame renders identically (Remotion's
 * determinism contract, same as illustrations/kit.tsx).
 */
import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig } from 'remotion';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';
import { SAFE, SAFE916 } from '../tokens/layout';

export const SERIF = CLAUDE_FONT.serif;
export const SANS = CLAUDE_FONT.ui;
export const MONO = CLAUDE_FONT.mono;
export const STAGE = '#F2F0E9';

export const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));
export const remap = (x: number, x0: number, x1: number, y0: number, y1: number) => {
  const t = clamp((x - x0) / (x1 - x0 || 1), 0, 1);
  return y0 + (y1 - y0) * t;
};
export const ease = (t: number) => 1 - Math.pow(1 - clamp(t, 0, 1), 3);

/** The single clock. p in [0,1] across the beat. */
export const useP = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  return clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);
};

/** Orientation + the title-safe box for whichever canvas we are on. */
export const useGeo = () => {
  const { width, height } = useVideoConfig();
  const portrait = height > width;
  const safe = portrait ? SAFE916 : SAFE;
  return { W: width, H: height, portrait, safe };
};

export const Spark: React.FC<{ size?: number; color?: string }> = ({ size = 30, color = CLAUDE.SPARK }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" style={{ display: 'block', flex: '0 0 auto' }}>
    {Array.from({ length: 8 }, (_, i) => (
      <line key={i} x1={12} y1={12}
        x2={12 + 10 * Math.cos((i * Math.PI) / 4 + 0.2)}
        y2={12 + 10 * Math.sin((i * Math.PI) / 4 + 0.2)}
        stroke={color} strokeWidth={3.2} strokeLinecap="round" />
    ))}
  </svg>
);

/**
 * VqaStage — cream ground, SPARK-LINE LAW header, the illustration, and a footer
 * that carries the source (left) and the LOGO LAW channel bug (right). Every band
 * lives inside the title-safe box, so nothing here can trip GATE V's edge-bleed
 * BLOCKER in either orientation.
 *
 * `source` is the "no source, no verdict" slot: any beat that puts a published
 * number on screen passes its citation here and it renders under the artwork.
 */
export const VqaStage: React.FC<{
  spark: string;
  source?: string;
  channel?: string;
  children: React.ReactNode;
}> = ({ spark, source = '', channel = '@HumanitariansAI', children }) => {
  const { portrait, safe } = useGeo();
  const p = useP();
  const headIn = ease(remap(p, 0, 0.06, 0, 1));
  const footIn = ease(remap(p, 0.05, 0.14, 0, 1));
  return (
    <AbsoluteFill style={{ background: STAGE }}>
      <div style={{
        position: 'absolute', left: safe.x, top: safe.y, width: safe.w, height: safe.h,
        display: 'flex', flexDirection: 'column',
      }}>
        {/* SPARK-LINE LAW — spark + one short serif line, never a lonely asterisk */}
        <div style={{
          flex: '0 0 auto', display: 'flex', alignItems: 'center', justifyContent: 'center',
          gap: 16, opacity: headIn, paddingBottom: portrait ? 26 : 14,
        }}>
          <Spark size={30} />
          <div style={{ fontFamily: SERIF, fontSize: 40, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>{spark}</div>
        </div>

        {/* The illustration owns everything between the header and the footer.
            `overflow: hidden` is a STRUCTURAL GUARD, not a style choice: GATE V treats any
            ink outside the title-safe inset as a BLOCKER, and a single content-sized flex
            row is enough to push a strip of bars past the edge. Clipping here means a
            layout bug shows up as truncated content (visible, fixable) instead of as
            edge-bleed on a 4K master. `minWidth: 0` lets flex children actually shrink. */}
        <div style={{
          flex: '1 1 auto', minHeight: 0, minWidth: 0, position: 'relative',
          display: 'flex', overflow: 'hidden',
        }}>
          {children}
        </div>

        {/* footer: the citation, and the channel bug (LOGO LAW — wordmark, since
            this toolkit ships no HAI logo file) */}
        <div style={{
          flex: '0 0 auto', display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between',
          gap: 24, opacity: footIn, paddingTop: portrait ? 22 : 12,
        }}>
          <div style={{
            fontFamily: MONO, fontSize: 24, color: CLAUDE.INK_SOFT, lineHeight: 1.35,
            maxWidth: portrait ? safe.w : safe.w * 0.78, overflow: 'hidden',
          }}>{source}</div>
          <div style={{
            fontFamily: SERIF, fontSize: 28, color: CLAUDE.INK_SOFT, opacity: 0.55, whiteSpace: 'nowrap',
          }}>{channel}</div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

/** A raised white card in the fidelity skin — the house container for a labelled block. */
export const Card: React.FC<{
  children: React.ReactNode;
  accent?: boolean;
  style?: React.CSSProperties;
}> = ({ children, accent = false, style }) => (
  <div style={{
    background: CLAUDE.CARD, border: `3px solid ${accent ? CLAUDE.SPARK : CLAUDE.BORDER}`,
    borderRadius: 20, position: 'relative', overflow: 'hidden', ...style,
  }}>
    <div style={{ position: 'absolute', left: 0, right: 0, top: 0, height: 8, background: accent ? CLAUDE.SPARK : CLAUDE.PILL }} />
    {children}
  </div>
);

/**
 * SceneGlyph — the reel's worked example, drawn (never a lifted photo, per
 * REBUILD LAW): a flat-vector street scene whose umbrella is the one attribute the
 * question asks about. B03 patchifies it, B04 attends to it, B07 shows its mirror
 * with the umbrella recoloured. `umbrella` is the answer the pixels support. Labels go
 * in HTML beside the glyph, never inside the stretched viewBox.
 */
export const SceneGlyph: React.FC<{
  umbrella: string;
  w: number;
  h: number;
  reveal?: number;
}> = ({ umbrella, w, h, reveal = 1 }) => {
  return (
    <svg width={w} height={h} viewBox="0 0 100 100" preserveAspectRatio="none" style={{ display: 'block', borderRadius: 8 }}>
      <rect x={0} y={0} width={100} height={100} fill="#CFC6AE" />
      <rect x={0} y={62} width={100} height={38} fill="#B0A488" />
      {/* building silhouettes — context the question does not ask about */}
      <rect x={6} y={26} width={17} height={36} fill="#968A6E" />
      <rect x={26} y={16} width={14} height={46} fill="#847860" />
      <rect x={78} y={22} width={16} height={40} fill="#968A6E" />
      {/* the person */}
      <rect x={52} y={54} width={4} height={22} rx={1.6} fill={CLAUDE.INK} />
      <circle cx={54} cy={49} r={4.2} fill={CLAUDE.INK} />
      {/* the umbrella — the answer-bearing region */}
      <g opacity={clamp(reveal, 0, 1)}>
        <path d="M 36 40 A 18 15 0 0 1 72 40 Z" fill={umbrella} />
        <rect x={53.2} y={40} width={1.8} height={16} fill={CLAUDE.INK} />
      </g>
      <rect x={0} y={0} width={100} height={100} fill="none" stroke={CLAUDE.BORDER} strokeWidth={1.4} />
    </svg>
  );
};
