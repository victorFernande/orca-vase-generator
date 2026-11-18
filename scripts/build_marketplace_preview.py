"""Build Vase Studio marketplace descriptions and an offline bilingual review page.

Copyright (c) 2026 Orca Gear Studio (MIT shared preview template; see LICENSE).
Copyright (c) 2026 Orca Vase Studio.
"""
from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "orcacloud"


def inline(value):
    value = escape(value)
    value = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", value)
    return re.sub(r"\[([^]]+)\]\((https://[^)]+)\)", r'<a href="\2">\1</a>', value)


def render(source):
    parts, list_kind = [], None
    for line in source.splitlines():
        is_bullet = line.startswith('- ')
        is_number = bool(re.match(r'^\d+\. ', line))
        next_list = 'ul' if is_bullet else 'ol' if is_number else None
        if list_kind != next_list:
            if list_kind:
                parts.append(f'</{list_kind}>')
            if next_list:
                parts.append(f'<{next_list}>')
            list_kind = next_list
        if not line.strip():
            continue
        if next_list:
            parts.append('<li>'+inline(re.sub(r'^(?:- |\d+\. )', '', line))+'</li>')
        elif (match := re.fullmatch(r'!\[([^]]*)\]\(([^)]+)\)', line)):
            parts.append(f'<figure><img src="{escape(match[2])}" alt="{escape(match[1])}" loading="lazy"></figure>')
        elif line.startswith('## '):
            parts.append('<h2>'+inline(line[3:])+'</h2>')
        elif line.startswith('### '):
            parts.append('<h3>'+inline(line[4:])+'</h3>')
        elif line.startswith('# '):
            parts.append('<h1>'+inline(line[2:])+'</h1>')
        else:
            parts.append('<p>'+inline(line)+'</p>')
    if list_kind:
        parts.append(f'</{list_kind}>')
    return '\n'.join(parts)


def main():
    drafts = {lang:(DOCS/f'DESCRIPTION_{lang}.md').read_text(encoding='utf-8') for lang in ('PT-BR','EN')}
    for lang, draft in drafts.items():
        ready = draft.replace('../../assets/marketplace/', 'https://raw.githubusercontent.com/victorFernande/orca-vase-generator/main/assets/marketplace/')
        if len(ready) > 4000:
            raise ValueError(f'{lang}: listing exceeds the reference author\'s 4000-character target')
        (DOCS/f'ORCACLOUD_{lang}.md').write_text(ready,encoding='utf-8',newline='\n')
        print(f'{lang}: {len(ready)} characters, 4 public image links')
    footer='**By @VictorFernande · Free / Gratuito · MIT**\n\n[GitHub & Docs](https://github.com/victorFernande/orca-vase-generator) · [Downloads](https://github.com/victorFernande/orca-vase-generator/releases)\n'
    combined='## English\n\n'+(DOCS/'ORCACLOUD_EN.md').read_text(encoding='utf-8').replace('\n## ','\n### ')+'\n---\n\n## Português\n\n'+(DOCS/'ORCACLOUD_PT-BR.md').read_text(encoding='utf-8').replace('\n## ','\n### ')+'\n---\n\n'+footer
    if len(combined)>4000:
        raise ValueError(f'Bilingual listing: {len(combined)} characters; shorten to 4000.')
    (DOCS/'ORCACLOUD_BILINGUAL.md').write_text(combined,encoding='utf-8',newline='\n')
    print(f'Bilingual: {len(combined)} characters, 8 public image links')
    pt = render(drafts['PT-BR'])
    en = render(drafts['EN'])
    html = '''<!doctype html>
<html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Orca Vase Studio — prévia da apresentação</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#eef2f0;color:#20312d;font:17px/1.7 system-ui,sans-serif}
nav{position:sticky;top:0;z-index:2;background:#11191b;color:#eaf4f0;padding:14px max(20px,calc((100vw - 1040px)/2));display:flex;gap:12px;align-items:center;flex-wrap:wrap}
nav strong{margin-right:auto;font-size:15px}button{border:1px solid #426659;background:transparent;color:#eaf4f0;padding:8px 16px;border-radius:8px;cursor:pointer;font:inherit;font-size:14px}button[aria-pressed=true]{background:#15dfae;color:#11191b;border-color:#15dfae}
.notice{background:#dce9e3;padding:14px 24px;text-align:center;font-size:14px}
main{max-width:1040px;margin:28px auto 64px;background:#fff;padding:48px;border:1px solid #d6e0da;border-radius:16px}
h1{font-size:46px;line-height:1.1;letter-spacing:-1.5px;margin:0 0 22px}h2{font-size:29px;line-height:1.25;margin:44px 0 20px;letter-spacing:-.6px}p{margin:18px 0}li{margin:10px 0}a{color:#007b61;text-underline-offset:3px}figure{margin:28px -24px}img{display:block;width:100%;height:auto;border-radius:12px}section[hidden]{display:none}
@media(max-width:640px){body{font-size:16px}main{margin:0;border:0;border-radius:0;padding:28px 20px}h1{font-size:34px}h2{font-size:25px}figure{margin:22px -10px}.notice{text-align:left}}
</style>
<nav><strong>ORCA VASE STUDIO · PRÉVIA EDITORIAL</strong><button data-lang="pt" aria-pressed="true">Português</button><button data-lang="en" aria-pressed="false">English</button></nav>
<div class="notice">Artes PT/EN em 1600 × 900. <a href="ORCACLOUD_BILINGUAL.md">Texto bilíngue para o OrcaCloud</a> · <a href="README.md">Arquivos e instruções</a></div>
<main><section id="pt" lang="pt-BR">__PT__</section><section id="en" lang="en" hidden>__EN__</section></main>
<script>document.querySelectorAll('[data-lang]').forEach(button=>button.addEventListener('click',()=>{const lang=button.dataset.lang;document.querySelectorAll('main section').forEach(section=>section.hidden=section.id!==lang);document.querySelectorAll('[data-lang]').forEach(item=>item.setAttribute('aria-pressed',String(item===button)));document.documentElement.lang=lang==='pt'?'pt-BR':'en';}));</script>
</html>
'''.replace('__PT__',pt).replace('__EN__',en)
    (DOCS/'PREVIEW.html').write_text(html,encoding='utf-8',newline='\n')
    print('docs/orcacloud/PREVIEW.html')


if __name__ == '__main__':
    main()
