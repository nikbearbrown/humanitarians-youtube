/**
 * JudgmentIsTheJob.tsx — reel-local scenes for
 * `claude-liam-the-judgment-is-the-job` ("The Judgment Is the Job.").
 *
 * HOUSE CONSTRAINT FOR THIS REEL (from the human, and it drives every shape here):
 * no statistics, percentages or counts anywhere on screen. Every comparison is either
 * ordinal (position, length, order of appearance) or stated in words. So none of these
 * components accepts a numeric datum to render — there is deliberately no code path that
 * can print a figure. That is the cheapest way to keep the constraint: make it
 * structurally impossible rather than remembering not to.
 *
 * Two of the reel's five body beats reuse the deckPatterns scenes that are genuinely
 * qualitative (DivergentFates, BinaryBranch) via SafeStage. The other three are new
 * shapes, per ILLUSTRATIONS.md ("a genuinely new shape becomes a new component"):
 *
 *   · JdgSplit   — a two-column ledger: what moved to the machine vs what is still yours.
 *   · JdgOptions — a wall of unranked concept cards, then ONE terracotta ring: the whole
 *                  thesis in one picture (generating is free, choosing is the job).
 *   · JdgStakes  — N named things the machine cannot own, each with a one-line why.
 *
 * Terracotta is the ONE accent in every scene and it always marks JUDGMENT — the half
 * that did not move — so the accent carries the argument instead of decorating it.
 */
import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {BinaryBranch, DivergentFates, type BranchData, type FatesData} from '../deckPatterns';
import {SAFE} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {SafeStage, PlainStage, Head, RULE, MUTE, win} from './claudeStage';

/** progress through the beat, 0..1 */
const useP = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));
};

/* ═══════════════════════════════════════════════════════════════════════════
   B01 — the split (REUSED: DivergentFates is qualitative)
   ═══════════════════════════════════════════════════════════════════════════ */
export const JdgDiverge: React.FC<{data: FatesData}> = ({data}) => (
  <SafeStage>
    <DivergentFates data={data} />
  </SafeStage>
);

/* ═══════════════════════════════════════════════════════════════════════════
   B02 — JdgSplit: the two halves of the work, side by side.
   ═══════════════════════════════════════════════════════════════════════════ */
export type SplitData = {
  slideMeta: string;
  title: string;
  left: {heading: string; items: string[]};
  right: {heading: string; items: string[]};
  note: string;
};

export const JdgSplit: React.FC<{data: SplitData}> = ({data}) => {
  const p = useP();
  const MID = SAFE.x + SAFE.w / 2;
  const TOP = SAFE.y + 250;
  const COL_W = SAFE.w / 2 - 80;
  const ROW = 92;

  const column = (
    side: {heading: string; items: string[]},
    x: number,
    accent: boolean,
    from: number,
  ) => (
    <>
      <div
        style={{
          position: 'absolute', left: x, top: TOP,
          fontFamily: CLAUDE_FONT.ui, fontSize: 30, letterSpacing: '.1em',
          color: accent ? CLAUDE.SPARK : MUTE, fontWeight: 600,
          opacity: win(p, from - 0.06, from),
          whiteSpace: 'nowrap',
        }}
      >
        {side.heading.toUpperCase()}
      </div>
      {side.items.map((it, i) => {
        const g = win(p, from + i * 0.075, from + 0.06 + i * 0.075);
        return (
          <div key={i} style={{position: 'absolute', left: x, top: TOP + 76 + i * ROW, width: COL_W, opacity: g}}>
            <div
              style={{
                fontFamily: CLAUDE_FONT.ui, fontSize: 40, lineHeight: 1.2,
                color: accent ? CLAUDE.SPARK : CLAUDE.INK,
                transform: `translateY(${(1 - g) * 14}px)`,
              }}
            >
              {it}
            </div>
            <div style={{marginTop: 18, width: COL_W, height: 1, backgroundColor: RULE}} />
          </div>
        );
      })}
    </>
  );

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {/* the divide — drawn before either column fills */}
      <div
        style={{
          position: 'absolute', left: MID, top: TOP - 20,
          width: 2, height: (SAFE.b - TOP - 90) * win(p, 0.06, 0.2),
          backgroundColor: RULE,
        }}
      />
      {column(data.left, SAFE.x, false, 0.22)}
      {column(data.right, MID + 78, true, 0.58)}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 60,
          fontFamily: CLAUDE_FONT.serif, fontSize: 40, color: CLAUDE.INK,
          opacity: win(p, 0.86, 0.95), maxWidth: SAFE.w,
        }}
      >
        {data.note}
      </div>
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B04 — JdgOptions: the wall fills for free, then ONE card is chosen.
   ═══════════════════════════════════════════════════════════════════════════ */
export type OptionsData = {
  slideMeta: string;
  title: string;
  options: string[];
  chosenIndex: number;
  caption: string;
};

export const JdgOptions: React.FC<{data: OptionsData}> = ({data}) => {
  const p = useP();
  const COLS = 4;
  const rows = Math.ceil(data.options.length / COLS);
  const GAP = 26;
  const CARD_W = (SAFE.w - GAP * (COLS - 1)) / COLS;
  const TOP = SAFE.y + 240;
  const CARD_H = Math.min(190, (SAFE.b - TOP - 130 - GAP * (rows - 1)) / rows);

  // The wall fills fast (.08–.52) — deliberately faster than the voice can list it.
  // The choice lands late (.78), on the spoken word.
  const chose = win(p, 0.78, 0.9);

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.options.map((label, i) => {
        const c = i % COLS;
        const r = Math.floor(i / COLS);
        const g = win(p, 0.08 + i * 0.032, 0.16 + i * 0.032);
        const isChosen = i === data.chosenIndex;
        const ring = isChosen ? chose : 0;
        return (
          <div
            key={i}
            style={{
              position: 'absolute',
              left: SAFE.x + c * (CARD_W + GAP),
              top: TOP + r * (CARD_H + GAP),
              width: CARD_W,
              height: CARD_H,
              backgroundColor: '#FFFFFF',
              border: `${1 + 4 * ring}px solid ${ring > 0 ? CLAUDE.SPARK : '#E5E2D9'}`,
              borderRadius: 10,
              opacity: g,
              transform: `scale(${0.94 + 0.06 * g})`,
              display: 'flex',
              alignItems: 'flex-end',
              boxSizing: 'border-box',
              padding: 20,
            }}
          >
            <div
              style={{
                fontFamily: CLAUDE_FONT.ui,
                fontSize: 28,
                lineHeight: 1.22,
                color: ring > 0 ? CLAUDE.SPARK : CLAUDE.INK,
                overflow: 'hidden',
              }}
            >
              {label}
            </div>
          </div>
        );
      })}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 56,
          fontFamily: CLAUDE_FONT.serif, fontSize: 42, color: CLAUDE.INK,
          opacity: win(p, 0.9, 0.97), maxWidth: SAFE.w,
        }}
      >
        {data.caption}
      </div>
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B05 — the role, walked (REUSED: BinaryBranch is qualitative)
   ═══════════════════════════════════════════════════════════════════════════ */
export const JdgBranch: React.FC<{data: BranchData}> = ({data}) => (
  <SafeStage>
    <BinaryBranch data={data} />
  </SafeStage>
);

/* ═══════════════════════════════════════════════════════════════════════════
   B06 — JdgStakes: what the machine cannot own.
   ═══════════════════════════════════════════════════════════════════════════ */
export type StakesData = {
  slideMeta: string;
  title: string;
  items: {label: string; why: string}[];
  closer: string;
};

export const JdgStakes: React.FC<{data: StakesData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 250;
  const n = data.items.length;
  const ROW = Math.min(160, (SAFE.b - TOP - 140) / n);

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.items.map((it, i) => {
        const g = win(p, 0.1 + i * 0.15, 0.24 + i * 0.15);
        const whyG = win(p, 0.2 + i * 0.15, 0.34 + i * 0.15);
        const y = TOP + i * ROW;
        return (
          <React.Fragment key={i}>
            {/* terracotta marker — the accent marks the thing that stays human */}
            <div style={{position: 'absolute', left: SAFE.x, top: y + 12, width: 10, height: 44 * g, backgroundColor: CLAUDE.SPARK}} />
            <div
              style={{
                position: 'absolute', left: SAFE.x + 40, top: y,
                fontFamily: CLAUDE_FONT.ui, fontSize: 44, color: CLAUDE.INK,
                opacity: g, transform: `translateY(${(1 - g) * 12}px)`,
                maxWidth: SAFE.w - 40,
              }}
            >
              {it.label}
            </div>
            <div
              style={{
                position: 'absolute', left: SAFE.x + 40, top: y + 58,
                fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: MUTE,
                opacity: whyG, maxWidth: SAFE.w - 80,
              }}
            >
              {it.why}
            </div>
          </React.Fragment>
        );
      })}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 56,
          fontFamily: CLAUDE_FONT.serif, fontSize: 42, color: CLAUDE.INK,
          opacity: win(p, 0.88, 0.96), maxWidth: SAFE.w,
        }}
      >
        {data.closer}
      </div>
    </PlainStage>
  );
};
