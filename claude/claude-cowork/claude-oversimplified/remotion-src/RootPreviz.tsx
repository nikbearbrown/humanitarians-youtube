import React from 'react';
import { Composition } from 'remotion';
import { ClaudeOversimplifiedPreviz, TOTAL_FRAMES } from './Previz';

export const RemotionRoot: React.FC = () => (
  <Composition id="ClaudeOversimplifiedPreviz" component={ClaudeOversimplifiedPreviz}
    durationInFrames={TOTAL_FRAMES} fps={30} width={1280} height={720} />
);
