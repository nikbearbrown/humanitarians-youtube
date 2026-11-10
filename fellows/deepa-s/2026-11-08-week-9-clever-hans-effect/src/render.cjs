const fs=require('fs'),path=require('path'),cp=require('child_process');
const p=path.resolve(process.argv[2]||path.join(__dirname,'..'));
const modules=process.env.REMOTION_MODULES||path.join(process.env.HOME,'Downloads/brutalist.art-main/runtime/remotion/node_modules');
const {bundle}=require(modules+'/@remotion/bundler');
const {selectComposition,renderStill,renderMedia}=require(modules+'/@remotion/renderer');
const browserExecutable=process.env.CHROME_BIN||modules+'/.remotion/chrome-headless-shell/mac-arm64/chrome-headless-shell-mac-arm64/chrome-headless-shell';
(async()=>{
const serveUrl=await bundle({entryPoint:p+'/src/Root.tsx',outDir:p+'/_qc/redesigned-final/bundle',publicDir:p+'/public',webpackOverride:c=>({...c,resolve:{...c.resolve,modules:[modules,...(c.resolve.modules||[])]},resolveLoader:{...c.resolveLoader,modules:[modules,'node_modules']}})});
const s=JSON.parse(fs.readFileSync(p+'/beat_sheet.json'));
fs.mkdirSync(p+'/_qc/redesigned-final/previews',{recursive:true});
for(const id of ['Landscape','Portrait']){
const composition=await selectComposition({serveUrl,id,browserExecutable});
console.log(JSON.stringify(composition));
if(process.argv.includes('--preview')){
for(let i=0;i<s.beats.length;i++){
let frame=Math.round((s.beats[i].start_s+Math.min(8,s.beats[i].duration_s/2))*24);
await renderStill({serveUrl,composition,frame,output:p+'/_qc/redesigned-final/previews/'+id+'-'+i+'.png',browserExecutable});
}await renderStill({serveUrl,composition,frame:composition.durationInFrames-1,output:p+'/_qc/redesigned-final/previews/'+id+'-end.png',browserExecutable});
}
if(process.argv.includes('--render')){
const silent=p+'/_qc/redesigned-final/'+id+'-silent.mp4';
if(!fs.existsSync(silent)){
console.log('RENDER '+p+' '+id);let prev=-1;
await renderMedia({serveUrl,composition,codec:'h264',crf:18,concurrency:4,browserExecutable,outputLocation:silent,onProgress:({progress})=>{let n=Math.floor(progress*10);if(n!==prev){console.log(id+' '+n*10+'%');prev=n}}});
}
const out=p+'/_qc/redesigned-final/'+'Week'+s.metadata.week+'_'+s.metadata.category+'_'+(id==='Landscape'?'16x9':'9x16')+'.mp4';
fs.mkdirSync(path.dirname(out),{recursive:true});
if(!fs.existsSync(out))cp.execFileSync('ffmpeg',['-v','error','-i',silent,'-i',p+'/audio/narration.wav','-map','0:v:0','-map','1:a:0','-c:v','copy','-af','loudnorm=I=-18:TP=-2:LRA=9','-c:a','aac','-b:a','192k','-ar','48000','-t',String(s.metadata.duration_s),'-movflags','+faststart',out]);
console.log('FINAL '+out);
}
}
})().catch(e=>{console.error(e);process.exit(1)});
