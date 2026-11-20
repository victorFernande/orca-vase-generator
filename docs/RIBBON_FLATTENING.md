# Achatamento das fitas / Ribbon flattening (1.3.1)

## Português

Em **Texturas combináveis → Relevo geométrico → Pétalas dobradas**, ajuste
**Achatamento das fitas** entre 0 e 60%. Quanto maior o valor, mais próximas
do corpo ficam as folhas dobradas. O padrão é 0%, preservando a geometria
publicada na versão 1.3.0 e os presets existentes. A largura continua
independente: diminua-a se também quiser folhas menores.

Comece em 30–50%. O achatamento modifica a superfície central da fita antes
de calcular suas duas faces, preservando a espessura existente, incluindo o
afinamento original das bordas e o efeito do estiramento. Não altera a
espessura da parede nem a cavidade interna do vaso. A mesma transformação
é usada na prévia e nas exportações STL/3MF, na aba e no painel lateral.

No exemplo matemático de um vaso cilíndrico de 160 mm de altura e raio
50 mm, oito fitas, quatro voltas, largura 34 mm, espessura nominal 1,2 mm e
qualidade Normal, 60% de achatamento reduz a projeção máxima da superfície
central de cerca de 13,914 para 5,566 mm. A área das faces das fitas com
overhang acima de 45° cai de aproximadamente 10.205 para 2.372 mm². Estas
áreas incluem faces internas/sobrepostas; não medem a área exposta após
união no fatiador e não constituem uma garantia de impressão sem suporte.

Uma proteção rejeita a inversão local da espessura nas dobras comprimidas.
Se aparecer esse aviso, reduza achatamento ou espessura, ou aumente a largura.
Ela não é uma verificação completa de autointerseções. As fitas e o vaso
continuam sólidos fechados separados com sobreposições intencionais.
Confira a união e todas as camadas na prévia fatiada. Ainda pode haver
overhang forte; avalie material, resfriamento e suportes. A impressão física
e o novo controle dentro do OrcaSlicer ainda precisam de validação.

## English

Under **Combinable Textures → Geometric Relief → Folded Petals**, use
**Ribbon Flattening (0–60%)** to bring folded leaves closer to the cup.
Start at 30–50%. The default is 0%, retaining the published 1.3.0 geometry.
Reduce Ribbon Width independently if smaller leaves are also desired.

The ribbon midsurface is compressed toward the actual cylindrical profile
before offsetting its skins. The existing thickness, edge taper and stretch
behavior are preserved. Cup walls and the inner cavity stay unchanged.
Python exports and the WebGL preview use the same transformation in both
the main tab and sidebar, with undo/redo and all seven modular languages.

For a 160 mm cylindrical sample of radius 50 mm, eight ribbons, four loops,
34 mm width, nominal thickness 1.2 mm and Normal quality, 60% flattening
reduces maximum midsurface projection from about 13.914 to 5.566 mm.
Ribbon face area above 45° overhang decreases from about 10,205 to 2,372 mm².
This includes internal/overlapping faces, not just the exposed sliced union;
it is not a support-free printing guarantee.

A local offset-inversion guard rejects pinched folds and explains how to
adjust the settings. It does not prove absence of all self-intersections.
Cup and ribbons remain intentionally overlapping closed shells. Inspect
the sliced union and every layer; steep overhangs may remain. Physical
printing and native OrcaSlicer validation of this new control are pending.
