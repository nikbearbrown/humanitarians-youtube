import React from 'react';
import { AbsoluteFill, Easing, OffthreadVideo, interpolate, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import { z } from 'zod';
import { C, SANS, SERIF, loadFonts } from './theme';

/**
 * PanelFocus916 — native 9:16 composition of REAL capture footage for the vertical edit.
 * Plays a frame-exact window of a raw 3840x2160 capture at real speed (no retiming) and
 * frames a region of it (tutor panel, cards, passage) that pans/zooms between keyframes,
 * under a short caption band. The caption only labels what is on screen; it adds no claims.
 * Crop rects are in source pixels; height follows the footage region's aspect.
 */
const key = z.object({ t: z.number(), x: z.number(), y: z.number(), w: z.number() });
export const panelFocusSchema = z.object({
  src: z.string(),               // path under public/, e.g. capture/run-portrait-p2.mp4
  startFrom: z.number(),         // seconds into the source
  caption: z.string(),
  keys: z.array(key).min(1),
  srcW: z.number().default(3840),
  srcH: z.number().default(2160),
  // Optional source-x mask [x0, x1]: only this column of the source is shown (e.g. the tutor
  // panel or the sidebar), so page text beside it never appears cut at the frame edge.
  clipX: z.array(z.number()).length(2).optional(),
});
export type PanelFocusProps = z.infer<typeof panelFocusSchema>;

const BAND = 430; // caption band height (comp px, 1080x1920 space)
const MARGIN = 40;

export const PanelFocus916: React.FC<PanelFocusProps> = ({ src, startFrom, caption, keys, srcW, srcH, clipX }) => {
  loadFonts();
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const t = frame / fps;

  const regionW = width - MARGIN * 2;
  const regionH = height - BAND - MARGIN;
  const aspect = regionH / regionW;

  const ease = Easing.inOut(Easing.cubic);
  const pick = (f: 'x' | 'y' | 'w') => {
    if (keys.length === 1) return keys[0][f];
    const ts = keys.map((k) => k.t);
    const vs = keys.map((k) => k[f]);
    return interpolate(t, ts, vs, { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: ease });
  };
  const cw = pick('w');
  const ch = cw * aspect;
  // No clamping: a key may frame WIDER/TALLER than the source ("fit"), e.g. a whole desktop
  // page or content column so no text line is cut by the crop edge. Area outside the
  // source shows the card background. Keys are authored so every text line is either
  // fully inside the frame or fully outside it.
  const cx = pick('x');
  const cy = pick('y');
  const s = regionW / cw;
  const [x0, x1] = clipX ?? [0, srcW];

  return (
    <AbsoluteFill style={{ background: C.PAGE }}>
      <div style={{ position: 'absolute', top: 0, left: 0, width, height: BAND, display: 'flex', flexDirection: 'column', justifyContent: 'center', padding: `0 ${MARGIN + 12}px`, boxSizing: 'border-box' }}>
        <div style={{ width: 64, height: 5, background: C.SPARK, borderRadius: 3, marginBottom: 26 }} />
        <div style={{ fontFamily: SERIF, fontSize: 70, color: C.INK, lineHeight: 1.08 }}>{caption}</div>
        <div style={{ fontFamily: SANS, fontSize: 26, color: C.INK_SOFT, marginTop: 18 }}>Live capture · Cancer textbook tutor</div>
      </div>
      <div style={{ position: 'absolute', left: MARGIN, top: BAND, width: regionW, height: regionH, overflow: 'hidden', borderRadius: 22, border: `2px solid ${C.BORDER}`, background: C.CARD }}>
        <div style={{ position: 'absolute', left: (x0 - cx) * s, top: -cy * s, width: (x1 - x0) * s, height: srcH * s, overflow: 'hidden' }}>
          <div style={{ position: 'absolute', left: -x0 * s, top: 0, width: srcW * s, height: srcH * s }}>
            <OffthreadVideo src={staticFile(src)} startFrom={Math.round(startFrom * fps)} muted style={{ width: '100%', height: '100%' }} />
          </div>
        </div>
      </div>
    </AbsoluteFill>
  );
};
