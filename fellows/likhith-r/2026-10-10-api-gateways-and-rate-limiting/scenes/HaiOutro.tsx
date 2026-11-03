/**
 * HaiOutro.tsx — default Humanitarians AI outro card for claude-hai reels, DUAL-ASPECT.
 *
 * Registered as `HaiOutro` (1920×1080 → 3840×2160 at --scale=2) and `HaiOutro916`
 * (1080×1920 → 2160×3840). Title restate + FULL-SIZE HAI mark (LOGO LAW) + Subscribe +
 * handle, with an optional note (e.g. the AI-narration disclosure the fellows guide requires).
 * Not ClaudeTitleOutro: OUTRO-LOCK.md reserves that card for @NikBearBrown.
 *
 * GATE T by construction: the Subscribe pill fill is the darker terracotta #A44A32
 * (white text 5.5:1; outside the #D97757 accent-text detector), all other text is INK on
 * cream, and portrait text is sized for the 9:16 floor (1.9% of 3840px).
 * Motion is a pure function of progress; `durationSeconds` conforms it to the beat's audio.
 */
import React from 'react';
import { AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from './tokens/claude';
import { SAFE, SAFE916 } from './tokens/layout';

const HAI_LOGO = 'logo-outro/humanitarians/humanitarians-logo-1.svg';
const PILL = '#A44A32';

const ramp = (t: number, a: number, b: number) =>
  interpolate(t, [a, b], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
const ease = (x: number) => 1 - Math.pow(1 - x, 3);

export const haiOutroSchema = z.object({
  title: z.string().default('Humanitarians AI.'),
  handle: z.string().default('@HumanitariansAI'),
  note: z.string().default(''),
  titleScale: z.number().default(1),   // manual nudge on top of the length-based fit
  durationSeconds: z.number().optional(),
});
export type HaiOutroProps = z.infer<typeof haiOutroSchema>;

export const haiOutroMeta = ({ props }: { props: Record<string, unknown> }) =>
  ({ durationInFrames: Math.max(30, Math.ceil(((props.durationSeconds as number) ?? 4) * 30)) });

export const HaiOutro: React.FC<HaiOutroProps> = ({ title, handle, note, titleScale }) => {
  const frame = useCurrentFrame();
  const { durationInFrames, width, height } = useVideoConfig();
  const t = frame / Math.max(1, durationInFrames - 1);
  const P = height > width;
  const S = P ? SAFE916 : SAFE;

  const logoIn = ease(ramp(t, 0.02, 0.16));
  const titleIn = ease(ramp(t, 0.12, 0.26));
  const ctaIn = ease(ramp(t, 0.3, 0.44));

  // Length-based fit: short titles grow so the card fills the safe area; long ones wrap.
  const len = Math.max(8, title.length);
  // landscape keeps the title on ONE line (~0.47em per glyph) so logo + title + CTA + note fit the safe height
  const base = P ? Math.min(150, Math.max(104, 2600 / len)) : Math.min(180, Math.max(96, (S.w - 40) / (len * 0.47)));
  const titleSize = base * titleScale;

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, alignItems: 'center', justifyContent: 'center' }}>
      <div style={{
        display: 'flex', flexDirection: 'column', alignItems: 'center', gap: P ? 72 : 40,
        width: S.w, marginTop: P ? -120 : 0,
      }}>
        <Img src={staticFile(HAI_LOGO)} style={{
          height: P ? 520 : 340, opacity: logoIn, transform: `scale(${0.92 + 0.08 * logoIn})`,
        }} />
        <div style={{
          fontFamily: CLAUDE_FONT.serif, fontSize: titleSize, lineHeight: 1.08, color: CLAUDE.INK,
          textAlign: 'center', maxWidth: S.w, opacity: titleIn, transform: `translateY(${(1 - titleIn) * 16}px)`,
        }}>{title}</div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 36, opacity: ctaIn }}>
          <div style={{
            fontFamily: CLAUDE_FONT.ui, fontWeight: 700, fontSize: P ? 50 : 46, color: '#FFFFFF', background: PILL,
            padding: P ? '20px 48px' : '18px 44px', borderRadius: 999, letterSpacing: 2, textTransform: 'uppercase',
          }}>Subscribe</div>
          <div style={{ fontFamily: CLAUDE_FONT.ui, fontSize: P ? 58 : 56, fontWeight: 600, color: CLAUDE.INK }}>{handle}</div>
        </div>
        {note ? (
          <div style={{
            fontFamily: CLAUDE_FONT.ui, fontSize: P ? 70 : 56, lineHeight: 1.15, color: CLAUDE.INK,
            textAlign: 'center', maxWidth: S.w, opacity: ctaIn,
          }}>{note}</div>
        ) : null}
      </div>
    </AbsoluteFill>
  );
};
