import React from 'react';
import { AbsoluteFill, Audio, Sequence, staticFile, interpolate, useCurrentFrame } from 'remotion';
import { ClaudeComposerAsk, claudeComposerAskSchema } from '../runtime/scenes/ClaudeComposerAsk';
import { ClaudeWindow } from '../onda/registry/components/claude-window/ClaudeWindow';
import { claudeWindowSchema } from '../onda/registry/components/claude-window/schema';
import { IlluStage, PredictCard, SparkLine } from './Illustrations';
import { EcosystemWheel } from './Wheel';
import { CLAUDE, CLAUDE_FONT } from '../runtime/tokens/claude';
import DATA from './debunked_data.json';

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;

/* The exhibit: the 1000x1200 wheel scaled onto the 16:9 stage. */
const WheelBeat: React.FC<{ spark: string; wheel: any }> = ({ spark, wheel }) => (
  <AbsoluteFill style={{ background: '#F2F0E9' }}>
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
      <div style={{
        width: 1000, height: 1200, flex: '0 0 auto',
        transform: 'translateY(-24px) scale(0.5)', transformOrigin: 'center center',
        borderRadius: 18, overflow: 'hidden', boxShadow: '0 18px 50px rgba(61,57,41,0.22)',
        position: 'relative',
      }}>
        <EcosystemWheel grade={wheel.grade} startAt={wheel.startAt ?? 0} focus={wheel.focus} />
      </div>
    </AbsoluteFill>
    <SparkLine text={spark} pos="bottom" />
  </AbsoluteFill>
);

const OutroCard: React.FC<{ props: any }> = ({ props }) => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [0, 12], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, alignItems: 'center', justifyContent: 'center', opacity: o }}>
      <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 68, color: '#111', letterSpacing: '-0.02em', textAlign: 'center', lineHeight: 1.05, maxWidth: 1050 }}>
        {props.title}<span style={{ color: CLAUDE.SEND }}>?</span>
      </div>
      <div style={{ fontFamily: SERIF, fontSize: 38, color: CLAUDE.INK, marginTop: 28 }}>{props.handle}</div>
      <div style={{ fontFamily: SANS, fontSize: 23, color: CLAUDE.INK_SOFT, marginTop: 12 }}>{props.subline}</div>
    </AbsoluteFill>
  );
};

export const DebunkedReel: React.FC = () => {
  let at = 0;
  const seqs = (DATA as any).beats.map((b: any) => {
    const from = at;
    at += b.frames;
    let content: React.ReactNode = null;
    switch (b.kind) {
      case 'ClaudeComposerAsk':
        content = <ClaudeComposerAsk {...claudeComposerAskSchema.parse(b.props)} />;
        break;
      case 'EcosystemWheelBeat':
        content = <WheelBeat spark={b.props.sparkLine} wheel={b.props.wheel} />;
        break;
      case 'PredictCard':
        content = (
          <IlluStage spark={b.props.sparkLine}>
            <PredictCard question={b.props.question} commit={b.props.commit} />
          </IlluStage>
        );
        break;
      case 'ClaudeVerdictArtifact':
        content = (
          <AbsoluteFill style={{ background: '#F2F0E9', alignItems: 'center', justifyContent: 'center' }}>
            <ClaudeWindow {...claudeWindowSchema.parse({
              view: 'artifact', width: 980, height: 590, fontSize: 16,
              artifactTitle: b.props.artifactTitle,
              artifactHeading: b.props.artifactHeading,
              artifactLines: b.props.artifactLines,
            })} />
          </AbsoluteFill>
        );
        break;
      default:
        content = <OutroCard props={b.props} />;
    }
    return (
      <Sequence key={b.id} from={from} durationInFrames={b.frames}>
        {content}
        <Audio src={staticFile(b.audio)} />
      </Sequence>
    );
  });
  return <AbsoluteFill style={{ background: CLAUDE.PAGE }}>{seqs}</AbsoluteFill>;
};
