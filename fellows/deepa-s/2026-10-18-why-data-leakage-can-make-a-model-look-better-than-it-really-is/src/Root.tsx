import React from 'react';
import {Composition} from 'remotion';
import {DeepaContinuation} from './scenes/DeepaContinuation';
const defaults={heading:'Review the data',labels:['Inspect inputs','Apply clear rules','Review the result'],mode:'flow',week:5,kind:'stem',frames:240};
export const Root:React.FC=()=> <>
<Composition id="DeepaContinuation" component={DeepaContinuation} width={1920} height={1080} fps={24} durationInFrames={240} defaultProps={defaults} calculateMetadata={({props})=>({durationInFrames:props.frames})}/>
<Composition id="DeepaContinuation916" component={DeepaContinuation} width={1080} height={1920} fps={24} durationInFrames={240} defaultProps={defaults} calculateMetadata={({props})=>({durationInFrames:props.frames})}/>
</>;
