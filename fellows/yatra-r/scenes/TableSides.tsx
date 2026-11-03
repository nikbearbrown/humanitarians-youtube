/**
 * TableSides.tsx — reel-local scenes for `yatra-both-sides-of-the-table`
 * ("Both Sides of the Table." — hiring as a standoff between two AIs).
 *
 * ── WHY THESE ARE NEW COMPONENTS ─────────────────────────────────────────────
 * The human asked for a video that is not a variation of any previous one. Nothing from
 * the `Msk*`, `Itm*`, `Wk*`, `Lnk*`, `Rcp*`, `Seo*`, `Ytw*` or `Jdg*` families is reused
 * or re-exported. The shapes come from this reel's own argument: a frame with two sides
 * that fill one at a time, a table whose only live exchange runs between the two
 * machines, and a resume with a second layer of text addressed to a reader who isn't
 * human.
 *
 * ── THE SOURCING CONSTRAINT, ENFORCED BY THE TYPES ───────────────────────────
 * Seven figures were supplied with their citations, from FIVE different publishers, and
 * the instruction was to cite them as given and alter nothing. So:
 *
 *   Every scene that renders a figure REQUIRES a `source` string.
 *
 * `TblSide`, `TblInterview`, `TblWalk`, `TblInject` each require one, and `TblTrust`
 * requires a SEPARATE source on each of its two figures — they come from different
 * studies and are never allowed to share a citation or be merged into one claim.
 * `SourceLine` always renders in MUTE, never in the accent.
 *
 * ── THE `value` / `bar` SPLIT (a bug this codebase has already paid for) ─────
 * `value` is a STRING printed verbatim and `bar` is a SEPARATE number that drives any
 * drawing. They are deliberately not derived from one another, for two reasons:
 *
 *   1. "4 in 5" is not a percentage and must never be rendered as "80%" on screen,
 *      even though its bar is drawn at 80. The supplied form is the published form.
 *   2. An earlier reel in this series shipped a bug where the house num() helper read
 *      a range like "4–13%" as 413 and drew a bar nine times its own track. Nothing
 *      here parses a displayed string, so that class of bug cannot recur.
 *
 * ── TWO MORE REFUSALS ────────────────────────────────────────────────────────
 *
 * 1. **No remainder is ever captioned.** `TblTrust`'s 26% leaves 74% of its track
 *    visibly unfilled, and that remainder carries no label. 100 − 26 is arithmetic,
 *    not a published figure, and this reel does not print arithmetic as if it were data.
 * 2. **`TblInject` requires a `stamp`.** The 41% is self-reported — what candidates
 *    *admit to* — and the qualifier renders against the figure rather than in a footnote.
 *
 * `TblInterview` carries the +13-point move as a `delta` string with a REQUIRED
 * `deltaNote`, because only the change was supplied: the earlier value is not shown,
 * and the component says so on screen rather than inferring 50% by subtraction.
 *
 * ── ACCENT SEMANTICS ─────────────────────────────────────────────────────────
 * Terracotta is the ONE accent per beat and it always marks THE DISTRUST — the share who
 * walked away, the share who don't think it's fair, the hidden instructions, the humans
 * left waiting. Adoption figures stay in plain ink: the reel is not about how fast AI
 * arrived, it is about nobody believing the result.
 */
import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {SAFE} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {PlainStage, Head, RULE, MUTE, win} from './claudeStage';

const useP = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));
};

const NoteLine: React.FC<{note: string; opacity: number; accent?: boolean}> = ({note, opacity, accent}) => (
  <div
    style={{
      position: 'absolute', left: SAFE.x, top: SAFE.b - 62, width: SAFE.w,
      fontFamily: CLAUDE_FONT.serif, fontSize: 40,
      color: accent ? CLAUDE.SPARK : CLAUDE.INK, opacity, lineHeight: 1.2,
    }}
  >
    {note}
  </div>
);

/** Provenance. Always MUTE, never the accent. */
const SourceLine: React.FC<{source: string; opacity: number; top?: number; left?: number; width?: number}> =
({source, opacity, top, left, width}) => (
  <div
    style={{
      position: 'absolute', left: left ?? SAFE.x, top: top ?? SAFE.b - 128,
      width: width ?? SAFE.w,
      fontFamily: CLAUDE_FONT.ui, fontSize: 25, color: MUTE, opacity, lineHeight: 1.3,
    }}
  >
    Source: {source}
  </div>
);

const Eyebrow: React.FC<{text: string; opacity?: number}> = ({text, opacity = 1}) => (
  <div
    style={{
      position: 'absolute', left: SAFE.x, top: SAFE.y + 6, width: SAFE.w,
      fontFamily: CLAUDE_FONT.ui, fontSize: 22, letterSpacing: '.18em',
      color: MUTE, fontWeight: 600, opacity,
    }}
  >
    {text.toUpperCase()}
  </div>
);

const Chip: React.FC<{
  text: string; left: number; top: number; hot?: boolean; opacity: number; size?: number;
}> = ({text, left, top, hot, opacity, size = 22}) => (
  <div
    style={{
      position: 'absolute', left, top, opacity,
      fontFamily: CLAUDE_FONT.ui, fontSize: size, fontWeight: 600,
      letterSpacing: '.16em', textTransform: 'uppercase' as const,
      color: hot ? CLAUDE.SPARK : MUTE,
      border: `1px solid ${hot ? CLAUDE.SPARK : RULE}`,
      padding: '9px 16px', display: 'inline-block', whiteSpace: 'nowrap' as const,
    }}
  >
    {text}
  </div>
);

/* ═══════════════════════════════════════════════════════════════════════════
   B01 — TblBluf: three claims, alternating sides, pivoting to the middle.

   EXECUTIVE-SUMMARY LAW. The first two claims sit on opposite sides of the frame
   because the reel's subject is two sides; the third lands and takes the accent,
   because "neither side trusts it" is the actual thesis.
   ═══════════════════════════════════════════════════════════════════════════ */
export type BlufData = {
  slideMeta: string;
  claims: {label: string; align: 'left' | 'right'}[];
  hotIndex: number;
  closer: string;
};

export const TblBluf: React.FC<{data: BlufData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 160;
  const STEP = 230;
  const COL_W = 1060;

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.16)} />
      {data.claims.map((c, i) => {
        const g = win(p, 0.08 + i * 0.26, 0.34 + i * 0.26);
        const hot = i === data.hotIndex;
        const y = TOP + i * STEP;
        const right = c.align === 'right';
        const x = right ? SAFE.r - COL_W : SAFE.x;
        return (
          <React.Fragment key={i}>
            <div
              style={{
                position: 'absolute', left: right ? SAFE.r - 8 : SAFE.x, top: y,
                width: 8, height: 150 * g,
                backgroundColor: hot ? CLAUDE.SPARK : RULE,
              }}
            />
            <div
              style={{
                position: 'absolute', left: x, top: y, width: COL_W,
                textAlign: right ? 'right' : 'left',
                paddingRight: right ? 40 : 0, paddingLeft: right ? 0 : 40,
                boxSizing: 'border-box',
                fontFamily: CLAUDE_FONT.serif, fontSize: 76, lineHeight: 1.16,
                color: hot ? CLAUDE.SPARK : CLAUDE.INK, opacity: g,
                transform: `translateY(${(1 - g) * 18}px)`,
              }}
            >
              {c.label}
            </div>
          </React.Fragment>
        );
      })}
      <NoteLine note={data.closer} opacity={win(p, 0.86, 0.97)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B02 / B03 — TblSide: one side of the table fills at a time.

   REQUIRES a `source`. `value` prints verbatim ("86%", "4 in 5" — the latter is NEVER
   converted to a percentage) and `bar` is the separate number that fills the track.
   The opposite side of the frame stays drawn but faint, so the viewer always sees that
   this is one half of a pair.

   Shared by two beats, so its registered duration is the SHORTER of the two: the render
   script freeze-extends a clip shorter than its beat (lossless) while compile.py trims
   one that is longer (lossy), and this scene's source line lands at ~88% of the span.
   ═══════════════════════════════════════════════════════════════════════════ */
export type SideData = {
  slideMeta: string;
  side: 'left' | 'right';
  head: string;
  /** printed VERBATIM — "4 in 5" stays "4 in 5" */
  value: string;
  /** SEPARATE from `value`; nothing ever parses the string */
  bar: number;
  label: string;
  qualifier: string;
  /** REQUIRED */
  source: string;
  note: string;
};

export const TblSide: React.FC<{data: SideData}> = ({data}) => {
  const p = useP();
  const isLeft = data.side === 'left';
  const COL_W = 790;
  const ACTIVE_X = isLeft ? SAFE.x : SAFE.r - COL_W;
  const GHOST_X = isLeft ? SAFE.r - COL_W : SAFE.x;
  const TOP = SAFE.y + 170;

  const fill = win(p, 0.42, 0.68);
  const set = win(p, 0.26, 0.46);

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />

      {/* the other side of the table: present, but not this beat's subject */}
      <div
        style={{
          position: 'absolute', left: GHOST_X, top: TOP, width: COL_W, height: 520,
          border: `1px dashed ${RULE}`, borderRadius: 14, opacity: 0.5,
        }}
      />
      <div
        style={{
          position: 'absolute', left: GHOST_X, top: TOP + 540, width: COL_W,
          textAlign: 'center', fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE,
          opacity: 0.55,
        }}
      >
        the other side of the table
      </div>

      {/* this beat's side */}
      <div
        style={{
          position: 'absolute', left: ACTIVE_X, top: TOP, width: COL_W,
          fontFamily: CLAUDE_FONT.ui, fontSize: 28, letterSpacing: '.14em',
          color: MUTE, fontWeight: 600, opacity: win(p, 0.06, 0.2),
        }}
      >
        {data.head.toUpperCase()}
      </div>
      <div
        style={{
          position: 'absolute', left: ACTIVE_X, top: TOP + 60, width: COL_W,
          fontFamily: CLAUDE_FONT.serif, fontSize: 190, lineHeight: 1,
          color: CLAUDE.INK, opacity: set, transform: `translateY(${(1 - set) * 20}px)`,
        }}
      >
        {data.value}
      </div>
      {/* the track: driven by `bar`, never by the string above it */}
      <div style={{position: 'absolute', left: ACTIVE_X, top: TOP + 280, width: COL_W, height: 54, border: `1px solid ${RULE}`, boxSizing: 'border-box'}} />
      <div
        style={{
          position: 'absolute', left: ACTIVE_X + 1, top: TOP + 281,
          width: (COL_W - 2) * (data.bar / 100) * fill, height: 52,
          backgroundColor: CLAUDE.INK, opacity: 0.85,
        }}
      />
      <div
        style={{
          position: 'absolute', left: ACTIVE_X, top: TOP + 356, width: COL_W,
          fontFamily: CLAUDE_FONT.ui, fontSize: 34, color: CLAUDE.INK, lineHeight: 1.3,
          opacity: win(p, 0.56, 0.72),
        }}
      >
        {data.label}
      </div>
      <Chip text={data.qualifier} left={ACTIVE_X} top={TOP + 470} opacity={win(p, 0.68, 0.82)} size={24} />

      <SourceLine source={data.source} opacity={win(p, 0.8, 0.92)} />
      <NoteLine note={data.note} opacity={win(p, 0.88, 0.98)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B05 — TblTable: four seats, one exchange.

   The ask→result pair's RESULT, and numeral-free by construction — there is no numeric
   prop on this type at all. The two human seats are pushed BACK from the table and
   dimmed (never below the legibility floor) while traffic runs only between the two
   machine seats. The arrangement is the argument.
   ═══════════════════════════════════════════════════════════════════════════ */
export type TableData = {
  slideMeta: string;
  title: string;
  leftOuter: string;
  leftInner: string;
  rightInner: string;
  rightOuter: string;
  trafficLabel: string;
  verdict: string;
  note: string;
};

export const TblTable: React.FC<{data: TableData}> = ({data}) => {
  const p = useP();
  const MID_Y = SAFE.y + 430;
  const TABLE_X = SAFE.x + 430;
  const TABLE_W = 868;
  const seatW = 360;

  const draw = win(p, 0.06, 0.2);
  const leftIn = win(p, 0.18, 0.36);
  const rightIn = win(p, 0.34, 0.52);
  const traffic = win(p, 0.56, 0.78);
  const pushBack = win(p, 0.74, 0.9);

  const seat = (x: number, y: number, label: string, g: number, machine: boolean, dim: number) => (
    <div
      style={{
        position: 'absolute', left: x, top: y, width: seatW, minHeight: 112,
        boxSizing: 'border-box',
        border: `2px solid ${machine ? CLAUDE.INK : RULE}`,
        backgroundColor: '#FFFFFF', borderRadius: 12,
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        padding: '14px 18px', textAlign: 'center',
        fontFamily: CLAUDE_FONT.ui, fontSize: 32, lineHeight: 1.22,
        color: CLAUDE.INK, opacity: g * dim,
      }}
    >
      {label}
    </div>
  );

  /* humans never drop below the ~40% legibility floor */
  const humanDim = 1 - 0.42 * pushBack;

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />

      {/* QC: the table sits ON the machine row, spanning between the two machine
          seats, so the exchange runs ACROSS its surface. Floating it above that row
          left an empty white box that read as a missing element rather than a table. */}
      <div
        style={{
          position: 'absolute', left: SAFE.x + 400, top: MID_Y + 86,
          width: (SAFE.r - 400 - (SAFE.x + 400)) * draw, height: 100,
          backgroundColor: '#FFFFFF', border: `2px solid ${CLAUDE.INK}`, borderRadius: 10,
        }}
      />

      {/* outer seats = the humans, pushed back as the beat lands */}
      {seat(SAFE.x, MID_Y - 56 - 150 * pushBack, data.leftOuter, draw, false, humanDim)}
      {seat(SAFE.r - seatW, MID_Y - 56 - 150 * pushBack, data.rightOuter, draw, false, humanDim)}

      {/* inner seats = the machines, at the table */}
      {seat(SAFE.x + 400 - 360, MID_Y + 80, data.leftInner, leftIn, true, 1)}
      {seat(SAFE.r - 400, MID_Y + 80, data.rightInner, rightIn, true, 1)}

      {/* the only live exchange: machine ↔ machine */}
      <div
        style={{
          position: 'absolute', left: SAFE.x + 400, top: MID_Y + 132,
          width: (SAFE.r - 400 - (SAFE.x + 400)) * traffic, height: 5,
          backgroundColor: CLAUDE.SPARK, opacity: 0.9,
        }}
      />
      <div
        style={{
          position: 'absolute', left: SAFE.x + 400, top: MID_Y + 206,
          width: SAFE.r - 400 - (SAFE.x + 400), textAlign: 'center',
          fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: CLAUDE.SPARK,
          opacity: win(p, 0.66, 0.8),
        }}
      >
        {data.trafficLabel}
      </div>

      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 148, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 54, color: CLAUDE.SPARK,
          opacity: win(p, 0.86, 0.96),
        }}
      >
        {data.verdict}
      </div>
      <NoteLine note={data.note} opacity={win(p, 0.92, 1.0)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B06 — TblInterview: a figure and its six-month move.

   REQUIRES `source` AND `deltaNote`. Only the CHANGE was published, so the earlier
   value is never drawn and never implied: there is no `previous` prop, and the note
   states on screen that the prior figure isn't shown. Subtracting 13 from 63 would be
   arithmetic presented as data, which this reel does not do.
   ═══════════════════════════════════════════════════════════════════════════ */
export type InterviewData = {
  slideMeta: string;
  value: string;
  bar: number;
  label: string;
  delta: string;
  /** REQUIRED — says on screen why no earlier value appears */
  deltaNote: string;
  /** REQUIRED */
  source: string;
  note: string;
};

export const TblInterview: React.FC<{data: InterviewData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 170;
  const set = win(p, 0.06, 0.26);
  const fill = win(p, 0.3, 0.52);

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />

      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 230, lineHeight: 1,
          color: CLAUDE.INK, opacity: set, transform: `translateY(${(1 - set) * 22}px)`,
        }}
      >
        {data.value}
      </div>
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP + 258, width: SAFE.w * 0.78,
          fontFamily: CLAUDE_FONT.ui, fontSize: 40, color: CLAUDE.INK, lineHeight: 1.28,
          opacity: win(p, 0.24, 0.42),
        }}
      >
        {data.label}
      </div>

      <div style={{position: 'absolute', left: SAFE.x, top: TOP + 360, width: SAFE.w, height: 48, border: `1px solid ${RULE}`, boxSizing: 'border-box'}} />
      <div
        style={{
          position: 'absolute', left: SAFE.x + 1, top: TOP + 361,
          width: (SAFE.w - 2) * (data.bar / 100) * fill, height: 46,
          backgroundColor: CLAUDE.INK, opacity: 0.85,
        }}
      />

      {/* the move: only the delta is shown, because only the delta was published */}
      <Chip text={data.delta} left={SAFE.x} top={TOP + 450} hot opacity={win(p, 0.6, 0.76)} size={30} />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP + 530, width: SAFE.w * 0.86,
          fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE, lineHeight: 1.3,
          opacity: win(p, 0.72, 0.86),
        }}
      >
        {data.deltaNote}
      </div>

      <SourceLine source={data.source} opacity={win(p, 0.82, 0.92)} />
      <NoteLine note={data.note} opacity={win(p, 0.9, 0.99)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B07 — TblWalk: the share that LEFT.

   REQUIRES a `source`. The motion matters to the claim: the marks move OUT of the row
   rather than being filtered out of it, because these candidates withdrew — they were
   not rejected. The `verdict` makes that distinction explicit on screen.
   ═══════════════════════════════════════════════════════════════════════════ */
export type WalkData = {
  slideMeta: string;
  value: string;
  bar: number;
  label: string;
  verdict: string;
  /** REQUIRED */
  source: string;
  note: string;
};

const WALK_MARKS = 25;

export const TblWalk: React.FC<{data: WalkData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 230;
  const leave = win(p, 0.34, 0.6);
  /* how many of the marks depart — from `bar`, never from the value string */
  const leaving = Math.round((data.bar / 100) * WALK_MARKS);

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />

      {Array.from({length: WALK_MARKS}).map((_, i) => {
        const goes = i >= WALK_MARKS - leaving;
        const g = win(p, 0.06 + i * 0.006, 0.2 + i * 0.006);
        const off = goes ? leave : 0;
        return (
          <div
            key={i}
            style={{
              position: 'absolute',
              left: SAFE.x + i * 66,
              top: TOP + off * 150,
              width: 46, height: 92, borderRadius: 8,
              backgroundColor: goes && leave > 0.1 ? CLAUDE.SPARK : CLAUDE.INK,
              opacity: (goes ? 1 - 0.45 * off : 0.82) * g,
            }}
          />
        );
      })}

      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP + 280, width: 620,
          fontFamily: CLAUDE_FONT.serif, fontSize: 200, lineHeight: 1,
          color: CLAUDE.SPARK, opacity: win(p, 0.5, 0.68),
        }}
      >
        {data.value}
      </div>
      <div
        style={{
          position: 'absolute', left: SAFE.x + 660, top: TOP + 300, width: SAFE.w - 660,
          fontFamily: CLAUDE_FONT.ui, fontSize: 38, color: CLAUDE.INK, lineHeight: 1.3,
          opacity: win(p, 0.6, 0.76),
        }}
      >
        {data.label}
      </div>
      <div
        style={{
          position: 'absolute', left: SAFE.x + 660, top: TOP + 420, width: SAFE.w - 660,
          fontFamily: CLAUDE_FONT.serif, fontSize: 52, color: CLAUDE.SPARK,
          opacity: win(p, 0.8, 0.92),
        }}
      >
        {data.verdict}
      </div>

      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} />
      <NoteLine note={data.note} opacity={win(p, 0.9, 0.99)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B08 — TblTrust: two figures from two studies, held side by side.

   Each figure carries its OWN required `source`, rendered beneath its own column. They
   are never merged, never added and never captioned as one finding — they measure
   different populations and answer different questions.

   The unfilled remainder of each track is deliberately left UNLABELLED: 100 − 26 is
   arithmetic, not a published figure, and this reel does not print arithmetic as data.
   ═══════════════════════════════════════════════════════════════════════════ */
export type TrustFigure = {
  value: string;
  bar: number;
  label: string;
  /** REQUIRED, and per-figure — these come from different studies */
  source: string;
};

export type TrustData = {
  slideMeta: string;
  title: string;
  left: TrustFigure;
  right: TrustFigure;
  note: string;
};

export const TblTrust: React.FC<{data: TrustData}> = ({data}) => {
  const p = useP();
  const COL_W = 790;
  const L_X = SAFE.x;
  const R_X = SAFE.r - COL_W;
  const TOP = SAFE.y + 250;

  const col = (x: number, f: TrustFigure, at: number) => {
    const set = win(p, at, at + 0.16);
    const fill = win(p, at + 0.1, at + 0.3);
    return (
      <>
        <div
          style={{
            position: 'absolute', left: x, top: TOP, width: COL_W,
            fontFamily: CLAUDE_FONT.serif, fontSize: 170, lineHeight: 1,
            color: CLAUDE.SPARK, opacity: set, transform: `translateY(${(1 - set) * 18}px)`,
          }}
        >
          {f.value}
        </div>
        <div style={{position: 'absolute', left: x, top: TOP + 200, width: COL_W, height: 46, border: `1px solid ${RULE}`, boxSizing: 'border-box'}} />
        <div
          style={{
            position: 'absolute', left: x + 1, top: TOP + 201,
            width: (COL_W - 2) * (f.bar / 100) * fill, height: 44,
            backgroundColor: CLAUDE.SPARK, opacity: 0.85,
          }}
        />
        <div
          style={{
            position: 'absolute', left: x, top: TOP + 272, width: COL_W,
            fontFamily: CLAUDE_FONT.ui, fontSize: 32, color: CLAUDE.INK, lineHeight: 1.3,
            opacity: win(p, at + 0.18, at + 0.34),
          }}
        >
          {f.label}
        </div>
        {/* each figure's own citation, under its own column */}
        <SourceLine source={f.source} opacity={win(p, at + 0.3, at + 0.44)} top={TOP + 430} left={x} width={COL_W} />
      </>
    );
  };

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {col(L_X, data.left, 0.08)}
      {col(R_X, data.right, 0.44)}
      <NoteLine note={data.note} opacity={win(p, 0.9, 0.99)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B09 — TblInject: the layer written for the machine.

   REQUIRES `source` AND `stamp`. The hidden text fades up INSIDE the page rather than
   being added to it, because the claim is that it was there all along and simply wasn't
   visible to a human reader. `visibleLines` are generic resume headings — no invented
   candidate, employer or injected string is ever rendered.
   ═══════════════════════════════════════════════════════════════════════════ */
export type InjectData = {
  slideMeta: string;
  value: string;
  bar: number;
  label: string;
  /** REQUIRED — the figure is self-reported */
  stamp: string;
  visibleLines: string[];
  hiddenLabel: string;
  /** REQUIRED */
  source: string;
  note: string;
};

export const TblInject: React.FC<{data: InjectData}> = ({data}) => {
  const p = useP();
  const PAGE_X = SAFE.x;
  const PAGE_W = 700;
  const PAGE_Y = SAFE.y + 150;
  const PAGE_H = 600;
  const draw = win(p, 0.06, 0.24);
  const hidden = win(p, 0.36, 0.58);

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />

      {/* an ordinary page */}
      <div
        style={{
          position: 'absolute', left: PAGE_X, top: PAGE_Y, width: PAGE_W, height: PAGE_H,
          backgroundColor: '#FFFFFF', border: `1px solid ${CLAUDE.BORDER}`, borderRadius: 10,
          opacity: draw,
        }}
      />
      {data.visibleLines.map((ln, i) => (
        <React.Fragment key={i}>
          <div
            style={{
              position: 'absolute', left: PAGE_X + 44, top: PAGE_Y + 54 + i * 170,
              fontFamily: CLAUDE_FONT.ui, fontSize: 30, fontWeight: 600, color: CLAUDE.INK,
              opacity: win(p, 0.1 + i * 0.04, 0.26 + i * 0.04),
            }}
          >
            {ln}
          </div>
          {[0, 1, 2].map((k) => (
            <div
              key={k}
              style={{
                position: 'absolute', left: PAGE_X + 44, top: PAGE_Y + 102 + i * 170 + k * 26,
                width: (PAGE_W - 120) * (k === 2 ? 0.62 : 1), height: 10, borderRadius: 3,
                backgroundColor: CLAUDE.INK, opacity: 0.16 * win(p, 0.12 + i * 0.04, 0.3 + i * 0.04),
              }}
            />
          ))}
        </React.Fragment>
      ))}

      {/* the layer that was always there and simply wasn't visible */}
      <div
        style={{
          position: 'absolute', left: PAGE_X + 44, top: PAGE_Y + 430, width: PAGE_W - 88,
          padding: '18px 20px', boxSizing: 'border-box',
          border: `2px dashed ${CLAUDE.SPARK}`, borderRadius: 8,
          fontFamily: CLAUDE_FONT.mono, fontSize: 24, lineHeight: 1.35,
          color: CLAUDE.SPARK, opacity: hidden,
        }}
      >
        {data.hiddenLabel}
      </div>

      {/* the figure */}
      <div
        style={{
          position: 'absolute', left: PAGE_X + PAGE_W + 100, top: PAGE_Y + 40, width: 800,
          fontFamily: CLAUDE_FONT.serif, fontSize: 200, lineHeight: 1,
          color: CLAUDE.SPARK, opacity: win(p, 0.66, 0.82),
        }}
      >
        {data.value}
      </div>
      <div
        style={{
          position: 'absolute', left: PAGE_X + PAGE_W + 100, top: PAGE_Y + 250, width: 800,
          fontFamily: CLAUDE_FONT.ui, fontSize: 34, color: CLAUDE.INK, lineHeight: 1.3,
          opacity: win(p, 0.74, 0.88),
        }}
      >
        {data.label}
      </div>
      <Chip text={data.stamp} left={PAGE_X + PAGE_W + 100} top={PAGE_Y + 420} opacity={win(p, 0.8, 0.92)} size={24} />

      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} />
      <NoteLine note={data.note} opacity={win(p, 0.9, 0.99)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B10 — TblLimits: being exact about figures from five different publishers.

   The FALSIFIABILITY beat. `provenance` and `falsifier` are both REQUIRED, and the
   provenance line lists EVERY source behind the reel rather than a representative one —
   the whole risk with this episode is that six figures from five publishers get read as
   one coherent dataset.
   ═══════════════════════════════════════════════════════════════════════════ */
export type LimitsData = {
  slideMeta: string;
  title: string;
  claims: {heading: string; items: string[]};
  refusals: {heading: string; items: string[]};
  /** REQUIRED — every source, not a representative one */
  provenance: string;
  /** REQUIRED */
  falsifier: string;
};

export const TblLimits: React.FC<{data: LimitsData}> = ({data}) => {
  const p = useP();
  const COL_W = 806;
  const L_X = SAFE.x;
  const R_X = SAFE.x + 922;
  const HEAD_Y = SAFE.y + 230;
  const ITEM_Y = SAFE.y + 304;
  const STEP = 136;

  const ledger = (x: number, heading: string, items: string[], startAt: number, hot: boolean) => (
    <>
      <div
        style={{
          position: 'absolute', left: x, top: HEAD_Y, width: COL_W,
          fontFamily: CLAUDE_FONT.ui, fontSize: 27, letterSpacing: '.16em', fontWeight: 600,
          color: hot ? CLAUDE.SPARK : MUTE, opacity: win(p, startAt, startAt + 0.08),
        }}
      >
        {heading.toUpperCase()}
      </div>
      <div
        style={{
          position: 'absolute', left: x, top: HEAD_Y + 44,
          width: COL_W * win(p, startAt, startAt + 0.12), height: 2,
          backgroundColor: hot ? CLAUDE.SPARK : RULE,
        }}
      />
      {items.map((it, i) => {
        const g = win(p, startAt + 0.05 + i * 0.07, startAt + 0.2 + i * 0.07);
        return (
          <div
            key={i}
            style={{
              position: 'absolute', left: x, top: ITEM_Y + i * STEP, width: COL_W,
              fontFamily: CLAUDE_FONT.ui, fontSize: 34, lineHeight: 1.32,
              color: hot ? CLAUDE.SPARK : CLAUDE.INK,
              opacity: g, transform: `translateY(${(1 - g) * 12}px)`,
            }}
          >
            · {it}
          </div>
        );
      })}
    </>
  );

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {ledger(L_X, data.claims.heading, data.claims.items, 0.08, false)}
      {ledger(R_X, data.refusals.heading, data.refusals.items, 0.44, true)}

      <div style={{position: 'absolute', left: SAFE.x, top: SAFE.b - 196, width: SAFE.w * win(p, 0.76, 0.86), height: 1, backgroundColor: RULE}} />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 176, width: SAFE.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 25, color: MUTE, lineHeight: 1.36,
          opacity: win(p, 0.78, 0.9),
        }}
      >
        {data.provenance}
      </div>
      <NoteLine note={data.falsifier} opacity={win(p, 0.9, 0.99)} />
    </PlainStage>
  );
};
