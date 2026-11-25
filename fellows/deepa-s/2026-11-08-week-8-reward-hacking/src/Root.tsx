import React,{useEffect,useState} from 'react';
import {AbsoluteFill,Composition,registerRoot,useCurrentFrame,useVideoConfig,staticFile,delayRender,continueRender} from 'remotion';
import sheet from '../beat_sheet.json';
import captions from '../captions.json';
import {VisualWorld,P,refs} from './redesign/Worlds';
const ease=(v:number)=>1-Math.pow(1-Math.max(0,Math.min(1,v)),3);
const Film=()=>{const frame=useCurrentFrame(),{fps,width,height}=useVideoConfig(),p=height>width,now=frame/fps;
const [gate]=useState(()=>delayRender('Editorial fonts'));
useEffect(()=>{Promise.all([['Montserrat-Medium.ttf','Montserrat','500'],['Montserrat-Bold.ttf','Montserrat','700'],['EBGaramond-Regular.ttf','Editorial','400']].map(async([file,family,weight])=>{const f=new FontFace(family,`url(${staticFile('fonts/'+file)})`,{weight});await f.load();document.fonts.add(f)})).then(()=>continueRender(gate))},[]);
const index=Math.max(0,sheet.beats.findIndex(b=>now>=b.start_s&&now<b.end_s));const b=sheet.beats[index],t=now-b.start_s;const cue=captions.find(c=>now*1000>=c.startMs&&now*1000<c.endMs);const opacity=ease(t/.32)*(index===sheet.beats.length-1?1:Math.min(1,(b.duration_s-t)/.2));
return <AbsoluteFill style={{background:P.paper,color:P.ink,fontFamily:'Montserrat',overflow:'hidden'}}>
<svg width={width} height={height} style={{position:'absolute',inset:0}}><defs><pattern id="paper" width={13} height={13} patternUnits="userSpaceOnUse"><path d="M1 2h1M8 10h1" stroke="#A99C81" strokeWidth={.7} opacity={.14}/></pattern></defs><rect width="100%" height="100%" fill="url(#paper)"/><path d={`M${width*.55} 0H${width}V${height*.55}Z`} fill="#E9E1D1"/></svg>
<div style={{position:'absolute',left:p?65:100,right:p?65:100,top:p?105:60,display:'flex',justifyContent:'space-between',fontSize:24,color:P.sage,fontWeight:700}}><span>HUMANITARIANS AI</span><span>DEEPA S. / WEEK {sheet.metadata.week}</span></div>
<div data-qc="heading" style={{position:'absolute',left:p?65:100,right:p?65:100,top:p?155:107,fontFamily:'Editorial',fontSize:p?72:78,lineHeight:1.02}}>{b.heading}</div>
<div data-qc="visual" style={{position:'absolute',left:p?65:100,top:p?340:245,width:p?950:1720,height:p?1140:600,opacity}}><VisualWorld week={sheet.metadata.week} stem={sheet.metadata.category==='STEM'} index={index} t={t} p={p}/></div>
<div data-qc="source" style={{position:'absolute',left:p?65:100,right:p?65:100,top:p?1508:855,fontSize:p?21:20,color:P.soft}}>{b.citations.length?b.citations.map(id=>refs[id]).join(' • '):(sheet.metadata.category==='STEM'?'Original educational illustration':'Illustrative workspace • Deepa’s reported work')}</div>
{cue&&<div data-qc="caption" style={{position:'absolute',left:p?65:100,right:p?65:100,bottom:p?165:85,background:'#F4F0E5F5',borderTop:'2px solid '+P.line,padding:'16px 0',fontSize:29,lineHeight:1.35,textAlign:'center'}}>{cue.text}</div>}
<div style={{position:'absolute',left:p?65:100,right:p?65:100,bottom:p?110:57,fontSize:p?21:20,display:'flex',justifyContent:'space-between',color:P.sage}}><span>@HumanitariansAI</span><span>Liam, narrating for Deepa.</span></div>
</AbsoluteFill>};
registerRoot(()=> <><Composition id="Landscape" component={Film} width={1920} height={1080} fps={24} durationInFrames={sheet.metadata.duration_frames}/><Composition id="Portrait" component={Film} width={1080} height={1920} fps={24} durationInFrames={sheet.metadata.duration_frames}/></>);
