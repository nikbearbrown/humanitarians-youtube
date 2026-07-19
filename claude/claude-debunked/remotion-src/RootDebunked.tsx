import React from 'react';
import { Composition } from 'remotion';
import { DebunkedReel } from './Debunked';
import DATA from './debunked_data.json';

export const RemotionRoot: React.FC = () => (
  <Composition id="ClaudeDebunked" component={DebunkedReel} durationInFrames={(DATA as any).totalFrames} fps={30} width={1280} height={720} />
);
