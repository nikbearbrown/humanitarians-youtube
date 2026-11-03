import React, {useEffect, useState} from 'react';
import {AbsoluteFill, Img, useCurrentFrame, useVideoConfig, interpolate, staticFile, delayRender, continueRender} from 'remotion';
import {z} from 'zod';
import {ClaudeComposerAsk, claudeComposerAskSchema} from './ClaudeComposerAsk';
import {BrutalistHesitantWriter, brutalistHesitantWriterSchema} from './BrutalistHesitantWriter';
import {HUMANITARIANS as C} from '../tokens/humanitarians';

/** DeepaAccuracy: source-checked 100-email worked example, HAI bookends and native portrait layout. */
export const deepaAccuracySchema=z.object({beat:z.string(),frames:z.number(),cues:z.record(z.string(),z.number()).default({})});
type Props=z.infer<typeof deepaAccuracySchema>;
const serif='"EB Garamond", Georgia, serif';
const sans='Montserrat, Arial, sans-serif';
const prompt1='Build a hypothetical example with 99 ordinary emails and one spam email. Predict ordinary for every email. Animate the correct labels and the miss. Show correct labels out of all emails, then spam caught out of actual spam.';
const prompt2='Using the same hypothetical example, show 99% accuracy beside 0% spam recall. Keep the denominators visible: 100 emails overall and one actual spam email. Highlight the missed spam without changing its true label.';
const prompt3='For ninety-nine ordinary emails and one spam email, predict ordinary every time. Calculate accuracy and spam recall, showing both denominators. Explain why the scores differ.';
export const DeepaAccuracy:React.FC<Props>=({beat,cues})=>{
 const f=useCurrentFrame(); const {width:w,height:h,fps}=useVideoConfig(); const p=h>w;
 const [handle]=useState(()=>delayRender('Load HAI fonts'));
 useEffect(()=>{Promise.all([['EB Garamond','EBGaramond-Regular.ttf'],['Montserrat','Montserrat-Medium.ttf']].map(async([name,file])=>{const font=new FontFace(name,`url(${staticFile('fonts/'+file)})`);await font.load();document.fonts.add(font);})).then(()=>continueRender(handle));},[handle]);
 const at=(name:string,fallback:number)=>cues[name]??Math.round(fallback*fps);
 const enter=(start:number)=>interpolate(f,[start,start+10],[0,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp'});
 const base:React.CSSProperties={position:'absolute',left:w*.08,right:w*.08};
 const label:React.CSSProperties={fontFamily:sans,fontSize:p?38:32,lineHeight:1.4};
 const isAsk=['B00','B02','B04','B07'].includes(beat);
 const footer=<div style={{...base,bottom:p?h*.15:h*.07,display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:p?34:30,fontFamily:serif}}><span>@HumanitariansAI</span><Img src={staticFile("hai-wordmark-outlined.svg")} style={{width:p?340:370,height:"auto",opacity:.85}}/></div>;
 const title=(text:string)=><div style={{...base,top:h*.105,fontSize:p?76:84,lineHeight:1.08,fontFamily:serif}}>{text}</div>;
 const source=(text:string)=><div style={{...base,bottom:p?h*.21:h*.13,fontFamily:sans,fontSize:p?36:32}}>{text}</div>;
 const metric=(name:string,value:string,denom:string,color:string)=><div style={{borderTop:`4px solid ${color}`,paddingTop:22,flex:1}}><div style={{...label,color:C.INK}}>{name}</div><div style={{fontFamily:serif,fontSize:p?150:160,lineHeight:1.05,color}}>{value}</div><div style={label}>{denom}</div></div>;
 return <AbsoluteFill style={{background:isAsk?'#F2F0E9':C.CREAM,color:C.INK,fontFamily:serif}}>
 {isAsk&&<>
   <div style={{position:'absolute',inset:0,transform:`translateY(${p?-h*.07:-h*.025}px) scale(${p?.88:.9})`}}><ClaudeComposerAsk {...claudeComposerAskSchema.parse({command:beat==='B00'?'Why can 99% accuracy hide missed spam?':beat==='B02'?(p?'Compare accuracy and spam recall.':prompt1):beat==='B04'?(p?'Show accuracy and recall for this example.':prompt2):(p?'Calculate accuracy and recall. Why do they differ?':prompt3),topic:'Irreducibly Human',segment:beat==='B00'?'Why 99% Accuracy Can Be Misleading':beat==='B02'?'Two Questions':beat==='B04'?'Look At The Miss':'Check The Answer',greeting:beat==='B00'?'Hi, Deepa':beat==='B07'?'Your turn.':'',runningText:beat==='B07'?(p?'':'paste this into Claude…'):'Illustrated explainer interface',output:beat==='B00'?['Count correct labels.','Check which emails were missed.']:beat==='B02'?['Correct labels out of all emails?','Spam caught out of actual spam?']:beat==='B04'?['Same example. Two different questions.']:['Check: 99% accuracy; 0% spam recall.'],folderLabel:'@HumanitariansAI',modelLabel:'Teaching example',effortLabel:'',placeholder:'',animateTyping:beat==='B00'||beat==='B07',largeText:!p})}/></div>
 </>}
 {beat==='B01'&&<>
 <BrutalistHesitantWriter {...brutalistHesitantWriterSchema.parse({text:p?'A high accuracy score\nreveals important\nmistakes.':'A high accuracy score\nreveals important mistakes.',triggerWords:'reveals',replacementWords:'can hide',seed:'deepa-9901',mistakeRate:0,hesitateWithin:0,hesitateBetween:0,jitter:0,charMs:32,fontSize:p?120:90,ink:C.INK,bg:C.CREAM,accent:C.CRIMSON,yOffset:p?-110:-30})}/>
 {title('Look Beyond The Score')}
 <div style={{...base,top:p?h*.64:h*.69,fontSize:p?50:48,opacity:enter(at('check',3))}}>Check which examples were missed.</div>
 {source('Source: Google · ML Crash Course')}
 </>}
 {beat==='B03'&&<>
 {title('One Hundred Emails')}
 <div style={{...base,top:h*.22,...label}}>Hypothetical teaching example</div>
 <div style={{position:'absolute',left:p?w*.235:w*.1,top:p?h*.29:h*.31,width:p?w*.53:w*.39,display:'grid',gridTemplateColumns:'repeat(10,1fr)',gap:p?8:10}}>
 {Array.from({length:100},(_,i)=>{const spam=i===99;const reveal=enter(at('grid',0)+i*.3);const assigned=f>=at('rule',10);return <div key={i} style={{aspectRatio:'1',background:spam?C.CREAM:C.TEAL,border:`${spam?5:2}px solid ${spam?C.CRIMSON:C.TEAL}`,opacity:Math.max(.42,reveal),display:'flex',alignItems:'center',justifyContent:'center',fontFamily:sans,fontSize:p?35:33,color:spam?C.INK:C.CREAM}}>{spam?'!':assigned?'✓':''}</div>})}
 </div>
 <div style={{position:'absolute',left:p?w*.1:w*.55,right:w*.08,top:p?h*.60:h*.33}}>
 <div style={{...label,fontSize:p?32:32}}>True labels: 99 ordinary + 1 spam</div>
 <div style={{...label,fontSize:p?32:32,marginTop:20,opacity:enter(at('rule',10))}}>Rule: always predict ordinary</div>
 <div style={{fontSize:p?100:170,lineHeight:1.2,color:C.TEAL,marginTop:15,opacity:enter(at('score',16))}}>99%</div>
 <div style={{...label,opacity:enter(at('score',16))}}>accuracy · 99 correct out of 100</div>
 </div>
 {source('Constructed example · Definitions: scikit-learn')}
 </>}
 {beat==='B05'&&<>
 {title('The Miss Behind The Score')}
 <div style={{...base,top:h*.235,...label}}>Hypothetical example · 1 actual spam email</div>
 <div style={{...base,top:p?h*.32:h*.34,fontSize:p?48:52}}>Spam → predicted ordinary → <span style={{color:C.INK,textDecorationColor:C.CRIMSON,textDecorationLine:'underline'}}>missed</span></div>
 <div style={{...base,top:p?h*.42:h*.47,display:'flex',flexDirection:p?'column':'row',gap:p?36:100}}>
 {metric('Accuracy','99%','99 correct out of 100 emails',C.TEAL)}
 <div style={{flex:1,opacity:enter(at('recall',4))}}>{metric('Spam recall','0%','0 caught out of 1 actual spam',C.INK)}</div>
 </div>
 {source('Source: scikit-learn · recall_score')}
 </>}
 {beat==='B06'&&<>
 {title('Ask Which Mistakes Matter')}
 <div style={{...base,top:h*.3,display:'flex',flexDirection:p?'column':'row',gap:60}}>
 {metric('Correct overall','99%','99 out of 100 emails',C.TEAL)}
 {metric('Spam caught','0 of 1','The important miss remains',C.INK)}
 </div>
 <div style={{...base,top:p?h*.73:h*.72,fontSize:p?48:50,opacity:enter(at('which',4))}}>Check the categories. Check the errors.</div>
 </>}
 {beat==='B08'&&<>
 <div style={{...base,top:h*.13,fontFamily:sans,fontSize:p?44:42}}>Humanitarians AI</div>
 <div style={{...base,top:h*.3,fontSize:p?96:120,lineHeight:1.12}}>Why 99% Accuracy<br/>Can Be Misleading</div>
 <div style={{...base,top:p?h*.62:h*.64,fontSize:p?56:58}}>Deepa Shenoy</div>
 <div style={{...base,top:p?h*.69:h*.73,...label}}>AI narration: Liam for Deepa</div>
 </>}
 {footer}
 </AbsoluteFill>;
};
