import React from 'react';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { MONO, SANS, SERIF, Stage, clamp, ease, remap, useGeo, useP } from './ReelKit';

/**
 * ReelFramework — the FRAMEWORK beat. Shown BEFORE any example, per the teaching arc:
 * the organizing structure is a graphic the viewer can score a new case against, not
 * a narration delivered after the fact.
 *
 * Four numbered rows are the reusable rubric — moves, axes, steps, whichever the reel
 * needs. ONE of them is load-bearing (`accentIndex`), so it takes the reel's single
 * terracotta accent and a rule that draws under it at the end.
 *
 * `receipt` is the optional "and here is where it is proven" slot: a short mono
 * pointer (a table number, a section) so the framework is not four assertions. A row
 * with no receipt renders exactly as before.
 *
 * PROVENANCE: promoted from `VqaFourMoves.tsx` when the BLIP reel needed the same
 * beat with a different accent row and per-row receipts. VqaFourMoves.tsx is now a
 * re-export shim; its props omit `receipt` and default `accentIndex` to 3, so that
 * reel renders identically.
 *
 * Responsive: 4 numbered rows down the long axis in both orientations (a 4-wide row on
 * 16:9 would starve each cell of width and force type under the legibility floor), but
 * the detail column drops below the label on 9:16 where width is scarce.
 */
export const reelFrameworkSchema = z.object({
  spark: z.string().default('Four moves, one audit.'),
  heading: z.string().default('The four moves'),
  moves: z.array(z.object({
    label: z.string(),
    detail: z.string(),
    /** Optional: where this row is proven (e.g. "Table 4"). Empty renders nothing. */
    receipt: z.string().default(''),
  })).default([]),
  /** Which row is load-bearing — it takes the beat's ONE terracotta moment. */
  accentIndex: z.number().default(3),
  keepNote: z.string().default('Move 4 is the rubric. Moves 1-3 can be perfect and still answer from memory.'),
  source: z.string().default(''),
  /** Beat length in seconds. calculateMetadata (Root.tsx) turns this into
   *  durationInFrames, and every ramp below is a fraction of p, so the scene
   *  RE-TIMES to the measured audio instead of animating early and freezing. */
  durationS: z.number().default(12),
});
export type ReelFrameworkProps = z.infer<typeof reelFrameworkSchema>;

export const ReelFramework: React.FC<ReelFrameworkProps> = ({
  spark, heading, moves, accentIndex, keepNote, source,
}) => {
  const p = useP();
  const { portrait } = useGeo();
  const head = ease(remap(p, 0.02, 0.12, 0, 1));
  const row = (i: number) => ease(remap(p, 0.14 + i * 0.11, 0.32 + i * 0.11, 0, 1));
  const ruleW = ease(remap(p, 0.68, 0.88, 0, 1));
  const noteIn = ease(remap(p, 0.76, 0.94, 0, 1));

  return (
    <Stage spark={spark} source={source}>
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: portrait ? 22 : 16, minHeight: 0 }}>
        <div style={{
          fontFamily: SERIF, fontSize: portrait ? 62 : 66, fontWeight: 700, color: CLAUDE.INK,
          opacity: head, flex: '0 0 auto',
        }}>{heading}</div>

        <div style={{
          flex: '1 1 auto', minHeight: 0, display: 'flex', flexDirection: 'column',
          // PORTRAIT: auto-height rows distributed by the container. Stretched rows
          // (`flex: 1`) gave each row ~375px for ~120px of content, and the slack fell
          // BETWEEN the detail line and the receipt — which parked every receipt just
          // above the NEXT axis's label. A receipt that attaches to the wrong claim is
          // worse than no receipt. Landscape rows stretch happily; only portrait changes.
          justifyContent: portrait ? 'space-between' : 'stretch',
          gap: portrait ? 16 : 12,
        }}>
          {moves.slice(0, 4).map((m, i) => {
            const o = clamp(row(i), 0, 1);
            const audit = i === accentIndex;
            const receipt = m.receipt ? (
              <div style={{
                fontFamily: MONO, fontSize: portrait ? 25 : 26, color: audit ? CLAUDE.SEND : CLAUDE.GHOST,
                flex: '0 0 auto', whiteSpace: 'nowrap', letterSpacing: 0.4,
              }}>{m.receipt}</div>
            ) : null;
            return (
              <div key={m.label} style={{
                flex: portrait ? '0 0 auto' : 1, minHeight: 0, display: 'flex',
                flexDirection: portrait ? 'column' : 'row',
                alignItems: portrait ? 'stretch' : 'center',
                gap: portrait ? 8 : 26,
                opacity: o,
                // vertical, NOT horizontal: a full-width row sliding in from the left
                // crosses the title-safe edge mid-entrance (GATE V edge-bleed BLOCKER).
                transform: `translateY(${(1 - o) * 12}px)`,
                borderTop: `2px solid ${CLAUDE.BORDER}`,
                paddingTop: portrait ? 14 : 8,
              }}>
                <div style={{
                  display: 'flex', alignItems: 'center', gap: 22, flex: '0 0 auto',
                  // in portrait the receipt rides the label line, so it sits beside the
                  // axis it proves instead of drifting toward the following one
                  justifyContent: portrait ? 'space-between' : 'flex-start',
                }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 22, minWidth: 0 }}>
                    <div style={{
                      fontFamily: MONO, fontSize: 30, fontWeight: 700,
                      color: audit ? CLAUDE.CARD : CLAUDE.INK_SOFT,
                      background: audit ? CLAUDE.SPARK : CLAUDE.PILL,
                      width: 54, height: 54, borderRadius: 12, flex: '0 0 auto',
                      display: 'flex', alignItems: 'center', justifyContent: 'center',
                    }}>{i + 1}</div>
                    <div style={{
                      fontFamily: SANS, fontSize: portrait ? 40 : 44, fontWeight: 700,
                      color: audit ? CLAUDE.SPARK : CLAUDE.INK, letterSpacing: 0.5,
                      width: portrait ? 'auto' : 300,
                    }}>{m.label}</div>
                  </div>
                  {portrait ? receipt : null}
                </div>
                <div style={{
                  fontFamily: SANS, fontSize: portrait ? 30 : 32, color: CLAUDE.INK_SOFT,
                  lineHeight: 1.3, flex: '1 1 auto', minWidth: 0,
                }}>{m.detail}</div>
                {portrait ? null : receipt}
              </div>
            );
          })}
        </div>

        {/* the accent rule + the one sentence that makes move 4 the rubric */}
        <div style={{ flex: '0 0 auto' }}>
          <div style={{ height: 6, borderRadius: 3, background: CLAUDE.SPARK, width: `${ruleW * 100}%` }} />
          <div style={{
            fontFamily: SERIF, fontSize: portrait ? 34 : 36, color: CLAUDE.INK,
            marginTop: 12, opacity: noteIn, lineHeight: 1.28,
          }}>{keepNote}</div>
        </div>
      </div>
    </Stage>
  );
};
