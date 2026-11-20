# Packs de idioma / Language packs

Cada idioma é um arquivo JSON independente em `src/vase_studio/locales/`.
Gear, Vase e Box adotam o mesmo formato; cada plugin inclui sua própria cópia do
leitor e mantém suas traduções, sem importar o projeto vizinho.

Para acrescentar um idioma, adicione somente um arquivo, por exemplo
`src/vase_studio/locales/nl.json`:

```json
{
  "schema_version": 1,
  "code": "nl",
  "native_name": "Nederlands",
  "direction": "ltr",
  "order": 7,
  "translations": {
    "Total Height": "Hoogte",
    "Preset Gallery": "Galerij",
    "Send to OrcaSlicer Plater": "Naar het OrcaSlicer-printbed sturen"
  }
}
```

Os valores são texto simples. Preserve exatamente os marcadores como `{n}`,
`{name}`, `{path}` e `{mm}`. O código aceita variantes regionais, como `nl-NL`,
normalizadas para minúsculas. A correspondência tenta primeiro o código exato,
depois suas bases (`nl-nl` → `nl`) e, por fim, inglês. Traduções ausentes usam a
frase inglesa original; um pack parcial é válido.

`native_name` é o nome exibido no seletor. `order` controla sua posição.
`direction` aceita `ltr` e `rtl`; o atributo de direção do documento acompanha a
seleção. Não inclua HTML, scripts nem instruções de instalação dentro do JSON.

Para uma frase que precisa de tradução diferente conforme o controle, há uma
chave opcional de contexto. Por exemplo:

```json
"ui:sec_presets::Preset Gallery": "Modellenbibliotheek"
```

Essa chave prevalece sobre `"Preset Gallery"` apenas nesse controle. Os demais
usos continuam procurando a frase inglesa comum. Os identificadores atuais estão
no adaptador `locale_catalog.UI_MESSAGES`.

## Gerar os três instaladores

```text
python -B -W error scripts/build_and_install.py --no-install
python -B -W error -m unittest discover -s tests -v
node scripts/check_multilingual.cjs
```

Não é preciso alterar listas em Python ou JavaScript para acrescentar o oitavo
idioma. O construtor descobre automaticamente todos os JSONs, valida os dados e
inclui os mesmos packs nos dois arquivos `.py` e no wheel. Os arquivos isolados
embutem o JSON compactado; o wheel mantém arquivos legíveis em
`vase_studio/locales/`. A interface, o idioma do host e as preferências usam a mesma
descoberta. O teste de extensão cria um oitavo idioma temporário, gera os três
formatos e os importa fora da árvore de fontes.

A validação de build rejeita JSON malformado, chaves duplicadas, códigos de idioma
duplicados, metadados inválidos, HTML e marcadores diferentes. Um arquivo opcional
inválido durante a execução é ignorado para preservar a interface. A instalação
isolada também pode ler uma pasta `locales/` ao lado do `.py`; seus arquivos válidos
prevalecem sobre os packs embutidos. Para distribuir pelo OrcaCloud, reconstrua e
publique o instalador com o novo arquivo incluído.

## English

Add a data-only JSON file to `src/vase_studio/locales/` and rebuild. No Python or
JavaScript allowlist needs editing. The schema and builder support partial packs,
native display names, text direction and regional fallback. An exact region wins
before its base language; missing phrases use the original English source. Keep
all placeholders unchanged. Optional `ui:<message-key>::<English source>` entries
override the common phrase in that specific UI control.

Both standalone formats embed every discovered pack; the readable wheel includes
all locale files. An optional `locales/` directory beside a standalone can override
its embedded data. Runtime invalid optional files are skipped; strict builds fail
before replacing artifacts. Pack contents are displayed as text and never run as
code. Source, bundled and wheel tests exercise a temporary extra language; it is
not shipped as a production Dutch translation.

## Verificação de manutenção da CI

Uma cópia privada recebeu somente um oitavo `nl.json` com uma frase traduzida.
O build real, os 40 testes completos e o script de navegador existente passaram
sem alteração adicional de Python ou JavaScript nessa cópia. O navegador exercitou
16 casos dos oito idiomas disponíveis e dois casos da extensão sintética, sem
erros. Os totais dos seletores e os códigos de fixtures são derivados do registro;
packs futuros parciais não precisam conter todas as frases para passar na CI.
Veja [a evidência sanitizada](validation/1.2.0-future-partial-pack-ci.json).
