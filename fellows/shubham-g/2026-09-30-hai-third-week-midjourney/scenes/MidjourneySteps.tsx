import React from 'react';
import {AbsoluteFill} from 'remotion';
import {z} from 'zod';
import {CLAUDE} from '../tokens/claude';
import {SAFE} from '../tokens/layout';
import {ACCENT, Card, INK, SANS, SERIF, SOFT, STAGE, useBeat} from './SocialAiVisibility';
import {LogoBug, SparkLine} from './ContentRepurpose';
import {Check} from './OneIntoTen';

/**
 * MidjourneySteps.tsx — concept illustrations (C3) for the ai-explainer reel
 * "Week 3 Learning: How to Use Midjourney?" (@Shubh & @HumanitariansAI).
 *
 * Five steps: a four-part prompt + --ar → a job of four images → refine (Vary
 * Subtle / Strong, or change one word) → upscale and use in three formats →
 * check before posting.
 *
 * HONESTY: Midjourney is never run (paid external service). Every "image" here is
 * <ScenePic>, a deterministic vector drawing of the drafted prompt, captioned
 * "Illustration — not Midjourney output". No Midjourney logo or UI imitation: the
 * prompt bar is a plain card.
 *
 * 16:9 layouts; native 9:16 layouts live in MidjourneySteps916.tsx and share these
 * zod schemas. `durationSeconds` = the beat's measured audio; every `*At` prop is a
 * beat fraction placed on the spoken word (faster-whisper timestamps). One
 * terracotta accent per beat (the --ar chip · the pick ring · the one-word strike ·
 * the --ar underlines · the loupe ring); accent is never used for text.
 */

const clamp01 = (v: number) => Math.min(1, Math.max(0, v));
const durationProp = {durationSeconds: z.number().default(16)};

// ─────────────────────────────────────────────────────────────────────────────
// ScenePic — "a lantern-lit bookshop on a rainy street, watercolor, warm evening light"
// Authored on a 160×90 stage centred on x=80; other aspects crop to the centre, so the
// shop (x 58–102) survives 16:9, 1:1 and 9:16. Muted illustration palette, kept well
// away from the terracotta accent.
// ─────────────────────────────────────────────────────────────────────────────
const SKY = ['#8C98A5', '#9690A2', '#8595A2', '#9A968C'];
const SHOP = ['#5E4A3A', '#4F5A4C', '#62503F', '#4C4A5A'];
const GOLD = '#F0C75E';
const WINDOW = '#EBD9A8';
const STREET = '#A8A290';
const SIDE = '#3D3929';

export type PicProps = {w: number; h: number; variant?: number; weather?: 'rain' | 'snow'; glow?: number;
  awning?: boolean; radius?: number; style?: React.CSSProperties};

export const ScenePic: React.FC<PicProps> = ({w, h, variant = 0, weather = 'rain', glow = 1, awning = false, radius = 14, style}) => {
  const v = ((variant % 4) + 4) % 4;
  const a = w / h;
  const vbH = 90, vbW = Math.min(160, vbH * a);
  const vbX = 80 - vbW / 2;
  const lx = [66, 94, 70, 90][v];
  const sideH = [[38, 52], [46, 34], [30, 44], [50, 40]][v];
  const drops = Array.from({length: 46}, (_, i) => ({x: (i * 37) % 160, y: (i * 23) % 78, r: 0.8 + ((i * 7) % 3) * 0.35}));
  return (
    <svg width={w} height={h} viewBox={`${vbX} 0 ${vbW} ${vbH}`} preserveAspectRatio="xMidYMid slice"
      style={{display: 'block', borderRadius: radius, ...style}}>
      <rect x={0} y={0} width={160} height={90} fill={SKY[v]} />
      {v % 2 === 1 && <circle cx={126} cy={16} r={6} fill="#E8E4D6" opacity={0.8} />}
      {/* side buildings */}
      <rect x={0} y={72 - sideH[0]} width={56} height={sideH[0]} fill={SIDE} />
      <rect x={104} y={72 - sideH[1]} width={56} height={sideH[1]} fill={SIDE} />
      {[10, 26, 40].map((x) => <rect key={x} x={x} y={72 - sideH[0] + 8} width={6} height={8} fill={WINDOW} opacity={0.55} />)}
      {[114, 132, 146].map((x) => <rect key={x} x={x} y={72 - sideH[1] + 8} width={6} height={8} fill={WINDOW} opacity={0.55} />)}
      {/* the bookshop */}
      <path d="M 56 30 L 80 16 L 104 30 Z" fill={SHOP[v]} />
      <rect x={58} y={30} width={44} height={42} fill={SHOP[v]} />
      <rect x={66} y={33} width={28} height={6} rx={1} fill="#EFE6CF" />
      <rect x={62} y={43} width={16} height={18} fill={WINDOW} />
      <rect x={84} y={43} width={14} height={29} fill="#3A3026" />
      {[46, 51, 56].map((y) => <line key={y} x1={63} y1={y} x2={77} y2={y} stroke="#9C7E55" strokeWidth={0.8} />)}
      {awning && <path d="M 60 41 L 100 41 L 97 46 L 63 46 Z" fill="#8B9A7E" />}
      {/* lantern + glow */}
      <circle cx={lx} cy={40} r={9 * glow} fill={GOLD} opacity={0.28} />
      <rect x={lx - 2} y={37} width={4} height={6} rx={1} fill={GOLD} />
      <line x1={lx} y1={31} x2={lx} y2={37} stroke={SIDE} strokeWidth={0.8} />
      {/* street + reflection */}
      <rect x={0} y={72} width={160} height={18} fill={STREET} />
      <rect x={lx - 3} y={74} width={6} height={12} fill={GOLD} opacity={0.3} />
      {weather === 'rain'
        ? drops.map((d, i) => <line key={i} x1={d.x} y1={d.y} x2={d.x - 1.6} y2={d.y + 5} stroke="#DCE3EA" strokeWidth={0.5} opacity={0.7} />)
        : drops.map((d, i) => <circle key={i} cx={d.x} cy={d.y} r={d.r} fill="#FFFFFF" opacity={0.85} />)}
      {weather === 'snow' && <rect x={0} y={70} width={160} height={4} fill="#F4F2EC" />}
    </svg>
  );
};

/** A picture in a card frame with an optional corner number. */
export const Frame: React.FC<PicProps & {n?: number; nPx?: number; left: number; top: number; opacity?: number;
  blur?: number; border?: string}> = ({n, nPx = 44, left, top, opacity = 1, blur = 0, border, ...pic}) => (
  <div style={{position: 'absolute', left, top, width: pic.w, height: pic.h, borderRadius: 16, opacity,
    boxShadow: '0 12px 36px rgba(61,57,41,0.16)', border: border ?? `3px solid ${CLAUDE.BORDER}`, overflow: 'hidden', boxSizing: 'content-box'}}>
    <div style={{filter: blur > 0 ? `blur(${blur}px)` : undefined}}><ScenePic {...pic} radius={0} /></div>
    {n !== undefined && (
      <div style={{position: 'absolute', left: 12, top: 12, minWidth: nPx * 1.3, height: nPx * 1.3, borderRadius: nPx * 0.65,
        background: CLAUDE.CARD, display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: SANS,
        fontSize: nPx, fontWeight: 700, color: INK}}>{n}</div>
    )}
  </div>
);

const Caption: React.FC<{text: string; opacity: number}> = ({text, opacity}) => (
  <div style={{position: 'absolute', left: SAFE.x, top: SAFE.b - 44, fontFamily: SANS, fontSize: 40, color: SOFT, opacity}}>{text}</div>
);

const ILLUSTRATION = 'Illustration — not Midjourney output';

// ─────────────────────────────────────────────────────────────────────────────
// B02 — step 1: the four-part prompt + one parameter
// ─────────────────────────────────────────────────────────────────────────────
export const promptAnatomySchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('Step 1 · The prompt'),
  barAt: z.number().default(0.03),
  parts: z.array(z.object({label: z.string(), question: z.string(), value: z.string(), at: z.number()})).default([
    {label: 'SUBJECT', question: 'what’s in it', value: 'a lantern-lit bookshop', at: 0.246},
    {label: 'SETTING', question: 'where it is', value: 'on a rainy street', at: 0.385},
    {label: 'STYLE', question: 'how it looks', value: 'watercolor illustration', at: 0.49},
    {label: 'LIGHT', question: 'the mood', value: 'warm evening light', at: 0.594},
  ]),
  barLabel: z.string().default('PROMPT'),
  param: z.string().default('--ar 16:9'),
  paramAt: z.number().default(0.75),
  shapes: z.array(z.object({ar: z.string(), label: z.string(), w: z.number(), h: z.number()})).default([
    {ar: '--ar 16:9', label: 'wide', w: 16, h: 9},
    {ar: '--ar 1:1', label: 'square', w: 1, h: 1},
    {ar: '--ar 9:16', label: 'tall', w: 9, h: 16},
  ]),
  activeShape: z.number().default(0),
  shapesAt: z.number().default(0.84),
  caption: z.string().default('Example prompt — illustrative'),
});
export type PromptAnatomyProps = z.infer<typeof promptAnatomySchema>;

export const PromptAnatomy: React.FC<PromptAnatomyProps> = (props) => {
  const {pop} = useBeat(props.durationSeconds);
  const S = SAFE;
  const n = props.parts.length, gap = 28;
  const cw = (S.w - gap * (n - 1)) / n;
  const barIn = pop(props.barAt), pIn = pop(props.paramAt), shIn = pop(props.shapesAt);
  const shapeH = 230;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} />
      {props.parts.map((pt, i) => {
        const t = pop(pt.at);
        return (
          <Card key={i} style={{position: 'absolute', left: S.x + i * (cw + gap), top: 160, width: cw, height: 150,
            boxSizing: 'border-box', padding: '22px 28px', opacity: 0.45 + 0.55 * t, background: t > 0.5 ? CLAUDE.CARD : CLAUDE.FOOTER}}>
            <div style={{fontFamily: SANS, fontSize: 44, fontWeight: 700, letterSpacing: '0.1em', color: SOFT, lineHeight: 1}}>
              {`${i + 1} · ${pt.label}`}</div>
            <div style={{fontFamily: SERIF, fontSize: 52, fontStyle: 'italic', color: INK, marginTop: 18, opacity: t}}>{pt.question}</div>
          </Card>
        );
      })}
      {/* the prompt bar: each part's value drops in under its card's word; the parameter lands last */}
      <div style={{position: 'absolute', left: S.x, top: 350, width: S.w, height: 232, borderRadius: 26, background: CLAUDE.CARD,
        border: `2px solid ${CLAUDE.BORDER}`, boxSizing: 'border-box', padding: '22px 30px', opacity: barIn,
        boxShadow: '0 14px 44px rgba(61,57,41,0.12)'}}>
        <div style={{fontFamily: SANS, fontSize: 40, fontWeight: 700, letterSpacing: '0.12em', color: SOFT, lineHeight: 1}}>{props.barLabel}</div>
        <div style={{display: 'flex', flexWrap: 'wrap', gap: '14px 16px', marginTop: 16}}>
          {props.parts.map((pt, i) => {
            const t = pop(pt.at + 0.02);
            return (
              <span key={i} style={{fontFamily: SERIF, fontSize: 50, color: INK, padding: '2px 18px', borderRadius: 14,
                background: CLAUDE.FOOTER, border: `2px solid ${CLAUDE.BORDER}`, opacity: t, transform: `translateY(${(1 - t) * -26}px)`,
                whiteSpace: 'nowrap'}}>{pt.value}{i < n - 1 ? ',' : ''}</span>
            );
          })}
          <span style={{fontFamily: SANS, fontSize: 48, fontWeight: 700, color: INK, padding: '4px 18px', borderRadius: 14,
            border: `4px solid ${ACCENT}`, background: CLAUDE.CARD, opacity: pIn, transform: `scale(${1.2 - 0.2 * pIn})`,
            whiteSpace: 'nowrap'}}>{props.param}</span>
        </div>
      </div>
      {/* the parameter sets the frame's shape */}
      <div style={{position: 'absolute', left: S.x, top: 628, width: S.w, height: 330, display: 'flex', justifyContent: 'center',
        alignItems: 'flex-end', gap: 90}}>
        {props.shapes.map((sh, i) => {
          const active = i === props.activeShape;
          const h = shapeH, w = (h * sh.w) / sh.h;
          return (
            <div key={i} style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 18,
              opacity: active ? pop(props.paramAt + 0.04) : 0.45 * shIn}}>
              {active
                ? <div style={{borderRadius: 14, border: `4px solid ${INK}`, overflow: 'hidden'}}><ScenePic w={w} h={h} radius={0} /></div>
                : <div style={{width: w, height: h, borderRadius: 14, border: `4px dashed ${SOFT}`, boxSizing: 'border-box'}} />}
              <div style={{fontFamily: SANS, fontSize: 44, fontWeight: 700, color: INK, whiteSpace: 'nowrap'}}>{`${sh.ar} · ${sh.label}`}</div>
            </div>
          );
        })}
      </div>
      <Caption text={props.caption} opacity={barIn} />
      <LogoBug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B04 — step 2: paste, generate, a job of four, pick one
// ─────────────────────────────────────────────────────────────────────────────
export const fourGridSchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('Step 2 · Generate'),
  barLabel: z.string().default('IMAGINE BAR · midjourney.com'),
  prompt: z.string().default('a lantern-lit bookshop on a rainy street, watercolor illustration, warm evening light --ar 16:9'),
  barAt: z.number().default(0.13),
  altLabel: z.string().default('or  /imagine  in Discord'),
  altAt: z.number().default(0.345),
  planLabel: z.string().default('Paid tool — you’ll need a plan'),
  planAt: z.number().default(0.534),
  gridAt: z.number().default(0.7),
  gridSpan: z.number().default(0.1),
  gridLabel: z.string().default('One job → four images'),
  pickIndex: z.number().default(2),
  pickAt: z.number().default(0.876),
  pickLine: z.string().default('Pick the one closest to what you pictured.'),
  caption: z.string().default(ILLUSTRATION),
});
export type FourGridProps = z.infer<typeof fourGridSchema>;

/** Resolve progress of grid frame i: blur → sharp, staggered. */
export const resolveAt = (props: FourGridProps, i: number) => props.gridAt + (i * props.gridSpan) / 4;

export const FourGrid: React.FC<FourGridProps> = (props) => {
  const {pop, ramp} = useBeat(props.durationSeconds);
  const S = SAFE;
  const leftW = 780;
  const gx = S.x + leftW + 60, gw = S.r - gx, gap = 24;
  const fw = (gw - gap) / 2, fh = (fw * 9) / 16, gy = 172;
  const bIn = pop(props.barAt), aIn = pop(props.altAt), plIn = pop(props.planAt), pIn = pop(props.pickAt);
  const px = gx + (props.pickIndex % 2) * (fw + gap), py = gy + Math.floor(props.pickIndex / 2) * (fh + gap);
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} />
      <Card style={{position: 'absolute', left: S.x, top: 172, width: leftW, height: 350, boxSizing: 'border-box', padding: '26px 32px',
        opacity: bIn, transform: `translateY(${(1 - bIn) * 18}px)`}}>
        <div style={{fontFamily: SANS, fontSize: 46, fontWeight: 700, letterSpacing: '0.06em', color: SOFT, lineHeight: 1}}>{props.barLabel}</div>
        <div style={{fontFamily: SERIF, fontSize: 54, color: INK, lineHeight: 1.14, marginTop: 20}}>{props.prompt}</div>
      </Card>
      <div style={{position: 'absolute', left: S.x, top: 552, height: 84, padding: '0 30px', borderRadius: 42, background: CLAUDE.FOOTER,
        border: `2px solid ${CLAUDE.BORDER}`, display: 'flex', alignItems: 'center', fontFamily: SANS, fontSize: 46, fontWeight: 700,
        color: INK, whiteSpace: 'pre', opacity: aIn}}>{props.altLabel}</div>
      <div style={{position: 'absolute', left: S.x, top: 672, width: leftW, fontFamily: SERIF, fontSize: 58, fontStyle: 'italic',
        color: INK, opacity: plIn}}>{props.planLabel}</div>
      {[0, 1, 2, 3].map((i) => {
        const t = ramp(resolveAt(props, i), 0.07);
        return (
          <Frame key={i} n={i + 1} left={gx + (i % 2) * (fw + gap)} top={gy + Math.floor(i / 2) * (fh + gap)} w={fw} h={fh}
            variant={i} opacity={clamp01(t * 2.5)} blur={(1 - t) * 18} />
        );
      })}
      <div style={{position: 'absolute', left: px - 14, top: py - 14, width: fw + 28, height: fh + 28, borderRadius: 26,
        border: `7px solid ${ACCENT}`, boxSizing: 'border-box', opacity: pIn, transform: `scale(${1.05 - 0.05 * pIn})`}} />
      <div style={{position: 'absolute', left: gx, width: gw, top: gy + 2 * fh + gap + 26, textAlign: 'center', fontFamily: SANS,
        fontSize: 46, fontWeight: 700, color: SOFT, opacity: pop(resolveAt(props, 3) + 0.04)}}>{props.gridLabel}</div>
      <div style={{position: 'absolute', left: S.x, width: S.w, top: 880, textAlign: 'center', fontFamily: SERIF, fontSize: 58,
        fontWeight: 700, color: INK, opacity: pIn}}>{props.pickLine}</div>
      <Caption text={props.caption} opacity={pop(props.gridAt)} />
      <LogoBug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B05 — step 3: Vary (Subtle) · Vary (Strong) · or change one word
// ─────────────────────────────────────────────────────────────────────────────
export const refineLoopSchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('Step 3 · Refine'),
  pickVariant: z.number().default(2),
  pickLabel: z.string().default('Your pick'),
  pickAt: z.number().default(0.03),
  subtleLabel: z.string().default('Vary (Subtle)'),
  subtleNote: z.string().default('small details'),
  subtleAt: z.number().default(0.14),
  strongLabel: z.string().default('Vary (Strong)'),
  strongNote: z.string().default('bigger changes'),
  strongAt: z.number().default(0.321),
  promptLabel: z.string().default('IDEA OFF? CHANGE THE PROMPT'),
  promptAt: z.number().default(0.5),
  before: z.string().default('…bookshop on a '),
  oldWord: z.string().default('rainy'),
  newWord: z.string().default('snowy'),
  after: z.string().default(' street'),
  strikeAt: z.number().default(0.701),
  typeAt: z.number().default(0.748),
  newPicAt: z.number().default(0.8),
  line: z.string().default('One word at a time — see what each word does.'),
  lineAt: z.number().default(0.86),
  caption: z.string().default(ILLUSTRATION),
});
export type RefineLoopProps = z.infer<typeof refineLoopSchema>;

/** The one-word swap: struck old word (accent strike), typed new word. */
export const WordSwap: React.FC<{props: RefineLoopProps; px: number; ramp: (f: number, d?: number) => number}> = ({props, px, ramp}) => {
  const strike = ramp(props.strikeAt, 0.04);
  const typed = ramp(props.typeAt, 0.05);
  const shown = props.newWord.slice(0, Math.round(typed * props.newWord.length));
  return (
    <span style={{fontFamily: SERIF, fontSize: px, color: INK, whiteSpace: 'nowrap'}}>
      {props.before}
      <span style={{position: 'relative', opacity: 1 - 0.55 * strike}}>
        {props.oldWord}
        <span style={{position: 'absolute', left: -4, top: '52%', height: px * 0.12, borderRadius: 4, background: ACCENT,
          width: `calc(${strike * 100}% + 8px)`, opacity: strike > 0 ? 1 : 0}} />
      </span>
      {typed > 0 && <span style={{fontWeight: 700}}>{' '}{shown}</span>}
      {props.after}
    </span>
  );
};

export const RefineLoop: React.FC<RefineLoopProps> = (props) => {
  const {pop, ramp, width, height} = useBeat(props.durationSeconds);
  const S = SAFE;
  const fw = 520, fh = 292.5, top = 176, gap = (S.w - 3 * fw) / 2;
  const xs = [S.x, S.x + fw + gap, S.x + 2 * (fw + gap)];
  const sIn = pop(props.subtleAt), stIn = pop(props.strongAt), prIn = pop(props.promptAt), nIn = pop(props.newPicAt);
  const labels: [string, string, number][] = [[props.pickLabel, '', pop(props.pickAt)], [props.subtleLabel, props.subtleNote, sIn],
    [props.strongLabel, props.strongNote, stIn]];
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} />
      <svg width={width} height={height} style={{position: 'absolute', inset: 0}}>
        {nIn > 0 && <path d={`M ${S.x + 1124} 760 L ${xs[2] - 18} 760`} fill="none" stroke={SOFT} strokeWidth={5}
          strokeDasharray={200} strokeDashoffset={200 * (1 - ramp(props.newPicAt - 0.02, 0.04))} />}
      </svg>
      <Frame left={xs[0]} top={top} w={fw} h={fh} variant={props.pickVariant} opacity={pop(props.pickAt)} border={`4px solid ${INK}`} />
      <Frame left={xs[1]} top={top} w={fw} h={fh} variant={props.pickVariant} glow={1.35} opacity={sIn} />
      <Frame left={xs[2]} top={top} w={fw} h={fh} variant={(props.pickVariant + 1) % 4} awning opacity={stIn} />
      {labels.map(([l, note, t], i) => (
        <div key={i} style={{position: 'absolute', left: xs[i], width: fw, top: top + fh + 22, textAlign: 'center', opacity: t}}>
          <div style={{fontFamily: SERIF, fontSize: 54, fontWeight: 700, color: INK, lineHeight: 1}}>{l}</div>
          {note && <div style={{fontFamily: SANS, fontSize: 48, fontStyle: 'italic', color: SOFT, marginTop: 10}}>{note}</div>}
        </div>
      ))}
      <Card style={{position: 'absolute', left: S.x, top: 650, width: 1110, height: 220, boxSizing: 'border-box', padding: '26px 34px',
        opacity: prIn, transform: `translateY(${(1 - prIn) * 18}px)`}}>
        <div style={{fontFamily: SANS, fontSize: 40, fontWeight: 700, letterSpacing: '0.1em', color: SOFT, lineHeight: 1}}>{props.promptLabel}</div>
        <div style={{marginTop: 30}}><WordSwap props={props} px={54} ramp={ramp} /></div>
      </Card>
      <Frame left={xs[2]} top={650} w={fw} h={fh * 0.75 > 220 ? 220 : fh * 0.75} variant={props.pickVariant} weather="snow" opacity={nIn} />
      <div style={{position: 'absolute', left: S.x, width: S.w, top: 912, textAlign: 'center', fontFamily: SERIF, fontSize: 56,
        fontWeight: 700, color: INK, opacity: pop(props.lineAt)}}>{props.line}</div>
      <Caption text={props.caption} opacity={pop(props.pickAt)} />
      <LogoBug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B06 — step 4: upscale, download, use in three formats (set --ar per format)
// ─────────────────────────────────────────────────────────────────────────────
export const upscaleToUseSchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('Step 4 · Upscale & use'),
  pickVariant: z.number().default(2),
  growAt: z.number().default(0.04),
  options: z.array(z.object({label: z.string(), note: z.string(), at: z.number()})).default([
    {label: 'Upscale (Subtle)', note: 'sharpens what’s there', at: 0.16},
    {label: 'Upscale (Creative)', note: 'adds new detail', at: 0.31},
  ]),
  formats: z.array(z.object({label: z.string(), ar: z.string(), w: z.number(), h: z.number(), at: z.number()})).default([
    {label: 'Blog header', ar: '--ar 16:9', w: 16, h: 9, at: 0.566},
    {label: 'Square post', ar: '--ar 1:1', w: 1, h: 1, at: 0.621},
    {label: 'Story', ar: '--ar 9:16', w: 9, h: 16, at: 0.68},
  ]),
  arAt: z.number().default(0.78),
  tip: z.string().default('Set --ar per format — don’t crop later.'),
  tipAt: z.number().default(0.9),
  caption: z.string().default(ILLUSTRATION),
});
export type UpscaleToUseProps = z.infer<typeof upscaleToUseSchema>;

export const UpscaleToUse: React.FC<UpscaleToUseProps> = (props) => {
  const {pop, ramp} = useBeat(props.durationSeconds);
  const S = SAFE;
  const g = ramp(props.growAt, 0.1), ge = g * g * (3 - 2 * g);
  const bigW = 660, bigH = (bigW * 9) / 16;
  const k = 0.42 + 0.58 * ge;
  const arIn = ramp(props.arAt, 0.06);
  const rowH = 270, rowTop = 610;
  const fws = props.formats.map((f) => (rowH * f.w) / f.h);
  const rowGap = 110;
  const rowW = fws.reduce((a, b) => a + b, 0) + rowGap * (props.formats.length - 1);
  let fx = S.x + (S.w - rowW) / 2;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} />
      <div style={{position: 'absolute', left: S.x, top: 150, width: bigW * k, height: bigH * k, borderRadius: 16, overflow: 'hidden',
        border: `4px solid ${INK}`, opacity: pop(0.01)}}>
        <ScenePic w={bigW * k} h={bigH * k} variant={props.pickVariant} radius={0} />
      </div>
      {props.options.map((o, i) => {
        const t = pop(o.at);
        return (
          <Card key={i} style={{position: 'absolute', left: S.x + bigW + 60, top: 150 + i * 150, width: S.w - bigW - 60, height: 128,
            boxSizing: 'border-box', padding: '0 34px', display: 'flex', alignItems: 'center', gap: 26, opacity: t,
            transform: `translateX(${(1 - t) * 24}px)`}}>
            <span style={{fontFamily: SERIF, fontSize: 54, fontWeight: 700, color: INK, whiteSpace: 'nowrap'}}>{o.label}</span>
            <span style={{fontFamily: SANS, fontSize: 44, fontStyle: 'italic', color: SOFT, whiteSpace: 'nowrap'}}>{o.note}</span>
          </Card>
        );
      })}
      <div style={{position: 'absolute', left: S.x + bigW + 60, top: 470, width: S.w - bigW - 60, fontFamily: SERIF, fontSize: 52,
        fontStyle: 'italic', color: INK, opacity: pop(props.tipAt)}}>{props.tip}</div>
      {props.formats.map((f, i) => {
        const w = fws[i];
        const x = fx;
        fx += w + rowGap;
        const t = pop(f.at);
        return (
          <div key={i} style={{position: 'absolute', left: x, top: rowTop, width: w, opacity: t, transform: `translateY(${(1 - t) * 30}px)`}}>
            <div style={{borderRadius: 14, overflow: 'hidden', border: `3px solid ${CLAUDE.BORDER}`, boxShadow: '0 10px 30px rgba(61,57,41,0.14)'}}>
              <ScenePic w={w} h={rowH} variant={props.pickVariant} radius={0} />
            </div>
            <div style={{position: 'absolute', left: -120, right: -120, top: rowH + 14, textAlign: 'center', fontFamily: SANS,
              fontSize: 44, fontWeight: 700, color: INK, whiteSpace: 'nowrap', lineHeight: 1.12}}>
              <div>{f.label}</div>
              <span style={{position: 'relative', color: SOFT}}>
                {f.ar}
                <span style={{position: 'absolute', left: 0, right: 0, bottom: -10, height: 7, borderRadius: 4, background: ACCENT,
                  transform: `scaleX(${arIn})`, transformOrigin: 'left'}} />
              </span>
            </div>
          </div>
        );
      })}
      <div style={{position: 'absolute', left: S.x, top: 150 + bigH + 22, fontFamily: SANS, fontSize: 40, color: SOFT,
        opacity: pop(0.01)}}>{props.caption}</div>
      <LogoBug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B07 — step 5: check before posting (a loupe finds garbled sign text)
// ─────────────────────────────────────────────────────────────────────────────
export const postCheckSchema = z.object({
  ...durationProp,
  sparkLine: z.string().default('Step 5 · Check before posting'),
  pickVariant: z.number().default(2),
  loupeAt: z.number().default(0.17),
  flawLine: z.string().default('Garbled sign text — easy to miss at full size.'),
  flawAt: z.number().default(0.44),
  checks: z.array(z.object({label: z.string(), at: z.number()})).default([
    {label: 'Zoom in: hands, faces, text', at: 0.2},
    {label: 'No real person without consent', at: 0.56},
    {label: 'Say it’s AI-made', at: 0.7},
    {label: 'Check your plan’s terms', at: 0.83},
  ]),
  caption: z.string().default(ILLUSTRATION),
});
export type PostCheckProps = z.infer<typeof postCheckSchema>;

/** Letter-like strokes that almost spell BOOKS — the kind of text error to catch. */
export const GarbledSign: React.FC<{w: number; h: number}> = ({w, h}) => {
  const glyphs = [
    'M 8 4 V 56 M 8 4 H 22 Q 34 4 34 16 Q 34 28 20 30 H 8 M 20 30 Q 36 32 36 44 Q 36 56 22 56 H 8',
    'M 22 4 Q 38 4 38 30 Q 38 56 22 56 Q 6 56 6 30 Q 6 4 22 4',
    'M 22 4 Q 38 4 38 30 Q 38 56 22 56 Q 6 56 6 30 Q 6 4 22 4 M 4 54 L 40 6',
    'M 8 4 V 56 M 36 4 L 10 32 L 34 56 M 24 20 L 40 12',
    'M 6 6 H 36 L 6 54 H 36 M 14 30 H 28',
  ];
  return (
    <svg width={w} height={h} viewBox="0 0 230 60">
      {glyphs.map((d, i) => (
        <path key={i} d={d} transform={`translate(${4 + i * 45} 0)`} fill="none" stroke={INK} strokeWidth={5}
          strokeLinecap="round" strokeLinejoin="round" />
      ))}
    </svg>
  );
};

/** Frame + magnifying loupe over the sign. `fw` is the frame width (16:9). */
export const LoupeFrame: React.FC<{left: number; top: number; fw: number; variant: number; loupe: number; r: number}> = (
  {left, top, fw, variant, loupe, r}) => {
  const fh = (fw * 9) / 16;
  // sign centre in the 16:9 stage: x 80, y 36 of 160×90
  const sx = left + fw * 0.5, sy = top + fh * (36 / 90);
  const lx = sx + fw * 0.2, ly = sy + fh * 0.36;
  return (
    <>
      <div style={{position: 'absolute', left, top, width: fw, height: fh, borderRadius: 16, overflow: 'hidden',
        border: `3px solid ${CLAUDE.BORDER}`, boxShadow: '0 12px 36px rgba(61,57,41,0.16)'}}>
        <ScenePic w={fw} h={fh} variant={variant} radius={0} />
      </div>
      <svg width={1920} height={1920} style={{position: 'absolute', left: 0, top: 0, pointerEvents: 'none', opacity: loupe}}>
        <line x1={sx} y1={sy} x2={lx} y2={ly} stroke={INK} strokeWidth={4} strokeDasharray="10 8" />
      </svg>
      <div style={{position: 'absolute', left: lx - r, top: ly - r, width: 2 * r, height: 2 * r, borderRadius: r, overflow: 'hidden',
        background: '#EFE6CF', border: `8px solid ${ACCENT}`, boxSizing: 'border-box', display: 'flex', alignItems: 'center',
        justifyContent: 'center', opacity: loupe, transform: `scale(${0.6 + 0.4 * loupe})`, boxShadow: '0 16px 40px rgba(61,57,41,0.22)'}}>
        <GarbledSign w={r * 1.55} h={r * 0.42} />
      </div>
    </>
  );
};

export const PostCheck: React.FC<PostCheckProps> = (props) => {
  const {pop} = useBeat(props.durationSeconds);
  const S = SAFE;
  const fw = 800;
  const listX = S.x + fw + 70, listW = S.r - listX;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} />
      <LoupeFrame left={S.x} top={170} fw={fw} variant={props.pickVariant} loupe={pop(props.loupeAt)} r={140} />
      <div style={{position: 'absolute', left: S.x, width: fw, top: 690, fontFamily: SERIF, fontSize: 52, fontStyle: 'italic',
        color: INK, lineHeight: 1.15, opacity: pop(props.flawAt)}}>{props.flawLine}</div>
      <Card style={{position: 'absolute', left: listX, top: 170, width: listW, height: 740, boxSizing: 'border-box', padding: '36px 40px'}}>
        {props.checks.map((c, i) => {
          const t = pop(c.at);
          return (
            <div key={i} style={{display: 'flex', alignItems: 'center', gap: 26, height: 168, opacity: 0.45 + 0.55 * t}}>
              <div style={{width: 76, height: 76, flexShrink: 0, borderRadius: 18, border: `3px solid ${CLAUDE.BORDER}`,
                background: CLAUDE.FOOTER, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                <div style={{opacity: t, transform: `scale(${0.6 + 0.4 * t})`}}><Check size={60} /></div>
              </div>
              <span style={{fontFamily: SERIF, fontSize: 52, fontWeight: 700, color: INK, lineHeight: 1.08}}>{c.label}</span>
            </div>
          );
        })}
      </Card>
      <Caption text={props.caption} opacity={pop(0.01)} />
      <LogoBug />
    </AbsoluteFill>
  );
};
