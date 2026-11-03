import React from 'react';
import { Composition } from 'remotion';
import { GroundingFlow, GroundingFlow916, groundingFlowSchema } from './GroundingFlow';
import { PanelFocus916, panelFocusSchema } from './PanelFocus916';

// Reel-local compositions only. Authored at 1920x1080 / 1080x1920 and rendered with
// --scale=2 (native 3840x2160 / 2160x3840), the same convention as the toolkit library.
// durationSeconds in props sets the length (matched to the beat's measured clock).
const dur = (fallback: number) => ({ props }: { props: Record<string, unknown> }) => ({
  durationInFrames: Math.round(((props.durationSeconds as number) ?? fallback) * 30),
});

export const RemotionRoot: React.FC = () => (
  <>
    <Composition id="GroundingFlow" component={GroundingFlow} schema={groundingFlowSchema}
      durationInFrames={514} fps={30} width={1920} height={1080}
      defaultProps={groundingFlowSchema.parse({})} calculateMetadata={dur(17.14)} />
    <Composition id="GroundingFlow916" component={GroundingFlow916} schema={groundingFlowSchema}
      durationInFrames={514} fps={30} width={1080} height={1920}
      defaultProps={groundingFlowSchema.parse({})} calculateMetadata={dur(17.14)} />
    <Composition id="PanelFocus916" component={PanelFocus916} schema={panelFocusSchema}
      durationInFrames={150} fps={30} width={1080} height={1920}
      defaultProps={{ src: 'capture/run-portrait-p2.mp4', startFrom: 28.6, caption: 'Retrieved passages',
        keys: [{ t: 0, x: 2580, y: 0, w: 1260 }], srcW: 3840, srcH: 2160 }}
      calculateMetadata={dur(5)} />
  </>
);
