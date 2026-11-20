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
| Pétalas dobradas | Fitas curvas espessas enroladas em volta de um vaso interno |
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

Os seis relevos usam a superfície radial contínua já existente, com a fórmula
equivalente no Python e no JavaScript. A opção **Pétalas dobradas** usa outro
construtor: um vaso interno e fitas curvas fechadas e sobrepostas, como na
referência. Essas superfícies não passam por uma união booleana.
Para os relevos, os modos oco e espiral continuam disponíveis. As fitas
usam um vaso interno redondo e oco; o modo espiral e as outras texturas
ficam indisponíveis enquanto esse estilo estiver ativo. Drenagem e prato
continuam disponíveis; as cotas de parede representam o vaso interno. O protetor de boca aberta no STL mantém seu comportamento.
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

Six relief families belong to the existing continuous radial wall.
**Folded Petals** instead builds a round hollow cup and separately closed,
overlapping curled ribbon solids, adapted from the reference. This is not
a Boolean union. Spiral mode and other texture layers are unavailable for
this style. Wall calipers refer to the inner cup. NumPy export and offline JavaScript preview use equivalent
equations. The other styles retain hollow/spiral construction. Drainage, matching
saucers and the open-mouth STL guard remain available. Aggressive relief may
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
plugin was not imported, registered or executed. Only the reviewed pure `mesh_plan` estimator and ribbon-coordinate builder
were evaluated in isolation, for estimates and coordinate fixtures, with literal parameters and
math/builtin functions, without filesystem or host access.

The installed file identifies `Copyright (c) 2026 Dante x` and
`SPDX-License-Identifier: MIT`. Its SHA-256 and comparison evidence are in
[the source-analysis report](validation/1.3.0-vase-maker-source-analysis.json).
Reference screenshots and the complete reference plugin are not redistributed.
The six radial relief families remain original interpretations. The curled
ribbon equations are now adapted from the installed MIT reference; its
copyright and full permission notice are preserved in `ribbon_geometry.py`,
each standalone bundle and the wheel license. The existing Studio profile
editor defines the inner cup. There is no claim that all Vase Maker features
or its complete cup meshing implementation were ported.

### Comparação após acesso ao código / Source comparison

| Família / Family | Vase Maker 0.8.19 | Vase Studio 1.3.0 nesta PR / in this PR |
| --- | --- | --- |
| Ondas / Ripple | Canelas cuja fase angular oscila ao longo da altura / Ribs with vertically varying angular phase | Anéis horizontais ondulados / Wavy horizontal rings |
| Losangos / Diamond | Produto de duas ondas cossenoidais / Product of angular and vertical cosine waves | Facetas em células alternadas / Facets in staggered cells |
| Coral | Onda bidimensional com expoente de nitidez / Two-dimensional wave with a sharpness exponent | Trama periódica de cristas curvas / Periodic curved-ridge lattice |
| Flor em espiral / Spiral Bloom | Pétalas helicoidais com raiz larga e crista arredondada / Helical petals with broad roots and rounded crests | Duas famílias de ondas helicoidais / Two families of helical waves |
| Escamas / Leaf Scales | Profundidades independentes de relevo e vale; nitidez, alternância e proporção da célula / Separate relief and valley depths, sharpness, stagger and cell aspect | Lentes periódicas; sem esses quatro controles específicos / Periodic lenses without those four specific controls |
| Crateras / Crater Cells | Cristas apontadas em torno de um centro rebaixado, com os mesmos controles de célula / Pointed rims around recessed centres, with the same cell controls | Bacias arredondadas com borda / Rounded basins with a rim |
| Pétalas dobradas / Folded Petals | Vaso interno mais fitas curvas espessas, com largura, curvatura, sobreposição e estiramento / Inner cup plus thick curved ribbons with width, curl, overlap and stretch | Fitas curvas com as equações adaptadas da referência e o perfil do Studio / Curled ribbons using the adapted reference equations and Studio profile |

### Fitas enroladas / Curled ribbons

A escolha do usuário foi reproduzir as fitas enroladas. Ao selecionar
**Pétalas dobradas**, a interface sugere oito fitas e quatro voltas, largura
34 mm, espessura 1,2 mm, curvatura 382°, sobreposição 1,4 mm,
estiramento 8% e alternância 0,5. A espessura é nominal na região central;
as bordas afinam até 35% desse valor e o estiramento também reduz a espessura. Os controles de intensidade por altura
modulam a curvatura, com interpolação linear e limite efetivo de 1,5×,
como na referência. A profundidade radial fica oculta por não se aplicar.

| Controle / Control | Intervalo / Range |
| --- | --- |
| Quantidade de fitas / Ribbon count | 3–36 |
| Voltas / Loops | 2–24 |
| Largura / Width | 8–80 mm |
| Espessura / Thickness | 0.4–4 mm |
| Curvatura / Curl | 180–430° |
| Achatamento / Flattening | 0–60% (1.3.1+) |
| Sobreposição / Overlap | 0–4 mm |
| Estiramento / Stretch | 0–25% |
| Alternância / Stagger | 0–1 |
| Qualidade / Quality | Draft, Normal, Fine, Adaptive |

**Fine** é a qualidade final padrão. Durante o arraste dos controles há uma
prévia Draft, seguida da malha final ao soltar. A amostragem final das fitas
usa o mesmo plano em Python e JavaScript. A qualidade Adaptativa usa o
diâmetro do bico sincronizado da impressora para definir a amostragem. A qualidade da parede interna
continua controlada pelos dois parâmetros de resolução existentes. Os dois
extremos das fitas são aparados entre Z=0 e a altura escolhida, corrigindo
pequenos excessos que o deslocamento normal pode causar na referência.
Acima de três milhões de triângulos só nas fitas, a geração é impedida antes
da alocação; diminua a quantidade ou selecione uma qualidade menor. Um vaso
interno estreito demais para a parede também impede a geração e a exportação.

The selected implementation uses actual curled ribbons rather than wall
relief. Width, thickness, curl, overlap, stretch and stagger are editable.
Fine is the final default, with Draft during slider dragging. Python and
JavaScript use the same final ribbon sampling plan. Adaptive quality uses
the synchronized printer nozzle diameter. The Studio resolution
controls still define cup detail. Ribbon vertices are trimmed to the requested
height; meshes above three million ribbon triangles are rejected before
allocation, and the cup must have room for its chosen wall thickness.

Cada fita é uma superfície fechada e orientada, com índices separados do
vaso. **As sobreposições são intencionais e não equivalem a uma união
geométrica.** Confira a união na prévia fatiada. O diagnóstico calcula os
overhangs da malha completa e identifica essa montagem; a estimativa de
material soma os sólidos, incluindo o volume sobreposto. O limitador de
inclinação e as cotas de parede atuam no vaso interno, sem achatar as fitas.
A tampa visual do corte Z preenche o vaso interno; as fitas ficam expostas
no plano de corte, sem uma tampa artificial que esconda sua seção.

Each ribbon is an oriented closed boundary with indices separate from the
cup. **Intentional intersections are not a Boolean union.** Inspect the sliced
union. Overhang diagnostics inspect the complete mesh and identify this
assembly; material estimates sum solids and include overlap volume. Wall
calipers and overhang clamping describe the cup, not an artificial radial
replacement for ribbons. The Z-cut visual cap fills the cup while ribbons
remain exposed at the clipping plane.

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

The new Python cases cover radial seam and row-boundary continuity, signed depth,
layer composition, independent strength zones, JS/NumPy agreement, closed
oriented topology, normals, volume, connected components and Euler characteristic,
including hollow, spiral, drainage, saucer and narrow-profile extremes. The
browser check selects every pattern in both views, exercises undo/redo and
seven languages, then passes the actual emitted export requests through the
production Python controller and checks the resulting STL/3MF files and
surface parity. Additional ribbon cases verify every shell boundary and its
connectivity, positive volume, requested Z bounds, production JS vertex and
oriented-triangle parity, 24 coordinate samples from the reviewed reference
builder, and isolated ribbon generation from both standalones and the wheel.
Browser flows exercise all four qualities, the six ribbon controls, undo/redo
and all seven languages, with 52 actual STL/3MF exports in total, including adaptive nozzle
synchronization, nested-saucer placement
and recovery after an oversized mesh is rejected. Evidence is
written under ignored `test-output/`.

Browser tests use isolated Chromium. They do not constitute native OrcaSlicer,
real-print, physical wall-thickness or watertight-container certification.
