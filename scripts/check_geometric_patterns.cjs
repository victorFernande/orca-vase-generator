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
        const observed = await page.evaluate(()=>{
          const api=window.VaseStudioMath;
          const gl=document.getElementById('gl-canvas').getContext('webgl2');
          return {params:api.state.params,radii:api.evaluateRadiusGrid(api.state.params,17,23).radii,
            gl:!!gl && !gl.isContextLost(),tris:api.state.clientMetrics.tris};
        });
        assert(observed.gl,'WebGL2 unavailable');
        assert(observed.tris>10000,'Preview geometry missing');
        for (const format of ['stl','3mf']) {
          await page.locator(`[data-action="export_${format}"]:visible`).first().click();
          const message = await page.evaluate(()=>window.__messages.filter(m=>m.type==='export_file').at(-1));
          assert.equal(message.format,format);
          assert.equal(message.params.textures.geometric.pattern,pattern);
          exportsFromUI.push({mode:packet.mode,pattern,message,radii:observed.radii});
          await page.evaluate(()=>window.__hostCallback({type:'action_result',ok:true,action:'export_file',message:'UI export request captured'}));
        }
        const elapsedMs=Math.round(performance.now()-start);
        await page.screenshot({path:path.join(output,`${packet.mode}-${pattern}.png`)});
        report.cases.push({mode:packet.mode,pattern,gl:true,tris:observed.tris,selectAndTwoRequestsMs:elapsedMs});
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
import numpy as np
data=json.load(sys.stdin);out=Path('test-output/geometric-patterns/exports').resolve();out.mkdir(parents=True,exist_ok=True)
rows=[]
with patch.object(plugin_main,'_resolve_storage_dir',return_value=out):
 controller=plugin_main.VaseStudioController()
 for item in data:
  message=item['message'];message['params']['name']=item['mode']+'_'+item['pattern']
  np.testing.assert_allclose(evaluate_radius_grid(message['params'],17,23)[2],item['radii'],atol=2e-9,rtol=0)
  replies=[];controller.handle_message(message,replies.append)
  result=next(r for r in replies if r['type']=='action_result');assert result['ok'],result
  p=Path(result['path']);assert p.is_file()
  if message['format']=='stl':
   content=p.read_bytes();n=struct.unpack_from('<I',content,80)[0];assert n>10000 and len(content)==84+50*n
  else:
   with zipfile.ZipFile(p) as z:
    assert z.testzip() is None
    assert message['params']['name'] in z.read('3D/3dmodel.model').decode('utf8')
  rows.append({'mode':item['mode'],'pattern':item['pattern'],'format':message['format'],'bytes':p.stat().st_size,'surfaceParity':True})
print(json.dumps(rows))
`,exportsFromUI);
    assert.equal(report.exports.length,28);
    report.ok=true;
  } finally {
    await browser.close();
    fs.writeFileSync(path.join(output,'report.json'),JSON.stringify(report,null,2)+'\n');
  }
  console.log(JSON.stringify({ok:report.ok,uiCases:report.cases.length,realExports:report.exports.length,errors:report.errors.length}));
})().catch(error=>{console.error(error);process.exitCode=1;});
