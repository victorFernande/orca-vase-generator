# Geometric sidewall patterns / Padrões geométricos na lateral

## Português

Na aba ou no painel lateral, abra **Texturas → Relevo geométrico**, ligue a
camada e escolha o **Padrão da lateral**. Para ver apenas o novo relevo,
desligue Ondas, Frisos, Origami e Celular; também é possível somar as camadas.

| Padrão | Resultado |
| --- | --- |
| Facetas de losangos | Células angulares em fileiras alternadas |
| Escamas de folhas | Lentes suaves com veio central e inclinação vertical |
| Células em cratera | Cavidades cercadas por uma borda elevada |
| Pétalas dobradas | Células com uma dobra central marcada |
| Flor em espiral | Faixas helicoidais cruzadas |
| Anéis ondulados | Anéis horizontais com ondulação ao redor do vaso |
| Trama de coral | Cristas curvas conectadas em uma trama periódica |

**Profundidade** aceita valores positivos e negativos, de −8 a 8 mm.
**Colunas** (3–36) e **fileiras** (2–24) controlam a repetição;
**torção** (−720° a 720°) e **fase** (0° a 360°) posicionam o padrão.
As intensidades na **base**, no **meio** e no **topo** variam de 0× a 2×,
com transição suave. O envelope global continua suavizando o contato com a
mesa e a borda superior. Desfazer/refazer e presets pessoais incluem esses
parâmetros, inclusive quando a interface muda de idioma.

O relevo usa a mesma superfície radial contínua já existente, com a fórmula
equivalente no Python e no JavaScript. Não acrescenta sólidos sobrepostos.
O modo oco, o modo espiral, a drenagem e o prato coordenado continuam
disponíveis. O protetor de boca aberta no STL mantém seu comportamento.
Relevos muito profundos, negativos ou densos podem exigir menor altura de
camada, ajustes de resfriamento ou limitação de overhang. Consulte o
diagnóstico calculado e a prévia fatiada antes de imprimir.

Os presets publicados anteriormente mantêm seus arrays de malha idênticos
com a nova camada desligada. Nenhuma dependência de execução foi adicionada.
A resolução final continua sendo controlada pelos dois controles de malha;
a prévia interativa pode usar uma resolução menor durante a edição.

## English

In either the page or the dock, expand **Textures → Geometric Relief**, enable
the layer and choose a **Sidewall Pattern**. Disable Waves, Ribbed, Origami
and Cellular to isolate it, or combine their displacements. Available patterns
are Diamond Facets, Leaf Scales, Crater Cells, Folded Petals, Spiral Bloom,
Ripple Rings and Coral Lattice.

Relief depth is −8 to 8 mm. Columns (3–36), rows (2–24), twist (±720°) and
phase (0–360°) control repetition and placement. Independent bottom, middle
and top strengths (0–2×) blend smoothly. The existing global fade envelope
still protects the bed-contact ring and softens the rim. Undo/redo and personal
presets preserve these settings across language changes.

Relief belongs to the existing continuous radial wall rather than overlapping
decorative solids. NumPy export and offline JavaScript preview use equivalent
equations. Hollow and spiral construction, drainage, matching saucers and the
open-mouth STL guard retain their existing behavior. Aggressive relief may
require lower layer heights, cooling changes or overhang clamping; inspect
the diagnostics and sliced preview before printing.

Existing published presets retain identical manufacturing arrays when this
layer is disabled. No runtime dependency was added. Final mesh resolution
remains user-controlled; the interactive preview may sample fewer rows and
columns while editing.

## Reference analysis and provenance

The public [Vase Maker gallery by Dante_x](https://cloud.orcaslicer.com/p/3e9de58df37d)
was inspected on 2026-11-20. Its public listing reported version 0.8.19;
the attached `Vase_0813.webp` screenshot showed Classic, Ripple, Coral,
Diamond, Hourglass, Spiral Bloom, Leaf Scales, Crater Cells and Folded Petals.
Classic and Hourglass are already expressible through this studio's silhouette
controls and existing presets. The listing also describes independent pattern
strength near the bottom, middle and top.

The initial official download request returned HTTP 401
(`missing_authorization`). After the user installed Vase Maker, its local
0.8.19 package became available for read-only source inspection. The complete
plugin was not imported, registered or executed. Only the reviewed, pure
`mesh_plan` estimator was evaluated in isolation with literal parameters and
math/builtin functions, without filesystem or host access.

The installed file identifies `Copyright (c) 2026 Dante x` and
`SPDX-License-Identifier: MIT`. Its SHA-256 and comparison evidence are in
[the source-analysis report](validation/1.3.0-vase-maker-source-analysis.json).
No third-party source or reference screenshots are redistributed. The current
Vase Studio equations remain original interpretations, with the differences
below; they are not exact replicas of the reference geometry.

### Comparação após acesso ao código / Source comparison

| Família / Family | Vase Maker 0.8.19 | Vase Studio 1.3.0 nesta PR / in this PR |
| --- | --- | --- |
| Ondas / Ripple | Canelas cuja fase angular oscila ao longo da altura / Ribs with vertically varying angular phase | Anéis horizontais ondulados / Wavy horizontal rings |
| Losangos / Diamond | Produto de duas ondas cossenoidais / Product of angular and vertical cosine waves | Facetas em células alternadas / Facets in staggered cells |
| Coral | Onda bidimensional com expoente de nitidez / Two-dimensional wave with a sharpness exponent | Trama periódica de cristas curvas / Periodic curved-ridge lattice |
| Flor em espiral / Spiral Bloom | Pétalas helicoidais com raiz larga e crista arredondada / Helical petals with broad roots and rounded crests | Duas famílias de ondas helicoidais / Two families of helical waves |
| Escamas / Leaf Scales | Profundidades independentes de relevo e vale; nitidez, alternância e proporção da célula / Separate relief and valley depths, sharpness, stagger and cell aspect | Lentes periódicas; sem esses quatro controles específicos / Periodic lenses without those four specific controls |
| Crateras / Crater Cells | Cristas apontadas em torno de um centro rebaixado, com os mesmos controles de célula / Pointed rims around recessed centres, with the same cell controls | Bacias arredondadas com borda / Rounded basins with a rim |
| Pétalas dobradas / Folded Petals | Vaso interno mais fitas curvas espessas, com largura, curvatura, sobreposição e estiramento / Inner cup plus thick curved ribbons with width, curl, overlap and stretch | Relevo dobrado integrado à parede; não gera fitas / Folded relief integrated into the wall; no ribbons |

**A opção atual de pétalas não reproduz as fitas do Vase Maker.** Para esse
formato é necessário outro construtor de geometria, com a mesma representação
na prévia e na exportação. A rotina da referência emite o vaso e cada fita
como sólidos indexados separados; não executa uma união booleana. Importar
essa rotina diretamente não comprovaria uma superfície única ou a ausência
de interseções. A escolha entre fitas e relevo contínuo está pendente com o
usuário; esta comparação não declara essa implementação concluída.

**The current petal option does not reproduce Vase Maker's ribbons.** That
form requires a different geometry builder and matching preview/export
representation. The reference emits its cup and each ribbon as separately
indexed solids without a Boolean union. Copying the builder would not prove
a single connected boundary or absence of intersections. The user has been
asked to choose ribbons or continuous relief; this comparison does not claim
that the ribbon implementation is complete.

For a 150 mm vase with eight ribbons, four rows, 34 mm ribbon width and
1.2 mm ribbon thickness, the reference estimator reports 106,624 triangles
in Draft, 359,456 in Normal, 910,720 in Fine and 281,088 in Adaptive quality.
Fine binary STL size is estimated at 45,536,084 bytes. These are estimates
from the reviewed planner, not generated-mesh validation or timings. The
current Studio example has roughly 211,200 triangles but represents a
different surface, so these counts are not an equivalent-quality benchmark.

## Reproducible verification

```console
python -B -W error scripts/build_and_install.py --no-install
python -B -W error -m unittest discover -s tests -v
node scripts/check_multilingual.cjs
node scripts/check_geometric_patterns.cjs
```

For the browser checks, install Playwright in an isolated tools directory and
set `ORCA_PLAYWRIGHT_MODULE` to its module directory. Set `ORCA_TEST_PYTHON`
and optionally `ORCA_CHROMIUM_EXECUTABLE` for custom local installations.

The new Python cases cover seam and row-boundary continuity, signed depth,
layer composition, independent strength zones, JS/NumPy agreement, closed
oriented topology, normals, volume, connected components and Euler characteristic,
including hollow, spiral, drainage, saucer and narrow-profile extremes. The
browser check selects every pattern in both views, exercises undo/redo and
seven languages, then passes the actual emitted export requests through the
production Python controller and checks the resulting STL/3MF files and
surface parity. Evidence is written under ignored `test-output/`.

Browser tests use isolated Chromium. They do not constitute native OrcaSlicer,
real-print, physical wall-thickness or watertight-container certification.
