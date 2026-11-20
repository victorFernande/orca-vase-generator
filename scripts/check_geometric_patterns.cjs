/* Offline UI -> production controller -> STL/3MF. Never controls the native app. */
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {spawnSync} = require('node:child_process');
const {chromium} = require(process.env.ORCA_PLAYWRIGHT_MODULE || 'playwright');
const root = path.resolve(__dirname, '..');
const output = path.join(root, 'test-output', 'geometric-patterns');
fs.mkdirSync(output, {recursive:true});
function python(code, input) {
  const result = spawnSync(process.env.ORCA_TEST_PYTHON || 'python', ['-B','-W','error','-c',code],
    {cwd:root,input:input && JSON.stringify(input),encoding:'utf8',maxBuffer:32*1024*1024});
  assert.equal(result.status,0,result.stderr || result.stdout);
  return JSON.parse(result.stdout);
}
const generated = python(String.raw`
import sys,json
sys.path.insert(0,'src')
from vase_studio.studio_ui import get_studio_html
from vase_studio.schema import normalize_params
from vase_studio.geometric_patterns import GEOMETRIC_PATTERNS
from vase_studio.locale_catalog import locale_vocabulary
p=normalize_params({'textures':{'waves':{'enabled':False}},'base_diameter_mm':90,'belly_diameter_mm':100,'waist_diameter_mm':90,'neck_diameter_mm':95,'lip_flare_mm':0})
print(json.dumps({'patterns':GEOMETRIC_PATTERNS,'vocabulary':locale_vocabulary(),'pages':[{'mode':m,'html':get_studio_html(m,{'lang':'en','params':p})} for m in ('page','dock')]},ensure_ascii=False))
`);
const report = {ok:false,cases:[],errors:[],exports:[],limitations:'Isolated Chromium and real Python controller. No native OrcaSlicer or physical print validation.'};
const exportsFromUI = [];
async function capturePreview(page) {
  return page.evaluate(()=>{
    const api=window.VaseStudioMath,mesh=api.state.lastRibbonGeometry;
    let ribbon=null;
    if(mesh) {
      const n=mesh.positions.length/3,indices=[0,1,16,Math.floor(n/7),Math.floor(n/3),Math.floor(n/2),n-2,n-1];
      ribbon={vertices:n,triangles:mesh.indices.length/3,placement:[api.state.lastGeoData.vaseOffsetX,0,api.state.lastGeoData.vaseLiftZ],samples:indices.map(index=>({index,position:Array.from(mesh.positions.subarray(index*3,index*3+3))}))};
    }
    const gl=document.getElementById('gl-canvas').getContext('webgl2');
    return {params:api.state.params,radii:api.evaluateRadiusGrid(api.state.params,17,23).radii,
      gl:!!gl&&!gl.isContextLost(),tris:api.state.clientMetrics.tris,ribbon};
  });
}
async function captureExports(page,mode,pattern,observed) {
  for(const format of ['stl','3mf']) {
    await page.locator(`[data-action="export_${format}"]:visible`).first().click();
    const message=await page.evaluate(()=>window.__messages.filter(m=>m.type==='export_file').at(-1));
    assert.equal(message.format,format);assert.equal(message.params.textures.geometric.pattern,pattern);
    exportsFromUI.push({mode,pattern,message,radii:observed.radii,ribbon:observed.ribbon});
    await page.evaluate(()=>window.__hostCallback({type:'action_result',ok:true,action:'export_file',message:'UI export request captured'}));
  }
}
(async () => {
  const browser = await chromium.launch({headless:true,executablePath:process.env.ORCA_CHROMIUM_EXECUTABLE || undefined});
  try {
    for (const packet of generated.pages) {
      const context = await browser.newContext({viewport:packet.mode==='dock'?{width:420,height:1000}:{width:1600,height:900}});
      const page = await context.newPage();
      page.on('pageerror',error=>report.errors.push(String(error)));
      await page.evaluate(()=>{
        window.__messages=[];
        window.orca={postMessage(message){window.__messages.push(message);},onMessage(callback){window.__hostCallback=callback;}};
      });
      await page.setContent(packet.html,{waitUntil:'load'});
      await page.waitForFunction(()=>window.VaseStudioMath?.state?.lastGeoData);
      if (packet.mode==='dock') await page.locator('[data-tab="textures"]').click();
      await page.locator('[data-tex-toggle-expand="geometric"]').click();
      for (const pattern of generated.patterns) {
        const start = performance.now();
        await page.getByLabel('Sidewall Pattern',{exact:true}).selectOption(pattern);
        await page.waitForFunction(pattern=>window.VaseStudioMath.state.params.textures.geometric.pattern===pattern && window.VaseStudioMath.state.params.textures.geometric.enabled,pattern);
        const observed = await capturePreview(page);
        const selectionMs=Math.round(performance.now()-start);
        assert(observed.gl,'WebGL2 unavailable');
        assert(observed.tris>10000,'Preview geometry missing');
        await captureExports(page,packet.mode,pattern,observed);
        if(pattern==='folded_petals') {
          assert(observed.ribbon?.vertices>100000,'Curled ribbons missing from the actual displayed mesh');
          assert(await page.locator('#btn-mode-spiral').isDisabled());
          const width=page.locator('[data-slider="textures.geometric.ribbon_width_mm"] input[type="number"]');
          await width.fill('36');await width.press('Tab');
          await page.locator('#btn-undo').click();assert.equal(await width.inputValue(),'34.0');
          await page.locator('#btn-redo').click();assert.equal(await width.inputValue(),'36.0');
          for(const [key,value] of Object.entries({ribbon_thickness_mm:1.4,ribbon_curl_deg:390,ribbon_overlap_mm:1.8,ribbon_stretch_pct:12,ribbon_stagger:0.35})) {
            const input=page.locator(`[data-slider="textures.geometric.${key}"] input[type="number"]`);
            await input.fill(String(value));await input.press('Tab');
          }
          for(const quality of ['draft','normal','fine','adaptive']) {
            await page.getByLabel('Ribbon Quality',{exact:true}).selectOption(quality);
            const tuned=await capturePreview(page);
            assert.equal(tuned.params.textures.geometric.ribbon_quality,quality);
            await captureExports(page,packet.mode,pattern,tuned);
          }
          const adaptive04=await capturePreview(page);
          await page.evaluate(()=>window.__hostCallback({type:'printer_updated',printer:{nozzle_mm:0.8}}));
          const adaptive08=await capturePreview(page);
          assert.equal(adaptive08.params.textures.geometric.ribbon_nozzle_mm,0.8);
          assert(adaptive08.ribbon.triangles<adaptive04.ribbon.triangles,'Adaptive mesh did not follow the synchronized nozzle');
          await captureExports(page,packet.mode,pattern,adaptive08);
          await page.evaluate(()=>window.__hostCallback({type:'printer_updated',printer:{nozzle_mm:0.4}}));
          const before=await page.evaluate(()=>JSON.stringify(window.VaseStudioMath.state.params));
          for(const [code,vocabulary] of Object.entries(generated.vocabulary)) {
            await page.locator('#lang-select').selectOption(code);
            assert.equal(await page.locator('[data-i18n="lbl_ribbon_quality"]').textContent(),vocabulary['Ribbon Quality']||'Ribbon Quality');
            assert.equal(await page.evaluate(()=>JSON.stringify(window.VaseStudioMath.state.params)),before);
          }
          await page.locator('#lang-select').selectOption('en');
          await page.getByLabel('Ribbon Quality',{exact:true}).selectOption('fine');
          const columns=page.locator('[data-slider="textures.geometric.cells_around"] input[type="number"]');
          const loops=page.locator('[data-slider="textures.geometric.cells_vertical"] input[type="number"]');
          await columns.fill('36');await columns.press('Tab');
          await loops.fill('24');await loops.press('Tab');
          assert(await page.locator('[data-action="export_stl"]:visible').first().isDisabled(),'Oversized ribbon mesh can still be exported');
          assert(await page.evaluate(()=>!!window.VaseStudioMath.state.geometryError));
          await columns.fill('8');await columns.press('Tab');
          await loops.fill('4');await loops.press('Tab');
          assert(await page.locator('[data-action="export_stl"]:visible').first().isEnabled(),'Valid mesh did not recover after a rejected parameter combination');
          assert(!(await page.locator('#toast-banner').evaluate(el=>el.classList.contains('error')&&el.classList.contains('visible'))),'Recovered mesh still displays the previous geometry error');
          await page.screenshot({path:path.join(output,`${packet.mode}-ribbons-tuned.png`)});
          if(packet.mode==='dock') await page.locator('[data-tab="print"]').click();
          await page.locator('label.toggle-switch').filter({has:page.locator('#chk-include-saucer')}).click();
          const withSaucer=await capturePreview(page);
          assert(withSaucer.ribbon.placement[2]>0,'Nested saucer preview did not lift the ribbons with the cup');
          await captureExports(page,packet.mode,pattern,withSaucer);
          await page.screenshot({path:path.join(output,`${packet.mode}-ribbons-saucer.png`)});
          await page.locator('label.toggle-switch').filter({has:page.locator('#chk-include-saucer')}).click();
          if(packet.mode==='dock') await page.locator('[data-tab="textures"]').click();
        }
        const elapsedMs=Math.round(performance.now()-start);
        await page.screenshot({path:path.join(output,`${packet.mode}-${pattern}.png`)});
        report.cases.push({mode:packet.mode,pattern,gl:true,tris:observed.tris,selectionMs,completeControlFlowMs:elapsedMs});
      }
      // All new controls participate in undo/redo, and language changes preserve geometry.
      const depth=page.locator('[data-slider="textures.geometric.depth_mm"] input[type="number"]');
      await depth.fill('4.5'); await depth.press('Tab');
      assert.equal(await depth.inputValue(),'4.5');
      await page.locator('#btn-undo').click(); assert.equal(await depth.inputValue(),'3.0');
      await page.locator('#btn-redo').click(); assert.equal(await depth.inputValue(),'4.5');
      const before=await page.evaluate(()=>JSON.stringify(window.VaseStudioMath.state.params));
      for (const [code,vocabulary] of Object.entries(generated.vocabulary)) {
        await page.locator('#lang-select').selectOption(code);
        assert.equal(await page.locator('[data-i18n="pattern_folded_petals"]').textContent(),vocabulary['Folded Petals'] || 'Folded Petals');
        assert.equal(await page.evaluate(()=>JSON.stringify(window.VaseStudioMath.state.params)),before);
      }
      await page.locator('#btn-theme').click();
      await page.screenshot({path:path.join(output,`${packet.mode}-light-japanese.png`)});
      await context.close();
    }
    assert.deepEqual(report.errors,[]);
    // Real exports from exactly the parameters emitted by the controls above.
    report.exports=python(String.raw`
import sys,json,struct,zipfile
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,'src')
from vase_studio import plugin_main
from vase_studio.mesh_generator import evaluate_radius_grid
from vase_studio.ribbon_geometry import ribbon_plan,build_ribbon_mesh
import numpy as np
data=json.load(sys.stdin);out=Path('test-output/geometric-patterns/exports').resolve();out.mkdir(parents=True,exist_ok=True)
rows=[]
with patch.object(plugin_main,'_resolve_storage_dir',return_value=out):
 controller=plugin_main.VaseStudioController()
 for item in data:
  message=item['message'];quality=message['params']['textures']['geometric']['ribbon_quality'];message['params']['name']=item['mode']+'_'+item['pattern']+'_'+quality
  np.testing.assert_allclose(evaluate_radius_grid(message['params'],17,23)[2],item['radii'],atol=2e-9,rtol=0)
  if item.get('ribbon'):
   plan=ribbon_plan(message['params']);profile=evaluate_radius_grid(message['params'],plan['nz']+1,3)[2][:,0]
   vertices,triangles=build_ribbon_mesh(message['params'],profile)
   assert item['ribbon']['vertices']==len(vertices) and item['ribbon']['triangles']==len(triangles)
   for sample in item['ribbon']['samples']:np.testing.assert_allclose(vertices[sample['index']]+item['ribbon']['placement'],sample['position'],atol=1e-5,rtol=1e-7)
  replies=[];controller.handle_message(message,replies.append)
  result=next(r for r in replies if r['type']=='action_result');assert result['ok'],result
  p=Path(result['path']);assert p.is_file()
  if message['format']=='stl':
   content=p.read_bytes();n=struct.unpack_from('<I',content,80)[0];assert n>10000 and len(content)==84+50*n
   assert n==result['report']['triangle_count']
  else:
   with zipfile.ZipFile(p) as z:
    assert z.testzip() is None
    assert message['params']['name'] in z.read('3D/3dmodel.model').decode('utf8')
  if item.get('ribbon'):assert 'RIBBON_ASSEMBLY' in [warning['code'] for warning in result['report']['warnings']]
  rows.append({'mode':item['mode'],'pattern':item['pattern'],'format':message['format'],'quality':quality,'includeSaucer':bool(message.get('include_saucer')),'bytes':p.stat().st_size,'surfaceParity':True,'ribbonParity':bool(item.get('ribbon'))})
print(json.dumps(rows))
`,exportsFromUI);
    assert.equal(report.exports.length,52);
    report.ok=true;
  } finally {
    await browser.close();
    fs.writeFileSync(path.join(output,'report.json'),JSON.stringify(report,null,2)+'\n');
  }
  console.log(JSON.stringify({ok:report.ok,uiCases:report.cases.length,realExports:report.exports.length,errors:report.errors.length}));
})().catch(error=>{console.error(error);process.exitCode=1;});
