import React from 'react';
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { z } from 'zod';
import { C, SANS, SERIF, loadFonts } from './theme';

/**
 * GroundingFlow / GroundingFlow916 — B10, "what connects the answer to the book".
 * Six plain-language steps light in turn with the narration. No implementation terms.
 * Landscape: a left-to-right row. Portrait: a top-to-bottom column (native layout, not a crop).
 * stepTimes are seconds from the start of the beat, matched to the Kokoro take.
 */
export const groundingFlowSchema = z.object({
  sparkLine: z.string().default('What connects the answer to the book'),
  steps: z.array(z.string()).default([
    'Your question',
    'Search the textbook',
    'Relevant passages',
    'Given to the model as context',
    'Answer',
    'You inspect the passages',
  ]),
  stepTimes: z.array(z.number()).default([0.4, 1.6, 3.6, 5.2, 12.6, 14.6]),
  contextLabels: z.array(z.string()).default(['Passages', 'Tutor instructions', 'Recent conversation']),
  contextTime: z.number().default(8.4),
  sideNote: z.string().default("The open page doesn't decide this search"),
  footnote: z.string().default('A place to check. Not a sentence-by-sentence citation.'),
  footnoteTime: z.number().default(15.4),
});
export type GroundingFlowProps = z.infer<typeof groundingFlowSchema>;

const useIn = (t: number) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return spring({ frame: frame - Math.round(t * fps), fps, config: { damping: 30, stiffness: 150, mass: 0.8 } });
};

// Portrait type floor (brutalist.art GATE T §8.1): every text run >= 1.9% of 3840 px = 72 px
// physical = 36 px in this 1080x1920 layout, and an all-lowercase word counts only its
// x-height (Inter ~0.55 em, EB Garamond ~0.42 em measured). So portrait text is Inter 68 and
// the serif title 90. Landscape sizes are unchanged.
const V_SANS = 68;
const V_SERIF = 90;

const Step: React.FC<{ label: string; t: number; index: number; w: number; h: number; fs: number; active: boolean; vertical?: boolean }> = ({
  label, t, index, w, h, fs, active, vertical = false,
}) => {
  const k = useIn(t);
  return (
    <div
      style={{
        width: w, ...(vertical ? { minHeight: h } : { height: h }), borderRadius: 18, background: C.CARD,
        // Ink, not terracotta: brutalist.art's type gate reads terracotta-on-cream pixels as
        // accent text (2.74:1 < 4.5:1) and only exempts scenes listed inside the toolkit.
        border: active ? `4px solid ${C.INK}` : `3px solid ${C.BORDER}`,
        boxShadow: active ? '0 6px 22px rgba(61,57,41,0.16)' : '0 2px 10px rgba(61,57,41,0.06)',
        opacity: interpolate(k, [0, 1], [0.18, 1]),
        transform: `translateY(${interpolate(k, [0, 1], [18, 0])}px)`,
        display: 'flex', boxSizing: 'border-box',
        ...(vertical
          ? { flexDirection: 'row' as const, alignItems: 'center', padding: '12px 30px' }
          : { flexDirection: 'column' as const, justifyContent: 'center', padding: '0 22px' }),
      }}
    >
      {/* Numbers are TEXT, so they stay ink (WCAG 4.5:1 on white); the ink border marks the active step. */}
      {/* Portrait drops the step numbers (the connectors carry the order) so labels get the full card width. */}
      {!vertical && (
        <div style={{ fontFamily: SANS, fontSize: fs * 0.55, color: active ? C.INK : C.INK_SOFT, fontWeight: 500, marginBottom: 6 }}>
          {String(index + 1).padStart(2, '0')}
        </div>
      )}
      <div style={{ fontFamily: vertical ? SANS : SERIF, fontSize: vertical ? V_SANS : fs, color: C.INK, lineHeight: vertical ? 1.1 : 1.12 }}>{label}</div>
    </div>
  );
};

// `skip` (portrait only): leave the first `skip` px of the gap empty so the connector
// starts below content placed there (the step-4 context pills) instead of running behind it.
const Arrow: React.FC<{ t: number; vertical: boolean; len: number; skip?: number }> = ({ t, vertical, len, skip = 0 }) => {
  const k = useIn(t);
  const size = vertical ? { width: 4, height: (len - skip) * k } : { width: len * k, height: 4 };
  return (
    <div style={{
      display: 'flex', alignItems: 'center',
      ...(vertical ? { height: len, flexDirection: 'column' as const, justifyContent: skip ? 'flex-end' : 'center' } : { width: len, justifyContent: 'center' }),
    }}>
      <div style={{ ...size, background: C.INK_SOFT, borderRadius: 2 }} />
    </div>
  );
};

const FlowBody: React.FC<GroundingFlowProps & { vertical: boolean }> = (p) => {
  loadFonts();
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const now = frame / fps;
  const active = p.stepTimes.reduce((a, t, i) => (now >= t ? i : a), -1);
  const ctxK = useIn(p.contextTime);
  const footK = useIn(p.footnoteTime);
  const noteK = useIn(p.stepTimes[1] + 0.6);
  const V = p.vertical;

  const stepW = V ? width * 0.88 : 262;
  const stepH = V ? 100 : 190;
  const fs = V ? V_SANS : 34;
  const gap = V ? 24 : 34;
  // Portrait: the step-4 pills wrap to two rows (~198 px), so that connector gap is longer
  // and its line starts below them.
  const pillGap = 228;
  const pillSkip = 206;

  return (
    <AbsoluteFill style={{ background: C.PAGE, alignItems: 'center', justifyContent: V ? 'flex-start' : 'center' }}>
      <div style={{ position: 'absolute', top: V ? 100 : 84, width: '100%', textAlign: 'center', fontFamily: SERIF, fontSize: V ? V_SERIF : 58, color: C.INK,
        ...(V ? { padding: '0 70px', boxSizing: 'border-box' as const, lineHeight: 1.02 } : {}) }}>
        {p.sparkLine}
      </div>

      <div style={{ display: 'flex', flexDirection: V ? 'column' : 'row', alignItems: 'center', marginTop: V ? 330 : 10 }}>
        {p.steps.map((s, i) => (
          <React.Fragment key={s}>
            {i > 0 && <Arrow t={p.stepTimes[i] - 0.25} vertical={V} len={V && i === 4 ? pillGap : gap} skip={V && i === 4 ? pillSkip : 0} />}
            <div style={{ position: 'relative' }}>
              <Step label={s} t={p.stepTimes[i]} index={i} w={stepW} h={stepH} fs={fs} active={active === i} vertical={V} />
              {i === 1 && (
                <div style={{
                  position: 'absolute', fontFamily: SANS, fontSize: V ? 26 : 19, color: C.INK_SOFT, opacity: noteK,
                  ...(V ? { left: stepW + 18, top: 0, width: width * 0.16, display: 'none' } : { top: stepH + 16, left: 0, width: stepW, textAlign: 'center' }),
                }}>
                  {p.sideNote}
                </div>
              )}
              {i === 3 && (
                <div style={{
                  position: 'absolute', display: 'flex', flexDirection: 'column', gap: 10, opacity: ctxK,
                  transform: `scale(${interpolate(ctxK, [0, 1], [0.94, 1])})`,
                  ...(V ? { top: '100%', marginTop: 12, left: 0, width: stepW, flexDirection: 'row' as const, flexWrap: 'wrap' as const, justifyContent: 'center', rowGap: 10, columnGap: 14 } : { top: stepH + 16, left: 0, width: stepW, alignItems: 'center' }),
                }}>
                  {p.contextLabels.map((c) => (
                    <div key={c} style={{ fontFamily: SANS, fontSize: V ? V_SANS : 19, color: C.INK, background: C.FOOTER, border: `2px solid ${C.BORDER}`, borderRadius: 999, padding: V ? '6px 22px' : '6px 16px', ...(V ? { whiteSpace: 'nowrap' as const } : {}) }}>
                      {c}
                    </div>
                  ))}
                </div>
              )}
            </div>
          </React.Fragment>
        ))}
      </div>

      {/* Portrait omits the side note: at the enforced type floor it cannot share the title-safe
          box with the six steps and the footnote. B05's narration carries the same point. */}
      {false && V && (
        <div style={{ position: 'absolute', top: 296, width: '100%', padding: '0 70px', boxSizing: 'border-box', textAlign: 'center', fontFamily: SANS, fontSize: V_SANS, lineHeight: 1.12, color: C.INK_SOFT, opacity: noteK }}>
          {p.sideNote}
        </div>
      )}
      <div style={{ position: 'absolute', bottom: V ? 280 : 90, width: '100%', textAlign: 'center', fontFamily: SANS, fontSize: V ? V_SANS : 26, color: C.INK_SOFT, opacity: footK,
        ...(V ? { padding: '0 70px', boxSizing: 'border-box' as const, lineHeight: 1.12 } : {}) }}>
        {p.footnote}
      </div>
    </AbsoluteFill>
  );
};

export const GroundingFlow: React.FC<GroundingFlowProps> = (p) => <FlowBody {...p} vertical={false} />;
export const GroundingFlow916: React.FC<GroundingFlowProps> = (p) => <FlowBody {...p} vertical />;
