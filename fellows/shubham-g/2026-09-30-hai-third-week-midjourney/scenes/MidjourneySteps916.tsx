import React from 'react';
import {AbsoluteFill} from 'remotion';
import {CLAUDE} from '../tokens/claude';
import {SAFE916} from '../tokens/layout';
import {ACCENT, Card, INK, SANS, SERIF, SOFT, STAGE, Spark, useBeat} from './SocialAiVisibility';
import {LogoBug} from './ContentRepurpose';
import {Check} from './OneIntoTen';
import {
  Frame, FourGridProps, LoupeFrame, PostCheckProps, PromptAnatomyProps, RefineLoopProps, ScenePic, UpscaleToUseProps,
  WordSwap, resolveAt,
} from './MidjourneySteps';

/**
 * MidjourneySteps916.tsx — native 9:16 layouts for the MidjourneySteps scenes.
 *
 * Registered as `<Name>916` with the same zod schemas. One column, fewer words per
 * frame; type clears GATE T's portrait floor (serif ≥ 92, sans ≥ 78). Long copy is
 * shortened through the vertical beat sheet's props, never by shrinking type.
 * Every picture is still <ScenePic> — an illustration, never Midjourney output.
 */

const S = SAFE916;
const SERIF_PX = 92;
const SANS_PX = 78;
const TOP = S.y + 260;

const SparkLine916: React.FC<{text: string}> = ({text}) => (
  <div style={{position: 'absolute', left: S.x, top: S.y, width: S.w, height: 230, display: 'flex',
    alignItems: 'center', justifyContent: 'center', gap: 26}}>
    <Spark size={78} />
    <span style={{fontFamily: SERIF, fontSize: SERIF_PX, color: INK, fontWeight: 600, lineHeight: 1.05,
      textAlign: 'center', maxWidth: S.w - 110}}>{text}</span>
  </div>
);

const Text916: React.FC<{text: string; top: number; size?: number; font?: string; color?: string; weight?: number;
  italic?: boolean; align?: 'left' | 'center'; opacity?: number}> = (
  {text, top, size = SERIF_PX, font = SERIF, color = INK, weight = 400, italic = false, align = 'center', opacity = 1}) => (
  <div style={{position: 'absolute', left: S.x, width: S.w, top, fontFamily: font, fontSize: size, color, fontWeight: weight,
    fontStyle: italic ? 'italic' : 'normal', textAlign: align, lineHeight: 1.05, opacity}}>{text}</div>
);

// ── B02 ──────────────────────────────────────────────────────────────────────
export const PromptAnatomy916: React.FC<PromptAnatomyProps> = (props) => {
  const {pop} = useBeat(props.durationSeconds);
  const gap = 24, cw = (S.w - gap) / 2, ch = 150;
  const barTop = TOP + 2 * ch + gap + 44;
  const barIn = pop(props.barAt), pIn = pop(props.paramAt), shIn = pop(props.shapesAt);
  const shapeH = 230;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      {props.parts.map((pt, i) => {
        const t = pop(pt.at);
        return (
          <Card key={i} style={{position: 'absolute', left: S.x + (i % 2) * (cw + gap), top: TOP + Math.floor(i / 2) * (ch + gap),
            width: cw, height: ch, boxSizing: 'border-box', display: 'flex', alignItems: 'center', gap: 22, padding: '0 28px',
            opacity: 0.45 + 0.55 * t, background: t > 0.5 ? CLAUDE.CARD : CLAUDE.FOOTER}}>
            <span style={{fontFamily: SANS, fontSize: SANS_PX, fontWeight: 700, color: SOFT, lineHeight: 1}}>{i + 1}</span>
            <span style={{fontFamily: SERIF, fontSize: SERIF_PX, fontWeight: 700, color: INK, lineHeight: 1}}>{pt.label}</span>
          </Card>
        );
      })}
      <div style={{position: 'absolute', left: S.x, top: barTop, width: S.w, height: 560, borderRadius: 30, background: CLAUDE.CARD,
        border: `2px solid ${CLAUDE.BORDER}`, boxSizing: 'border-box', padding: '26px 30px', opacity: barIn}}>
        <div style={{display: 'flex', flexWrap: 'wrap', gap: '18px 16px'}}>
          {props.parts.map((pt, i) => {
            const t = pop(pt.at + 0.02);
            return (
              <span key={i} style={{fontFamily: SERIF, fontSize: SERIF_PX, color: INK, padding: '0 18px', borderRadius: 16, lineHeight: 1.1,
                background: CLAUDE.FOOTER, border: `2px solid ${CLAUDE.BORDER}`, opacity: t, whiteSpace: 'nowrap'}}>{pt.value}</span>
            );
          })}
          <span style={{fontFamily: SANS, fontSize: SANS_PX, fontWeight: 700, color: INK, padding: '6px 18px', borderRadius: 16,
            border: `5px solid ${ACCENT}`, background: CLAUDE.CARD, opacity: pIn, whiteSpace: 'nowrap'}}>{props.param}</span>
        </div>
      </div>
      <div style={{position: 'absolute', left: S.x, top: barTop + 600, width: S.w, display: 'flex', justifyContent: 'center',
        alignItems: 'flex-end', gap: 56}}>
        {props.shapes.map((sh, i) => {
          const active = i === props.activeShape;
          const w = (shapeH * sh.w) / sh.h;
          return (
            <div key={i} style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 14,
              opacity: active ? pop(props.paramAt + 0.04) : 0.45 * shIn}}>
              {active
                ? <div style={{borderRadius: 14, border: `4px solid ${INK}`, overflow: 'hidden'}}><ScenePic w={w} h={shapeH} radius={0} /></div>
                : <div style={{width: w, height: shapeH, borderRadius: 14, border: `4px dashed ${SOFT}`, boxSizing: 'border-box'}} />}
              <div style={{fontFamily: SANS, fontSize: SANS_PX, fontWeight: 700, color: INK, whiteSpace: 'nowrap', lineHeight: 1}}>{sh.label}</div>
            </div>
          );
        })}
      </div>
      <LogoBug portrait />
    </AbsoluteFill>
  );
};

// ── B04 ──────────────────────────────────────────────────────────────────────
export const FourGrid916: React.FC<FourGridProps> = (props) => {
  const {pop, ramp} = useBeat(props.durationSeconds);
  const bIn = pop(props.barAt), aIn = pop(props.altAt), plIn = pop(props.planAt), pIn = pop(props.pickAt);
  const gap = 24, fw = (S.w - gap) / 2, fh = (fw * 9) / 16;
  const gy = TOP + 620;
  const px = S.x + (props.pickIndex % 2) * (fw + gap), py = gy + Math.floor(props.pickIndex / 2) * (fh + gap);
  const below = gy + 2 * fh + gap;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      <Card style={{position: 'absolute', left: S.x, top: TOP, width: S.w, height: 370, boxSizing: 'border-box', padding: '26px 32px',
        opacity: bIn}}>
        <div style={{fontFamily: SANS, fontSize: SANS_PX, fontWeight: 700, color: SOFT, lineHeight: 1}}>{props.barLabel}</div>
        <div style={{fontFamily: SERIF, fontSize: SERIF_PX, color: INK, lineHeight: 1.06, marginTop: 22}}>{props.prompt}</div>
      </Card>
      <Text916 text={props.altLabel} top={TOP + 410} size={SANS_PX} font={SANS} weight={700} align="left" opacity={aIn} />
      <Text916 text={props.planLabel} top={TOP + 506} size={SANS_PX} font={SANS} italic color={SOFT} align="left" opacity={plIn} />
      {[0, 1, 2, 3].map((i) => {
        const t = ramp(resolveAt(props, i), 0.07);
        return <Frame key={i} n={i + 1} nPx={SANS_PX * 0.7} left={S.x + (i % 2) * (fw + gap)} top={gy + Math.floor(i / 2) * (fh + gap)}
          w={fw} h={fh} variant={i} opacity={Math.min(1, t * 2.5)} blur={(1 - t) * 16} />;
      })}
      <div style={{position: 'absolute', left: px - 14, top: py - 14, width: fw + 28, height: fh + 28, borderRadius: 26,
        border: `8px solid ${ACCENT}`, boxSizing: 'border-box', opacity: pIn}} />
      <Text916 text={props.gridLabel} top={below + 30} size={SANS_PX} font={SANS} weight={700} color={SOFT}
        opacity={pop(resolveAt(props, 3) + 0.04)} />
      <Text916 text={props.pickLine} top={below + 130} weight={700} opacity={pIn} />
      <Text916 text={props.caption} top={S.b - 90} size={SANS_PX} font={SANS} color={SOFT} align="left" opacity={pop(props.gridAt)} />
      <LogoBug portrait />
    </AbsoluteFill>
  );
};

// ── B05 ──────────────────────────────────────────────────────────────────────
export const RefineLoop916: React.FC<RefineLoopProps> = (props) => {
  const {pop, ramp} = useBeat(props.durationSeconds);
  const bigW = 700, bigH = (bigW * 9) / 16;
  const gap = 24, fw = (S.w - gap) / 2, fh = (fw * 9) / 16;
  const rowY = TOP + bigH + 90;
  const sIn = pop(props.subtleAt), stIn = pop(props.strongAt), prIn = pop(props.promptAt);
  const cardTop = rowY + fh + 190;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      <Frame left={S.x + (S.w - bigW) / 2} top={TOP} w={bigW} h={bigH} variant={props.pickVariant} opacity={pop(props.pickAt)}
        border={`5px solid ${INK}`} />
      <Frame left={S.x} top={rowY} w={fw} h={fh} variant={props.pickVariant} glow={1.35} opacity={sIn} />
      <Frame left={S.x + fw + gap} top={rowY} w={fw} h={fh} variant={(props.pickVariant + 1) % 4} awning opacity={stIn} />
      <div style={{position: 'absolute', left: S.x, width: fw, top: rowY + fh + 22, textAlign: 'center', fontFamily: SANS,
        fontSize: SANS_PX, fontWeight: 700, color: INK, opacity: sIn, lineHeight: 1}}>{props.subtleLabel}</div>
      <div style={{position: 'absolute', left: S.x + fw + gap, width: fw, top: rowY + fh + 22, textAlign: 'center', fontFamily: SANS,
        fontSize: SANS_PX, fontWeight: 700, color: INK, opacity: stIn, lineHeight: 1}}>{props.strongLabel}</div>
      <Card style={{position: 'absolute', left: S.x, top: cardTop, width: S.w, height: 250, boxSizing: 'border-box', padding: '24px 34px',
        opacity: prIn}}>
        <div style={{fontFamily: SANS, fontSize: SANS_PX, fontWeight: 700, color: SOFT, lineHeight: 1}}>{props.promptLabel}</div>
        <div style={{marginTop: 34}}><WordSwap props={props} px={SERIF_PX} ramp={ramp} /></div>
      </Card>
      <Text916 text={props.line} top={cardTop + 290} weight={700} opacity={pop(props.lineAt)} />
      <LogoBug portrait />
    </AbsoluteFill>
  );
};

// ── B06 ──────────────────────────────────────────────────────────────────────
export const UpscaleToUse916: React.FC<UpscaleToUseProps> = (props) => {
  const {pop, ramp} = useBeat(props.durationSeconds);
  const g = ramp(props.growAt, 0.1), ge = g * g * (3 - 2 * g);
  const bigW = S.w, bigH = (bigW * 9) / 16;
  const k = 0.45 + 0.55 * ge;
  const arIn = ramp(props.arAt, 0.06);
  const optTop = TOP + bigH + 40;
  const rowH = 270, rowTop = optTop + 2 * 124 + 60;
  const fws = props.formats.map((f) => (rowH * f.w) / f.h);
  const rowGap = 30;
  let fx = S.x + (S.w - (fws.reduce((a, b) => a + b, 0) + rowGap * (fws.length - 1))) / 2;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      <div style={{position: 'absolute', left: S.x + (bigW - bigW * k) / 2, top: TOP, width: bigW * k, height: bigH * k, borderRadius: 18,
        overflow: 'hidden', border: `5px solid ${INK}`}}>
        <ScenePic w={bigW * k} h={bigH * k} variant={props.pickVariant} radius={0} />
      </div>
      {props.options.map((o, i) => (
        <Text916 key={i} text={o.label} top={optTop + i * 124} size={SANS_PX} font={SANS} weight={700} align="left" opacity={pop(o.at)} />
      ))}
      {props.formats.map((f, i) => {
        const w = fws[i];
        const x = fx;
        fx += w + rowGap;
        const t = pop(f.at);
        return (
          <div key={i} style={{position: 'absolute', left: x, top: rowTop, width: w, opacity: t}}>
            <div style={{borderRadius: 14, overflow: 'hidden', border: `3px solid ${CLAUDE.BORDER}`}}>
              <ScenePic w={w} h={rowH} variant={props.pickVariant} radius={0} />
            </div>
            <div style={{position: 'absolute', left: -60, right: -60, top: rowH + 16, textAlign: 'center', fontFamily: SANS,
              fontSize: SANS_PX, fontWeight: 700, color: INK, whiteSpace: 'nowrap', lineHeight: 1}}>
              <span style={{position: 'relative'}}>
                {f.ar}
                <span style={{position: 'absolute', left: 0, right: 0, bottom: -14, height: 9, borderRadius: 5, background: ACCENT,
                  transform: `scaleX(${arIn})`, transformOrigin: 'left'}} />
              </span>
            </div>
          </div>
        );
      })}
      <Text916 text={props.tip} top={rowTop + rowH + 140} weight={700} opacity={pop(props.tipAt)} />
      <LogoBug portrait />
    </AbsoluteFill>
  );
};

// ── B07 ──────────────────────────────────────────────────────────────────────
export const PostCheck916: React.FC<PostCheckProps> = (props) => {
  const {pop} = useBeat(props.durationSeconds);
  const fw = S.w, fh = (fw * 9) / 16;
  const listTop = TOP + fh + 170;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine916 text={props.sparkLine} />
      <LoupeFrame left={S.x} top={TOP} fw={fw} variant={props.pickVariant} loupe={pop(props.loupeAt)} r={150} />
      <Text916 text={props.caption} top={TOP + fh + 40} size={SANS_PX} font={SANS} color={SOFT} align="left" opacity={pop(0.01)} />
      {props.checks.map((c, i) => {
        const t = pop(c.at);
        return (
          <div key={i} style={{position: 'absolute', left: S.x, top: listTop + i * 170, width: S.w, height: 150, display: 'flex',
            alignItems: 'center', gap: 30, opacity: 0.45 + 0.55 * t}}>
            <div style={{width: 110, height: 110, flexShrink: 0, borderRadius: 24, border: `3px solid ${CLAUDE.BORDER}`,
              background: CLAUDE.CARD, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
              <div style={{opacity: t}}><Check size={84} /></div>
            </div>
            <span style={{fontFamily: SERIF, fontSize: SERIF_PX, fontWeight: 700, color: INK, lineHeight: 1, whiteSpace: 'nowrap'}}>{c.label}</span>
          </div>
        );
      })}
      <LogoBug portrait />
    </AbsoluteFill>
  );
};
