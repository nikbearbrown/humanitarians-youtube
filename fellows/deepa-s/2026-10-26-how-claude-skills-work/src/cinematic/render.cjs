const fs=require('fs'),path=require('path');const stem=path.resolve(__dirname,'../..');
const c={src:__dirname,runtime:stem+'/_qc/cinematic-runtime',modules:path.dirname(path.dirname(require.resolve('remotion/package.json')))};

const {bundle}=require(c.modules+'/@remotion/bundler');
const {selectComposition,renderStill,renderMedia}=require(c.modules+'/@remotion/renderer');
const browserExecutable=c.modules+'/.remotion/chrome-headless-shell/mac-arm64/chrome-headless-shell-mac-arm64/chrome-headless-shell';
(async()=>{
const serveUrl=await bundle({entryPoint:c.src+'/Root.tsx',outDir:c.runtime+'/bundle',publicDir:c.src+'/public'});
fs.mkdirSync(c.runtime+'/previews',{recursive:true});
for(const id of ['STEMwide','STEMtall','Progresstall']){
const composition=await selectComposition({serveUrl,id,browserExecutable});
const sheet=require(c.src+(id==='Progresstall'?'/progress-sheet.json':'/sheet.json'));
for(let i=0;i<sheet.beats.length;i++){
const frame=Math.round((sheet.beats[i].start_s+Math.min(9,sheet.beats[i].actual_duration_s/2))*24);
await renderStill({serveUrl,composition,frame,output:c.runtime+'/previews/'+id+'-'+i+'.png',browserExecutable});
}console.log('PREVIEWS '+id);
}
if(process.argv.includes('--render')){
for(const id of ['STEMwide','STEMtall','Progresstall']){
const composition=await selectComposition({serveUrl,id,browserExecutable});
console.log('RENDER '+id);
await renderMedia({serveUrl,composition,codec:'h264',crf:18,concurrency:3,browserExecutable,outputLocation:c.runtime+'/'+id+'.mp4',onProgress:({progress})=>{if(Math.floor(progress*100)%10===0)process.stdout.write(Math.floor(progress*100)+' ')}});
console.log('DONE '+id);
}
}
})().catch(e=>{console.error(e);process.exit(1)});
