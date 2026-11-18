# Orca Vase Studio — apresentação para OrcaCloud

Quatro banners em **1600 × 900**, cada um em **português e inglês**, com **By @VictorFernande** no canto inferior direito. A identidade segue o material do Gear, com cinza escuro e verde Orca.

## Descrição

- **Campo único do OrcaCloud:** [ORCACLOUD_BILINGUAL.md](ORCACLOUD_BILINGUAL.md)
- [Texto em português](ORCACLOUD_PT-BR.md)
- [English copy](ORCACLOUD_EN.md)
- [Prévia local com troca de idioma](PREVIEW.html)

O arquivo bilíngue contém os oito links HTTPS das imagens no repositório `victorFernande/orca-vase-generator`, com seções separadas para inglês e português. Use esse arquivo no campo único de descrição do catálogo. As versões individuais servem para outros canais.

## Oito imagens

| Tema | Português | English |
| --- | --- | --- |
| Criação da forma | [01-vase-studio-pt-BR.png](../../assets/marketplace/01-vase-studio-pt-BR.png) | [01-vase-studio-en.png](../../assets/marketplace/01-vase-studio-en.png) |
| Texturas combináveis | [02-surface-textures-pt-BR.png](../../assets/marketplace/02-surface-textures-pt-BR.png) | [02-surface-textures-en.png](../../assets/marketplace/02-surface-textures-en.png) |
| Parede e inspeção | [03-wall-inspection-pt-BR.png](../../assets/marketplace/03-wall-inspection-pt-BR.png) | [03-wall-inspection-en.png](../../assets/marketplace/03-wall-inspection-en.png) |
| Cachepô e pratinho | [04-planter-saucer-pt-BR.png](../../assets/marketplace/04-planter-saucer-pt-BR.png) | [04-planter-saucer-en.png](../../assets/marketplace/04-planter-saucer-en.png) |

Os SVGs editáveis estão na mesma pasta. As ilustrações são projeções de malhas reais do Vase, geradas por `generate_vase_mesh()` e `generate_saucer_mesh()`. Não são fotografias de objetos impressos. Os títulos e as legendas das artes foram traduzidos; a captura real da interface permanece em inglês nas duas versões.

`source-inspection.png` é a cópia de autoria da captura original `assets/vase3.png`, já usada na apresentação do plugin. O original permanece preservado. Os scripts e banners não alteram o código executável nem a versão do Vase.

## Inserir no catálogo

1. Abra **Edit plugin** no seu [Vase no OrcaCloud](https://cloud.orcaslicer.com/app/plugins/shared-plugins/51603699-f020-468b-b722-595265e8a0a5).
2. Cole `ORCACLOUD_BILINGUAL.md` no campo de descrição.
3. Confira os quatro banners de cada idioma na prévia e salve.

As imagens no texto usam URLs públicas do GitHub e são independentes da galeria de anexos do catálogo. As estimativas de impressão e desempenho não são anunciadas como garantias.

## Reproduzir

Com Python 3.12+, NumPy e ferramentas locais de autoria Node.js/Playwright/Chromium:

```console
python -B scripts/build_marketplace_artwork.py
node scripts/render_marketplace_artwork.cjs
python -B scripts/build_marketplace_preview.py
```

`ORCA_PLAYWRIGHT_MODULE` e `ORCA_CHROMIUM_PATH` selecionam instalações alternativas do navegador. São ferramentas de autoria e não dependências do plugin. O renderizador verifica os limites dos textos no canvas; a prévia permite conferir carregamento e idiomas.

O template dos scripts de apresentação deriva do material do Orca Gear Studio, sob MIT, com autoria preservada nos fontes. As malhas, a captura e o conteúdo são específicos do Vase.
