import React from 'react';
import { AbsoluteFill, Audio, Sequence, staticFile, interpolate, useCurrentFrame } from 'remotion';
import { ClaudeComposerAsk, claudeComposerAskSchema } from '../runtime/scenes/ClaudeComposerAsk';
import { ClaudeWindow } from '../onda/registry/components/claude-window/ClaudeWindow';
import { claudeWindowSchema } from '../onda/registry/components/claude-window/schema';
import { IlluStage, PredictCard } from './Illustrations';
import { TeachersLayerStack, StandardsToCowork, ConnectorGrid, CoworkScheduleBeat } from './TeachersIllu';
import { CLAUDE, CLAUDE_FONT } from '../runtime/tokens/claude';
import DATA from './teachers_data.json';

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;

const OutroCard: React.FC<{ props: any }> = ({ props }) => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [0, 12], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, alignItems: 'center', justifyContent: 'center', opacity: o }}>
      <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 68, color: '#111', letterSpacing: '-0.02em', textAlign: 'center', lineHeight: 1.05, maxWidth: 1050 }}>
        {String(props.title).replace(/\.$/, '')}<span style={{ color: CLAUDE.SEND }}>.</span>
      </div>
      <div style={{ fontFamily: SERIF, fontSize: 38, color: CLAUDE.INK, marginTop: 28 }}>{props.handle}</div>
      <div style={{ fontFamily: SANS, fontSize: 23, color: CLAUDE.INK_SOFT, marginTop: 12 }}>{props.subline}</div>
    </AbsoluteFill>
  );
};

export const TeachersReel: React.FC = () => {
  let at = 0;
  const seqs = (DATA as any).beats.map((b: any) => {
    const from = at;
    at += b.frames;
    let content: React.ReactNode = null;
    switch (b.kind) {
      case 'ClaudeComposerAsk':
        content = <ClaudeComposerAsk {...claudeComposerAskSchema.parse(b.props)} />;
        break;
      case 'TeachersLayerStack':
        content = <IlluStage spark={b.props.sparkLine}><TeachersLayerStack /></IlluStage>;
        break;
      case 'StandardsToCowork':
        content = <IlluStage spark={b.props.sparkLine}><StandardsToCowork /></IlluStage>;
        break;
      case 'ConnectorGrid':
        content = <IlluStage spark={b.props.sparkLine}><ConnectorGrid /></IlluStage>;
        break;
      case 'CoworkScheduleBeat':
        content = <CoworkScheduleBeat sparkLine={b.props.sparkLine} />;
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
