/**
 * BottleneckMoved.tsx — reel-local scenes for
 * `claude-liam-the-bottleneck-moved` ("The Bottleneck Moved.").
 *
 * ── WHY THIS FILE EXISTS (read before "simplifying" it back to deckPatterns) ──
 *
 * The reel's five body beats were first authored against the shared C2 rhetorical
 * pattern library in ../deckPatterns. Visual QC on real frames showed that three of
 * the five are QUANTITATIVE-MEASUREMENT visuals, and this reel is deliberately
 * non-quantitative — it argues from a stated model and asserts no measured figure
 * anywhere (see the reel's FACTCHECK.md). Concretely, on real renders:
 *
 *   · ScaleComparison — CRASHED the render (`RangeError: Invalid array length`): it
 *     builds decade ticks with `for (e = ceil(log10(min)) …)`, and this beat's axis
 *     starts at 0, so log10(0) = -Infinity and the loop never terminates. Raising
 *     min to 1 would stop the crash but not the real problem: it is a LOG-SCALE
 *     component that stamps "(log scale, <unit>)" on its own axis.
 *   · AttritionChain — multiplied per-stage survivals cumulatively and printed
 *     "1 / 100" and "1% remain" on screen, in five otherwise-empty boxes.
 *   · Threshold — printed a numeric 0–100 axis plus "60 rel.", clipped its own axis
 *     label off the left edge, and left ~80% of the frame empty.
 *
 * Numbers that look measured but aren't are the one thing this reel must not do, so
 * those three beats get purpose-built shapes here (sanctioned by ILLUSTRATIONS.md:
 * "a genuinely new shape becomes a new component"). The two patterns that are
 * genuinely qualitative — DivergentFates and BinaryBranch — are reused unchanged.
 *
 * HOUSE RULES HONOURED BY EVERY SCENE BELOW
 *   · NO NUMBERS ON SCREEN. Lengths and positions encode RANK; annotations are words.
 *   · ONE terracotta event per beat — always the cost that did NOT fall.
 *   · Claude stage: cream ground, warm ink, EB Garamond serif for titles, UI sans for
 *     labels. deckPatterns already uses the claude values, so nothing is retinted.
 *   · LOGO LAW: the @NikBearBrown bug, low-opacity, lower-right, positioned from SAFE.
 *   · durationInFrames per composition = the beat's MEASURED Kokoro length × 30fps.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {
  BinaryBranch,
  DivergentFates,
  type BranchData,
  type FatesData,
} from '../deckPatterns';
import {CANVAS, SAFE} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';

/** The claude stage ground — matches deckPatterns' own BG constant. */
const STAGE = '#F2F0E9';
const RULE = '#D8D4C8';
const MUTE = '#7A7265';

const ease = (t: number) => 1 - Math.pow(1 - Math.min(1, Math.max(0, t)), 3);
/** progress within a window, eased and clamped */
const win = (p: number, a: number, b: number) => ease((p - a) / (b - a));

/**
 * LOGO LAW — small, low-opacity corner bug, lower-right, INSIDE the title-safe
 * inset. No logo file ships for @NikBearBrown in this tree, so the law's stated
 * fallback applies: the handle as a clean wordmark in the Claude serif.
 */
const LogoBug: React.FC = () => (
  <div
    style={{
      position: 'absolute',
      right: CANVAS.w - SAFE.r,
      bottom: CANVAS.h - SAFE.b,
      fontFamily: CLAUDE_FONT.serif,
      fontSize: 26,
      color: CLAUDE.INK,
      opacity: 0.3,
      letterSpacing: '.04em',
      pointerEvents: 'none',
    }}
  >
    @NikBearBrown
  </div>
);

/**
 * SAFE-AREA MAPPING — needed only by the two REUSED deckPatterns scenes.
 *
 * DivergentFates and BinaryBranch lay out against useVideoConfig() and place their
 * end-of-track label boxes hard against the canvas edge. At 1920×1080 that put those
 * boxes at x≈3792/3840 in the 4K render — past the 5% title-safe inset (SAFE.r =
 * 1824), caught by reading frames. They are shared with other reels, so widening
 * their internal margins is not this reel's call. Instead the pattern renders at full
 * canvas and the whole composition is mapped onto the safe box: the inset is a
 * uniform 5%, so SAFE.w/CANVAS.w === SAFE.h/CANVAS.h === 0.9 exactly — isotropic, no
 * distortion — and ink coverage as a fraction of SAFE is unchanged.
 *
 * The three purpose-built scenes below don't need this: they are authored inside the
 * safe box directly, which is why they get PlainStage instead.
 */
const SAFE_SCALE = SAFE.w / CANVAS.w;

const Stage: React.FC<{children: React.ReactNode}> = ({children}) => (
  <AbsoluteFill style={{backgroundColor: STAGE}}>
    <div
      style={{
        position: 'absolute',
        left: SAFE.x,
        top: SAFE.y,
        width: CANVAS.w,
        height: CANVAS.h,
        transform: `scale(${SAFE_SCALE})`,
        transformOrigin: 'top left',
      }}
    >
      {children}
    </div>
    <LogoBug />
  </AbsoluteFill>
);

const PlainStage: React.FC<{children: React.ReactNode}> = ({children}) => (
  <AbsoluteFill style={{backgroundColor: STAGE}}>
    {children}
    <LogoBug />
  </AbsoluteFill>
);

/** Shared eyebrow + title block, authored at safe-box coordinates. */
const Head: React.FC<{meta: string; title: string}> = ({meta, title}) => (
  <>
    <div
      style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 6,
        fontFamily: CLAUDE_FONT.ui, fontSize: 22, letterSpacing: '.18em',
        color: MUTE, fontWeight: 600,
      }}
    >
      {meta.toUpperCase()}
    </div>
    <div
      style={{
        position: 'absolute', left: SAFE.x, top: SAFE.y + 62,
        fontFamily: CLAUDE_FONT.serif, fontSize: 78, color: CLAUDE.INK,
        lineHeight: 1.05, maxWidth: SAFE.w,
      }}
    >
      {title}
    </div>
  </>
);

/* ═══════════════════════════════════════════════════════════════════════════
   B01 — the split (REUSED: DivergentFates is qualitative and works)
   ═══════════════════════════════════════════════════════════════════════════ */
export const BnkSplit: React.FC<{data: FatesData}> = ({data}) => (
  <Stage>
    <DivergentFates data={data} />
  </Stage>
);

/* ═══════════════════════════════════════════════════════════════════════════
   B02 — where the effort sits now. Ordinal bars, words not numbers.
   ═══════════════════════════════════════════════════════════════════════════ */
export type CostsData = {
  slideMeta: string;
  title: string;
  rows: {label: string; note: string; rank: number; hot?: boolean}[];
  band: string;
};

export const BnkCosts: React.FC<{data: CostsData}> = ({data}) => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  const p = Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));

  const X0 = SAFE.x + 40;
  const TRACK = SAFE.w - 400;
  const ROW_Y = [SAFE.y + 300, SAFE.y + 500, SAFE.y + 700];
  const BAR_H = 96;
  const CUE = [0.25, 0.5, 0.72];

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.rows.map((r, i) => {
        const g = win(p, CUE[i], CUE[i] + 0.16);
        const w = TRACK * r.rank * g;
        const color = r.hot ? CLAUDE.SPARK : CLAUDE.INK;
        return (
          <React.Fragment key={i}>
            <div
              style={{
                position: 'absolute', left: X0, top: ROW_Y[i] - 50,
                fontFamily: CLAUDE_FONT.ui, fontSize: 36, color: CLAUDE.INK,
                maxWidth: TRACK, whiteSpace: 'nowrap',
                opacity: 0.35 + 0.65 * g,
              }}
            >
              {r.label}
            </div>
            {/* full-span rule, so a short bar reads as SHORT rather than as absent */}
            <div style={{position: 'absolute', left: X0, top: ROW_Y[i] + BAR_H, width: TRACK, height: 1, backgroundColor: RULE}} />
            <div style={{position: 'absolute', left: X0, top: ROW_Y[i], width: w, height: BAR_H, backgroundColor: color}} />
            <div
              style={{
                position: 'absolute', left: X0 + w + 30, top: ROW_Y[i] + 28,
                fontFamily: CLAUDE_FONT.ui, fontSize: 34, color, opacity: g,
                whiteSpace: 'nowrap',
              }}
            >
              {r.note}
            </div>
          </React.Fragment>
        );
      })}
      {/* the band brackets ONLY the cheap bar */}
      <div style={{opacity: win(p, 0.86, 0.94)}}>
        <div style={{position: 'absolute', left: X0, top: ROW_Y[0] - 96, width: TRACK * data.rows[0].rank, height: 4, backgroundColor: CLAUDE.SPARK}} />
        <div
          style={{
            position: 'absolute', left: X0, top: ROW_Y[0] - 140,
            fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: CLAUDE.SPARK, letterSpacing: '.06em',
            whiteSpace: 'nowrap',
          }}
        >
          {data.band}
        </div>
      </div>
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B04 — the funnel AI didn't touch. Ordinal widths; the top doubles, the tail
   visibly does not move. No counts, no percentages.
   ═══════════════════════════════════════════════════════════════════════════ */
export type FunnelData = {
  slideMeta: string;
  title: string;
  stages: {label: string; rank: number}[];
  bracket: string;
  doubleNote: string;
  tailNote: string;
};

export const BnkFunnel: React.FC<{data: FunnelData}> = ({data}) => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  const p = Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));

  const n = data.stages.length;
  const X0 = SAFE.x + 300;
  const TRACK = SAFE.w - 520;
  const TOP = SAFE.y + 250;
  const H = 96;
  const GAP = 28;
  // Stages light in narration order across .10–.62, then the top doubles at .82.
  const dbl = win(p, 0.82, 0.96);

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.stages.map((s, i) => {
        const g = win(p, 0.1 + i * 0.13, 0.24 + i * 0.13);
        // row 0 doubles at the end; every other row is untouched — the whole point
        const rank = i === 0 ? s.rank * (1 + dbl) : s.rank;
        const w = TRACK * rank * g;
        const y = TOP + i * (H + GAP);
        return (
          <React.Fragment key={i}>
            <div
              style={{
                position: 'absolute', left: SAFE.x, top: y + 26,
                width: 240, textAlign: 'right',
                fontFamily: CLAUDE_FONT.ui, fontSize: 34, color: CLAUDE.INK,
                opacity: 0.3 + 0.7 * g, whiteSpace: 'nowrap',
              }}
            >
              {s.label}
            </div>
            <div style={{position: 'absolute', left: X0, top: y, width: w, height: H, backgroundColor: CLAUDE.INK, opacity: 0.9}} />
            {/* ghost of row 0's original width, so the doubling is legible AS a change */}
            {i === 0 && dbl > 0 && (
              <div style={{position: 'absolute', left: X0 + TRACK * s.rank, top: y, width: 3, height: H, backgroundColor: CLAUDE.SPARK}} />
            )}
          </React.Fragment>
        );
      })}

      {/* terracotta bracket down the whole chain — the ONE accent event.
          Sits in the 40px gutter between the right-aligned labels (which end at
          SAFE.x + 240) and the bar origin at X0 — QC caught it running THROUGH the
          label text at the previous offset. Its caption clears the tailNote below. */}
      <div style={{opacity: win(p, 0.64, 0.76)}}>
        <div style={{position: 'absolute', left: X0 - 26, top: TOP, width: 4, height: n * (H + GAP) - GAP, backgroundColor: CLAUDE.SPARK}} />
        <div
          style={{
            position: 'absolute', left: SAFE.x, top: TOP + n * (H + GAP) + 76,
            fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: CLAUDE.SPARK, letterSpacing: '.04em',
            whiteSpace: 'nowrap',
          }}
        >
          {data.bracket}
        </div>
      </div>

      <div style={{opacity: dbl}}>
        <div
          style={{
            position: 'absolute', left: X0, top: TOP - 62,
            fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: CLAUDE.SPARK, whiteSpace: 'nowrap',
          }}
        >
          {data.doubleNote}
        </div>
        <div
          style={{
            position: 'absolute', left: X0, top: TOP + (n - 1) * (H + GAP) + H + 14,
            fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE, whiteSpace: 'nowrap',
          }}
        >
          {data.tailNote}
        </div>
      </div>
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B05 — the cutoff. Two zones, a verdict each, and the falsifier. No axis ticks,
   no numbers: the point is the SIGN FLIP, not a measured threshold.
   ═══════════════════════════════════════════════════════════════════════════ */
export type CutoffData = {
  slideMeta: string;
  title: string;
  axisLabel: string;
  cutoffLabel: string;
  below: {label: string; verdict: string};
  above: {label: string; verdict: string};
  falsifier: string;
};

export const BnkCutoff: React.FC<{data: CutoffData}> = ({data}) => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  const p = Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));

  const X0 = SAFE.x + 20;
  const W = SAFE.w - 40;
  const CUT = X0 + W * 0.46;
  const TOP = SAFE.y + 300;
  const BAND = 300;

  const zoneA = win(p, 0.14, 0.34);
  const cut = win(p, 0.5, 0.62);
  const zoneB = win(p, 0.64, 0.82);
  const fals = win(p, 0.88, 0.98);

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />

      {/* below-cutoff zone */}
      <div style={{position: 'absolute', left: X0, top: TOP, width: (CUT - X0) * zoneA, height: BAND, backgroundColor: CLAUDE.INK, opacity: 0.08}} />
      <div style={{position: 'absolute', left: X0 + 34, top: TOP + 58, opacity: zoneA, maxWidth: CUT - X0 - 68}}>
        <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 36, color: CLAUDE.INK, lineHeight: 1.25}}>{data.below.label}</div>
        <div style={{marginTop: 22, fontFamily: CLAUDE_FONT.serif, fontSize: 52, color: CLAUDE.INK}}>{data.below.verdict}</div>
      </div>

      {/* the cutoff itself — the ONE accent event */}
      <div style={{position: 'absolute', left: CUT, top: TOP - 44, width: 5, height: (BAND + 88) * cut, backgroundColor: CLAUDE.SPARK}} />
      <div
        style={{
          position: 'absolute', left: CUT + 20, top: TOP - 96, opacity: cut,
          fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: CLAUDE.SPARK, letterSpacing: '.06em',
          whiteSpace: 'nowrap',
        }}
      >
        {data.cutoffLabel}
      </div>

      {/* above-cutoff zone */}
      <div style={{position: 'absolute', left: CUT + 5, top: TOP, width: (X0 + W - CUT - 5) * zoneB, height: BAND, backgroundColor: CLAUDE.SPARK, opacity: 0.1}} />
      <div style={{position: 'absolute', left: CUT + 44, top: TOP + 58, opacity: zoneB, maxWidth: X0 + W - CUT - 88}}>
        <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 36, color: CLAUDE.INK, lineHeight: 1.25}}>{data.above.label}</div>
        <div style={{marginTop: 22, fontFamily: CLAUDE_FONT.serif, fontSize: 52, color: CLAUDE.SPARK}}>{data.above.verdict}</div>
      </div>

      {/* the volume axis — direction only, deliberately unticked and unnumbered */}
      <div style={{position: 'absolute', left: X0, top: TOP + BAND + 34, width: W, height: 2, backgroundColor: RULE}} />
      <div
        style={{
          position: 'absolute', left: X0, top: TOP + BAND + 52,
          fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE, letterSpacing: '.1em',
        }}
      >
        {data.axisLabel.toUpperCase()} →
      </div>

      {/* the falsifier — the reason this beat exists */}
      <div
        style={{
          position: 'absolute', left: X0, top: TOP + BAND + 130, opacity: fals,
          fontFamily: CLAUDE_FONT.serif, fontSize: 44, color: CLAUDE.INK,
          maxWidth: W, lineHeight: 1.3,
        }}
      >
        {data.falsifier}
      </div>
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B06 — the worked example (REUSED: BinaryBranch is qualitative and works)
   ═══════════════════════════════════════════════════════════════════════════ */
export const BnkBranch: React.FC<{data: BranchData}> = ({data}) => (
  <Stage>
    <BinaryBranch data={data} />
  </Stage>
);
