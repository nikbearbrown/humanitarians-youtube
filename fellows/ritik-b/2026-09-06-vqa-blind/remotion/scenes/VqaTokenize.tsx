import React from 'react';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { MONO, SANS, SERIF, SceneGlyph, VqaStage, clamp, ease, remap, useGeo, useP } from './VqaKit';

/**
 * VqaTokenize — MOVE 1. A transformer only eats sequences, so both inputs are cut
 * into tokens of the same width and concatenated into one sequence.
 *
 * Three bands down the long axis in both orientations:
 *   A  the image lane — the worked-example scene, sliced into a patch grid, the
 *      patches lifting out as a strip of vectors
 *   B  the text lane — the question splitting into subword chips
 *   C  the merged sequence — one bar, two tints, so the viewer SEES that pixels and
 *      words have become the same kind of thing
 *
 * The patch arithmetic on screen is derivable, not asserted: 224 / 16 = 14 per side,
 * 14 x 14 = 196 patch tokens.
 */
export const vqaTokenizeSchema = z.object({
  spark: z.string().default('One currency: tokens.'),
  imageCaption: z.string().default('224 x 224 px  ·  16 x 16 patches  ·  14 x 14 = 196 patch tokens'),
  question: z.string().default('What color is the umbrella?'),
  textTokens: z.array(z.string()).default(['what', 'color', 'is', 'the', 'umb', '##rella', '?']),
  textCaption: z.string().default('subword tokens  ·  embedded to the SAME width as a patch vector'),
  mergedLabel: z.string().default('one sequence  ·  [CLS] + text tokens + [SEP] + patch tokens'),
  source: z.string().default(''),
  /** Beat length in seconds. calculateMetadata (Root.tsx) turns this into
   *  durationInFrames, and every ramp below is a fraction of p, so the scene
   *  RE-TIMES to the measured audio instead of animating early and freezing. */
  durationS: z.number().default(12),
});
export type VqaTokenizeProps = z.infer<typeof vqaTokenizeSchema>;

const GRID = 14;

export const VqaTokenize: React.FC<VqaTokenizeProps> = ({
  spark, imageCaption, question, textTokens, textCaption, mergedLabel, source,
}) => {
  const p = useP();
  const { portrait, safe } = useGeo();

  const imgIn = ease(remap(p, 0.03, 0.14, 0, 1));
  const gridDraw = ease(remap(p, 0.12, 0.34, 0, 1));   // grid lines sweep across
  const patchIn = (i: number) => ease(remap(p, 0.30 + i * 0.012, 0.44 + i * 0.012, 0, 1));
  const qIn = ease(remap(p, 0.40, 0.50, 0, 1));
  const chipIn = (i: number) => ease(remap(p, 0.48 + i * 0.022, 0.60 + i * 0.022, 0, 1));
  const mergeIn = ease(remap(p, 0.66, 0.94, 0, 1));

  const bandGap = portrait ? 26 : 16;
  // The image band is sized FROM the safe box, not from a magic number: portrait gets
  // ~40% of its (narrow) width, landscape ~20% of its (wide) width. Both land near the
  // largest square that still leaves the token strip room to read.
  const glyphS = Math.round(portrait ? safe.w * 0.40 : safe.w * 0.20);
  const PATCH_STRIP = portrait ? 14 : 18;   // 196 bars would be mush; portrait fits fewer

  return (
    <VqaStage spark={spark} source={source}>
      <div style={{
        flex: 1, display: 'flex', flexDirection: 'column',
        justifyContent: 'space-between', gap: bandGap, minHeight: 0,
      }}>

        {/* ── BAND A · the image lane ─────────────────────────────── */}
        <div style={{ flex: '0 0 auto', width: '100%', minWidth: 0, display: 'flex', flexDirection: 'column', gap: 10 }}>
          <Lane label="IMAGE" />
          <div style={{
            display: 'flex', alignItems: 'center', gap: portrait ? 16 : 30,
            flex: '0 0 auto', width: '100%', minWidth: 0,
          }}>
            <div style={{ position: 'relative', width: glyphS, height: glyphS, flex: '0 0 auto', opacity: imgIn }}>
              <SceneGlyph umbrella={CLAUDE.SPARK} w={glyphS} h={glyphS} />
              {/* the patch grid, drawn on */}
              <svg width={glyphS} height={glyphS} style={{ position: 'absolute', inset: 0 }}>
                {Array.from({ length: GRID - 1 }, (_, i) => {
                  const t = (i + 1) / GRID;
                  const on = clamp(remap(gridDraw, t * 0.9, t * 0.9 + 0.16, 0, 1), 0, 1);
                  return (
                    <g key={i} opacity={on * 0.75}>
                      <line x1={t * glyphS} y1={0} x2={t * glyphS} y2={glyphS} stroke={CLAUDE.INK} strokeWidth={1} />
                      <line x1={0} y1={t * glyphS} x2={glyphS} y2={t * glyphS} stroke={CLAUDE.INK} strokeWidth={1} />
                    </g>
                  );
                })}
              </svg>
            </div>
            <Arrow o={gridDraw} />
            {/* the patches, lifted out as a strip of column vectors */}
            <div style={{ display: 'flex', gap: 6, alignItems: 'flex-end', flex: '1 1 auto', minWidth: 0, overflow: 'hidden' }}>
              {Array.from({ length: PATCH_STRIP }, (_, i) => {
                const o = clamp(patchIn(i), 0, 1);
                const hh = Math.round(glyphS * (0.30 + ((i * 37) % 5) * 0.055));  // deterministic vector "values"
                return (
                  <div key={i} style={{
                    flex: '1 1 0', minWidth: 5,
                    maxWidth: Math.round(glyphS * (portrait ? 0.075 : 0.09)),
                    height: hh, borderRadius: 5,
                    background: i === 8 ? CLAUDE.SPARK : CLAUDE.GHOST,
                    opacity: o, transform: `translateY(${(1 - o) * 16}px)`,
                  }} />
                );
              })}
              <div style={{
                fontFamily: MONO, fontSize: 26, color: CLAUDE.INK_SOFT, marginLeft: 10,
                opacity: clamp(patchIn(PATCH_STRIP - 1), 0, 1), whiteSpace: 'nowrap',
                flex: '0 0 auto',
              }}>… 196</div>
            </div>
          </div>
          <Caption text={imageCaption} o={gridDraw} />
        </div>

        {/* ── BAND B · the text lane ──────────────────────────────── */}
        <div style={{ flex: '0 0 auto', width: '100%', minWidth: 0, display: 'flex', flexDirection: 'column', gap: 10 }}>
          <Lane label="QUESTION" />
          <div style={{
            display: 'flex', alignItems: 'center', gap: portrait ? 14 : 26,
            flexDirection: portrait ? 'column' : 'row', alignSelf: 'stretch',
          }}>
            <div style={{
              fontFamily: SERIF, fontSize: portrait ? 40 : 44, color: CLAUDE.INK,
              opacity: qIn, flex: '0 0 auto', whiteSpace: 'nowrap',
            }}>{question}</div>
            {portrait ? null : <Arrow o={qIn} />}
            <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap', flex: '1 1 auto', minWidth: 0 }}>
              {textTokens.map((t, i) => {
                const o = clamp(chipIn(i), 0, 1);
                return (
                  <div key={`${t}-${i}`} style={{
                    fontFamily: MONO, fontSize: 27,
                    color: t === 'color' ? CLAUDE.CARD : CLAUDE.INK,
                    background: t === 'color' ? CLAUDE.SPARK : CLAUDE.PILL,
                    border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 8,
                    padding: '6px 12px', opacity: o,
                    transform: `translateY(${(1 - o) * 10}px)`,
                  }}>{t}</div>
                );
              })}
            </div>
          </div>
          <Caption text={textCaption} o={clamp(chipIn(textTokens.length - 1), 0, 1)} />
        </div>

        {/* ── BAND C · the merged sequence ────────────────────────── */}
        <div style={{ flex: '0 0 auto', width: '100%', minWidth: 0, display: 'flex', flexDirection: 'column', gap: 8 }}>
          <div style={{ display: 'flex', gap: 3, height: portrait ? 52 : 44, overflow: 'hidden' }}>
            {Array.from({ length: 44 }, (_, i) => {
              const isText = i < 9;
              const on = clamp(remap(mergeIn, i / 44 * 0.82, i / 44 * 0.82 + 0.18, 0, 1), 0, 1);
              return (
                <div key={i} style={{
                  flex: 1, borderRadius: 4, opacity: on,
                  background: isText ? CLAUDE.INK : CLAUDE.GHOST,
                }} />
              );
            })}
          </div>
          <Caption text={mergedLabel} o={mergeIn} />
        </div>
      </div>
    </VqaStage>
  );
};

const Lane: React.FC<{ label: string }> = ({ label }) => (
  <div style={{
    fontFamily: SANS, fontSize: 25, fontWeight: 700, letterSpacing: 3.4,
    color: CLAUDE.SPARK, flex: '0 0 auto',
  }}>{label}</div>
);

const Caption: React.FC<{ text: string; o: number }> = ({ text, o }) => (
  <div style={{
    fontFamily: SANS, fontSize: 27, color: CLAUDE.INK_SOFT, opacity: clamp(o, 0, 1),
    flex: '0 0 auto', lineHeight: 1.28,
  }}>{text}</div>
);

const Arrow: React.FC<{ o: number }> = ({ o }) => (
  <svg width={54} height={26} viewBox="0 0 54 26" style={{ flex: '0 0 auto', opacity: clamp(o, 0, 1) }}>
    <line x1={2} y1={13} x2={40} y2={13} stroke={CLAUDE.INK_SOFT} strokeWidth={3} />
    <path d="M 38 5 L 52 13 L 38 21 Z" fill={CLAUDE.INK_SOFT} />
  </svg>
);
