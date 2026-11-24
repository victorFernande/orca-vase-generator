"""Published additions are complete packs, not English fallbacks."""
import json
from pathlib import Path
import re
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from vase_studio import locale_catalog,language_packs,studio_ui,plugin_main

class NewPublishedLanguageTests(unittest.TestCase):
    def test_new_packs_cover_every_english_entry_and_preserve_placeholders(self):
        folder=ROOT/'src/vase_studio/locales'
        english=json.loads((folder/'en.json').read_text(encoding='utf8'))['translations']
        names={'ru':'Русский','cs':'Čeština','zh':'简体中文'}
        for code,name in names.items():
            raw=json.loads((folder/(code+'.json')).read_text(encoding='utf8'))
            pack=language_packs.validate_language_pack(raw)
            self.assertEqual(pack['native_name'],name)
            self.assertEqual(set(pack['translations']),set(english))
            for key,value in pack['translations'].items():
                self.assertEqual(sorted(re.findall(r'\{[A-Za-z_]\w*\}',key)),sorted(re.findall(r'\{[A-Za-z_]\w*\}',value)))
                self.assertTrue(value.strip())
            self.assertNotEqual(pack['translations']['Save'],'Save')
            self.assertNotEqual(pack['translations']['Reset'],'Reset')

    def test_regional_names_detect_and_render_in_both_views(self):
        for regional,code in (('ru_RU.UTF-8','ru'),('cs_CZ','cs'),('zh_CN.UTF-8','zh'),('zh-Hans-CN','zh')):
            self.assertEqual(locale_catalog.normalize_language(regional),code)
            self.assertEqual(plugin_main._detect_language({'language':regional}),code)
            for mode in ('page','dock'):
                html=studio_ui.get_studio_html(mode,{'lang':regional})
                self.assertTrue('<html lang="'+code+'"' in html,(code,mode))
                for new_code,native_name in (('ru','Русский'),('cs','Čeština'),('zh','简体中文')):
                    self.assertTrue(re.search(r'(?:"code"\s*:\s*"'+new_code+r'"|value="'+new_code+r'")',html),(code,mode,new_code))
                    self.assertTrue(native_name in html,(code,mode,native_name))
