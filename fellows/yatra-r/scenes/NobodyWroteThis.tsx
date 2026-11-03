/**
 * NobodyWroteThis.tsx — reel-local scenes for `yatra-nobody-wrote-this`
 * ("Nobody Wrote This." — how much of LinkedIn is AI-written).
 *
 * ── THE CONSTRAINT THAT SHAPES EVERY COMPONENT HERE ──────────────────────────
 * The human supplied seven figures and one instruction: cite them on screen, and
 * invent nothing beyond them. Two failure modes follow from that, and each is
 * closed structurally rather than by remembering:
 *
 * 1. A FIGURE DRIFTING FROM ITS PROVENANCE.
 *    Every component that can print a figure REQUIRES a `source` string. There is
 *    no code path that renders a number without a citation beneath it. Values are
 *    typed as STRINGS and rendered verbatim — never parsed for display, never
 *    rounded, never recomputed.
 *
 * 2. A BAR SILENTLY INVENTING A NUMBER.
 *    A bar has to have a length, and three of this reel's values are RANGES
 *    ("25–29%", "4–13%") or prose ("about a third"). The house `num()` helper used
 *    by the older stat components strips non-digits, so it reads "4–13%" as 413 —
 *    a bar nine times the width of its own track. So the components here take an
 *    explicit `bar: number` that is SEPARATE from the verbatim `value: string`.
 *    The printed figure is the human's; the bar is only a drawing instruction, and
 *    the rule mapping one to the other is recorded in the reel's FACTCHECK.md.
 *    That is why this reel does not reuse SeoCompare/SeoShare.
 *
 * 3. THE DERIVED THIRD BIN.
 *    41% of LinkedIn long-form posts are fully AI-generated and 4.3% are
 *    AI-assisted. The human-written share is therefore arithmetically available
 *    and is NOT shown, because it was not supplied. `LnkAllOrNothing` accepts a
 *    `remainderLabel` string and has deliberately NO `remainderBar` prop — the
 *    remainder band renders as a dashed, unfilled outline. A bar length is a
 *    number; refusing the prop is the only way to refuse the number.
 *
 * ── ACCENT SEMANTICS ─────────────────────────────────────────────────────────
 * Terracotta is the ONE accent per beat and it always marks THE MACHINE-WRITTEN
 * SHARE — the quantity under measurement. Citations render in muted ink, never in
 * the accent: provenance is not emphasis, and colouring it would spend the accent
 * on the footnote.
 */
import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {SAFE} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {PlainStage, Head, RULE, MUTE, win} from './claudeStage';
import {JdgStakes} from './JudgmentIsTheJob';

/**
 * B09's stress-test beat is exactly JdgStakes' shape (N named things, each with a
 * one-line why, plus a closer), so it is reused under this episode's name rather
 * than cloned. ILLUSTRATE LAW is satisfied because its neighbours (B08 collision,
 * B10 pressure axis) are different schemes — the ban is on consecutive repeats.
 */
export const LnkFalsify = JdgStakes;

/** progress through the beat, 0..1 */
const useP = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));
};

/** The citation line — same treatment in every scene so the eye learns one place. */
const SourceLine: React.FC<{source: string; opacity: number}> = ({source, opacity}) => (
  <div
    style={{
      position: 'absolute', left: SAFE.x, top: SAFE.b - 118, width: SAFE.w, opacity,
      fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE, letterSpacing: '.04em',
    }}
  >
    Source: {source}
  </div>
);

const NoteLine: React.FC<{note: string; opacity: number}> = ({note, opacity}) => (
  <div
    style={{
      position: 'absolute', left: SAFE.x, top: SAFE.b - 62, width: SAFE.w,
      fontFamily: CLAUDE_FONT.serif, fontSize: 40, color: CLAUDE.INK, opacity,
    }}
  >
    {note}
  </div>
);

/* ═══════════════════════════════════════════════════════════════════════════
   B01 — LnkBluf: the executive summary as kinetic type.

   EXECUTIVE-SUMMARY LAW allows a framing card here, but SHOW-DON'T-TELL still
   binds, so the beat ENACTS its own reframe: the wrong description is typed,
   struck through on the spoken beat, and replaced. No figure appears — the BLUF
   states the shape of the idea without spending the reveals.
   ═══════════════════════════════════════════════════════════════════════════ */
export type BlufData = {
  slideMeta: string;
  lead: string;         // ink
  hot: string;          // terracotta — the thesis phrase, THE accent of the beat
  struck: string;       // the wrong description, struck through
  replacement: string;  // what replaces it
  closer: string;
};

export const LnkBluf: React.FC<{data: BlufData}> = ({data}) => {
  const p = useP();
  const leadIn = win(p, 0.04, 0.22);
  const hotIn = win(p, 0.26, 0.46);
  const struckIn = win(p, 0.5, 0.62);
  const strikeIn = win(p, 0.66, 0.76);
  const replaceIn = win(p, 0.76, 0.88);

  return (
    <PlainStage>
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.y + 6,
          fontFamily: CLAUDE_FONT.ui, fontSize: 22, letterSpacing: '.18em',
          color: MUTE, fontWeight: 600, opacity: leadIn,
        }}
      >
        {data.slideMeta.toUpperCase()}
      </div>

      {/* the statement — one block so lead and hot flow as a single sentence */}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.y + 120, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 92, lineHeight: 1.14, color: CLAUDE.INK,
        }}
      >
        <span style={{opacity: leadIn}}>{data.lead} </span>
        <span style={{color: CLAUDE.SPARK, opacity: hotIn}}>{data.hot}</span>
      </div>

      {/* the reframe, performed: struck line then its replacement */}
      <div style={{position: 'absolute', left: SAFE.x, top: SAFE.y + 560, width: SAFE.w}}>
        <span
          style={{
            position: 'relative', display: 'inline-block',
            fontFamily: CLAUDE_FONT.ui, fontSize: 58, color: MUTE, opacity: struckIn,
          }}
        >
          {data.struck}
          <span
            style={{
              position: 'absolute', left: 0, top: '54%', height: 4,
              width: `${100 * strikeIn}%`, backgroundColor: MUTE,
            }}
          />
        </span>
      </div>
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.y + 660, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 86, color: CLAUDE.INK,
          opacity: replaceIn, transform: `translateY(${(1 - replaceIn) * 18}px)`,
        }}
      >
        {data.replacement}
      </div>

      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 92, width: SAFE.w * 0.42 * win(p, 0.9, 0.99),
          height: 3, backgroundColor: RULE,
        }}
      />
      <NoteLine note={data.closer} opacity={win(p, 0.9, 0.99)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B02 — LnkFrame: the three bins, EMPTY.

   This is the FRAMEWORK beat, and it runs before any example, so the bins must
   stay unfilled: showing a share here would spend B03's and B07's reveals. The
   type carries no numeric prop at all.
   ═══════════════════════════════════════════════════════════════════════════ */
export type FrameData = {
  slideMeta: string;
  title: string;
  bins: {label: string; sub: string}[];
  hotIndex: number;     // which bin the narration points at last
  source: string;
  note: string;
};

export const LnkFrame: React.FC<{data: FrameData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 250;
  const BAND = 150;
  const GAP = 40;

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.bins.map((b, i) => {
        const draw = win(p, 0.08 + i * 0.18, 0.24 + i * 0.18);
        const text = win(p, 0.16 + i * 0.18, 0.3 + i * 0.18);
        const hot = i === data.hotIndex ? win(p, 0.8, 0.92) : 0;
        const y = TOP + i * (BAND + GAP);
        return (
          <React.Fragment key={i}>
            {/* the empty bin — a drawn outline, never a fill */}
            <div
              style={{
                position: 'absolute', left: SAFE.x, top: y,
                width: SAFE.w * draw, height: BAND,
                border: `2px solid ${RULE}`, boxSizing: 'border-box',
              }}
            />
            {/* the accent: the last bin's outline reddens on the spoken cue */}
            <div
              style={{
                position: 'absolute', left: SAFE.x, top: y,
                width: SAFE.w, height: BAND,
                border: `3px solid ${CLAUDE.SPARK}`, boxSizing: 'border-box',
                opacity: hot,
              }}
            />
            <div
              style={{
                position: 'absolute', left: SAFE.x + 36, top: y + 32, maxWidth: SAFE.w - 80,
                fontFamily: CLAUDE_FONT.ui, fontSize: 46, color: CLAUDE.INK, opacity: text,
              }}
            >
              {b.label}
            </div>
            <div
              style={{
                position: 'absolute', left: SAFE.x + 36, top: y + 92, maxWidth: SAFE.w - 80,
                fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: MUTE, opacity: text,
              }}
            >
              {b.sub}
            </div>
          </React.Fragment>
        );
      })}
      <SourceLine source={data.source} opacity={win(p, 0.86, 0.95)} />
      <NoteLine note={data.note} opacity={win(p, 0.88, 0.97)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B03 — LnkStat: the hero figure.

   Differs from SeoStat by carrying a `rank` line: the "highest of any platform
   studied" claim is ORDINAL, and stating it in words next to the figure avoids
   printing a second, uncited number to make the same point.
   ═══════════════════════════════════════════════════════════════════════════ */
export type StatData = {
  slideMeta: string;
  title: string;
  value: string;   // verbatim
  label: string;
  rank: string;    // the ordinal claim, in words
  source: string;
  note: string;
};

export const LnkStat: React.FC<{data: StatData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 240;
  const figIn = win(p, 0.1, 0.36);

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 300, lineHeight: 1,
          color: CLAUDE.SPARK, opacity: figIn,
          transform: `translateY(${(1 - figIn) * 26}px)`,
        }}
      >
        {data.value}
      </div>
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP + 326,
          width: SAFE.w * 0.52 * win(p, 0.4, 0.6), height: 5, backgroundColor: CLAUDE.SPARK,
        }}
      />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP + 366, width: SAFE.w * 0.86,
          fontFamily: CLAUDE_FONT.ui, fontSize: 48, color: CLAUDE.INK, lineHeight: 1.25,
          opacity: win(p, 0.44, 0.64),
        }}
      >
        {data.label}
      </div>
      {/* the ordinal claim — words, not a second figure */}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP + 466,
          fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE, letterSpacing: '.1em',
          textTransform: 'uppercase' as const, opacity: win(p, 0.62, 0.78),
          border: `1px solid ${RULE}`, padding: '12px 22px', display: 'inline-block',
        }}
      >
        {data.rank}
      </div>
      <SourceLine source={data.source} opacity={win(p, 0.78, 0.9)} />
      <NoteLine note={data.note} opacity={win(p, 0.86, 0.96)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B05 — LnkLadder: the five platforms, sorted.

   `bar` is separate from `value` (see the header note). `baseline` draws the
   cross-platform rate as a dashed reference so the comparison the narration makes
   ("one long post in four") is visible rather than merely asserted.
   ═══════════════════════════════════════════════════════════════════════════ */
export type LadderData = {
  slideMeta: string;
  title: string;
  items: {label: string; value: string; bar: number; hot?: boolean}[];
  baseline: {bar: number; label: string};
  source: string;
  note: string;
};

export const LnkLadder: React.FC<{data: LadderData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 250;
  const ROW = 104;
  const GUTTER = 300;          // left column for the platform name
  const TRACK_X = SAFE.x + GUTTER + 20;
  const TRACK_W = SAFE.w - GUTTER - 20 - 250;   // 250 reserved for the printed value
  const maxBar = Math.max(...data.items.map((i) => i.bar), data.baseline.bar) * 1.06;
  const BAR_H = 58;

  const baseX = TRACK_X + TRACK_W * (data.baseline.bar / maxBar);
  const baseIn = win(p, 0.74, 0.88);

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />

      {data.items.map((it, i) => {
        const g = win(p, 0.08 + i * 0.12, 0.26 + i * 0.12);
        const w = TRACK_W * (it.bar / maxBar) * g;
        const c = it.hot ? CLAUDE.SPARK : CLAUDE.INK;
        const y = TOP + i * ROW;
        return (
          <React.Fragment key={i}>
            <div
              style={{
                position: 'absolute', left: SAFE.x, top: y + 10, width: GUTTER,
                fontFamily: CLAUDE_FONT.ui, fontSize: 40, color: CLAUDE.INK,
                opacity: 0.35 + 0.65 * g, lineHeight: 1.1,
              }}
            >
              {it.label}
            </div>
            <div style={{position: 'absolute', left: TRACK_X, top: y + BAR_H, width: TRACK_W, height: 1, backgroundColor: RULE}} />
            <div style={{position: 'absolute', left: TRACK_X, top: y + 2, width: w, height: BAR_H, backgroundColor: c}} />
            <div
              style={{
                position: 'absolute', left: TRACK_X + w + 24, top: y - 4,
                fontFamily: CLAUDE_FONT.serif, fontSize: 62, color: c, opacity: g,
                lineHeight: 1, whiteSpace: 'nowrap' as const,
              }}
            >
              {it.value}
            </div>
          </React.Fragment>
        );
      })}

      {/* the cross-platform rate, as a dashed reference across every row */}
      <div
        style={{
          position: 'absolute', left: baseX, top: TOP - 24,
          width: 0, height: (data.items.length * ROW - 24) * baseIn,
          borderLeft: `3px dashed ${MUTE}`, opacity: 0.85 * baseIn,
        }}
      />
      <div
        style={{
          position: 'absolute', left: Math.min(baseX + 14, SAFE.r - 520), top: TOP + data.items.length * ROW - 8,
          fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE, opacity: baseIn,
          whiteSpace: 'nowrap' as const,
        }}
      >
        {data.baseline.label}
      </div>

      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} />
      <NoteLine note={data.note} opacity={win(p, 0.88, 0.97)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B06 — LnkDisproportion: share of the corpus vs share of the AI found.

   The dashed carry-down is the whole argument: it marks where the second track
   would stop if the two shares were proportional, so the overshoot is something
   the viewer SEES rather than something the voice claims.
   ═══════════════════════════════════════════════════════════════════════════ */
export type DispData = {
  slideMeta: string;
  title: string;
  top: {label: string; value: string; bar: number};
  bottom: {label: string; value: string; bar: number};
  source: string;
  note: string;
};

export const LnkDisproportion: React.FC<{data: DispData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 240;
  const BAND = 120;
  const T2 = TOP + 286;
  const track = SAFE.w;
  const topIn = win(p, 0.1, 0.36);
  const botIn = win(p, 0.42, 0.68);
  const refIn = win(p, 0.7, 0.84);
  const topW = track * (data.top.bar / 100) * topIn;
  const botW = track * (data.bottom.bar / 100) * botIn;
  const refX = SAFE.x + track * (data.top.bar / 100);

  const row = (y: number, d: {label: string; value: string}, w: number, accent: boolean, g: number) => (
    <>
      <div style={{position: 'absolute', left: SAFE.x, top: y, width: track, height: BAND, border: `1px solid ${RULE}`, boxSizing: 'border-box'}} />
      <div style={{position: 'absolute', left: SAFE.x, top: y, width: w, height: BAND, backgroundColor: accent ? CLAUDE.SPARK : CLAUDE.INK, opacity: accent ? 1 : 0.85}} />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: y + BAND + 14, width: track * 0.7,
          fontFamily: CLAUDE_FONT.ui, fontSize: 32, color: accent ? CLAUDE.SPARK : CLAUDE.INK,
          opacity: g, lineHeight: 1.2,
        }}
      >
        {d.label}
      </div>
      <div
        style={{
          position: 'absolute', left: SAFE.x + track * 0.72, top: y + BAND + 4, width: track * 0.28,
          fontFamily: CLAUDE_FONT.serif, fontSize: 66, color: accent ? CLAUDE.SPARK : CLAUDE.INK,
          opacity: g, lineHeight: 1, textAlign: 'right' as const, whiteSpace: 'nowrap' as const,
        }}
      >
        {d.value}
      </div>
    </>
  );

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {row(TOP, data.top, topW, false, topIn)}
      {row(T2, data.bottom, botW, true, botIn)}

      {/* Where the second track would stop if the two shares were proportional.
          TWO SEGMENTS, one per band, rather than one continuous rule: the gap
          between the bands carries the first track's label, and a continuous
          line struck straight through that text (QC defect, caught at frame
          level). Both segments share refX, so it still reads as a carry-down. */}
      <div
        style={{
          position: 'absolute', left: refX, top: TOP,
          width: 0, height: BAND * refIn,
          borderLeft: `3px dashed ${MUTE}`, opacity: 0.9 * refIn,
        }}
      />
      <div
        style={{
          position: 'absolute', left: refX, top: T2,
          width: 0, height: BAND * refIn,
          borderLeft: `3px dashed ${MUTE}`, opacity: 0.9 * refIn,
        }}
      />
      <div
        style={{
          position: 'absolute', left: Math.min(refX + 16, SAFE.r - 560), top: T2 + BAND + 96,
          fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: MUTE, opacity: refIn,
          whiteSpace: 'nowrap' as const,
        }}
      >
        proportional would stop here
      </div>

      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} />
      <NoteLine note={data.note} opacity={win(p, 0.88, 0.97)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B07 — LnkAllOrNothing: B02's bins, filled.

   NOTE THE MISSING PROP. There is `assisted.bar` and `generated.bar`, and there
   is NO remainder bar — only `remainderLabel`. The human-written share was not
   supplied, and a bar length is a number, so the remainder renders as a dashed
   empty band. The refusal is in the type, not in the author's memory.
   ═══════════════════════════════════════════════════════════════════════════ */
export type AllOrNothingData = {
  slideMeta: string;
  title: string;
  assisted: {label: string; value: string; bar: number};
  generated: {label: string; value: string; bar: number};
  remainderLabel: string;
  source: string;
  note: string;
};

export const LnkAllOrNothing: React.FC<{data: AllOrNothingData}> = ({data}) => {
  const p = useP();
  // GEOMETRY NOTE: three bands + their labels have to fit between the title and
  // the citation line at SAFE.b - 118, i.e. 604px. At 150px bands on a 236px step
  // the remainder band ran to y=972 and sat on top of the citation AND the closer
  // (QC defect, caught at frame level). 118px bands on a 196px step land the last
  // band at y=860, clearing the citation by 48px.
  const TOP = SAFE.y + 250;
  const BAND = 118;
  const STEP = 196;
  const track = SAFE.w;

  const filled = (
    y: number,
    d: {label: string; value: string; bar: number},
    accent: boolean,
    g: number,
  ) => (
    <>
      <div style={{position: 'absolute', left: SAFE.x, top: y, width: track, height: BAND, border: `2px solid ${RULE}`, boxSizing: 'border-box'}} />
      <div style={{position: 'absolute', left: SAFE.x, top: y, width: track * (d.bar / 100) * g, height: BAND, backgroundColor: accent ? CLAUDE.SPARK : CLAUDE.INK, opacity: accent ? 1 : 0.88}} />
      <div style={{position: 'absolute', left: SAFE.x + 36, top: y - 44, maxWidth: track - 320, fontFamily: CLAUDE_FONT.ui, fontSize: 32, color: CLAUDE.INK, opacity: g}}>
        {d.label}
      </div>
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: y + 22, width: track - 36,
          fontFamily: CLAUDE_FONT.serif, fontSize: 68, color: accent ? CLAUDE.SPARK : CLAUDE.INK,
          opacity: g, lineHeight: 1, textAlign: 'right' as const,
        }}
      >
        {d.value}
      </div>
    </>
  );

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {/* the sliver first — the narration points at the middle bin before anything else */}
      {filled(TOP + 46, data.assisted, true, win(p, 0.16, 0.4))}
      {filled(TOP + 46 + STEP, data.generated, false, win(p, 0.44, 0.66))}
      {/* the remainder: dashed, empty, unlabelled by any figure */}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP + 46 + 2 * STEP,
          width: track, height: BAND, border: `2px dashed ${RULE}`, boxSizing: 'border-box',
          opacity: win(p, 0.66, 0.82),
        }}
      />
      <div
        style={{
          position: 'absolute', left: SAFE.x + 36, top: TOP + 46 + 2 * STEP + 40,
          maxWidth: track - 80, fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE,
          opacity: win(p, 0.7, 0.86),
        }}
      >
        {data.remainderLabel}
      </div>

      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} />
      <NoteLine note={data.note} opacity={win(p, 0.88, 0.97)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B08 — LnkContradiction: two policies of one platform, driving at each other.

   The arrows meet and STALL. The stall is the argument — a static two-column card
   would state the contradiction; this one performs it.
   ═══════════════════════════════════════════════════════════════════════════ */
export type ContraData = {
  slideMeta: string;
  title: string;
  left: {heading: string; label: string; sub: string};
  right: {heading: string; label: string; sub: string};
  collision: string;
  source: string;
  note: string;
};

export const LnkContradiction: React.FC<{data: ContraData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 240;
  const BOX_W = 720;
  const BOX_H = 300;
  const MIDX = SAFE.x + SAFE.w / 2;
  const LANE = TOP + BOX_H + 76;
  const leftIn = win(p, 0.08, 0.3);
  const rightIn = win(p, 0.34, 0.56);
  const driveIn = win(p, 0.56, 0.76);
  const hitIn = win(p, 0.76, 0.9);

  const block = (x: number, d: {heading: string; label: string; sub: string}, g: number) => (
    <>
      <div style={{position: 'absolute', left: x, top: TOP, width: BOX_W, height: BOX_H, border: `2px solid ${RULE}`, boxSizing: 'border-box', opacity: g}} />
      <div style={{position: 'absolute', left: x + 32, top: TOP + 28, fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.18em', color: MUTE, fontWeight: 600, opacity: g}}>
        {d.heading.toUpperCase()}
      </div>
      <div style={{position: 'absolute', left: x + 32, top: TOP + 76, maxWidth: BOX_W - 64, fontFamily: CLAUDE_FONT.serif, fontSize: 64, color: CLAUDE.INK, opacity: g, lineHeight: 1.1}}>
        {d.label}
      </div>
      <div style={{position: 'absolute', left: x + 32, top: TOP + 186, maxWidth: BOX_W - 64, fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE, opacity: g, lineHeight: 1.3}}>
        {d.sub}
      </div>
    </>
  );

  const reach = (MIDX - SAFE.x - BOX_W - 20) * driveIn;

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {block(SAFE.x, data.left, leftIn)}
      {block(SAFE.r - BOX_W, data.right, rightIn)}

      {/* the two drives, growing toward each other from the inner edge of each block */}
      <div style={{position: 'absolute', left: SAFE.x + BOX_W + 10, top: LANE, width: reach, height: 12, backgroundColor: CLAUDE.INK, opacity: 0.75 * driveIn}} />
      <div style={{position: 'absolute', left: SAFE.r - BOX_W - 10 - reach, top: LANE, width: reach, height: 12, backgroundColor: CLAUDE.INK, opacity: 0.75 * driveIn}} />

      {/* the stall */}
      <div
        style={{
          position: 'absolute', left: MIDX - 13, top: LANE - 20,
          width: 26, height: 52, backgroundColor: CLAUDE.SPARK,
          opacity: hitIn, transform: `scaleY(${0.4 + 0.6 * hitIn})`,
        }}
      />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: LANE + 66, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 54, color: CLAUDE.SPARK,
          opacity: hitIn, textAlign: 'center' as const,
        }}
      >
        {data.collision}
      </div>

      <SourceLine source={data.source} opacity={win(p, 0.86, 0.95)} />
      <NoteLine note={data.note} opacity={win(p, 0.9, 0.98)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B10 — LnkPressure: an opinion and a dated fact, kept visibly apart.

   The `tag` chips do real work: one block is tagged INTERPRETATION and carries
   "the narrator's read, not a published finding" where the others carry a
   citation. Separating judgment from evidence ON SCREEN is the Teardown honesty
   move — doing it only in the voice would leave the frame making a claim the
   sources do not support.
   ═══════════════════════════════════════════════════════════════════════════ */
export type PressureData = {
  slideMeta: string;
  title: string;
  left: {tag: string; label: string; sub: string; cite: string};
  right: {tag: string; label: string; sub: string; cite: string};
  marker: string;
  axisLabel: string;
  note: string;
};

export const LnkPressure: React.FC<{data: PressureData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 230;
  const BOX_W = (SAFE.w - 88) / 2;
  const BOX_H = 340;
  const AXIS = TOP + BOX_H + 90;
  const markX = SAFE.x + SAFE.w * 0.62;

  const block = (x: number, d: {tag: string; label: string; sub: string; cite: string}, g: number, accent: boolean) => (
    <>
      <div style={{position: 'absolute', left: x, top: TOP, width: BOX_W, height: BOX_H, border: `2px solid ${RULE}`, boxSizing: 'border-box', opacity: g}} />
      <div
        style={{
          position: 'absolute', left: x + 30, top: TOP + 26,
          fontFamily: CLAUDE_FONT.ui, fontSize: 22, letterSpacing: '.2em', fontWeight: 600,
          color: accent ? CLAUDE.SPARK : MUTE, border: `1px solid ${accent ? CLAUDE.SPARK : RULE}`,
          padding: '8px 16px', display: 'inline-block', opacity: g,
        }}
      >
        {d.tag}
      </div>
      <div style={{position: 'absolute', left: x + 30, top: TOP + 96, maxWidth: BOX_W - 60, fontFamily: CLAUDE_FONT.serif, fontSize: 60, color: CLAUDE.INK, opacity: g, lineHeight: 1.08}}>
        {d.label}
      </div>
      <div style={{position: 'absolute', left: x + 30, top: TOP + 172, maxWidth: BOX_W - 60, fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: CLAUDE.INK, opacity: g * 0.9, lineHeight: 1.32}}>
        {d.sub}
      </div>
      <div style={{position: 'absolute', left: x + 30, top: TOP + BOX_H - 52, maxWidth: BOX_W - 60, fontFamily: CLAUDE_FONT.ui, fontSize: 24, color: MUTE, opacity: g}}>
        {d.cite}
      </div>
    </>
  );

  const axisIn = win(p, 0.6, 0.78);
  const markIn = win(p, 0.78, 0.92);

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {block(SAFE.x, data.left, win(p, 0.08, 0.32), false)}
      {block(SAFE.x + BOX_W + 88, data.right, win(p, 0.36, 0.6), true)}

      {/* the date axis — the fact half has a position in time; the opinion half does not */}
      <div style={{position: 'absolute', left: SAFE.x, top: AXIS, width: SAFE.w * axisIn, height: 2, backgroundColor: RULE}} />
      <div style={{position: 'absolute', left: markX, top: AXIS - 26, width: 4, height: 54 * markIn, backgroundColor: CLAUDE.SPARK}} />
      {/* ABOVE the rule, not straddling it: at AXIS - 34 with a 48px face the
          date sat centred on the axis line and the rule struck through it
          (QC defect, caught at frame level). AXIS - 86 clears it. */}
      <div
        style={{
          position: 'absolute', left: markX + 20, top: AXIS - 86,
          fontFamily: CLAUDE_FONT.serif, fontSize: 48, color: CLAUDE.SPARK, opacity: markIn,
          whiteSpace: 'nowrap' as const,
        }}
      >
        {data.marker}
      </div>
      <div
        style={{
          position: 'absolute', left: markX + 20, top: AXIS + 26, maxWidth: SAFE.r - markX - 40,
          fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: MUTE, opacity: markIn,
        }}
      >
        {data.axisLabel}
      </div>

      <NoteLine note={data.note} opacity={win(p, 0.9, 0.98)} />
    </PlainStage>
  );
};
