import React, {useEffect, useState} from 'react';
import {AbsoluteFill, Img, staticFile, delayRender, continueRender, useCurrentFrame, useVideoConfig, interpolate} from 'remotion';
import {z} from 'zod';
import {HUMANITARIANS as C} from '../tokens/humanitarians';

export const deepaWeek2SetupSchema=z.object({beat:z.string(),frames:z.number(),audit:z.boolean().optional()});
/** Reuses Deepa's HAI palette, bundled fonts, wordmark and native-layout card/outro system. */
export const DeepaWeek2Setup:React.FC<z.infer<typeof deepaWeek2SetupSchema>>=({beat,audit=false})=>{
 const f=useCurrentFrame();const {width:w,height:h}=useVideoConfig();const p=h>w;
 const [gate]=useState(()=>delayRender('HAI fonts and layout'));
 useEffect(()=>{Promise.all([['EB Garamond','EBGaramond-Regular.ttf'],['Montserrat','Montserrat-Medium.ttf']].map(async([name,file])=>{const face=new FontFace(name,`url(${staticFile('fonts/'+file)})`);await face.load();(document.fonts as any).add(face);})).then(()=>requestAnimationFrame(()=>requestAnimationFrame(()=>{
  if(audit){const root=document.querySelector('[data-setup-root]')!;const rr=root.getBoundingClientRect();const sx=w/rr.width,sy=h/rr.height;const rows=Array.from(root.querySelectorAll('[data-qc]')).map((el)=>{const r=el.getBoundingClientRect(),s=getComputedStyle(el);return {text:el.textContent,x:(r.x-rr.x)*sx,y:(r.y-rr.y)*sy,w:r.width*sx,h:r.height*sy,font:parseFloat(s.fontSize),color:s.color,background:s.backgroundColor,scrollOverflow:(el as HTMLElement).scrollWidth>(el as HTMLElement).clientWidth+2};});console.log('DEEPA_QC '+JSON.stringify({beat,portrait:p,width:w,height:h,rows}));}
  continueRender(gate);
 })));},[gate]);
 const show=(delay=0)=>interpolate(f,[delay,delay+12],[0,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp'});
 const X=w*.08,W=w*.84;const serif='EB Garamond, Georgia, serif',sans='Montserrat, Arial, sans-serif';
 const label=p?72:48,body=p?84:66,title=p?104:96;
 const txt=(text:string,size=body,color=C.INK,extra:React.CSSProperties={})=><div data-qc style={{fontSize:size,lineHeight:1.16,color,fontFamily:serif,overflowWrap:'break-word',...extra}}>{text}</div>;
 const small=(text:string,color=C.SLATE)=>txt(text,label,color,{fontFamily:sans,fontWeight:500});
 const box=(children:React.ReactNode,delay=0,extra:React.CSSProperties={})=><div style={{padding:p?34:38,border:`3px solid ${C.SLATE}`,borderRadius:18,background:'#FFFCF5',boxSizing:'border-box',opacity:show(delay),transform:`translateY(${(1-show(delay))*14}px)`,...extra}}>{children}</div>;
 const stack:React.CSSProperties={display:'flex',flexDirection:'column',gap:p?26:30};
 const grid=(count:number):React.CSSProperties=>({display:'grid',gridTemplateColumns:`repeat(${count},minmax(0,1fr))`,gap:p?24:30});
 const head=(text:string)=><div style={{position:'absolute',left:X,right:X,top:h*(p?.155:.19)}}>{txt(text,title,C.INK,{fontWeight:600})}</div>;
 let content:React.ReactNode;
 switch(beat){
 case 'B00':content=<>
  <div style={{position:'absolute',left:X,right:X,top:h*(p?.22:.17)}}>{txt('Setting Up My',p?100:100)}{txt('Brutalist',p?138:150,C.TEAL,{fontWeight:600})}{txt('Film-as-Code Environment',p?96:100)}</div>
  <div style={{position:'absolute',left:X,right:X,top:h*(p?.57:.57)}}>{box(<>{small('MY MAC · MY SETUP')}{txt('Learning an existing workflow',p?86:72,C.INK,{marginTop:18})}{small('AI narration: Liam for Deepa',C.SLATE)}</>,18)}</div>
 </>;break;
 case 'B01':{
 const steps=f<90?['Repository','Prerequisites','Environment','Dependencies']:['Problem / fix','Codex','Brutalist CLI','Ready'];
 content=<>{head('From setup to production')}<div style={{position:'absolute',left:X,right:X,top:h*(p?.285:.43),...grid(p?1:4),gap:p?14:30}}>{steps.map((s,i)=><React.Fragment key={s}>{box(<>{small(String(i+1+(f<90?0:4)).padStart(2,'0'),C.TEAL)}{txt(s,p?76:60,C.INK,{marginTop:p?4:12})}</>,f<90?i*10:90+i*8,{padding:p?20:38})}</React.Fragment>)}</div></>;break;}
 case 'B02':content=<>{head('The existing repository')}<div style={{position:'absolute',left:X,right:X,top:h*(p?.31:.30),...stack,gap:p?26:12}}>{box(<>{small('Downloaded + extracted')}{txt('Brutalist.art',p?96:90,C.TEAL,{marginTop:16})}</>)}<div style={grid(3)}>{['skills','runtime','fellows'].map((s,i)=><React.Fragment key={s}>{box(txt(s,p?54:64,C.INK,{fontFamily:sans,whiteSpace:'nowrap'}),20+i*12,{padding:p?'20px 8px':36,textAlign:'center'})}</React.Fragment>)}</div>{box(<>{small('Reviewed video builders')}{txt('ai-explainer · cli-explainer',p?70:66,C.INK,{marginTop:12})}</>,52,{padding:p?34:18})}</div></>;break;
 case 'B03':content=<>{head('A project environment')}<div style={{position:'absolute',left:X,right:X,top:h*.32,...stack}}><div style={grid(3)}>{['Python','Git','Node'].map((s,i)=><React.Fragment key={s}>{box(txt(s,p?68:68,C.TEAL,{textAlign:'center',fontFamily:sans}),i*10,{padding:p?'28px 8px':32})}</React.Fragment>)}</div>{box(<>{small('Python 3.12')}{txt('.venv',p?120:106,C.TEAL,{fontFamily:sans,marginTop:16})}{txt('Required Python dependencies',p?82:66,C.INK,{marginTop:26})}</>,40,{borderWidth:5})}</div></>;break;
 case 'B04':content=<>{head('Resolving the Manim setup')}<div style={{position:'absolute',left:X,right:X,top:h*(p?.34:.32),...stack}}>{box(<>{small('THE ISSUE')}{txt('Additional dependencies needed',p?82:74,C.INK,{marginTop:16})}</>,0,{padding:p?34:18})}<div style={grid(2)}>{['Pango','pkg-config'].map((s,i)=><React.Fragment key={s}>{box(<>{small('Installed',C.TEAL)}{txt(s,p?74:84,C.INK,{marginTop:20})}</>,40+i*14,{borderColor:C.TEAL,padding:p?34:18})}</React.Fragment>)}</div>{box(txt('Setup could continue',p?86:76,C.TEAL),78,{padding:p?34:18})}</div></>;break;
 case 'B05':content=<>{head('My coding agent')}<div style={{position:'absolute',left:X,right:X,top:h*(p?.32:.42),...grid(p?1:2)}}>{box(<>{small('Installed + configured')}{txt('OpenAI Codex',p?100:94,C.TEAL,{marginTop:26})}</>)}{box(<>{small('USED WITH')}{txt('My Brutalist workspace',p?100:86,C.INK,{marginTop:26})}</>,34)}</div></>;break;
 case 'B06':content=<>{head('Checking the Brutalist CLI')}<div style={{position:'absolute',left:X,right:X,top:h*(p?.32:.315),...stack}}>{box(<>{txt('./art --list',p?98:106,C.TEAL,{fontFamily:'monospace',whiteSpace:'nowrap'})}<div style={{height:p?30:24}}/>{small('Current verification — excerpt')}{txt('Builder names',label,C.SLATE,{fontFamily:sans,marginTop:24})}<div style={{...stack,marginTop:24,gap:p?30:16}}>{['ai-explainer','cli-explainer','fellows'].map((s,i)=><div key={s} style={{opacity:show(35+i*16)}}>{txt(s,p?82:64,C.INK,{fontFamily:'monospace'})}</div>)}</div></>,0,{padding:p?34:16})}</div></>;break;
 case 'B07':content=<>{head('Ready to make videos')}<div style={{position:'absolute',left:X,right:X,top:h*(p?.31:.39),...stack}}>{box(<>{small('ENVIRONMENT WORKING',C.TEAL)}{txt('Next: creating and reviewing',p?82:84,C.INK,{marginTop:18})}</>)}<div style={grid(p?2:4)}>{['Planning','Narration','Visuals','Review'].map((s,i)=><React.Fragment key={s}>{box(txt(s,p?72:64,C.INK,{textAlign:'center'}),30+i*16,{padding:p?'42px 12px':32})}</React.Fragment>)}</div></div></>;break;
 default:content=<><div style={{position:'absolute',left:X,right:X,top:h*.24}}>{txt('Setting Up My',p?108:112)}{txt('Brutalist',p?138:156,C.TEAL,{fontWeight:600})}{txt('Film-as-Code Environment',p?102:104)}</div><div style={{position:'absolute',left:X,right:X,top:h*(p?.63:.67),...stack}}>{txt('Deepa Shenoy',p?106:96)}{small('AI narration: Liam for Deepa')}</div></>;
 }
 return <AbsoluteFill data-setup-root style={{background:C.CREAM,color:C.INK,fontFamily:serif}}>
 <div style={{position:'absolute',left:X,right:X,top:h*.075,display:'flex',justifyContent:'space-between',gap:24}}>{small('Deepa Shenoy')}{small('WEEK 2',C.TEAL)}</div>
 {content}
 <div style={{position:'absolute',left:X,right:X,top:h*(p?.88:.895),display:'flex',flexDirection:p?'column':'row',alignItems:p?'flex-start':'center',justifyContent:'space-between',gap:p?20:24}}>
 {txt('@HumanitariansAI',p?66:48,C.INK,{fontFamily:sans})}<Img src={staticFile('hai-wordmark-outlined.svg')} style={{width:p?400:420,height:p?42:48,objectFit:'contain',objectPosition:'left'}}/>
 </div>
 </AbsoluteFill>;
};
