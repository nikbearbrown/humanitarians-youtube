import React,{useEffect,useState} from 'react';
import {AbsoluteFill,Composition,registerRoot,useCurrentFrame,useVideoConfig,staticFile,delayRender,continueRender} from 'remotion';
import sheet from '../../beat_sheet.json';
import captions from '../../captions.json';
const P={paper:'#F4F0E5',ink:'#302E27',rust:'#B34D32',sage:'#38685B',gold:'#DDA451',line:'#CFC6B4',soft:'#6C6558'};
const E=(n:number)=>1-Math.pow(1-Math.max(0,Math.min(1,n)),3);
const Txt:React.FC<any>=({x,y,children,size=28,fill=P.ink,serif=false,...rest})=><text x={x} y={y} fill={fill} fontFamily={serif?'Editorial':'Montserrat'} fontSize={size} {...rest}>{children}</text>;
const Tag:React.FC<any>=({x,y,w=300,children,color=P.rust})=><g><rect x={x} y={y-31} width={w} height={48} rx={3} fill={color}/><Txt x={x+16} y={y} size={22} fill="#fff">{children}</Txt></g>;
const Plant=({x,y,s=1}:{x:number;y:number;s?:number})=><g transform={`translate(${x},${y}) scale(${s})`}><path d="M-33 0L-22 75H22L33 0" fill="#AC654C"/><path d="M0 0V-160M0-40Q-70-130-90-90Q-50-30 0-40M0-85Q75-160 85-110Q50-70 0-85M0-110Q-40-200-52-165Q-48-110 0-110" fill={P.sage} stroke="#294D43" strokeWidth={4}/></g>;
function RobotRoom({t}:{t:number}){
 const turn=E((t-1)/4);return <g clipPath="url(#roomclip)"><defs><clipPath id="roomclip"><rect y={20} width={1100} height={830}/></clipPath></defs>
 <rect x={0} y={20} width={1100} height={760} fill="#E2D5BB"/>
 <path d="M0 20H1100V480H0Z" fill="#EBE1CD"/><path d="M0 480H1100V850H0Z" fill="#C79C70"/>
 {Array.from({length:8},(_,i)=><path key={i} d={`M${550+(i-4)*100} 480L${550+(i-4)*350} 850`} stroke="#B78B62" strokeWidth={3}/>)}
 {[530,600,700,820].map(y=><path key={y} d={`M0 ${y}H1100`} stroke="#A77D57" strokeWidth={3}/>)}
 <g transform={`translate(${Math.sin(t*.3)*3},0)`}><rect x={660} y={55} width={340} height={300} fill="#AFC8BF" stroke="#FAF4E6" strokeWidth={22}/><circle cx={900} cy={120} r={45} fill="#F1CE87"/><path d="M660 310L720 210L780 260L870 165L1000 280V345H660" fill="#688C7D"/><path d="M830 50V355M660 200H1000" stroke="#FAF4E6" strokeWidth={14}/></g>
 <path d="M690 355L1020 355L1100 680L470 680Z" fill="#FFF6D7" opacity={.22}/>
 <rect x={70} y={110} width={205} height={145} fill="#695446"/><rect x={84} y={124} width={177} height={117} fill="#EEE9D8"/><path d="M90 225L130 150L180 218L230 172L250 227" fill="#B77D56"/>
 <g transform="translate(80 375)"><rect x={0} y={-30} width={390} height={180} rx={45} fill="#728376"/><rect x={-20} y={35} width={90} height={125} rx={25} fill="#536E62"/><rect x={320} y={35} width={90} height={125} rx={25} fill="#536E62"/><path d="M60 150H330" stroke="#3D5B4D" strokeWidth={7}/><rect x={90} y={15} width={100} height={90} rx={12} fill="#B28A60" transform="rotate(-8 140 60)"/><rect x={220} y={15} width={90} height={90} rx={12} fill="#DDD1AE"/><path d="M20 160V190M370 160V190" stroke="#493D30" strokeWidth={14}/></g>
 <Plant x={1010} y={440} s={1.2}/>
 <ellipse cx={465} cy={710} rx={340} ry={100} fill="#B66E4F" opacity={.3}/>
 {[[130,650],[270,720],[420,590],[580,770],[850,690],[960,750]].map(([x,y],i)=><g key={i} transform={`translate(${x},${y}) rotate(${i*31})`}><ellipse cx={5} cy={18} rx={44} ry={13} fill="#76513B" opacity={.18}/>{i%2?<><path d="M-30-20L35-10L24 26L-28 15Z" fill="#F7EEDD"/><path d="M-20-9L20-3M-18 0L17 8" stroke="#BCB39F" strokeWidth={3}/></>:<><rect x={-27} y={-15} width={64} height={38} rx={3} fill={i%3?P.rust:P.sage}/><path d="M-25 15H36" stroke="#FAE4C8" strokeWidth={6}/></>}</g>)}
 <path d="M710 485H985L1040 600H720Z" fill="#EFE3BC" stroke="#7A8F66" strokeWidth={4} strokeDasharray="10 8"/>
 <g transform={`translate(${580+Math.sin(t*.5)*8},620)`}>
 <path d={`M0-90L${120+turn*160} -${30+turn*95}L${160+turn*230} -${20+turn*10}Z`} fill="#FBE8A2" opacity={.4}/>
 <ellipse cy={50} rx={112} ry={40} fill="#4D4033" opacity={.2}/><ellipse cy={20} rx={110} ry={55} fill="#667370"/><path d="M-110-12V23Q0 95 110 23V-12" fill="#83928B"/><ellipse cy={-12} rx={110} ry={52} fill="#EEEBDD" stroke="#415B52" strokeWidth={5}/>
 <rect x={-73} y={-122} width={146} height={94} rx={37} fill="#F6F0DC" stroke="#415B52" strokeWidth={5}/><rect x={-54} y={-100} width={108} height={47} rx={19} fill="#314D46"/>
 <circle cx={-24} cy={-78} r={8} fill="#EBD39B"/><circle cx={24} cy={-78} r={8} fill="#EBD39B"/>
 <g transform={`translate(65,-115) rotate(${-30*turn})`}><rect x={-15} y={-25} width={55} height={42} rx={9} fill={P.rust}/><circle cx={41} cy={-5} r={16} fill="#2E4039" stroke="#D8D8BD" strokeWidth={5}/></g>
 </g><Txt x={40} y={815} size={25}>The room is still messy.</Txt>
 </g>;
}
function Dog({x,y,s=1}:{x:number;y:number;s?:number}){return <g transform={`translate(${x},${y}) scale(${s})`}>
 <ellipse cx={0} cy={100} rx={135} ry={20} fill="#33483D" opacity={.18}/><path d="M-110-15Q-55-70 55-35L80-110L128-135L150-82L190-57L180-30L128-15L100 35L80 100H54L55 22L-45 20L-65 100H-95L-85 5L-130-25Q-195-75-180-118Q-135-90-110-15Z" fill="#705C4A"/>
 <path d="M80-110L94-63L122-87L140-56L125-22L92 9L64-10Z" fill="#EADCC4"/><path d="M-45 20L54 22L80 65L54 65L25 17" fill="#F6E9D1"/><path d="M83-113L86-153L114-132M123-128L145-156L148-85" fill="#4B453C"/><circle cx={141} cy={-71} r={5} fill="#191E19"/><circle cx={185} cy={-55} r={8} fill="#272D25"/>
 </g>}
function Landscape({snow,t,w=740,h=650}:{snow:boolean;t:number;w?:number;h?:number}){return <svg width={w} height={h} viewBox="0 0 740 650">
 <rect width={740} height={650} fill={snow?'#DDE7DE':'#E8D5A4'}/><circle cx={590} cy={95} r={55} fill="#F7EAD1"/>
 <g transform={`translate(${Math.sin(t*.2)*5},0)`}><path d="M-20 330L150 95L330 320L480 135L780 350V650H0Z" fill={snow?'#9CAFA5':'#9B9F71'}/><path d="M100 170L150 95L205 170L165 150L143 170Z M425 210L480 135L540 218L478 195Z" fill="#F6F3E7"/></g>
 <path d="M0 370Q180 280 380 385Q570 305 740 375V650H0Z" fill={snow?'#C6D5C9':'#718B5C'}/>
 {[30,100,600,685].map((x,i)=><g key={i} transform={`translate(${x+Math.sin(t*.4+i)*2},${320+i%2*70})`}><path d="M0-135L-60 0H-40L-80 60H80L40 0H60Z" fill={snow?'#496A59':'#395A43'}/><path d="M0 0V130" stroke="#685644" strokeWidth={14}/>{snow&&<path d="M0-135L-35-55H35Z" fill="#E9F1E7"/>}</g>)}
 <path d="M0 500Q250 410 440 500Q600 440 740 500V650H0Z" fill={snow?'#F4F2E6':'#A9A96F'}/>
 <Dog x={345} y={455} s={1.1}/>
 {snow?Array.from({length:32},(_,i)=><circle key={i} cx={(i*93+t*9)%740} cy={(i*57+t*18)%640} r={i%3+2} fill="#fff" opacity={.75}/>):Array.from({length:22},(_,i)=><path key={i} d={`M${i*37} 625l${Math.sin(t+i)*4} -${18+i%4*8}`} stroke="#5F7445" strokeWidth={3}/>)}
 <path d={`M135 ${340+(t*22)%200}H570`} stroke={P.rust} strokeWidth={3} opacity={.65}/><path d="M130 300V275H165M550 275H585V300M130 555V580H165M550 580H585V555" fill="none" stroke={P.rust} strokeWidth={4}/>
 </svg>}
function HorseWorld({t}:{t:number}){return <svg viewBox="0 0 1100 850" width="100%" height="100%"><rect width={1100} height={850} fill="#DDCEAE"/>
 <path d="M0 590Q300 500 550 590T1100 570V850H0Z" fill="#B1AD87"/>
 {[90,270,490,720,950].map(x=><g key={x}><path d={`M${x} 500V690`} stroke="#8A7456" strokeWidth={18}/></g>)}<path d="M0 540H1100M0 610H1100" stroke="#AD9370" strokeWidth={16}/>
 <path d="M0 150H1100M0 170H1100" stroke="#BBA785" strokeWidth={2}/><Txt x={55} y={115} serif size={52}>Clever Hans / a closer look</Txt>
 <g transform="translate(430 430)"><ellipse cy={240} rx={250} ry={30} fill="#74654B" opacity={.2}/><path d="M-210-50Q-100-130 80-65L135-230L195-250L250-180L230-135L177-125L135 35L85 90L55 230H16L25 75L-120 70L-150 230H-190L-175 20L-220-45Q-300 20-290 160L-315 150Q-310-65-210-50Z" fill="#77553B" stroke="#4F402F" strokeWidth={5}/><path d="M135-230L140-280L168-250M178-248L200-284L205-230" fill="#4B3D2B"/><path d="M80-65L135-230L155-245" stroke="#42382C" strokeWidth={22}/><circle cx={218} cy={-194} r={6} fill="#161B15"/><path d={`M-130 70L${-105+Math.sin(t*6)*20} ${205+Math.sin(t*6)*18}H-145L-165 55`} fill="#9F7450" stroke="#4F402F" strokeWidth={5}/></g>
 <g transform={`translate(875,${350+Math.sin(t*1.2)*5})`}><circle cy={-70} r={36} fill="#C18C65"/><path d="M-50-89H50M-32-90V-135H31V-90" stroke="#3F4138" strokeWidth={15}/><path d="M-35-25L-55 150H55L35-25Z" fill="#424E44"/><path d="M-20 150L-30 310M20 150L40 310" stroke="#494738" strokeWidth={28}/><path d="M-35 0L-85 100" stroke="#424E44" strokeWidth={24}/></g>
 <path d="M820 270Q720 230 655 270" fill="none" stroke={P.rust} strokeWidth={4} strokeDasharray="9 9"/><Tag x={650} y={205} w={360}>SUBTLE HUMAN CUES</Tag><Txt x={60} y={790} size={25}>Original illustration • Pfungst, 1911</Txt></svg>}
function PipelineWorld({t}:{t:number}){const names=['Anjana N. · 4','Tanmay K. · 4','Om M. · 4','Mohammed S. · 3','Uday S. · 2'];const travel=E((t-1)/4);return <svg viewBox="0 0 1100 850" width="100%" height="100%"><rect width={1100} height={850} fill="#DED7C5"/><path d="M0 0H1100V460H0Z" fill="#E9DFCE"/>{Array.from({length:12},(_,i)=><path key={i} d={`M0 ${80+i*60}H1100`} stroke="#C8BDA7" strokeWidth={1} opacity={.5}/>)}
<Txt x={50} y={65} size={26} fill={P.sage}>WEEK 9 / CONTRIBUTOR COLLECTION</Txt>
{names.map((n,i)=><g key={n} transform={`translate(${45+i*207},${110+Math.sin(t*.8+i)*4}) rotate(${(i-2)*2})`}><rect x={6} y={8} width={182} height={165} fill="#A99A7E" opacity={.25}/><rect width={182} height={165} rx={3} fill="#FBF7EB"/><rect x={13} y={13} width={156} height={95} fill={i%2?'#A3B1A0':'#CBA57E'}/><circle cx={91} cy={60} r={24} fill="#F6EDDA"/><path d="M85 47L104 60L85 74Z" fill={P.rust}/><Txt x={12} y={139} size={18}>{n}</Txt><path d={`M91 185V220L${550-(45+i*207)} 255`} fill="none" stroke="#AA9475" strokeWidth={2} strokeDasharray="7 7"/></g>)}
<ellipse cx={545} cy={660} rx={370} ry={64} fill="#9D8C6A" opacity={.18}/><path d="M180 700L920 700L1020 790H80Z" fill="#AD8C66"/><path d="M80 790H1020V825H80Z" fill="#8E7051"/>
<g transform={`translate(${160+travel*420},${470-Math.sin(travel*Math.PI)*70}) rotate(${-8+travel*8})`}><rect x={8} y={10} width={340} height={210} fill="#74624A" opacity={.17}/><rect width={340} height={210} fill="#FFF9E9" stroke="#BEB198" strokeWidth={3}/><path d="M0 0L170 120L340 0" fill="#E8DBC1" stroke="#BEB198" strokeWidth={3}/><Tag x={28} y={154} w={285} color={P.sage}>TITLE + DESCRIPTION</Tag></g>
<g transform={`translate(770,${Math.max(0,1-E((t-3)/1))*-80})`}><rect x={0} y={342} width={180} height={95} rx={5} fill={P.rust}/><rect x={55} y={295} width={70} height={60} rx={14} fill="#713E2C"/><Txt x={16} y={400} size={22} fill="#FFF7E8">FOR REVIEW</Txt></g>
<Txt x={58} y={400} serif size={48}>Package the evidence.</Txt><Txt x={58} y={445} size={25}>Keep the decision with the reviewer.</Txt><Txt x={60} y={752} size={24} fill={P.ink}>17 submissions • titles and descriptions prepared</Txt>
</svg>}

function Workspace({t,week,pipeline=false}:{t:number;week:number;pipeline?:boolean}){
 const names=week===8?['Tanmay K. · 4','Anjana N. · 4','Mohammed S. · 4','Uday S. · 2']:['Anjana N. · 4','Tanmay K. · 4','Om M. · 4','Mohammed S. · 3','Uday S. · 2'];
 return <svg viewBox="0 0 1100 850" width="100%" height="100%">
 <rect width={1100} height={850} fill="#E5DCC8"/><rect x={0} y={70} width={1100} height={500} fill="#EDE7DA"/>
 <path d="M60 560H1040L1100 850H0Z" fill="#C6AA84"/>{[630,720,820].map(y=><path key={y} d={`M0 ${y}H1100`} stroke="#B7956B" strokeWidth={3}/>)}
 <Plant x={1020} y={570} s={.8}/><path d="M50 530L100 130L310 150" fill="none" stroke="#696C59" strokeWidth={18}/><path d="M210 140Q290 30 370 155Z" fill={P.sage}/><path d="M230 150L410 500L70 500Z" fill="#FFEFBB" opacity={.15}/>
 <g transform={`translate(135,${190-Math.sin(t*.4)*3})`}><rect x={16} y={18} width={820} height={435} rx={15} fill="#796E5D" opacity={.22}/><rect width={820} height={435} rx={15} fill="#FAF8F1" stroke="#393C33" strokeWidth={12}/><path d="M0 56H820" stroke="#D5CEBD" strokeWidth={2}/><circle cx={28} cy={28} r={7} fill={P.rust}/><circle cx={53} cy={28} r={7} fill={P.gold}/><circle cx={78} cy={28} r={7} fill={P.sage}/><Txt x={115} y={36} size={21}>Illustrative metadata workspace</Txt>
 <rect x={24} y={88} width={215} height={145} rx={3} fill="#DCCBB1"/><path d="M24 195L85 130L140 178L206 120L239 190V233H24" fill="#9C9B72"/><circle cx={110} cy={155} r={32} fill="#F9F4E8"/><path d="M103 139L125 155L103 172Z" fill={P.rust}/><Txt x={28} y={270} size={20}>VIDEO PREVIEW</Txt>
 <Txt x={280} y={105} size={21} fill={P.soft}>{pipeline?'REVIEW PACKAGE':'TITLE / EDITING'}</Txt><rect x={270} y={123} width={510} height={65} fill="#fff" stroke={P.rust} strokeWidth={2}/><Txt x={289} y={165} size={23}>{(pipeline?'Title + description prepared':'Clear subject → specific focus').slice(0,Math.floor(8+t*5))}</Txt>
 <Txt x={280} y={225} size={21} fill={P.soft}>DESCRIPTION</Txt>{['Summarize the subject.','Explain the educational purpose.','Identify the key concepts.'].map((l,i)=><Txt key={l} x={280} y={262+i*35} size={22} opacity={E((t-i*.5)/.8)}>{l.slice(0,Math.floor(Math.max(0,t-i*.5)*15))}</Txt>)}
 <rect x={560} y={365} width={215} height={42} rx={4} fill={P.sage}/><Txt x={575} y={394} size={20} fill="#fff">{pipeline?'Sent for review':'Prepare for review'}</Txt>
 <path d={`M${650+Math.sin(t*.6)*60} ${350+Math.cos(t*.7)*20}l28 28 -18 1 -8 19Z`} fill={P.ink} stroke="#fff" strokeWidth={3}/></g>
 <path d="M485 630H610L630 685H465Z" fill="#5D6052"/><ellipse cx={550} cy={695} rx={155} ry={20} fill="#5D6052"/>
 <g transform={`translate(${70+Math.sin(t*.5)*6},675) rotate(-9)`}><rect width={240} height={130} rx={3} fill="#FAF6E8" stroke="#B6A68B" strokeWidth={2}/><Txt x={18} y={38} size={17}>CONTRIBUTOR QUEUE</Txt>{names.slice(0,3).map((n,i)=><Txt key={n} x={18} y={68+i*25} size={18}>{n}</Txt>)}</g>
 <g transform="translate(830 715)"><ellipse cy={60} rx={55} ry={16} fill="#7E6E53" opacity={.25}/><path d="M-40-20V35Q0 75 40 35V-20" fill="#EEE8D6" stroke="#A89F8C" strokeWidth={3}/><ellipse cy={-20} rx={40} ry={14} fill="#695340"/><path d="M42-5Q90-5 65 32H40" fill="none" stroke="#EEE8D6" strokeWidth={13}/></g>
 </svg>;
}
const Preview=({kind='main'}:{kind?:string})=>{
 const frame=useCurrentFrame(),{width,height,fps}=useVideoConfig(),t=frame/fps,p=height>width;
 const [gate]=useState(()=>delayRender('Editorial fonts'));
 useEffect(()=>{Promise.all([['Montserrat-Medium.ttf','Montserrat','500'],['Montserrat-Bold.ttf','Montserrat','700'],['EBGaramond-Regular.ttf','Editorial','400']].map(async([file,family,weight])=>{const f=new FontFace(family,`url(${staticFile('fonts/'+file)})`,{weight});await f.load();document.fonts.add(f)})).then(()=>continueRender(gate))},[]);
 const week=sheet.metadata.week,stem=sheet.metadata.category==='STEM';const beat=sheet.beats[stem?(week===8?2:kind==='horse'?1:3):(week===8?3:5)];const offset=beat.start_s+2;const cue=captions.find(c=>(offset+t)*1000>=c.startMs&&(offset+t)*1000<c.endMs);
 const title=stem?(week===8?'A perfect score. A messy room.':kind==='horse'?'Watch the cue, not the count.':'Same dog. Different background.'):(week===8?'From submission to story.':'Prepared. Submitted. Decision pending.');
 const heroX=p?65:100,heroY=p?340:245,heroW=p?950:1720,heroH=p?1140:600;
 return <AbsoluteFill style={{background:P.paper,color:P.ink,fontFamily:'Montserrat',overflow:'hidden'}}>
 <svg width={width} height={height} style={{position:'absolute',inset:0}}><defs><pattern id="paper" width={13} height={13} patternUnits="userSpaceOnUse"><path d="M1 2h1M8 10h1" stroke="#A99C81" strokeWidth={.7} opacity={.14}/></pattern></defs><rect width="100%" height="100%" fill="url(#paper)"/><path d={`M${width*.55} 0L${width} 0V${height*.55}Z`} fill="#E9E1D1"/></svg>
 <div style={{position:'absolute',left:p?65:100,right:p?65:100,top:p?105:60,display:'flex',justifyContent:'space-between',fontSize:24,color:P.sage,fontWeight:700}}><span>HUMANITARIANS AI</span><span>DEEPA S. / WEEK {week}</span></div>
 <div style={{position:'absolute',left:p?65:100,top:p?155:107,right:80,fontFamily:'Editorial',fontSize:p?76:83,lineHeight:1.02}}>{title}</div>
 <div style={{position:'absolute',left:heroX,top:heroY,width:heroW,height:heroH}}>
 {stem&&week===8?<svg width="100%" height="100%" viewBox={p?'0 0 950 1230':'0 0 1720 650'}>
 <svg x={0} y={0} width={p?950:1120} height={p?850:650} viewBox="0 0 1100 850"><g transform={`translate(${Math.sin(t*.3)*4},0)`}><RobotRoom t={t}/></g></svg>
 <g transform={`translate(${p?20:1180},${p?900:70})`}><Tag x={0} y={0} w={p?420:400}>HYPOTHETICAL EXAMPLE</Tag><Txt x={0} y={85} serif size={p?55:55}>What the camera sees</Txt><rect x={0} y={110} width={p?380:400} height={p?160:220} fill="#E9D9B4" stroke={P.sage} strokeWidth={3}/><path d={p?'M0 190H380M190 110V270':'M0 220H400M200 110V330'} stroke="#C8AE86" strokeWidth={3}/><Txt x={p?430:0} y={p?155:405} size={24} fill={P.sage}>REWARD SIGNAL</Txt><Txt x={p?430:0} y={p?230:480} size={p?65:78} fill={P.sage} fontWeight={700}>HIGH</Txt><Txt x={p?430:0} y={p?280:535} size={24}>Cleaning is not established.</Txt></g></svg>:
 stem&&kind==='horse'?<HorseWorld t={t}/>:
 stem?<svg width="100%" height="100%" viewBox={p?'0 0 950 1230':'0 0 1720 650'}><svg x={0} y={0} width={p?950:835} height={p?540:590} viewBox="0 0 740 650"><Landscape snow={false} t={t}/></svg><svg x={p?0:885} y={p?630:0} width={p?950:835} height={p?540:590} viewBox="0 0 740 650"><Landscape snow t={t}/></svg><Tag x={p?140:100} y={p?560:620} w={p?660:625} color={P.sage}>ILLUSTRATION / PREDICTION: DOG</Tag><Tag x={p?140:985} y={p?1190:620} w={p?660:625}>SHORTCUT PREDICTION: WOLF</Tag></svg>:
 <svg width="100%" height="100%" viewBox={p?'0 0 950 1230':'0 0 1720 650'}><svg x={0} y={0} width={p?950:1120} height={p?850:650} viewBox="0 0 1100 850">{week===9?<PipelineWorld t={t}/>:<Workspace t={t} week={week}/>}</svg><g transform={`translate(${p?30:1180},${p?900:80})`}><Txt x={0} y={0} serif size={53}>{week===8?'14 submissions':'17 submissions'}</Txt><Txt x={0} y={45} size={22} fill={P.soft}>Deepa’s reported work</Txt>{['Prepared','Submitted for review','Approval not confirmed'].map((n,i)=><g key={n} transform={`translate(${p?i*300:0},${p?110:125+i*120})`} opacity={E((t-i*.3)/.8)}><circle cx={25} cy={0} r={23} fill={i<2?P.sage:P.paper} stroke={i<2?P.sage:P.rust} strokeWidth={3}/><Txt x={25} y={9} size={23} textAnchor="middle" fill={i<2?'#fff':P.rust}>{i<2?i+1:'?'}</Txt><Txt x={p?0:65} y={p?65:9} size={p?20:25}>{n}</Txt>{i<2&&!p&&<path d="M25 30V88" stroke={P.sage} strokeWidth={3} strokeDasharray="5 6"/>}</g>)}</g></svg>}
 </div>
 <div style={{position:'absolute',left:p?65:100,top:p?1508:855,fontSize:p?23:21,color:P.soft}}>{stem?(week===8?'Original robot example • Concepts: DeepMind, 2020':kind==='horse'?'Pfungst, 1911 • Original historical illustration':'Illustrative classification • Ribeiro et al., 2016'):'Illustrative interface • no invented contributor titles'}</div>
 {cue&&<div style={{position:'absolute',left:p?65:100,right:p?65:100,bottom:p?165:85,background:'#F4F0E5F5',borderTop:'2px solid '+P.line,padding:'16px 0',fontSize:p?29:29,lineHeight:1.35,textAlign:'center'}}>{cue.text}</div>}
 <div style={{position:'absolute',left:p?65:100,right:p?65:100,bottom:p?110:57,fontSize:p?21:20,display:'flex',justifyContent:'space-between',color:P.sage}}><span>@HumanitariansAI</span><span>VISUAL DRAFT • APPROVAL PENDING</span></div>
 </AbsoluteFill>;
};
registerRoot(()=> <><Composition id="LandscapeDraft" component={Preview} width={1920} height={1080} fps={24} durationInFrames={144}/><Composition id="PortraitDraft" component={Preview} width={1080} height={1920} fps={24} durationInFrames={144}/><Composition id="HorseDraft" component={Preview} defaultProps={{kind:'horse'}} width={1920} height={1080} fps={24} durationInFrames={144}/></>);
