import React, {useEffect, useState} from 'react';
import {AbsoluteFill, Img, staticFile, useCurrentFrame, useVideoConfig, interpolate, delayRender, continueRender} from 'remotion';
import {HUMANITARIANS as C} from '../tokens/humanitarians';

/** HAI educational/workflow diagrams; separate native wide and tall arrangements.
 * Metadata/labels are project inputs, never fabricated terminal output. */
export type DeepaProps={heading:string;labels:string[];mode:string;week:number;kind:string;frames:number;audit?:boolean};
export const DeepaContinuation:React.FC<DeepaProps>=({heading,labels,mode,week,kind,frames,audit=false})=>{
 const frame=useCurrentFrame(),{width,height}=useVideoConfig(),p=height>width;
 const [gate]=useState(()=>delayRender('Load HAI fonts'));
 useEffect(()=>{Promise.all([['EB Garamond','EBGaramond-Regular.ttf'],['Montserrat','Montserrat-Medium.ttf']].map(async([family,file])=>{const font=new FontFace(family,`url(${staticFile('fonts/'+file)})`);await font.load();document.fonts.add(font)})).then(()=>continueRender(gate)).catch(()=>continueRender(gate))},[gate]);
 const W=p?1080:1920,H=p?1920:1080,s=width/W;
 const progress=frame/Math.max(1,frames-1);
 const reveal=(i:number)=>interpolate(progress,[.10+i*.20,.16+i*.20],[0,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp'});
 const serif='EB Garamond, Georgia, serif',sans='Montserrat, Arial, sans-serif';
 const pos=(i:number)=>p?{x:94,y:470+i*310,w:892,h:290}:{x:120+i*570,y:380,w:540,h:390};
 const path=(i:number)=>{const a=pos(i),b=pos(i+1);return p?`M ${a.x+a.w/2} ${a.y+a.h+8} L ${b.x+b.w/2} ${b.y-12}`:`M ${a.x+a.w+5} ${a.y+a.h/2} L ${b.x-8} ${b.y+b.h/2}`};
 useEffect(()=>{if(!audit)return;requestAnimationFrame(()=>{const nodes=[...document.querySelectorAll('[data-qc]')];console.log('DEEPA_LAYOUT '+JSON.stringify({heading,portrait:p,width,height,rows:nodes.map(n=>{const r=n.getBoundingClientRect();const e=n as HTMLElement;return{text:n.textContent,x:r.x,y:r.y,w:r.width,h:r.height,overflow:e.scrollWidth>e.clientWidth+2||e.scrollHeight>e.clientHeight+2}})}))})},[audit,heading,p,width,height]);
 const special=heading==='Seeing the answers';
 return <AbsoluteFill style={{background:C.CREAM,color:C.INK,overflow:'hidden'}}>
 <div style={{position:'absolute',width:W,height:H,transform:`scale(${s})`,transformOrigin:'top left',fontFamily:serif}}>
  <div data-qc style={{position:'absolute',left:p?94:120,top:p?125:75,fontFamily:sans,fontSize:p?72:38,color:C.TEAL}}>{p?`Deepa S. · Week ${week}`:`Deepa S. · Week ${week} · ${kind==='stem'?'STEM':'Progress'}`}</div>
  <div data-qc style={{position:'absolute',left:p?94:120,top:p?225:150,width:p?892:1680,fontSize:p?90:88,lineHeight:p?1.2:1.35,paddingBottom:12,fontWeight:600}}>{heading}</div>
  <svg width={W} height={H} style={{position:'absolute',inset:0}} aria-hidden>
   <defs><marker id="tip" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0L8 4L0 8" fill={C.TEAL}/></marker></defs>
   {(mode==='flow'||mode==='timeline')&&[0,1].map(i=><path key={i} d={path(i)} stroke={C.TEAL} strokeWidth={5} fill="none" strokeDasharray={p?70:30} strokeDashoffset={(1-reveal(i+1))*(p?70:30)} opacity={reveal(i+1)} markerEnd="url(#tip)"/>)}
  </svg>
  {labels.map((text,i)=>{const a=pos(i);const r=reveal(i);return <div key={i} style={{position:'absolute',left:a.x,top:a.y,width:a.w,height:a.h,boxSizing:'border-box',border:`3px solid ${i===2?C.TEAL:C.SLATE}`,background:'#FFFAF1',padding:p?'24px 30px':'34px 32px',display:p?'flex':'block',flexDirection:'column',justifyContent:'center',transform:`translate${p?'X':'Y'}(${(1-r)*18}px)`,opacity:1}}>
   <div data-qc style={{fontFamily:sans,fontSize:p?72:38,color:C.TEAL,marginBottom:p?10:22,display:p?'none':'block'}}>{mode==='timeline'?['BEFORE','PREDICT','AFTER'][i]:String(i+1).padStart(2,'0')}</div>
   <div data-qc style={{fontFamily:p?sans:serif,fontSize:p?72:54,lineHeight:p?1.15:1.4,paddingBottom:12,maxWidth:'100%',overflowWrap:'break-word'}}>{text}</div>
   {special&&!p&&<div style={{display:'flex',gap:p?35:23,marginTop:p?24:35}}>{[0,1,0,1].map((v,j)=><div key={j} style={{width:p?48:60,height:p?48:60,borderRadius:'50%',background:i===1&&v===1?'#D8C6B6':C.TEAL,opacity:.4+.6*interpolate(progress,[.18+i*.2+j*.015,.22+i*.2+j*.015],[0,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp'})}}/>)}</div>}

  </div>})}
  <div data-qc style={{position:'absolute',left:p?94:120,top:p?1410:830,width:p?892:1680,fontFamily:sans,fontSize:p?72:38,color:C.SLATE,lineHeight:1.25}}>{p?(special||heading==='Bad inputs change the answer'?'Illustrative example':mode==='outro'?'Liam for Deepa':'Humanitarians AI'):(special?'Fictional illustration · not a real model result':heading==='Bad inputs change the answer'?'Fictional illustration · units explicitly stipulated':mode==='outro'?'Liam, narrating for Deepa.':'Humanitarians AI · '+(kind==='stem'?'Understand the evidence':'Learn the workflow'))}</div>
  <div style={{position:'absolute',left:p?94:120,right:p?94:120,bottom:p?300:75,display:'flex',justifyContent:'space-between',alignItems:'center',gap:35}}><span data-qc style={{fontFamily:sans,fontSize:p?72:38,color:C.TEAL}}>@HumanitariansAI</span>{!p&&<Img src={staticFile('hai-wordmark-outlined.svg')} style={{width:p?280:330,height:p?65:60,objectFit:'contain'}}/>}</div>
 </div>
 </AbsoluteFill>
};
