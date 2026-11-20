/* Isolated offline language integration: real controls, no Orca process or network. */
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {spawnSync} = require('node:child_process');
const root = path.resolve(__dirname, '..');
const {chromium} = require(process.env.ORCA_PLAYWRIGHT_MODULE || 'playwright');
const output = path.resolve(process.env.ORCA_I18N_OUTPUT || path.join(root, 'test-output', 'multilingual'));
fs.mkdirSync(output, {recursive:true});
const python = process.env.ORCA_TEST_PYTHON || process.env.PYTHON || 'python';
const generate = spawnSync(python, ['-B', '-W', 'error', '-c', String.raw`
import sys,json,tempfile,shutil
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,'src')
from vase_studio.studio_ui import get_studio_html
from vase_studio.schema import DEFAULT_PARAMS
from vase_studio.locale_catalog import locale_vocabulary
from vase_studio import language_packs
packets=[]
for mode in ('page','dock'):
 html=get_studio_html(mode,{'lang':'pt','user_presets':[{'id':'user_i18n','name':'Custom Ω 日本語','category':'user','params':DEFAULT_PARAMS}]})
 html=html.replace('  bootStudioUI();','  window.__vaseQA = {state:state, localizedWarning:localizedWarning};\n  bootStudioUI();')
 packets.append({'mode':mode,'html':html})
dynamic=[]
with tempfile.TemporaryDirectory() as temporary:
 folder=Path(temporary)/'locales'
 shutil.copytree('src/vase_studio/locales',folder)
 extra_code='nl' if 'nl' not in locale_vocabulary() else 'qaa'
 extra={'schema_version':1,'code':extra_code,'native_name':'Nederlands','direction':'ltr','order':7,
        'translations':{'Total Height':'Hoogte','Preset Gallery':'Galerij','ui:sec_presets::Preset Gallery':'Modellenbibliotheek'}}
 (folder/(extra_code+'.json')).write_text(json.dumps(extra),encoding='utf8')
 with patch.object(language_packs,'__file__',str(Path(temporary)/'language_packs.py')):
  for mode in ('page','dock'):
   html=get_studio_html(mode,{'lang':extra_code+'-NL'})
   html=html.replace('  bootStudioUI();','  window.__vaseQA = {state:state, localizedWarning:localizedWarning};\n  bootStudioUI();')
   dynamic.append({'mode':mode,'html':html,'code':extra_code,'expected_count':len(locale_vocabulary())})
print(json.dumps({'packets':packets,'vocabulary':locale_vocabulary(),'locales':list(locale_vocabulary()),'dynamic':dynamic},ensure_ascii=False))
`], {cwd:root,encoding:'utf8',maxBuffer:16*1024*1024});
if (generate.status !== 0) throw Error(generate.stderr || generate.stdout);
const generated = JSON.parse(generate.stdout);
const report = {ok:false, locales:generated.locales, checks:[], dynamicDataOnly:[], consoleErrors:[], limitations:'Isolated Chromium; no native OrcaSlicer or native speaker certification.'};

(async function() {
  const browser = await chromium.launch({headless:true, executablePath:process.env.ORCA_CHROMIUM_EXECUTABLE || undefined});
  try {
    for (const packet of generated.packets) {
      const context = await browser.newContext({viewport:packet.mode === 'dock' ? {width:420,height:1000} : {width:1600,height:900}});
      await context.addInitScript(() => {
        window.__messages = [];
        window.orca = {postMessage(message) { window.__messages.push(message); }, onMessage(callback) {window.__hostCallback=callback;}};
      });
      const page = await context.newPage();
      page.on('pageerror', error => report.consoleErrors.push(String(error)));
      // setContent does not create a new document: initialize the mock before the application.
      await page.evaluate(() => {
        window.__messages=[];
        window.orca={postMessage(message){window.__messages.push(message);}, onMessage(callback){window.__hostCallback=callback;}};
      });
      await page.setContent(packet.html, {waitUntil:'load'});
      await page.waitForFunction(() => Boolean(window.__vaseQA && document.querySelector('.preset-card')));
      const before = await page.evaluate(() => JSON.stringify(window.__vaseQA.state.params));
      for (const code of report.locales) {
        await page.locator('#lang-select').selectOption(code);
        const snapshot = await page.evaluate(() => ({
          lang:document.documentElement.lang,
          params:JSON.stringify(window.__vaseQA.state.params),
          height:document.querySelector('[data-spec-label="height_mm"]').textContent,
          send:document.querySelector('[data-i18n="btn_send_plater"]').textContent,
          custom:[...document.querySelectorAll('.preset-name')].some(node=>node.textContent==='Custom Ω 日本語'),
          warning:window.__vaseQA.localizedWarning({code:'HEIGHT_OVERFLOW',en:'Height (310.5 mm) exceeds printer Z limit (250 mm).',pt:'Altura (310.5 mm) excede o limite Z da impressora (250 mm).'}),
          messages:window.__messages.filter(m=>m.type==='set_language')
        }));
        assert.equal(snapshot.lang,code);
        assert.equal(snapshot.params,before,'Changing language modified manufacturing params');
        assert(snapshot.custom,'Personal preset title changed');
        if (generated.vocabulary[code]) {
          assert.equal(snapshot.height,generated.vocabulary[code]['Total Height'] || 'Total Height');
          assert.equal(snapshot.send,generated.vocabulary[code]['ui:btn_send_plater::Send to OrcaSlicer Plater'] || generated.vocabulary[code]['Send to OrcaSlicer Plater'] || 'Send to OrcaSlicer Plater');
          assert.equal(snapshot.warning,(generated.vocabulary[code]['Height ({a} mm) exceeds printer Z limit ({b} mm).'] || 'Height ({a} mm) exceeds printer Z limit ({b} mm).').replace('{a}','310.5').replace('{b}','250'));
        }
        assert.equal(snapshot.messages.at(-1).lang,code);
        // Runtime UI callbacks preserve the selected language and all names.
        await page.evaluate(code => window.__hostCallback({type:'preferences_updated',lang:code}),code);
        await page.locator('[data-action="export_stl"]:visible').first().click();
        const action = await page.evaluate(()=>window.__messages.at(-1));
        assert.equal(action.type,'export_file');
        assert.equal(action.format,'stl');
        assert.equal(action.params.name,JSON.parse(before).name);
        await page.evaluate(()=>window.__hostCallback({type:'action_result',ok:true,action:'export_file',message:'QA export'}));
        report.checks.push({mode:packet.mode,language:code,params_unchanged:true,personal_title_preserved:true,warning_numbers_preserved:true,export_request:true});
      }
      // A real number edit survives a locale switch, and Undo restores it.
      const height = page.locator('[data-slider="height_mm"] input[type="number"]');
      await height.fill('180');
      await height.press('Tab');
      await page.locator('#lang-select').selectOption('it');
      await page.locator('#lang-select').selectOption('fr');
      const recent = await page.evaluate(()=>window.__messages.filter(m=>m.type==='set_language').slice(-2));
      await page.evaluate(({mode,id})=>window.__hostCallback({type:'preferences_updated',lang:'it',source_mode:mode,request_id:id,language_revision:10001}),{mode:packet.mode,id:recent[0].request_id});
      assert.equal(await page.locator('html').getAttribute('lang'),'fr','Stale language acknowledgment reverted a newer manual choice');
      await page.evaluate(({mode,id})=>window.__hostCallback({type:'preferences_updated',lang:'fr',source_mode:mode,request_id:id,language_revision:10002}),{mode:packet.mode,id:recent[1].request_id});
      await page.evaluate(({mode,id})=>window.__hostCallback({type:'preferences_updated',lang:'it',source_mode:mode,request_id:id,language_revision:10001}),{mode:packet.mode,id:recent[0].request_id});
      assert.equal(await page.locator('html').getAttribute('lang'),'fr','Older revision replaced acknowledged language');
      await page.locator('#lang-select').selectOption('it');
      const pendingPeerCase = await page.evaluate(()=>window.__messages.filter(m=>m.type==='set_language').at(-1));
      await page.evaluate(mode=>window.__hostCallback({type:'preferences_updated',lang:'fr',source_mode:mode==='page'?'dock':'page',request_id:55,language_revision:10005}),packet.mode);
      assert.equal(await page.locator('html').getAttribute('lang'),'it','Pending local choice flickered to a peer acknowledgment');
      await page.evaluate(({mode,id})=>window.__hostCallback({type:'preferences_updated',lang:'it',source_mode:mode,request_id:id,language_revision:10004}),{mode:packet.mode,id:pendingPeerCase.request_id});
      assert.equal(await page.locator('html').getAttribute('lang'),'fr','Newer peer preference was lost while waiting for local acknowledgment');
      await page.locator('#lang-select').selectOption('it');
      assert.equal(await height.inputValue(),'180');
      await page.locator('#btn-undo').click();
      assert.equal(Number(await height.inputValue()),JSON.parse(before).height_mm);
      await page.screenshot({path:path.join(output,`${packet.mode}-italian.png`)});
      await context.close();
    }
    for (const packet of generated.dynamic) {
      const context = await browser.newContext({viewport:packet.mode==='dock'?{width:420,height:1000}:{width:1600,height:900}});
      const page = await context.newPage();
      page.on('pageerror',error=>report.consoleErrors.push(String(error)));
      await page.evaluate(()=>{
        window.__messages=[];
        window.orca={postMessage(message){window.__messages.push(message);},onMessage(callback){window.__hostCallback=callback;}};
      });
      await page.setContent(packet.html,{waitUntil:'load'});
      assert.equal(await page.locator('html').getAttribute('lang'),packet.code);
      assert.equal(await page.locator('html').getAttribute('dir'),'ltr');
      assert.equal(await page.locator('#lang-select option').count(),packet.expected_count);
      assert.equal(await page.locator('[data-spec-label="height_mm"]').textContent(),'Hoogte');
      assert.equal(await page.locator('[data-i18n="sec_presets"]').textContent(),'Modellenbibliotheek');
      assert.equal(await page.locator('[data-i18n="btn_send_plater"]').first().textContent(),'Send to OrcaSlicer Plater');
      await page.locator('#lang-select').selectOption('en');
      await page.locator('#lang-select').selectOption(packet.code);
      assert.equal(await page.locator('[data-spec-label="height_mm"]').textContent(),'Hoogte');
      await page.screenshot({path:path.join(output,`${packet.mode}-data-only-dutch.png`)});
      report.dynamicDataOnly.push({mode:packet.mode,language:packet.code,host_region_fallback:true,context_override:true,english_fallback:true,added_json_only:true});
      await context.close();
    }
    assert.equal(report.consoleErrors.length,0,report.consoleErrors.join('\n'));
    report.ok=true;
  } finally {
    await browser.close();
    fs.writeFileSync(path.join(output,'report.json'),JSON.stringify(report,null,2)+'\n');
  }
  console.log(JSON.stringify({ok:report.ok,cases:report.checks.length,dynamicCases:report.dynamicDataOnly.length,consoleErrors:report.consoleErrors.length}));
})().catch(error=>{console.error(error);process.exitCode=1;});
