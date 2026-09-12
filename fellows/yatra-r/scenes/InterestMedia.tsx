/**
 * InterestMedia.tsx — reel-local scenes for `yatra-interest-media`
 * ("Interest Media." — the shift from follower-sorted feeds to interest-sorted ones,
 * built on a concept the human credits to Gary Vaynerchuk).
 *
 * ── WHY THESE ARE NEW COMPONENTS ─────────────────────────────────────────────
 * The human asked for a video that is not a variation of any previous one, and
 * re-skinning the `Wk*`, `Lnk*`, `Rcp*`, `Seo*` or `Jdg*` families is exactly what
 * that would have been. Nothing is reused here. The shapes are driven by what makes
 * THIS reel's argument move: a machine whose sort key is swapped out mid-beat, a
 * track with a gate on it and a track without one, and a field of posts dense enough
 * that a network visibly cannot sort it.
 *
 * ── TWO CONSTRAINTS, ENFORCED BY THE TYPES ───────────────────────────────────
 *
 * 1. NEVER QUOTED. The framing is Gary Vaynerchuk's and the human's instruction was
 *    explicit: credit him, do not quote him — the script is already a paraphrase.
 *
 *      `SourceData` has a `claimParaphrase` field and NO `quote` field.
 *
 *    There is no prop on any component in this file that renders quotation marks
 *    around attributed words, and `ItmSource` requires a `stamp` which the reel sets
 *    to "paraphrased — not a quote" and renders directly beneath the attribution.
 *    A component that *can* render a quote will eventually be given one.
 *
 * 2. NUMERAL-FREE BY CONSTRUCTION. The human has asked across this whole series not
 *    to invent statistics, and this reel supplies no verified figures at all — so it
 *    claims none. Every type in this file carries only strings that are rendered
 *    verbatim; there is no `value`, `pct`, `count`, `bar` or `stat` prop anywhere,
 *    and nothing in this file computes a number and prints it.
 *
 *    The one place a count could have leaked is `ItmVolume`, whose whole subject is
 *    "too much content to sort". Its marks are deliberately UNLABELLED and UNCOUNTED:
 *    the scene argues density, never a figure, and there is no prop by which a total
 *    could be captioned. Same for `ItmJob`'s tick row — marks, not a tally.
 *
 * ── ACCENT SEMANTICS ─────────────────────────────────────────────────────────
 * Terracotta is the ONE accent per beat and it always marks THE INTEREST SIDE of the
 * shift: the new sort key, the word INTEREST, the match node that replaced the gate,
 * the question that retired the old one. Attribution and provenance stay muted ink —
 * the credit is never dressed up as the point.
 */
import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {SAFE} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {PlainStage, Head, RULE, MUTE, win} from './claudeStage';

/** progress through the beat, 0..1 */
const useP = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));
};

/**
 * Deterministic pseudo-random in [0,1) from an integer seed. Remotion renders every
 * frame independently and may render them out of order, so Math.random() would make
 * the field of posts in ItmVolume flicker. Same seed → same layout, every frame,
 * every render.
 */
export const rnd = (seed: number): number => {
  const x = Math.sin(seed * 127.1 + 311.7) * 43758.5453;
  return x - Math.floor(x);
};

const NoteLine: React.FC<{note: string; opacity: number; accent?: boolean}> = ({note, opacity, accent}) => (
  <div
    style={{
      position: 'absolute', left: SAFE.x, top: SAFE.b - 62, width: SAFE.w,
      fontFamily: CLAUDE_FONT.serif, fontSize: 42,
      color: accent ? CLAUDE.SPARK : CLAUDE.INK, opacity,
    }}
  >
    {note}
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

/** A small bordered chip. `hot` is the reel's one accent per beat. */
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
   B01 — ItmBluf: the whole idea as three claims that land in order.

   EXECUTIVE-SUMMARY LAW: the gist before any specific. `hotIndex` picks the ONE
   claim that carries the thesis (here: "it runs on what you're interested in"),
   so the accent states the point up front rather than saving it for the body.
   Each claim gets a rule that GROWS as it lands — the stack builds, it doesn't
   just fade in, so the beat cannot be exported as a static slide.
   ═══════════════════════════════════════════════════════════════════════════ */
export type BlufData = {
  slideMeta: string;
  claims: {label: string}[];
  hotIndex: number;
  closer: string;
};

export const ItmBluf: React.FC<{data: BlufData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 150;
  const STEP = 240;

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.16)} />

      {data.claims.map((c, i) => {
        const g = win(p, 0.08 + i * 0.28, 0.34 + i * 0.28);
        const hot = i === data.hotIndex;
        const y = TOP + i * STEP;
        return (
          <React.Fragment key={i}>
            {/* the rule grows with the claim — the stack builds itself */}
            <div
              style={{
                position: 'absolute', left: SAFE.x, top: y,
                width: 8, height: 150 * g,
                backgroundColor: hot ? CLAUDE.SPARK : RULE,
              }}
            />
            <div
              style={{
                position: 'absolute', left: SAFE.x + 56, top: y, width: SAFE.w - 56,
                fontFamily: CLAUDE_FONT.serif, fontSize: 78, lineHeight: 1.16,
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
   B02 — ItmSource: who this idea belongs to, then the rename it implies.

   ATTRIBUTION beat. `claimParaphrase` is a paraphrase and is typed as one — there
   is no `quote` prop and no quotation marks are rendered anywhere in this component,
   so the source cannot be made to say words he did not say. The `stamp` sits directly
   under the attribution so the disclaimer travels with the credit.

   The rename runs as a SIDE-BY-SIDE comparison (SHOW-DON'T-TELL: comparisons sort
   visibly, held on screen) — old word struck on the left, new word in the accent on
   the right, each carrying the question its model asks.
   ═══════════════════════════════════════════════════════════════════════════ */
export type SourceData = {
  slideMeta: string;
  who: string;
  /** a PARAPHRASE — deliberately not a `quote` field, and never rendered in quotes */
  claimParaphrase: string;
  stamp: string;
  oldWord: string;
  newWord: string;
  tail: string;
  oldAsks: string;
  newAsks: string;
  note: string;
};

export const ItmSource: React.FC<{data: SourceData}> = ({data}) => {
  const p = useP();
  const card = win(p, 0.06, 0.24);
  const band = win(p, 0.18, 0.36);
  const strike = win(p, 0.44, 0.60);
  const arrive = win(p, 0.56, 0.72);
  const qOld = win(p, 0.72, 0.84);
  const qNew = win(p, 0.86, 0.96);

  const COL_W = 800;
  const R_X = SAFE.x + 928;
  /* QC: the rename row sits low enough that the beat fills SAFE rather than
     clustering under the attribution card (FILL-THE-CANVAS LAW). */
  const ROW_Y = SAFE.y + 540;

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={card} />

      {/* ── attribution card — muted ink, never the accent ── */}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.y + 74, width: SAFE.w,
          backgroundColor: '#FFFFFF', border: `1px solid ${CLAUDE.BORDER}`, borderRadius: 14,
          padding: '34px 40px', boxSizing: 'border-box', opacity: card,
          transform: `translateY(${(1 - card) * 16}px)`,
        }}
      >
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: 62, color: CLAUDE.INK, lineHeight: 1.1}}>
          {data.who}
        </div>
        <div
          style={{
            marginTop: 18, fontFamily: CLAUDE_FONT.serif, fontSize: 38, color: MUTE,
            lineHeight: 1.3, maxWidth: SAFE.w - 80, opacity: band,
          }}
        >
          {data.claimParaphrase}
        </div>
      </div>
      <Chip text={data.stamp} left={SAFE.x} top={SAFE.y + 330} opacity={band} />

      {/* ── the rename, side by side ── */}
      {/* old: struck through */}
      <div style={{position: 'absolute', left: SAFE.x, top: ROW_Y, width: COL_W, opacity: card}}>
        <div style={{position: 'relative', display: 'inline-block'}}>
          <span style={{fontFamily: CLAUDE_FONT.serif, fontSize: 96, color: CLAUDE.INK, letterSpacing: '.01em'}}>
            {data.oldWord}
          </span>
          <div
            style={{
              position: 'absolute', left: 0, top: 66,
              width: `${100 * strike}%`, height: 6, backgroundColor: CLAUDE.INK,
            }}
          />
        </div>
        <span style={{fontFamily: CLAUDE_FONT.serif, fontSize: 96, color: MUTE, marginLeft: 22}}>
          {data.tail}
        </span>
      </div>
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: ROW_Y + 168, width: COL_W,
          fontFamily: CLAUDE_FONT.ui, fontSize: 48, color: MUTE, opacity: qOld,
          transform: `translateY(${(1 - qOld) * 12}px)`,
        }}
      >
        {data.oldAsks}
      </div>

      {/* new: THE accent */}
      <div
        style={{
          position: 'absolute', left: R_X, top: ROW_Y, width: COL_W,
          opacity: arrive, transform: `translateY(${(1 - arrive) * 22}px)`,
        }}
      >
        <span style={{fontFamily: CLAUDE_FONT.serif, fontSize: 96, color: CLAUDE.SPARK, letterSpacing: '.01em'}}>
          {data.newWord}
        </span>
        <span style={{fontFamily: CLAUDE_FONT.serif, fontSize: 96, color: MUTE, marginLeft: 22}}>
          {data.tail}
        </span>
      </div>
      <div
        style={{
          position: 'absolute', left: R_X, top: ROW_Y + 168, width: COL_W,
          fontFamily: CLAUDE_FONT.ui, fontSize: 48, color: CLAUDE.INK, opacity: qNew,
          transform: `translateY(${(1 - qNew) * 12}px)`,
        }}
      >
        {data.newAsks}
      </div>

      <NoteLine note={data.note} opacity={win(p, 0.9, 0.99)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B03 — ItmFeed: the worked example, run on the viewer's own feed.

   Two columns held side by side (the legibility contract wants comparisons sorted
   visibly and held). The left column DIMS rather than disappears — it never drops
   below the ~40% opacity floor, because "you stopped seeing these" is the claim,
   not "these ceased to exist". The signal rail is the cause and the terracotta wire
   is the ONE accent: it physically connects the signals to the column they explain.
   ═══════════════════════════════════════════════════════════════════════════ */
export type FeedData = {
  slideMeta: string;
  leftHead: string;
  leftItems: string[];
  leftFoot: string;
  rightHead: string;
  rightItems: string[];
  rightFoot: string;
  signals: string[];
  note: string;
};

export const ItmFeed: React.FC<{data: FeedData}> = ({data}) => {
  const p = useP();
  const COL_W = 800;
  const L_X = SAFE.x;
  const R_X = SAFE.x + 928;
  const HEAD_Y = SAFE.y + 60;
  const CARD_Y = SAFE.y + 130;
  const CARD_H = 118;
  const GAP = 20;
  const RAIL_Y = SAFE.y + 700;

  /* the left column dims as a block, floor 0.42 — dimmed, never illegible */
  const dim = 1 - 0.58 * win(p, 0.32, 0.48);

  const column = (
    x: number, head: string, items: string[], foot: string,
    startAt: number, opacityScale: number, marked: boolean,
  ) => (
    <>
      <div
        style={{
          position: 'absolute', left: x, top: HEAD_Y, width: COL_W,
          fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.14em',
          color: MUTE, fontWeight: 600, opacity: opacityScale * win(p, startAt, startAt + 0.1),
        }}
      >
        {head.toUpperCase()}
      </div>
      {items.map((it, i) => {
        const g = win(p, startAt + 0.04 + i * 0.06, startAt + 0.18 + i * 0.06);
        return (
          <div
            key={i}
            style={{
              position: 'absolute', left: x, top: CARD_Y + i * (CARD_H + GAP), width: COL_W,
              height: CARD_H, boxSizing: 'border-box',
              backgroundColor: '#FFFFFF', border: `1px solid ${CLAUDE.BORDER}`, borderRadius: 12,
              padding: '30px 32px',
              fontFamily: CLAUDE_FONT.serif, fontSize: 44, color: CLAUDE.INK,
              opacity: opacityScale * g, transform: `translateY(${(1 - g) * 14}px)`,
              overflow: 'hidden', whiteSpace: 'nowrap', textOverflow: 'ellipsis',
            }}
          >
            {it}
          </div>
        );
      })}
      <div
        style={{
          position: 'absolute', left: x, top: CARD_Y + items.length * (CARD_H + GAP) + 14,
          width: COL_W, fontFamily: CLAUDE_FONT.ui, fontSize: 30,
          color: marked ? CLAUDE.INK : MUTE,
          opacity: opacityScale * win(p, startAt + 0.24, startAt + 0.36),
        }}
      >
        {foot}
      </div>
    </>
  );

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />

      {column(L_X, data.leftHead, data.leftItems, data.leftFoot, 0.08, dim, false)}
      {column(R_X, data.rightHead, data.rightItems, data.rightFoot, 0.48, 1, true)}

      {/* ── the signal rail: the cause, lit in spoken order ── */}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: RAIL_Y - 34, width: SAFE.w * win(p, 0.68, 0.78),
          height: 1, backgroundColor: RULE,
        }}
      />
      {data.signals.map((s, i) => (
        <Chip
          key={i}
          text={s}
          left={SAFE.x + i * 300}
          top={RAIL_Y}
          opacity={win(p, 0.70 + i * 0.06, 0.80 + i * 0.06)}
          size={26}
        />
      ))}

      {/* the ONE accent: a wire from the signals up into the column they explain */}
      <div
        style={{
          position: 'absolute', left: R_X + COL_W / 2, top: RAIL_Y + 4,
          width: 5, height: 120 * win(p, 0.86, 0.96),
          backgroundColor: CLAUDE.SPARK, transform: 'translateY(-120px)',
        }}
      />
      <div
        style={{
          position: 'absolute', left: R_X + COL_W / 2 - 60, top: RAIL_Y + 12,
          width: 5 + 60 * win(p, 0.88, 0.97), height: 5,
          backgroundColor: CLAUDE.SPARK, opacity: win(p, 0.88, 0.97),
        }}
      />

      <NoteLine note={data.note} opacity={win(p, 0.9, 0.99)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B04 — ItmVolume: why the old sort key gave out.

   The subject is DENSITY, and density is the one thing here that must not become a
   number. There is no `count`, `perDay` or `total` prop on this type and no caption
   slot a figure could occupy — the marks are unlabelled and the band says "more than
   a network can sort", which is an ordering claim, not a measurement.

   The field is seeded deterministically (see `rnd`) so every frame and every re-render
   places the same marks; only how MANY have arrived changes with progress, which is
   what makes the flood read as motion rather than noise.
   ═══════════════════════════════════════════════════════════════════════════ */
export type VolumeData = {
  slideMeta: string;
  title: string;
  networkLabel: string;
  networkSub: string;
  verdictBand: string;
  note: string;
};

/**
 * Exported so the portrait cut imports the SAME density rather than declaring its
 * own. Nothing counts these marks on screen, but the two cuts of one reel should not
 * silently disagree about how dense "too much" looks.
 */
export const MARKS = 150;
export const NODES = 7;

export const ItmVolume: React.FC<{data: VolumeData}> = ({data}) => {
  const p = useP();
  const flood = win(p, 0.22, 0.80);
  const give = win(p, 0.68, 0.84);
  const bandG = win(p, 0.84, 0.95);

  /* QC: deepened from 560 — the field now runs to the note line instead of
     leaving the bottom third of SAFE empty (FILL-THE-CANVAS LAW). */
  const FIELD_TOP = SAFE.y + 210;
  const FIELD_H = 620;
  const RING_CX = SAFE.x + 300;
  const RING_CY = FIELD_TOP + FIELD_H / 2;
  const RING_R = 130;

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />

      {/* ── the flood: unlabelled, uncounted, deterministic ── */}
      {Array.from({length: MARKS}).map((_, i) => {
        const ax = rnd(i * 3 + 1);
        const ay = rnd(i * 3 + 2);
        const aw = rnd(i * 3 + 3);
        /* each mark has its own arrival point in the flood window */
        const arrive = Math.min(1, Math.max(0, (flood - ax * 0.85) / 0.15));
        if (arrive <= 0) return null;
        const x = SAFE.x + ax * (SAFE.w - 130);
        const y = FIELD_TOP + ay * (FIELD_H - 30);
        return (
          <div
            key={i}
            style={{
              position: 'absolute', left: x, top: y - (1 - arrive) * 90,
              width: 60 + aw * 68, height: 12,
              backgroundColor: CLAUDE.INK, opacity: 0.34 * arrive, borderRadius: 3,
            }}
          />
        );
      })}

      {/* ── the network that can no longer sort ── */}
      <div
        style={{
          position: 'absolute', left: RING_CX - RING_R - 26, top: RING_CY - RING_R - 26,
          width: (RING_R + 26) * 2, height: (RING_R + 26) * 2,
          borderRadius: '50%', backgroundColor: '#F2F0E9',
          border: `1px solid ${RULE}`, opacity: 1 - 0.45 * give,
        }}
      />
      {Array.from({length: NODES}).map((_, i) => {
        const a = (i / NODES) * Math.PI * 2 - Math.PI / 2;
        const g = win(p, 0.04 + i * 0.02, 0.16 + i * 0.02);
        return (
          <div
            key={i}
            style={{
              position: 'absolute',
              left: RING_CX + Math.cos(a) * RING_R - 13,
              top: RING_CY + Math.sin(a) * RING_R - 13,
              width: 26, height: 26, borderRadius: '50%',
              backgroundColor: CLAUDE.INK, opacity: (1 - 0.55 * give) * g,
            }}
          />
        );
      })}
      <div
        style={{
          position: 'absolute', left: RING_CX - 200, top: RING_CY - 34, width: 400,
          textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: 40,
          color: CLAUDE.INK, opacity: (1 - 0.5 * give) * win(p, 0.08, 0.2),
        }}
      >
        {data.networkLabel}
      </div>
      <div
        style={{
          position: 'absolute', left: RING_CX - 200, top: RING_CY + 12, width: 400,
          textAlign: 'center', fontFamily: CLAUDE_FONT.ui, fontSize: 26,
          color: MUTE, opacity: (1 - 0.5 * give) * win(p, 0.1, 0.22),
        }}
      >
        {data.networkSub}
      </div>

      {/* ── the ONE accent: the verdict band lands across the field ── */}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: FIELD_TOP + FIELD_H - 108,
          width: SAFE.w * bandG, height: 92,
          backgroundColor: CLAUDE.SPARK, opacity: 0.97,
          display: 'flex', alignItems: 'center', overflow: 'hidden',
        }}
      >
        <div
          style={{
            fontFamily: CLAUDE_FONT.serif, fontSize: 50, color: '#FFFFFF',
            paddingLeft: 34, whiteSpace: 'nowrap', opacity: win(p, 0.88, 0.96),
          }}
        >
          {data.verdictBand}
        </div>
      </div>

      <NoteLine note={data.note} opacity={win(p, 0.92, 1.0)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B05 — ItmQuestion: same machine, different key.

   The mechanism PERFORMS the sentence (SHOW-DON'T-TELL): the old key is seated in the
   slot and routing runs through it; on "they stopped asking" it lifts out and greys;
   the new key drops in and the routing re-runs. Nothing here is a label change — the
   part that does the sorting is physically swapped, which is the actual claim.
   ═══════════════════════════════════════════════════════════════════════════ */
export type QuestionData = {
  slideMeta: string;
  inputLabel: string;
  outputLabel: string;
  oldKey: string;
  newKey: string;
  note: string;
};

export const ItmQuestion: React.FC<{data: QuestionData}> = ({data}) => {
  const p = useP();
  const draw = win(p, 0.06, 0.22);
  const seat = win(p, 0.22, 0.36);
  const lift = win(p, 0.50, 0.64);
  const drop = win(p, 0.64, 0.78);
  const rerun = win(p, 0.80, 0.96);

  const BOX_X = SAFE.x + 420;
  const BOX_W = 800;
  /* QC: raised and deepened — the machine now occupies the middle of SAFE instead of
     sitting small in it, and the old key has room to lift CLEAR of the box's top edge
     rather than straddling the border (which read as a bug, not a lift). */
  const BOX_Y = SAFE.y + 250;
  const BOX_H = 470;
  const IN_X = SAFE.x;
  const OUT_X = SAFE.x + 1340;
  const COL_W = 388;
  const MID_Y = BOX_Y + BOX_H / 2;

  const stack = (x: number, label: string, g: number, hot: boolean) => (
    <>
      {Array.from({length: 4}).map((_, i) => (
        <div
          key={i}
          style={{
            position: 'absolute', left: x, top: MID_Y - 130 + i * 72,
            width: COL_W, height: 52, borderRadius: 5,
            backgroundColor: hot ? CLAUDE.SPARK : CLAUDE.INK,
            opacity: (hot ? 0.5 : 0.26) * win(p, g + i * 0.02, g + 0.14 + i * 0.02),
          }}
        />
      ))}
      <div
        style={{
          position: 'absolute', left: x, top: MID_Y + 180, width: COL_W,
          fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE,
          opacity: win(p, g, g + 0.12),
        }}
      >
        {label}
      </div>
    </>
  );

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={draw} />

      {stack(IN_X, data.inputLabel, 0.08, false)}
      {stack(OUT_X, data.outputLabel, 0.82, true)}

      {/* the machine */}
      <div
        style={{
          position: 'absolute', left: BOX_X, top: BOX_Y, width: BOX_W, height: BOX_H,
          border: `2px solid ${CLAUDE.INK}`, borderRadius: 16,
          backgroundColor: '#FFFFFF', opacity: draw,
        }}
      />
      {/* the key slot */}
      <div
        style={{
          position: 'absolute', left: BOX_X + 60, top: BOX_Y + 175, width: BOX_W - 120, height: 120,
          border: `2px dashed ${RULE}`, borderRadius: 10, opacity: draw,
        }}
      />

      {/* routing wires in and out — they re-run after the swap */}
      <div
        style={{
          position: 'absolute', left: IN_X + COL_W, top: MID_Y - 3,
          width: (BOX_X - IN_X - COL_W) * Math.max(seat, rerun), height: 5,
          backgroundColor: rerun > 0.02 ? CLAUDE.SPARK : CLAUDE.INK,
          opacity: rerun > 0.02 ? 0.85 : 0.5,
        }}
      />
      <div
        style={{
          position: 'absolute', left: BOX_X + BOX_W, top: MID_Y - 3,
          width: (OUT_X - BOX_X - BOX_W) * rerun, height: 5,
          backgroundColor: CLAUDE.SPARK, opacity: 0.85,
        }}
      />

      {/* OLD KEY — seats, then lifts out and greys */}
      <div
        style={{
          position: 'absolute', left: BOX_X + 80, top: BOX_Y + 199 - 300 * lift,
          width: BOX_W - 160, height: 72, borderRadius: 8,
          border: `2px solid ${CLAUDE.INK}`, backgroundColor: '#FFFFFF',
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          fontFamily: CLAUDE_FONT.ui, fontSize: 42,
          color: CLAUDE.INK, opacity: seat * (1 - 0.72 * lift),
        }}
      >
        {data.oldKey}
      </div>

      {/* NEW KEY — the ONE accent, drops into the emptied slot */}
      <div
        style={{
          position: 'absolute', left: BOX_X + 80, top: BOX_Y + 199 - 150 * (1 - drop),
          width: BOX_W - 160, height: 72, borderRadius: 8,
          border: `2px solid ${CLAUDE.SPARK}`, backgroundColor: CLAUDE.SPARK,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          fontFamily: CLAUDE_FONT.ui, fontSize: 42, fontWeight: 600,
          color: '#FFFFFF', opacity: drop,
        }}
      >
        {data.newKey}
      </div>

      <NoteLine note={data.note} opacity={win(p, 0.9, 0.99)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B07 — ItmModels: what a post has to get past.

   The ask→result pair's RESULT. Two tracks, and the difference between them is a
   physical object on the line: the follower track has a GATE and a post visibly
   STOPS at it; the interest track has a match node and the post goes through. The
   accent lands on the match node — the thing that replaced the gate — never on both.
   ═══════════════════════════════════════════════════════════════════════════ */
export type ModelsData = {
  slideMeta: string;
  oldTitle: string;
  oldSteps: string[];
  oldGateLabel: string;
  oldFoot: string;
  newTitle: string;
  newSteps: string[];
  newFoot: string;
  note: string;
};

export const ItmModels: React.FC<{data: ModelsData}> = ({data}) => {
  const p = useP();
  const RAIL_X = SAFE.x + 40;
  const RAIL_W = SAFE.w - 80;
  /* QC: spread from 170/530 — the two tracks now use the vertical span of SAFE. */
  const T1_Y = SAFE.y + 200;
  const T2_Y = SAFE.y + 600;

  /* node centres along the rail */
  const nx = (f: number) => RAIL_X + RAIL_W * f;
  const FR = [0.1, 0.5, 0.9];

  const node = (
    cx: number, y: number, label: string, g: number, hot: boolean, wide: number,
  ) => (
    <div
      style={{
        position: 'absolute', left: cx - wide / 2, top: y - 46, width: wide,
        minHeight: 92, boxSizing: 'border-box',
        border: `2px solid ${hot ? CLAUDE.SPARK : CLAUDE.INK}`,
        backgroundColor: hot ? CLAUDE.SPARK : '#FFFFFF', borderRadius: 10,
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        padding: '10px 16px',
        fontFamily: CLAUDE_FONT.ui, fontSize: 30, lineHeight: 1.2, textAlign: 'center',
        color: hot ? '#FFFFFF' : CLAUDE.INK, opacity: g,
      }}
    >
      {label}
    </div>
  );

  const trackHead = (y: number, text: string, g: number) => (
    <div
      style={{
        position: 'absolute', left: SAFE.x, top: y - 130, width: SAFE.w,
        fontFamily: CLAUDE_FONT.ui, fontSize: 28, letterSpacing: '.14em',
        color: MUTE, fontWeight: 600, opacity: g,
      }}
    >
      {text.toUpperCase()}
    </div>
  );

  const foot = (y: number, text: string, g: number, accent: boolean) => (
    <div
      style={{
        position: 'absolute', left: SAFE.x, top: y + 150, width: SAFE.w,
        fontFamily: CLAUDE_FONT.serif, fontSize: 36,
        color: accent ? CLAUDE.SPARK : MUTE, opacity: g,
      }}
    >
      {text}
    </div>
  );

  const t1 = win(p, 0.06, 0.20);
  const t2 = win(p, 0.48, 0.62);
  /* the travelling post: stops dead at the gate on track 1, goes through on track 2 */
  const run1 = win(p, 0.22, 0.40);
  const run2 = win(p, 0.66, 0.86);
  const matchHot = win(p, 0.84, 0.95);

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={t1} />

      {/* ── TRACK 1: the gate holds ── */}
      {trackHead(T1_Y, data.oldTitle, t1)}
      <div style={{position: 'absolute', left: RAIL_X, top: T1_Y - 2, width: RAIL_W * t1, height: 4, backgroundColor: RULE}} />
      {node(nx(FR[0]), T1_Y, data.oldSteps[0], t1, false, 300)}
      {node(nx(FR[1]), T1_Y, data.oldSteps[1], win(p, 0.12, 0.26), false, 460)}
      {node(nx(FR[2]), T1_Y, data.oldSteps[2], win(p, 0.16, 0.30), false, 300)}
      {/* the gate: a closed barrier just left of the middle node */}
      {Array.from({length: 5}).map((_, i) => (
        <div
          key={i}
          style={{
            position: 'absolute', left: nx(FR[1]) - 330 + i * 16, top: T1_Y - 62,
            width: 5, height: 124, backgroundColor: CLAUDE.INK,
            opacity: 0.75 * win(p, 0.20, 0.34),
          }}
        />
      ))}
      <div
        style={{
          position: 'absolute', left: nx(FR[1]) - 330, top: T1_Y + 74,
          fontFamily: CLAUDE_FONT.ui, fontSize: 24, letterSpacing: '.16em',
          color: CLAUDE.INK, fontWeight: 600, opacity: win(p, 0.24, 0.38),
        }}
      >
        {data.oldGateLabel.toUpperCase()}
      </div>
      {/* the post stops at the barrier and stays there */}
      <div
        style={{
          position: 'absolute',
          left: nx(FR[0]) + 160 + (nx(FR[1]) - 370 - nx(FR[0]) - 160) * run1,
          top: T1_Y - 13, width: 26, height: 26, borderRadius: '50%',
          backgroundColor: CLAUDE.INK, opacity: win(p, 0.20, 0.30),
        }}
      />
      {foot(T1_Y, data.oldFoot, win(p, 0.36, 0.48), false)}

      {/* ── TRACK 2: no gate on the line ── */}
      {trackHead(T2_Y, data.newTitle, t2)}
      <div style={{position: 'absolute', left: RAIL_X, top: T2_Y - 2, width: RAIL_W * t2, height: 4, backgroundColor: RULE}} />
      {node(nx(FR[0]), T2_Y, data.newSteps[0], t2, false, 300)}
      {node(nx(FR[1]), T2_Y, data.newSteps[1], win(p, 0.54, 0.68), matchHot > 0.5, 620)}
      {node(nx(FR[2]), T2_Y, data.newSteps[2], win(p, 0.58, 0.72), false, 300)}
      {/* the post crosses straight through */}
      <div
        style={{
          position: 'absolute',
          left: nx(FR[0]) + 160 + (nx(FR[2]) - 160 - nx(FR[0]) - 160) * run2,
          top: T2_Y - 13, width: 26, height: 26, borderRadius: '50%',
          backgroundColor: CLAUDE.SPARK, opacity: win(p, 0.64, 0.74),
        }}
      />
      {foot(T2_Y, data.newFoot, win(p, 0.88, 0.97), true)}

      <NoteLine note={data.note} opacity={win(p, 0.93, 1.0)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B08 — ItmJob: the question a marketer is actually answering.

   The old question is RETIRED, not deleted — it desaturates and settles back but
   stays fully legible, because the reel's own honesty beat says followers did not
   become worthless. The tick row under the new card is marks, not a tally: there is
   no count prop, and nothing here renders a number.
   ═══════════════════════════════════════════════════════════════════════════ */
export type JobData = {
  slideMeta: string;
  oldHead: string;
  oldQuestion: string;
  newHead: string;
  newQuestion: string;
  tickLabel: string;
  note: string;
};

/** Exported for the same reason as MARKS — both cuts tick the same marks. */
export const TICKS = 9;

export const ItmJob: React.FC<{data: JobData}> = ({data}) => {
  const p = useP();
  const COL_W = 810;
  const L_X = SAFE.x;
  const R_X = SAFE.x + 918;
  const CARD_Y = SAFE.y + 190;
  const CARD_H = 330;

  const oldIn = win(p, 0.08, 0.24);
  const retire = win(p, 0.34, 0.50);
  const newIn = win(p, 0.52, 0.70);

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />

      {/* ── retired ── */}
      <div
        style={{
          position: 'absolute', left: L_X, top: SAFE.y + 128, width: COL_W,
          fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.16em',
          color: MUTE, fontWeight: 600, opacity: oldIn,
        }}
      >
        {data.oldHead.toUpperCase()}
      </div>
      <div
        style={{
          position: 'absolute', left: L_X, top: CARD_Y + 14 * retire, width: COL_W,
          minHeight: CARD_H, boxSizing: 'border-box',
          backgroundColor: '#FFFFFF', border: `1px solid ${RULE}`, borderRadius: 14,
          padding: 42, opacity: oldIn * (1 - 0.42 * retire),
          fontFamily: CLAUDE_FONT.serif, fontSize: 62, color: CLAUDE.INK, lineHeight: 1.18,
        }}
      >
        {data.oldQuestion}
      </div>

      {/* ── the job now: the ONE accent ── */}
      <div
        style={{
          position: 'absolute', left: R_X, top: SAFE.y + 128, width: COL_W,
          fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.16em',
          color: CLAUDE.SPARK, fontWeight: 600, opacity: newIn,
        }}
      >
        {data.newHead.toUpperCase()}
      </div>
      <div
        style={{
          position: 'absolute', left: R_X, top: CARD_Y - 18 * (1 - newIn), width: COL_W,
          minHeight: CARD_H, boxSizing: 'border-box',
          backgroundColor: '#FFFFFF', border: `2px solid ${CLAUDE.SPARK}`, borderRadius: 14,
          padding: 42, opacity: newIn,
          fontFamily: CLAUDE_FONT.serif, fontSize: 62, color: CLAUDE.SPARK, lineHeight: 1.18,
        }}
      >
        {data.newQuestion}
      </div>

      {/* ── one post at a time: marks, never a tally ── */}
      {Array.from({length: TICKS}).map((_, i) => {
        const g = win(p, 0.74 + i * 0.018, 0.80 + i * 0.018);
        return (
          <div
            key={i}
            style={{
              position: 'absolute', left: R_X + i * 88, top: CARD_Y + CARD_H + 52,
              width: 62, height: 62, borderRadius: 8,
              border: `2px solid ${CLAUDE.SPARK}`,
              backgroundColor: CLAUDE.SPARK, opacity: 0.85 * g,
              transform: `scale(${0.6 + 0.4 * g})`,
            }}
          />
        );
      })}
      <div
        style={{
          position: 'absolute', left: R_X, top: CARD_Y + CARD_H + 132, width: COL_W,
          fontFamily: CLAUDE_FONT.ui, fontSize: 32, color: MUTE,
          opacity: win(p, 0.86, 0.95),
        }}
      >
        {data.tickLabel}
      </div>

      <NoteLine note={data.note} opacity={win(p, 0.92, 1.0)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B09 — ItmLimits: being exact about the claim.

   The FALSIFIABILITY beat. The accent sits on the REFUSALS column, not on the claims
   column — in this reel the honest part is what is being declined, so that is what
   gets the one accent. `provenance` is required and renders in muted ink at the foot,
   and `falsifier` is required too: the beat cannot be authored without giving the
   viewer a way to check the claim themselves.
   ═══════════════════════════════════════════════════════════════════════════ */
export type LimitsData = {
  slideMeta: string;
  title: string;
  claims: {heading: string; items: string[]};
  refusals: {heading: string; items: string[]};
  /** REQUIRED — the credit travels with the claim, in muted ink, never the accent */
  provenance: string;
  /** REQUIRED — how a viewer could check this for themselves */
  falsifier: string;
};

export const ItmLimits: React.FC<{data: LimitsData}> = ({data}) => {
  const p = useP();
  const COL_W = 810;
  const L_X = SAFE.x;
  const R_X = SAFE.x + 918;
  const HEAD_Y = SAFE.y + 250;
  const ITEM_Y = SAFE.y + 320;
  const STEP = 132;

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
              fontFamily: CLAUDE_FONT.ui, fontSize: 36, lineHeight: 1.32,
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
      {ledger(R_X, data.refusals.heading, data.refusals.items, 0.42, true)}

      {/* provenance — muted ink, at the foot, never dressed up */}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 168,
          width: SAFE.w * win(p, 0.78, 0.88), height: 1, backgroundColor: RULE,
        }}
      />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 148, width: SAFE.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: MUTE, lineHeight: 1.3,
          opacity: win(p, 0.80, 0.90),
        }}
      >
        {data.provenance}
      </div>

      <NoteLine note={data.falsifier} opacity={win(p, 0.90, 0.99)} />
    </PlainStage>
  );
};
