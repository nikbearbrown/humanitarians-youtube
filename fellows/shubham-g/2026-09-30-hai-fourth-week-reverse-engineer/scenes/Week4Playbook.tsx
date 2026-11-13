import React from 'react';
import {AbsoluteFill} from 'remotion';
import {z} from 'zod';
import {CLAUDE} from '../tokens/claude';
import {ACCENT, Card, INK, SANS, SERIF, SOFT, STAGE, useBeat} from './SocialAiVisibility';
import {LogoBug} from './ContentRepurpose';
import {Check} from './OneIntoTen';
import {Caption, SparkLine, ty} from './ContentPerformance';

/**
 * Week4Playbook.tsx — concept illustrations (C3) for the ai-explainer reel
 * "Week 4 Learning: Build It, Then Reverse Engineer It" (@Shubh & @HumanitariansAI).
 *
 * Seven scenes: build forward / save backward (framework) → the decision log → the
 * template (fixed spine, open slots) → the six-step playbook → fix → rule → the gains
 * (speed, efficiency, consistency) → the limits (a starting point, not a cage).
 *
 * Dual-aspect: every scene reads useVideoConfig() and lays out natively for 1920×1080
 * (SAFE) or 1080×1920 (SAFE916); Root.tsx registers `<Name>` and `<Name>916`. Portrait
 * type clears GATE T's floor (serif ≥ 92, sans ≥ 78) — shorter copy comes through the
 * vertical sheet's props. Checker lessons baked in: no accent-bordered text chips (accent
 * lives in bars / underlines / arrows), no number discs, hairline borders in portrait.
 *
 * HONESTY: the decisions and fixes shown are the real ones from this series' builds; the
 * time comparison in ThreeGains is illustrative (no axis, no numbers). One accent per beat.
 */

const dur = {durationSeconds: z.number().default(14)};
const clamp01 = (v: number) => Math.min(1, Math.max(0, v));

/** A card with an optional accent bar along its top edge (the house-safe accent). */
const BarCard: React.FC<{style: React.CSSProperties; bar?: number; children?: React.ReactNode}> = ({style, bar = 0, children}) => (
  <Card style={{...style, position: 'absolute', boxSizing: 'border-box', overflow: 'hidden'}}>
    {bar > 0 && <div style={{position: 'absolute', left: 0, top: 0, height: 14, width: `${bar * 100}%`, background: ACCENT}} />}
    {children}
  </Card>
);

// ─────────────────────────────────────────────────────────────────────────────
// B02 — build forward, then walk it backwards and save each decision
// ─────────────────────────────────────────────────────────────────────────────
export const buildThenReverseSchema = z.object({
  ...dur,
  sparkLine: z.string().default('Build forward. Save backward.'),
  buildLabel: z.string().default('BUILD ONE VIDEO →'),
  reverseLabel: z.string().default('← WALK IT BACKWARDS'),
  stages: z.array(z.object({label: z.string(), saved: z.string(), at: z.number(), savedAt: z.number()})).default([
    {label: 'Idea', saved: 'Brief template', at: 0.29, savedAt: 0.78},
    {label: 'Script', saved: 'Beat-sheet spine', at: 0.33, savedAt: 0.73},
    {label: 'Voice', saved: 'Voice settings', at: 0.37, savedAt: 0.68},
    {label: 'Visuals', saved: 'Scene library', at: 0.4, savedAt: 0.63},
    {label: 'Render', saved: 'Export checklist', at: 0.46, savedAt: 0.58},
  ]),
  reverseAt: z.number().default(0.54),
  line: z.string().default('Decide once. Save it for the next editor.'),
  lineAt: z.number().default(0.87),
});
export type BuildThenReverseProps = z.infer<typeof buildThenReverseSchema>;

export const BuildThenReverse: React.FC<BuildThenReverseProps> = (props) => {
  const {portrait, S, pop, ramp, width, height} = useBeat(props.durationSeconds);
  const T = ty(portrait);
  const n = props.stages.length;
  const rev = ramp(props.reverseAt, 0.3);
  const fwd = ramp(props.stages[0]?.at ?? 0.29, (props.stages[n - 1]?.at ?? 0.46) - (props.stages[0]?.at ?? 0.29) + 0.04);
  if (portrait) {
    const top = S.y + 260 + 100, rowH = 200, gap = 26, colW = (S.w - 70) / 2;
    const rx = S.x + colW + 70;
    return (
      <AbsoluteFill style={{background: STAGE}}>
        <SparkLine text={props.sparkLine} portrait S={S} />
        <div style={{position: 'absolute', left: S.x, top: top - 100, width: colW, fontFamily: SANS, fontSize: T.sans, fontWeight: 700,
          color: SOFT, lineHeight: 1, opacity: pop(props.stages[0]?.at ?? 0.3)}}>{props.buildLabel}</div>
        <div style={{position: 'absolute', left: rx, top: top - 100, width: colW, fontFamily: SANS, fontSize: T.sans, fontWeight: 700,
          color: SOFT, lineHeight: 1, opacity: pop(props.reverseAt)}}>{props.reverseLabel}</div>
        {props.stages.map((s, i) => {
          const y = top + i * (rowH + gap);
          const t = pop(s.at), sv = pop(s.savedAt), arrow = ramp(s.savedAt - 0.03, 0.04);
          return (
            <React.Fragment key={i}>
              <BarCard style={{left: S.x, top: y, width: colW, height: rowH, display: 'flex', alignItems: 'center', justifyContent: 'center',
                opacity: 0.45 + 0.55 * t, border: `3px solid ${CLAUDE.BORDER}`}}>
                <span style={{fontFamily: SERIF, fontSize: T.serif, fontWeight: 700, color: INK, lineHeight: 1}}>{s.label}</span>
              </BarCard>
              <svg width={width} height={height} style={{position: 'absolute', left: 0, top: 0}}>
                <line x1={rx - 8} y1={y + rowH / 2} x2={rx - 8 - 54 * arrow} y2={y + rowH / 2} stroke={ACCENT} strokeWidth={9} strokeLinecap="round" />
              </svg>
              <BarCard style={{left: rx, top: y, width: colW, height: rowH, display: 'flex', alignItems: 'center', justifyContent: 'center',
                opacity: sv, transform: `translateX(${(1 - sv) * 24}px)`, border: `3px solid ${CLAUDE.BORDER}`}}>
                <span style={{fontFamily: SANS, fontSize: T.sans, fontWeight: 700, color: INK, lineHeight: 1.05, textAlign: 'center', padding: '0 16px'}}>{s.saved}</span>
              </BarCard>
            </React.Fragment>
          );
        })}
        <div style={{position: 'absolute', left: S.x, width: S.w, top: top + n * (rowH + gap) + 30, textAlign: 'center', fontFamily: SERIF,
          fontSize: T.serif, fontStyle: 'italic', color: INK, lineHeight: 1.05, opacity: pop(props.lineAt)}}>{props.line}</div>
        <LogoBug portrait />
      </AbsoluteFill>
    );
  }
  const gap = 26, cw = (S.w - gap * (n - 1)) / n;
  const stageY = 250, stageH = 190, savedY = 625, savedH = 190;
  const fwdY = 205, revY = 520;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={false} S={S} />
      <div style={{position: 'absolute', left: S.x, top: 140, fontFamily: SANS, fontSize: T.sans, fontWeight: 700, color: SOFT, lineHeight: 1,
        opacity: pop(props.stages[0]?.at ?? 0.3)}}>{props.buildLabel}</div>
      <svg width={width} height={height} style={{position: 'absolute', left: 0, top: 0}}>
        <line x1={S.x + 480} y1={fwdY - 40} x2={S.x + 480 + (S.w - 500) * fwd} y2={fwdY - 40} stroke={INK} strokeWidth={6} strokeLinecap="round" />
        {rev > 0 && (<>
          <line x1={S.r - 10} y1={revY} x2={S.r - 10 - (S.w - 20) * rev} y2={revY} stroke={ACCENT} strokeWidth={10} strokeLinecap="round" />
          <path d={`M ${S.r - 10 - (S.w - 20) * rev + 26} ${revY - 22} L ${S.r - 10 - (S.w - 20) * rev} ${revY} L ${S.r - 10 - (S.w - 20) * rev + 26} ${revY + 22}`}
            fill="none" stroke={ACCENT} strokeWidth={10} strokeLinecap="round" strokeLinejoin="round" />
        </>)}
      </svg>
      <div style={{position: 'absolute', left: S.x, top: revY + 26, fontFamily: SANS, fontSize: T.sans, fontWeight: 700, color: SOFT, lineHeight: 1,
        opacity: pop(props.reverseAt)}}>{props.reverseLabel}</div>
      {props.stages.map((s, i) => {
        const x = S.x + i * (cw + gap);
        const t = pop(s.at), sv = pop(s.savedAt);
        return (
          <React.Fragment key={i}>
            <BarCard style={{left: x, top: stageY, width: cw, height: stageH, display: 'flex', alignItems: 'center', justifyContent: 'center',
              opacity: 0.45 + 0.55 * t, border: `3px solid ${t > 0.5 ? INK : CLAUDE.BORDER}`}}>
              <span style={{fontFamily: SERIF, fontSize: 62, fontWeight: 700, color: INK, lineHeight: 1}}>{s.label}</span>
            </BarCard>
            <BarCard style={{left: x, top: savedY, width: cw, height: savedH, display: 'flex', alignItems: 'center', justifyContent: 'center',
              opacity: sv, transform: `translateY(${(1 - sv) * -30}px)`}}>
              <span style={{fontFamily: SANS, fontSize: 46, fontWeight: 700, color: INK, lineHeight: 1.1, textAlign: 'center', padding: '0 18px'}}>{s.saved}</span>
            </BarCard>
          </React.Fragment>
        );
      })}
      <div style={{position: 'absolute', left: S.x, width: S.w, top: 850, textAlign: 'center', fontFamily: SERIF, fontSize: 62, fontStyle: 'italic',
        color: INK, lineHeight: 1, opacity: pop(props.lineAt)}}>{props.line}</div>
      <LogoBug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B03 — the decision log: every choice with its reason
// ─────────────────────────────────────────────────────────────────────────────
export const decisionLogSchema = z.object({
  ...dur,
  sparkLine: z.string().default('Log the why.'),
  colA: z.string().default('DECISION'),
  colB: z.string().default('WHY'),
  rows: z.array(z.object({decision: z.string(), why: z.string(), at: z.number()})).default([
    {decision: 'Voice: af_bella', why: 'one steady narrator, every week', at: 0.14},
    {decision: 'A new greeting each week', why: 'a fresh opening for the series', at: 0.22},
    {decision: '@Shubh & @HumanitariansAI', why: 'the brand on every Claude page', at: 0.36},
  ]),
  whyAt: z.number().default(0.66),
  line: z.string().default('The reason lets the next editor make the same call.'),
  lineAt: z.number().default(0.8),
});
export type DecisionLogProps = z.infer<typeof decisionLogSchema>;

export const DecisionLog: React.FC<DecisionLogProps> = (props) => {
  const {portrait, S, pop, ramp} = useBeat(props.durationSeconds);
  const T = ty(portrait);
  const whyIn = ramp(props.whyAt, 0.06);
  if (portrait) {
    const top = S.y + 260, cardH = 330, gap = 36;
    return (
      <AbsoluteFill style={{background: STAGE}}>
        <SparkLine text={props.sparkLine} portrait S={S} />
        {props.rows.map((r, i) => {
          const t = pop(r.at);
          return (
            <BarCard key={i} style={{left: S.x, top: top + i * (cardH + gap), width: S.w, height: cardH, padding: '44px 40px',
              opacity: 0.45 + 0.55 * t, border: `3px solid ${CLAUDE.BORDER}`}}>
              <div style={{fontFamily: SERIF, fontSize: T.serif, fontWeight: 700, color: INK, lineHeight: 1.05}}>{r.decision}</div>
              <div style={{position: 'relative', display: 'inline-block', marginTop: 34, fontFamily: SANS, fontSize: T.sans, fontStyle: 'italic', color: SOFT, lineHeight: 1.05}}>
                {r.why}
                <span style={{position: 'absolute', left: 0, right: 0, bottom: -14, height: 10, borderRadius: 5, background: ACCENT,
                  transform: `scaleX(${whyIn})`, transformOrigin: 'left'}} />
              </div>
            </BarCard>
          );
        })}
        <div style={{position: 'absolute', left: S.x, width: S.w, top: top + props.rows.length * (cardH + gap) + 20, textAlign: 'center',
          fontFamily: SERIF, fontSize: T.serif, fontStyle: 'italic', color: INK, lineHeight: 1.05, opacity: pop(props.lineAt)}}>{props.line}</div>
        <LogoBug portrait />
      </AbsoluteFill>
    );
  }
  const top = 170, headH = 90, rowH = 190;
  const colAW = 830;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={false} S={S} />
      <Card style={{position: 'absolute', left: S.x, top, width: S.w, height: headH + props.rows.length * rowH + 20, boxSizing: 'border-box',
        opacity: pop(0.03)}}>
        <div style={{position: 'absolute', left: 44, top: 32, fontFamily: SANS, fontSize: T.sans, fontWeight: 700, letterSpacing: '0.1em', color: SOFT, lineHeight: 1}}>{props.colA}</div>
        <div style={{position: 'absolute', left: colAW + 44, top: 32, fontFamily: SANS, fontSize: T.sans, fontWeight: 700, letterSpacing: '0.1em', color: SOFT, lineHeight: 1}}>
          {props.colB}
          <div style={{height: 9, borderRadius: 5, marginTop: 10, background: ACCENT, width: 150 * whyIn}} />
        </div>
        {props.rows.map((r, i) => {
          const t = pop(r.at);
          const y = headH + i * rowH;
          return (
            <div key={i} style={{position: 'absolute', left: 0, top: y, width: '100%', height: rowH, borderTop: `2px solid ${CLAUDE.BORDER}`,
              display: 'flex', alignItems: 'center', opacity: 0.45 + 0.55 * t}}>
              <div style={{width: colAW, paddingLeft: 44, boxSizing: 'border-box', fontFamily: SERIF, fontSize: 60, fontWeight: 700, color: INK, lineHeight: 1.05}}>{r.decision}</div>
              <div style={{flex: 1, paddingRight: 44, fontFamily: SERIF, fontSize: 56, fontStyle: 'italic', color: INK, lineHeight: 1.1,
                opacity: clamp01(t * 1.2)}}>{r.why}</div>
            </div>
          );
        })}
      </Card>
      <div style={{position: 'absolute', left: S.x, width: S.w, top: top + headH + props.rows.length * rowH + 70, textAlign: 'center',
        fontFamily: SERIF, fontSize: 60, fontStyle: 'italic', color: INK, lineHeight: 1, opacity: pop(props.lineAt)}}>{props.line}</div>
      <LogoBug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B04 — the template: a fixed spine with open slots
// ─────────────────────────────────────────────────────────────────────────────
export const templateSlotsSchema = z.object({
  ...dur,
  sparkLine: z.string().default('Fixed spine. Open slots.'),
  spineLabel: z.string().default('FIXED — EVERY VIDEO'),
  blocks: z.array(z.object({label: z.string(), at: z.number()})).default([
    {label: 'Cold open', at: 0.29}, {label: 'Summary', at: 0.33}, {label: 'Body', at: 0.37},
    {label: 'Recap', at: 0.39}, {label: 'Your turn', at: 0.43}, {label: 'Outro', at: 0.46},
  ]),
  slotLabel: z.string().default('SLOTS — CHANGE EACH WEEK'),
  slots: z.array(z.object({label: z.string(), value: z.string(), at: z.number()})).default([
    {label: 'TOPIC', value: 'Week 4: the playbook', at: 0.64},
    {label: 'EXAMPLES', value: 'Our own build log', at: 0.68},
    {label: 'PROMPT', value: 'Reverse engineer my video', at: 0.73},
  ]),
  line: z.string().default('Fill the slots — don’t invent the structure.'),
  lineAt: z.number().default(0.84),
});
export type TemplateSlotsProps = z.infer<typeof templateSlotsSchema>;

const Lock: React.FC<{size: number; on: number}> = ({size, on}) => (
  <svg width={size} height={size} viewBox="0 0 100 100" style={{flexShrink: 0, opacity: on}}>
    <path d="M 30 44 V 32 Q 30 12 50 12 Q 70 12 70 32 V 44" fill="none" stroke={SOFT} strokeWidth={10} strokeLinecap="round" />
    <rect x={20} y={44} width={60} height={46} rx={10} fill={SOFT} />
  </svg>
);

export const TemplateSlots: React.FC<TemplateSlotsProps> = (props) => {
  const {portrait, S, pop, ramp} = useBeat(props.durationSeconds);
  const T = ty(portrait);
  const nb = props.blocks.length, ns = props.slots.length;
  const typed = (s: {value: string; at: number}) => s.value.slice(0, Math.round(ramp(s.at, 0.06) * s.value.length));
  if (portrait) {
    const top = S.y + 260 + 90, cols = 2, gap = 18, bw = (S.w - gap) / cols, bh = 130;
    const rows = Math.ceil(nb / cols);
    const slotTop = top + rows * (bh + gap) + 122, slotH = 225;
    return (
      <AbsoluteFill style={{background: STAGE}}>
        <SparkLine text={props.sparkLine} portrait S={S} />
        <div style={{position: 'absolute', left: S.x, top: top - 100, fontFamily: SANS, fontSize: T.sans, fontWeight: 700, color: SOFT, lineHeight: 1,
          opacity: pop(props.blocks[0]?.at ?? 0.3)}}>{props.spineLabel}</div>
        {props.blocks.map((b, i) => {
          const t = pop(b.at);
          return (
            <BarCard key={i} style={{left: S.x + (i % cols) * (bw + gap), top: top + Math.floor(i / cols) * (bh + gap), width: bw, height: bh,
              display: 'flex', alignItems: 'center', justifyContent: 'center', opacity: 0.45 + 0.55 * t, border: `3px solid ${CLAUDE.BORDER}`}}>
              <span style={{fontFamily: SERIF, fontSize: T.serif, fontWeight: 700, color: INK, lineHeight: 1, whiteSpace: 'nowrap'}}>{b.label}</span>
            </BarCard>
          );
        })}
        <div style={{position: 'absolute', left: S.x, top: slotTop - 100, fontFamily: SANS, fontSize: T.sans, fontWeight: 700, color: SOFT, lineHeight: 1,
          opacity: pop(props.slots[0]?.at ?? 0.6)}}>{props.slotLabel}</div>
        {props.slots.map((s, i) => {
          const t = pop(s.at);
          return (
            <BarCard key={i} bar={t} style={{left: S.x, top: slotTop + i * (slotH + 20), width: S.w, height: slotH, padding: '24px 40px',
              opacity: 0.45 + 0.55 * t, border: `3px dashed ${SOFT}`, background: CLAUDE.CARD}}>
              <div style={{fontFamily: SANS, fontSize: T.sans, fontWeight: 700, color: SOFT, lineHeight: 1}}>{s.label}</div>
              <div style={{fontFamily: SERIF, fontSize: T.serif, fontWeight: 700, color: INK, lineHeight: 1.05, marginTop: 16, whiteSpace: 'nowrap'}}>{typed(s)}</div>
            </BarCard>
          );
        })}
        <LogoBug portrait />
      </AbsoluteFill>
    );
  }
  const gap = 20, bw = (S.w - gap * (nb - 1)) / nb, bh = 170, top = 200;
  const sgap = 30, sw = (S.w - sgap * (ns - 1)) / ns, sh = 250, stop = 510;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={false} S={S} />
      <div style={{position: 'absolute', left: S.x, top: 130, fontFamily: SANS, fontSize: T.sans, fontWeight: 700, color: SOFT, lineHeight: 1,
        opacity: pop(props.blocks[0]?.at ?? 0.3)}}>{props.spineLabel}</div>
      {props.blocks.map((b, i) => {
        const t = pop(b.at);
        return (
          <BarCard key={i} style={{left: S.x + i * (bw + gap), top, width: bw, height: bh, display: 'flex', flexDirection: 'column',
            alignItems: 'center', justifyContent: 'center', gap: 14, opacity: 0.45 + 0.55 * t, border: `3px solid ${CLAUDE.BORDER}`,
            background: t > 0.5 ? CLAUDE.CARD : CLAUDE.FOOTER}}>
            <Lock size={46} on={t} />
            <span style={{fontFamily: SERIF, fontSize: 52, fontWeight: 700, color: INK, lineHeight: 1, whiteSpace: 'nowrap'}}>{b.label}</span>
          </BarCard>
        );
      })}
      <div style={{position: 'absolute', left: S.x, top: stop - 70, fontFamily: SANS, fontSize: T.sans, fontWeight: 700, color: SOFT, lineHeight: 1,
        opacity: pop(props.slots[0]?.at ?? 0.6)}}>{props.slotLabel}</div>
      {props.slots.map((s, i) => {
        const t = pop(s.at);
        return (
          <BarCard key={i} bar={t} style={{left: S.x + i * (sw + sgap), top: stop, width: sw, height: sh, padding: '44px 36px',
            opacity: 0.45 + 0.55 * t, border: `3px dashed ${SOFT}`}}>
            <div style={{fontFamily: SANS, fontSize: T.sans, fontWeight: 700, letterSpacing: '0.08em', color: SOFT, lineHeight: 1}}>{s.label}</div>
            <div style={{fontFamily: SERIF, fontSize: 56, fontWeight: 700, color: INK, lineHeight: 1.1, marginTop: 26}}>{typed(s)}</div>
          </BarCard>
        );
      })}
      <div style={{position: 'absolute', left: S.x, width: S.w, top: 850, textAlign: 'center', fontFamily: SERIF, fontSize: 62, fontStyle: 'italic',
        color: INK, lineHeight: 1, opacity: pop(props.lineAt)}}>{props.line}</div>
      <LogoBug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B06 — the six-step playbook, a checklist under every step
// ─────────────────────────────────────────────────────────────────────────────
export const playbookStepsSchema = z.object({
  ...dur,
  sparkLine: z.string().default('Six steps, six checklists.'),
  steps: z.array(z.object({title: z.string(), checks: z.array(z.string()), at: z.number()})).default([
    {title: 'Brief', checks: ['topic + audience', 'length + both aspects'], at: 0.15},
    {title: 'Script', checks: ['the fixed spine', 'one idea per beat'], at: 0.21},
    {title: 'Voice', checks: ['narration first', 'its length sets the timing'], at: 0.24},
    {title: 'Visuals', checks: ['search the library first', 'one accent per beat'], at: 0.3},
    {title: 'Check', checks: ['look at the frames', 'run every gate'], at: 0.33},
    {title: 'Export', checks: ['16:9 and 9:16, in 4K', 'render only — never publish'], at: 0.38},
  ]),
  checksAt: z.number().default(0.44),
  checksSpan: z.number().default(0.2),
  accentIndex: z.number().default(2),
  accentAt: z.number().default(0.73),
});
export type PlaybookStepsProps = z.infer<typeof playbookStepsSchema>;

export const PlaybookSteps: React.FC<PlaybookStepsProps> = (props) => {
  const {portrait, S, pop} = useBeat(props.durationSeconds);
  const T = ty(portrait);
  const n = props.steps.length;
  const acc = pop(props.accentAt);
  const cols = portrait ? 1 : 2;
  const top = portrait ? S.y + 260 : 160;
  const gap = portrait ? 18 : 24;
  const cw = (S.w - gap * (cols - 1)) / cols;
  const rows = Math.ceil(n / cols);
  const ch = portrait ? 205 : (965 - top - gap * (rows - 1)) / rows;
  const perCheck = props.checksSpan / Math.max(1, n * 2 - 1);
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={portrait} S={S} />
      {props.steps.map((s, i) => {
        const c = portrait ? 0 : Math.floor(i / rows), r = portrait ? i : i % rows;
        const t = pop(s.at);
        const checks = s.checks;
        return (
          <BarCard key={i} bar={i === props.accentIndex ? acc : 0} style={{left: S.x + c * (cw + gap), top: top + r * (ch + gap), width: cw, height: ch,
            padding: portrait ? '22px 36px' : '30px 36px', opacity: 0.45 + 0.55 * t, border: portrait ? `3px solid ${CLAUDE.BORDER}` : undefined}}>
            <div style={{fontFamily: SERIF, fontSize: portrait ? T.serif : 60, fontWeight: 700, color: INK, lineHeight: 1}}>
              <span style={{color: SOFT}}>{`${i + 1}. `}</span>{s.title}
            </div>
            <div style={{display: 'flex', flexDirection: portrait ? 'row' : 'column', gap: portrait ? 24 : 14, marginTop: portrait ? 18 : 20}}>
              {checks.map((k, j) => {
                const ct = pop(props.checksAt + (i * 2 + j) * perCheck);
                return (
                  <div key={j} style={{display: 'flex', alignItems: 'center', gap: 12, fontFamily: SANS, fontSize: T.sans, color: INK, lineHeight: 1.1}}>
                    <span style={{opacity: 0.35 + 0.65 * ct}}><Check size={portrait ? 60 : 44} color={ct > 0.5 ? INK : SOFT} /></span>{portrait ? null : k}
                  </div>
                );
              })}
            </div>
          </BarCard>
        );
      })}
      <LogoBug portrait={portrait} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B07 — every fix becomes a rule
// ─────────────────────────────────────────────────────────────────────────────
export const fixToRuleSchema = z.object({
  ...dur,
  sparkLine: z.string().default('Every fix becomes a rule.'),
  fixLabel: z.string().default('THE FIX (ONCE)'),
  ruleLabel: z.string().default('THE RULE (EVERY TIME)'),
  rows: z.array(z.object({fix: z.string(), rule: z.string(), at: z.number(), ruleAt: z.number()})).default([
    {fix: 'Labels too small', rule: 'A minimum label size', at: 0.32, ruleAt: 0.4},
    {fix: 'A chip covered the logo', rule: 'Keep the logo corner clear', at: 0.51, ruleAt: 0.62},
  ]),
  luck: z.string().default('A fix made once is luck.'),
  luckAt: z.number().default(0.74),
  process: z.string().default('A fix written down is process.'),
  processAt: z.number().default(0.87),
});
export type FixToRuleProps = z.infer<typeof fixToRuleSchema>;

export const FixToRule: React.FC<FixToRuleProps> = (props) => {
  const {portrait, S, pop, ramp, width, height} = useBeat(props.durationSeconds);
  const T = ty(portrait);
  const ruleHead = pop(props.rows[0]?.ruleAt ?? 0.4);
  if (portrait) {
    const top = S.y + 260, fixH = 170, ruleH = 190, arrowH = 90, rowGap = 50;
    const rowH = fixH + arrowH + ruleH;
    return (
      <AbsoluteFill style={{background: STAGE}}>
        <SparkLine text={props.sparkLine} portrait S={S} />
        <svg width={width} height={height} style={{position: 'absolute', left: 0, top: 0}}>
          {props.rows.map((r, i) => {
            const y = top + i * (rowH + rowGap) + fixH;
            const a = ramp(r.ruleAt - 0.04, 0.04);
            const cx = S.x + S.w / 2;
            return (
              <g key={i} opacity={a > 0 ? 1 : 0}>
                <line x1={cx} y1={y + 14} x2={cx} y2={y + 14 + (arrowH - 34) * a} stroke={INK} strokeWidth={8} strokeLinecap="round" />
                <path d={`M ${cx - 24} ${y + arrowH - 40} L ${cx} ${y + arrowH - 18} L ${cx + 24} ${y + arrowH - 40}`} fill="none" stroke={INK}
                  strokeWidth={8} strokeLinecap="round" strokeLinejoin="round" opacity={a} />
              </g>
            );
          })}
        </svg>
        {props.rows.map((r, i) => {
          const y = top + i * (rowH + rowGap);
          const f = pop(r.at), ru = pop(r.ruleAt);
          return (
            <React.Fragment key={i}>
              <BarCard style={{left: S.x, top: y, width: S.w, height: fixH, display: 'flex', alignItems: 'center', justifyContent: 'center',
                opacity: 0.45 + 0.55 * f, background: CLAUDE.FOOTER, border: `3px solid ${CLAUDE.BORDER}`}}>
                <span style={{fontFamily: SANS, fontSize: T.sans, fontStyle: 'italic', color: SOFT, lineHeight: 1}}>{r.fix}</span>
              </BarCard>
              <BarCard bar={ru} style={{left: S.x, top: y + fixH + arrowH, width: S.w, height: ruleH, display: 'flex', alignItems: 'center', justifyContent: 'center',
                opacity: ru, border: `3px solid ${CLAUDE.BORDER}`}}>
                <span style={{fontFamily: SERIF, fontSize: T.serif, fontWeight: 700, color: INK, lineHeight: 1}}>{r.rule}</span>
              </BarCard>
            </React.Fragment>
          );
        })}
        <div style={{position: 'absolute', left: S.x, width: S.w, top: top + props.rows.length * (rowH + rowGap) + 10, textAlign: 'center',
          fontFamily: SERIF, fontSize: T.serif, fontStyle: 'italic', color: INK, lineHeight: 1.1}}>
          <div style={{opacity: pop(props.luckAt), color: SOFT}}>{props.luck}</div>
          <div style={{opacity: pop(props.processAt), fontWeight: 700, marginTop: 20}}>{props.process}</div>
        </div>
        <LogoBug portrait />
      </AbsoluteFill>
    );
  }
  const top = 250, rowH = 240, rowGap = 50, fixW = 700, ruleX = S.x + fixW + 220, ruleW = S.r - ruleX;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={false} S={S} />
      <div style={{position: 'absolute', left: S.x, top: 160, fontFamily: SANS, fontSize: T.sans, fontWeight: 700, letterSpacing: '0.08em', color: SOFT,
        lineHeight: 1, opacity: pop(props.rows[0]?.at ?? 0.3)}}>{props.fixLabel}</div>
      <div style={{position: 'absolute', left: ruleX, top: 160, fontFamily: SANS, fontSize: T.sans, fontWeight: 700, letterSpacing: '0.08em', color: INK,
        lineHeight: 1, opacity: ruleHead}}>{props.ruleLabel}</div>
      <svg width={width} height={height} style={{position: 'absolute', left: 0, top: 0}}>
        {props.rows.map((r, i) => {
          const y = top + i * (rowH + rowGap) + rowH / 2;
          const a = ramp(r.ruleAt - 0.04, 0.04);
          const x0 = S.x + fixW + 30, x1 = ruleX - 30;
          return (
            <g key={i} opacity={a > 0 ? 1 : 0}>
              <line x1={x0} y1={y} x2={x0 + (x1 - x0 - 10) * a} y2={y} stroke={INK} strokeWidth={8} strokeLinecap="round" />
              <path d={`M ${x1 - 34} ${y - 24} L ${x1 - 8} ${y} L ${x1 - 34} ${y + 24}`} fill="none" stroke={INK} strokeWidth={8}
                strokeLinecap="round" strokeLinejoin="round" opacity={a} />
            </g>
          );
        })}
      </svg>
      {props.rows.map((r, i) => {
        const y = top + i * (rowH + rowGap);
        const f = pop(r.at), ru = pop(r.ruleAt);
        return (
          <React.Fragment key={i}>
            <BarCard style={{left: S.x, top: y, width: fixW, height: rowH, display: 'flex', alignItems: 'center', padding: '0 40px',
              opacity: 0.45 + 0.55 * f, background: CLAUDE.FOOTER}}>
              <span style={{fontFamily: SERIF, fontSize: 58, fontStyle: 'italic', color: SOFT, lineHeight: 1.1}}>{r.fix}</span>
            </BarCard>
            <BarCard bar={ru} style={{left: ruleX, top: y, width: ruleW, height: rowH, display: 'flex', alignItems: 'center', padding: '0 40px',
              opacity: ru, transform: `translateX(${(1 - ru) * 24}px)`}}>
              <span style={{fontFamily: SERIF, fontSize: 60, fontWeight: 700, color: INK, lineHeight: 1.1}}>{r.rule}</span>
            </BarCard>
          </React.Fragment>
        );
      })}
      <div style={{position: 'absolute', left: S.x, width: S.w, top: top + props.rows.length * (rowH + rowGap) + 40, textAlign: 'center',
        fontFamily: SERIF, fontSize: 64, fontStyle: 'italic', lineHeight: 1.1}}>
        <span style={{opacity: pop(props.luckAt), color: SOFT}}>{props.luck} </span>
        <span style={{opacity: pop(props.processAt), color: INK, fontWeight: 700}}>{props.process}</span>
      </div>
      <LogoBug />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B08 — the gains: speed, efficiency, consistency
// ─────────────────────────────────────────────────────────────────────────────
export const threeGainsSchema = z.object({
  ...dur,
  sparkLine: z.string().default('Faster. Efficient. Consistent.'),
  firstLabel: z.string().default('First video: figure it out'),
  nextLabel: z.string().default('Next video: follow the playbook'),
  pathsAt: z.number().default(0.03),
  gains: z.array(z.object({title: z.string(), why: z.string(), at: z.number()})).default([
    {title: 'Speed', why: 'no blank page', at: 0.1},
    {title: 'Efficiency', why: 'checks before long renders', at: 0.31},
    {title: 'Consistency', why: 'the same spine, every video', at: 0.62},
  ]),
  caption: z.string().default('Illustrative — not measured'),
});
export type ThreeGainsProps = z.infer<typeof threeGainsSchema>;

export const ThreeGains: React.FC<ThreeGainsProps> = (props) => {
  const {portrait, S, pop, ramp, width, height} = useBeat(props.durationSeconds);
  const T = ty(portrait);
  const draw = ramp(props.pathsAt, 0.18);
  const lanes = portrait
    ? [{y: S.y + 260 + 230, label: props.firstLabel}, {y: S.y + 260 + 490, label: props.nextLabel}]
    : [{y: 250, label: props.firstLabel}, {y: 470, label: props.nextLabel}];
  const x0 = S.x + 30, x1 = portrait ? S.r - 30 : S.r - 30;
  const shortX = x0 + (x1 - x0) * 0.62;
  // winding path for the first video (loops and detours), straight path for the next
  const wind = (y: number) => {
    const amp = portrait ? 70 : 60;
    const pts: string[] = [`M ${x0} ${y}`];
    const seg = (x1 - x0) / 6;
    for (let k = 0; k < 6; k++) {
      const xa = x0 + k * seg;
      pts.push(`C ${xa + seg * 0.3} ${y - amp * (k % 2 ? -1 : 1)} ${xa + seg * 0.7} ${y + amp * (k % 2 ? -1 : 1)} ${xa + seg} ${y}`);
    }
    return pts.join(' ');
  };
  const gTop = portrait ? S.y + 260 + 620 : 690;
  const gN = props.gains.length;
  const gGap = portrait ? 20 : 30;
  const gW = portrait ? S.w : (S.w - gGap * (gN - 1)) / gN, gH = portrait ? 240 : 250;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={portrait} S={S} />
      {lanes.map((l, i) => (
        <div key={i} style={{position: 'absolute', left: S.x, top: l.y - (portrait ? 150 : 110), fontFamily: SANS, fontSize: T.sans, fontWeight: 700,
          color: i === 0 ? SOFT : INK, lineHeight: 1, opacity: pop(props.pathsAt)}}>{l.label}</div>
      ))}
      <svg width={width} height={height} style={{position: 'absolute', left: 0, top: 0}}>
        <path d={wind(lanes[0].y)} fill="none" stroke={SOFT} strokeWidth={8} strokeLinecap="round" pathLength={1} strokeDasharray={1}
          strokeDashoffset={1 - draw} />
        <line x1={x0} y1={lanes[1].y} x2={x0 + (shortX - x0) * draw} y2={lanes[1].y} stroke={ACCENT} strokeWidth={12} strokeLinecap="round" />
        <circle cx={x1} cy={lanes[0].y} r={16} fill={SOFT} opacity={clamp01(draw * 3 - 2)} />
        <circle cx={shortX} cy={lanes[1].y} r={18} fill={INK} opacity={clamp01(draw * 3 - 2)} />
      </svg>
      {props.gains.map((g, i) => {
        const t = pop(g.at);
        return (
          <BarCard key={i} style={{left: portrait ? S.x : S.x + i * (gW + gGap), top: portrait ? gTop + i * (gH + gGap) : gTop, width: gW, height: gH,
            padding: portrait ? '26px 40px' : '40px 40px', opacity: 0.45 + 0.55 * t, border: portrait ? `3px solid ${CLAUDE.BORDER}` : undefined}}>
            <div style={{display: 'flex', alignItems: 'center', gap: 16}}>
              <span style={{opacity: t}}><Check size={portrait ? 80 : 58} /></span>
              <span style={{fontFamily: SERIF, fontSize: portrait ? T.serif : 64, fontWeight: 700, color: INK, lineHeight: 1}}>{g.title}</span>
            </div>
            <div style={{fontFamily: SANS, fontSize: T.sans, fontStyle: 'italic', color: SOFT, lineHeight: 1.1, marginTop: portrait ? 14 : 26}}>{g.why}</div>
          </BarCard>
        );
      })}
      <Caption text={props.caption} S={S} portrait={portrait} opacity={pop(props.pathsAt)} />
      <LogoBug portrait={portrait} />
    </AbsoluteFill>
  );
};

// ─────────────────────────────────────────────────────────────────────────────
// B09 — the limit: a starting point, not a cage
// ─────────────────────────────────────────────────────────────────────────────
const col = z.object({title: z.string(), items: z.array(z.object({label: z.string(), at: z.number()}))});
export const playbookLimitsSchema = z.object({
  ...dur,
  sparkLine: z.string().default('A starting point, not a cage.'),
  fixed: col.default({title: 'KEEP FIXED', items: [{label: 'The spine', at: 0.32}, {label: 'The checks', at: 0.39}, {label: 'The brand', at: 0.45}]}),
  changing: col.default({title: 'KEEP CHANGING', items: [{label: 'The examples', at: 0.62}, {label: 'The visuals', at: 0.69}, {label: 'The hooks', at: 0.74}]}),
  loopLabel: z.string().default('Update the playbook when something new works.'),
  loopAt: z.number().default(0.82),
});
export type PlaybookLimitsProps = z.infer<typeof playbookLimitsSchema>;

export const PlaybookLimits: React.FC<PlaybookLimitsProps> = (props) => {
  const {portrait, S, pop, ramp, width, height} = useBeat(props.durationSeconds);
  const T = ty(portrait);
  const loop = ramp(props.loopAt, 0.1);
  const cols = [props.fixed, props.changing];
  const gap = portrait ? 30 : 40;
  const cw = portrait ? S.w : (S.w - gap) / 2;
  const top = portrait ? S.y + 260 : 170;
  const itemH = portrait ? 118 : 120;
  const ch = (portrait ? 130 : 110) + 3 * itemH + 30;
  const loopTop = portrait ? top + 2 * (ch + gap) + 30 : top + ch + 60;
  const r = portrait ? 56 : 48;
  const lx = S.x + r + 10, ly = loopTop + r + 8;
  return (
    <AbsoluteFill style={{background: STAGE}}>
      <SparkLine text={props.sparkLine} portrait={portrait} S={S} />
      {cols.map((c, i) => (
        <BarCard key={i} style={{left: portrait ? S.x : S.x + i * (cw + gap), top: portrait ? top + i * (ch + gap) : top, width: cw, height: ch,
          padding: portrait ? '36px 40px' : '34px 44px', opacity: pop(c.items[0]?.at ?? 0.3), border: portrait ? `3px solid ${CLAUDE.BORDER}` : undefined}}>
          <div style={{fontFamily: SANS, fontSize: T.sans, fontWeight: 700, letterSpacing: '0.08em', color: SOFT, lineHeight: 1}}>{c.title}</div>
          <div style={{marginTop: portrait ? 26 : 30}}>
            {c.items.map((it, j) => {
              const t = pop(it.at);
              return (
                <div key={j} style={{height: itemH, display: 'flex', alignItems: 'center', gap: 18, opacity: 0.45 + 0.55 * t}}>
                  <span style={{opacity: t}}><Check size={portrait ? 76 : 56} /></span>
                  <span style={{fontFamily: SERIF, fontSize: portrait ? T.serif : 62, fontWeight: 700, color: INK, lineHeight: 1}}>{it.label}</span>
                </div>
              );
            })}
          </div>
        </BarCard>
      ))}
      <svg width={width} height={height} style={{position: 'absolute', left: 0, top: 0}}>
        <path d={`M ${lx} ${ly - r} A ${r} ${r} 0 1 1 ${lx - r * Math.sin(0.9)} ${ly - r * Math.cos(0.9)}`} fill="none" stroke={ACCENT} strokeWidth={10}
          strokeLinecap="round" pathLength={1} strokeDasharray={1} strokeDashoffset={1 - loop} opacity={loop > 0 ? 1 : 0} />
        <path d={`M ${lx + 4} ${ly - r - 20} L ${lx + 26} ${ly - r} L ${lx + 4} ${ly - r + 20}`} fill="none" stroke={ACCENT} strokeWidth={10}
          strokeLinecap="round" strokeLinejoin="round" opacity={clamp01(loop * 4 - 3)} />
      </svg>
      <div style={{position: 'absolute', left: S.x + 2 * r + 50, width: S.w - 2 * r - 50, top: loopTop, minHeight: 2 * r + 16, display: 'flex',
        alignItems: 'center', fontFamily: SERIF, fontSize: portrait ? T.serif : 60, fontStyle: 'italic', color: INK, lineHeight: 1.08,
        opacity: pop(props.loopAt)}}>{props.loopLabel}</div>
      <LogoBug portrait={portrait} />
    </AbsoluteFill>
  );
};
