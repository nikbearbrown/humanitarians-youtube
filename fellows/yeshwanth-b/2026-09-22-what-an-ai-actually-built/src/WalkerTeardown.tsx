/**
 * WalkerTeardown.tsx — reel-local components for walker-towerdefense-teardown
 * ("It Passed Every Test." — an AI rebuilt a lost game; it compiled, it passed,
 * and it was unplayable twice).
 *
 * GATE L was searched for all four ("a grid of automated test checks turning
 * green", "before and after comparison of numbers speeding up") and returned
 * no renderable match, so these are PUNT-resolved components rather than
 * slates.
 *
 *   WtDamageCollapse  B04 — four cosmetic variants converging on one damage
 *                     path, with the resistance table drawn as an absence.
 *   WtCheckGrid       B05 + B08 — the automated check grid. Same component
 *                     twice: 56 green, then 9 keyboard checks with 5 reverted
 *                     to red. Reusing it is the point — the second run is the
 *                     first run's claim being tested.
 *   WtPacingTable     B10 — the before/after pacing table. The bars re-time
 *                     together on one 3x stamp, because the fix scaled the
 *                     clock rather than the values.
 *   WtThesis          B11 — what machine checks proved, against what only a
 *                     person caught.
 *
 * House rules: cream stage via IlluStage, ONE terracotta moment per beat,
 * everything inside SAFE, motion a pure function of useP().
 */
import React from 'react';
import { z } from 'zod';
import { IlluStage, useP, remap, ease, SERIF, SANS, MONO } from './illustrations/kit';
import { CLAUDE } from './tokens/claude';
import { SAFE916 } from './tokens/layout';

const reveal = (p: number, at: number, span = 0.08) => ease(remap(p, at, at + span, 0, 1));
const GREEN = '#4F7A4A';
const RED = '#A44A32';

// ── WtDamageCollapse ────────────────────────────────────────────────────────

export const wtDamageCollapseSchema = z.object({
  sparkLine: z.string().default('The colours are cosmetic.'),
  variants: z.array(z.string()).default(['Fire', 'Ice', 'Poison', 'Storm']),
  sink: z.string().default('take_damage(amount)'),
  absent: z.string().default('resistance table'),
  caption: z.string().optional(),
});
export type WtDamageCollapseProps = z.infer<typeof wtDamageCollapseSchema>;

export const WtDamageCollapse: React.FC<WtDamageCollapseProps> = ({
  sparkLine, variants, sink, absent, caption,
}) => {
  const p = useP();
  const CHIP_W = 380, CHIP_H = 168, GAP = 44;
  const total = variants.length * CHIP_W + (variants.length - 1) * GAP;
  const x0 = (1920 - total) / 2;
  const chipY = 196;
  const sinkY = 580;
  const sinkW = 900, sinkH = 184;
  const sinkX = (1920 - sinkW) / 2;

  return (
    <IlluStage spark={sparkLine}>
      {variants.map((v, i) => {
        const o = reveal(p, 0.06 + i * 0.05, 0.08);
        const x = x0 + i * (CHIP_W + GAP);
        // all four dim equally at the converge moment: none is special, which
        // is the whole claim of the beat
        const dim = 1 - 0.45 * reveal(p, 0.3, 0.12);
        return (
          <React.Fragment key={v}>
            <div style={{
              position: 'absolute', left: x, top: chipY, width: CHIP_W, height: CHIP_H,
              background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 14,
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              fontFamily: SANS, fontSize: 58, fontWeight: 600, color: CLAUDE.INK,
              opacity: o * dim, transform: `translateY(${(1 - o) * 20}px)`,
            }}>{v}</div>
            {/* converging arrow */}
            <div style={{
              position: 'absolute',
              left: x + CHIP_W / 2, top: chipY + CHIP_H,
              width: 2, height: (sinkY - chipY - CHIP_H) * reveal(p, 0.26 + i * 0.03, 0.1),
              background: CLAUDE.INK_SOFT, opacity: 0.55,
              transformOrigin: 'top',
            }} />
          </React.Fragment>
        );
      })}

      <div style={{
        position: 'absolute', left: sinkX, top: sinkY, width: sinkW, height: sinkH,
        background: CLAUDE.CARD, border: `3px solid ${CLAUDE.SPARK}`, borderRadius: 16,
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        fontFamily: MONO, fontSize: 54, color: CLAUDE.SPARK,
        opacity: reveal(p, 0.34, 0.1),
      }}>{sink}</div>

      {/* the thing that is not there, drawn as an absence and struck out */}
      <div style={{
        position: 'absolute', left: sinkX, top: sinkY + sinkH + 52, width: sinkW, height: 124,
        border: `2px dashed ${CLAUDE.INK_SOFT}`, borderRadius: 14,
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        fontFamily: SANS, fontSize: 46, color: CLAUDE.INK_SOFT,
        opacity: 0.8 * reveal(p, 0.48, 0.1),
      }}>
        {absent}
        <div style={{
          position: 'absolute', left: 40, right: 40, top: '50%', height: 3,
          background: CLAUDE.INK_SOFT,
          transform: `scaleX(${reveal(p, 0.58, 0.1)})`, transformOrigin: 'left',
        }} />
      </div>

      {caption ? (
        <div style={{
          position: 'absolute', left: 130, right: 130, top: 960, textAlign: 'center',
          fontFamily: SERIF, fontSize: 34, fontStyle: 'italic', color: CLAUDE.INK_SOFT,
          opacity: reveal(p, 0.68, 0.1),
        }}>{caption}</div>
      ) : null}
    </IlluStage>
  );
};

// ── WtCheckGrid ─────────────────────────────────────────────────────────────

export const wtCheckGridSchema = z.object({
  sparkLine: z.string().default('Everything green.'),
  suites: z.array(z.object({ label: z.string(), count: z.number() })).default([]),
  /** How many cells flip red, counted from the END of the last suite. */
  failCount: z.number().default(0),
  revertLabel: z.string().optional(),
  caption: z.string().optional(),
});
export type WtCheckGridProps = z.infer<typeof wtCheckGridSchema>;

export const WtCheckGrid: React.FC<WtCheckGridProps> = ({
  sparkLine, suites, failCount, revertLabel, caption,
}) => {
  const p = useP();
  const totalChecks = suites.reduce((a, s) => a + s.count, 0);
  const cols = totalChecks > 20 ? 15 : 5;
  const CELL = totalChecks > 20 ? 92 : 230;
  const PAD = totalChecks > 20 ? 10 : 28;

  // cells are laid out suite by suite, each suite starting a new row block
  let cursor = 0;
  const blocks = suites.map((s) => {
    const start = cursor;
    cursor += s.count;
    return { ...s, start };
  });
  const rowsFor = (n: number) => Math.ceil(n / cols);
  let yCursor = totalChecks > 20 ? 212 : 226;
  const laid: { x: number; y: number; idx: number; suite: number }[] = [];
  const labels: { y: number; text: string; count: number }[] = [];
  // A card panel behind each suite: it groups the cells into a readable unit
  // and stops the grid reading as a scatter of dots on an empty page.
  const panels: { x: number; y: number; w: number; h: number }[] = [];
  const PANEL_PAD = 30;
  blocks.forEach((b, si) => {
    labels.push({ y: yCursor - 46, text: b.label, count: b.count });
    const widest = Math.min(cols, b.count) * (CELL + PAD) - PAD;
    const rows = rowsFor(b.count);
    panels.push({
      x: (1920 - widest) / 2 - PANEL_PAD,
      y: yCursor - PANEL_PAD,
      w: widest + PANEL_PAD * 2,
      h: rows * (CELL + PAD) - PAD + PANEL_PAD * 2,
    });
    for (let i = 0; i < b.count; i++) {
      const r = Math.floor(i / cols), c = i % cols;
      const rowW = Math.min(cols, b.count - r * cols) * (CELL + PAD) - PAD;
      laid.push({ x: (1920 - rowW) / 2 + c * (CELL + PAD), y: yCursor + r * (CELL + PAD), idx: b.start + i, suite: si });
    }
    yCursor += rowsFor(b.count) * (CELL + PAD) + 54;
  });

  const firstFail = totalChecks - failCount;
  // Derived, not fixed: with large cells the old constants put the caption
  // underneath the counter and pushed it past the safe inset.
  const bottomTop = yCursor + 8;
  const counterSize = totalChecks > 20 ? 72 : 64;
  const captionTop = Math.min(bottomTop + counterSize + 40, 972);
  const fillEnd = 0.46;

  return (
    <IlluStage spark={sparkLine}>
      {panels.map((pn, i) => (
        <div key={`panel-${i}`} style={{
          position: 'absolute', left: pn.x, top: pn.y, width: pn.w, height: pn.h,
          background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 18,
          opacity: 0.9 * reveal(p, 0.04, 0.08),
        }} />
      ))}

      {labels.map((l) => (
        <div key={l.text} style={{
          position: 'absolute', left: 0, right: 0, top: l.y, textAlign: 'center',
          fontFamily: SANS, fontSize: 30, fontWeight: 600, letterSpacing: 2,
          textTransform: 'uppercase' as const, color: CLAUDE.INK_SOFT,
          opacity: reveal(p, 0.06, 0.08),
        }}>{l.text} · {l.count}</div>
      ))}

      {laid.map((cell) => {
        const at = 0.08 + (cell.idx / Math.max(1, totalChecks)) * (fillEnd - 0.08);
        const o = reveal(p, at, 0.05);
        const isFail = failCount > 0 && cell.idx >= firstFail;
        // failures only turn red AFTER the revert stamp lands
        const flip = isFail ? reveal(p, 0.56 + (cell.idx - firstFail) * 0.03, 0.06) : 0;
        const bg = isFail && flip > 0.5 ? RED : GREEN;
        return (
          <div key={cell.idx} style={{
            position: 'absolute', left: cell.x, top: cell.y, width: CELL, height: CELL,
            borderRadius: 10, background: bg,
            opacity: o * (isFail ? 0.35 + 0.65 * Math.max(1 - flip, flip) : 1),
            transform: `scale(${0.82 + 0.18 * o})`,
          }} />
        );
      })}

      {/* stamp and counter share one row, so neither can land on the caption */}
      <div style={{
        position: 'absolute', left: 0, right: 0, top: bottomTop,
        display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 40,
      }}>
        {revertLabel ? (
          <span style={{
            fontFamily: SANS, fontSize: 34, fontWeight: 700, letterSpacing: 3,
            textTransform: 'uppercase' as const, color: CLAUDE.CARD, background: RED,
            padding: '12px 28px', borderRadius: 8,
            opacity: reveal(p, 0.48, 0.08),
          }}>{revertLabel}</span>
        ) : null}
        <span style={{
          fontFamily: SANS, fontSize: counterSize, fontWeight: 700,
          color: failCount > 0 ? RED : GREEN, opacity: reveal(p, 0.6, 0.08),
        }}>
          {failCount > 0 ? `${failCount} of ${totalChecks} failed` : `${totalChecks} / ${totalChecks}`}
        </span>
      </div>

      {caption ? (
        <div style={{
          position: 'absolute', left: 160, right: 160, top: captionTop, textAlign: 'center',
          fontFamily: SERIF, fontSize: 34, fontStyle: 'italic', color: CLAUDE.INK_SOFT,
          opacity: reveal(p, 0.7, 0.08),
        }}>{caption}</div>
      ) : null}
    </IlluStage>
  );
};

// ── WtPacingTable ───────────────────────────────────────────────────────────

export const wtPacingTableSchema = z.object({
  sparkLine: z.string().default('Scale the clock.'),
  rows: z.array(z.object({
    measure: z.string(),
    before: z.string(),
    after: z.string(),
    beforeFrac: z.number(),
    afterFrac: z.number(),
    accent: z.boolean().optional(),
  })).default([]),
  stamp: z.string().default('3× CLOCK'),
  caption: z.string().optional(),
});
export type WtPacingTableProps = z.infer<typeof wtPacingTableSchema>;

export const WtPacingTable: React.FC<WtPacingTableProps> = ({
  sparkLine, rows, stamp, caption,
}) => {
  const p = useP();
  const X = 140, W = 1640;
  const ROW_H = 118;
  const Y0 = 232;
  const LABEL_W = 620;
  const BAR_X = X + LABEL_W + 40;
  const BAR_W = 620;
  const VAL_X = BAR_X + BAR_W + 36;
  // one stamp, one re-time: every bar moves on the same trigger because the
  // fix scaled the clock, not the individual values
  const retime = reveal(p, 0.56, 0.16);

  return (
    <IlluStage spark={sparkLine}>
      {rows.map((r, i) => {
        const o = reveal(p, 0.1 + i * 0.05, 0.08);
        const frac = r.beforeFrac + (r.afterFrac - r.beforeFrac) * retime;
        const val = retime > 0.5 ? r.after : r.before;
        const col = r.accent ? CLAUDE.SPARK : CLAUDE.INK;
        const y = Y0 + i * ROW_H;
        return (
          <React.Fragment key={r.measure}>
            <div style={{
              position: 'absolute', left: X, top: y, width: LABEL_W, height: ROW_H - 26,
              display: 'flex', alignItems: 'center',
              fontFamily: SANS, fontSize: 38, color: col, opacity: o,
            }}>{r.measure}</div>
            <div style={{
              position: 'absolute', left: BAR_X, top: y + 22, width: BAR_W, height: 40,
              background: CLAUDE.BORDER, borderRadius: 8, opacity: o * 0.5,
            }} />
            <div style={{
              position: 'absolute', left: BAR_X, top: y + 22, width: BAR_W * frac, height: 40,
              background: r.accent ? CLAUDE.SPARK : CLAUDE.INK_SOFT, borderRadius: 8, opacity: o,
            }} />
            <div style={{
              position: 'absolute', left: VAL_X, top: y, width: 320, height: ROW_H - 26,
              display: 'flex', alignItems: 'center',
              fontFamily: MONO, fontSize: 38, fontWeight: 600, color: col, opacity: o,
            }}>{val}</div>
          </React.Fragment>
        );
      })}

      <div style={{
        position: 'absolute', left: 0, right: 0, top: Y0 + rows.length * ROW_H + 26,
        textAlign: 'center', opacity: reveal(p, 0.54, 0.06),
      }}>
        <span style={{
          fontFamily: SANS, fontSize: 44, fontWeight: 700, letterSpacing: 4,
          color: CLAUDE.CARD, background: CLAUDE.SPARK, padding: '14px 34px', borderRadius: 10,
        }}>{stamp}</span>
      </div>

      {caption ? (
        <div style={{
          position: 'absolute', left: 160, right: 160, top: 978, textAlign: 'center',
          fontFamily: SERIF, fontSize: 34, fontStyle: 'italic', color: CLAUDE.INK_SOFT,
          opacity: reveal(p, 0.84, 0.08),
        }}>{caption}</div>
      ) : null}
    </IlluStage>
  );
};

// ── WtThesis ────────────────────────────────────────────────────────────────

export const wtThesisSchema = z.object({
  leftTitle: z.string().default('What the checks proved'),
  leftItems: z.array(z.string()).default([]),
  rightTitle: z.string().default('What only a person caught'),
  rightItems: z.array(z.string()).default([]),
  thesis: z.string().default('It never played it.'),
  caption: z.string().optional(),
});
export type WtThesisProps = z.infer<typeof wtThesisSchema>;

export const WtThesis: React.FC<WtThesisProps> = ({
  leftTitle, leftItems, rightTitle, rightItems, thesis, caption,
}) => {
  const p = useP();
  const COL_W = 800, GAP = 70;
  const x0 = (1920 - (COL_W * 2 + GAP)) / 2;
  const TOP = 182;

  const column = (title: string, items: string[], x: number, at: number, accent: boolean) => (
    <>
      <div style={{
        position: 'absolute', left: x, top: TOP, width: COL_W,
        fontFamily: SANS, fontSize: 32, fontWeight: 700, letterSpacing: 2,
        textTransform: 'uppercase' as const,
        color: accent ? CLAUDE.SPARK : CLAUDE.INK_SOFT,
        opacity: reveal(p, at, 0.08),
      }}>{title}</div>
      {items.map((it, i) => {
        const o = reveal(p, at + 0.06 + i * 0.05, 0.08);
        return (
          <div key={it} style={{
            position: 'absolute', left: x, top: TOP + 92 + i * 176, width: COL_W, minHeight: 150,
            background: CLAUDE.CARD,
            border: `${accent ? 3 : 2}px solid ${accent ? CLAUDE.SPARK : CLAUDE.BORDER}`,
            borderRadius: 14, padding: '26px 30px', boxSizing: 'border-box',
            fontFamily: SANS, fontSize: 44, lineHeight: 1.22,
            color: CLAUDE.INK, opacity: o, transform: `translateY(${(1 - o) * 18}px)`,
          }}>{it}</div>
        );
      })}
    </>
  );

  return (
    <IlluStage spark="">
      {column(leftTitle, leftItems, x0, 0.1, false)}
      {column(rightTitle, rightItems, x0 + COL_W + GAP, 0.26, true)}
      <div style={{
        position: 'absolute', left: 0, right: 0, top: 826, textAlign: 'center',
        fontFamily: SERIF, fontSize: 94, color: CLAUDE.SPARK,
        opacity: reveal(p, 0.72, 0.1),
      }}>{thesis}</div>
      {caption ? (
        <div style={{
          position: 'absolute', left: 160, right: 160, top: 950, textAlign: 'center',
          fontFamily: SERIF, fontSize: 34, fontStyle: 'italic', color: CLAUDE.INK_SOFT,
          opacity: reveal(p, 0.86, 0.08),
        }}>{caption}</div>
      ) : null}
    </IlluStage>
  );
};

// ── Portrait 9:16 variants ──────────────────────────────────────────────────
// `./art vertical` rewires each beat to <pattern>916 where one is registered,
// which is what makes the vertical cut portrait-NATIVE rather than a crop.
// Same zod schemas as the landscape twins (shorts.py standing rule #4); only
// the layout changes — rows become a tall stack, side-by-side becomes stacked.
//
// IlluStage's own spark sits at y=44, above SAFE916.y (96), so these pass
// spark="" and place their own inside the portrait safe area.

const PSAFE = SAFE916;

const PSpark: React.FC<{ text: string }> = ({ text }) => {
  const p = useP();
  if (!text) return null;
  return (
    <div style={{
      position: 'absolute', top: PSAFE.y + 20, left: PSAFE.x, width: PSAFE.w,
      textAlign: 'center', fontFamily: SERIF, fontSize: 46, color: CLAUDE.INK,
      opacity: remap(p, 0, 0.06, 0, 1),
    }}>{text}</div>
  );
};

const PCaption: React.FC<{ text?: string; top: number; at?: number }> = ({ text, top, at = 0.8 }) => {
  const p = useP();
  if (!text) return null;
  return (
    <div style={{
      position: 'absolute', left: PSAFE.x, width: PSAFE.w, top,
      textAlign: 'center', fontFamily: SERIF, fontSize: 40, fontStyle: 'italic',
      color: CLAUDE.INK_SOFT, lineHeight: 1.3, opacity: reveal(p, at, 0.08),
    }}>{text}</div>
  );
};

export const WtDamageCollapse916: React.FC<WtDamageCollapseProps> = ({
  sparkLine, variants, sink, absent, caption,
}) => {
  const p = useP();
  const CW = 460, CH = 150, GAP = 28;
  const cols = 2;
  const gridW = cols * CW + GAP;
  const x0 = (1080 - gridW) / 2;
  const top = 280;
  const sinkY = 900, sinkH = 190;
  const sinkW = PSAFE.w;

  return (
    <IlluStage spark="">
      <PSpark text={sparkLine} />
      {variants.slice(0, 4).map((v, i) => {
        const o = reveal(p, 0.06 + i * 0.05, 0.08);
        const col = i % cols, rowN = Math.floor(i / cols);
        const dim = 1 - 0.45 * reveal(p, 0.3, 0.12);
        return (
          <React.Fragment key={v}>
            <div style={{
              position: 'absolute', left: x0 + col * (CW + GAP), top: top + rowN * (CH + GAP),
              width: CW, height: CH, background: CLAUDE.CARD,
              border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 16,
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              fontFamily: SANS, fontSize: 58, fontWeight: 600, color: CLAUDE.INK,
              opacity: o * dim, transform: `translateY(${(1 - o) * 18}px)`,
            }}>{v}</div>
          </React.Fragment>
        );
      })}
      {/* one shared trunk: all four resolve to the same place */}
      <div style={{
        position: 'absolute', left: 1080 / 2 - 1, top: top + 2 * CH + GAP + 20,
        width: 3, height: (sinkY - (top + 2 * CH + GAP + 20)) * reveal(p, 0.3, 0.12),
        background: CLAUDE.INK_SOFT, opacity: 0.6,
      }} />
      <div style={{
        position: 'absolute', left: PSAFE.x, top: sinkY, width: sinkW, height: sinkH,
        background: CLAUDE.CARD, border: `3px solid ${CLAUDE.SPARK}`, borderRadius: 18,
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        fontFamily: MONO, fontSize: 52, color: CLAUDE.SPARK, textAlign: 'center',
        opacity: reveal(p, 0.36, 0.1),
      }}>{sink}</div>
      <div style={{
        position: 'absolute', left: PSAFE.x, top: sinkY + sinkH + 56, width: sinkW, height: 150,
        border: `2px dashed ${CLAUDE.INK_SOFT}`, borderRadius: 16,
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        fontFamily: SANS, fontSize: 46, color: CLAUDE.INK_SOFT, textAlign: 'center',
        opacity: 0.8 * reveal(p, 0.5, 0.1),
      }}>
        {absent}
        <div style={{
          position: 'absolute', left: 40, right: 40, top: '50%', height: 3,
          background: CLAUDE.INK_SOFT,
          transform: `scaleX(${reveal(p, 0.6, 0.1)})`, transformOrigin: 'left',
        }} />
      </div>
      <PCaption text={caption} top={sinkY + sinkH + 250} at={0.7} />
    </IlluStage>
  );
};

export const WtCheckGrid916: React.FC<WtCheckGridProps> = ({
  sparkLine, suites, failCount, revertLabel, caption,
}) => {
  const p = useP();
  const total = suites.reduce((a, s) => a + s.count, 0);
  const cols = total > 20 ? 8 : 3;
  const CELL = total > 20 ? 104 : 230;
  const PAD = total > 20 ? 12 : 26;

  let cursor = 0;
  const blocks = suites.map((s) => { const start = cursor; cursor += s.count; return { ...s, start }; });
  let y = 300;
  const laid: { x: number; y: number; idx: number }[] = [];
  const labels: { y: number; text: string; count: number }[] = [];
  const panels: { x: number; y: number; w: number; h: number }[] = [];
  const PP = 24;
  blocks.forEach((b) => {
    labels.push({ y: y - 46, text: b.label, count: b.count });
    const widest = Math.min(cols, b.count) * (CELL + PAD) - PAD;
    const rows = Math.ceil(b.count / cols);
    panels.push({ x: (1080 - widest) / 2 - PP, y: y - PP, w: widest + PP * 2, h: rows * (CELL + PAD) - PAD + PP * 2 });
    for (let i = 0; i < b.count; i++) {
      const r = Math.floor(i / cols), c = i % cols;
      const rowW = Math.min(cols, b.count - r * cols) * (CELL + PAD) - PAD;
      laid.push({ x: (1080 - rowW) / 2 + c * (CELL + PAD), y: y + r * (CELL + PAD), idx: b.start + i });
    }
    y += rows * (CELL + PAD) + 70;
  });
  const firstFail = total - failCount;
  const counterTop = y + (revertLabel ? 84 : 12);

  return (
    <IlluStage spark="">
      <PSpark text={sparkLine} />
      {panels.map((pn, i) => (
        <div key={`p${i}`} style={{
          position: 'absolute', left: pn.x, top: pn.y, width: pn.w, height: pn.h,
          background: CLAUDE.CARD, border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 18,
          opacity: 0.9 * reveal(p, 0.04, 0.08),
        }} />
      ))}
      {labels.map((l) => (
        <div key={l.text} style={{
          position: 'absolute', left: 0, right: 0, top: l.y, textAlign: 'center',
          fontFamily: SANS, fontSize: 32, fontWeight: 600, letterSpacing: 2,
          textTransform: 'uppercase' as const, color: CLAUDE.INK_SOFT,
          opacity: reveal(p, 0.06, 0.08),
        }}>{l.text} · {l.count}</div>
      ))}
      {laid.map((cell) => {
        const at = 0.08 + (cell.idx / Math.max(1, total)) * (0.46 - 0.08);
        const o = reveal(p, at, 0.05);
        const isFail = failCount > 0 && cell.idx >= firstFail;
        const flip = isFail ? reveal(p, 0.56 + (cell.idx - firstFail) * 0.03, 0.06) : 0;
        return (
          <div key={cell.idx} style={{
            position: 'absolute', left: cell.x, top: cell.y, width: CELL, height: CELL,
            borderRadius: 10, background: isFail && flip > 0.5 ? RED : GREEN,
            opacity: o, transform: `scale(${0.82 + 0.18 * o})`,
          }} />
        );
      })}
      {revertLabel ? (
        <div style={{ position: 'absolute', left: 0, right: 0, top: y + 4, textAlign: 'center', opacity: reveal(p, 0.48, 0.08) }}>
          <span style={{
            fontFamily: SANS, fontSize: 38, fontWeight: 700, letterSpacing: 3,
            textTransform: 'uppercase' as const, color: CLAUDE.CARD, background: RED,
            padding: '12px 26px', borderRadius: 8,
          }}>{revertLabel}</span>
        </div>
      ) : null}
      <div style={{
        position: 'absolute', left: 0, right: 0, top: counterTop, textAlign: 'center',
        fontFamily: SANS, fontSize: 78, fontWeight: 700,
        color: failCount > 0 ? RED : GREEN, opacity: reveal(p, 0.6, 0.08),
      }}>
        {failCount > 0 ? `${failCount} of ${total} failed` : `${total} / ${total}`}
      </div>
      <PCaption text={caption} top={Math.min(counterTop + 110, 1660)} at={0.7} />
    </IlluStage>
  );
};

export const WtPacingTable916: React.FC<WtPacingTableProps> = ({
  sparkLine, rows, stamp, caption,
}) => {
  const p = useP();
  const X = PSAFE.x, W = PSAFE.w;
  const ROW_H = 190;
  const Y0 = 260;
  const retime = reveal(p, 0.56, 0.16);

  return (
    <IlluStage spark="">
      <PSpark text={sparkLine} />
      {rows.map((r, i) => {
        const o = reveal(p, 0.1 + i * 0.05, 0.08);
        const frac = r.beforeFrac + (r.afterFrac - r.beforeFrac) * retime;
        const val = retime > 0.5 ? r.after : r.before;
        const col = r.accent ? CLAUDE.SPARK : CLAUDE.INK;
        const y = Y0 + i * ROW_H;
        return (
          <React.Fragment key={r.measure}>
            {/* portrait stacks label above bar instead of three columns */}
            <div style={{
              position: 'absolute', left: X, top: y, width: W - 260,
              fontFamily: SANS, fontSize: 40, color: col, opacity: o, lineHeight: 1.15,
            }}>{r.measure}</div>
            <div style={{
              position: 'absolute', left: X + W - 250, top: y - 4, width: 250,
              textAlign: 'right', fontFamily: MONO, fontSize: 44, fontWeight: 600,
              color: col, opacity: o,
            }}>{val}</div>
            <div style={{
              position: 'absolute', left: X, top: y + 96, width: W, height: 34,
              background: CLAUDE.BORDER, borderRadius: 8, opacity: o * 0.5,
            }} />
            <div style={{
              position: 'absolute', left: X, top: y + 96, width: W * frac, height: 34,
              background: r.accent ? CLAUDE.SPARK : CLAUDE.INK_SOFT, borderRadius: 8, opacity: o,
            }} />
          </React.Fragment>
        );
      })}
      <div style={{
        position: 'absolute', left: 0, right: 0, top: Y0 + rows.length * ROW_H + 30,
        textAlign: 'center', opacity: reveal(p, 0.54, 0.06),
      }}>
        <span style={{
          fontFamily: SANS, fontSize: 48, fontWeight: 700, letterSpacing: 4,
          color: CLAUDE.CARD, background: CLAUDE.SPARK, padding: '14px 32px', borderRadius: 10,
        }}>{stamp}</span>
      </div>
      <PCaption text={caption} top={Y0 + rows.length * ROW_H + 140} at={0.74} />
    </IlluStage>
  );
};
