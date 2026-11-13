import React from 'react';
import {AbsoluteFill} from 'remotion';
import {z} from 'zod';
import {CLAUDE} from '../tokens/claude';
import {SAFE} from '../tokens/layout';
import {ACCENT, Card, INK, SANS, SERIF, SOFT, STAGE, useBeat} from './SocialAiVisibility';
import {Glyph, GlyphKind, LogoBug, SparkLine} from './ContentRepurpose';

/**
 * OneIntoTen.tsx — concept illustrations (C3) for the ai-explainer reel
 * "How to Turn 1 Piece of Content Into 10?" (@Shubh & @HumanitariansAI).
 *
 * One long-form video is a bundle of atoms (big idea · stories · quotes · steps);
 * each atom becomes a native format (ten tiles); formats are reshaped, never
 * copy-pasted; the ten are released over a two-week runway that points back to
 * the anchor; and a three-question gate cuts the weak ones.
 *
 * These are the 16:9 layouts. Native 9:16 layouts live in OneIntoTen916.tsx and
 * share these zod schemas; Root.tsx registers `<Name>` and `<Name>916`.
 * Pure functions of the beat clock: `durationSeconds` = the beat's measured audio,
 * and every `*At` prop is a beat fraction placed on the spoken word (faster-whisper
 * word timestamps).
 *
 * Palette: claude C3 stage — cream, warm ink, ONE terracotta accent per beat
 * (big-idea ring · the ten counter rule · the copy-paste strike · the anchor ring ·
 * the quality gate). Accent is never used for text (WCAG on cream). All example
 * copy, schedules and counts are labelled illustrative — no statistics.
 */

const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const ease = (t: number) => t * t * (3 - 2 * t);
const lerp = (a: number, b: number, t: number) => a + (b - a) * t;
const durationProp = {durationSeconds: z.number().default(16)};

/** Format glyphs: the ContentRepurpose set plus phone, quote and audio wave. */
export const glyphKinds = ['video', 'lines', 'doc', 'slides', 'bubble', 'mail', 'phone', 'quote', 'wave'] as const;
export type TenGlyphKind = typeof glyphKinds[number];
export const TenGlyph: React.FC<{kind: TenGlyphKind; size: number; color?: string}> = ({kind, size, color = INK}) => {
  const common = {fill: 'none', stroke: color, strokeWidth: 5, strokeLinecap: 'round' as const, strokeLinejoin: 'round' as const};
  if (kind === 'phone') {
    return (
      <svg width={size} height={size} viewBox="0 0 100 100" style={{flexShrink: 0}}>
        <rect x={28} y={6} width={44} height={88} rx={9} {...common} />
        <line x1={43} y1={15} x2={57} y2={15} {...common} />
        <path d="M 43 38 L 61 50 L 43 62 Z" fill={color} stroke="none" />
      </svg>
    );
  }
  if (kind === 'quote') {
    return (
      <svg width={size} height={size} viewBox="0 0 100 100" style={{flexShrink: 0}}>
        {[0, 38].map((dx) => (
          <React.Fragment key={dx}>
            <circle cx={30 + dx} cy={58} r={11} fill={color} />
            <path d={`M ${19 + dx} 58 C ${19 + dx} 40, ${26 + dx} 30, ${40 + dx} 26`} {...common} />
          </React.Fragment>
        ))}
      </svg>
    );
  }
  if (kind === 'wave') {
    const hs = [18, 40, 66, 36, 56, 26, 46];
    return (
      <svg width={size} height={size} viewBox="0 0 100 100" style={{flexShrink: 0}}>
        {hs.map((h, i) => <line key={i} x1={14 + i * 12} y1={50 - h / 2} x2={14 + i * 12} y2={50 + h / 2} {...common} />)}
      </svg>
    );
  }
  return <Glyph kind={kind as GlyphKind} size={size} color={color} />;
};
const glyphEnum = z.enum(glyphKinds);

/** Small letter-spaced label (sans, soft ink). */
const Label: React.FC<{text: string; px?: number; style?: React.CSSProperties}> = ({text, px = 44, style}) => (
  <div style={{fontFamily: SANS, fontSize: px, fontWeight: 700, letterSpacing: '0.1em', color: SOFT, lineHeight: 1, ...style}}>{text}</div>
);

const Caption: React.FC<{text: string; opacity: number}> = ({text, opacity}) => (
  <div style={{position: 'absolute', left: SAFE.x, top: SAFE.b - 44, fontFamily: SANS, fontSize: 40, color: SOFT, opacity}}>{text}</div>
);

// ─────────────────────────────────────────────────────────────────────────────
// B02 — a long video is a bundle of atoms; the atoms fly out into four bins
// ─────────────────────────────────────────────────────────────────────────────
export const atomSplitSchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('Find the atoms first.'),
  videoLabel: z.string().default('Long-form video'),
  videoAt: z.number().default(0.03),
  splitAt: z.number().default(0.3),
  bins: z.array(z.object({label: z.string(), chips: z.array(z.string()), at: z.number()})).default([
    {label: 'Big idea', chips: ['“Make it once, then make it fit.”'], at: 0.425},
    {label: 'Stories', chips: ['Story 1', 'Story 2', 'Story 3'], at: 0.505},
    {label: 'Quotes', chips: ['Quote 1', 'Quote 2', 'Quote 3'], at: 0.575},
    {label: 'Steps', chips: ['Step 1', 'Step 2', 'Step 3', 'Step 4'], at: 0.655},
  ]),
  flyStagger: z.number().default(0.018),
  flySpan: z.number().default(0.055),
  focusIndex: z.number().default(0),
  ringAt: z.number().default(0.8),
  line: z.string().default('Pull the atoms out first — then package each one.'),
  lineAt: z.number().default(0.78),
  caption: z.string().default('Example atoms — illustrative'),
});
export type AtomSplitProps = z.infer<typeof atomSplitSchema>;

/** Flight of chip k from its bundle cell (inside the video card) to its bin slot. */
export const atomFlight = (at: number, j: number, props: AtomSplitProps, ramp: (f: number, d?: number) => number) =>
  ease(ramp(at + j * props.flyStagger, props.flySpan));

export const AtomSplit: React.FC<AtomSplitProps> = (props) => {
  const {pop, ramp} = useBeat(props.durationSeconds);
  const S = SAFE;
  const card = {x: S.x, y: 196, w: 520, h: 628};
  const rowsX = 700, rowH = 128, rowGap = 38, rowsY = 196;
  const labelW = 290;
  const chipsX = rowsX + labelW, chipsW = S.r - chipsX - 24, chipGap = 20, chipH = 92;
  const vIn = pop(props.videoAt);
  const split = ramp(props.splitAt, 0.06);
  // bundle grid inside the card: 3 columns under the label
  const cellW = 136, cellH = 72, cellGapX = 18, cellGapY = 22;
  const gridX = card.x + (card.w - (3 * cellW + 2 * cellGapX)) / 2, gridY = card.y + 150;
  let k = 0;
  const chips: {text: string; bin: number; j: number; x0: number; y0: number; x1: number; y1: number; w: number}[] = [];
  props.bins.forEach((b, i) => {
    const n = b.chips.length;
    const w = (chipsW - (n - 1) * chipGap) / n;
    b.chips.forEach((text, j) => {
      const col = k % 3, row = Math.floor(k / 3);
      chips.push({text, bin: i, j, w,
        x0: gridX + col * (cellW + cellGapX), y0: gridY + row * (cellH + cellGapY),
        x1: chipsX + j * (w + chipGap), y1: rowsY + i * (rowH + rowGap) + (rowH - chipH) / 2});
      k++;
    });
  });
  const ringIn = pop(props.ringAt);
  const focus = chips.find((c) => c.bin === props.focusIndex && c.j === 0);
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} />
      {/* the long video — one card that turns out to be a bundle */}
      <Card style={{position: 'absolute', left: card.x, top: card.y, width: card.w, height: card.h, boxSizing: 'border-box',
        opacity: vIn, transform: `scale(${0.92 + 0.08 * vIn})`,
        border: split > 0 ? `3px dashed ${CLAUDE.GHOST}` : `2px solid ${CLAUDE.BORDER}`}}>
        <div style={{position: 'absolute', left: 0, right: 0, top: 44, textAlign: 'center', fontFamily: SERIF, fontSize: 60,
          fontWeight: 700, color: INK}}>{props.videoLabel}</div>
        <div style={{position: 'absolute', left: 0, right: 0, top: 200, display: 'flex', justifyContent: 'center',
          opacity: 1 - 0.8 * split, transform: `scale(${1 - 0.25 * split})`}}>
          <TenGlyph kind="video" size={260} />
        </div>
      </Card>
      {/* the four bins */}
      {props.bins.map((b, i) => {
        const y = rowsY + i * (rowH + rowGap);
        const bIn = pop(props.splitAt + 0.03 + i * 0.015);
        const landed = pop(b.at + 0.03);
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: rowsX, top: y, width: S.r - rowsX, height: rowH, borderRadius: 22,
              background: CLAUDE.FOOTER, border: `2px solid ${CLAUDE.BORDER}`, boxSizing: 'border-box', opacity: bIn}} />
            <div style={{position: 'absolute', left: rowsX + 30, top: y, height: rowH, width: labelW - 30, display: 'flex',
              alignItems: 'center', fontFamily: SERIF, fontSize: 58, fontWeight: 700, color: INK, opacity: bIn * (0.5 + 0.5 * landed)}}>
              {b.label}</div>
          </React.Fragment>
        );
      })}
      {/* the atoms: blank pills inside the bundle, labelled chips once they land */}
      {chips.map((c, i) => {
        const b = props.bins[c.bin];
        const appear = pop(props.splitAt + 0.02 + i * 0.008);
        const t = atomFlight(b.at, c.j, props, ramp);
        const sx = cellW / c.w, sy = cellH / chipH;
        const x = lerp(c.x0, c.x1, t), y = lerp(c.y0, c.y1, t);
        const scaleX = lerp(sx, 1, t), scaleY = lerp(sy, 1, t);
        const big = c.bin === props.focusIndex;
        return (
          <div key={i} style={{position: 'absolute', left: x, top: y, width: c.w, height: chipH, transformOrigin: '0 0',
            transform: `scale(${scaleX}, ${scaleY})`, borderRadius: 18, background: CLAUDE.CARD,
            border: `3px solid ${t > 0.5 ? CLAUDE.BORDER : CLAUDE.GHOST}`, boxSizing: 'border-box', opacity: appear,
            boxShadow: t > 0.5 ? '0 8px 24px rgba(61,57,41,0.12)' : 'none',
            display: 'flex', alignItems: 'center', justifyContent: 'center', overflow: 'hidden'}}>
            <span style={{fontFamily: big ? SERIF : SANS, fontStyle: big ? 'italic' : 'normal', fontSize: big ? 50 : 46,
              fontWeight: big ? 400 : 700, color: INK, whiteSpace: 'nowrap', opacity: clamp01((t - 0.75) / 0.25)}}>{c.text}</span>
          </div>
        );
      })}
      {focus && (
        <div style={{position: 'absolute', left: focus.x1 - 12, top: focus.y1 - 12, width: focus.w + 24, height: chipH + 24,
          borderRadius: 26, border: `6px solid ${ACCENT}`, boxSizing: 'border-box', opacity: ringIn,
          transform: `scale(${1.06 - 0.06 * ringIn})`}} />
      )}
      <div style={{position: 'absolute', left: S.x, width: S.w, top: 872, textAlign: 'center', fontFamily: SERIF, fontSize: 58,
        fontWeight: 700, color: INK, opacity: pop(props.lineAt), transform: `translateY(${(1 - pop(props.lineAt)) * 16}px)`}}>
        {props.line}</div>
      <Caption text={props.caption} opacity={pop(props.splitAt)} />
      <LogoBug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B04 — ten numbered formats light in spoken order; the counter climbs to 10
// ─────────────────────────────────────────────────────────────────────────────
export const tenFormatsSchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('One video. Ten pieces.'),
  slotsAt: z.number().default(0.02),
  tiles: z.array(z.object({label: z.string(), glyph: glyphEnum, from: z.string(), at: z.number()})).default([
    {label: 'Reel', glyph: 'phone', from: 'Big idea', at: 0.17},
    {label: 'TikTok', glyph: 'phone', from: 'Big idea', at: 0.2},
    {label: 'YouTube Short', glyph: 'phone', from: 'Big idea', at: 0.245},
    {label: 'LinkedIn post', glyph: 'bubble', from: 'Story', at: 0.358},
    {label: 'Carousel', glyph: 'slides', from: 'Steps', at: 0.47},
    {label: 'Blog post', glyph: 'doc', from: 'Transcript', at: 0.583},
    {label: 'Email', glyph: 'mail', from: 'Blog', at: 0.664},
    {label: 'Thread', glyph: 'lines', from: 'Quotes', at: 0.752},
    {label: 'Quote card', glyph: 'quote', from: 'Quotes', at: 0.785},
    {label: 'Podcast clip', glyph: 'wave', from: 'Audio', at: 0.888},
  ]),
  sourceLabel: z.string().default('1 video'),
  countLabel: z.string().default('pieces'),
  tenAt: z.number().default(0.962),
});
export type TenFormatsProps = z.infer<typeof tenFormatsSchema>;

/** How many tiles are lit at progress p (the counter's value, min 1 once the first lands). */
export const litCount = (props: TenFormatsProps, p: number) => props.tiles.filter((t) => p >= t.at).length;

export const TenFormats: React.FC<TenFormatsProps> = (props) => {
  const {pop, ramp, p} = useBeat(props.durationSeconds);
  const S = SAFE;
  const cols = 5, gap = 28, rowGap = 26;
  const tw = (S.w - (cols - 1) * gap) / cols, th = 320, top = 168;
  const n = litCount(props, p);
  const tenIn = ramp(props.tenAt, 0.05);
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} />
      {props.tiles.map((t, i) => {
        const x = S.x + (i % cols) * (tw + gap), y = top + Math.floor(i / cols) * (th + rowGap);
        const slot = pop(props.slotsAt + i * 0.006);
        const lit = pop(t.at);
        return (
          <React.Fragment key={i}>
            {/* the empty numbered slot */}
            <div style={{position: 'absolute', left: x, top: y, width: tw, height: th, borderRadius: 22, boxSizing: 'border-box',
              border: `3px dashed ${CLAUDE.GHOST}`, opacity: slot * (1 - lit)}}>
              <div style={{position: 'absolute', left: 26, top: 22, fontFamily: SANS, fontSize: 46, fontWeight: 700, color: SOFT,
                opacity: 0.6}}>{String(i + 1).padStart(2, '0')}</div>
            </div>
            <Card style={{position: 'absolute', left: x, top: y, width: tw, height: th, boxSizing: 'border-box', padding: '22px 26px',
              opacity: lit, transform: `scale(${0.9 + 0.1 * lit})`}}>
              <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start'}}>
                <span style={{fontFamily: SANS, fontSize: 46, fontWeight: 700, color: SOFT, lineHeight: 1}}>{String(i + 1).padStart(2, '0')}</span>
                <TenGlyph kind={t.glyph} size={80} />
              </div>
              <div style={{fontFamily: SERIF, fontSize: 54, fontWeight: 700, color: INK, lineHeight: 1.04, marginTop: 8,
                maxWidth: tw - 52}}>{t.label}</div>
              <div style={{position: 'absolute', left: 26, bottom: 24, height: 58, padding: '0 16px', borderRadius: 29,
                background: CLAUDE.FOOTER, border: `2px solid ${CLAUDE.BORDER}`, display: 'flex', alignItems: 'center',
                fontFamily: SANS, fontSize: 42, fontWeight: 600, color: INK, whiteSpace: 'nowrap'}}>{t.from}</div>
            </Card>
          </React.Fragment>
        );
      })}
      {/* the counter: 1 video → N pieces; the one accent lands on "That's ten" */}
      <div style={{position: 'absolute', left: S.x, width: S.w, top: 852, height: 150, display: 'flex', alignItems: 'center',
        justifyContent: 'center', gap: 40, opacity: pop(props.slotsAt)}}>
        <span style={{fontFamily: SERIF, fontSize: 92, fontWeight: 700, color: INK}}>{props.sourceLabel}</span>
        <svg width={120} height={60} viewBox="0 0 120 60">
          <path d="M 6 30 L 104 30 M 84 12 L 106 30 L 84 48" fill="none" stroke={INK} strokeWidth={7} strokeLinecap="round" strokeLinejoin="round" />
        </svg>
        <span style={{position: 'relative', fontFamily: SERIF, fontSize: 140, fontWeight: 700, color: INK, lineHeight: 1,
          minWidth: 170, textAlign: 'center'}}>
          {Math.max(1, n)}
          <span style={{position: 'absolute', left: 0, right: 0, bottom: -8, height: 12, borderRadius: 6, background: ACCENT,
            transform: `scaleX(${tenIn})`}} />
        </span>
        <span style={{fontFamily: SERIF, fontSize: 92, fontWeight: 700, color: INK}}>{props.countLabel}</span>
      </div>
      <LogoBug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B05 — reshape, don't copy: three pasted copies are struck, then each column
// reshapes into its platform's native opening and ending
// ─────────────────────────────────────────────────────────────────────────────
export const reshapeNotCopySchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('Reshape, don’t copy.'),
  ideaLabel: z.string().default('ONE IDEA'),
  idea: z.string().default('“Make it once, then make it fit.”'),
  ideaAt: z.number().default(0.16),
  pasted: z.string().default('Make it once, then make it fit. Here’s how I turned one video into ten posts.'),
  pastedLabel: z.string().default('Pasted'),
  copiesAt: z.number().default(0.02),
  strikeAt: z.number().default(0.07),
  openLabel: z.string().default('OPENS WITH'),
  endLabel: z.string().default('ENDS WITH'),
  cols: z.array(z.object({platform: z.string(), shape: z.string(), open: z.string(), end: z.string(),
    at: z.number(), openAt: z.number(), endAt: z.number()})).default([
    {platform: 'TikTok', shape: 'vertical · fast', open: '“Stop posting your video once.”', end: '“Part two tomorrow.”',
      at: 0.31, openAt: 0.39, endAt: 0.42},
    {platform: 'LinkedIn', shape: 'text · a short read', open: '“Last month I posted one video. Then I stopped.”',
      end: '“How do you reuse yours?”', at: 0.468, openAt: 0.54, endAt: 0.61},
    {platform: 'Email', shape: 'one reader · one link', open: '“Hi — a quick note this week.”', end: '“One link: the full video.”',
      at: 0.694, openAt: 0.74, endAt: 0.82},
  ]),
  sameLine: z.string().default('Same idea, three shapes.'),
  sameAt: z.number().default(0.89),
  caption: z.string().default('Example copy — illustrative'),
});
export type ReshapeNotCopyProps = z.infer<typeof reshapeNotCopySchema>;

export const ReshapeNotCopy: React.FC<ReshapeNotCopyProps> = (props) => {
  const {pop, ramp} = useBeat(props.durationSeconds);
  const S = SAFE;
  const gap = 40, colTop = 268, colH = 640;
  const cw = (S.w - gap * 2) / 3;
  const copiesIn = pop(props.copiesAt);
  const strike = ramp(props.strikeAt, 0.05);
  const ideaIn = pop(props.ideaAt);
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} />
      <div style={{position: 'absolute', left: S.x, width: S.w, top: 150, height: 96, display: 'flex', alignItems: 'center',
        justifyContent: 'center', gap: 30, opacity: ideaIn, transform: `translateY(${(1 - ideaIn) * -14}px)`}}>
        <Label text={props.ideaLabel} px={44} />
        <span style={{fontFamily: SERIF, fontSize: 62, fontStyle: 'italic', color: INK}}>{props.idea}</span>
      </div>
      {props.cols.map((c, i) => {
        const x = S.x + i * (cw + gap);
        const re = pop(c.at);
        const oIn = pop(c.openAt), eIn = pop(c.endAt);
        const out = Math.max(0, 1 - 2 * re), inn = Math.max(0, 2 * re - 1);
        const pastedOp = (1 - 0.55 * strike) * out;
        return (
          <Card key={i} style={{position: 'absolute', left: x, top: colTop, width: cw, height: colH, boxSizing: 'border-box',
            padding: '30px 36px', opacity: copiesIn, transform: `translateY(${(1 - copiesIn) * 20}px)`}}>
            <div style={{fontFamily: SERIF, fontSize: 64, fontWeight: 700, color: INK, lineHeight: 1}}>{c.platform}</div>
            <div style={{position: 'relative', height: 56, marginTop: 14}}>
              <div style={{position: 'absolute', top: 0, height: 52, padding: '0 16px', borderRadius: 26,
                border: `2px solid ${CLAUDE.BORDER}`, background: CLAUDE.FOOTER, display: 'flex', alignItems: 'center',
                fontFamily: SANS, fontSize: 40, fontWeight: 700, color: SOFT, opacity: out}}>{props.pastedLabel}</div>
              <div style={{position: 'absolute', top: 4, fontFamily: SANS, fontSize: 44, fontStyle: 'italic', color: SOFT,
                opacity: inn, whiteSpace: 'nowrap'}}>{c.shape}</div>
            </div>
            {/* the pasted copy — identical in every column, struck on "copy and paste" */}
            <div style={{position: 'absolute', left: 36, right: 36, top: 190, opacity: pastedOp}}>
              <div style={{position: 'relative', fontFamily: SERIF, fontSize: 50, color: INK, lineHeight: 1.18}}>
                {props.pasted}
                <div style={{position: 'absolute', left: -8, top: '46%', height: 8, borderRadius: 4, background: ACCENT,
                  width: `calc(${strike * 100}% + 16px)`, opacity: strike > 0 ? 1 : 0}} />
              </div>
            </div>
            {/* the reshaped version */}
            <div style={{position: 'absolute', left: 36, right: 36, top: 200, opacity: inn}}>
              <Label text={props.openLabel} style={{opacity: oIn}} />
              <div style={{fontFamily: SERIF, fontSize: 50, fontStyle: 'italic', color: INK, lineHeight: 1.16, marginTop: 14,
                minHeight: 124, opacity: oIn, transform: `translateY(${(1 - oIn) * 12}px)`}}>{c.open}</div>
              <Label text={props.endLabel} style={{marginTop: 22, opacity: eIn}} />
              <div style={{fontFamily: SERIF, fontSize: 50, fontStyle: 'italic', color: INK, lineHeight: 1.16, marginTop: 14,
                opacity: eIn, transform: `translateY(${(1 - eIn) * 12}px)`}}>{c.end}</div>
            </div>
          </Card>
        );
      })}
      <div style={{position: 'absolute', left: S.x, width: S.w, top: 922, textAlign: 'center', fontFamily: SERIF, fontSize: 56,
        fontWeight: 700, color: INK, opacity: pop(props.sameAt)}}>{props.sameLine}</div>
      <Caption text={props.caption} opacity={copiesIn} />
      <LogoBug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B06 — the release runway: the anchor on day 1, the ten spread over two weeks,
// every piece pointing back to the original
// ─────────────────────────────────────────────────────────────────────────────
export const releaseRunwaySchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('Don’t post all ten at once.'),
  days: z.number().default(14),
  runwayAt: z.number().default(0.03),
  anchorLabel: z.string().default('Day 1 · Long video — the anchor'),
  anchorAt: z.number().default(0.18),
  ringAt: z.number().default(0.29),
  pieces: z.array(z.object({label: z.string(), glyph: glyphEnum, day: z.number(), at: z.number()})).default([
    {label: 'Reel', glyph: 'phone', day: 2, at: 0.37},
    {label: 'TikTok', glyph: 'phone', day: 3, at: 0.395},
    {label: 'Short', glyph: 'phone', day: 4, at: 0.42},
    {label: 'Carousel', glyph: 'slides', day: 6, at: 0.565},
    {label: 'LinkedIn', glyph: 'bubble', day: 7, at: 0.62},
    {label: 'Quote card', glyph: 'quote', day: 8, at: 0.645},
    {label: 'Thread', glyph: 'lines', day: 9, at: 0.67},
    {label: 'Blog', glyph: 'doc', day: 11, at: 0.73},
    {label: 'Podcast', glyph: 'wave', day: 12, at: 0.75},
    {label: 'Email', glyph: 'mail', day: 13, at: 0.77},
  ]),
  phases: z.array(z.object({label: z.string(), from: z.number(), to: z.number(), at: z.number()})).default([
    {label: 'Pull people in', from: 2, to: 4, at: 0.45},
    {label: 'Go deeper', from: 6, to: 9, at: 0.68},
    {label: 'Let it land', from: 11, to: 13, at: 0.79},
  ]),
  backAt: z.number().default(0.86),
  backLine: z.string().default('Every piece points back to the original.'),
  caption: z.string().default('Example schedule — illustrative'),
});
export type ReleaseRunwayProps = z.infer<typeof releaseRunwaySchema>;

export const ReleaseRunway: React.FC<ReleaseRunwayProps> = (props) => {
  const {pop, ramp, width, height} = useBeat(props.durationSeconds);
  const S = SAFE;
  const dayW = S.w / props.days;
  const cx = (d: number) => S.x + (d - 0.5) * dayW;
  const lineY = 560, tile = 100;
  const drawn = ramp(props.runwayAt, 0.12);
  const aIn = pop(props.anchorAt), ringIn = pop(props.ringAt);
  const back = ramp(props.backAt, 0.08);
  const backY = 716;
  const lastX = cx(Math.max(...props.pieces.map((q) => q.day)));
  const backLen = (lastX - cx(1)) + (backY - (lineY + 22));
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} />
      <svg width={width} height={height} style={{position: 'absolute', inset: 0}}>
        <line x1={S.x} y1={lineY} x2={S.x + S.w * drawn} y2={lineY} stroke={SOFT} strokeWidth={6} strokeLinecap="round" />
        {Array.from({length: props.days}, (_, i) => (
          <line key={i} x1={cx(i + 1)} y1={lineY - 14} x2={cx(i + 1)} y2={lineY + 14} stroke={SOFT} strokeWidth={4}
            opacity={drawn >= (i + 0.5) / props.days ? 1 : 0} />
        ))}
        {/* anchor leader */}
        <line x1={cx(1)} y1={372} x2={cx(1)} y2={lineY - tile - 14} stroke={INK} strokeWidth={4} opacity={aIn} />
        {/* phase brackets */}
        {props.phases.map((ph, i) => {
          const t = ramp(ph.at, 0.05);
          const xa = cx(ph.from) - dayW * 0.4, xb = cx(ph.to) + dayW * 0.4, y = 762;
          return t > 0 ? <path key={i} d={`M ${xa} ${y - 18} L ${xa} ${y} L ${xa + (xb - xa) * t} ${y} ${t > 0.98 ? `L ${xb} ${y - 18}` : ''}`}
            fill="none" stroke={INK} strokeWidth={4} opacity={0.7} /> : null;
        })}
        {/* every piece points back: ink arrow along the underside, up into the anchor */}
        {back > 0 && (
          <path d={`M ${lastX} ${backY} L ${cx(1)} ${backY} L ${cx(1)} ${lineY + 24}`} fill="none" stroke={INK} strokeWidth={6}
            strokeLinecap="round" strokeLinejoin="round" strokeDasharray={backLen} strokeDashoffset={backLen * (1 - back)} />
        )}
        {back > 0.97 && <path d={`M ${cx(1) - 18} ${lineY + 48} L ${cx(1)} ${lineY + 24} L ${cx(1) + 18} ${lineY + 48}`}
          fill="none" stroke={INK} strokeWidth={6} strokeLinecap="round" strokeLinejoin="round" />}
      </svg>
      {/* day numbers (day 1 is named by the anchor label) */}
      {Array.from({length: props.days - 1}, (_, i) => i + 2).map((d) => (
        <div key={d} style={{position: 'absolute', left: cx(d) - 50, width: 100, top: lineY + 22, textAlign: 'center',
          fontFamily: SANS, fontSize: 44, fontWeight: 600, color: SOFT, opacity: drawn >= (d - 0.5) / props.days ? 1 : 0}}>{d}</div>
      ))}
      <div style={{position: 'absolute', left: S.x, top: 300, fontFamily: SERIF, fontSize: 58, fontWeight: 700, color: INK,
        opacity: aIn, whiteSpace: 'nowrap'}}>{props.anchorLabel}</div>
      {/* the anchor tile — the one accent */}
      <Card style={{position: 'absolute', left: cx(1) - tile / 2, top: lineY - tile - 14, width: tile, height: tile, display: 'flex',
        alignItems: 'center', justifyContent: 'center', opacity: aIn, transform: `translateY(${(1 - aIn) * -60}px)`,
        background: CLAUDE.FOOTER}}>
        <TenGlyph kind="video" size={72} />
      </Card>
      <div style={{position: 'absolute', left: cx(1) - tile / 2 - 12, top: lineY - tile - 26, width: tile + 24, height: tile + 24,
        borderRadius: 30, border: `6px solid ${ACCENT}`, boxSizing: 'border-box', opacity: ringIn}} />
      {props.pieces.map((q, i) => {
        const t = pop(q.at);
        const up = i % 2 === 0;
        return (
          <React.Fragment key={i}>
            <Card style={{position: 'absolute', left: cx(q.day) - tile / 2, top: lineY - tile - 14, width: tile, height: tile,
              display: 'flex', alignItems: 'center', justifyContent: 'center', opacity: t, transform: `translateY(${(1 - t) * -70}px)`}}>
              <TenGlyph kind={q.glyph} size={70} />
            </Card>
            <div style={{position: 'absolute', left: cx(q.day) - 130, width: 260, top: up ? 380 : 640, textAlign: 'center',
              fontFamily: SANS, fontSize: 44, fontWeight: 700, color: INK, opacity: t, whiteSpace: 'nowrap'}}>{q.label}</div>
          </React.Fragment>
        );
      })}
      {props.phases.map((ph, i) => (
        <div key={i} style={{position: 'absolute', left: cx(ph.from) - dayW * 0.4 - 60, width: cx(ph.to) - cx(ph.from) + dayW * 0.8 + 120,
          top: 784, textAlign: 'center', fontFamily: SERIF, fontSize: 52, fontStyle: 'italic', color: INK,
          opacity: pop(ph.at + 0.03), whiteSpace: 'nowrap'}}>{ph.label}</div>
      ))}
      <div style={{position: 'absolute', left: S.x, width: S.w, top: 884, textAlign: 'center', fontFamily: SERIF, fontSize: 58,
        fontWeight: 700, color: INK, opacity: pop(props.backAt + 0.03)}}>{props.backLine}</div>
      <Caption text={props.caption} opacity={drawn} />
      <LogoBug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B07 — the quality gate: three questions, a sweep, the weak pieces cut
// ─────────────────────────────────────────────────────────────────────────────
export const qualityGateSchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('Ten is a ceiling.'),
  tilesAt: z.number().default(0.02),
  glyphs: z.array(glyphEnum).default(['phone', 'phone', 'phone', 'bubble', 'slides', 'doc', 'mail', 'lines', 'quote', 'wave']),
  checks: z.array(z.object({label: z.string(), at: z.number()})).default([
    {label: 'Stands on its own?', at: 0.335},
    {label: 'Feels native?', at: 0.45},
    {label: 'Worth a scroll-stop?', at: 0.595},
  ]),
  fails: z.array(z.number()).default([2, 7, 8]),
  gateAt: z.number().default(0.7),
  gateSpan: z.number().default(0.1),
  cutLabel: z.string().default('cut'),
  shipLine: z.string().default('7 of 10 ship.'),
  shipAt: z.number().default(0.81),
  verdict: z.string().default('Seven strong posts beat ten weak ones.'),
  verdictAt: z.number().default(0.84),
  caption: z.string().default('Example — illustrative'),
});
export type QualityGateProps = z.infer<typeof qualityGateSchema>;

/** Gate position 0..1 across the tile row, and whether it has passed tile i of n. */
export const gateState = (props: QualityGateProps, p: number, i: number, n: number) => {
  const g = clamp01((p - props.gateAt) / props.gateSpan);
  const passed = clamp01((g - (i + 0.5) / n) * n * 1.5);
  return {g, passed};
};

export const Check: React.FC<{size: number; color?: string}> = ({size, color = INK}) => (
  <svg width={size} height={size} viewBox="0 0 100 100">
    <path d="M 16 54 L 40 76 L 86 26" fill="none" stroke={color} strokeWidth={12} strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

export const QualityGate: React.FC<QualityGateProps> = (props) => {
  const {pop, p} = useBeat(props.durationSeconds);
  const S = SAFE;
  const n = props.glyphs.length;
  const gap = 20, tw = (S.w - gap * (n - 1)) / n, th = 200, rowY = 380;
  const cGap = 36, cw = (S.w - cGap * 2) / 3;
  const {g} = gateState(props, p, 0, n);
  const gateVis = p >= props.gateAt ? 1 - clamp01((p - props.gateAt - props.gateSpan - 0.02) / 0.04) : 0;
  const gx = S.x + 8 + g * (S.w - 16);
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} />
      {props.checks.map((c, i) => {
        const t = pop(c.at);
        return (
          <Card key={i} style={{position: 'absolute', left: S.x + i * (cw + cGap), top: 166, width: cw, height: 124,
            boxSizing: 'border-box', display: 'flex', alignItems: 'center', gap: 22, padding: '0 30px', opacity: t,
            border: `3px solid ${CLAUDE.BORDER}`, transform: `translateY(${(1 - t) * 16}px)`}}>
            <span style={{fontFamily: SANS, fontSize: 52, fontWeight: 700, color: SOFT}}>{i + 1}</span>
            <span style={{fontFamily: SERIF, fontSize: 52, fontWeight: 700, color: INK, lineHeight: 1.05}}>{c.label}</span>
          </Card>
        );
      })}
      {props.glyphs.map((gk, i) => {
        const x = S.x + i * (tw + gap);
        const appear = pop(props.tilesAt + i * 0.01);
        const {passed} = gateState(props, p, i, n);
        const fail = props.fails.includes(i);
        const drop = fail ? ease(passed) : 0;
        return (
          <React.Fragment key={i}>
            <Card style={{position: 'absolute', left: x, top: rowY + drop * 70, width: tw, height: th, boxSizing: 'border-box',
              display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 12,
              opacity: appear * (1 - 0.55 * drop), background: fail && passed > 0.5 ? CLAUDE.FOOTER : CLAUDE.CARD}}>
              <span style={{fontFamily: SANS, fontSize: 46, fontWeight: 700, color: SOFT, lineHeight: 1}}>{String(i + 1).padStart(2, '0')}</span>
              <TenGlyph kind={gk} size={88} />
            </Card>
            {fail ? (
              <div style={{position: 'absolute', left: x + (tw - 120) / 2, width: 120, top: rowY + th + 92, height: 60, borderRadius: 30,
                border: `3px solid ${CLAUDE.BORDER}`, background: CLAUDE.CARD, display: 'flex', alignItems: 'center', justifyContent: 'center',
                fontFamily: SANS, fontSize: 44, fontWeight: 700, color: INK, opacity: passed}}>{props.cutLabel}</div>
            ) : (
              <div style={{position: 'absolute', left: x + (tw - 70) / 2, top: rowY + th + 20, opacity: passed}}><Check size={70} /></div>
            )}
          </React.Fragment>
        );
      })}
      {/* the gate — the one accent */}
      <div style={{position: 'absolute', left: gx - 6, top: rowY - 40, width: 12, height: th + 200, borderRadius: 6,
        background: ACCENT, opacity: gateVis}} />
      <div style={{position: 'absolute', left: S.x, width: S.w, top: 776, textAlign: 'center', fontFamily: SERIF, fontSize: 76,
        fontWeight: 700, color: INK, opacity: pop(props.shipAt), lineHeight: 1}}>{props.shipLine}</div>
      <div style={{position: 'absolute', left: S.x, width: S.w, top: 880, textAlign: 'center', fontFamily: SERIF, fontSize: 58,
        fontStyle: 'italic', color: INK, opacity: pop(props.verdictAt)}}>{props.verdict}</div>
      <Caption text={props.caption} opacity={pop(props.tilesAt)} />
      <LogoBug />
    </AbsoluteFill>
  );
};
