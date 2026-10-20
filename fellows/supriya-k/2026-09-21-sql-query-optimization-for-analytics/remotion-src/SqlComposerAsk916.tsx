/**
 * SqlComposerAsk916 — portrait composer for B00 / B02 / B08.
 *
 * WHY THIS EXISTS: the library `ClaudeComposerAsk916` is built for SHORT
 * commands. This reel's ask is ~300 characters and its handoff prompt ~380, and
 * in portrait the library card overflowed the bottom of the frame — the prompt
 * was cut mid-sentence and **B00's three RESULT output lines never rendered at
 * all**, breaking COLD OPEN LAW ("B00's composer always shows its RESULT output
 * lines — the ask lands answered"). QC pass 1 of the vertical companion caught it.
 *
 * THE FIX: the command font AUTO-FITS. The component estimates the wrapped line
 * count at a candidate size and shrinks until the block fits its budget, and the
 * output lines get reserved space BELOW the card that the card can never eat.
 * Long asks therefore shrink rather than overflow.
 *
 * Props are a superset-compatible match for `claudeComposerAskSchema`, so the
 * 16:9 beat props carry over unchanged (standing rule #4).
 *
 * Registered 1080x1920; --scale=2 renders 2160x3840 native.
 *
 * REEL-LOCAL. Register per remotion-src/REGISTER.md.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate} from 'remotion';
import {z} from 'zod';
import {clamp, remap, scW, wrapText} from './sqlDeckKit';

export const sqlComposerAsk916Schema = z.object({
  command: z.string().default(''),
  topic: z.string().default(''),
  segment: z.string().default(''),
  greeting: z.string().default(''),
  runningText: z.string().default(''),
  output: z.array(z.string()).optional(),
  folderLabel: z.string().default('@HumanitariansAI'),
  modelLabel: z.string().default('Fable 5'),
  effortLabel: z.string().default('High'),
  placeholder: z.string().default('Type / for skills'),
});
export type SqlComposerAsk916Props = z.infer<typeof sqlComposerAsk916Schema>;

const PAGE = '#FAF9F5', CARD = '#FFFFFF', BORDER = '#E5E2D9';
const INK = '#3D3929', INK_SOFT = '#73705F', SPARK = '#D97757', SEND = '#C6613F';
const SERIF = "'EB Garamond', Georgia, serif";
const SANS = "system-ui, -apple-system, 'Segoe UI', sans-serif";
const MONO = "'JetBrains Mono', ui-monospace, monospace";

const Spark: React.FC<{size: number; color?: string}> = ({size, color = SPARK}) => (
  <svg width={size} height={size} viewBox="0 0 24 24" style={{flexShrink: 0}}>
    {Array.from({length: 8}, (_, i) => (
      <line key={i} x1={12} y1={12}
        x2={12 + Math.cos((i * Math.PI) / 4) * 9}
        y2={12 + Math.sin((i * Math.PI) / 4) * 9}
        stroke={color} strokeWidth={2} strokeLinecap="round" />
    ))}
  </svg>
);

export const SqlComposerAsk916: React.FC<SqlComposerAsk916Props> = ({
  command, topic, segment, greeting, runningText, output,
  folderLabel, modelLabel, effortLabel,
}) => {
  const frame = useCurrentFrame();
  const {fps, width: W, height: H, durationInFrames} = useVideoConfig();
  const p = clamp(frame / Math.max(1, durationInFrames - 1), 0, 1);
  const S = scW(W);

  const outs = output ?? [];
  const cardX = 56 * S, cardW = W - 112 * S;
  const innerW = cardW - 64 * S;

  // ── AUTO-FIT: shrink until the wrapped command fits its budget ──
  const budgetH = (outs.length > 0 ? 520 : 760) * S;   // reserve room for outputs
  let fs = 36 * S, lines = wrapText(command, 1);
  for (let cand = 36; cand >= 20; cand -= 2) {
    const f = cand * S;
    const chars = Math.max(12, Math.floor(innerW / (f * 0.52)));
    const ls = wrapText(command, chars);
    if (ls.length * f * 1.34 <= budgetH || cand === 20) { fs = f; lines = ls; break; }
  }
  const textH = lines.length * fs * 1.34;
  const chromeH = 96 * S;
  const cardH = textH + 56 * S + chromeH;
  const cardY = clamp(H * 0.36, 0, H);

  // typing
  const typed = clamp(remap(p, 0.06, 0.52, 0, 1), 0, 1);
  const shown = Math.floor(command.length * typed);
  let acc = 0;
  const visLines = lines.map((ln) => {
    const take = clamp(shown - acc, 0, ln.length);
    acc += ln.length + 1;
    return ln.slice(0, take);
  });

  const greetIn = spring({frame, fps, config: {damping: 28, stiffness: 140, mass: 0.8}});
  const sendArm = clamp(remap(p, 0.54, 0.60, 0, 1), 0, 1);
  const runIn = clamp(remap(p, 0.58, 0.64, 0, 1), 0, 1);

  const afterCard = cardY + cardH;

  return (
    <AbsoluteFill style={{background: PAGE}}>
      <div style={{position: 'absolute', left: 64 * S, top: 108 * S,
        fontFamily: SANS, fontSize: 25 * S, fontWeight: 700, color: INK_SOFT, letterSpacing: 3 * S}}>
        {topic}
      </div>
      <div style={{position: 'absolute', left: 64 * S, top: 158 * S, right: 64 * S,
        fontFamily: SERIF, fontSize: 62 * S, color: INK, lineHeight: 1.12}}>
        {segment}
      </div>

      {greeting ? (
        <div style={{
          position: 'absolute', left: 0, right: 0, top: H * 0.24,
          display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 18 * S,
          opacity: clamp(greetIn, 0, 1),
        }}>
          <Spark size={40 * S} />
          <span style={{fontFamily: SERIF, fontSize: 66 * S, color: INK}}>{greeting}</span>
        </div>
      ) : null}

      {/* composer card */}
      <div style={{
        position: 'absolute', left: cardX, top: cardY, width: cardW, height: cardH,
        background: CARD, border: `${1 * S}px solid ${BORDER}`, borderRadius: 26 * S,
        boxShadow: '0 10px 40px rgba(61,57,41,0.10)', overflow: 'hidden',
      }}>
        <div style={{padding: `${28 * S}px ${32 * S}px 0`, fontFamily: SANS,
          fontSize: fs, lineHeight: 1.34, color: INK, textAlign: 'left'}}>
          {visLines.map((ln, i) => <div key={i}>{ln || ' '}</div>)}
        </div>
        <div style={{
          position: 'absolute', left: 0, right: 0, bottom: 0, height: chromeH,
          display: 'flex', alignItems: 'center', padding: `0 ${32 * S}px`, gap: 14 * S,
        }}>
          <div style={{width: 44 * S, height: 44 * S, borderRadius: '50%',
            border: `${1.5 * S}px solid ${BORDER}`, display: 'flex',
            alignItems: 'center', justifyContent: 'center',
            fontFamily: SANS, fontSize: 28 * S, color: INK_SOFT}}>+</div>
          <div style={{marginLeft: 'auto', display: 'flex', alignItems: 'center', gap: 14 * S}}>
            <span style={{fontFamily: SANS, fontSize: 25 * S, fontWeight: 700, color: INK}}>{modelLabel}</span>
            <span style={{fontFamily: SANS, fontSize: 25 * S, color: '#A9A491'}}>{effortLabel}</span>
            <div style={{width: 48 * S, height: 48 * S, borderRadius: 12 * S,
              background: sendArm > 0.5 ? SEND : BORDER, display: 'flex',
              alignItems: 'center', justifyContent: 'center',
              fontFamily: SANS, fontSize: 26 * S, color: '#fff'}}>↑</div>
          </div>
        </div>
      </div>

      {/* folder chip */}
      <div style={{position: 'absolute', left: 64 * S, top: afterCard + 40 * S,
        fontFamily: SANS, fontSize: 25 * S, fontWeight: 700, color: INK_SOFT}}>
        {folderLabel}
      </div>

      {/* running indicator */}
      {runningText ? (
        <div style={{position: 'absolute', left: 64 * S, top: afterCard + 92 * S,
          display: 'flex', alignItems: 'center', gap: 12 * S, opacity: runIn}}>
          <Spark size={22 * S} />
          <span style={{fontFamily: MONO, fontSize: 27 * S, color: SPARK}}>{runningText}</span>
        </div>
      ) : null}

      {/* RESULT lines — reserved space; the card can never eat them */}
      {outs.map((ln, i) => {
        const st = 0.66 + i * 0.09;
        const op = clamp(remap(p, st, st + 0.08, 0, 1), 0, 1);
        const wrapped = wrapText(ln, Math.floor((W - 128 * S) / (26 * S * 0.6)));
        return (
          <div key={i} style={{
            position: 'absolute', left: 64 * S, right: 64 * S,
            top: afterCard + (152 + i * 76) * S,
            fontFamily: MONO, fontSize: 26 * S, lineHeight: 1.32, color: INK, opacity: op,
          }}>
            {wrapped.map((w, k) => <div key={k}>{w}</div>)}
          </div>
        );
      })}
    </AbsoluteFill>
  );
};
