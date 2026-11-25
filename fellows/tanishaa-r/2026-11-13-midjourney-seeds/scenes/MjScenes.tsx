/**
 * MjScenes.tsx — Remotion components for "Why the Same Prompt Gives Four Different Images"
 * (Midjourney seeds; Humanitarians AI fellow video, Tanishaa). Registered in Root.tsx under
 * the folder "MidjourneySeeds".
 *
 * Same look as GpsScenes / QrScenes: Claude cream, ink, terracotta as the one accent.
 * 1920x1080 and native 1080x1920 <Name>916, 30 fps. Every reveal is a prop cued to Bella's
 * MEASURED word. Every picture is real output of youtube/midjourney-seeds/demo/seed_demo.py,
 * a TOY generator (not Midjourney), copied to public/midjourney-seeds/. The Midjourney mark
 * is public/logos/midjourney/midjourney-01.svg (LOGO LAW).
 */
import React from 'react';
import { AbsoluteFill, Img, staticFile, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { HaiBug } from './RagScenes';

const BG = '#FAF9F5';
const INK = '#3D3929';
const SOFT = '#6C6959';
const CARD = '#FFFFFF';
const BORDER = '#E5E2D9';
const ACC = '#D97757';
const ACC_TEXT = '#AF4B2D';
const OK = '#3F6B4A';
const SERIF = '"EB Garamond", Georgia, "Times New Roman", serif';
const SANS = '-apple-system, "SF Pro Text", "Segoe UI", "Helvetica Neue", sans-serif';
const MONO = 'ui-monospace, "SF Mono", Menlo, monospace';

const SX = 96;
const PX = 54, PY = 96, PSERIF = 92, PSANS = 72;
const PW = 1080;

const cl = (v: number, a = 0, b = 1) => Math.min(b, Math.max(a, v));
let FADE = 0.03;
const rise = (t: number, a: number, len = FADE) => {
  const p = cl(interpolate(t, [a, a + len], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));
  return 1 - Math.pow(1 - p, 3);
};
const useT = () => {
  const frame = useCurrentFrame();
  const { durationInFrames, fps } = useVideoConfig();
  FADE = (0.35 * fps) / Math.max(1, durationInFrames);
  return frame / Math.max(1, durationInFrames - 1);
};
const dur = { durationSeconds: z.number().optional() };
/** faint from the start, full on its word — the screen is never empty while Bella talks */
const ghost = (o: number) => 0.55 + 0.45 * o;

const PBug: React.FC = () => (
  <Img src={staticFile('logos/humanitarians/humanitarians-logo-1.svg')}
    style={{ position: 'absolute', right: PX, bottom: PY, height: 60, opacity: 0.32 }} />
);
const Bug: React.FC<{ portrait: boolean }> = ({ portrait }) => (portrait ? <PBug /> : <HaiBug />);
const MjLogo: React.FC<{ h: number; o?: number }> = ({ h, o = 1 }) => (
  <Img src={staticFile('logos/midjourney/midjourney-01.svg')} style={{ height: h, width: h, opacity: o, display: 'block' }} />
);
const Pic: React.FC<{ src: string; size: number; o?: number; border?: string; style?: React.CSSProperties }> =
  ({ src, size, o = 1, border = BORDER, style }) => (
    <Img src={staticFile(src)} style={{ width: size, height: size, borderRadius: 14, border: `3px solid ${border}`, opacity: o,
      display: 'block', boxSizing: 'border-box', ...style }} />
  );
const PromptBar: React.FC<{ text: string; flag?: string; flagO?: number; o: number; size: number; portrait?: boolean }> =
  ({ text, flag, flagO = 0, o, size, portrait }) => (
    <div style={{ display: 'inline-flex', alignItems: 'center', gap: 18, background: CARD, border: `3px solid ${BORDER}`, borderRadius: 999,
      padding: portrait ? '18px 36px' : '14px 34px', opacity: o, boxShadow: '0 4px 20px rgba(61,57,41,0.08)', flexWrap: 'wrap' }}>
      <span style={{ fontFamily: SERIF, fontSize: size, color: INK }}>{text}</span>
      {flag ? <span style={{ fontFamily: MONO, fontSize: size * 0.82, color: ACC_TEXT, opacity: flagO }}>{flag}</span> : null}
    </div>
  );
const Line: React.FC<{ text: string; o: number; size: number; color?: string; font?: string; style?: React.CSSProperties }> =
  ({ text, o, size, color = INK, font = SERIF, style }) => (
    <div style={{ fontFamily: font, fontSize: size, lineHeight: 1.12, color, opacity: o, transform: `translateY(${(1 - o) * 18}px)`, ...style }}>{text}</div>
  );

// ===========================================================================
// MjPuzzle — one prompt, four different pictures; the same prompt again, four more.
// ===========================================================================
export const mjPuzzleSchema = z.object({
  prompt: z.string(), images: z.array(z.string()), more: z.array(z.string()),
  promptAt: z.number(), imagesAt: z.number(), againAt: z.number(), moreAt: z.number(),
  label: z.string(), labelAt: z.number(), questionAt: z.number(),
  ...dur,
});
const PuzzleScene: React.FC<{ p: z.infer<typeof mjPuzzleSchema>; portrait: boolean }> = ({ p, portrait }) => {
  const t = useT();
  const po = rise(t, p.promptAt), io = rise(t, p.imagesAt), ag = rise(t, p.againAt), mo = rise(t, p.moreAt);
  const lo = rise(t, p.labelAt), qo = rise(t, p.questionAt);
  const size = portrait ? 440 : 405;
  const grid = (srcs: string[], o: number) => (
    <div style={{ display: 'grid', gridTemplateColumns: portrait ? 'repeat(2, auto)' : 'repeat(4, auto)', gap: portrait ? 28 : 36 }}>
      {srcs.map((s, i) => <Pic key={i} src={s} size={size} o={o} style={{ transform: `translateY(${(1 - o) * 30}px)` }} />)}
    </div>
  );
  const showMore = mo > 0.01;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: portrait ? PX : SX, right: portrait ? PX : SX, top: portrait ? PY : 70,
        display: 'flex', alignItems: 'center', gap: 30 }}>
        <MjLogo h={portrait ? 120 : 96} />
        <PromptBar text={p.prompt} o={ghost(po)} size={portrait ? PSERIF - 6 : 58} portrait={portrait}
          flag={!portrait && ag > 0.5 ? '↻ again' : undefined} flagO={ag} />
      </div>
      {portrait ? <div style={{ position: 'absolute', left: PX + 150, top: PY + 160, fontFamily: MONO, fontSize: PSANS + 4, color: ACC_TEXT,
        opacity: ag }}>↻ again</div> : null}
      <div style={{ position: 'absolute', left: portrait ? (PW - 2 * size - 28) / 2 : SX, top: portrait ? 370 : 230 }}>
        <div style={{ position: 'absolute', opacity: 1 - mo }}>{grid(p.images, io)}</div>
        <div style={{ opacity: showMore ? 1 : 0 }}>{grid(p.more, mo)}</div>
      </div>
      <div style={{ position: 'absolute', left: portrait ? PX : SX, right: portrait ? PX : SX, top: portrait ? 1340 : 720 }}>
        <Line text={p.label} o={lo} size={portrait ? PSERIF : 64} color={ACC_TEXT} />
        <Line text="Where does the difference come from?" o={qo} size={portrait ? PSERIF - 6 : 56} style={{ marginTop: portrait ? 30 : 16 }} />
      </div>
      <Bug portrait={portrait} />
    </AbsoluteFill>
  );
};
export const MjPuzzle: React.FC<z.infer<typeof mjPuzzleSchema>> = (p) => <PuzzleScene p={p} portrait={false} />;
export const MjPuzzle916: React.FC<z.infer<typeof mjPuzzleSchema>> = (p) => <PuzzleScene p={p} portrait />;

// ===========================================================================
// MjNoise — every image starts as random noise (TV static); the model cleans it up.
// ===========================================================================
export const mjNoiseSchema = z.object({
  noise: z.string(), picture: z.string(), noiseAt: z.number(), label: z.string(), labelAt: z.number(),
  quote: z.string(), quoteAt: z.number(), cleanAt: z.number(),
  ...dur,
});
const NoiseScene: React.FC<{ p: z.infer<typeof mjNoiseSchema>; portrait: boolean }> = ({ p, portrait }) => {
  const t = useT();
  const no = rise(t, p.noiseAt), lo = rise(t, p.labelAt), qo = rise(t, p.quoteAt);
  // "step by step": the picture comes through in five visible steps after cleanAt
  const prog = cl((t - p.cleanAt) / Math.max(0.05, 0.92 - p.cleanAt));
  const step = Math.floor(prog * 5) / 5;
  const size = portrait ? 860 : 820;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: portrait ? (PW - size) / 2 : SX + 20, top: portrait ? PY + 40 : 130, width: size, height: size }}>
        <Pic src={p.noise} size={size} o={ghost(no)} style={{ position: 'absolute' }} />
        <Pic src={p.picture} size={size} o={step} style={{ position: 'absolute', filter: `blur(${(1 - step) * 24}px)` }} />
      </div>
      <div style={{ position: 'absolute', left: portrait ? PX : SX + 20 + size + 80, right: portrait ? PX : SX, top: portrait ? 1040 : 170 }}>
        <Line text={p.label} o={lo} size={portrait ? PSERIF : 66} />
        <Line text={p.quote} o={qo} size={portrait ? PSANS : 44} font={SANS} color={SOFT} style={{ marginTop: portrait ? 40 : 40 }} />
        <Line text="→ cleaned up, step by step, into a picture" o={rise(t, p.cleanAt)} size={portrait ? PSERIF - 6 : 56} color={ACC_TEXT}
          style={{ marginTop: portrait ? 40 : 50 }} />
      </div>
      <Bug portrait={portrait} />
    </AbsoluteFill>
  );
};
export const MjNoise: React.FC<z.infer<typeof mjNoiseSchema>> = (p) => <NoiseScene p={p} portrait={false} />;
export const MjNoise916: React.FC<z.infer<typeof mjNoiseSchema>> = (p) => <NoiseScene p={p} portrait />;

// ===========================================================================
// MjSteps — schematic: noise → rough shapes → picture; the prompt says what, the noise nudges where.
// ===========================================================================
export const mjStepsSchema = z.object({
  noise: z.string(), picture: z.string(), prompt: z.string(),
  promptAt: z.number(), noiseAt: z.number(), shapesAt: z.number(), diffAt: z.number(), caption: z.string(),
  ...dur,
});
const StepsScene: React.FC<{ p: z.infer<typeof mjStepsSchema>; portrait: boolean }> = ({ p, portrait }) => {
  const t = useT();
  const po = rise(t, p.promptAt), no = rise(t, p.noiseAt), so = rise(t, p.shapesAt), dfo = rise(t, p.diffAt);
  const size = portrait ? 420 : 470;
  const panels = [
    { el: <Pic src={p.noise} size={size} border={no > 0.5 ? ACC_TEXT : BORDER} />, label: 'noise', o: 1 },
    { el: <div style={{ position: 'relative', width: size, height: size }}>
        <Pic src={p.noise} size={size} style={{ position: 'absolute' }} />
        <Pic src={p.picture} size={size} o={0.6} style={{ position: 'absolute', filter: 'blur(14px)' }} /></div>, label: 'rough shapes', o: ghost(so) },
    { el: <Pic src={p.picture} size={size} border={po > 0.5 ? OK : BORDER} />, label: 'picture', o: ghost(so) },
  ];
  const arrow = <div style={{ fontFamily: SERIF, fontSize: portrait ? PSERIF : 80, color: SOFT, alignSelf: 'center' }}>{portrait ? '↓' : '→'}</div>;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: portrait ? PX : SX, right: portrait ? PX : SX, top: portrait ? PY : 60 }}>
        <Line text={`prompt “${p.prompt}” → what it's about`} o={ghost(po)} size={portrait ? PSERIF - 6 : 54} color={po > 0.5 ? OK : INK} />
        <Line text="noise → where things land" o={no} size={portrait ? PSERIF - 6 : 54} color={ACC_TEXT} style={{ marginTop: 8 }} />
      </div>
      <div style={{ position: 'absolute', left: portrait ? PX + 100 : SX, top: portrait ? 420 : 260, display: 'flex',
        flexDirection: portrait ? 'column' : 'row', gap: portrait ? 0 : 30 }}>
        {panels.map((pn, i) => (
          <React.Fragment key={i}>
            {i > 0 && !portrait ? arrow : null}
            <div style={{ opacity: pn.o, display: 'flex', flexDirection: portrait ? 'row' : 'column', alignItems: portrait ? 'center' : 'flex-start',
              gap: portrait ? 30 : 10, marginBottom: portrait ? 26 : 0 }}>
              {portrait ? <div style={{ width: size * 0.7, height: size * 0.7, overflow: 'hidden', borderRadius: 14 }}>
                <div style={{ transform: 'scale(0.7)', transformOrigin: 'top left' }}>{pn.el}</div></div> : pn.el}
              <div style={{ fontFamily: SERIF, fontSize: portrait ? PSERIF - 6 : 54, color: SOFT }}>{pn.label}</div>
            </div>
          </React.Fragment>
        ))}
      </div>
      <div style={{ position: 'absolute', left: portrait ? PX : SX, right: portrait ? PX : SX, top: portrait ? 1400 : 820 }}>
        <Line text="different noise → different picture" o={dfo} size={portrait ? PSERIF - 6 : 58} color={ACC_TEXT} />
        <Line text={p.caption} o={ghost(po)} size={portrait ? PSANS : 44} font={SANS} color={SOFT} style={{ marginTop: portrait ? 24 : 18 }} />
      </div>
      <Bug portrait={portrait} />
    </AbsoluteFill>
  );
};
export const MjSteps: React.FC<z.infer<typeof mjStepsSchema>> = (p) => <StepsScene p={p} portrait={false} />;
export const MjSteps916: React.FC<z.infer<typeof mjStepsSchema>> = (p) => <StepsScene p={p} portrait />;

// ===========================================================================
// MjFour — four starting noises → four pictures; no seed = new random noise every time.
// ===========================================================================
export const mjFourSchema = z.object({
  noises: z.array(z.string()), images: z.array(z.string()),
  fourAt: z.number(), eachAt: z.number(), randomAt: z.number(), label: z.string(), randomLabel: z.string(),
  ...dur,
});
const FourScene: React.FC<{ p: z.infer<typeof mjFourSchema>; portrait: boolean }> = ({ p, portrait }) => {
  const t = useT();
  const fo = rise(t, p.fourAt), eo = rise(t, p.eachAt), ro = rise(t, p.randomAt);
  const size = portrait ? 260 : 330;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: portrait ? PX : SX + 40, top: portrait ? PY : 70, display: 'flex', flexDirection: portrait ? 'column' : 'row',
        gap: portrait ? 26 : 70 }}>
        {p.noises.map((n, i) => (
          <div key={i} style={{ display: 'flex', flexDirection: portrait ? 'row' : 'column', alignItems: 'center', gap: portrait ? 30 : 16 }}>
            <Pic src={n} size={size} o={ghost(fo)} />
            <div style={{ fontFamily: SERIF, fontSize: portrait ? PSERIF : 64, color: SOFT, opacity: eo }}>{portrait ? '→' : '↓'}</div>
            <Pic src={p.images[i]} size={size} o={eo} />
          </div>
        ))}
      </div>
      <div style={{ position: 'absolute', left: portrait ? PX : SX + 40, right: portrait ? PX : SX, top: portrait ? 1300 : 860 }}>
        <Line text={p.label} o={eo} size={portrait ? PSERIF - 6 : 58} color={ACC_TEXT} />
        <Line text={p.randomLabel} o={ro} size={portrait ? PSERIF - 6 : 54} style={{ marginTop: portrait ? 30 : 10 }} />
      </div>
      <Bug portrait={portrait} />
    </AbsoluteFill>
  );
};
export const MjFour: React.FC<z.infer<typeof mjFourSchema>> = (p) => <FourScene p={p} portrait={false} />;
export const MjFour916: React.FC<z.infer<typeof mjFourSchema>> = (p) => <FourScene p={p} portrait />;

// ===========================================================================
// MjSeed — the seed is the number that picks the noise; --seed locks it.
// ===========================================================================
export const mjSeedSchema = z.object({
  seed: z.number(), prompt: z.string(), noise: z.string(), range: z.string(),
  seedAt: z.number(), rangeAt: z.number(), flagAt: z.number(), lockAt: z.number(),
  ...dur,
});
const SeedScene: React.FC<{ p: z.infer<typeof mjSeedSchema>; portrait: boolean }> = ({ p, portrait }) => {
  const t = useT();
  const so = rise(t, p.seedAt), ro = rise(t, p.rangeAt), fo = rise(t, p.flagAt), lo = rise(t, p.lockAt);
  const size = portrait ? 430 : 480;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: portrait ? PX : SX + 20, top: portrait ? PY + 40 : 120, display: 'flex',
        flexDirection: portrait ? 'column' : 'row', alignItems: portrait ? 'flex-start' : 'center', gap: portrait ? 30 : 50 }}>
        <div style={{ border: `5px solid ${ACC_TEXT}`, borderRadius: 24, padding: portrait ? '24px 40px' : '26px 44px', background: CARD, opacity: ghost(so) }}>
          <div style={{ fontFamily: SANS, fontSize: portrait ? PSANS : 44, color: SOFT }}>seed</div>
          <div style={{ fontFamily: MONO, fontSize: portrait ? 150 : 140, color: ACC_TEXT, lineHeight: 1.05 }}>{p.seed}</div>
        </div>
        <div style={{ fontFamily: SERIF, fontSize: portrait ? PSERIF : 90, color: SOFT, opacity: ghost(so) }}>{portrait ? '↓ picks' : '→'}</div>
        <div style={{ position: 'relative' }}>
          <Pic src={p.noise} size={size} o={ghost(so)} border={lo > 0.5 ? ACC_TEXT : BORDER} />
          <div style={{ marginTop: 16, display: 'inline-block', background: ACC_TEXT, color: CARD, borderRadius: 14, padding: '8px 22px',
            fontFamily: SERIF, fontSize: portrait ? PSERIF - 6 : 54, opacity: lo }}>🔒 starting noise locked</div>
        </div>
      </div>
      <div style={{ position: 'absolute', left: portrait ? PX : SX + 20, right: portrait ? PX : SX, top: portrait ? 1250 : 740 }}>
        <Line text={portrait ? p.range.replace(' from ', ':\n') : p.range} o={ro} size={portrait ? PSERIF - 6 : 54} style={{ whiteSpace: 'pre-line', lineHeight: portrait ? 1.35 : 1.12 }} />
        <div style={{ marginTop: portrait ? 40 : 30, opacity: ghost(fo) }}>
          <PromptBar text={p.prompt} flag={portrait ? undefined : `--seed ${p.seed}`} flagO={fo} o={1} size={portrait ? PSERIF - 6 : 54} portrait={portrait} />
          {portrait ? <div style={{ fontFamily: MONO, fontSize: PSANS + 8, color: ACC_TEXT, opacity: fo, marginTop: 24 }}>+ --seed {p.seed}</div> : null}
        </div>
      </div>
      <Bug portrait={portrait} />
    </AbsoluteFill>
  );
};
export const MjSeed: React.FC<z.infer<typeof mjSeedSchema>> = (p) => <SeedScene p={p} portrait={false} />;
export const MjSeed916: React.FC<z.infer<typeof mjSeedSchema>> = (p) => <SeedScene p={p} portrait />;

// ===========================================================================
// MjDemo — real toy results: four random seeds; seed 1234 twice (identical); one word changed.
// ===========================================================================
export const mjDemoSchema = z.object({
  four: z.array(z.string()), a: z.string(), b: z.string(), forest: z.string(), prompt: z.string(), prompt2: z.string(),
  toyAt: z.number(), fourAt: z.number(), sameAt: z.number(), matchAt: z.number(), wordAt: z.number(), stayAt: z.number(),
  identical: z.boolean(), toyLabel: z.string(),
  ...dur,
});
const DemoScene: React.FC<{ p: z.infer<typeof mjDemoSchema>; portrait: boolean }> = ({ p, portrait }) => {
  const t = useT();
  const to = rise(t, p.toyAt), fo = rise(t, p.fourAt), so = rise(t, p.sameAt), mo = rise(t, p.matchAt);
  const wo = rise(t, p.wordAt), sto = rise(t, p.stayAt);
  const head = (text: string, o: number) => (
    <div style={{ fontFamily: SERIF, fontSize: portrait ? PSERIF - 6 : 54, color: INK, opacity: ghost(o), marginBottom: 14 }}>{text}</div>
  );
  const note = (text: string, o: number, color: string) => (
    <div style={{ fontFamily: SERIF, fontSize: portrait ? PSERIF - 6 : 54, color, opacity: o, marginTop: 12, lineHeight: 1.1 }}>{text}</div>
  );
  if (portrait) {
    const s = 220;
    return (
      <AbsoluteFill style={{ background: BG }}>
        <div style={{ position: 'absolute', left: PX, right: PX, top: PY, fontFamily: SANS, fontSize: PSANS, color: SOFT, opacity: ghost(to) }}>toy, not Midjourney</div>
        <div style={{ position: 'absolute', left: PX, top: PY + 120 }}>
          {head('no seed', fo)}
          <div style={{ display: 'flex', gap: 16 }}>{p.four.map((f, i) => <Pic key={i} src={f} size={s} o={ghost(fo)} />)}</div>
        </div>
        <div style={{ position: 'absolute', left: PX, top: PY + 520 }}>
          {head('seed 1234, twice', so)}
          <div style={{ display: 'flex', gap: 16, alignItems: 'center' }}>
            <Pic src={p.a} size={s * 1.3} o={ghost(so)} />
            <div style={{ fontFamily: SERIF, fontSize: PSERIF, color: OK, opacity: mo }}>=</div>
            <Pic src={p.b} size={s * 1.3} o={ghost(so)} border={mo > 0.5 ? OK : BORDER} />
          </div>
          {note(p.identical ? '0 pixels different' : '', mo, OK)}
        </div>
        <div style={{ position: 'absolute', left: PX, top: PY + 1110 }}>
          {head('seed 1234, sunset → forest', wo)}
          <div style={{ display: 'flex', gap: 16, alignItems: 'center' }}>
            <Pic src={p.a} size={s * 1.3} o={ghost(wo)} />
            <div style={{ fontFamily: SERIF, fontSize: PSERIF, color: SOFT, opacity: ghost(wo) }}>→</div>
            <Pic src={p.forest} size={s * 1.3} o={ghost(wo)} />
          </div>
          {note('same hills, new colours', sto, ACC_TEXT)}
        </div>
        <PBug />
      </AbsoluteFill>
    );
  }
  const s = 250;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: SX, top: 56, fontFamily: SANS, fontSize: 44, color: SOFT, opacity: ghost(to) }}>{p.toyLabel}</div>
      <div style={{ position: 'absolute', left: SX, top: 140 }}>
        {head('no seed: 4 random seeds', fo)}
        <div style={{ display: 'grid', gridTemplateColumns: `repeat(2, ${s}px)`, gap: 16 }}>{p.four.map((f, i) => <Pic key={i} src={f} size={s} o={ghost(fo)} />)}</div>
      </div>
      <div style={{ position: 'absolute', left: SX + 620, top: 140 }}>
        {head('seed 1234, twice', so)}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
          <Pic src={p.a} size={s} o={ghost(so)} />
          <Pic src={p.b} size={s} o={ghost(so)} border={mo > 0.5 ? OK : BORDER} />
        </div>
        {note(p.identical ? '= 0 pixels different' : '', mo, OK)}
      </div>
      <div style={{ position: 'absolute', left: SX + 1130, top: 140 }}>
        {head('seed 1234, one word changed', wo)}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
          <Pic src={p.a} size={s} o={ghost(wo)} />
          <Pic src={p.forest} size={s} o={ghost(wo)} border={sto > 0.5 ? ACC_TEXT : BORDER} />
        </div>
        {note('“sunset” → “forest”: same hills, new colours', sto, ACC_TEXT)}
      </div>
      <HaiBug />
    </AbsoluteFill>
  );
};
export const MjDemo: React.FC<z.infer<typeof mjDemoSchema>> = (p) => <DemoScene p={p} portrait={false} />;
export const MjDemo916: React.FC<z.infer<typeof mjDemoSchema>> = (p) => <DemoScene p={p} portrait />;

// ===========================================================================
// MjInMidjourney — what Midjourney says: same seed + same prompt → almost the same image; find a seed.
// ===========================================================================
export const mjInMjSchema = z.object({
  same: z.string(), pct: z.string(), find: z.string(), sameAt: z.number(), pctAt: z.number(), findAt: z.number(),
  stepAt: z.array(z.number()).default([]),
  ...dur,
});
const InMjScene: React.FC<{ p: z.infer<typeof mjInMjSchema>; portrait: boolean }> = ({ p, portrait }) => {
  const t = useT();
  const so = rise(t, p.sameAt), po = rise(t, p.pctAt), fo = rise(t, p.findAt);
  const steps = p.find.replace(/^find a seed:\s*/, '').split('→').map((x) => x.trim());
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: portrait ? PX : SX, top: portrait ? PY : 70, display: 'flex', alignItems: 'center', gap: 26 }}>
        <MjLogo h={portrait ? 170 : 100} />
        <div style={{ fontFamily: SERIF, fontSize: portrait ? PSERIF : 64, color: INK }}>In Midjourney</div>
      </div>
      <div style={{ position: 'absolute', left: portrait ? PX : SX, right: portrait ? PX : SX, top: portrait ? 330 : 230 }}>
        <Line text={portrait ? p.same.replace(' → ', ' gives ') : p.same} o={ghost(so)} size={portrait ? PSERIF : 64} color={so > 0.5 ? INK : SOFT} />
        <Line text={p.pct} o={po} size={portrait ? PSANS + 10 : 44} font={SANS} color={SOFT} style={{ marginTop: portrait ? 30 : 22 }} />
      </div>
      <div style={{ position: 'absolute', left: portrait ? PX : SX, right: portrait ? PX : SX, top: portrait ? 900 : 560, opacity: fo }}>
        <div style={{ fontFamily: SERIF, fontSize: portrait ? PSERIF + 4 : 54, color: ACC_TEXT, marginBottom: 24 }}>find a seed</div>
        <div style={{ display: 'flex', flexDirection: portrait ? 'column' : 'row', gap: portrait ? 18 : 22, alignItems: portrait ? 'flex-start' : 'center' }}>
          {steps.map((s, i) => (
            <React.Fragment key={i}>
              {i > 0 && !portrait ? <span style={{ fontFamily: SERIF, fontSize: 54, color: SOFT, opacity: rise(t, p.stepAt[i] ?? p.findAt) }}>→</span> : null}
              <span style={{ opacity: rise(t, p.stepAt[i] ?? p.findAt), background: CARD, border: `3px solid ${BORDER}`, borderRadius: 16, padding: portrait ? '14px 30px' : '12px 28px',
                fontFamily: SERIF, fontSize: portrait ? PSERIF + 4 : 54, color: INK }}>{portrait ? `${i + 1}. ${s}` : s}</span>
            </React.Fragment>
          ))}
        </div>
      </div>
      <Bug portrait={portrait} />
    </AbsoluteFill>
  );
};
export const MjInMidjourney: React.FC<z.infer<typeof mjInMjSchema>> = (p) => <InMjScene p={p} portrait={false} />;
export const MjInMidjourney916: React.FC<z.infer<typeof mjInMjSchema>> = (p) => <InMjScene p={p} portrait />;

// ===========================================================================
// MjYourTurn — the your-turn prompt shown whole (no self-running typing); the three
// runs appear as Bella names them; then "what stays, what moves?".
// ===========================================================================
export const mjYourTurnSchema = z.object({
  prompt: z.string(), steps: z.array(z.object({ text: z.string(), at: z.number() })),
  askAt: z.number(), runAt: z.number(), runText: z.string(),
  ...dur,
});
const YourTurnScene: React.FC<{ p: z.infer<typeof mjYourTurnSchema>; portrait: boolean }> = ({ p, portrait }) => {
  const t = useT();
  const ao = rise(t, p.askAt), ro = rise(t, p.runAt);
  const card = (
    <div style={{ background: CARD, border: `3px solid ${ao > 0.5 ? ACC_TEXT : BORDER}`, borderRadius: 24, padding: portrait ? '30px 36px' : '34px 40px',
      fontFamily: SANS, fontSize: portrait ? PSANS : 40, lineHeight: 1.3, color: INK, opacity: ghost(ao), boxSizing: 'border-box' }}>
      <div style={{ fontSize: portrait ? PSANS : 34, color: SOFT, marginBottom: portrait ? 14 : 12 }}>paste into Claude</div>
      {p.prompt}
    </div>
  );
  const steps = (
    <div>
      {p.steps.map((st, i) => (
        <Line key={i} text={`${i + 1}. ${st.text}`} o={rise(t, st.at)} size={portrait ? PSERIF - 6 : 58} style={{ marginBottom: portrait ? 18 : 16 }} />
      ))}
      <Line text={p.runText} o={ro} size={portrait ? PSERIF - 6 : 58} color={ACC_TEXT} style={{ marginTop: portrait ? 24 : 24 }} />
    </div>
  );
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: portrait ? PX : SX, top: portrait ? PY + 20 : 80, display: 'flex', alignItems: 'center', gap: 24 }}>
        <Img src={staticFile('logos/claude/claude-01.svg')} style={{ height: portrait ? 110 : 90, width: portrait ? 110 : 90 }} />
        <div style={{ fontFamily: SERIF, fontSize: portrait ? PSERIF + 20 : 84, color: INK }}>Your turn.</div>
      </div>
      {portrait ? (
        <>
          <div style={{ position: 'absolute', left: PX, right: PX, top: 290 }}>{card}</div>
          <div style={{ position: 'absolute', left: PX, right: PX, top: 1180 }}>{steps}</div>
        </>
      ) : (
        <>
          <div style={{ position: 'absolute', left: SX, width: 860, top: 230 }}>{steps}</div>
          <div style={{ position: 'absolute', left: SX + 920, right: SX, top: 230 }}>{card}</div>
        </>
      )}
      <Bug portrait={portrait} />
    </AbsoluteFill>
  );
};
export const MjYourTurn: React.FC<z.infer<typeof mjYourTurnSchema>> = (p) => <YourTurnScene p={p} portrait={false} />;
export const MjYourTurn916: React.FC<z.infer<typeof mjYourTurnSchema>> = (p) => <YourTurnScene p={p} portrait />;
