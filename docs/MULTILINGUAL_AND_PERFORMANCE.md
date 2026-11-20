# Orca Vase Studio 1.2.0 — idiomas e otimização / languages and optimization

A revisão atual usa **um arquivo JSON por idioma**, com descoberta automática no
código-fonte, nos dois formatos standalone e no wheel. Para incluir outro idioma,
adicione somente o arquivo e reconstrua; consulte [o formato dos packs](LANGUAGE_PACKS.md).
O seletor, as preferências, a direção do texto e a correspondência regional são
derivados dos dados, sem uma lista fixa de sete idiomas em Python ou JavaScript.

Os artefatos atuais têm **339.529 bytes por standalone** e **168.361 bytes no wheel**.
Comparados com a versão publicada 1.1.1, o standalone ficou **29,5% menor** e o wheel
**35,9% maior**, incluindo sete JSONs legíveis e o leitor independente. As medidas e
os hashes atuais estão no [relatório da modularização](performance/1.2.0-modular-language-packs.json).
Não houve nova medição de abertura ou FPS após a modularização; a tabela de tempos
abaixo é identificada como um registro histórico do primeiro snapshot com sete idiomas.

## Idiomas offline

O seletor do cabeçalho oferece **Português, English, Español, Italiano, Français,
Deutsch e 日本語** na aba principal e no painel lateral. O idioma do OrcaSlicer é
usado inicialmente, incluindo identificadores como `it_IT`, `es-MX` e `ja_JP`.
Uma escolha explícita é salva no armazenamento próprio do plugin em
`ui_preferences.json` e compartilhada com as duas vistas abertas. A leitura desse
arquivo ocorre no primeiro callback da interface, nunca durante a importação ou o
registro do plugin. Idiomas não suportados usam inglês; sem idioma informado,
permanece o padrão português.

O pacote inclui títulos e descrições dos doze modelos internos, parâmetros,
ferramentas, avisos de impressão, mensagens de exportação e textos auxiliares.
Nomes pessoais, nomes de impressoras, arquivos e valores de fabricação permanecem
intactos. Erros técnicos sem uma mensagem cadastrada aparecem no texto original
para preservar o diagnóstico. Os manuais completos continuam em PT/EN. As cinco
traduções novas usam terminologia de impressão 3D e ainda podem receber revisão
editorial de falantes nativos.

As traduções são texto incluído no instalador: não há tradução automática por
rede, download de fontes nem dependência nova durante a execução.

## Lossless changes and measured limits

The standalone builder compresses only the immutable HTML/CSS/JavaScript template
using Python's standard-library zlib and Base85. Plugin classes and Python source
remain inspectable in the `.py` installer; the wheel keeps ordinary readable
modules. Decompression happens once at import. The encoded expression is not
retained in a separate global cache. Locale rows include each English key once
and construct the five lookup dictionaries inside the WebView.

Wireframe line vertices are now constructed and uploaded only while wireframe is
enabled. Disabling it replaces its GPU payload with an empty allocation. Enabling
it rebuilds the same exact line bytes; triangle geometry, normals, material roles,
overhang values, tessellation and manufacturing exports are unchanged. There is
no reduction in preview quality, mesh resolution or sampling.

| Measurement | Published 1.1.1 | Initial fixed-catalog snapshot |
| --- | ---: | ---: |
| Standalone `.py` / `_any.py`, each | 481,852 bytes | 344,637 bytes |
| Universal wheel | 123,921 bytes | 144,250 bytes |
| Isolated import median, including NumPy | 656.1 ms | 701.4 ms |
| Page HTML generation median | 3.43 ms | 5.55 ms |
| Default requested GPU buffer bytes, wire OFF | 6,604,800 | 6,328,080 |

In that historical fixed-catalog snapshot, the standalone installer was **28.5% smaller**
and the wheel **16.4% larger**. Current modular-pack artifact sizes are listed above. The five-sample
comparison measured about 45 ms more import time; a startup improvement has not
been demonstrated. HTML creation includes the new offline vocabulary and costs
about 2.1 ms more in this measurement. Neither
measurement represents native Orca startup. Requested buffer bytes are allocation
requests, not physical GPU memory or whole-process RAM.

The import comparison uses five fresh Python 3.12 processes per artifact,
alternating baseline/final and final/baseline order. One sample includes reading,
compiling and executing that bundle with NumPy. OS caches were not flushed. The
complete measurements, hashes and order are in
[the import report](performance/1.2.0-import-comparison.json). Machine load and
hardware affect these values; no universal startup, selection-time or FPS
guarantee is claimed.

## Verification

- **40 Python tests passed in 28.048 s**, with `-B -W error` and no skips, including original geometry/export/bridge
  tests, locale variants, catalog completeness, exact placeholder parity, corrupt
  preference recovery and persistent page/dock preference synchronization.
- All twelve published full-resolution preset vases and the botanical saucer were
  generated independently from the archived 1.1.1 standalone bundle and current
  source. Their **39 vertex/triangle/normal digests match exactly**. The five
  manufacturing source files are byte-identical to the published Git baseline;
  see [the immutable reference](../tests/fixtures/published_1_1_1_mesh_digests.json).
- Real STL and 3MF files are created for all five new locales in isolated temporary
  storage. STL payload lengths/facet counts and 3MF user object names are checked;
  names, export paths and numbers are preserved across language changes.
- `scripts/check_multilingual.cjs` exercises all seven languages in both page and
  dock using real Chromium controls: parameter preservation, personal preset
  names, numeric warnings, export requests and edit/Undo across a language change.
  All **14 shipped language/view cases and two data-only extra-language cases passed
  with zero JavaScript errors**, including
  delayed old acknowledgments and reordered preferences from the other view. It
  records a report plus Italian screenshots.
- A temporary eighth JSON alone is detected by the host and page/dock selector;
  both standalone files and the wheel are rebuilt and imported outside the source
  tree. Regional precedence, partial fallback, context overrides, RTL metadata,
  strict malformed/duplicate/placeholder rejection and lossless catalog migration
  are covered. That temporary Dutch pack is not part of the production files.
- Independent visual review covers seven languages × two views × two themes and
  compares baseline/current main GPU input hashes. A separate wire OFF/ON/OFF/ON
  check verifies exact original line bytes and release of the optional payload.

The tests operate in temporary folders and isolated Chromium. They do not change
the user's installed plugin or control OrcaSlicer. Installation, restart and
native integration on the user's Windows session, native macOS/Linux rendering,
physical printing and watertightness are not newly validated by this delivery.

## Reproducing

```text
python -B -W error scripts/build_and_install.py --no-install
python -B -W error -m unittest discover -s tests -v
node scripts/check_multilingual.cjs
```

The browser script requires development-only Playwright. CI installs it in an
isolated runner folder and runs all seven languages on Linux; Python tests and
packaging run on Windows, macOS and Linux. Test jobs have read-only repository
permissions. Write permission is restricted to the tag-triggered release job.

Install one distribution format, activate it and restart OrcaSlicer. A Cloud
subscription is a separate installation from a local plugin: disable the old local
copy when switching to Cloud. This branch does not publish or replace the existing
OrcaCloud listing automatically.
