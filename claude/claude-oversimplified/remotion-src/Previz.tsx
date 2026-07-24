import React from 'react';
import { AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame, interpolate } from 'remotion';
import TIMING from './beats_timing.json';
import { ClaudeComposerAsk } from '../runtime/scenes/ClaudeComposerAsk';
import { claudeComposerAskSchema } from '../runtime/scenes/ClaudeComposerAsk';
import { ClaudeWindow } from '../onda/registry/components/claude-window/ClaudeWindow';
import { claudeWindowSchema } from '../onda/registry/components/claude-window/schema';
import { ClaudeCallout } from '../onda/registry/components/claude-callout/ClaudeCallout';
import { claudeCalloutSchema } from '../onda/registry/components/claude-callout/schema';
import { CLAUDE, CLAUDE_FONT } from '../runtime/tokens/claude';

const FPS = 30;
const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;

// ---- The six poster callouts (canvas fractions match the poster layout) ----
const ITEMS = [
  { title: 'no more copy-paste', body: 'point claude at 1 folder.\nthe real Excel, the real PDF,\nsaved on your computer.', x: 0.22, y: 0.2, targetX: 0.49, targetY: 0.242, bend: 0.2, delay: 0 },
  { title: 'make an app tonight', body: 'describe it in english.\n4 minutes later it exists.\n0 lines of code.', x: 0.78, y: 0.2, targetX: 0.548, targetY: 0.242, bend: -0.2, delay: 0 },
  { title: 'teach it once', body: 'a skill = a saved playbook.\n/skill-creator teaches claude\nyour way of working.', x: 0.22, y: 0.42, targetX: 0.34, targetY: 0.52, bend: 0.2, delay: 0 },
  { title: 'claude prompts YOU', body: 'end every request with\nthis word. it asks the questions.\nyou click the answers.', x: 0.78, y: 0.42, targetX: 0.56, targetY: 0.52, bend: -0.2, delay: 0 },
  { title: 'drop in anything', body: 'a messy doc, an old proposal,\nlast month\u2019s numbers.\nit reads it all.', x: 0.22, y: 0.66, targetX: 0.3, targetY: 0.635, bend: 0.15, delay: 0 },
  { title: 'the smartest AI on earth', body: 'Fable 5. effort on High.\nthat\u2019s the whole setup.', x: 0.78, y: 0.66, targetX: 0.688, targetY: 0.632, bend: -0.15, delay: 0 },
];

const V2_ITEMS = [
  { title: 'it keeps working when you leave', body: 'cowork runs in the cloud.\nclose the laptop \u2014 the task\nfinishes without you.', x: 0.22, y: 0.2, targetX: 0.49, targetY: 0.242, bend: 0.2, delay: 0 },
  { title: 'schedule it', body: 'tasks can run on a clock.\n\u201cevery monday, prep my week\u201d\nis a real thing.', x: 0.78, y: 0.2, targetX: 0.55, targetY: 0.5, bend: -0.2, delay: 0 },
  { title: 'it asks before it acts', body: 'folder access is scoped.\nrisky commands need\nyour click first.', x: 0.22, y: 0.78, targetX: 0.3125, targetY: 0.694, bend: 0.15, delay: 0 },
  { title: 'answers become files', body: 'reports, decks, spreadsheets \u2014\nreal files saved back\nto your folder.', x: 0.78, y: 0.42, targetX: 0.56, targetY: 0.52, bend: -0.2, delay: 0 },
  { title: 'watch it think', body: 'a live task list shows\nevery step \u2014 audit it,\ndon\u2019t trust it blindly.', x: 0.22, y: 0.52, targetX: 0.45, targetY: 0.6, bend: 0.2, delay: 0 },
  { title: 'effort is a dial, not magic', body: 'High burns usage faster.\nMedium is right for\nmost work.', x: 0.78, y: 0.66, targetX: 0.688, targetY: 0.632, bend: -0.15, delay: 0 },
];

// SPARK-LINE LAW: inner beats never show a lonely asterisk — the spark
// carries one short serif line summarizing the beat (the narration's key
// line, compressed). B00's line is the hello greeting.
const SPARK_LINES = [
  'Holds. Real files.',        // B01 no more copy-paste
  'The code exists.',          // B02 make an app tonight
  'Steal this one.',           // B03 teach it once
  'Cowork already asks.',      // B04 claude prompts YOU
  'Librarian, not scanner.',   // B05 drop in anything
  'Marketing, not measurement.', // B06 smartest AI
];
const V2_SPARK_LINE = 'Five of six hold.';

// ---- Beats (mirror of beat_sheet.json) ----
type Beat = { id: string; frames: number; narration: string; kind: string; calloutIndex?: number };
export const BEATS: Beat[] = [
  { id: 'B00', frames: 10 * FPS, narration: 'There’s a poster going around that explains Claude in six arrows. It’s mostly right — and where it’s wrong is instructive. Let’s grade it.', kind: 'ask' },
  { id: 'B01', frames: 11 * FPS, narration: 'Claim one: no more copy-paste. Real. Point Claude at a folder and it edits the actual files — the spreadsheet that comes back is your spreadsheet, saved on your disk.', kind: 'claim', calloutIndex: 0 },
  { id: 'B02', frames: 12 * FPS, narration: 'Make an app tonight — four minutes, zero lines of code. Zero lines you write. The code exists, and you’ll meet it the first time it breaks. Tonight is the honest part.', kind: 'claim', calloutIndex: 1 },
  { id: 'B03', frames: 9 * FPS, narration: 'Teach it once. A skill is a saved playbook, and slash skill-creator does exactly this. Most underrated arrow on the poster. Steal this one.', kind: 'claim', calloutIndex: 2 },
  { id: 'B04', frames: 12 * FPS, narration: 'End every request with AskUserQuestion, and Claude interviews you — real tool, real behavior. Small print: Cowork already asks before big work. The magic word earns its keep in Chat and Code.', kind: 'claim', calloutIndex: 3 },
  { id: 'B05', frames: Math.round(11.5 * FPS), narration: 'Drop in anything — the messy doc, last month’s numbers. Mostly true. On a big folder it reads selectively — a librarian, not a scanner. That’s a feature. Just know it.', kind: 'claim', calloutIndex: 4 },
  { id: 'B06', frames: 13 * FPS, narration: 'The smartest AI on earth — that’s marketing, not a measurement. And effort on High, that’s the whole setup, mis-sets the one knob it mentions. High burns usage. Medium is right for most work.', kind: 'claim', calloutIndex: 5 },
  { id: 'B07', frames: 13 * FPS, narration: 'Verdict: five of six hold. What the poster skips matters more — it keeps working after you close the laptop, it asks before it acts, and answers come back as files. That’s the next video.', kind: 'verdict' },
  { id: 'B08', frames: 4 * FPS, narration: 'If this saved you a bad share, subscribe. Nik Bear Brown.', kind: 'outro' },
];
// AUDIO-FIRST CONFORM: the mp3 durations in beats_timing.json are the master
// clock — each beat's frames come from its measured audio, not the estimates.
const TIMED = BEATS.map((b, i) => ({ ...b, frames: TIMING[i].frames, audio: TIMING[i].audio }));
export const TOTAL_FRAMES = TIMED.reduce((a, b) => a + b.frames, 0);

const Caption: React.FC<{ text: string; beatId: string }> = ({ text, beatId }) => (
  <div style={{
    position: 'absolute', left: '8%', right: '8%', bottom: '3.5%',
    textAlign: 'center', fontFamily: SANS, fontSize: 22, lineHeight: 1.4,
    color: CLAUDE.INK_SOFT, background: 'rgba(250,249,245,0.92)',
    border: `1px solid ${CLAUDE.BORDER}`, borderRadius: 10, padding: '10px 18px',
  }}>
    <span style={{ color: CLAUDE.SPARK, fontWeight: 700, marginRight: 10 }}>{beatId}</span>
    {text}
  </div>
);

const OpenCard: React.FC<{ lines: string[] }> = ({ lines }) => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [0, 12], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, alignItems: 'center', justifyContent: 'center', opacity: o }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 26 }}>
        <svg width={64} height={64} viewBox="0 0 24 24">
          {Array.from({ length: 8 }, (_, i) => (
            <line key={i} x1={12} y1={12}
              x2={12 + 10 * Math.cos((i * Math.PI) / 4 + 0.2)}
              y2={12 + 10 * Math.sin((i * Math.PI) / 4 + 0.2)}
              stroke={CLAUDE.SPARK} strokeWidth={3.2} strokeLinecap="round" />
          ))}
        </svg>
        <div style={{ fontFamily: SERIF, fontSize: 72, color: CLAUDE.INK }}>{lines[0]}</div>
      </div>
      <div style={{ fontFamily: SANS, fontSize: 28, color: CLAUDE.INK_SOFT, marginTop: 24 }}>{lines[1]}</div>
    </AbsoluteFill>
  );
};

const PosterBeat: React.FC<{ upTo: number }> = ({ upTo }) => {
  const settled = ITEMS.slice(0, upTo).map((it) => ({ ...it }));
  const sparkLine = SPARK_LINES[upTo];
  const active = [{ ...ITEMS[upTo] }];
  return (
    <AbsoluteFill style={{ background: '#F2F0E9' }}>
      <div style={{ position: 'absolute', top: 22, width: '100%', textAlign: 'center', fontFamily: SERIF, fontWeight: 700, fontSize: 44, lineHeight: 1.02, color: '#111', letterSpacing: '-0.02em' }}>
        Claude, oversimplified<span style={{ color: CLAUDE.SEND }}>.</span>
      </div>
      <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
        <div style={{ marginTop: 44 }}>
          <ClaudeWindow {...claudeWindowSchema.parse({ view: 'composer', width: 640, height: 460, fontSize: 13, greeting: sparkLine, delay: 0, typeSpeed: 1 })} />
        </div>
      </AbsoluteFill>
      {settled.length > 0 && (
        <ClaudeCallout {...claudeCalloutSchema.parse({ items: settled, delay: -600, increment: 0, titleSize: 26, bodySize: 17, maxWidth: 260 })} />
      )}
      <ClaudeCallout {...claudeCalloutSchema.parse({ items: active, delay: 8, increment: 0, titleSize: 26, bodySize: 17, maxWidth: 260, arrowColor: '#161511' })} />
    </AbsoluteFill>
  );
};

const V2Beat: React.FC = () => (
  <AbsoluteFill style={{ background: '#F2F0E9' }}>
    <div style={{ position: 'absolute', top: 22, width: '100%', textAlign: 'center', fontFamily: SERIF, fontWeight: 700, fontSize: 44, lineHeight: 1.02, color: '#111', letterSpacing: '-0.02em' }}>
      Claude, still oversimplified<span style={{ color: CLAUDE.SEND }}>.</span>
    </div>
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
      <div style={{ marginTop: 44 }}>
        <ClaudeWindow {...claudeWindowSchema.parse({ view: 'composer', width: 640, height: 460, fontSize: 13, greeting: V2_SPARK_LINE, delay: 0, typeSpeed: 1 })} />
      </div>
    </AbsoluteFill>
    <ClaudeCallout {...claudeCalloutSchema.parse({ items: V2_ITEMS, delay: 10, increment: 14, titleSize: 26, bodySize: 17, maxWidth: 260 })} />
  </AbsoluteFill>
);

// Outro law (claude brand): the outro RESTATES THE TITLE, poster-style,
// with the channel handle beneath. Keep this card; never a generic brand outro.
const OutroCard: React.FC = () => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [0, 12], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, alignItems: 'center', justifyContent: 'center', opacity: o }}>
      <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 76, color: '#111', letterSpacing: '-0.02em', textAlign: 'center', lineHeight: 1.05 }}>
        Claude, oversimplified<span style={{ color: CLAUDE.SEND }}>.</span>
      </div>
      <div style={{ fontFamily: SERIF, fontSize: 40, color: CLAUDE.INK, marginTop: 30 }}>@HumanitariansAI</div>
      <div style={{ fontFamily: SANS, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 12 }}>subscribe · the poster, taken apart</div>
    </AbsoluteFill>
  );
};

export const ClaudeOversimplifiedPreviz: React.FC = () => {
  let at = 0;
  const seqs = TIMED.map((b) => {
    const from = at;
    at += b.frames;
    let content: React.ReactNode = null;
    if (b.kind === 'open') content = <OpenCard lines={['Nik Bear Brown', 'The poster, taken apart.']} />;
    else if (b.kind === 'ask') content = (
      <ClaudeComposerAsk {...claudeComposerAskSchema.parse({
        greeting: 'Jambo, Bear',
        topic: 'COWORK · THE POSTER',
        segment: 'Claude, Oversimplified',
        command: '/how-to help me do [X]. AskUserQuestion.',
        runningText: 'grading six claims…',
      })} />
    );
    else if (b.kind === 'claim') content = <PosterBeat upTo={b.calloutIndex!} />;
    else if (b.kind === 'verdict') content = <V2Beat />;
    else content = <OutroCard />;
    return (
      <Sequence key={b.id} from={from} durationInFrames={b.frames}>
        {content}
        <Audio src={staticFile(b.audio)} />
        <Caption text={b.narration} beatId={b.id} />
      </Sequence>
    );
  });
  return <AbsoluteFill style={{ background: CLAUDE.PAGE }}>{seqs}</AbsoluteFill>;
};
