import React from 'react';
import { Composition } from 'remotion';
import { TeachersReel } from './Teachers';
import DATA from './teachers_data.json';

export const RemotionRoot: React.FC = () => (
  <Composition id="ClaudeForTeachers" component={TeachersReel} durationInFrames={(DATA as any).totalFrames} fps={30} width={1280} height={720} />
);
