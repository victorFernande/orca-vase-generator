# /// script
# requires-python = ">=3.12"
# dependencies = ["numpy>=1.26"]
#
# [tool.orcaslicer.plugin]
# id = "orca-vase-studio"
# name = "Orca Vase Studio"
# description = "Parametric 3D Vase & Planter Studio with X-Ray Wall Calipers & 1-Click Plater | Estudio 3D de Vasos e Cachepos"
# author = "Orca Vase Studio"
# version = "1.2.0"
# ///

from __future__ import annotations

import sys as _orca_init_sys
import types as _orca_init_types
if __name__ not in _orca_init_sys.modules:
    _orca_init_sys.modules[__name__] = _orca_init_types.ModuleType(__name__)

# ===========================================================================
# MODULE: vase_studio.locale_catalog
# ===========================================================================

"""Offline interface vocabulary. Geometry and user-supplied names are never translated.

Rows use English as a stable source and contain Spanish, Italian, French, German
and Japanese in that order. Original Portuguese/English vocabulary stays in the UI.
"""

pass  # [bundled] hoisted __future__ import

SUPPORTED_LANGUAGES = ("pt", "en", "es", "it", "fr", "de", "ja")
LANGUAGE_NAMES = {"pt": "Português", "en": "English", "es": "Español", "it": "Italiano", "fr": "Français", "de": "Deutsch", "ja": "日本語"}


def normalize_language(value: object, default: str = "pt") -> str:
    raw = str(value or "").strip().lower().replace("_", "-")
    if not raw:
        return default if default in SUPPORTED_LANGUAGES else "en"
    code = raw.split("-", 1)[0].split(".", 1)[0]
    return code if code in SUPPORTED_LANGUAGES else "en"


_VOCABULARY = """
Surprise Me|Sorpréndeme|Sorprendimi|Surprenez-moi|Überraschen|おまかせ生成
Shape|Forma|Forma|Forme|Form|形状
Textures|Texturas|Texture|Textures|Texturen|テクスチャ
Wall & Print|Pared e impresión|Parete e stampa|Paroi et impression|Wand und Druck|壁と印刷
Presets|Ajustes|Preimpostazioni|Préréglages|Vorlagen|プリセット
Preset Gallery|Galería de modelos|Galleria modelli|Galerie de modèles|Modellgalerie|モデルギャラリー
+ Save|+ Guardar|+ Salva|+ Enregistrer|+ Speichern|＋保存
Save|Guardar|Salva|Enregistrer|Speichern|保存
All|Todos|Tutti|Tous|Alle|すべて
Organic|Orgánicos|Organici|Organiques|Organisch|有機的
Geometric|Geométricos|Geometrici|Géométriques|Geometrisch|幾何学的
Planters|Maceteros|Vasi per piante|Cache-pots|Pflanzgefäße|植木鉢
Saved|Guardados|Salvati|Enregistrés|Gespeichert|保存済み
Silhouette & 2D Curve|Silueta y curva 2D|Silhouette e curva 2D|Silhouette et courbe 2D|Silhouette und 2D-Kurve|輪郭と2D曲線
Sliders|Deslizadores|Cursori|Curseurs|Schieberegler|スライダー
Freeform 2D Curve|Curva 2D libre|Curva 2D libera|Courbe 2D libre|Freie 2D-Kurve|自由な2D曲線
Sliders → Curve|Deslizadores → Curva|Cursori → Curva|Curseurs → Courbe|Regler → Kurve|スライダー → 曲線
Drag handles directly on the 2D silhouette or fine-tune sliders below.|Arrastra los puntos de la silueta 2D o ajusta los controles inferiores.|Trascina i punti sulla silhouette 2D o regola i cursori sotto.|Déplacez les poignées sur la silhouette 2D ou ajustez les curseurs ci-dessous.|Punkte an der 2D-Silhouette ziehen oder die Regler unten einstellen.|2D輪郭のハンドルをドラッグするか、下のスライダーで微調整します。
Drag knots · Click curve to add knot · Double-click/right-click interior knot to remove.|Arrastra puntos · Clic en la curva para añadir · Doble clic/clic derecho para eliminar.|Trascina i punti · Clic sulla curva per aggiungere · Doppio clic/clic destro per eliminare.|Déplacez les points · Cliquez pour ajouter · Double-clic/clic droit pour supprimer.|Punkte ziehen · Kurve anklicken zum Hinzufügen · Doppelklick/Rechtsklick zum Entfernen.|点をドラッグ・曲線をクリックして追加・内部の点をダブルクリックまたは右クリックして削除。
Mesh Resolution|Resolución de malla|Risoluzione mesh|Résolution du maillage|Netzauflösung|メッシュ解像度
Orca Emerald Silk|Seda esmeralda Orca|Seta smeraldo Orca|Soie émeraude Orca|Orca-Smaragdseide|Orcaエメラルドシルク
Terracotta Clay|Arcilla terracota|Argilla terracotta|Argile terre cuite|Terrakotta|テラコッタ
Matte White Ceramic|Cerámica blanca mate|Ceramica bianca opaca|Céramique blanche mate|Matte weiße Keramik|白いマット陶器
Copper Bronze|Bronce cobrizo|Bronzo ramato|Bronze cuivré|Kupferbronze|銅色ブロンズ
🔬 X-Ray / Wall (Translucent)|🔬 Rayos X / Pared (translúcida)|🔬 Raggi X / Parete (traslucida)|🔬 Rayons X / Paroi (translucide)|🔬 Röntgen / Wand (durchscheinend)|🔬 X線／壁（半透明）
Overhang Heatmap (°)|Mapa de voladizos (°)|Mappa degli sbalzi (°)|Carte des surplombs (°)|Überhangkarte (°)|オーバーハング分布（°）
🔬 X-Ray / Wall|🔬 Rayos X / Pared|🔬 Raggi X / Parete|🔬 Rayons X / Paroi|🔬 Röntgen / Wand|🔬 X線／壁
📏 mm Calipers|📏 Cotas en mm|📏 Quote in mm|📏 Cotes en mm|📏 Maße in mm|📏 寸法（mm）
🔥 Overhang|🔥 Voladizos|🔥 Sbalzi|🔥 Surplombs|🔥 Überhänge|🔥 オーバーハング
⌗ Wireframe|⌗ Alambre|⌗ Reticolo|⌗ Filaire|⌗ Drahtgitter|⌗ ワイヤーフレーム
🍽 Saucer|🍽 Plato|🍽 Sottovaso|🍽 Soucoupe|🍽 Untersetzer|🍽 受け皿
Nested|Encajado|Sovrapposto|Emboîté|Ineinander|重ねて表示
Side-by-Side|Lado a lado|Affiancati|Côte à côte|Nebeneinander|横並び
Printability|Imprimibilidad|Stampabilità|Imprimabilité|Druckbarkeit|印刷適性
Wall / Floor|Pared / Fondo|Parete / Fondo|Paroi / Fond|Wand / Boden|壁／底
Ø Mouth Bore|Ø Abertura|Ø Apertura|Ø Ouverture|Ø Öffnung|開口内径 Ø
Dimensions (mm)|Dimensiones (mm)|Dimensioni (mm)|Dimensions (mm)|Abmessungen (mm)|寸法（mm）
Max Overhang|Voladizo máximo|Sbalzo massimo|Surplomb maximal|Max. Überhang|最大オーバーハング
Est. Filament|Filamento estimado|Filamento stimato|Filament estimé|Geschätztes Filament|推定フィラメント量
Triangles|Triángulos|Triangoli|Triangles|Dreiecke|三角形数
Outer Wall|Pared exterior|Parete esterna|Paroi extérieure|Außenwand|外壁
Cavity & Floor|Cavidad y fondo|Cavità e fondo|Cavité et fond|Hohlraum und Boden|空洞と底
Front|Frente|Fronte|Face|Vorne|正面
Top|Superior|Alto|Dessus|Oben|上面
Bottom|Inferior|Fondo|Dessous|Unten|底面
Fit View|Encuadrar|Inquadra|Cadrer|Ansicht anpassen|全体表示
✂ Cross-Section Cut|✂ Corte transversal|✂ Sezione trasversale|✂ Coupe transversale|✂ Querschnitt|✂ 断面表示
✂ Vertical Cut (Profile Y)|✂ Corte vertical (perfil Y)|✂ Sezione verticale (profilo Y)|✂ Coupe verticale (profil Y)|✂ Vertikalschnitt (Profil Y)|✂ 垂直断面（Y方向）
💿 Horizontal Z Slice (Plan 5%–100%)|💿 Corte horizontal Z (5%–100%)|💿 Sezione orizzontale Z (5%–100%)|💿 Coupe horizontale Z (5 %–100 %)|💿 Horizontaler Z-Schnitt (5%–100%)|💿 水平Z断面（5%～100%）
Envelope & Global Twist|Envolvente y torsión global|Inviluppo e torsione globale|Enveloppe et torsion globale|Hüllform und Gesamtverdrehung|全体形状とねじれ
Combinable Textures|Texturas combinables|Texture combinabili|Textures combinables|Kombinierbare Texturen|組み合わせ可能なテクスチャ
Ribbed / Fluted|Estriado / Acanalado|Nervato / Scanalato|Cannelures / Rainures|Gerippt / Kanneliert|リブ／溝
Organic Waves|Ondas orgánicas|Onde organiche|Ondes organiques|Organische Wellen|有機的な波
Origami Diamond|Diamantes de origami|Diamanti origami|Diamants origami|Origami-Rauten|折り紙のひし形
Cellular / Coral 3D|Celular / Coral 3D|Cellulare / Corallo 3D|Cellulaire / Corail 3D|Zellular / 3D-Koralle|細胞／3Dサンゴ
Ridged Coral Veins|Vetas de coral en relieve|Venature di corallo in rilievo|Veines de corail en relief|Erhabene Korallenadern|サンゴ状の隆起
Wall & Opening (mm)|Pared y abertura (mm)|Parete e apertura (mm)|Paroi et ouverture (mm)|Wand und Öffnung (mm)|壁と開口（mm）
True Hollow Vase (mm Wall)|Vaso hueco (pared en mm)|Vaso cavo (parete in mm)|Vase creux (paroi en mm)|Hohle Vase (Wand in mm)|中空の花瓶（壁厚mm）
Spiral Mode (1 Line)|Modo espiral (1 línea)|Modalità spirale (1 linea)|Mode spirale (1 ligne)|Spiralmodus (1 Linie)|スパイラルモード（1周）
Always keep open mouth on .STL export|Mantener la boca abierta al exportar .STL|Mantieni l'apertura nell'esportazione .STL|Garder l'ouverture à l'export .STL|Öffnung beim .STL-Export offen halten|.STL書き出し時に開口を維持
Spiral Mode builds a solid base block whose top is removed by the slicer (.3MF). Keep the toggle below checked so .STL exports stay open!|El modo espiral genera un bloque sólido; el laminador elimina la parte superior (.3MF). Activa la protección para exportar .STL abierto.|La modalità spirale genera un blocco solido; lo slicer rimuove la parte superiore (.3MF). Mantieni attiva la protezione per esportare .STL aperti.|Le mode spirale crée un bloc plein dont le trancheur retire le dessus (.3MF). Gardez la protection active pour exporter les .STL ouverts.|Der Spiralmodus erzeugt einen Vollkörper; der Slicer entfernt die Oberseite (.3MF). Schutz aktiv lassen, damit .STL offen bleibt.|スパイラルモードはソリッドを生成し、スライサーが上面を除去します（.3MF）。.STLの開口を維持するには保護を有効にしてください。
Spiral Mode: solid base block for .3MF (slicer removes top) · .STL protected w/ Open Mouth|Espiral: bloque para .3MF (se elimina el techo) · .STL con boca abierta|Spirale: blocco per .3MF (lo slicer rimuove il tetto) · .STL aperto protetto|Spirale : bloc .3MF (dessus retiré par le trancheur) · .STL ouvert protégé|Spirale: Vollkörper für .3MF (Slicer entfernt Deckfläche) · .STL offen geschützt|スパイラル：.3MF用ソリッド（上面はスライサーで除去）・.STLは開口保護
Warning: Solid Spiral Block — .STL will export CLOSED at top for Spiral Slicing!|Atención: bloque espiral sólido; el .STL tendrá la parte superior CERRADA.|Attenzione: blocco spirale solido; il .STL avrà la parte superiore CHIUSA.|Attention : bloc spirale plein ; le .STL sera FERMÉ au sommet.|Achtung: Spiral-Vollkörper – .STL wird OBEN GESCHLOSSEN exportiert!|注意：スパイラル用ソリッドの.STLは上面が閉じた状態で書き出されます。
≈ {n} loops of {lw} mm · Bore Ø {id} mm|≈ {n} perímetros de {lw} mm · Abertura Ø {id} mm|≈ {n} perimetri da {lw} mm · Apertura Ø {id} mm|≈ {n} périmètres de {lw} mm · Ouverture Ø {id} mm|≈ {n} Bahnen mit {lw} mm · Öffnung Ø {id} mm|約{n}周 × {lw} mm・内径 Ø {id} mm
≈ {mm} mm floor ({n} lay.) · Nozzle {noz}mm (ideal {wmin}–{wmax} mm)|≈ {mm} mm de fondo ({n} capas) · Boquilla {noz}mm (ideal {wmin}–{wmax} mm)|≈ {mm} mm di fondo ({n} strati) · Ugello {noz}mm (ideale {wmin}–{wmax} mm)|≈ {mm} mm de fond ({n} couches) · Buse {noz}mm (idéal {wmin}–{wmax} mm)|≈ {mm} mm Boden ({n} Schichten) · Düse {noz}mm (ideal {wmin}–{wmax} mm)|底約{mm} mm（{n}層）・ノズル{noz}mm（推奨{wmin}～{wmax} mm）
Hollow · {w} mm|Hueco · {w} mm|Cavo · {w} mm|Creux · {w} mm|Hohl · {w} mm|中空・{w} mm
Spiral · {w} mm|Espiral · {w} mm|Spirale · {w} mm|Spirale · {w} mm|Spirale · {w} mm|スパイラル・{w} mm
Ø Outer: {v} mm|Ø Exterior: {v} mm|Ø Esterno: {v} mm|Ø Extérieur : {v} mm|Ø Außen: {v} mm|外径 Ø：{v} mm
Ø Bore: {v} mm|Ø Interior: {v} mm|Ø Interno: {v} mm|Ø Intérieur : {v} mm|Ø Innen: {v} mm|内径 Ø：{v} mm
Wall: {v} mm|Pared: {v} mm|Parete: {v} mm|Paroi : {v} mm|Wand: {v} mm|壁厚：{v} mm
Wall: {v} mm ({min}–{max} mm)|Pared: {v} mm ({min}–{max} mm)|Parete: {v} mm ({min}–{max} mm)|Paroi : {v} mm ({min}–{max} mm)|Wand: {v} mm ({min}–{max} mm)|壁厚：{v} mm（{min}～{max} mm）
Bottom: {v} mm|Fondo: {v} mm|Fondo: {v} mm|Fond : {v} mm|Boden: {v} mm|底厚：{v} mm
💿 Z Slice = {z} mm ({pct}%)|💿 Corte Z = {z} mm ({pct}%)|💿 Sezione Z = {z} mm ({pct}%)|💿 Coupe Z = {z} mm ({pct} %)|💿 Z-Schnitt = {z} mm ({pct}%)|💿 Z断面 = {z} mm（{pct}%）
Wall {v} mm|Pared {v} mm|Parete {v} mm|Paroi {v} mm|Wand {v} mm|壁厚 {v} mm
Bottom {v} mm|Fondo {v} mm|Fondo {v} mm|Fond {v} mm|Boden {v} mm|底厚 {v} mm
Ø Bore {v} mm|Ø Interior {v} mm|Ø Interno {v} mm|Ø Intérieur {v} mm|Ø Innen {v} mm|内径 Ø {v} mm
Spiral Cap (.3MF)|Tapa espiral (.3MF)|Chiusura spirale (.3MF)|Dessus spirale (.3MF)|Spiral-Deckfläche (.3MF)|スパイラル上面（.3MF）
Auto-configure OrcaSlicer on send|Configurar OrcaSlicer al enviar|Configura OrcaSlicer all'invio|Configurer OrcaSlicer à l'envoi|OrcaSlicer beim Senden einstellen|送信時にOrcaSlicerを自動設定
Smooth Spiral XY Seam|Suavizar costura espiral XY|Smussa la giunzione spirale XY|Lisser la couture spirale XY|Spiralnaht XY glätten|スパイラルXY継ぎ目を滑らかに
Auto-Clamp Overhang Slope|Limitar automáticamente el voladizo|Limita automaticamente gli sbalzi|Limiter automatiquement les surplombs|Überhangneigung automatisch begrenzen|オーバーハング角度を自動制限
Gardening: Drainage & Saucer|Jardinería: drenaje y plato|Giardinaggio: drenaggio e sottovaso|Jardinage : drainage et soucoupe|Garten: Drainage und Untersetzer|園芸：排水と受け皿
Bottom Drainage Holes|Orificios de drenaje|Fori di drenaggio sul fondo|Trous de drainage du fond|Abflusslöcher im Boden|底面の排水穴
Smart blind cavities through solid bottom layers: real drainage holes without breaking single-contour Spiral Vase!|Cavidades ciegas en las capas del fondo: drenaje sin romper el contorno único del modo espiral.|Cavità cieche negli strati del fondo: drenaggio senza interrompere il contorno unico della spirale.|Cavités borgnes dans les couches du fond : drainage sans rompre le contour unique de la spirale.|Sacklöcher durch die Bodenschichten: Drainage ohne Unterbrechung der Spiral-Kontur.|底のソリッド層に止まり穴を形成し、スパイラルの単一輪郭を維持して排水します。
Watertight cylindrical drainage tunnels straight through the hollow pot floor.|Túneles de drenaje cilíndricos con malla cerrada a través del fondo del vaso.|Fori cilindrici passanti con mesh chiusa nel fondo del vaso cavo.|Tunnels cylindriques traversant le fond du vase avec maillage fermé.|Zylindrische Abflüsse durch den Hohlboden mit geschlossenem Netz.|中空鉢の底を貫通する円筒状排水穴。メッシュの閉鎖性を維持します。
Include Matching Saucer|Incluir plato a juego|Includi sottovaso abbinato|Inclure la soucoupe assortie|Passenden Untersetzer einschließen|対応する受け皿を追加
Vase + Saucer together automatically switch to Open Hollow Mesh on send/export.|Vaso y plato juntos cambian a malla hueca abierta al enviar/exportar.|Vaso e sottovaso passano automaticamente alla mesh cava aperta all'invio/esportazione.|Vase et soucoupe passent automatiquement au maillage creux ouvert à l'envoi/export.|Vase und Untersetzer wechseln beim Senden/Export zum offenen Hohlnetz.|花瓶と受け皿を同時に送信・書き出す場合、開口した中空メッシュに自動切替します。
Match Vase Texture on Saucer|Aplicar textura al plato|Abbina la texture al sottovaso|Assortir la texture de la soucoupe|Vasentextur auf Untersetzer übertragen|花瓶のテクスチャを受け皿にも適用
Send to OrcaSlicer Plater|Enviar a la mesa de OrcaSlicer|Invia al piatto di OrcaSlicer|Envoyer au plateau OrcaSlicer|An OrcaSlicer-Druckplatte senden|OrcaSlicerのプレートへ送信
Export .3MF|Exportar .3MF|Esporta .3MF|Exporter .3MF|.3MF exportieren|.3MFを書き出す
Export .STL|Exportar .STL|Esporta .STL|Exporter .STL|.STL exportieren|.STLを書き出す
Smooth Circle|Círculo liso|Cerchio liscio|Cercle lisse|Glatter Kreis|滑らかな円
{n}-Gon|{n} lados|{n} lati|{n} côtés|{n}-Eck|{n}角形
{n} active|Texturas activas: {n}|Texture attive: {n}|Textures actives : {n}|{n} aktiv|{n}件有効
Exceeds printer build volume ({bx}×{by}×{bz} mm)!|Supera el volumen de impresión ({bx}×{by}×{bz} mm).|Supera il volume di stampa ({bx}×{by}×{bz} mm).|Dépasse le volume d'impression ({bx}×{by}×{bz} mm).|Überschreitet den Bauraum ({bx}×{by}×{bz} mm)!|造形範囲を超えています（{bx}×{by}×{bz} mm）。
Fit to Printer|Ajustar a la impresora|Adatta alla stampante|Adapter à l'imprimante|An Drucker anpassen|造形範囲に合わせる
Click to sync active OrcaSlicer printer|Sincronizar la impresora activa de OrcaSlicer|Sincronizza la stampante attiva di OrcaSlicer|Synchroniser l'imprimante active OrcaSlicer|Aktiven OrcaSlicer-Drucker synchronisieren|現在のOrcaSlicerプリンターを同期
Synced active printer: {name} ({dims})|Impresora sincronizada: {name} ({dims})|Stampante sincronizzata: {name} ({dims})|Imprimante synchronisée : {name} ({dims})|Drucker synchronisiert: {name} ({dims})|プリンターを同期：{name}（{dims}）
Dimensions fitted to {name} build volume!|Dimensiones ajustadas al volumen de {name}.|Dimensioni adattate al volume di {name}.|Dimensions adaptées au volume de {name}.|Abmessungen an den Bauraum von {name} angepasst!|{name}の造形範囲に合わせました。
PRINTABLE|IMPRIMIBLE|STAMPABILE|IMPRIMABLE|DRUCKBAR|印刷可能
WARNING|ATENCIÓN|ATTENZIONE|ATTENTION|WARNUNG|注意
CRITICAL|CRÍTICO|CRITICO|CRITIQUE|KRITISCH|重大
Generated printable vase design!|Se generó un vaso imprimible.|Generato un vaso stampabile.|Modèle de vase imprimable généré.|Druckbare Vase erstellt!|印刷可能な花瓶を生成しました。
Preset saved!|Modelo guardado.|Preimpostazione salvata.|Préréglage enregistré.|Vorlage gespeichert!|プリセットを保存しました。
Converted sliders to PCHIP Freeform Curve!|Convertido a curva libre PCHIP.|Convertito in curva libera PCHIP.|Conversion en courbe libre PCHIP.|In freie PCHIP-Kurve umgewandelt!|PCHIP自由曲線に変換しました。
Total Height|Altura total|Altezza totale|Hauteur totale|Gesamthöhe|全高
Base Diameter|Diámetro de la base|Diametro base|Diamètre de base|Basisdurchmesser|底面直径
Belly Diameter|Diámetro del cuerpo|Diametro pancia|Diamètre du renflement|Bauchdurchmesser|胴部直径
Belly Height Ratio|Altura relativa del cuerpo|Altezza relativa pancia|Hauteur relative du renflement|Relative Bauchhöhe|胴部の高さ比
Waist Diameter|Diámetro de cintura|Diametro vita|Diamètre du col rétréci|Taillendurchmesser|くびれ直径
Waist Height Ratio|Altura relativa de cintura|Altezza relativa vita|Hauteur relative du rétrécissement|Relative Taillenhöhe|くびれの高さ比
Neck Diameter|Diámetro del cuello|Diametro collo|Diamètre du col|Halsdurchmesser|首部直径
Top Lip Flare|Apertura del borde|Svasatura bordo|Évasement du bord|Randaufweitung|上縁の広がり
Top Rim Bevel|Chaflán del borde|Smusso bordo|Chanfrein du bord|Randfase|上縁の面取り
Polygon Sides (0=Circle)|Lados del polígono (0=círculo)|Lati poligono (0=cerchio)|Côtés du polygone (0=cercle)|Polygonseiten (0=Kreis)|多角形の辺数（0=円）
Polygon Roundness|Redondeo del polígono|Arrotondamento poligono|Arrondi du polygone|Polygonrundung|角の丸み
Angular Resolution|Resolución angular|Risoluzione angolare|Résolution angulaire|Winkelauflösung|円周方向の解像度
Vertical Resolution|Resolución vertical|Risoluzione verticale|Résolution verticale|Vertikale Auflösung|垂直方向の解像度
Bottom Texture Fade|Desvanecimiento inferior|Attenuazione texture inferiore|Atténuation de texture en bas|Textur unten ausblenden|底部テクスチャの減衰
Top Texture Fade|Desvanecimiento superior|Attenuazione texture superiore|Atténuation de texture en haut|Textur oben ausblenden|上部テクスチャの減衰
Global Helical Twist|Torsión helicoidal global|Torsione elicoidale globale|Torsion hélicoïdale globale|Globale Schraubenverdrehung|全体のねじれ角
Rib Depth|Profundidad de estrías|Profondità scanalature|Profondeur des cannelures|Rippentiefe|リブの深さ
Rib Count (Density)|Número de estrías (densidad)|Numero nervature (densità)|Nombre de cannelures (densité)|Rippenzahl (Dichte)|リブ数（密度）
Rib Width / Duty Cycle|Anchura de estría / Proporción|Larghezza nervatura / Rapporto|Largeur de cannelure / Rapport|Rippenbreite / Anteil|リブ幅／比率
Crest Sharpness|Nitidez de cresta|Nitidezza cresta|Netteté des crêtes|Scheitelschärfe|山の鋭さ
Rib Helical Twist|Torsión helicoidal de estrías|Torsione elicoidale nervature|Torsion des cannelures|Rippenverdrehung|リブのねじれ角
Angular Phase|Fase angular|Fase angolare|Phase angulaire|Winkelphase|角度位相
Wave Depth|Profundidad de onda|Profondità onda|Amplitude des ondes|Wellentiefe|波の深さ
Vertical Wavelength|Longitud de onda vertical|Lunghezza d'onda verticale|Longueur d'onde verticale|Vertikale Wellenlänge|垂直方向の波長
Angular Lobes|Lóbulos angulares|Lobi angolari|Lobes angulaires|Winkellappen|円周方向の波数
Counter-Wave Mix|Mezcla de ondas opuestas|Miscela contro-onde|Mélange d'ondes opposées|Gegenwellenmischung|逆方向の波の混合率
Wave Skew|Asimetría de onda|Asimmetria onda|Asymétrie des ondes|Wellenschiefe|波の非対称性
Wave Phase|Fase de onda|Fase onda|Phase des ondes|Wellenphase|波の位相
Facet Depth|Profundidad de facetas|Profondità sfaccettature|Profondeur des facettes|Facettentiefe|面の深さ
Cells Around|Celdas alrededor|Celle per giro|Cellules par tour|Zellen im Umfang|円周方向のセル数
Vertical Tiers|Niveles verticales|Livelli verticali|Étages verticaux|Vertikale Ebenen|垂直方向の段数
Crease Sharpness|Nitidez de pliegues|Nitidezza pieghe|Netteté des plis|Faltenschärfe|折り目の鋭さ
Row Stagger|Desfase de filas|Sfalsamento righe|Décalage des rangées|Reihenversatz|行のずれ
Cellular Depth|Profundidad celular|Profondità cellulare|Profondeur cellulaire|Zelltiefe|セルの深さ
Angular Cell Scale|Escala angular celular|Scala angolare celle|Échelle angulaire des cellules|Winkel-Zellgröße|円周方向のセル寸法
Vertical Cell Size|Tamaño vertical celular|Dimensione verticale celle|Taille verticale des cellules|Vertikale Zellgröße|垂直方向のセル寸法
Detail Octaves|Octavas de detalle|Ottave di dettaglio|Octaves de détail|Detailoktaven|詳細度（オクターブ）
Pattern Seed|Semilla del patrón|Seme del motivo|Graine du motif|Muster-Startwert|模様のシード
Spiral Line Width|Anchura de línea espiral|Larghezza linea spirale|Largeur de ligne spirale|Spiral-Linienbreite|スパイラルの線幅
Bottom Solid Layers|Capas sólidas inferiores|Strati solidi inferiori|Couches solides du fond|Massive Bodenschichten|底のソリッド層数
Wall Thickness|Espesor de pared|Spessore parete|Épaisseur de paroi|Wandstärke|壁厚
Bottom Floor Thickness|Espesor del fondo|Spessore fondo|Épaisseur du fond|Bodenstärke|底厚
Max Safe Overhang|Voladizo máximo seguro|Sbalzo massimo sicuro|Surplomb maximal sûr|Max. sicherer Überhang|安全な最大オーバーハング
Drainage Hole Count|Número de orificios|Numero fori di drenaggio|Nombre de trous de drainage|Anzahl Abflusslöcher|排水穴の数
Hole Diameter|Diámetro del orificio|Diametro foro|Diamètre des trous|Lochdurchmesser|穴の直径
Ring Radius Ratio|Relación del radio del anillo|Rapporto raggio anello|Rapport du rayon d'anneau|Relativer Ringradius|穴配置の半径比
Saucer Inner Clearance|Holgura interior del plato|Gioco interno sottovaso|Jeu intérieur de soucoupe|Inneres Untersetzerspiel|受け皿の内側クリアランス
Saucer Rim Height|Altura del borde del plato|Altezza bordo sottovaso|Hauteur de soucoupe|Untersetzerrandhöhe|受け皿の縁高さ
Saucer Wall Thickness|Espesor de pared del plato|Spessore parete sottovaso|Épaisseur de paroi de soucoupe|Untersetzerwandstärke|受け皿の壁厚
Saucer Floor Thickness|Espesor del fondo del plato|Spessore fondo sottovaso|Épaisseur du fond de soucoupe|Untersetzerbodenstärke|受け皿の底厚
Inner Drainage Ribs|Estrías interiores de drenaje|Nervature interne di drenaggio|Rainures intérieures de drainage|Innere Drainagerippen|内側の排水リブ
Architectural Fluted|Columnas acanaladas|Colonne scanalate|Colonnes cannelées|Architektonische Kanneluren|建築的な縦溝
Twisted Helix|Hélice retorcida|Elica ritorta|Hélice torsadée|Gedrehte Helix|ねじれたらせん
Yoshimura Origami Diamond|Origami Yoshimura|Origami Yoshimura|Origami Yoshimura|Yoshimura-Origami|吉村パターンの折り紙
Cellular Coral|Coral celular|Corallo cellulare|Corail cellulaire|Zellkoralle|細胞状サンゴ
Minimalist Tulip|Tulipán minimalista|Tulipano minimalista|Tulipe minimaliste|Minimalistische Tulpe|ミニマルなチューリップ
Botanical Planter + Saucer|Macetero botánico + plato|Vaso botanico + sottovaso|Pot botanique + soucoupe|Pflanztopf + Untersetzer|植木鉢と受け皿
Hourglass Wave-Ribbed Hybrid|Reloj de arena con ondas y estrías|Clessidra con onde e nervature|Sablier à ondes et cannelures|Sanduhr mit Wellen und Rippen|波とリブの砂時計型
Low-Poly Geometric Crystal|Cristal geométrico facetado|Cristallo geometrico sfaccettato|Cristal géométrique facetté|Facettierter Kristall|多面体クリスタル
Hammered Zen Ceramic|Cerámica zen martillada|Ceramica zen martellata|Céramique zen martelée|Gehämmerte Zen-Keramik|槌目の禅陶器
Pleated Paper Lantern|Farol de papel plegado|Lanterna di carta pieghettata|Lanterne en papier plissé|Gefaltete Papierlaterne|折り目のある提灯
Mediterranean Amphora|Ánfora mediterránea|Anfora mediterranea|Amphore méditerranéenne|Mediterrane Amphore|地中海のアンフォラ
Flowing counter-helical ripples inspired by coastal dunes and ocean currents.|Ondas helicoidales opuestas inspiradas en dunas y corrientes marinas.|Onde elicoidali opposte ispirate a dune e correnti marine.|Ondulations hélicoïdales opposées inspirées des dunes et courants marins.|Gegenläufige Wellen nach dem Vorbild von Dünen und Meeresströmungen.|砂丘と海流に着想を得た、逆方向に流れるらせん状の波。
Crisp vertical architectural flutes with balanced flat fillets and clean shadow lines.|Estrías verticales arquitectónicas con perfiles equilibrados y sombras limpias.|Scanalature architettoniche verticali con profili equilibrati e ombre nette.|Cannelures architecturales verticales aux profils équilibrés et ombres nettes.|Klare vertikale Kanneluren mit ausgewogenen Stegen und Schattenlinien.|均整の取れた縦溝と明確な陰影を持つ建築的な造形。
Sweeping helical fins paired with a softened octagonal cross-section.|Aletas helicoidales sobre una sección octogonal suavizada.|Alette elicoidali su una sezione ottagonale arrotondata.|Ailettes hélicoïdales sur une section octogonale adoucie.|Geschwungene Helixrippen auf sanft gerundetem Achteck.|柔らかな八角形の断面と、流れるようならせん状のフィン。
Authentic staggered diamond origami facets with crisp Yoshimura paper creases.|Facetas de diamante alternadas con pliegues definidos Yoshimura.|Sfaccettature a diamante sfalsate con pieghe Yoshimura nette.|Facettes de losanges décalées aux plis Yoshimura marqués.|Versetzte Origami-Rauten mit klaren Yoshimura-Falten.|明確な吉村パターンの折り目を持つ、交互配置のひし形面。
Three-dimensional ridged veins inspired by reef coral and carved volcanic stone.|Vetas en relieve 3D inspiradas en coral y roca volcánica tallada.|Venature 3D ispirate a coralli e pietra vulcanica scolpita.|Veines en relief 3D inspirées du corail et de la pierre volcanique.|Dreidimensionale Adern nach Korallen und behauenem Vulkangestein.|サンゴ礁と彫刻された火山岩を思わせる、立体的な隆起模様。
Pure Scandinavian silhouette with a serene waist and gently flared tulip rim.|Silueta escandinava con cintura suave y borde de tulipán abierto.|Silhouette scandinava con vita morbida e bordo a tulipano svasato.|Silhouette scandinave épurée au col doux et bord évasé en tulipe.|Skandinavische Silhouette mit sanfter Taille und Tulpenrand.|穏やかなくびれとチューリップ状の縁を持つ北欧風の輪郭。
Sturdy shelled hollow planter with real drainage tunnels and matching drip saucer.|Macetero hueco robusto con drenaje real y plato a juego.|Vaso cavo robusto con fori di drenaggio reali e sottovaso abbinato.|Pot creux robuste avec drainage traversant et soucoupe assortie.|Stabiler hohler Pflanztopf mit echten Abflüssen und passendem Untersetzer.|実際の排水穴と対応する受け皿を備えた、丈夫な中空の植木鉢。
Dual-belly hourglass profile layering fine twisted ribs over gentle harmonic waves.|Perfil de reloj de arena con estrías finas sobre ondas suaves.|Profilo a clessidra con nervature sottili su onde armoniche.|Profil de sablier mêlant fines nervures torsadées et ondes douces.|Sanduhrprofil mit feinen gedrehten Rippen über sanften Wellen.|緩やかな波の上に細いねじれリブを重ねた、二つの膨らみのある砂時計型。
Gem-cut heptagonal crystal facets designed to showcase silk and dual-color filaments.|Cristal heptagonal facetado para filamentos de seda y bicolor.|Cristallo eptagonale sfaccettato per filamenti seta e bicolore.|Cristal heptagonal facetté pour filaments soyeux et bicolores.|Siebeneckige Kristallfacetten für Seiden- und Zweifarbfilamente.|シルクや二色フィラメントの美しさを引き出す七角形の結晶面。
Thick-walled wabi-sabi vessel with soft hammered dimples tailored for matte filaments.|Vaso wabi-sabi de paredes gruesas con suaves marcas martilladas.|Vaso wabi-sabi a pareti spesse con morbide impronte martellate.|Vase wabi-sabi épais aux creux martelés doux pour filaments mats.|Dickwandiges Wabi-Sabi-Gefäß mit sanften Hammerschlägen für matte Filamente.|マットなフィラメントに適した、厚い壁と柔らかな槌目の侘び寂び風の器。
Sharp accordion pleats crossed by subtle horizontal rings inspired by chochin lanterns.|Pliegues de acordeón con anillos sutiles inspirados en faroles chochin.|Pieghe a fisarmonica con anelli sottili ispirati alle lanterne chochin.|Plis d'accordéon et anneaux discrets inspirés des lanternes chōchin.|Klare Falten mit feinen Querringen nach Chōchin-Laternen.|提灯に着想を得た、鋭い蛇腹の折り目と繊細な水平リング。
Classical Greco-Roman proportions with a tapered foot, broad shoulder, and fine lathe ribs.|Proporciones grecorromanas con pie estrecho, hombros amplios y estrías finas.|Proporzioni greco-romane con piede affusolato, spalle ampie e scanalature fini.|Proportions gréco-romaines avec pied effilé, épaule large et fines stries.|Griechisch-römische Proportionen mit schmalem Fuß, breiter Schulter und feinen Rillen.|細い脚、広い肩、繊細なろくろ模様を備えた古典的なギリシャ・ローマ風の形。
Segments|Segmentos|Segmenti|Segments|Segmente|分割
Layers|Capas|Strati|Couches|Schichten|層
Count|Cantidad|Quantità|Nombre|Anzahl|個
Octaves|Octavas|Ottave|Octaves|Oktaven|オクターブ
Design Name|Nombre del proyecto|Nome del progetto|Nom du projet|Projektname|作品名
Language|Idioma|Lingua|Langue|Sprache|言語
Undo|Deshacer|Annulla|Annuler|Rückgängig|元に戻す
Redo|Rehacer|Ripeti|Rétablir|Wiederholen|やり直す
Reset|Restablecer|Ripristina|Réinitialiser|Zurücksetzen|初期値に戻す
Reset Camera|Restablecer cámara|Ripristina vista|Réinitialiser la vue|Kamera zurücksetzen|視点を初期化
Toggle Theme|Cambiar tema|Cambia tema|Changer le thème|Design wechseln|テーマ切替
Auto-Rotate|Giro automático|Rotazione automatica|Rotation automatique|Automatisch drehen|自動回転
New Seed|Nueva semilla|Nuovo seme|Nouvelle graine|Neuer Startwert|新しいシード
Open Exports Folder|Abrir carpeta de exportación|Apri cartella esportazioni|Ouvrir le dossier d'export|Exportordner öffnen|書き出しフォルダーを開く
Delete|Eliminar|Elimina|Supprimer|Löschen|削除
Preset name...|Nombre del modelo...|Nome preimpostazione...|Nom du préréglage...|Name der Vorlage...|プリセット名...
OrcaSlicer host bridge not connected (Standalone Preview).|Puente de OrcaSlicer no conectado (vista previa independiente).|Collegamento OrcaSlicer non connesso (anteprima autonoma).|Passerelle OrcaSlicer non connectée (aperçu autonome).|OrcaSlicer-Verbindung nicht hergestellt (eigenständige Vorschau).|OrcaSlicerとの接続がありません（単独プレビュー）。
Off|Desactivado|Disattivato|Désactivé|Aus|オフ
Default|Predeterminado|Predefinito|Par défaut|Standard|標準
Vase|Vaso|Vaso|Vase|Vase|花瓶
Saucer|Plato|Sottovaso|Soucoupe|Untersetzer|受け皿
XY dimensions ({a} x {b} mm) exceed build plate ({c} x {d} mm).|Las dimensiones XY ({a} x {b} mm) superan la mesa ({c} x {d} mm).|Le dimensioni XY ({a} x {b} mm) superano il piatto ({c} x {d} mm).|Les dimensions XY ({a} x {b} mm) dépassent le plateau ({c} x {d} mm).|XY-Abmessungen ({a} x {b} mm) überschreiten die Druckplatte ({c} x {d} mm).|XY寸法（{a} x {b} mm）がプレート（{c} x {d} mm）を超えています。
Height ({a} mm) exceeds printer Z limit ({b} mm).|La altura ({a} mm) supera el límite Z ({b} mm).|L'altezza ({a} mm) supera il limite Z ({b} mm).|La hauteur ({a} mm) dépasse la limite Z ({b} mm).|Höhe ({a} mm) überschreitet die Z-Grenze ({b} mm).|高さ（{a} mm）がZ上限（{b} mm）を超えています。
Critical overhang of {a}° ({b}% of wall > 55°). Enable 'Auto-Clamp Overhang' or reduce texture depth.|Voladizo crítico de {a}° ({b}% de pared > 55°). Activa el límite de voladizo o reduce la textura.|Sbalzo critico di {a}° ({b}% della parete > 55°). Attiva il limite sbalzi o riduci la texture.|Surplomb critique de {a}° ({b}% de paroi > 55°). Activez la limitation ou réduisez la texture.|Kritischer Überhang {a}° ({b}% der Wand > 55°). Begrenzung aktivieren oder Texturtiefe verringern.|重大なオーバーハング {a}°（壁の{b}%が55°超）。自動制限を有効にするかテクスチャの深さを減らしてください。
Moderate overhang of {a}° ({b}% > 45°). Ensure strong part cooling.|Voladizo moderado de {a}° ({b}% > 45°). Asegura una buena refrigeración.|Sbalzo moderato di {a}° ({b}% > 45°). Assicura un buon raffreddamento.|Surplomb modéré de {a}° ({b}% > 45°). Assurez un bon refroidissement.|Mäßiger Überhang {a}° ({b}% > 45°). Gute Bauteilkühlung sicherstellen.|中程度のオーバーハング {a}°（{b}%が45°超）。十分に冷却してください。
Gap risk in Spiral Vase mode (stepover exceeds {a} mm line width). Increase spiral line width, lower layer height, or switch to Shelled Hollow mode.|Riesgo de huecos en espiral (paso lateral > ancho {a} mm). Aumenta la línea, baja la capa o usa modo hueco.|Rischio di fessure in spirale (passo laterale > larghezza {a} mm). Allarga la linea, riduci lo strato o usa il modo cavo.|Risque de fentes en spirale (pas latéral > largeur {a} mm). Élargissez la ligne, réduisez la couche ou utilisez le mode creux.|Spaltgefahr im Spiralmodus (seitlicher Schritt > {a} mm Linienbreite). Breite erhöhen, Schicht senken oder Hohlmodus wählen.|スパイラルに隙間が生じるおそれ（横方向の移動量が線幅{a} mm超）。線幅を広げるか層高を下げるか中空モードに切り替えてください。
Spiral line width ({a} mm) exceeds 2x nozzle diameter ({b} mm).|El ancho espiral ({a} mm) supera 2x la boquilla ({b} mm).|La larghezza spirale ({a} mm) supera 2x l'ugello ({b} mm).|La largeur spirale ({a} mm) dépasse 2x la buse ({b} mm).|Spirallinienbreite ({a} mm) überschreitet 2x Düsendurchmesser ({b} mm).|スパイラル線幅（{a} mm）がノズル直径（{b} mm）の2倍を超えています。
Wall thickness ({a} mm) is thin for dual perimeters ({b} mm).|La pared ({a} mm) es fina para dos perímetros ({b} mm).|La parete ({a} mm) è sottile per due perimetri ({b} mm).|La paroi ({a} mm) est mince pour deux périmètres ({b} mm).|Wandstärke ({a} mm) ist zu dünn für zwei Bahnen ({b} mm).|壁厚（{a} mm）が2周分（{b} mm）には不足しています。
Tall slender aspect ratio — consider enabling a Brim in OrcaSlicer for extra bed adhesion.|Forma alta y estrecha: considera un borde de adhesión en OrcaSlicer.|Forma alta e stretta: valuta un brim in OrcaSlicer per l'adesione.|Forme haute et étroite : envisagez une bordure d'adhérence dans OrcaSlicer.|Hohes schlankes Modell: Brim in OrcaSlicer für bessere Haftung erwägen.|細長い形状です。接着性を高めるためOrcaSlicerのブリムを検討してください。
Exported successfully: {name}|Exportado correctamente: {name}|Esportazione riuscita: {name}|Export réussi : {name}|Erfolgreich exportiert: {name}|書き出しました：{name}
Sent to OrcaSlicer Plater ({n} object(s)).|Enviado a la mesa de OrcaSlicer ({n} objetos).|Inviato al piatto OrcaSlicer ({n} oggetti).|Envoyé au plateau OrcaSlicer ({n} objets).|An OrcaSlicer-Druckplatte gesendet ({n} Objekte).|OrcaSlicerへ送信しました（{n}オブジェクト）。
Exports folder: {path}|Carpeta de exportación: {path}|Cartella esportazioni: {path}|Dossier d'export : {path}|Exportordner: {path}|書き出しフォルダー：{path}
 (open-mouthed {mm} mm shell)| (pared abierta de {mm} mm)| (parete aperta da {mm} mm)| (paroi ouverte de {mm} mm)| (offene Hülle mit {mm} mm)|（開口した壁厚{mm} mm）
 (Converted to open hollow shell to slice vase + saucer together.)| (Convertido a hueco abierto para laminar vaso y plato juntos.)| (Convertito in cavo aperto per affettare vaso e sottovaso insieme.)| (Converti en creux ouvert pour trancher vase et soucoupe ensemble.)| (Für gemeinsames Slicing von Vase und Untersetzer in offene Hülle umgewandelt.)|（花瓶と受け皿を同時にスライスするため開口した中空に変換しました。）
"""


def locale_rows() -> list[list[str]]:
    rows = []
    for line in _VOCABULARY.strip().splitlines():
        source, *translations = line.split("|")
        if len(translations) != 5 or not all(translations):
            raise ValueError("Invalid offline translation row")
        rows.append([source, *translations])
    return rows


def locale_vocabulary() -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {code: {} for code in SUPPORTED_LANGUAGES[2:]}
    for source, *translations in locale_rows():
        for code, text in zip(SUPPORTED_LANGUAGES[2:], translations, strict=True):
            result[code][source] = text
    return result


def translate_text(text: str, language: object) -> str:
    code = normalize_language(language)
    return locale_vocabulary().get(code, {}).get(text, text)

# ===========================================================================
# MODULE: vase_studio.schema
# ===========================================================================

"""Unified parameter schema and validation for Orca Vase Studio."""

pass  # [bundled] hoisted __future__ import

import copy
import math
from typing import Any

SCHEMA_VERSION = "1.0"

DEFAULT_PARAMS: dict[str, Any] = {
    "name": "Ondas Organicas",
    "height_mm": 160.0,              # [30.0, 500.0]
    "base_diameter_mm": 76.0,        # [20.0, 450.0]
    "belly_diameter_mm": 110.0,      # [20.0, 450.0]
    "belly_height_ratio": 0.34,      # [0.08, 0.85]
    "waist_diameter_mm": 68.0,       # [16.0, 450.0]
    "waist_height_ratio": 0.68,      # [0.15, 0.92]
    "neck_diameter_mm": 82.0,        # [16.0, 450.0]
    "lip_flare_mm": 4.0,             # [-15.0, 25.0] extra radius added smoothly over top 8% (z_norm 0.92..1.0)
    "lip_bevel_mm": 1.0,             # [0.0, 4.0] subtle top rim rounding/bevel
    "polygon_sides": 0,              # 0 = smooth circle; 3..24 = polygonal cross-section
    "polygon_roundness": 0.35,       # [0.0, 1.0] blends polygon radius toward circle (1.0 = pure circle)
    "use_custom_profile": False,     # bool: when True, base silhouette comes from profile_points instead of base/belly/waist/neck
    "profile_points": [              # list of [z_norm (0..1), radius_mm (8..225)], >= 2 points, endpoints clamped to z=0.0 and z=1.0
        [0.0, 38.0],
        [0.34, 55.0],
        [0.68, 34.0],
        [0.92, 41.0],
        [1.0, 45.0],
    ],
    "resolution_angular": 240,       # [64, 360]
    "resolution_vertical": 220,      # [60, 400]

    # Global texture envelope & helical twist
    "bottom_fade_mm": 8.0,           # [0.0, 60.0] smoothstep 0->1 from z=0 to z=bottom_fade_mm (flat bed adhesion!)
    "top_fade_mm": 6.0,              # [0.0, 60.0] smoothstep 1->0 from z=(H - top_fade_mm) to z=H
    "global_twist_deg": 0.0,         # [-720.0, 720.0]

    # Combinable Surface Texture Layers (summed radial displacement in mm)
    "textures": {
        "ribbed": {
            "enabled": False,
            "depth_mm": 2.6,         # [-15.0, 15.0]
            "count": 32,             # [3, 180] circumferential rib count (density)
            "duty_cycle": 0.50,      # [0.10, 0.90] width of rib vs flat spacing gap
            "sharpness": 0.35,       # [0.0, 1.0] 0=smooth cosine, 0.5=rounded flute, 1.0=sharp triangular/chiseled
            "twist_deg": 60.0,       # [-720.0, 720.0]
            "phase_deg": 0.0,        # [0.0, 360.0]
        },
        "waves": {
            "enabled": True,
            "depth_mm": 3.0,         # [-15.0, 15.0]
            "vertical_wavelength_mm": 26.0,  # [4.0, 120.0] vertical wave spacing in mm
            "angular_lobes": 6,      # [0, 48] circumferential wave count
            "interference_mix": 0.45,  # [0.0, 1.0] mix of counter-helical wave creating organic woven/ripple pockets
            "wave_skew": 0.0,        # [-0.8, 0.8]
            "phase_deg": 0.0,        # [0.0, 360.0]
        },
        "origami": {
            "enabled": False,
            "depth_mm": 3.2,         # [-15.0, 15.0]
            "cells_around": 12,      # [3, 60] horizontal diamond density
            "cells_vertical": 8,     # [2, 50] vertical diamond tiers
            "crease_sharpness": 0.75,  # [0.0, 1.0]
            "stagger": 0.50,         # [0.0, 1.0]
        },
        "cellular": {
            "enabled": False,
            "depth_mm": 2.4,         # [-12.0, 12.0]
            "scale_angular": 8,      # [2, 40] cells around circumference
            "scale_vertical_mm": 22.0,  # [5.0, 100.0] vertical cell spacing in mm
            "ridge_mode": True,      # bool: True = ridged coral/stone veins, False = smooth organic billows
            "octaves": 2,            # [1, 4]
            "seed": 42,              # [1, 99999]
        },
    },

    # Printability & Wall Structure
    "print_mode": "shelled_hollow",  # "shelled_hollow" | "spiral_vase"
    "stl_always_open_hollow": True,  # keep open mouth when exporting .stl even if spiral_vase is selected
    "auto_configure_slicer": True,
    "spiral_line_width_mm": 0.65,    # [0.40, 1.20]
    "spiral_bottom_layers": 5,       # [2, 15]
    "spiral_smooth": True,
    "wall_thickness_mm": 2.4,        # [0.8, 25.0] used when print_mode == "shelled_hollow"
    "bottom_thickness_mm": 3.2,      # [1.0, 25.0] used when print_mode == "shelled_hollow"
    "auto_clamp_overhang": False,
    "max_safe_overhang_deg": 48.0,   # [35.0, 65.0]

    # Gardening: Drainage & Matching Saucer
    "drainage": {
        "enabled": False,
        "hole_count": 4,             # [1, 9]
        "hole_diameter_mm": 8.0,     # [3.0, 20.0]
        "ring_radius_ratio": 0.48,   # [0.0, 0.68]
    },
    "saucer": {
        "clearance_mm": 8.0,         # [3.0, 25.0]
        "rim_height_mm": 22.0,       # [10.0, 60.0]
        "wall_thickness_mm": 2.4,    # [1.2, 5.0]
        "floor_thickness_mm": 2.6,   # [1.2, 6.0]
        "inner_ribs_height_mm": 2.0, # [0.0, 6.0] raised drainage ribs inside saucer floor
        "match_vase_texture": True,
    },
}


def _to_float(val: Any, default: float, lo: float, hi: float) -> float:
    if isinstance(val, bool):
        return default
    try:
        f = float(val)
    except (TypeError, ValueError):
        return default
    if not math.isfinite(f):
        return default
    return max(lo, min(hi, f))


def _to_int(val: Any, default: int, lo: int, hi: int) -> int:
    if isinstance(val, bool):
        return default
    try:
        f = float(val)
    except (TypeError, ValueError):
        return default
    if not math.isfinite(f):
        return default
    i = int(round(f))
    return max(lo, min(hi, i))


def _to_bool(val: Any, default: bool) -> bool:
    if isinstance(val, bool):
        return val
    if isinstance(val, (int, float)):
        if math.isfinite(val):
            return bool(val)
        return default
    if isinstance(val, str):
        s = val.strip().lower()
        if s in ("true", "1", "yes", "on"):
            return True
        if s in ("false", "0", "no", "off", ""):
            return False
    return default


def _normalize_profile_points(raw_pts: Any) -> list[list[float]]:
    default_pts = copy.deepcopy(DEFAULT_PARAMS["profile_points"])
    if not isinstance(raw_pts, (list, tuple)) or len(raw_pts) < 2:
        return default_pts

    parsed: list[list[float]] = []
    for item in raw_pts:
        z_raw: Any = None
        r_raw: Any = None
        if isinstance(item, (list, tuple)) and len(item) >= 2:
            z_raw, r_raw = item[0], item[1]
        elif isinstance(item, dict):
            z_raw = item.get("z", item.get("z_norm"))
            r_raw = item.get("r", item.get("radius_mm", item.get("radius")))
        else:
            continue

        z_val = _to_float(z_raw, -1.0, 0.0, 1.0)
        r_val = _to_float(r_raw, -1.0, 8.0, 225.0)
        if z_raw is None or r_raw is None:
            continue
        try:
            zf = float(z_raw)
            rf = float(r_raw)
            if not (math.isfinite(zf) and math.isfinite(rf)):
                continue
        except (TypeError, ValueError):
            continue
        parsed.append([max(0.0, min(1.0, zf)), max(8.0, min(225.0, rf))])

    if len(parsed) < 2:
        return default_pts

    parsed.sort(key=lambda p: p[0])
    parsed[0][0] = 0.0
    parsed[-1][0] = 1.0

    # Deduplicate near-identical z_norm knots so PCHIP never divides by zero
    cleaned: list[list[float]] = [parsed[0]]
    for pt in parsed[1:]:
        if pt[0] - cleaned[-1][0] < 1e-4:
            if pt[0] >= 1.0:
                cleaned[-1] = [1.0, pt[1]]
            else:
                cleaned[-1][1] = 0.5 * (cleaned[-1][1] + pt[1])
        else:
            cleaned.append(pt)

    if len(cleaned) < 2:
        return default_pts
    cleaned[0][0] = 0.0
    cleaned[-1][0] = 1.0
    return cleaned


def _deep_merge_dict(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    for k, v in override.items():
        if k in base and isinstance(base[k], dict) and isinstance(v, dict):
            _deep_merge_dict(base[k], v)
        elif k in base:
            base[k] = v
    return base


def normalize_params(raw: dict[str, Any] | None) -> dict[str, Any]:
    """Deep-copy DEFAULT_PARAMS, merge raw recursively, coerce types, and clamp bounds."""
    out = copy.deepcopy(DEFAULT_PARAMS)
    if isinstance(raw, dict):
        _deep_merge_dict(out, raw)

    # Top-level string & mode fields
    raw_name = out.get("name")
    if isinstance(raw_name, str) and raw_name.strip():
        out["name"] = raw_name.strip()[:120]
    else:
        out["name"] = DEFAULT_PARAMS["name"]

    d = DEFAULT_PARAMS
    out["height_mm"] = _to_float(out["height_mm"], d["height_mm"], 30.0, 500.0)
    out["base_diameter_mm"] = _to_float(out["base_diameter_mm"], d["base_diameter_mm"], 20.0, 450.0)
    out["belly_diameter_mm"] = _to_float(out["belly_diameter_mm"], d["belly_diameter_mm"], 20.0, 450.0)
    out["belly_height_ratio"] = _to_float(out["belly_height_ratio"], d["belly_height_ratio"], 0.08, 0.85)
    out["waist_diameter_mm"] = _to_float(out["waist_diameter_mm"], d["waist_diameter_mm"], 16.0, 450.0)
    out["waist_height_ratio"] = _to_float(out["waist_height_ratio"], d["waist_height_ratio"], 0.15, 0.92)
    out["neck_diameter_mm"] = _to_float(out["neck_diameter_mm"], d["neck_diameter_mm"], 16.0, 450.0)
    out["lip_flare_mm"] = _to_float(out["lip_flare_mm"], d["lip_flare_mm"], -15.0, 25.0)
    out["lip_bevel_mm"] = _to_float(out["lip_bevel_mm"], d["lip_bevel_mm"], 0.0, 4.0)

    poly_sides = _to_int(out["polygon_sides"], d["polygon_sides"], 0, 24)
    out["polygon_sides"] = 0 if poly_sides < 3 else poly_sides
    out["polygon_roundness"] = _to_float(out["polygon_roundness"], d["polygon_roundness"], 0.0, 1.0)

    out["use_custom_profile"] = _to_bool(out["use_custom_profile"], d["use_custom_profile"])
    out["profile_points"] = _normalize_profile_points(out.get("profile_points"))

    out["resolution_angular"] = _to_int(out["resolution_angular"], d["resolution_angular"], 64, 360)
    out["resolution_vertical"] = _to_int(out["resolution_vertical"], d["resolution_vertical"], 60, 400)

    out["bottom_fade_mm"] = _to_float(out["bottom_fade_mm"], d["bottom_fade_mm"], 0.0, 60.0)
    out["top_fade_mm"] = _to_float(out["top_fade_mm"], d["top_fade_mm"], 0.0, 60.0)
    out["global_twist_deg"] = _to_float(out["global_twist_deg"], d["global_twist_deg"], -720.0, 720.0)

    # Textures
    tex = out["textures"]
    dt = d["textures"]

    rib = tex["ribbed"]
    d_rib = dt["ribbed"]
    rib["enabled"] = _to_bool(rib["enabled"], d_rib["enabled"])
    rib["depth_mm"] = _to_float(rib["depth_mm"], d_rib["depth_mm"], -15.0, 15.0)
    rib["count"] = _to_int(rib["count"], d_rib["count"], 3, 180)
    rib["duty_cycle"] = _to_float(rib["duty_cycle"], d_rib["duty_cycle"], 0.10, 0.90)
    rib["sharpness"] = _to_float(rib["sharpness"], d_rib["sharpness"], 0.0, 1.0)
    rib["twist_deg"] = _to_float(rib["twist_deg"], d_rib["twist_deg"], -720.0, 720.0)
    rib["phase_deg"] = _to_float(rib["phase_deg"], d_rib["phase_deg"], 0.0, 360.0)

    wav = tex["waves"]
    d_wav = dt["waves"]
    wav["enabled"] = _to_bool(wav["enabled"], d_wav["enabled"])
    wav["depth_mm"] = _to_float(wav["depth_mm"], d_wav["depth_mm"], -15.0, 15.0)
    wav["vertical_wavelength_mm"] = _to_float(wav["vertical_wavelength_mm"], d_wav["vertical_wavelength_mm"], 4.0, 120.0)
    wav["angular_lobes"] = _to_int(wav["angular_lobes"], d_wav["angular_lobes"], 0, 48)
    wav["interference_mix"] = _to_float(wav["interference_mix"], d_wav["interference_mix"], 0.0, 1.0)
    wav["wave_skew"] = _to_float(wav["wave_skew"], d_wav["wave_skew"], -0.8, 0.8)
    wav["phase_deg"] = _to_float(wav["phase_deg"], d_wav["phase_deg"], 0.0, 360.0)

    ori = tex["origami"]
    d_ori = dt["origami"]
    ori["enabled"] = _to_bool(ori["enabled"], d_ori["enabled"])
    ori["depth_mm"] = _to_float(ori["depth_mm"], d_ori["depth_mm"], -15.0, 15.0)
    ori["cells_around"] = _to_int(ori["cells_around"], d_ori["cells_around"], 3, 60)
    ori["cells_vertical"] = _to_int(ori["cells_vertical"], d_ori["cells_vertical"], 2, 50)
    ori["crease_sharpness"] = _to_float(ori["crease_sharpness"], d_ori["crease_sharpness"], 0.0, 1.0)
    ori["stagger"] = _to_float(ori["stagger"], d_ori["stagger"], 0.0, 1.0)

    cel = tex["cellular"]
    d_cel = dt["cellular"]
    cel["enabled"] = _to_bool(cel["enabled"], d_cel["enabled"])
    cel["depth_mm"] = _to_float(cel["depth_mm"], d_cel["depth_mm"], -12.0, 12.0)
    cel["scale_angular"] = _to_int(cel["scale_angular"], d_cel["scale_angular"], 2, 40)
    cel["scale_vertical_mm"] = _to_float(cel["scale_vertical_mm"], d_cel["scale_vertical_mm"], 5.0, 100.0)
    cel["ridge_mode"] = _to_bool(cel["ridge_mode"], d_cel["ridge_mode"])
    cel["octaves"] = _to_int(cel["octaves"], d_cel["octaves"], 1, 4)
    cel["seed"] = _to_int(cel["seed"], d_cel["seed"], 1, 99999)

    # Printability & Wall Structure
    pm = str(out.get("print_mode", d["print_mode"])).strip().lower()
    out["print_mode"] = pm if pm in ("spiral_vase", "shelled_hollow") else d["print_mode"]
    out["stl_always_open_hollow"] = _to_bool(out["stl_always_open_hollow"], d["stl_always_open_hollow"])
    out["auto_configure_slicer"] = _to_bool(out["auto_configure_slicer"], d["auto_configure_slicer"])
    out["spiral_line_width_mm"] = _to_float(out["spiral_line_width_mm"], d["spiral_line_width_mm"], 0.40, 1.20)
    out["spiral_bottom_layers"] = _to_int(out["spiral_bottom_layers"], d["spiral_bottom_layers"], 2, 15)
    out["spiral_smooth"] = _to_bool(out["spiral_smooth"], d["spiral_smooth"])
    out["wall_thickness_mm"] = _to_float(out["wall_thickness_mm"], d["wall_thickness_mm"], 0.8, 25.0)
    out["bottom_thickness_mm"] = _to_float(out["bottom_thickness_mm"], d["bottom_thickness_mm"], 1.0, 25.0)
    out["auto_clamp_overhang"] = _to_bool(out["auto_clamp_overhang"], d["auto_clamp_overhang"])
    out["max_safe_overhang_deg"] = _to_float(out["max_safe_overhang_deg"], d["max_safe_overhang_deg"], 35.0, 65.0)

    # Drainage
    dr = out["drainage"]
    d_dr = d["drainage"]
    dr["enabled"] = _to_bool(dr["enabled"], d_dr["enabled"])
    dr["hole_count"] = _to_int(dr["hole_count"], d_dr["hole_count"], 1, 9)
    dr["hole_diameter_mm"] = _to_float(dr["hole_diameter_mm"], d_dr["hole_diameter_mm"], 3.0, 20.0)
    dr["ring_radius_ratio"] = _to_float(dr["ring_radius_ratio"], d_dr["ring_radius_ratio"], 0.0, 0.68)

    # Saucer
    sc = out["saucer"]
    d_sc = d["saucer"]
    sc["clearance_mm"] = _to_float(sc["clearance_mm"], d_sc["clearance_mm"], 3.0, 25.0)
    sc["rim_height_mm"] = _to_float(sc["rim_height_mm"], d_sc["rim_height_mm"], 10.0, 60.0)
    sc["wall_thickness_mm"] = _to_float(sc["wall_thickness_mm"], d_sc["wall_thickness_mm"], 1.2, 5.0)
    sc["floor_thickness_mm"] = _to_float(sc["floor_thickness_mm"], d_sc["floor_thickness_mm"], 1.2, 6.0)
    sc["inner_ribs_height_mm"] = _to_float(sc["inner_ribs_height_mm"], d_sc["inner_ribs_height_mm"], 0.0, 6.0)
    sc["match_vase_texture"] = _to_bool(sc["match_vase_texture"], d_sc["match_vase_texture"])

    return out

# ===========================================================================
# MODULE: vase_studio.mesh_generator
# ===========================================================================

"""Parametric 3D vase and saucer manifold mesh generator for Orca Vase Studio."""

pass  # [bundled] hoisted __future__ import

from dataclasses import dataclass
import math
from typing import Any

try:
    import numpy as np
except ModuleNotFoundError:
    import os as _os
    from pathlib import Path as _Path
    import sys as _sys

    if _sys.platform == "win32":
        _appdata = _os.environ.get("APPDATA", "").strip()
        _orca_base = _Path(_appdata) / "OrcaSlicer" if _appdata else _Path.home() / "AppData" / "Roaming" / "OrcaSlicer"
    elif _sys.platform == "darwin":
        _orca_base = _Path.home() / "Library" / "Application Support" / "OrcaSlicer"
    else:
        _xdg = _os.environ.get("XDG_CONFIG_HOME", "").strip()
        _orca_base = (_Path(_xdg) if _xdg else (_Path.home() / ".config")) / "OrcaSlicer"

    _orca_pkg_dir = str(_orca_base / "python" / "packages" / f"cp{_sys.version_info.major}{_sys.version_info.minor}")
    if _orca_pkg_dir not in _sys.path:
        _sys.path.insert(0, _orca_pkg_dir)
    import numpy as np

pass  # [bundled] resolved intra-package import


@dataclass
class MeshData:
    vertices: np.ndarray      # float32, shape (V, 3), min Z == 0.0, centered at X=0, Y=0
    triangles: np.ndarray     # int32, shape (F, 3), outward CCW winding (right-hand rule)
    face_normals: np.ndarray  # float32, shape (F, 3), unit normals
    bounds_mm: dict[str, list[float]]  # {"min": [x,y,z], "max": [x,y,z], "size": [dx,dy,dz]}
    volume_cm3: float


# ---------------------------------------------------------------------------
# Section 2: Shared Mathematical Surface Evaluation (Python <-> WebGL2 Parity)
# ---------------------------------------------------------------------------

def _smoothstep(edge0: float, edge1: float, x: np.ndarray) -> np.ndarray:
    span = edge1 - edge0
    if span <= 1e-9:
        return np.where(x > edge0, 1.0, 0.0)
    u = np.clip((x - edge0) / span, 0.0, 1.0)
    return u * u * (3.0 - 2.0 * u)


def _prepare_knots(params: dict[str, Any]) -> tuple[np.ndarray, np.ndarray]:
    if params["use_custom_profile"]:
        raw = [[float(p[0]), float(p[1])] for p in params["profile_points"]]
    else:
        r_base = 0.5 * float(params["base_diameter_mm"])
        r_belly = 0.5 * float(params["belly_diameter_mm"])
        r_waist = 0.5 * float(params["waist_diameter_mm"])
        r_neck = 0.5 * float(params["neck_diameter_mm"])
        r_lip = max(4.0, r_neck + float(params["lip_flare_mm"]))
        raw = [
            [0.0, r_base],
            [float(params["belly_height_ratio"]), r_belly],
            [float(params["waist_height_ratio"]), r_waist],
            [0.92, r_neck],
            [1.0, r_lip],
        ]

    raw.sort(key=lambda pair: pair[0])
    raw[0][0] = 0.0
    raw[-1][0] = 1.0

    # Ensure strictly increasing z_norm knots so PCHIP never divides by zero
    dedup: list[list[float]] = [raw[0]]
    for z_k, r_k in raw[1:]:
        if z_k - dedup[-1][0] < 1e-4:
            if z_k >= 1.0:
                dedup[-1] = [1.0, r_k]
            else:
                dedup[-1][1] = 0.5 * (dedup[-1][1] + r_k)
        else:
            dedup.append([z_k, r_k])

    if len(dedup) < 2:
        dedup = [[0.0, raw[0][1]], [1.0, raw[-1][1]]]

    xs = np.array([p[0] for p in dedup], dtype=np.float64)
    ys = np.array([p[1] for p in dedup], dtype=np.float64)
    return xs, ys


def _pchip_interpolate(xs: np.ndarray, ys: np.ndarray, x_eval: np.ndarray) -> np.ndarray:
    """Monotone Piecewise Cubic Hermite Interpolating Polynomial (Fritsch-Carlson / PCHIP)."""
    m = len(xs)
    if m == 2:
        t = np.clip((x_eval - xs[0]) / max(xs[1] - xs[0], 1e-9), 0.0, 1.0)
        return ys[0] + t * (ys[1] - ys[0])

    h = np.diff(xs)
    delta = np.diff(ys) / h
    d = np.zeros(m, dtype=np.float64)

    # Interior slopes: weighted harmonic mean when adjacent secants share sign
    for k in range(1, m - 1):
        if delta[k - 1] * delta[k] > 0.0:
            w1 = 2.0 * h[k] + h[k - 1]
            w2 = h[k] + 2.0 * h[k - 1]
            d[k] = (w1 + w2) / (w1 / delta[k - 1] + w2 / delta[k])
        else:
            d[k] = 0.0

    # Shape-preserving endpoint slopes
    d0 = ((2.0 * h[0] + h[1]) * delta[0] - h[0] * delta[1]) / (h[0] + h[1])
    if d0 * delta[0] <= 0.0:
        d0 = 0.0
    elif (delta[0] * delta[1] <= 0.0) and (abs(d0) > abs(3.0 * delta[0])):
        d0 = 3.0 * delta[0]
    d[0] = d0

    dn = ((2.0 * h[-1] + h[-2]) * delta[-1] - h[-1] * delta[-2]) / (h[-1] + h[-2])
    if dn * delta[-1] <= 0.0:
        dn = 0.0
    elif (delta[-1] * delta[-2] <= 0.0) and (abs(dn) > abs(3.0 * delta[-1])):
        dn = 3.0 * delta[-1]
    d[-1] = dn

    x_clamped = np.clip(x_eval, xs[0], xs[-1])
    idx = np.searchsorted(xs, x_clamped, side="right") - 1
    idx = np.clip(idx, 0, m - 2)

    hk = h[idx]
    t = (x_clamped - xs[idx]) / hk
    t2 = t * t
    t3 = t2 * t

    h00 = 2.0 * t3 - 3.0 * t2 + 1.0
    h10 = t3 - 2.0 * t2 + t
    h01 = -2.0 * t3 + 3.0 * t2
    h11 = t3 - t2

    return h00 * ys[idx] + h10 * hk * d[idx] + h01 * ys[idx + 1] + h11 * hk * d[idx + 1]


def _hash3_u32(ix: np.ndarray, iy: np.ndarray, iz: np.ndarray, seed: int) -> np.ndarray:
    """Deterministic 32-bit integer hash matching JS Math.imul bit-for-bit."""
    ux = ix.astype(np.int64).astype(np.uint32)
    uy = iy.astype(np.int64).astype(np.uint32)
    uz = iz.astype(np.int64).astype(np.uint32)
    us = np.uint32(int(seed) & 0xFFFFFFFF)

    with np.errstate(over="ignore"):
        h = (
            ux * np.uint32(374761393)
            + uy * np.uint32(668265263)
            + uz * np.uint32(1274126177)
            + us * np.uint32(1597334677)
        )
        h = h ^ (h >> np.uint32(13))
        h = h * np.uint32(1274126177)
        h = h ^ (h >> np.uint32(16))

    return h.astype(np.float64) / 4294967295.0


def _value_noise_3d(cx: np.ndarray, cy: np.ndarray, cz: np.ndarray, octaves: int, seed: int) -> np.ndarray:
    total = np.zeros_like(cx, dtype=np.float64)
    amp_sum = 0.0
    freq = 1.0
    amp = 1.0

    for oct_idx in range(max(1, int(octaves))):
        x = cx * freq
        y = cy * freq
        z = cz * freq

        ix0 = np.floor(x).astype(np.int64)
        iy0 = np.floor(y).astype(np.int64)
        iz0 = np.floor(z).astype(np.int64)

        fx = x - ix0
        fy = y - iy0
        fz = z - iz0

        ux = fx * fx * (3.0 - 2.0 * fx)
        uy = fy * fy * (3.0 - 2.0 * fy)
        uz = fz * fz * (3.0 - 2.0 * fz)

        s_oct = int(seed)
        c000 = _hash3_u32(ix0, iy0, iz0, s_oct)
        c100 = _hash3_u32(ix0 + 1, iy0, iz0, s_oct)
        c010 = _hash3_u32(ix0, iy0 + 1, iz0, s_oct)
        c110 = _hash3_u32(ix0 + 1, iy0 + 1, iz0, s_oct)
        c001 = _hash3_u32(ix0, iy0, iz0 + 1, s_oct)
        c101 = _hash3_u32(ix0 + 1, iy0, iz0 + 1, s_oct)
        c011 = _hash3_u32(ix0, iy0 + 1, iz0 + 1, s_oct)
        c111 = _hash3_u32(ix0 + 1, iy0 + 1, iz0 + 1, s_oct)

        nx00 = c000 + ux * (c100 - c000)
        nx10 = c010 + ux * (c110 - c010)
        nx01 = c001 + ux * (c101 - c001)
        nx11 = c011 + ux * (c111 - c011)

        nxy0 = nx00 + uy * (nx10 - nx00)
        nxy1 = nx01 + uy * (nx11 - nx01)

        n_val = nxy0 + uz * (nxy1 - nxy0)
        total += amp * n_val
        amp_sum += amp
        freq *= 2.0
        amp *= 0.5

    return total / max(amp_sum, 1e-9)


def _compute_texture_displacement(
    z_grid: np.ndarray,
    z_norm_grid: np.ndarray,
    theta_grid: np.ndarray,
    theta_g: np.ndarray,
    textures: dict[str, Any],
    global_twist_rad: float,
) -> np.ndarray:
    dr = np.zeros_like(theta_g, dtype=np.float64)

    rib = textures["ribbed"]
    if rib["enabled"] and abs(rib["depth_mm"]) > 1e-9:
        count = float(rib["count"])
        duty = float(rib["duty_cycle"])
        sharp = float(rib["sharpness"])
        twist_rad = math.radians(float(rib["twist_deg"]))
        phase_rad = math.radians(float(rib["phase_deg"]))

        phi = np.mod((theta_grid + twist_rad * z_norm_grid + phase_rad) * count / (2.0 * math.pi), 1.0)
        u = np.abs(phi - 0.5) * 2.0
        t = np.clip(u / max(duty, 1e-6), 0.0, 1.0)
        w_smooth = 0.5 * (1.0 + np.cos(math.pi * t))
        w_sharp = 1.0 - t
        shape = (1.0 - sharp) * w_smooth + sharp * w_sharp
        dr += float(rib["depth_mm"]) * shape

    wav = textures["waves"]
    if wav["enabled"] and abs(wav["depth_mm"]) > 1e-9:
        wl = max(float(wav["vertical_wavelength_mm"]), 1.0)
        lobes = float(wav["angular_lobes"])
        mix = float(wav["interference_mix"])
        skew = float(wav["wave_skew"])
        phase_rad = math.radians(float(wav["phase_deg"]))

        kz = (2.0 * math.pi * z_grid / wl) + phase_rad
        ka = lobes * theta_grid + global_twist_rad * z_norm_grid
        w1 = np.sin(kz + ka + skew * np.sin(kz))
        w2 = np.sin(kz - ka)
        dr += float(wav["depth_mm"]) * ((1.0 - 0.5 * mix) * w1 + 0.5 * mix * w2)

    ori = textures["origami"]
    if ori["enabled"] and abs(ori["depth_mm"]) > 1e-9:
        c_around = float(ori["cells_around"])
        c_vert = float(ori["cells_vertical"])
        crease = float(ori["crease_sharpness"])
        stagger = float(ori["stagger"])

        v = z_norm_grid * c_vert
        tier = np.floor(v)
        fv = v - tier
        u = (theta_grid / (2.0 * math.pi)) * c_around + tier * stagger
        fu = u - np.floor(u)

        diamond = 1.0 - (np.abs(2.0 * fu - 1.0) + np.abs(2.0 * fv - 1.0))
        soft = np.sin(math.pi * (fu - 0.5)) * np.sin(math.pi * (fv - 0.5))
        val = crease * diamond + (1.0 - crease) * soft
        dr += float(ori["depth_mm"]) * val

    cel = textures["cellular"]
    if cel["enabled"] and abs(cel["depth_mm"]) > 1e-9:
        s_ang = float(cel["scale_angular"])
        s_vert = max(float(cel["scale_vertical_mm"]), 1.0)
        octaves = int(cel["octaves"])
        seed = int(cel["seed"])
        ridge = bool(cel["ridge_mode"])

        cyl_scale = s_ang / (2.0 * math.pi) * 4.0
        cx = np.cos(theta_g) * cyl_scale
        cy = np.sin(theta_g) * cyl_scale
        cz = z_grid / s_vert

        n = _value_noise_3d(cx, cy, cz, octaves, seed)
        val = (1.0 - 2.0 * np.abs(n - 0.5)) if ridge else (2.0 * (n - 0.5))
        dr += float(cel["depth_mm"]) * val

    return dr


def evaluate_radius_grid(
    params: dict[str, Any],
    n_z: int | None = None,
    n_theta: int | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Evaluate outer vase surface radius grid (z_vals, theta_vals, radii_grid)."""
    p = normalize_params(params)
    nz = max(2, int(n_z)) if n_z is not None else int(p["resolution_vertical"])
    nt = max(3, int(n_theta)) if n_theta is not None else int(p["resolution_angular"])

    height_mm = float(p["height_mm"])
    z_vals = np.linspace(0.0, height_mm, nz, dtype=np.float64)
    z_norm = z_vals / height_mm
    theta_vals = np.linspace(0.0, 2.0 * math.pi, nt, endpoint=False, dtype=np.float64)

    # 1. Base silhouette R_base(z_norm) via monotone PCHIP
    knot_x, knot_r = _prepare_knots(p)
    r_base_1d = _pchip_interpolate(knot_x, knot_r, z_norm)

    z_grid = z_vals[:, None]
    z_norm_grid = z_norm[:, None]
    theta_grid = theta_vals[None, :]

    global_twist_rad = math.radians(float(p["global_twist_deg"]))
    theta_g = theta_grid + global_twist_rad * z_norm_grid

    # 2. Polygonal cross-section factor
    n_sides = int(p["polygon_sides"])
    if n_sides >= 3:
        alpha = math.pi / float(n_sides)
        two_alpha = 2.0 * alpha
        sector = np.mod(np.mod(theta_g, two_alpha) + two_alpha, two_alpha) - alpha
        poly_scale = math.cos(alpha) / np.cos(sector)
        roundness = float(p["polygon_roundness"])
        r_prof = r_base_1d[:, None] * ((1.0 - roundness) * poly_scale + roundness * 1.0)
    else:
        r_prof = np.broadcast_to(r_base_1d[:, None], (nz, nt)).copy()

    # 3. Vertical texture fade envelope E(z) (forced 0.0 at z == 0 for flat bed contact)
    bfade = float(p["bottom_fade_mm"])
    tfade = float(p["top_fade_mm"])
    if bfade <= 0.01:
        e_bot = np.where(z_vals > 1e-9, 1.0, 0.0)
    else:
        e_bot = _smoothstep(0.0, bfade, z_vals)
        e_bot[0] = 0.0

    if tfade <= 0.01:
        e_top = np.ones_like(z_vals)
    else:
        e_top = _smoothstep(0.0, tfade, height_mm - z_vals)

    env = (e_bot * e_top)[:, None]

    # 4. Combinable surface textures
    dr = _compute_texture_displacement(
        z_grid=z_grid,
        z_norm_grid=z_norm_grid,
        theta_grid=theta_grid,
        theta_g=theta_g,
        textures=p["textures"],
        global_twist_rad=global_twist_rad,
    )

    radii = np.maximum(6.0, r_prof + env * dr)

    # 5. Optional overhang slope clamping (2-pass 1D Lipschitz projection)
    if p["auto_clamp_overhang"] and nz >= 2:
        dz = height_mm / float(nz - 1)
        max_dr = dz * math.tan(math.radians(float(p["max_safe_overhang_deg"])))
        for i in range(nz - 1):
            radii[i + 1] = np.clip(radii[i + 1], radii[i] - max_dr, radii[i] + max_dr)
        for i in range(nz - 2, -1, -1):
            radii[i] = np.clip(radii[i], radii[i + 1] - max_dr, radii[i + 1] + max_dr)
        radii = np.maximum(6.0, radii)

    return z_vals, theta_vals, radii


# ---------------------------------------------------------------------------
# Watertight 2-Manifold Mesh Construction Primitives
# ---------------------------------------------------------------------------

class _MeshBuilder:
    """Collects indexed vertices and CCW outward-facing triangles."""

    def __init__(self) -> None:
        self._verts_chunks: list[np.ndarray] = []
        self._tris_chunks: list[np.ndarray] = []
        self._v_count: int = 0

    @property
    def vertex_count(self) -> int:
        return self._v_count

    def add_vertices(self, pts: np.ndarray) -> np.ndarray:
        arr = np.asarray(pts, dtype=np.float64)
        if arr.ndim == 1:
            arr = arr[None, :]
        n = arr.shape[0]
        start = self._v_count
        self._verts_chunks.append(arr)
        self._v_count += n
        return np.arange(start, start + n, dtype=np.int32)

    def add_vertex(self, x: float, y: float, z: float) -> int:
        idx = self._v_count
        self._verts_chunks.append(np.array([[x, y, z]], dtype=np.float64))
        self._v_count += 1
        return idx

    def add_polar_ring(self, radii: np.ndarray | float, thetas: np.ndarray, z: float | np.ndarray) -> np.ndarray:
        r_arr = np.broadcast_to(np.asarray(radii, dtype=np.float64), thetas.shape)
        z_arr = np.broadcast_to(np.asarray(z, dtype=np.float64), thetas.shape)
        pts = np.column_stack((r_arr * np.cos(thetas), r_arr * np.sin(thetas), z_arr))
        return self.add_vertices(pts)

    def add_circle_ring(self, cx: float, cy: float, radius: float, z: float, count: int) -> np.ndarray:
        phis = np.linspace(0.0, 2.0 * math.pi, count, endpoint=False, dtype=np.float64)
        pts = np.column_stack((cx + radius * np.cos(phis), cy + radius * np.sin(phis), np.full(count, z, dtype=np.float64)))
        return self.add_vertices(pts)

    def add_triangles(self, tris: np.ndarray) -> None:
        arr = np.asarray(tris, dtype=np.int32)
        if arr.size > 0:
            self._tris_chunks.append(arr.reshape(-1, 3))

    def add_quad_strip(self, ring_a: np.ndarray, ring_b: np.ndarray, reverse: bool = False) -> None:
        """Connect two equal-length closed CCW rings.

        With reverse=False, normal is (+dz * r_hat - dr * z_hat):
        - upward outer wall (dz > 0) -> outward (+r_hat)
        - inward top rim (dr < 0) -> upward (+z_hat)
        - downward inner cavity wall (dz < 0) -> inward (-r_hat)
        """
        a0 = ring_a
        a1 = np.roll(ring_a, -1)
        b0 = ring_b
        b1 = np.roll(ring_b, -1)
        if not reverse:
            t1 = np.column_stack((a0, a1, b1))
            t2 = np.column_stack((a0, b1, b0))
        else:
            t1 = np.column_stack((a0, b1, a1))
            t2 = np.column_stack((a0, b0, b1))
        self.add_triangles(np.vstack((t1, t2)))

    def add_tube_grid(self, rings: list[np.ndarray], reverse: bool = False) -> None:
        """Vectorized quad-strip across an ordered sequence of equal-length rings."""
        arr = np.asarray(rings, dtype=np.int32)  # (S, M)
        a0 = arr[:-1, :]
        a1 = np.roll(a0, -1, axis=1)
        b0 = arr[1:, :]
        b1 = np.roll(b0, -1, axis=1)
        if not reverse:
            t1 = np.stack((a0, a1, b1), axis=-1).reshape(-1, 3)
            t2 = np.stack((a0, b1, b0), axis=-1).reshape(-1, 3)
        else:
            t1 = np.stack((a0, b1, a1), axis=-1).reshape(-1, 3)
            t2 = np.stack((a0, b0, b1), axis=-1).reshape(-1, 3)
        self.add_triangles(np.vstack((t1, t2)))

    def add_disk_fan(self, center_idx: int, ring: np.ndarray, normal_up: bool = True) -> None:
        m = len(ring)
        c = np.full(m, center_idx, dtype=np.int32)
        r0 = ring
        r1 = np.roll(ring, -1)
        if normal_up:
            tris = np.column_stack((c, r0, r1))
        else:
            tris = np.column_stack((c, r1, r0))
        self.add_triangles(tris)

    def get_vertices_array(self) -> np.ndarray:
        if not self._verts_chunks:
            return np.zeros((0, 3), dtype=np.float64)
        return np.vstack(self._verts_chunks)

    def build(self) -> MeshData:
        verts64 = self.get_vertices_array()
        tris = np.vstack(self._tris_chunks).astype(np.int32) if self._tris_chunks else np.zeros((0, 3), dtype=np.int32)

        # Anchor min Z cleanly at exact 0.0 in float32
        z_min = float(verts64[:, 2].min()) if len(verts64) else 0.0
        verts64[:, 2] -= z_min
        verts64[np.abs(verts64[:, 2]) < 1e-7, 2] = 0.0

        verts32 = verts64.astype(np.float32)
        if len(verts32):
            z_min32 = float(verts32[:, 2].min())
            if z_min32 != 0.0:
                verts32[:, 2] -= np.float32(z_min32)
            verts32[np.abs(verts32[:, 2]) < 1e-7, 2] = np.float32(0.0)

        # Compute exact face normals & signed volume from float32 vertex positions
        v0 = verts32[tris[:, 0]].astype(np.float64)
        v1 = verts32[tris[:, 1]].astype(np.float64)
        v2 = verts32[tris[:, 2]].astype(np.float64)

        cross = np.cross(v1 - v0, v2 - v0)
        norms = np.linalg.norm(cross, axis=1, keepdims=True)
        face_normals = (cross / np.maximum(norms, 1e-30)).astype(np.float32)

        signed_vol_mm3 = float(np.sum(np.einsum("ij,ij->i", v0, cross)) / 6.0)
        volume_cm3 = signed_vol_mm3 / 1000.0

        vmin = verts32.min(axis=0)
        vmax = verts32.max(axis=0)
        vsize = vmax - vmin
        bounds_mm = {
            "min": [float(vmin[0]), float(vmin[1]), float(vmin[2])],
            "max": [float(vmax[0]), float(vmax[1]), float(vmax[2])],
            "size": [float(vsize[0]), float(vsize[1]), float(vsize[2])],
        }

        return MeshData(
            vertices=verts32,
            triangles=tris,
            face_normals=face_normals,
            bounds_mm=bounds_mm,
            volume_cm3=float(volume_cm3),
        )


def _bridge_closed_loops_up(
    verts_xy: np.ndarray,
    loop_in: list[int] | np.ndarray,
    loop_out: list[int] | np.ndarray,
    center_xy: tuple[float, float],
) -> np.ndarray:
    """Triangulate the annular region between two star-shaped closed CCW loops (normal +Z).

    Guarantees:
    - Outer loop edges emitted once as (O_q, O_{q+1})
    - Inner loop edges emitted once as (I_{p+1}, I_p)
    - Every internal spoke emitted once forward and once backward (strict 2-manifold)
    """
    lin = [int(i) for i in loop_in]
    lout = [int(i) for i in loop_out]
    m1 = len(lin)
    m2 = len(lout)
    cx, cy = center_xy

    ang_in: list[float] = []
    for p, idx in enumerate(lin):
        a = math.atan2(float(verts_xy[idx, 1]) - cy, float(verts_xy[idx, 0]) - cx)
        if p > 0:
            while a <= ang_in[-1]:
                a += 2.0 * math.pi
        ang_in.append(a)
    ang_in.append(ang_in[0] + 2.0 * math.pi)

    raw_out = [
        math.atan2(float(verts_xy[idx, 1]) - cy, float(verts_xy[idx, 0]) - cx)
        for idx in lout
    ]
    best_s = min(
        range(m2),
        key=lambda s: abs(((raw_out[s] - ang_in[0] + math.pi) % (2.0 * math.pi)) - math.pi),
    )
    lout = lout[best_s:] + lout[:best_s]

    a0 = math.atan2(float(verts_xy[lout[0], 1]) - cy, float(verts_xy[lout[0], 0]) - cx)
    while a0 - ang_in[0] > math.pi:
        a0 -= 2.0 * math.pi
    while ang_in[0] - a0 > math.pi:
        a0 += 2.0 * math.pi

    ang_out: list[float] = [a0]
    for q in range(1, m2):
        idx = lout[q]
        a = math.atan2(float(verts_xy[idx, 1]) - cy, float(verts_xy[idx, 0]) - cx)
        while a <= ang_out[-1]:
            a += 2.0 * math.pi
        ang_out.append(a)
    ang_out.append(ang_out[0] + 2.0 * math.pi)

    tris: list[tuple[int, int, int]] = []
    p = 0
    q = 0

    while p < m1 or q < m2:
        if p == m1:
            advance_out = True
        elif q == m2:
            advance_out = False
        else:
            skew_if_in = abs(ang_in[p + 1] - ang_out[q])
            skew_if_out = abs(ang_out[q + 1] - ang_in[p])
            advance_out = skew_if_out < skew_if_in

        if advance_out:
            tris.append((lin[p % m1], lout[q % m2], lout[(q + 1) % m2]))
            q += 1
        else:
            tris.append((lin[p % m1], lout[q % m2], lin[(p + 1) % m1]))
            p += 1

    return np.array(tris, dtype=np.int32)


def _drainage_zone_radii(r_avail: float) -> tuple[float, float]:
    """Return (r_collar, r_guard) strictly inside r_avail with guaranteed manifold margins."""
    r_av = max(2.2, float(r_avail))
    safe_margin = max(0.35, 0.10 * r_av)
    r_usable = max(1.2, r_av - safe_margin)
    r_guard = min(r_av - 0.15, max(r_usable + 0.10, r_av - 0.50 * safe_margin))
    r_collar = 0.92 * r_usable
    return r_collar, r_guard


def _compute_drainage_layout(
    drainage_cfg: dict[str, Any],
    r_avail: float,
) -> list[tuple[float, float, float]]:
    """Compute safe non-overlapping (cx, cy, r_hole) list for 1..9 holes inside r_avail."""
    k = int(drainage_cfg["hole_count"])
    req_r = 0.5 * float(drainage_cfg["hole_diameter_mm"])
    req_ratio = float(drainage_cfg["ring_radius_ratio"])
    r_collar, _ = _drainage_zone_radii(r_avail)

    if k <= 1:
        max_safe_r = 0.68 * r_collar
        r_h = max(0.20, min(req_r, max_safe_r))
        return [(0.0, 0.0, min(r_h, max_safe_r))]

    if k == 2:
        eff_ratio = req_ratio if req_ratio >= 0.15 else 0.45
        r_ring = min(max(0.36 * r_collar, eff_ratio * r_avail), 0.68 * r_collar)
        max_safe_r = 0.60 * min(r_ring, r_collar - r_ring)
        r_h = max(0.18, min(req_r, max_safe_r))
        r_h = min(r_h, max_safe_r)
        return [(r_ring, 0.0, r_h), (-r_ring, 0.0, r_h)]

    eff_ratio = req_ratio if req_ratio >= 0.15 else 0.48
    r_ring = min(max(0.42 * r_collar, eff_ratio * r_avail), 0.72 * r_collar)
    dpsi = math.pi / float(k)
    r_hub = 0.32 * r_ring
    max_safe_r = 0.60 * min(r_ring * math.sin(dpsi), r_ring - r_hub, r_collar - r_ring)
    r_h = max(0.18, min(req_r, max_safe_r))
    r_h = min(r_h, max_safe_r)

    holes: list[tuple[float, float, float]] = []
    for c in range(k):
        psi = 2.0 * math.pi * float(c) / float(k)
        holes.append((r_ring * math.cos(psi), r_ring * math.sin(psi), r_h))
    return holes


def _add_planar_disk_with_holes(
    mb: _MeshBuilder,
    outer_ring: np.ndarray,
    z_plane: float,
    holes: list[tuple[float, float, float]],
    r_avail: float,
    normal_up: bool,
    m_hole: int = 32,
) -> list[np.ndarray]:
    """Triangulate a planar disk bounded by outer_ring with 0..9 circular holes.

    Uses a radial polar guard ring + strictly convex sector decomposition + loop bridging
    so zero triangles can flip or degenerate even on sharp polygonal/textured profiles
    or 25 mm walls with 9 holes, and every shared edge is traversed once in each direction.
    """
    k = len(holes)
    if k == 0:
        c_idx = mb.add_vertex(0.0, 0.0, z_plane)
        mb.add_disk_fan(c_idx, outer_ring, normal_up=normal_up)
        return []

    r_collar, r_guard = _drainage_zone_radii(r_avail)

    # Project outer_ring radially onto a pure circular guard_ring at r_guard < r_avail
    verts_init = mb.get_vertices_array()
    outer_xy = verts_init[outer_ring, :2]
    outer_norms = np.maximum(np.hypot(outer_xy[:, 0], outer_xy[:, 1]), 1e-9)
    guard_pts = np.column_stack((
        (r_guard / outer_norms) * outer_xy[:, 0],
        (r_guard / outer_norms) * outer_xy[:, 1],
        np.full(len(outer_ring), z_plane, dtype=np.float64),
    ))
    guard_ring = mb.add_vertices(guard_pts)

    o0 = np.asarray(outer_ring, dtype=np.int32)
    o1 = np.roll(o0, -1)
    g0 = guard_ring
    g1 = np.roll(g0, -1)

    hole_rings: list[np.ndarray] = [
        mb.add_circle_ring(cx, cy, rh, z_plane, m_hole)
        for (cx, cy, rh) in holes
    ]

    tris_list: list[np.ndarray] = [
        np.vstack((
            np.column_stack((o0, o1, g1)),
            np.column_stack((o0, g1, g0)),
        ))
    ]

    if k == 1:
        verts_xy = mb.get_vertices_array()[:, :2]
        cx, cy, _ = holes[0]
        tris_list.append(_bridge_closed_loops_up(verts_xy, hole_rings[0], guard_ring, (cx, cy)))

    elif k == 2:
        m_semi = 24
        n_diam = 16
        bot_pole = mb.add_vertex(0.0, -r_collar, z_plane)
        top_pole = mb.add_vertex(0.0, r_collar, z_plane)

        right_angs = np.linspace(-0.5 * math.pi, 0.5 * math.pi, m_semi + 1, dtype=np.float64)[1:-1]
        right_semi = mb.add_vertices(
            np.column_stack((r_collar * np.cos(right_angs), r_collar * np.sin(right_angs), np.full(len(right_angs), z_plane)))
        )

        left_angs = np.linspace(0.5 * math.pi, 1.5 * math.pi, m_semi + 1, dtype=np.float64)[1:-1]
        left_semi = mb.add_vertices(
            np.column_stack((r_collar * np.cos(left_angs), r_collar * np.sin(left_angs), np.full(len(left_angs), z_plane)))
        )

        diam_ys = np.linspace(-r_collar, r_collar, n_diam + 1, dtype=np.float64)[1:-1]
        diam_mid = mb.add_vertices(
            np.column_stack((np.zeros(len(diam_ys)), diam_ys, np.full(len(diam_ys), z_plane)))
        )

        # Right half-disk CCW around (+r_ring, 0)
        cell_0 = [bot_pole, *right_semi.tolist(), top_pole, *diam_mid[::-1].tolist()]
        # Left half-disk CCW around (-r_ring, 0)
        cell_1 = [top_pole, *left_semi.tolist(), bot_pole, *diam_mid.tolist()]
        # Full collar loop CCW around (0, 0)
        collar_ring = [bot_pole, *right_semi.tolist(), top_pole, *left_semi.tolist()]

        verts_xy = mb.get_vertices_array()[:, :2]
        tris_list.append(_bridge_closed_loops_up(verts_xy, hole_rings[0], cell_0, (holes[0][0], holes[0][1])))
        tris_list.append(_bridge_closed_loops_up(verts_xy, hole_rings[1], cell_1, (holes[1][0], holes[1][1])))
        tris_list.append(_bridge_closed_loops_up(verts_xy, collar_ring, guard_ring, (0.0, 0.0)))

    else:
        r_ring = math.hypot(holes[0][0], holes[0][1])
        dpsi = math.pi / float(k)
        r_hub = 0.32 * r_ring

        n_spoke = 14
        n_chord = 6
        m_arc = max(12, int(round(64.0 / float(k))))

        spoke_angs = [2.0 * math.pi * float(c) / float(k) - dpsi for c in range(k)]
        spoke_radii = np.linspace(r_hub, r_collar, n_spoke + 1, dtype=np.float64)

        spokes: list[np.ndarray] = []
        for ang in spoke_angs:
            pts = np.column_stack((
                spoke_radii * math.cos(ang),
                spoke_radii * math.sin(ang),
                np.full(len(spoke_radii), z_plane),
            ))
            spokes.append(mb.add_vertices(pts))

        verts_so_far = mb.get_vertices_array()
        chord_interiors: list[np.ndarray] = []
        arc_interiors: list[np.ndarray] = []
        t_chord = np.linspace(0.0, 1.0, n_chord + 1, dtype=np.float64)[1:-1][:, None]
        for c in range(k):
            c_next = (c + 1) % k
            u0 = verts_so_far[spokes[c][0]]
            u1 = verts_so_far[spokes[c_next][0]]
            c_pts = u0[None, :] + t_chord * (u1 - u0)[None, :]
            c_pts[:, 2] = z_plane
            chord_interiors.append(mb.add_vertices(c_pts))

            ang0 = spoke_angs[c]
            ang1 = ang0 + 2.0 * dpsi
            a_pts = np.linspace(ang0, ang1, m_arc + 1, dtype=np.float64)[1:-1]
            arc_interiors.append(
                mb.add_vertices(
                    np.column_stack((r_collar * np.cos(a_pts), r_collar * np.sin(a_pts), np.full(len(a_pts), z_plane)))
                )
            )

        # Center hub k-gon fan (+Z first; flipped at end if not normal_up)
        hub_center = mb.add_vertex(0.0, 0.0, z_plane)
        hub_loop: list[int] = []
        for c in range(k):
            hub_loop.append(int(spokes[c][0]))
            hub_loop.extend(chord_interiors[c].tolist())
        hc = np.full(len(hub_loop), hub_center, dtype=np.int32)
        hr0 = np.array(hub_loop, dtype=np.int32)
        hr1 = np.roll(hr0, -1)
        tris_list.append(np.column_stack((hc, hr0, hr1)))

        collar_ring = []
        for c in range(k):
            collar_ring.append(int(spokes[c][-1]))
            collar_ring.extend(arc_interiors[c].tolist())

        verts_xy = mb.get_vertices_array()[:, :2]
        for c in range(k):
            c_next = (c + 1) % k
            cell_loop: list[int] = [
                *spokes[c][:-1].tolist(),              # U_c .. before W_c (outward)
                int(spokes[c][-1]),                    # W_c
                *arc_interiors[c].tolist(),            # collar arc CCW
                *spokes[c_next][::-1][:-1].tolist(),   # W_{c+1} .. before U_{c+1} (inward)
                int(spokes[c_next][0]),                # U_{c+1}
                *chord_interiors[c][::-1].tolist(),    # inner chord back toward U_c
            ]
            tris_list.append(
                _bridge_closed_loops_up(verts_xy, hole_rings[c], cell_loop, (holes[c][0], holes[c][1]))
            )

        tris_list.append(_bridge_closed_loops_up(verts_xy, collar_ring, guard_ring, (0.0, 0.0)))

    all_tris = np.vstack(tris_list)
    if not normal_up:
        all_tris = all_tris[:, [0, 2, 1]]
    mb.add_triangles(all_tris)
    return hole_rings


# ---------------------------------------------------------------------------
# Public Mesh Generators (Section 3)
# ---------------------------------------------------------------------------

def generate_vase_mesh(params: dict[str, Any], layer_height_mm: float = 0.2) -> MeshData:
    """Generate a 100% closed, watertight 2-manifold vase mesh for spiral_vase or shelled_hollow."""
    p = normalize_params(params)
    lh = max(0.05, min(1.0, float(layer_height_mm)))
    z_vals, theta_vals, radii_grid = evaluate_radius_grid(p)
    nz, _ = radii_grid.shape
    height_mm = float(p["height_mm"])

    mb = _MeshBuilder()
    drain_cfg = p["drainage"]
    drain_enabled = bool(drain_cfg["enabled"])

    if p["print_mode"] == "spiral_vase":
        # Outer wall rings from Z = 0 to Z = height_mm
        outer_rings: list[np.ndarray] = [
            mb.add_polar_ring(radii_grid[i], theta_vals, float(z_vals[i]))
            for i in range(nz)
        ]
        mb.add_tube_grid(outer_rings, reverse=False)

        # Top solid cap at Z = height_mm (+Z normal)
        top_center = mb.add_vertex(0.0, 0.0, height_mm)
        mb.add_disk_fan(top_center, outer_rings[-1], normal_up=True)

        # Bottom cap at Z = 0.0 (-Z normal), with optional blind drainage cavities
        if not drain_enabled:
            bot_center = mb.add_vertex(0.0, 0.0, 0.0)
            mb.add_disk_fan(bot_center, outer_rings[0], normal_up=False)
        else:
            z_cap = min(
                float(p["spiral_bottom_layers"]) * lh + 0.30,
                0.34 * height_mm,
            )
            z_cap = max(0.45, z_cap)
            sub_cap_mask = z_vals <= (z_cap + 1e-3)
            r_avail = float(radii_grid[sub_cap_mask].min()) if np.any(sub_cap_mask) else float(radii_grid[0].min())
            holes = _compute_drainage_layout(drain_cfg, r_avail)
            bot_hole_rings = _add_planar_disk_with_holes(
                mb=mb,
                outer_ring=outer_rings[0],
                z_plane=0.0,
                holes=holes,
                r_avail=r_avail,
                normal_up=False,
            )
            m_hole = len(bot_hole_rings[0])
            for idx_h, (cx, cy, rh) in enumerate(holes):
                top_hole_ring = mb.add_circle_ring(cx, cy, rh, z_cap, m_hole)
                # Tunnel wall facing inward into blind cavity (reverse=True)
                mb.add_quad_strip(bot_hole_rings[idx_h], top_hole_ring, reverse=True)
                # Blind cavity ceiling facing -Z into cavity
                roof_center = mb.add_vertex(cx, cy, z_cap)
                mb.add_disk_fan(roof_center, top_hole_ring, normal_up=False)

        return mb.build()

    # Mode 2: shelled_hollow (true thick-walled hollow shell with optional lip bevel & through-drainage)
    wall_t = float(p["wall_thickness_mm"])
    effective_bottom = min(float(p["bottom_thickness_mm"]), height_mm * 0.65)
    z_floor = max(1.0, effective_bottom)

    if nz >= 5:
        r_for_slope = (
            0.25 * np.vstack((radii_grid[0:1], radii_grid[:-1]))
            + 0.50 * radii_grid
            + 0.25 * np.vstack((radii_grid[1:], radii_grid[-1:]))
        )
    else:
        r_for_slope = radii_grid
    slope_z = np.gradient(r_for_slope, z_vals, axis=0)
    slope_z = np.clip(slope_z, -1.75, 1.75)
    extra_radial = np.minimum(wall_t * (np.sqrt(1.0 + slope_z * slope_z) - 1.0), 8.0)
    radial_wall = wall_t + extra_radial

    # Smooth C1 clamp above min_inner_r = 3.0 mm so narrow waists with 25 mm walls never invert or crease
    min_inner_r = 3.0
    min_wall_gap = min(0.65, 0.80 * wall_t)
    delta_in = (radii_grid - radial_wall) - min_inner_r
    inner_grid = min_inner_r + 0.5 * (delta_in + np.sqrt(delta_in * delta_in + 0.16))
    inner_grid = np.minimum(inner_grid, radii_grid - min_wall_gap)
    inner_grid = np.maximum(min_inner_r, inner_grid)

    if p["auto_clamp_overhang"] and nz >= 2:
        dz = height_mm / float(nz - 1)
        max_dr = dz * math.tan(math.radians(float(p["max_safe_overhang_deg"])))
        for i in range(nz - 1):
            inner_grid[i + 1] = np.clip(inner_grid[i + 1], inner_grid[i] - max_dr, inner_grid[i] + max_dr)
        for i in range(nz - 2, -1, -1):
            inner_grid[i] = np.clip(inner_grid[i], inner_grid[i + 1] - max_dr, inner_grid[i + 1] + max_dr)
        inner_grid = np.minimum(inner_grid, radii_grid - min_wall_gap)
        inner_grid = np.maximum(min_inner_r, inner_grid)

    # Determine safe lip bevel radius
    top_wall_span = float(np.min(radii_grid[-1] - inner_grid[-1]))
    bevel = min(
        float(p["lip_bevel_mm"]),
        0.42 * max(0.0, top_wall_span),
        0.15 * (height_mm - z_floor),
    )

    profile_rings: list[np.ndarray] = []

    if bevel > 0.08:
        z_lip_base = height_mm - bevel
        # Outer wall up to z_lip_base (keep >= 0.05 mm Z margin so adjacent rings never quantize-collapse)
        outer_mask = z_vals < (z_lip_base - 0.05)
        for i in np.nonzero(outer_mask)[0]:
            profile_rings.append(mb.add_polar_ring(radii_grid[i], theta_vals, float(z_vals[i])))

        # Interpolate outer & inner radii cleanly at z_lip_base
        r_out_lip = np.array([np.interp(z_lip_base, z_vals, radii_grid[:, j]) for j in range(len(theta_vals))])
        r_in_lip = np.array([np.interp(z_lip_base, z_vals, inner_grid[:, j]) for j in range(len(theta_vals))])
        r_in_lip = np.minimum(r_in_lip, r_out_lip - min_wall_gap)
        r_in_lip = np.maximum(min_inner_r, r_in_lip)

        r_mid = 0.5 * (r_out_lip + r_in_lip)
        half_w = 0.5 * (r_out_lip - r_in_lip)

        # Semicircular lip arch peaking at exact Z = height_mm (gamma = pi/2)
        for gamma in (0.0, 0.25 * math.pi, 0.5 * math.pi, 0.75 * math.pi, math.pi):
            z_a = height_mm if abs(gamma - 0.5 * math.pi) < 1e-9 else (z_lip_base + bevel * math.sin(gamma))
            r_a = r_mid + half_w * math.cos(gamma)
            profile_rings.append(mb.add_polar_ring(r_a, theta_vals, z_a))

        z_inner_top = z_lip_base
    else:
        for i in range(nz):
            profile_rings.append(mb.add_polar_ring(radii_grid[i], theta_vals, float(z_vals[i])))
        profile_rings.append(mb.add_polar_ring(inner_grid[-1], theta_vals, height_mm))
        z_inner_top = height_mm

    # Inner cavity wall descending from below z_inner_top down to z_floor
    inner_mask = (z_vals < z_inner_top - 0.05) & (z_vals > z_floor + 0.05)
    for i in np.nonzero(inner_mask)[0][::-1]:
        profile_rings.append(mb.add_polar_ring(inner_grid[i], theta_vals, float(z_vals[i])))

    r_in_floor = np.array([np.interp(z_floor, z_vals, inner_grid[:, j]) for j in range(len(theta_vals))])
    r_in_floor = np.maximum(min_inner_r, r_in_floor)
    profile_rings.append(mb.add_polar_ring(r_in_floor, theta_vals, z_floor))

    # Connect continuous meridian revolution (outer wall -> lip -> inner cavity wall)
    mb.add_tube_grid(profile_rings, reverse=False)

    outer_bot_ring = profile_rings[0]
    inner_floor_ring = profile_rings[-1]

    if not drain_enabled:
        bot_center = mb.add_vertex(0.0, 0.0, 0.0)
        mb.add_disk_fan(bot_center, outer_bot_ring, normal_up=False)

        floor_center = mb.add_vertex(0.0, 0.0, z_floor)
        mb.add_disk_fan(floor_center, inner_floor_ring, normal_up=True)
    else:
        sub_floor_mask = z_vals <= (z_floor + 1e-3)
        min_outer_below_floor = (
            float(radii_grid[sub_floor_mask].min())
            if np.any(sub_floor_mask)
            else float(radii_grid[0].min())
        )
        r_avail = max(min_inner_r, float(min(min_outer_below_floor - min_wall_gap, r_in_floor.min())))
        holes = _compute_drainage_layout(drain_cfg, r_avail)

        bot_hole_rings = _add_planar_disk_with_holes(
            mb=mb,
            outer_ring=outer_bot_ring,
            z_plane=0.0,
            holes=holes,
            r_avail=r_avail,
            normal_up=False,
        )
        top_hole_rings = _add_planar_disk_with_holes(
            mb=mb,
            outer_ring=inner_floor_ring,
            z_plane=z_floor,
            holes=holes,
            r_avail=r_avail,
            normal_up=True,
        )
        for idx_h in range(len(holes)):
            mb.add_quad_strip(bot_hole_rings[idx_h], top_hole_rings[idx_h], reverse=True)

    return mb.build()


def generate_saucer_mesh(params: dict[str, Any]) -> MeshData:
    """Generate a watertight 2-manifold matching plant saucer tray centered at (0, 0), min(Z) == 0.0."""
    p = normalize_params(params)
    sc = p["saucer"]

    nt = max(96, min(240, int(p["resolution_angular"])))
    theta_vals = np.linspace(0.0, 2.0 * math.pi, nt, endpoint=False, dtype=np.float64)

    # Account for custom profile or polygonal vase base radius so the vase always fits comfortably
    _, _, vase_base_radii = evaluate_radius_grid(p, n_z=12, n_theta=nt)
    vase_foot_radius = max(0.5 * float(p["base_diameter_mm"]), float(vase_base_radii[0].max()))

    r_saucer_inner = vase_foot_radius + float(sc["clearance_mm"])
    rim_h = float(sc["rim_height_mm"])
    wall_t = float(sc["wall_thickness_mm"])
    floor_t = min(float(sc["floor_thickness_mm"]), rim_h - 3.0)
    floor_t = max(1.2, floor_t)
    ribs_h = min(float(sc["inner_ribs_height_mm"]), 0.45 * (rim_h - floor_t))
    ribs_h = max(0.0, ribs_h)

    flare_tan = math.tan(math.radians(12.0))
    n_wall = 28
    z_out = np.linspace(0.0, rim_h, n_wall, dtype=np.float64)
    z_out_norm = z_out / max(rim_h, 1.0)

    r_out_base = (r_saucer_inner + wall_t) + z_out * flare_tan
    r_out_grid = np.broadcast_to(r_out_base[:, None], (n_wall, nt)).copy()

    # Optional matching outer vase texture with clean bed/rim fade
    if sc["match_vase_texture"]:
        e_bot = _smoothstep(0.0, min(3.5, 0.25 * rim_h), z_out)
        e_bot[0] = 0.0
        e_top = _smoothstep(0.0, min(3.0, 0.22 * rim_h), rim_h - z_out)
        env = (e_bot * e_top)[:, None]

        twist_rad = math.radians(float(p["global_twist_deg"])) * 0.25
        theta_g = theta_vals[None, :] + twist_rad * z_out_norm[:, None]
        dr_tex = _compute_texture_displacement(
            z_grid=z_out[:, None],
            z_norm_grid=z_out_norm[:, None],
            theta_grid=theta_vals[None, :],
            theta_g=theta_g,
            textures=p["textures"],
            global_twist_rad=twist_rad,
        )
        max_tex = 0.45 * wall_t
        r_out_grid += env * np.clip(0.40 * dr_tex, -max_tex, max_tex)

    mb = _MeshBuilder()
    rings: list[np.ndarray] = []

    # 1. Outer flared wall from Z = 0 up to Z = rim_h - bevel
    lip_r = 0.5 * wall_t
    z_arch_base = max(floor_t + 1.0, rim_h - lip_r)
    for i in range(n_wall):
        if z_out[i] < z_arch_base - 1e-4:
            rings.append(mb.add_polar_ring(r_out_grid[i], theta_vals, float(z_out[i])))

    # 2. Smooth rounded top rim peaking at exact Z = rim_h
    r_outer_top = np.array([np.interp(z_arch_base, z_out, r_out_grid[:, j]) for j in range(nt)])
    r_inner_top = np.full(nt, r_saucer_inner + (z_arch_base - floor_t) * flare_tan, dtype=np.float64)
    r_inner_top = np.minimum(r_inner_top, r_outer_top - 0.6)

    r_mid = 0.5 * (r_outer_top + r_inner_top)
    half_w = 0.5 * (r_outer_top - r_inner_top)
    arch_h = rim_h - z_arch_base
    for gamma in (0.0, 0.25 * math.pi, 0.5 * math.pi, 0.75 * math.pi, math.pi):
        z_a = rim_h if abs(gamma - 0.5 * math.pi) < 1e-9 else (z_arch_base + arch_h * math.sin(gamma))
        r_a = r_mid + half_w * math.cos(gamma)
        rings.append(mb.add_polar_ring(r_a, theta_vals, z_a))

    # 3. Inner flared wall descending to inner floor edge (r_saucer_inner, floor_t)
    n_in_wall = 16
    z_in = np.linspace(z_arch_base, floor_t, n_in_wall, dtype=np.float64)[1:]
    for zv in z_in:
        r_v = r_saucer_inner + (zv - floor_t) * flare_tan
        rings.append(mb.add_polar_ring(r_v, theta_vals, float(zv)))

    # 4. Inner floor radial rings with raised drainage ribs so the pot sits above water
    n_floor_rings = 22
    r_floor_vals = np.linspace(r_saucer_inner, 0.06 * r_saucer_inner, n_floor_rings, dtype=np.float64)[1:]
    n_ribs = 8
    rib_ang_profile = np.maximum(0.0, np.cos(float(n_ribs) * theta_vals)) ** 2

    for rv in r_floor_vals:
        if ribs_h > 1e-4:
            u_rad = np.clip((rv - 0.16 * r_saucer_inner) / max(0.70 * r_saucer_inner, 1e-6), 0.0, 1.0)
            rib_env = math.sin(math.pi * float(u_rad)) ** 2
            z_ring = floor_t + ribs_h * rib_env * rib_ang_profile
        else:
            z_ring = floor_t
        rings.append(mb.add_polar_ring(rv, theta_vals, z_ring))

    mb.add_tube_grid(rings, reverse=False)

    # Bottom flat cap at Z = 0 (-Z normal) & inner floor center fan (+Z normal)
    bot_center = mb.add_vertex(0.0, 0.0, 0.0)
    mb.add_disk_fan(bot_center, rings[0], normal_up=False)

    top_center = mb.add_vertex(0.0, 0.0, floor_t)
    mb.add_disk_fan(top_center, rings[-1], normal_up=True)

    return mb.build()

# ===========================================================================
# MODULE: vase_studio.printability
# ===========================================================================

"""Printability, overhang, bed-fit, and filament weight analysis for Orca Vase Studio."""

pass  # [bundled] hoisted __future__ import

import math
from typing import Any

try:
    import numpy as np
except ModuleNotFoundError:
    import os as _os
    from pathlib import Path as _Path
    import sys as _sys

    if _sys.platform == "win32":
        _appdata = _os.environ.get("APPDATA", "").strip()
        _orca_base = _Path(_appdata) / "OrcaSlicer" if _appdata else _Path.home() / "AppData" / "Roaming" / "OrcaSlicer"
    elif _sys.platform == "darwin":
        _orca_base = _Path.home() / "Library" / "Application Support" / "OrcaSlicer"
    else:
        _xdg = _os.environ.get("XDG_CONFIG_HOME", "").strip()
        _orca_base = (_Path(_xdg) if _xdg else (_Path.home() / ".config")) / "OrcaSlicer"

    _orca_pkg_dir = str(_orca_base / "python" / "packages" / f"cp{_sys.version_info.major}{_sys.version_info.minor}")
    if _orca_pkg_dir not in _sys.path:
        _sys.path.insert(0, _orca_pkg_dir)
    import numpy as np

pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import

PLA_DENSITY_G_CM3 = 1.24


def _ctx_float(ctx: dict[str, Any], key: str, default: float, lo: float, hi: float) -> float:
    val = ctx.get(key, default)
    if isinstance(val, (list, tuple)) and len(val) > 0:
        val = val[0]
    if isinstance(val, str):
        val = val.strip().rstrip("%mM ").strip()
    try:
        f = float(val)
    except (TypeError, ValueError):
        return default
    if not math.isfinite(f) or f <= 0.0:
        return default
    return max(lo, min(hi, f))


def analyze_printability(
    mesh: MeshData,
    params: dict[str, Any],
    host_context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Analyze a generated mesh for overhangs, bed bounds, spiral vase gap risk, and PLA usage."""
    p = normalize_params(params)
    ctx = host_context if isinstance(host_context, dict) else {}

    bed_x = _ctx_float(ctx, "bed_x", 220.0, 50.0, 2000.0)
    bed_y = _ctx_float(ctx, "bed_y", 220.0, 50.0, 2000.0)
    max_z = _ctx_float(ctx, "max_z", 250.0, 50.0, 2000.0)
    nozzle_mm = _ctx_float(ctx, "nozzle_mm", 0.4, 0.15, 2.0)
    layer_h = _ctx_float(ctx, "layer_height_mm", 0.2, 0.04, 1.2)
    line_w = _ctx_float(ctx, "line_width_mm", 0.42, 0.15, 2.5)

    verts = np.asarray(mesh.vertices, dtype=np.float64)
    tris = np.asarray(mesh.triangles, dtype=np.int32)
    normals = np.asarray(mesh.face_normals, dtype=np.float64)
    tri_count = int(len(tris))

    size = mesh.bounds_mm.get("size", [0.0, 0.0, 0.0])
    dx = round(float(size[0]), 2)
    dy = round(float(size[1]), 2)
    dz = round(float(size[2]), 2)

    bed_shape = str(ctx.get("bed_shape") or "rectangular").strip().lower()
    if bed_shape == "circular":
        bed_diam = min(bed_x, bed_y)
        verts_xy_r = float(np.max(np.hypot(verts[:, 0], verts[:, 1]))) if len(verts) > 0 else 0.5 * max(dx, dy)
        fits_bed = bool(2.0 * verts_xy_r <= bed_diam + 1e-3 and max(dx, dy) <= bed_diam + 1e-3)
    else:
        fits_bed = bool(dx <= bed_x + 1e-3 and dy <= bed_y + 1e-3)
    fits_height = bool(dz <= max_z + 1e-3)

    if tri_count == 0 or len(verts) == 0:
        return {
            "max_overhang_deg": 0.0,
            "warning_faces_pct": 0.0,
            "critical_faces_pct": 0.0,
            "fits_bed": fits_bed,
            "fits_height": fits_height,
            "spiral_gap_risk": False,
            "estimated_weight_g": 0.0,
            "estimated_volume_cm3": 0.0,
            "dimensions_mm": [dx, dy, dz],
            "triangle_count": 0,
            "warnings": [],
        }

    v0 = verts[tris[:, 0]]
    v1 = verts[tris[:, 1]]
    v2 = verts[tris[:, 2]]
    face_areas = 0.5 * np.linalg.norm(np.cross(v1 - v0, v2 - v0), axis=1)

    face_z_max = np.maximum(np.maximum(v0[:, 2], v1[:, 2]), v2[:, 2])
    face_z_min = np.minimum(np.minimum(v0[:, 2], v1[:, 2]), v2[:, 2])
    nz = normals[:, 2]

    # Exclude flat bottom faces resting on bed Z == 0
    non_bed_mask = face_z_max > 1e-3

    # In spiral_vase mode, top cap and blind-drainage internal roof are unprinted slicing caps
    is_spiral = p["print_mode"] == "spiral_vase"
    if is_spiral:
        top_cap_mask = (face_z_min >= dz - 1e-2) & (nz > 0.999)
        eval_mask = non_bed_mask & (~top_cap_mask)
        if p["drainage"]["enabled"]:
            z_blind_cap = min(float(p["spiral_bottom_layers"]) * layer_h + 0.30, 0.34 * float(p["height_mm"]))
            blind_roof_mask = (face_z_max <= z_blind_cap + 0.08) & (nz < -0.999)
            eval_mask = eval_mask & (~blind_roof_mask)
    else:
        eval_mask = non_bed_mask

    downward_mask = eval_mask & (nz < -1e-4)
    overhang_deg = np.zeros(tri_count, dtype=np.float64)
    if np.any(downward_mask):
        overhang_deg[downward_mask] = np.degrees(np.arcsin(np.clip(-nz[downward_mask], 0.0, 1.0)))

    # Robust 99.8th area-weighted percentile avoids single microscopic facet spikes while catching real slopes;
    # still report true max on clean surfaces
    eval_areas = face_areas[eval_mask]
    total_eval_area = float(np.sum(eval_areas)) if eval_areas.size > 0 else 0.0

    max_overhang_deg = round(float(np.max(overhang_deg)), 1) if np.any(downward_mask) else 0.0
    if total_eval_area > 1e-6:
        warn_area = float(np.sum(face_areas[eval_mask & (overhang_deg > 45.0)]))
        crit_area = float(np.sum(face_areas[eval_mask & (overhang_deg > 55.0)]))
        warning_faces_pct = round(100.0 * warn_area / total_eval_area, 2)
        critical_faces_pct = round(100.0 * crit_area / total_eval_area, 2)
    else:
        warning_faces_pct = 0.0
        critical_faces_pct = 0.0

    # Spiral vase gap risk & realistic filament usage estimate
    eff_spiral_lw = float(p["spiral_line_width_mm"]) if p["auto_configure_slicer"] else line_w
    if is_spiral:
        horiz_step_mm = layer_h * math.tan(math.radians(min(max_overhang_deg, 84.0)))
        spiral_gap_risk = bool(
            (horiz_step_mm > 0.68 * eff_spiral_lw and warning_faces_pct > 0.25)
            or critical_faces_pct > 0.5
            or max_overhang_deg > 55.0
        )
        # Estimate actual printed shell volume (1 outer wall + bottom solid layers)
        bed_area_mm2 = float(np.sum(face_areas[~non_bed_mask]))
        wall_area_mm2 = total_eval_area
        bottom_h_mm = float(p["spiral_bottom_layers"]) * layer_h
        printed_vol_mm3 = wall_area_mm2 * eff_spiral_lw + bed_area_mm2 * bottom_h_mm
        est_vol_cm3 = max(0.5, min(float(mesh.volume_cm3), printed_vol_mm3 / 1000.0))
    else:
        spiral_gap_risk = False
        est_vol_cm3 = max(0.5, float(mesh.volume_cm3))

    est_vol_cm3 = round(est_vol_cm3, 2)
    est_weight_g = round(est_vol_cm3 * PLA_DENSITY_G_CM3, 1)

    warnings: list[dict[str, str]] = []

    if not fits_bed:
        warnings.append({
            "code": "BED_OVERFLOW",
            "pt": f"Dimensoes XY ({dx:.1f} x {dy:.1f} mm) excedem a mesa ({bed_x:.0f} x {bed_y:.0f} mm).",
            "en": f"XY dimensions ({dx:.1f} x {dy:.1f} mm) exceed build plate ({bed_x:.0f} x {bed_y:.0f} mm).",
        })

    if not fits_height:
        warnings.append({
            "code": "HEIGHT_OVERFLOW",
            "pt": f"Altura ({dz:.1f} mm) excede o limite Z da impressora ({max_z:.0f} mm).",
            "en": f"Height ({dz:.1f} mm) exceeds printer Z limit ({max_z:.0f} mm).",
        })

    if critical_faces_pct > 0.5 or max_overhang_deg > 55.0:
        warnings.append({
            "code": "CRITICAL_OVERHANG",
            "pt": (
                f"Overhang critico de {max_overhang_deg:.1f}° ({critical_faces_pct:.1f}% da parede > 55°). "
                "Ative 'Limitar Overhang Automaticamente' ou reduza a profundidade das texturas."
            ),
            "en": (
                f"Critical overhang of {max_overhang_deg:.1f}° ({critical_faces_pct:.1f}% of wall > 55°). "
                "Enable 'Auto-Clamp Overhang' or reduce texture depth."
            ),
        })
    elif warning_faces_pct > 1.0 or max_overhang_deg > 45.0:
        warnings.append({
            "code": "MODERATE_OVERHANG",
            "pt": f"Overhang moderado de {max_overhang_deg:.1f}° ({warning_faces_pct:.1f}% > 45°). Use boa ventilacao de camada.",
            "en": f"Moderate overhang of {max_overhang_deg:.1f}° ({warning_faces_pct:.1f}% > 45°). Ensure strong part cooling.",
        })

    if spiral_gap_risk:
        warnings.append({
            "code": "SPIRAL_GAP_RISK",
            "pt": (
                f"Risco de frestas no Modo Vaso Espiral (passo lateral > largura de linha {eff_spiral_lw:.2f} mm). "
                "Aumente a largura da parede espiral, reduza altura de camada ou mude para Parede Dupla."
            ),
            "en": (
                f"Gap risk in Spiral Vase mode (stepover exceeds {eff_spiral_lw:.2f} mm line width). "
                "Increase spiral line width, lower layer height, or switch to Shelled Hollow mode."
            ),
        })

    if is_spiral and eff_spiral_lw > 2.0 * nozzle_mm + 1e-4:
        warnings.append({
            "code": "LINE_WIDTH_HIGH",
            "pt": f"Largura espiral ({eff_spiral_lw:.2f} mm) acima de 2x o bico ({nozzle_mm:.2f} mm).",
            "en": f"Spiral line width ({eff_spiral_lw:.2f} mm) exceeds 2x nozzle diameter ({nozzle_mm:.2f} mm).",
        })

    if (not is_spiral) and float(p["wall_thickness_mm"]) < 2.0 * line_w - 1e-4:
        warnings.append({
            "code": "THIN_SHELL_WALL",
            "pt": f"Espessura da parede ({p['wall_thickness_mm']:.2f} mm) muito fina para perimetros duplos ({2.0 * line_w:.2f} mm).",
            "en": f"Wall thickness ({p['wall_thickness_mm']:.2f} mm) is thin for dual perimeters ({2.0 * line_w:.2f} mm).",
        })

    min_foot = max(1.0, min(dx, dy))
    if dz / min_foot > 3.2:
        warnings.append({
            "code": "TALL_SLENDER_RATIO",
            "pt": "Proporcao alta e estreita — considere adicionar Brim no OrcaSlicer para aderencia extra.",
            "en": "Tall slender aspect ratio — consider enabling a Brim in OrcaSlicer for extra bed adhesion.",
        })

    return {
        "max_overhang_deg": max_overhang_deg,
        "warning_faces_pct": warning_faces_pct,
        "critical_faces_pct": critical_faces_pct,
        "fits_bed": fits_bed,
        "fits_height": fits_height,
        "spiral_gap_risk": spiral_gap_risk,
        "estimated_weight_g": est_weight_g,
        "estimated_volume_cm3": est_vol_cm3,
        "dimensions_mm": [dx, dy, dz],
        "triangle_count": tri_count,
        "warnings": warnings,
    }

# ===========================================================================
# MODULE: vase_studio.exporters
# ===========================================================================

"""Binary STL and OrcaSlicer 2.5.1 3MF project exporters for Orca Vase Studio."""

pass  # [bundled] hoisted __future__ import

import datetime as _dt
import json
import math
import struct
import uuid
import zipfile
from pathlib import Path
from typing import Any
from xml.sax.saxutils import escape as _xml_escape

import numpy as np

_STL_RECORD_DTYPE = np.dtype(
    [
        ("normal", "<f4", (3,)),
        ("v0", "<f4", (3,)),
        ("v1", "<f4", (3,)),
        ("v2", "<f4", (3,)),
        ("attr", "<u2"),
    ]
)

_CONTENT_TYPES_XML = """<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
 <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
 <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>
 <Default Extension="config" ContentType="text/xml"/>
 <Default Extension="png" ContentType="image/png"/>
 <Default Extension="json" ContentType="application/json"/>
</Types>
"""

_RELS_XML = """<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Target="/3D/3dmodel.model" Id="rel-1" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/>
</Relationships>
"""


def _extract_mesh_arrays(mesh: Any) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Extract validated (vertices, triangles, face_normals) arrays from duck-typed MeshData."""
    vertices = np.asarray(mesh.vertices, dtype=np.float32)
    if vertices.ndim != 2 or vertices.shape[1] != 3:
        raise ValueError(f"Expected vertices shape (V, 3), got {vertices.shape!r}")
    vertices = np.nan_to_num(vertices, nan=0.0, posinf=0.0, neginf=0.0).astype(np.float32, copy=False)

    triangles = np.asarray(mesh.triangles, dtype=np.int32)
    if triangles.size == 0:
        triangles = np.zeros((0, 3), dtype=np.int32)
    elif triangles.ndim != 2 or triangles.shape[1] != 3:
        raise ValueError(f"Expected triangles shape (F, 3), got {triangles.shape!r}")

    num_tris = triangles.shape[0]
    raw_normals = getattr(mesh, "face_normals", None)
    if (
        raw_normals is not None
        and np.asarray(raw_normals).shape == (num_tris, 3)
        and np.all(np.isfinite(raw_normals))
    ):
        normals = np.asarray(raw_normals, dtype=np.float32)
    elif num_tris > 0:
        tris_xyz = vertices[triangles]
        e1 = tris_xyz[:, 1, :] - tris_xyz[:, 0, :]
        e2 = tris_xyz[:, 2, :] - tris_xyz[:, 0, :]
        cross = np.cross(e1, e2)
        lengths = np.linalg.norm(cross, axis=1, keepdims=True)
        safe_lengths = np.where(lengths > 1e-12, lengths, 1.0)
        normals = (cross / safe_lengths).astype(np.float32)
        normals = np.where(lengths > 1e-12, normals, np.array([[0.0, 0.0, 1.0]], dtype=np.float32))
    else:
        normals = np.zeros((0, 3), dtype=np.float32)

    return vertices, triangles, normals


def _mesh_xy_extents(mesh: Any, vertices: np.ndarray | None = None) -> tuple[float, float]:
    """Return (width_x_mm, depth_y_mm) of a mesh from bounds_mm or vertices."""
    bounds = getattr(mesh, "bounds_mm", None)
    if isinstance(bounds, dict):
        size = bounds.get("size")
        if isinstance(size, (list, tuple)) and len(size) >= 2:
            return max(float(size[0]), 1.0), max(float(size[1]), 1.0)
        bmin = bounds.get("min")
        bmax = bounds.get("max")
        if isinstance(bmin, (list, tuple)) and isinstance(bmax, (list, tuple)) and len(bmin) >= 2 and len(bmax) >= 2:
            return max(float(bmax[0]) - float(bmin[0]), 1.0), max(float(bmax[1]) - float(bmin[1]), 1.0)
    verts = vertices if vertices is not None else np.asarray(mesh.vertices, dtype=np.float32)
    if verts.shape[0] == 0:
        return 10.0, 10.0
    dx = float(np.max(verts[:, 0]) - np.min(verts[:, 0]))
    dy = float(np.max(verts[:, 1]) - np.min(verts[:, 1]))
    return max(dx, 1.0), max(dy, 1.0)


def _resolve_bed_dimensions(host_config: dict | None) -> tuple[float, float]:
    """Extract (bed_x, bed_y) in mm from host_config with 220x220 fallback."""
    bed_x = 220.0
    bed_y = 220.0
    if isinstance(host_config, dict):
        if "bed_x" in host_config:
            try:
                bed_x = max(float(host_config["bed_x"]), 60.0)
            except (TypeError, ValueError):
                pass
        if "bed_y" in host_config:
            try:
                bed_y = max(float(host_config["bed_y"]), 60.0)
            except (TypeError, ValueError):
                pass
        printer = host_config.get("printer")
        if isinstance(printer, dict):
            if "bed_x" in printer and "bed_x" not in host_config:
                try:
                    bed_x = max(float(printer["bed_x"]), 60.0)
                except (TypeError, ValueError):
                    pass
            if "bed_y" in printer and "bed_y" not in host_config:
                try:
                    bed_y = max(float(printer["bed_y"]), 60.0)
                except (TypeError, ValueError):
                    pass
    return bed_x, bed_y


def _positions_overlap(
    positions: list[tuple[float, float, float]],
    extents: list[tuple[float, float]],
    min_clearance_mm: float = 3.0,
) -> bool:
    """Return True if any two items overlap on the XY build plate."""
    n = len(positions)
    for i in range(n):
        xi, yi, _ = positions[i]
        wxi, wyi = extents[i]
        for j in range(i + 1, n):
            xj, yj, _ = positions[j]
            wxj, wyj = extents[j]
            overlap_x = abs(xi - xj) < (0.5 * (wxi + wxj) + min_clearance_mm)
            overlap_y = abs(yi - yj) < (0.5 * (wyi + wyj) + min_clearance_mm)
            if overlap_x and overlap_y:
                return True
    return False


def _arrange_items_on_bed(
    extents: list[tuple[float, float]],
    z_offsets: list[float],
    bed_x: float,
    bed_y: float,
    gap_mm: float = 10.0,
) -> list[tuple[float, float, float]]:
    """Arrange 1 or more items cleanly around the bed center without XY overlap."""
    cx = bed_x * 0.5
    cy = bed_y * 0.5
    count = len(extents)
    if count == 0:
        return []
    if count == 1:
        return [(cx, cy, z_offsets[0])]

    if count == 2:
        (w0, d0), (w1, d1) = extents
        total_w = w0 + gap_mm + w1
        if total_w <= bed_x - 8.0:
            left_edge = cx - 0.5 * total_w
            x0 = left_edge + 0.5 * w0
            x1 = left_edge + w0 + gap_mm + 0.5 * w1
            return [(x0, cy, z_offsets[0]), (x1, cy, z_offsets[1])]

        # Place along the bed diagonal when side-by-side exceeds X width
        r0 = 0.5 * max(w0, d0)
        r1 = 0.5 * max(w1, d1)
        diag_sep = r0 + r1 + gap_mm
        step = diag_sep / math.sqrt(2.0)
        half_step = 0.5 * step
        x0 = max(r0 + 2.0, cx - half_step)
        y0 = max(r0 + 2.0, cy - half_step)
        x1 = min(bed_x - r1 - 2.0, cx + half_step)
        y1 = min(bed_y - r1 - 2.0, cy + half_step)
        if math.hypot(x1 - x0, y1 - y0) >= (r0 + r1 + 2.0):
            return [(x0, y0, z_offsets[0]), (x1, y1, z_offsets[1])]
        # If combined radii exceed diagonal bed size, still place cleanly separated
        return [(cx - half_step, cy - half_step, z_offsets[0]), (cx + half_step, cy + half_step, z_offsets[1])]

    # General grid/row layout for 3+ items
    total_w = sum(w for w, _ in extents) + gap_mm * (count - 1)
    cursor_x = cx - 0.5 * total_w
    placed: list[tuple[float, float, float]] = []
    for idx, (w, _) in enumerate(extents):
        px = cursor_x + 0.5 * w
        placed.append((px, cy, z_offsets[idx]))
        cursor_x += w + gap_mm
    return placed


def _build_project_settings_dict(params: dict | None, host_config: dict | None) -> dict[str, Any]:
    """Merge host project settings with print-mode overrides for OrcaSlicer 2.5.1."""
    merged: dict[str, Any] = {}
    if isinstance(host_config, dict):
        raw_ps = host_config.get("project_settings")
        if isinstance(raw_ps, dict):
            merged.update(raw_ps)

    p = params if isinstance(params, dict) else {}
    print_mode = str(p.get("print_mode", "spiral_vase")).strip().lower()

    if print_mode == "shelled_hollow":
        wall_thickness = max(0.8, float(p.get("wall_thickness_mm", 2.2)))
        bottom_thickness = max(1.0, float(p.get("bottom_thickness_mm", 3.2)))
        merged["spiral_mode"] = "0"
        merged["spiral_mode_smooth"] = "0"
        if str(merged.get("wall_loops", "")).strip() in ("", "0", "1"):
            merged["wall_loops"] = str(max(2, min(6, int(round(wall_thickness / 0.84)))))
        if str(merged.get("top_shell_layers", "")).strip() in ("", "0"):
            merged["top_shell_layers"] = "4"
        if str(merged.get("bottom_shell_layers", "")).strip() in ("", "0"):
            merged["bottom_shell_layers"] = str(max(3, int(round(bottom_thickness / 0.20))))
        if str(merged.get("sparse_infill_density", "")).strip() in ("", "0", "0%"):
            merged["sparse_infill_density"] = "15%"
    else:
        spiral_smooth = bool(p.get("spiral_smooth", True))
        spiral_bottom_layers = max(2, min(20, int(round(float(p.get("spiral_bottom_layers", 5))))))
        spiral_line_width = max(0.30, min(1.50, float(p.get("spiral_line_width_mm", 0.65))))
        merged["spiral_mode"] = "1"
        merged["spiral_mode_smooth"] = "1" if spiral_smooth else "0"
        merged["wall_loops"] = "1"
        merged["top_shell_layers"] = "0"
        merged["sparse_infill_density"] = "0%"
        merged["bottom_shell_layers"] = str(spiral_bottom_layers)
        merged["outer_wall_line_width"] = f"{spiral_line_width:.2f}"

    return merged


def write_binary_stl(path: str | Path, mesh: Any, header_name: str = "OrcaVaseStudio") -> Path:
    """Write a duck-typed MeshData object to a standard little-endian binary STL file.

    Binary layout: 80-byte ASCII header + uint32 triangle count + F * 50-byte facet records.
    """
    out_path = Path(path)
    if not out_path.parent.exists():
        out_path.parent.mkdir(parents=True, exist_ok=True)

    vertices, triangles, normals = _extract_mesh_arrays(mesh)
    num_triangles = int(triangles.shape[0])

    clean_header = str(header_name or "OrcaVaseStudio").strip() or "OrcaVaseStudio"
    if clean_header.lower().startswith("solid"):
        clean_header = f"Orca_{clean_header}"
    header_text = f"{clean_header} - Orca Vase Studio Binary STL"
    header_bytes = header_text.encode("ascii", errors="replace")[:80].ljust(80, b"\x00")

    records = np.zeros(num_triangles, dtype=_STL_RECORD_DTYPE)
    if num_triangles > 0:
        tris_xyz = vertices[triangles]
        records["normal"] = normals.astype("<f4", copy=False)
        records["v0"] = tris_xyz[:, 0, :].astype("<f4", copy=False)
        records["v1"] = tris_xyz[:, 1, :].astype("<f4", copy=False)
        records["v2"] = tris_xyz[:, 2, :].astype("<f4", copy=False)
        records["attr"] = 0

    with open(out_path, "wb") as fh:
        fh.write(header_bytes)
        fh.write(struct.pack("<I", num_triangles))
        if num_triangles > 0:
            fh.write(records.tobytes())

    return out_path


def write_orca_3mf(
    path: str | Path,
    items: list[tuple[str, Any, tuple[float, float, float]]],
    params: dict,
    host_config: dict | None = None,
) -> Path:
    """Write an OrcaSlicer 2.5.1 compatible .3mf project archive with meshes and slicer settings."""
    if not items:
        raise ValueError("write_orca_3mf requires at least one item in 'items'.")

    out_path = Path(path)
    if not out_path.parent.exists():
        out_path.parent.mkdir(parents=True, exist_ok=True)

    bed_x, bed_y = _resolve_bed_dimensions(host_config)
    cx, cy = bed_x * 0.5, bed_y * 0.5

    parsed_items: list[tuple[str, np.ndarray, np.ndarray, tuple[float, float]]] = []
    raw_positions: list[tuple[float, float, float] | None] = []
    z_offsets: list[float] = []

    for idx, entry in enumerate(items):
        if len(entry) == 2:
            raw_name, mesh = entry  # type: ignore[misc]
            raw_pos = None
        elif len(entry) >= 3:
            raw_name, mesh, raw_pos = entry[0], entry[1], entry[2]
        else:
            raise ValueError(f"Invalid item tuple at index {idx}: {entry!r}")

        item_name = str(raw_name or f"Object_{idx + 1}").strip() or f"Object_{idx + 1}"
        vertices, triangles, _ = _extract_mesh_arrays(mesh)
        ext = _mesh_xy_extents(mesh, vertices)
        parsed_items.append((item_name, vertices, triangles, ext))

        if raw_pos is None:
            raw_positions.append(None)
            z_offsets.append(0.0)
        else:
            px, py, pz = float(raw_pos[0]), float(raw_pos[1]), float(raw_pos[2])
            raw_positions.append((px, py, pz))
            z_offsets.append(pz)

    extents_list = [it[3] for it in parsed_items]
    if any(pos is None for pos in raw_positions):
        if len(parsed_items) == 1:
            final_positions = [(cx, cy, z_offsets[0])]
        else:
            final_positions = _arrange_items_on_bed(extents_list, z_offsets, bed_x, bed_y, gap_mm=10.0)
    else:
        concrete_positions = [pos for pos in raw_positions if pos is not None]
        if len(concrete_positions) >= 2 and _positions_overlap(concrete_positions, extents_list, min_clearance_mm=3.0):
            final_positions = _arrange_items_on_bed(extents_list, z_offsets, bed_x, bed_y, gap_mm=10.0)
        else:
            final_positions = concrete_positions

    title = str((params or {}).get("name") or parsed_items[0][0] or "Orca Vase Studio").strip()
    escaped_title = _xml_escape(title, {'"': "&quot;"})
    today_iso = _dt.date.today().isoformat()
    ns_seed = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
    build_uuid = str(uuid.uuid5(ns_seed, f"orca-vase-build-{title}"))

    object_blocks: list[str] = []
    build_items_xml: list[str] = []
    model_settings_objects: list[str] = []
    model_settings_instances: list[str] = []
    model_settings_assemble: list[str] = []

    for idx, (item_name, vertices, triangles, _) in enumerate(parsed_items):
        obj_id = idx + 1
        tx, ty, tz = final_positions[idx]
        esc_name = _xml_escape(item_name, {'"': "&quot;"})
        obj_uuid = str(uuid.uuid5(ns_seed, f"orca-vase-obj-{obj_id}-{item_name}"))
        item_uuid = str(uuid.uuid5(ns_seed, f"orca-vase-item-{obj_id}-{item_name}"))

        verts_py = vertices.tolist()
        tris_py = triangles.tolist()

        vertex_lines = "\n".join(
            f'     <vertex x="{vx:.5f}" y="{vy:.5f}" z="{vz:.5f}"/>'
            for vx, vy, vz in verts_py
        )
        triangle_lines = "\n".join(
            f'     <triangle v1="{v1}" v2="{v2}" v3="{v3}"/>'
            for v1, v2, v3 in tris_py
        )

        object_blocks.append(
            f'  <object id="{obj_id}" p:UUID="{obj_uuid}" name="{esc_name}" type="model">\n'
            f"   <mesh>\n"
            f"    <vertices>\n"
            f"{vertex_lines}\n"
            f"    </vertices>\n"
            f"    <triangles>\n"
            f"{triangle_lines}\n"
            f"    </triangles>\n"
            f"   </mesh>\n"
            f"  </object>"
        )

        transform_3x4 = f"1 0 0 0 1 0 0 0 1 {tx:.4f} {ty:.4f} {tz:.4f}"
        build_items_xml.append(
            f'  <item objectid="{obj_id}" p:UUID="{item_uuid}" transform="{transform_3x4}" printable="1"/>'
        )

        model_settings_objects.append(
            f'  <object id="{obj_id}">\n'
            f'    <metadata key="name" value="{esc_name}"/>\n'
            f'    <metadata key="extruder" value="1"/>\n'
            f'    <part id="1" subtype="normal_part">\n'
            f'      <metadata key="name" value="{esc_name}"/>\n'
            f'      <metadata key="matrix" value="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>\n'
            f'      <mesh_stat edges_fixed="0" degenerate_facets="0" facets_removed="0" facets_reversed="0" backwards_edges="0"/>\n'
            f"    </part>\n"
            f"  </object>"
        )
        model_settings_instances.append(
            f"    <model_instance>\n"
            f'      <metadata key="object_id" value="{obj_id}"/>\n'
            f'      <metadata key="instance_id" value="0"/>\n'
            f'      <metadata key="identify_id" value="{100 + obj_id}"/>\n'
            f"    </model_instance>"
        )
        model_settings_assemble.append(
            f'    <assemble_item object_id="{obj_id}" instance_id="0" transform="{transform_3x4}" offset="0 0 0"/>'
        )

    model_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<model unit="millimeter" xml:lang="en-US" '
        'xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" '
        'xmlns:BambuStudio="http://schemas.bambulab.com/package/2021" '
        'xmlns:p="http://schemas.microsoft.com/3dmanufacturing/production/2015/06" '
        'requiredextensions="p">\n'
        ' <metadata name="Application">OrcaSlicer-2.5.1</metadata>\n'
        ' <metadata name="OrcaSlicer">2.5.1</metadata>\n'
        ' <metadata name="BambuStudio:3mfVersion">1</metadata>\n'
        f' <metadata name="Title">{escaped_title}</metadata>\n'
        f' <metadata name="CreationDate">{today_iso}</metadata>\n'
        " <resources>\n"
        + "\n".join(object_blocks)
        + "\n </resources>\n"
        + f' <build p:UUID="{build_uuid}">\n'
        + "\n".join(build_items_xml)
        + "\n </build>\n"
        "</model>\n"
    )

    model_settings_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        "<config>\n"
        + "\n".join(model_settings_objects)
        + "\n  <plate>\n"
        '    <metadata key="plater_id" value="1"/>\n'
        '    <metadata key="plater_name" value=""/>\n'
        '    <metadata key="locked" value="false"/>\n'
        + "\n".join(model_settings_instances)
        + "\n  </plate>\n"
        "  <assemble>\n"
        + "\n".join(model_settings_assemble)
        + "\n  </assemble>\n"
        "</config>\n"
    )

    project_settings = _build_project_settings_dict(params, host_config)
    project_settings_json = json.dumps(project_settings, indent=2, ensure_ascii=False)

    with zipfile.ZipFile(out_path, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        zf.writestr("[Content_Types].xml", _CONTENT_TYPES_XML)
        zf.writestr("_rels/.rels", _RELS_XML)
        zf.writestr("3D/3dmodel.model", model_xml)
        zf.writestr("Metadata/model_settings.config", model_settings_xml)
        zf.writestr("Metadata/project_settings.config", project_settings_json)

    return out_path

# ===========================================================================
# MODULE: vase_studio.presets_catalog
# ===========================================================================

"""Curated built-in presets catalog, user preset storage, and smart printable randomizer."""

pass  # [bundled] hoisted __future__ import

import copy
import datetime as _dt
import json
import math
import random
import re
import uuid
from pathlib import Path
from typing import Any

_PRESETS_FALLBACK_DEFAULT_PARAMS: dict[str, Any] = {
    "name": "Ondas Organicas",
    "height_mm": 160.0,
    "base_diameter_mm": 76.0,
    "belly_diameter_mm": 110.0,
    "belly_height_ratio": 0.34,
    "waist_diameter_mm": 68.0,
    "waist_height_ratio": 0.68,
    "neck_diameter_mm": 82.0,
    "lip_flare_mm": 4.0,
    "lip_bevel_mm": 1.0,
    "polygon_sides": 0,
    "polygon_roundness": 0.35,
    "use_custom_profile": False,
    "profile_points": [
        [0.0, 38.0],
        [0.34, 55.0],
        [0.68, 34.0],
        [0.92, 41.0],
        [1.0, 45.0],
    ],
    "resolution_angular": 240,
    "resolution_vertical": 220,
    "bottom_fade_mm": 8.0,
    "top_fade_mm": 6.0,
    "global_twist_deg": 0.0,
    "textures": {
        "ribbed": {
            "enabled": False,
            "depth_mm": 2.6,
            "count": 32,
            "duty_cycle": 0.50,
            "sharpness": 0.35,
            "twist_deg": 60.0,
            "phase_deg": 0.0,
        },
        "waves": {
            "enabled": True,
            "depth_mm": 3.0,
            "vertical_wavelength_mm": 26.0,
            "angular_lobes": 6,
            "interference_mix": 0.45,
            "wave_skew": 0.0,
            "phase_deg": 0.0,
        },
        "origami": {
            "enabled": False,
            "depth_mm": 3.2,
            "cells_around": 12,
            "cells_vertical": 8,
            "crease_sharpness": 0.75,
            "stagger": 0.50,
        },
        "cellular": {
            "enabled": False,
            "depth_mm": 2.4,
            "scale_angular": 8,
            "scale_vertical_mm": 22.0,
            "ridge_mode": True,
            "octaves": 2,
            "seed": 42,
        },
    },
    "print_mode": "shelled_hollow",
    "stl_always_open_hollow": True,
    "auto_configure_slicer": True,
    "spiral_line_width_mm": 0.65,
    "spiral_bottom_layers": 5,
    "spiral_smooth": True,
    "wall_thickness_mm": 2.4,
    "bottom_thickness_mm": 3.2,
    "auto_clamp_overhang": False,
    "max_safe_overhang_deg": 48.0,
    "drainage": {
        "enabled": False,
        "hole_count": 4,
        "hole_diameter_mm": 8.0,
        "ring_radius_ratio": 0.48,
    },
    "saucer": {
        "clearance_mm": 8.0,
        "rim_height_mm": 22.0,
        "wall_thickness_mm": 2.4,
        "floor_thickness_mm": 2.6,
        "inner_ribs_height_mm": 2.0,
        "match_vase_texture": True,
    },
}


def _presets_clamp_float(val: Any, lo: float, hi: float, default: float) -> float:
    try:
        num = float(val)
        if not math.isfinite(num):
            return default
        return max(lo, min(hi, num))
    except (TypeError, ValueError):
        return default


def _presets_clamp_int(val: Any, lo: int, hi: int, default: int) -> int:
    try:
        num = int(round(float(val)))
        return max(lo, min(hi, num))
    except (TypeError, ValueError):
        return default


def _presets_to_bool(val: Any, default: bool) -> bool:
    if isinstance(val, bool):
        return val
    if isinstance(val, (int, float)):
        return bool(val) if math.isfinite(val) else default
    if isinstance(val, str):
        s = val.strip().lower()
        if s in ("true", "1", "yes", "on"):
            return True
        if s in ("false", "0", "no", "off", ""):
            return False
    return default


def _presets_deep_merge(dst: dict[str, Any], src: dict[str, Any]) -> None:
    for k, v in src.items():
        if isinstance(v, dict) and isinstance(dst.get(k), dict):
            _presets_deep_merge(dst[k], v)
        else:
            dst[k] = copy.deepcopy(v)


def _presets_fallback_normalize(raw: dict | None = None) -> dict[str, Any]:
    out = copy.deepcopy(_PRESETS_FALLBACK_DEFAULT_PARAMS)
    if isinstance(raw, dict):
        _presets_deep_merge(out, raw)

    out["name"] = str(out.get("name") or "Ondas Organicas").strip()[:100] or "Ondas Organicas"
    out["height_mm"] = _presets_clamp_float(out.get("height_mm"), 30.0, 500.0, 160.0)
    out["base_diameter_mm"] = _presets_clamp_float(out.get("base_diameter_mm"), 20.0, 450.0, 76.0)
    out["belly_diameter_mm"] = _presets_clamp_float(out.get("belly_diameter_mm"), 20.0, 450.0, 110.0)
    out["belly_height_ratio"] = _presets_clamp_float(out.get("belly_height_ratio"), 0.08, 0.85, 0.34)
    out["waist_diameter_mm"] = _presets_clamp_float(out.get("waist_diameter_mm"), 16.0, 450.0, 68.0)
    out["waist_height_ratio"] = _presets_clamp_float(out.get("waist_height_ratio"), 0.15, 0.92, 0.68)
    out["neck_diameter_mm"] = _presets_clamp_float(out.get("neck_diameter_mm"), 16.0, 450.0, 82.0)
    out["lip_flare_mm"] = _presets_clamp_float(out.get("lip_flare_mm"), -15.0, 25.0, 4.0)
    out["lip_bevel_mm"] = _presets_clamp_float(out.get("lip_bevel_mm"), 0.0, 4.0, 1.0)

    poly = _presets_clamp_int(out.get("polygon_sides"), 0, 24, 0)
    out["polygon_sides"] = 0 if poly < 3 else poly
    out["polygon_roundness"] = _presets_clamp_float(out.get("polygon_roundness"), 0.0, 1.0, 0.35)
    out["use_custom_profile"] = bool(out.get("use_custom_profile", False))

    pts_raw = out.get("profile_points")
    pts: list[list[float]] = []
    if isinstance(pts_raw, list):
        for item in pts_raw:
            if isinstance(item, (list, tuple)) and len(item) >= 2:
                zn = _presets_clamp_float(item[0], 0.0, 1.0, 0.0)
                rm = _presets_clamp_float(item[1], 8.0, 225.0, 38.0)
                pts.append([zn, rm])
    if len(pts) < 2:
        pts = copy.deepcopy(_PRESETS_FALLBACK_DEFAULT_PARAMS["profile_points"])
    pts.sort(key=lambda pair: pair[0])
    pts[0][0] = 0.0
    pts[-1][0] = 1.0
    out["profile_points"] = pts

    out["resolution_angular"] = _presets_clamp_int(out.get("resolution_angular"), 64, 360, 240)
    out["resolution_vertical"] = _presets_clamp_int(out.get("resolution_vertical"), 60, 400, 220)
    out["bottom_fade_mm"] = _presets_clamp_float(out.get("bottom_fade_mm"), 0.0, 60.0, 8.0)
    out["top_fade_mm"] = _presets_clamp_float(out.get("top_fade_mm"), 0.0, 60.0, 6.0)
    out["global_twist_deg"] = _presets_clamp_float(out.get("global_twist_deg"), -720.0, 720.0, 0.0)

    tex = out["textures"]
    rib = tex["ribbed"]
    rib["enabled"] = bool(rib.get("enabled", False))
    rib["depth_mm"] = _presets_clamp_float(rib.get("depth_mm"), -15.0, 15.0, 2.6)
    rib["count"] = _presets_clamp_int(rib.get("count"), 3, 180, 32)
    rib["duty_cycle"] = _presets_clamp_float(rib.get("duty_cycle"), 0.10, 0.90, 0.50)
    rib["sharpness"] = _presets_clamp_float(rib.get("sharpness"), 0.0, 1.0, 0.35)
    rib["twist_deg"] = _presets_clamp_float(rib.get("twist_deg"), -720.0, 720.0, 60.0)
    rib["phase_deg"] = _presets_clamp_float(rib.get("phase_deg"), 0.0, 360.0, 0.0)

    wav = tex["waves"]
    wav["enabled"] = bool(wav.get("enabled", True))
    wav["depth_mm"] = _presets_clamp_float(wav.get("depth_mm"), -15.0, 15.0, 3.0)
    wav["vertical_wavelength_mm"] = _presets_clamp_float(wav.get("vertical_wavelength_mm"), 4.0, 120.0, 26.0)
    wav["angular_lobes"] = _presets_clamp_int(wav.get("angular_lobes"), 0, 48, 6)
    wav["interference_mix"] = _presets_clamp_float(wav.get("interference_mix"), 0.0, 1.0, 0.45)
    wav["wave_skew"] = _presets_clamp_float(wav.get("wave_skew"), -0.8, 0.8, 0.0)
    wav["phase_deg"] = _presets_clamp_float(wav.get("phase_deg"), 0.0, 360.0, 0.0)

    ori = tex["origami"]
    ori["enabled"] = bool(ori.get("enabled", False))
    ori["depth_mm"] = _presets_clamp_float(ori.get("depth_mm"), -15.0, 15.0, 3.2)
    ori["cells_around"] = _presets_clamp_int(ori.get("cells_around"), 3, 60, 12)
    ori["cells_vertical"] = _presets_clamp_int(ori.get("cells_vertical"), 2, 50, 8)
    ori["crease_sharpness"] = _presets_clamp_float(ori.get("crease_sharpness"), 0.0, 1.0, 0.75)
    ori["stagger"] = _presets_clamp_float(ori.get("stagger"), 0.0, 1.0, 0.50)

    cel = tex["cellular"]
    cel["enabled"] = bool(cel.get("enabled", False))
    cel["depth_mm"] = _presets_clamp_float(cel.get("depth_mm"), -12.0, 12.0, 2.4)
    cel["scale_angular"] = _presets_clamp_int(cel.get("scale_angular"), 2, 40, 8)
    cel["scale_vertical_mm"] = _presets_clamp_float(cel.get("scale_vertical_mm"), 5.0, 100.0, 22.0)
    cel["ridge_mode"] = bool(cel.get("ridge_mode", True))
    cel["octaves"] = _presets_clamp_int(cel.get("octaves"), 1, 4, 2)
    cel["seed"] = _presets_clamp_int(cel.get("seed"), 1, 99999, 42)

    pm = str(out.get("print_mode", "shelled_hollow")).strip().lower()
    out["print_mode"] = pm if pm in ("spiral_vase", "shelled_hollow") else "shelled_hollow"
    out["stl_always_open_hollow"] = _presets_to_bool(out.get("stl_always_open_hollow"), True)
    out["auto_configure_slicer"] = _presets_to_bool(out.get("auto_configure_slicer"), True)
    out["spiral_line_width_mm"] = _presets_clamp_float(out.get("spiral_line_width_mm"), 0.40, 1.20, 0.65)
    out["spiral_bottom_layers"] = _presets_clamp_int(out.get("spiral_bottom_layers"), 2, 15, 5)
    out["spiral_smooth"] = _presets_to_bool(out.get("spiral_smooth"), True)
    out["wall_thickness_mm"] = _presets_clamp_float(out.get("wall_thickness_mm"), 0.8, 25.0, 2.4)
    out["bottom_thickness_mm"] = _presets_clamp_float(out.get("bottom_thickness_mm"), 1.0, 25.0, 3.2)
    out["auto_clamp_overhang"] = _presets_to_bool(out.get("auto_clamp_overhang"), False)
    out["max_safe_overhang_deg"] = _presets_clamp_float(out.get("max_safe_overhang_deg"), 35.0, 65.0, 48.0)

    drn = out["drainage"]
    drn["enabled"] = bool(drn.get("enabled", False))
    drn["hole_count"] = _presets_clamp_int(drn.get("hole_count"), 1, 9, 4)
    drn["hole_diameter_mm"] = _presets_clamp_float(drn.get("hole_diameter_mm"), 3.0, 20.0, 8.0)
    drn["ring_radius_ratio"] = _presets_clamp_float(drn.get("ring_radius_ratio"), 0.0, 0.68, 0.48)

    scr = out["saucer"]
    scr["clearance_mm"] = _presets_clamp_float(scr.get("clearance_mm"), 3.0, 25.0, 8.0)
    scr["rim_height_mm"] = _presets_clamp_float(scr.get("rim_height_mm"), 10.0, 60.0, 22.0)
    scr["wall_thickness_mm"] = _presets_clamp_float(scr.get("wall_thickness_mm"), 1.2, 5.0, 2.4)
    scr["floor_thickness_mm"] = _presets_clamp_float(scr.get("floor_thickness_mm"), 1.2, 6.0, 2.6)
    scr["inner_ribs_height_mm"] = _presets_clamp_float(scr.get("inner_ribs_height_mm"), 0.0, 6.0, 2.0)
    scr["match_vase_texture"] = bool(scr.get("match_vase_texture", True))

    return out


try:
    pass  # [bundled] resolved intra-package import

    pass
except (ImportError, KeyError, ValueError):
    pass

if "DEFAULT_PARAMS" not in globals() or "normalize_params" not in globals():
    DEFAULT_PARAMS = _PRESETS_FALLBACK_DEFAULT_PARAMS
    normalize_params = _presets_fallback_normalize


_USER_PRESETS_FILENAME = "user_presets.json"


def _make_preset_params(overrides: dict[str, Any]) -> dict[str, Any]:
    """Build a clean preset parameter dictionary starting with all textures disabled unless specified."""
    base = copy.deepcopy(DEFAULT_PARAMS)
    for t_cfg in base["textures"].values():
        t_cfg["enabled"] = False
    _presets_deep_merge(base, overrides)
    return normalize_params(base)


BUILTIN_PRESETS: list[dict[str, Any]] = [
    {
        "id": "ondas_organicas",
        "title_pt": "Ondas Orgânicas",
        "title_en": "Organic Waves",
        "category": "organic",
        "description_pt": "Ondulações contra-helicoidais fluidas inspiradas em dunas e correntes marinhas.",
        "description_en": "Flowing counter-helical ripples inspired by coastal dunes and ocean currents.",
        "params": _make_preset_params(
            {
                "name": "Ondas Orgânicas",
                "height_mm": 165.0,
                "base_diameter_mm": 76.0,
                "belly_diameter_mm": 112.0,
                "belly_height_ratio": 0.34,
                "waist_diameter_mm": 68.0,
                "waist_height_ratio": 0.68,
                "neck_diameter_mm": 82.0,
                "lip_flare_mm": 4.0,
                "bottom_fade_mm": 10.0,
                "top_fade_mm": 7.0,
                "global_twist_deg": 40.0,
                "textures": {
                    "waves": {
                        "enabled": True,
                        "depth_mm": 3.0,
                        "vertical_wavelength_mm": 26.0,
                        "angular_lobes": 6,
                        "interference_mix": 0.45,
                        "wave_skew": 0.15,
                        "phase_deg": 0.0,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.4,
                "bottom_thickness_mm": 3.2,
                "spiral_line_width_mm": 0.65,
                "spiral_bottom_layers": 5,
            }
        ),
    },
    {
        "id": "colunas_caneladas",
        "title_pt": "Colunas Caneladas",
        "title_en": "Architectural Fluted",
        "category": "architectural",
        "description_pt": "Caneluras verticais clássicas com espaçamento arquitetônico limpo e sombra marcada.",
        "description_en": "Crisp vertical architectural flutes with balanced flat fillets and clean shadow lines.",
        "params": _make_preset_params(
            {
                "name": "Colunas Caneladas",
                "height_mm": 190.0,
                "base_diameter_mm": 84.0,
                "belly_diameter_mm": 102.0,
                "belly_height_ratio": 0.40,
                "waist_diameter_mm": 88.0,
                "waist_height_ratio": 0.76,
                "neck_diameter_mm": 90.0,
                "lip_flare_mm": 3.0,
                "bottom_fade_mm": 9.0,
                "top_fade_mm": 8.0,
                "global_twist_deg": 0.0,
                "textures": {
                    "ribbed": {
                        "enabled": True,
                        "depth_mm": 2.5,
                        "count": 36,
                        "duty_cycle": 0.58,
                        "sharpness": 0.35,
                        "twist_deg": 0.0,
                        "phase_deg": 0.0,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.8,
                "bottom_thickness_mm": 3.6,
                "spiral_line_width_mm": 0.65,
                "spiral_bottom_layers": 5,
            }
        ),
    },
    {
        "id": "helice_escultural",
        "title_pt": "Hélice Escultural",
        "title_en": "Twisted Helix",
        "category": "sculptural",
        "description_pt": "Lâminas helicoidais contínuas combinadas com seção octogonal suavizada.",
        "description_en": "Sweeping helical fins paired with a softened octagonal cross-section.",
        "params": _make_preset_params(
            {
                "name": "Hélice Escultural",
                "height_mm": 185.0,
                "base_diameter_mm": 78.0,
                "belly_diameter_mm": 108.0,
                "belly_height_ratio": 0.36,
                "waist_diameter_mm": 72.0,
                "waist_height_ratio": 0.72,
                "neck_diameter_mm": 80.0,
                "lip_flare_mm": 3.5,
                "polygon_sides": 8,
                "polygon_roundness": 0.55,
                "bottom_fade_mm": 12.0,
                "top_fade_mm": 8.0,
                "global_twist_deg": 180.0,
                "textures": {
                    "ribbed": {
                        "enabled": True,
                        "depth_mm": 2.4,
                        "count": 16,
                        "duty_cycle": 0.65,
                        "sharpness": 0.55,
                        "twist_deg": 180.0,
                        "phase_deg": 0.0,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.4,
                "bottom_thickness_mm": 3.2,
                "spiral_line_width_mm": 0.68,
                "spiral_bottom_layers": 5,
            }
        ),
    },
    {
        "id": "origami_yoshimura",
        "title_pt": "Origami Yoshimura",
        "title_en": "Yoshimura Origami Diamond",
        "category": "geometric",
        "description_pt": "Dobragem geométrica em diamantes alternados estilo Yoshimura com vincos precisos.",
        "description_en": "Authentic staggered diamond origami facets with crisp Yoshimura paper creases.",
        "params": _make_preset_params(
            {
                "name": "Origami Yoshimura",
                "height_mm": 160.0,
                "base_diameter_mm": 82.0,
                "belly_diameter_mm": 104.0,
                "belly_height_ratio": 0.42,
                "waist_diameter_mm": 86.0,
                "waist_height_ratio": 0.76,
                "neck_diameter_mm": 84.0,
                "lip_flare_mm": 1.5,
                "bottom_fade_mm": 10.0,
                "top_fade_mm": 8.0,
                "global_twist_deg": 15.0,
                "textures": {
                    "origami": {
                        "enabled": True,
                        "depth_mm": 3.2,
                        "cells_around": 12,
                        "cells_vertical": 9,
                        "crease_sharpness": 0.82,
                        "stagger": 0.50,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.0,
                "bottom_thickness_mm": 3.0,
                "auto_clamp_overhang": True,
                "max_safe_overhang_deg": 48.0,
            }
        ),
    },
    {
        "id": "recife_celular",
        "title_pt": "Recife Celular",
        "title_en": "Cellular Coral",
        "category": "organic",
        "description_pt": "Veios orgânicos tridimensionais inspirados em corais marinhos e rocha vulcânica.",
        "description_en": "Three-dimensional ridged veins inspired by reef coral and carved volcanic stone.",
        "params": _make_preset_params(
            {
                "name": "Recife Celular",
                "height_mm": 150.0,
                "base_diameter_mm": 80.0,
                "belly_diameter_mm": 118.0,
                "belly_height_ratio": 0.38,
                "waist_diameter_mm": 76.0,
                "waist_height_ratio": 0.74,
                "neck_diameter_mm": 70.0,
                "lip_flare_mm": 2.5,
                "bottom_fade_mm": 10.0,
                "top_fade_mm": 8.0,
                "global_twist_deg": 24.0,
                "textures": {
                    "cellular": {
                        "enabled": True,
                        "depth_mm": 2.8,
                        "scale_angular": 9,
                        "scale_vertical_mm": 20.0,
                        "ridge_mode": True,
                        "octaves": 3,
                        "seed": 108,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.6,
                "bottom_thickness_mm": 3.4,
                "auto_clamp_overhang": True,
                "max_safe_overhang_deg": 48.0,
            }
        ),
    },
    {
        "id": "tulipa_minimalista",
        "title_pt": "Tulipa Minimalista",
        "title_en": "Minimalist Tulip",
        "category": "minimal",
        "description_pt": "Silhueta escandinava pura e serena com lábio suavemente aberto e parede espessa.",
        "description_en": "Pure Scandinavian silhouette with a serene waist and gently flared tulip rim.",
        "params": _make_preset_params(
            {
                "name": "Tulipa Minimalista",
                "height_mm": 175.0,
                "base_diameter_mm": 70.0,
                "belly_diameter_mm": 106.0,
                "belly_height_ratio": 0.28,
                "waist_diameter_mm": 58.0,
                "waist_height_ratio": 0.72,
                "neck_diameter_mm": 66.0,
                "lip_flare_mm": 6.0,
                "lip_bevel_mm": 1.4,
                "bottom_fade_mm": 8.0,
                "top_fade_mm": 6.0,
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.6,
                "bottom_thickness_mm": 3.4,
                "spiral_line_width_mm": 0.75,
                "spiral_bottom_layers": 6,
            }
        ),
    },
    {
        "id": "cachepo_botanico",
        "title_pt": "Cachepô Botânico + Pratinho",
        "title_en": "Botanical Planter + Saucer",
        "category": "garden",
        "description_pt": "Vaso estrutural oco com parede dupla, furos de drenagem reais e pratinho coletor.",
        "description_en": "Sturdy shelled hollow planter with real drainage tunnels and matching drip saucer.",
        "params": _make_preset_params(
            {
                "name": "Cachepô Botânico",
                "height_mm": 125.0,
                "base_diameter_mm": 112.0,
                "belly_diameter_mm": 132.0,
                "belly_height_ratio": 0.45,
                "waist_diameter_mm": 136.0,
                "waist_height_ratio": 0.78,
                "neck_diameter_mm": 138.0,
                "lip_flare_mm": 2.0,
                "lip_bevel_mm": 1.4,
                "bottom_fade_mm": 8.0,
                "top_fade_mm": 6.0,
                "textures": {
                    "ribbed": {
                        "enabled": True,
                        "depth_mm": 1.8,
                        "count": 42,
                        "duty_cycle": 0.62,
                        "sharpness": 0.25,
                        "twist_deg": 0.0,
                        "phase_deg": 0.0,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 3.2,
                "bottom_thickness_mm": 3.8,
                "drainage": {
                    "enabled": True,
                    "hole_count": 4,
                    "hole_diameter_mm": 8.0,
                    "ring_radius_ratio": 0.46,
                },
                "saucer": {
                    "clearance_mm": 8.0,
                    "rim_height_mm": 22.0,
                    "wall_thickness_mm": 2.4,
                    "floor_thickness_mm": 2.6,
                    "inner_ribs_height_mm": 2.0,
                    "match_vase_texture": True,
                },
            }
        ),
    },
    {
        "id": "ampulheta_hibrida",
        "title_pt": "Ampulheta Ondas & Frisos",
        "title_en": "Hourglass Wave-Ribbed Hybrid",
        "category": "sculptural",
        "description_pt": "Curva ampulheta de duplo bojo combinando micro-frisos torcidos sobre ondas suaves.",
        "description_en": "Dual-belly hourglass profile layering fine twisted ribs over gentle harmonic waves.",
        "params": _make_preset_params(
            {
                "name": "Ampulheta Ondas & Frisos",
                "height_mm": 175.0,
                "base_diameter_mm": 88.0,
                "belly_diameter_mm": 116.0,
                "belly_height_ratio": 0.24,
                "waist_diameter_mm": 68.0,
                "waist_height_ratio": 0.52,
                "neck_diameter_mm": 84.0,
                "lip_flare_mm": 4.0,
                "use_custom_profile": True,
                "profile_points": [
                    [0.0, 44.0],
                    [0.24, 58.0],
                    [0.52, 34.0],
                    [0.80, 51.0],
                    [0.93, 42.0],
                    [1.0, 46.0],
                ],
                "bottom_fade_mm": 10.0,
                "top_fade_mm": 7.0,
                "global_twist_deg": 35.0,
                "textures": {
                    "ribbed": {
                        "enabled": True,
                        "depth_mm": 1.6,
                        "count": 44,
                        "duty_cycle": 0.55,
                        "sharpness": 0.40,
                        "twist_deg": 45.0,
                        "phase_deg": 0.0,
                    },
                    "waves": {
                        "enabled": True,
                        "depth_mm": 2.1,
                        "vertical_wavelength_mm": 32.0,
                        "angular_lobes": 5,
                        "interference_mix": 0.50,
                        "wave_skew": 0.0,
                        "phase_deg": 0.0,
                    },
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.4,
                "bottom_thickness_mm": 3.2,
            }
        ),
    },
    {
        "id": "cristal_lowpoly",
        "title_pt": "Cristal Facetado Low-Poly",
        "title_en": "Low-Poly Geometric Crystal",
        "category": "geometric",
        "description_pt": "Prisma heptagonal lapidado com facetas angulares que capturam reflexos de seda.",
        "description_en": "Gem-cut heptagonal crystal facets designed to showcase silk and dual-color filaments.",
        "params": _make_preset_params(
            {
                "name": "Cristal Facetado Low-Poly",
                "height_mm": 168.0,
                "base_diameter_mm": 74.0,
                "belly_diameter_mm": 114.0,
                "belly_height_ratio": 0.38,
                "waist_diameter_mm": 78.0,
                "waist_height_ratio": 0.74,
                "neck_diameter_mm": 68.0,
                "lip_flare_mm": 1.0,
                "polygon_sides": 7,
                "polygon_roundness": 0.08,
                "bottom_fade_mm": 8.0,
                "top_fade_mm": 6.0,
                "global_twist_deg": 90.0,
                "textures": {
                    "origami": {
                        "enabled": True,
                        "depth_mm": 2.5,
                        "cells_around": 7,
                        "cells_vertical": 5,
                        "crease_sharpness": 0.92,
                        "stagger": 0.50,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.2,
                "bottom_thickness_mm": 3.0,
                "auto_clamp_overhang": True,
                "max_safe_overhang_deg": 48.0,
            }
        ),
    },
    {
        "id": "zen_martelado",
        "title_pt": "Cerâmica Zen Martelada",
        "title_en": "Hammered Zen Ceramic",
        "category": "organic",
        "description_pt": "Vaso wabi-sabi de parede espessa com relevo martelado suave ideal para PLA fosco.",
        "description_en": "Thick-walled wabi-sabi vessel with soft hammered dimples tailored for matte filaments.",
        "params": _make_preset_params(
            {
                "name": "Cerâmica Zen Martelada",
                "height_mm": 138.0,
                "base_diameter_mm": 82.0,
                "belly_diameter_mm": 122.0,
                "belly_height_ratio": 0.36,
                "waist_diameter_mm": 92.0,
                "waist_height_ratio": 0.75,
                "neck_diameter_mm": 76.0,
                "lip_flare_mm": 1.5,
                "lip_bevel_mm": 1.5,
                "bottom_fade_mm": 10.0,
                "top_fade_mm": 8.0,
                "textures": {
                    "cellular": {
                        "enabled": True,
                        "depth_mm": 2.0,
                        "scale_angular": 12,
                        "scale_vertical_mm": 16.0,
                        "ridge_mode": False,
                        "octaves": 2,
                        "seed": 77,
                    },
                    "waves": {
                        "enabled": True,
                        "depth_mm": 0.9,
                        "vertical_wavelength_mm": 38.0,
                        "angular_lobes": 3,
                        "interference_mix": 0.70,
                        "wave_skew": 0.0,
                        "phase_deg": 30.0,
                    },
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 4.0,
                "bottom_thickness_mm": 4.4,
            }
        ),
    },
    {
        "id": "lanterna_plissada",
        "title_pt": "Lanterna Plissada",
        "title_en": "Pleated Paper Lantern",
        "category": "architectural",
        "description_pt": "Pregas sanfonadas agudas com anéis horizontais sutis inspiradas em lanternas chochin.",
        "description_en": "Sharp accordion pleats crossed by subtle horizontal rings inspired by chochin lanterns.",
        "params": _make_preset_params(
            {
                "name": "Lanterna Plissada",
                "height_mm": 155.0,
                "base_diameter_mm": 78.0,
                "belly_diameter_mm": 124.0,
                "belly_height_ratio": 0.48,
                "waist_diameter_mm": 102.0,
                "waist_height_ratio": 0.80,
                "neck_diameter_mm": 78.0,
                "lip_flare_mm": 2.0,
                "bottom_fade_mm": 9.0,
                "top_fade_mm": 7.0,
                "textures": {
                    "ribbed": {
                        "enabled": True,
                        "depth_mm": 3.2,
                        "count": 48,
                        "duty_cycle": 0.86,
                        "sharpness": 0.88,
                        "twist_deg": 18.0,
                        "phase_deg": 0.0,
                    },
                    "waves": {
                        "enabled": True,
                        "depth_mm": 1.1,
                        "vertical_wavelength_mm": 18.0,
                        "angular_lobes": 0,
                        "interference_mix": 0.0,
                        "wave_skew": 0.0,
                        "phase_deg": 0.0,
                    },
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 1.8,
                "bottom_thickness_mm": 2.8,
                "auto_clamp_overhang": True,
                "max_safe_overhang_deg": 48.0,
            }
        ),
    },
    {
        "id": "anfora_mediterranea",
        "title_pt": "Ânfora Mediterrânea",
        "title_en": "Mediterranean Amphora",
        "category": "classic",
        "description_pt": "Proporções greco-romanas esbeltas com pedestal suave, ombros largos e estrias finas.",
        "description_en": "Classical Greco-Roman proportions with a tapered foot, broad shoulder, and fine lathe ribs.",
        "params": _make_preset_params(
            {
                "name": "Ânfora Mediterrânea",
                "height_mm": 195.0,
                "base_diameter_mm": 72.0,
                "belly_diameter_mm": 120.0,
                "belly_height_ratio": 0.46,
                "waist_diameter_mm": 62.0,
                "waist_height_ratio": 0.74,
                "neck_diameter_mm": 60.0,
                "lip_flare_mm": 7.0,
                "use_custom_profile": True,
                "profile_points": [
                    [0.0, 36.0],
                    [0.12, 33.0],
                    [0.46, 60.0],
                    [0.74, 31.0],
                    [0.90, 30.0],
                    [0.96, 36.5],
                    [1.0, 40.0],
                ],
                "bottom_fade_mm": 28.0,
                "top_fade_mm": 24.0,
                "textures": {
                    "ribbed": {
                        "enabled": True,
                        "depth_mm": 1.2,
                        "count": 60,
                        "duty_cycle": 0.50,
                        "sharpness": 0.20,
                        "twist_deg": 0.0,
                        "phase_deg": 0.0,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 3.0,
                "bottom_thickness_mm": 3.8,
                "spiral_line_width_mm": 0.65,
                "spiral_bottom_layers": 5,
            }
        ),
    },
]


def _slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")
    return slug[:32] or "preset"


def _user_presets_path(storage_dir: str | Path) -> Path:
    return Path(storage_dir) / _USER_PRESETS_FILENAME


def _sanitize_user_preset_entry(entry: dict[str, Any]) -> dict[str, Any] | None:
    if not isinstance(entry, dict):
        return None
    raw_params = entry.get("params")
    if not isinstance(raw_params, dict):
        return None
    name = str(entry.get("name") or entry.get("title_pt") or raw_params.get("name") or "Meu Vaso").strip()[:80]
    if not name:
        name = "Meu Vaso"
    preset_id = str(entry.get("id") or "").strip() or f"user_{_slugify(name)}_{uuid.uuid4().hex[:6]}"
    norm_params = normalize_params(raw_params)
    norm_params["name"] = name
    now_iso = _dt.datetime.now(_dt.timezone.utc).isoformat()
    return {
        "id": preset_id,
        "name": name,
        "title_pt": str(entry.get("title_pt") or name),
        "title_en": str(entry.get("title_en") or name),
        "category": "user",
        "description_pt": str(entry.get("description_pt") or "Preset salvo pelo usuário"),
        "description_en": str(entry.get("description_en") or "User-saved custom preset"),
        "created_at": str(entry.get("created_at") or now_iso),
        "updated_at": str(entry.get("updated_at") or now_iso),
        "params": norm_params,
    }


def _write_user_presets_file(storage_dir: str | Path, presets: list[dict[str, Any]]) -> None:
    folder = Path(storage_dir)
    if not folder.exists():
        folder.mkdir(parents=True, exist_ok=True)
    target = folder / _USER_PRESETS_FILENAME
    payload = {"version": "1.0", "presets": presets}
    with open(target, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)


def load_user_presets(storage_dir: str | Path) -> list[dict[str, Any]]:
    """Load and validate user-saved presets from storage_dir/user_presets.json."""
    target = _user_presets_path(storage_dir)
    if not target.is_file():
        return []
    try:
        with open(target, "r", encoding="utf-8") as fh:
            raw = json.load(fh)
    except (OSError, json.JSONDecodeError, TypeError, ValueError):
        return []

    raw_list = raw.get("presets") if isinstance(raw, dict) else raw
    if not isinstance(raw_list, list):
        return []

    cleaned: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for item in raw_list:
        sanitized = _sanitize_user_preset_entry(item)
        if sanitized is not None and sanitized["id"] not in seen_ids:
            seen_ids.add(sanitized["id"])
            cleaned.append(sanitized)
    return cleaned


def save_user_preset(
    storage_dir: str | Path,
    name: str,
    params: dict[str, Any],
    preset_id: str | None = None,
) -> list[dict[str, Any]]:
    """Save or update a user preset in storage_dir and return the updated list."""
    existing = load_user_presets(storage_dir)
    clean_name = str(name or "").strip()[:80]
    if not clean_name:
        clean_name = str((params or {}).get("name") or "Meu Vaso").strip()[:80] or "Meu Vaso"

    norm_params = normalize_params(params if isinstance(params, dict) else {})
    norm_params["name"] = clean_name
    now_iso = _dt.datetime.now(_dt.timezone.utc).isoformat()

    target_id = str(preset_id).strip() if preset_id else ""
    updated = False
    if target_id:
        for idx, item in enumerate(existing):
            if item.get("id") == target_id:
                existing[idx] = {
                    **item,
                    "id": target_id,
                    "name": clean_name,
                    "title_pt": clean_name,
                    "title_en": clean_name,
                    "updated_at": now_iso,
                    "params": norm_params,
                }
                updated = True
                break

    if not updated:
        if not target_id:
            target_id = f"user_{_slugify(clean_name)}_{uuid.uuid4().hex[:8]}"
        existing.append(
            {
                "id": target_id,
                "name": clean_name,
                "title_pt": clean_name,
                "title_en": clean_name,
                "category": "user",
                "description_pt": "Preset salvo pelo usuário",
                "description_en": "User-saved custom preset",
                "created_at": now_iso,
                "updated_at": now_iso,
                "params": norm_params,
            }
        )

    _write_user_presets_file(storage_dir, existing)
    return existing


def delete_user_preset(storage_dir: str | Path, preset_id: str) -> list[dict[str, Any]]:
    """Delete a user preset by preset_id and return the remaining presets list."""
    target_id = str(preset_id or "").strip()
    existing = load_user_presets(storage_dir)
    remaining = [item for item in existing if item.get("id") != target_id]
    if len(remaining) != len(existing) or _user_presets_path(storage_dir).is_file():
        _write_user_presets_file(storage_dir, remaining)
    return remaining


def generate_random_printable_params(
    seed: int | None = None,
    current_params: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Generate a cohesive, aesthetically balanced, FDM-printable random vase parameter dict."""
    actual_seed = int(seed) if seed is not None else random.SystemRandom().randint(1, 99999)
    rng = random.Random(actual_seed)

    base_state = normalize_params(current_params) if isinstance(current_params, dict) else copy.deepcopy(DEFAULT_PARAMS)
    params = copy.deepcopy(DEFAULT_PARAMS)
    params["print_mode"] = "shelled_hollow"
    params["stl_always_open_hollow"] = True

    rand_wall_mm = round(rng.uniform(1.8, 4.0), 1)
    rand_bottom_mm = round(max(2.6, rand_wall_mm + rng.uniform(0.6, 1.2)), 1)
    params["wall_thickness_mm"] = rand_wall_mm
    params["bottom_thickness_mm"] = rand_bottom_mm

    # Preserve print mode, slicer settings, and drainage/saucer preferences if current_params was supplied
    if isinstance(current_params, dict):
        for keep_key in (
            "print_mode",
            "stl_always_open_hollow",
            "auto_configure_slicer",
            "spiral_line_width_mm",
            "spiral_bottom_layers",
            "spiral_smooth",
            "wall_thickness_mm",
            "bottom_thickness_mm",
            "drainage",
            "saucer",
            "resolution_angular",
            "resolution_vertical",
        ):
            params[keep_key] = copy.deepcopy(base_state[keep_key])

    params["use_custom_profile"] = False
    height_mm = round(rng.uniform(115.0, 215.0), 1)
    min_stable_base = max(64.0, round(0.40 * height_mm, 1))
    base_diam = round(rng.uniform(min_stable_base, min(126.0, min_stable_base + 38.0)), 1)
    base_r = 0.5 * base_diam

    belly_ratio = round(rng.uniform(0.26, 0.48), 2)
    waist_ratio = round(rng.uniform(belly_ratio + 0.22, 0.82), 2)

    # Bound radial slope dR/dz <= tan(30 deg) (~0.577) so base curve + texture stays well below 45 deg overhang
    max_slope = 0.52
    dz_belly = belly_ratio * height_mm
    max_delta_belly = min(28.0, dz_belly * max_slope)
    belly_r = max(28.0, min(88.0, base_r + rng.uniform(-0.35 * max_delta_belly, max_delta_belly)))

    dz_waist = (waist_ratio - belly_ratio) * height_mm
    max_delta_waist = min(26.0, dz_waist * max_slope)
    waist_r = max(24.0, min(82.0, belly_r + rng.uniform(-max_delta_waist, 0.40 * max_delta_waist)))

    dz_neck = (0.92 - waist_ratio) * height_mm
    max_delta_neck = min(18.0, dz_neck * max_slope)
    neck_r = max(24.0, min(84.0, waist_r + rng.uniform(-0.45 * max_delta_neck, max_delta_neck)))

    dz_lip = 0.08 * height_mm
    max_lip_flare = min(7.0, dz_lip * 0.46)
    lip_flare = round(rng.uniform(-1.5, max_lip_flare), 1)

    params["height_mm"] = height_mm
    params["base_diameter_mm"] = round(base_r * 2.0, 1)
    params["belly_diameter_mm"] = round(belly_r * 2.0, 1)
    params["belly_height_ratio"] = belly_ratio
    params["waist_diameter_mm"] = round(waist_r * 2.0, 1)
    params["waist_height_ratio"] = waist_ratio
    params["neck_diameter_mm"] = round(neck_r * 2.0, 1)
    params["lip_flare_mm"] = lip_flare
    params["lip_bevel_mm"] = round(rng.uniform(0.6, 1.8), 1)

    # Sync profile_points with the generated 5-knot silhouette for seamless switching to custom curve editor
    params["profile_points"] = [
        [0.0, round(base_r, 2)],
        [belly_ratio, round(belly_r, 2)],
        [waist_ratio, round(waist_r, 2)],
        [0.92, round(neck_r, 2)],
        [1.0, round(max(12.0, neck_r + lip_flare), 2)],
    ]

    poly_choices = [0, 0, 0, 0, 5, 6, 7, 8, 9, 10, 12]
    poly_sides = rng.choice(poly_choices)
    params["polygon_sides"] = poly_sides
    params["polygon_roundness"] = round(rng.uniform(0.18, 0.72), 2)
    params["bottom_fade_mm"] = round(rng.uniform(8.0, 16.0), 1)
    params["top_fade_mm"] = round(rng.uniform(6.0, 13.0), 1)
    params["global_twist_deg"] = round(rng.choice([-1, 1]) * rng.choice([0.0, 30.0, 60.0, 90.0, 135.0, 180.0, 240.0]), 1)
    params["auto_clamp_overhang"] = True
    params["max_safe_overhang_deg"] = 46.0

    for t_cfg in params["textures"].values():
        t_cfg["enabled"] = False

    archetypes = [
        ("Ondas Harmônicas", ["waves"]),
        ("Coluna Canelada", ["ribbed"]),
        ("Cristal Origami", ["origami"]),
        ("Coral Orgânico", ["cellular"]),
        ("Trama Ondas & Frisos", ["waves", "ribbed"]),
        ("Cerâmica Texturizada", ["cellular", "waves"]),
    ]
    archetype_label, active_layers = rng.choice(archetypes)
    depth_scale = 0.72 if len(active_layers) > 1 else 1.0

    if "ribbed" in active_layers:
        rib = params["textures"]["ribbed"]
        rib["enabled"] = True
        rib["depth_mm"] = round(rng.uniform(1.5, 3.2) * depth_scale, 2)
        rib["count"] = rng.choice([14, 18, 24, 30, 36, 42, 48, 56])
        rib["duty_cycle"] = round(rng.uniform(0.38, 0.78), 2)
        rib["sharpness"] = round(rng.uniform(0.15, 0.75), 2)
        rib["twist_deg"] = round(rng.choice([-180.0, -90.0, -45.0, 0.0, 0.0, 45.0, 90.0, 180.0]), 1)
        rib["phase_deg"] = round(rng.uniform(0.0, 180.0), 1)

    if "waves" in active_layers:
        wav = params["textures"]["waves"]
        wav["enabled"] = True
        wav["depth_mm"] = round(rng.uniform(1.6, 3.3) * depth_scale, 2)
        wav["vertical_wavelength_mm"] = round(rng.uniform(18.0, 44.0), 1)
        wav["angular_lobes"] = rng.choice([0, 3, 4, 5, 6, 7, 8, 10])
        wav["interference_mix"] = round(rng.uniform(0.0, 0.75), 2)
        wav["wave_skew"] = round(rng.uniform(-0.35, 0.35), 2)
        wav["phase_deg"] = round(rng.uniform(0.0, 360.0), 1)

    if "origami" in active_layers:
        ori = params["textures"]["origami"]
        ori["enabled"] = True
        ori["depth_mm"] = round(rng.uniform(2.0, 3.4) * depth_scale, 2)
        ori["cells_around"] = poly_sides if poly_sides >= 5 else rng.choice([8, 10, 12, 14, 16])
        ori["cells_vertical"] = rng.randint(5, 11)
        ori["crease_sharpness"] = round(rng.uniform(0.55, 0.90), 2)
        ori["stagger"] = rng.choice([0.0, 0.5, 0.5, 0.5])

    if "cellular" in active_layers:
        cel = params["textures"]["cellular"]
        cel["enabled"] = True
        cel["depth_mm"] = round(rng.uniform(1.6, 2.9) * depth_scale, 2)
        cel["scale_angular"] = rng.randint(6, 15)
        cel["scale_vertical_mm"] = round(rng.uniform(15.0, 30.0), 1)
        cel["ridge_mode"] = rng.choice([True, False])
        cel["octaves"] = rng.choice([2, 3])
        cel["seed"] = rng.randint(1, 99999)

    params["name"] = f"{archetype_label} #{actual_seed % 10000:04d}"
    return normalize_params(params)

# ===========================================================================
# MODULE: vase_studio.studio_ui
# ===========================================================================

"""Self-contained offline HTML5 + CSS3 + WebGL2 + 2D Curve Studio UI for Orca Vase Studio.

Generates the interactive 3D & 2D parametric vase design studio for both:
- `mode="page"`: Wide 3-column studio tab inside OrcaSlicer (`PagesPluginCapabilityBase`)
- `mode="dock"`: Compact tabbed side-docked panel beside OrcaSlicer's 3D Plater (`UiDockPanel`)

Zero external CDN scripts, stylesheets, or web fonts are referenced so WebView2 runs 100% offline
without network permission prompts.
"""

pass  # [bundled] hoisted __future__ import

import copy
import json
from typing import Any
pass  # [bundled] resolved intra-package import

if "DEFAULT_PARAMS" not in globals():
    try:
        pass  # [bundled] resolved intra-package import
    except Exception:
        DEFAULT_PARAMS = None  # type: ignore[assignment]

if "BUILTIN_PRESETS" not in globals():
    try:
        pass  # [bundled] resolved intra-package import
    except Exception:
        BUILTIN_PRESETS = None  # type: ignore[assignment]

__all__ = ["get_studio_html"]


def _studio_ui_safe_json(payload: dict[str, Any]) -> str:
    """Serialize payload into script-safe JSON (escaping `</` and line separators)."""
    raw = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    return (
        raw.replace("</", "<\\/")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


_STUDIO_UI_HTML_TEMPLATE = __import__('zlib').decompress(__import__('base64').b85decode('c-rK>Yi}e;av=D<e}#9Brjc32Oy+}Ru~=2?W09<C&ajHLB)fWgYD!dOW@KhGGb3^$BKfM}LC^uZT|l}$NWzV<5N<Tu69fqopgZlZfH~|gF#IR|VR0Yz6VA;15$+xykx5on&+OeuUCi)@xw*NyxtY1S`{Pe{4z`cKeznU+>14e5$z%M(#$GslQaL%<d%1VKx3zz=zxDF@$w`Ivz0|9xBY)!SxyN7ZzSxCqtnGV!_%rcSkM%}gocQUJ$}An!*DGvUW`rKrKMVZxX%wdw){DZ_524_B&`(EC`u<ta^Xv4n#DXwL18-bUdfwQ7(rPq0pfpIw{^mj4^Vn-I@!3&2>j%-}WuE@Y<0QSrzZ-EBrAwc@(Gl-^@oD8Pd-n-r^?G+$_omYg_Py3xYrWNbBon7z=#MekZ#Ua(D!J#yeMoJuw%0pNBegz?&iokjdYxv+Q+Yu+ouvrqLF-}5SIM&X^)$lP+nx3U4WP>HMpU=mT4}AT+|dkhh=*OT+Fn^=?FUP&(^+E8#`;=Kl!@ZLAJ>yv7l;A%JFU*zO4H0s<0u?L-b!m_eN}WY^)J%;#0x@5_x(Y8V5HAdAN&5$^E%zOmeCI;ki6zUc(DF}Cr2<Wb+6ZhL4}-V(_4SImdjBDYc{(BZ#AEvM1xfHv$@28dhpNMDt5HBTFV#b9dlP$Sr-+O)JtbcJvya!d+VzmBmLZqvG0RHx6^DIIlVYYDQ6YNUgV6tesnI-Y_j#~1#7RsKN11)|Ba5sHum}ffJ%T|YtsuOZ32{iXr+x|cv@|lIEauWUYKmKGcT@+zGLbVs~q{m$Y)>fRhAgC^VqK^mr3eRme|vA5T3s9dPnsAjEWydz*f-``?5O=)7cV3sP)8;gF#JeYZ8Ug2CHm)F!TC>$F`%s5Ae66Fp0)qf~`J#0cGlk{%|(-V#vcP$<*rsn_quoPP%b09HseLr*oM$>jv~cd)5tB2M-3Gd)E1$4`Y*?brv9N*7f`Tir*`mb-f4uR=?+(b*sQs*+0$3!)C$6>#z2E{)&6zb=P~H-XK5mTD^9=-E~a7)z!7;gJy2xJ?O5lIi?pe`1->K-Li@I;Ne<#?!@bWfN8Z!!nE3pOgyc^%Bo}HwYm@em9A^z^&hUc-4n0>u+wa>E->+0G%QPOh2~xhM+SKD9x+}wx~M0?Re<yt!vRSMbmGNBq&~Gh_4<7()1<n%A}&Gs{v`pSbqQu>v-y22Jo1sVvu~vBU>u!quu%Z~6=GV~>zxkcXcqS6<mD59Xw!?vQ7qFHBTyF2!+|#m#+R~y5(8NQ=#h_-qOr<l1<ZKAuFz@_`^^$$J%8-?AT5kSz7U=J-P0fyFek85j;PySh%0UY%W9tpu(2UaCcQWskGo#1Q$olx*&=;jyDHVw7zn{fLZb+zh9EU!;HAQfquHdJt0+jR&nu#eNa11><m$r`j1ce!O^5>U8mDts>dw+M3Q;iu5d*@Lh)R`>;R?bLNYvCCB`sBqyGjAjjfAuqU~qptCXoFgnT|aGHyHawW&8^hKZZ7g2pATi%qGNSrF;p%m+!GJKs$quK85kSx2#$l@l<DXzy`yx9>CH8ghU$nF(!XAOVVI)Sr?ky1|z9o@A~Pv&sl!xO|fmx8frp4fLSV+H0PwC1wbD}5XET(Vy*=>VciM()~J)DttrYRqZrmZF^{ic8R+{L8?4PIa-$2J)~{ou(_3|yIwO|nNf6crshhG{Ko9=Uo28N7&Nv!I`aEe{6GeVo?D`;29-Ps@tV1jUNL5>%)xJMmlByGHet$_ya~f}=$DPMA%MvWAt)h7%lT0OnjItQUmgKQZ3F`=1EXYHedU9JXH_4wtLz|)=N9VU6S0S$qw6f`ZE(YrXUzT)%+ff47PgCSYm;-#-Xb2WRA3>9p?xWN_kG&~x>I`HnN13EZkz^Bkj5Z$@nFtm?@nTB%tQixs!^bPPmS{<m0&AQCCCinRKx=|7B-jH!f&wY3O&WZHl&}f0F^GCI&J)orMYhjYD;+|iaBfV2HE}Sefh|FUkQT;;Swf={Di^JmbGANwSR&0(L%rqTImnCZUv9N;m2eoUGZ%7}z=WxS;yArnVykOs=e1%P)>JYK(3r&u;xUZ^NtyD|T+%2YQ|!Uk$3|as%Li5vsa8s5uG5z5Q#J-32$wTH)v0fTD4qyyWbCE>*HxgggR2PUomp$uy^7?u#$2;FOQ>19t~S{1HL>Elv{0f&mH{e8FinD_gpF=B|8oc@Q@_XOa(>k)XmBp~JCtEGI&;&b*-&EL#OX5Z6`*v>(JWaujd|+U%5$B~*=M!PEUAxuv~*f|sjB!Em)G@#`5;cQ*G|*BfD)ww)u_|JIv@~>AZfEGj=*~JtDUtbC@L0n^rKW)iyoL-(F3QLUFAw`sd}!_%^qEBo~yZak5r1}_IiRCM;GXB8s0@9l(3NAqFRPlaT#hl>El}DZ=o@iE?)BtR7*fOxqsezVyqo2xSCii45sPa-ds;gG%OquzQSyTQCi)Af$_Ry5G2K#mbHqw7A4!#6z%YJ#MMywvO<+*1+Md;2AN)>2D#GK$p*0N-WbHTu*k7$JpjI;Y6gQmQ0goc;S(d*=^}d~F9W1$fsUliv@nTd*zb9x;aW#!u|ZiFKQUm0r33jz5SFAuZ_<1h02Qk}x}DZCSI`#;Yy+=yIW3FchU-lru8~8h!3&t|?5ij~rCG+F#~?^F@4>msd6!wkQpJ%%-CSUY0D^=Z`~`tBnc}>ta~lt2S*L?mBvc2*rrKE{)wMN%QSPj*6lpg&iU5H75AI@98ko*;O}Lt;)^VNIRoYmr_HzWVs7<By>T21aQ=3=kPOZ74Ad#;FX{5HV1c+Q+Zb3ZF(Zl&=C+eND7g675FTJy1=wStR>~#}X<>Z3Z5!ZennjQLV0wrt2P<^OaPqCmee#-v)!2Tk`x)T;3b!Me_p_eGu<%+LSTEPQY62_fYX-l3Kx=L?tEIQSB$HI(&NM+GA5`DRbrHHS|#Jf6CG_$TmZ79<>EPxHoO8YI6%ta`cdnaIaY(p;-_8B|!g&wMjQlvn+g7N`9L6d&%gG~K(sc&!v3Y6@R;YnUITCsd|wzBDR+z|t6`q*qb^<j7t-|fI#m3nJ26W`6rNceZX{xFY!vv`(fqm;?2g&k4ONpfe-w>mJF;a|mm;-^WbH%uv^J_yE0^Fo&`u^sC38%%l!GU<$z6aadoU}|c?9jOJ|E`ilz0v8eU{Y<FLds`-{b0YZK=-k2*u(p_&)T!r*QAz5klbHiDM_Y^isqdxL_L9`tnp|6}+1^xiQ>m?w=Bla5IkXX}J+(7O4l$0BlG8}8N3jn$0gY}wEgx7G_FBd|AK$>vbeCItTUT=4)|JFwxKVc$4je_b(tXZ5o4{HF2CL3lg|&7Tkysi7WShalgVbr7E~L(yTZ8)mdtw?I6w3Clct_AEtem%ts%0g+EN<87tvtROX27L3Vh<bZg{z;ES|1pVzCTt<bvCiV7yvnw(!{2aoeoD#hz9W`_nj<HV#_^~S4`3FGB2_ypY=BX59ZifUXW`cDn&ZC!|j`&>>q$FEjpG?bsKHhdXRW$eqF$n@g6yoO!rb2pe%(sjh<;0Q4-3|zL$*r664syr4dd2(4{n3MYF9{%O2Jz>m7Gpi}t5(vGuy*R#Su)%ax}ie>g!>_PIfQbRML=5jPq9VOb!<Z)7vMtr^j3)kZ|itmRc(qs{I3+7tIXw}%TYU(vVQX=rXQTYHCX&td?w?S*Gv!k$JKG|oLtto!{Sjbc)VOH`kaud-wu<aEJ(k7L{8T`(B4I|hrnBuuH@Zkjs<y*Nsekr(hGh-ST!*t(JYLDm$thqyo^c{%mowx=;!*KZTIq=eg?pe2`qQq0C#pL-F&s>fh%M>9wC+5G)cS6jET0}IfY6Q9AWje;=E+rKhwCg1;lFi{5O5zrHswr!{xM`P|l>80^_jwxB}!RRR49HGF#eOw0yHZu0Q!cA?8{?2^8%Me<t&87zR%o}GS;#PK$NrG@T(benKGRFS^Ys!jcgrWCeMi6Nh4e5Nh4g_e;@#9=)eSZJoBZ4#wgS5!EQ^eVZUeb~-HKOgC^l}RG4%VQdUwPZ0MiV{--f1zs-W1GmDAd!CcBK`F-__d&H|2tEb0l-PHRg0k3(%!+&C<JTH#?R|(D@M21(MU-iqo|SNi!a@#rFboXF^sCyMGva-LlY*R&r<RX@-F2{iMTG)fPWU!^P@xG#rji6_bA6I;e6%fvEh(DK%W@tu5l%5y2I<M$uWZ#(KSIAIEAkvlFuYcMWb+2Wr&M!r9#xYY>7NQfy}|7Po%O*opNdhvCLX*N0)3{#r3AmCB<+#O3U<DY_!#T?eVs_DRucFFLKXiBibyW*789+USk^-YHl^_gQ`n=7;Xz2BbkWR~*NWs;xB{ABfWjg!v4LZ}oaW1l;o6_byRQq5U45P9W~*?C{u1<Oj0PoGzL9p}7*@h971TDhuze(aiQQKE{TSahhPE@LQLMJ=Z-G-G!Z!Sc~?f?x=b_D7Hm&5!tdm;MucS1ph3gWn}7O;jGJz`US9KU(!WyF(2mlP>b@z((0^K&SRv;Zk>;v9nZF?*;KC4ix{Y)&g9XP{v+C<rSV~%9rjwB2c+q%4hKS8x7mJJ^eDreFch59px&#Hs9q5FV7c~El(MYTRsm4fDMvjv$~xkx#YefV`QcbM<>#Dx%Uk*`quthduC-S5fNZ@~7Z`>kbT);e<6w#sC_`-i;(Ke<g`lYWXF%&DLtdRIT9w@L6?%k@M?vp2^pk}Bs~P-Kd!C=MSAHB!eB`Gu(Bwr%I)@t4MR~W~PZbv|XA7Ts1Xyi{x_zE2>z1+A$&4*~_5KdGKyT^0Xn)jr7DdMegIN~XCR=2~O>g-lM7<OokhqP@$BAC)PV-`BGoKMSQ;HlzD+@ZS7T~0h;n#5o9~8`|+YIM|8xN%eW)XI7z{az21glv%%$C0c?qB6<EXd$Ais<mH3U@5ou#@Y%h-EAdGBV}eBByAwlP|C?^r|S(S)H|4+oYLm^13DbWPtr}>?KLD5<Z&s)r9TG(NqMg;NmcgtLp;r2aUnfT?S%@E<52~Q;2IPjY~0~E2}>AzR#-r5Miq<;KrenQz!G`JR0<mzrj&L!w;~Nbe98TBHl^T=EJQ?8O-k@!brANzlgod+aCKX^WN%ki#oE<`RT!6eb8*OR_88<99-w1QP{Z;LJO~3Bbf#<DD@ZuUGI8f=ojp>m&jMC(3$eJP%y3u`Q<!Q<Tya*W^L<+iH<31+mGxJ_D;znw!p#7B7OYYML{sslAtTXL+^a}*9{tPDX|0e>#m3pELd|!m8<{<bXI^BR@B8YMXPry0?ufaHbQT=Ip~#a<>+}6wK?kMB^frqy0*}At=l55HMTcP7i`e2AIO6fMeW}<rcVMY!WC(plyb~(M?i)9RD#xtEQYF3A^i^GE1I`j`3qyoicK`D$BQhA`C9KCwjlu)?B*7e;MS*~WhgaJ%<Bf@AiZQ?e7Pg_aZp;c!$S)w<JR<&hsQg%G4oKn_u#g>>T3lv4w2>l(ht9}G@l3Wcp6}lxD4!=5dZ4(2_tU*LFpdrypsSA_*TE&Od~pVF9@J>w43nHI={GUy)b$)I;}YY&sl3)4<3rW%yzR7wpa%p&@uS11bP;C*>2B^yOhMgb?AC)5aWNkRhex|BE*TG#zF6PK_%CE)%xizVrylPi(dci_Mttk#$9f2kzK|S1CCAZ9!X<H`af(J1^VkP(qu0V2r?G4wbH2GIlS8H)N<Ns+gh`29j<IiF*>j~Q;Q2M=c$o8gZo}O@upCA=!bo`nXtf>HV!GXNQCZP@2t7D5qE3nDtwn0swd~3j0F&D(?fG7`k|8t+SW>C1`5zYZ@*vn#y;+U+|ArtZR_f)*x+_=57$?PA!%x&ZO+1KGkt-O8_q$kP8L4$uvsg(pKH#YRmvx0nyYld(V8?@ji$s6j@dfC>N3dW*`31s7%alSx0NR3Gyxt2X<qMbYn#K19`17A?zy&FD;6z!L35F{M`aPc<d)ZD*c2#;`gdd7X)DF@kd((Q66)+(6ybgq>Xv-(4%Qk<dFMJV`az>%Z@b<+D7}&e)}T0YZCx6jP!rL(+O2qq7V+oa{^~ySehrs*$u`|`(|4uF+tjXotYatoTr@eAJI&=qV7ZH1uCoCuzOX_$-pO3S?bT|l(R@%dtH00fD;z@66)dZ(I^E7ac}b^#!FSN1e$IqhOygAI(hLnA`D5JLhORgc2hTS`7Iab+Xg#*Qo4-^h$NQY|@V{oR10TXyX6tTEEm+Y@QuZ<ewhVgwh6xI>!eo7E&sOq5aN+k2$J5&FR&t$(@T>xln=k?fi=qaMpqJL#{Jo4xzjpUK1q&P(h1WODzw&Y3{**cO1x?U&v!;GKF*J#X4<A~->W9s<a}lVQ4WyweD1x_cF<i}B9;hG3QStSIIsF@W?#T!IA2iFh4_>_5+CFASdpo=JorCQkvKI$CyR7<q<P1h9)sqTdGg0|H2AGCkjKW67?<DN;6ZQ~q`>P?W4~ZMjB#e-HW8-1nAh%Rl%Dza|Qn2w3<${{7dr{@$t-|7qDmyPEx`o|djFlbwC1zf|Wt?DISuHwte9OCO%22Vred_FM+i_Xk1I>Rdj(8LS)@}ddkzH)V>beYleJ|ox_4F+T$JITOxVf8r=0bJ*&9ze~dG}4p2o>C7B-u}}PO}t-yi01Sw1j<MRJPz0-~TkHQ4Z3f_vfcD@91zGb%7zuN|q9;q`r#DbOYcilG;xyup~|WJZTn0rwH2jC`3zKj&UntW<wM(J{X1>JdR@$j7QN7UDr!@gaDuD><FUp!{C*_Q$%+R-jaMNkFQVk>G3{jYVhP32O*aQOLqk^gnxXLpzp~jfXIjHrUb?j^usfM98GV*A$o1u--6!#4-+4siK*)P94RPNK7TQ{!|`^F1)a-yp+(hRZ)TSTw%4@F0-M4^aSg~lUKZ~`Jzf?sR8b7LMu6-!E7Zc&TUWM3fSUc_jP)>v4AQjc8X$|Y$Dh{g?D*gn`(k%%XZMiR>y#>9STJkxM5+cwG^pAu1tQm#kFN_<7%5p#D)u{Asvgu#&W2n|cv5MtRfM|2f1_gaG`e_FX=2FA3jBWst?u!Y3XVvHVXV+8fCn2Gw}7`%MV6^`0khp`t0Z)G^t|bl3K=a%@;6``$@C04KyT`$Bi4UXd9ltqqxEsU)mUXKjn!To{^EZf_-|GGe%M&8Hy+^6db`nKD|INE)K?lEtW{sFuk`Az`U-2-c^N3a4^Xcv%kCD}03_bx--G`E!a93^3GlboVokjgu+Q004aG8yMe(@sXASfL$Q6-q6_|toW)B^pDvn3au&7a&Ys&$23Vzj<7G06>EWH}|hE5UUjIN+m9{b@C2Xnm%OyP}Z$Wme7OV~j?^g=MPlM3_Vz~fupPbxcp5)4E3lG-o`rPIdv;LoNIj=Ct2sPJrsuvLU}`Sv*Y=?t%pj6IeFVK0ut;0jd2V1g@65<xPa!|+%?Vo0>3anMsUEJtJQI_k=%O;cXdMz+og=D?BX<i|4y!5Ef&&gOF;l<J^|$4_4IT*q*`LDPNfZrD6)^Vk23_blA}od2`hWRnSlv}R*vGRaY3F^b^j-vw<_4si`XR08}K&!CIn{^9>^0)M>BM_-6S&Nex*Xx`slaWNLU<Uqhg3L(_$<yFawjlP5uth$}X<NH6ZRhV@D0bc*f#3T<q_U8dV^cC>0P2m4L7dXuMXaZ(Nt_Ae7*lfJ{FTeO-{xA0+(aIIH)<c4DlFVWlm;@+)gui?rW_EqzmyLm|=b*~X>pB*Jp8hHaOoT2YFnn54gfi>kaIv^VD4F`uB3GF-$iS8}WzaqVnt4NCwXYI3A4gMCV}&T20#>iUexD6zH-DErUgo)WDL<@i?uNs0kc<k80Nd>X)o%XJXk1h#fX4Pxd_F6TipmT?C_RJWzWEz3D8#1^9og|`Y0@ji=NqrG`QLv2*Z=J={{H{@yZ=2aw9Ls{G?Wx)SU!|HUVO@y**=9LZhrgc|HU~)@duxkG+jyg$sAe7TThRq0u*{`8Y}zQ98JEoscTWCS|m`n>XNn29slx8(o99u*&mWmgyQxriYK1cjbi9JSf%INkX6PeKmF?^cY@EgY#TUF-Q44A+s(g^?g*P(V|nO2eN!A&(}6!;hT+Oa^u^ZROV+7xAMAhm;wAg);P8h>ueP>#<<O!t+0ty4>MlnS!R+roJ7yfn277h5d$fCe#O|}Bz5Oo^zT7=N-h~gm1nJAe*Sl<YXYcqxs?Q`p_}-*wC%fre+DJ}CIlC2G7oLcWx|Gx#kNx<PPHC&w6d0T^y8U0V`iXhwny)u5ufsJ;SUN~{o2@ZI(A{i=p5wkb7*>6sE&&@yNnRsxOmcD5J-ZLhy{bsDE5)pM!0S=w^AcN6mE5udpaqtdO&CaTeCEZr<j?7W263&6-7@-G=~h=wZC5XBXji$r;0o2=HL!cYuI%}vXbjTqN#$iU@llK9wHu9wq2;>h4bpQE#FJ8j^G%r?$>rTrISNOouw>tXti}zyx<+VSyjyX1Nfg)b*EM8q&ja((L%m$X7ZOh}ZSy$lM~MsHvIca>5jQz<&}BN<L&KZDf?w~~%+QZ`j9spwEC;mlXmazn`1}1D1Li`-IM<X+-`w_kBY%4HAKt4KeB?9N1SM|1@Mp<gn20;?EEW=pn^t9AaaWS|DcP;cH_1L@d)Q+UdaZ7~+ocQcN<?tx-uzCbu-5D*_F{&YzJ5kXdw{)D5@&`|G`{3lWmk-*c+%!}5clxmWQT!gQPS*_y85wFE|R8kG!S<IX-k*5j?tLWyuauOJCWr#`88{E_|a&Ju6DB<%D2FaZE_Os2WPQQge>IEqLH;PMzpCRZU`U_(yk?}NM~55+049QU=brf^CA|YT%+23gI1&Z=sPaRtC(=iyv-kDbPU?#H-F9^tToU&ckx%A`eMvr&9}xtx2yC8e$86oU5if|$&nJAz`p&%KjDmDz!N!9QYc%pO8_m3jBHI96F43jXKuxyX@e+<5;lcSz@HHPL1J=7Gv;By66N>!C4qjzysj5qM2!NTB4tESF`M#YmPraqcQtKHS=-2B7a4aQanrTpU?J)iZv>qg$ag1`NluEILfDHv5eeQ8Ji16C!6&Of08TEfx*)7iWJ5*BIV<|(@#TBe6y%68lxN|p=U_aicWRW^yi=p0-#fiio8w@5G5~4s7Y=#>ALO8P{WE`D$~s0BT!n@a=<D#A+_Db&>oM}qQE!pe|An87*kQJ>ILFS)b|AmgMP6%mlOuccH(+o>G4{e6kG#SKx{QPw&=d4ajd88GT{T!`(xB&!ixjQg2ReRe>Pzn_4#D>B%j4ZcWqI%6*Vgv&9$49(9ro4k)93qb_Ihvkt5*ky$AuQR9s-lu+S(GUZt=-4qk6I24L*ADPc+Usj;8f}-28murD*<+LF>W`DYAQCGd9wB!MdKp@S0{$NcdTw2*4Gss`N|ho+*id$$pk&Z~`jrxR2`Msj2aR1}-vTA@zZyb`$>T(H4br+7-iw)<Ip4($vdA*0MIY{rKjuCcrQ3Sfnlj9H6A2k^x2&%MwEP6wOb*)1D8OipQSfHJcud$pXN85gw~M>Bdob<>!F&+{)%t%7$_6f+o0|^rAD+hZca22mW(FDRJ{(e(`62&kjA18$V*p>=g*zzR#-16cKpyt6tELY6~<VPOjwIkm;K*yeYY5@P3pLOmbHJ^*=fQ+y2<R0(Zu*FVH!W%x?W|0|Sk-X-QA>>Y1ZGF$)vBO}iOY4x0MYe+#3O!c0cRbb&S$0n3|E^n}j*wIb$1Eu4e0GY>qK+5Gm8elCUi0&o*=hC7FIAd6Cf_aFaf_6qfga1`AFK1i5L-6~McSjruRN7#+?x+kzWr+y!IE_$Hg(#%<;{b>;9n-$Lgtr-{+hjg<a(Cruhl-tcQR(g`wUqpxpJEHJF{#JpyJ!mf+MC>U&7-flUlEk@)!fff!2OG-kdn&GdNl~5`<@*^hG=KE_#XFg14Zej7$VVWCC})FBkYyO^#caCF8l4x<&_HV(9q%)+c~gG~vV`@P+0zKb;#L<{Y|q|T%Mt5fme#>s?)rT;Mkj~}yL3^<J~owEc6NrnJNWIt`^(~fXSI2scY=u@CO7{P>?Hr92O?y`B6f!6gO5s3w!i*q4yMIhcn}G=M{EQaZ0>6(mU3n%q@T#zn_Fnec`>{BOVlL21sD<427a1pA4zMRnE#CNe$umhczj+XxQE)Y)KFA}tv*Gvuv-@s>ig9C0e448fNtH+`X?gDBg3@s_5HFvf9oW5MQ>L>e~#YcgCFL%^-WdMLYzDH3iRykTymMBt)G6b*uBLY$-oSXA{bq<E-$lZxMyGPO5@?l<8htWb+mO>*=#pf09vQfc6v_S%J+xs+62V$=wuY(Xx{uebSjQWEX?m1)vQxZcgFzS`s#0}Tm4{?7!sm7nbhX@iK@AK(`v2V{G9)@*8J`}6bS_bW{1?<UflfhVt$uY#RBeIZ>;?KAHVzl@WVQl&1b>b!^eVf^-3EHOefzEab{=!$CY(9{O<d590$0Y9tSsng*J1+R;SU86sr_4T66VuZXa9%5n-c#Ee@?$v=AiiEPGzIZ$1uWQR5`L(&)4kUEgaC`fI&5+P}eOZe@V#Cm<DY5!}6iKcN&O1uMg?S{@A6d!6-?mIJO*Y<p+48nMs3$@GySrWaXOXoO6PeH=nId+Vzm-kop%&Hu5o>YRmlpi&pN2ng)T>bJlDr>h?faHlT;e>O}Xx!@MkQ#+<(aJ@?0w7f&4*_cYwwudeV5d^_rfwEBIO%dmHDtVpHX&gcECzT+HDw}&ri7irGcMwO`9snet@YKy`7>4ZM1#B8kb3id|6Ewy<;mOY%<zR~BP2BgqQ}+W$=P{;iH~i_$>&N+60EZU*l#pOMGcd+PL=~7}7zB!&tl|Ns>TBU&1V)Gk!PsYCv-@Dl#laQO8k5H$87PL9{kT@bAmU)w9JN@#X|2L=Q|3uU?5`McU;^FkSxR=KDI4sd3we6Wbe-sDx*YqQ=+ywr`4WuVzxV^T4K^xRtCAMgSAGn{U|-jqTarZxToobUYWWK7(m(mH?3tGao=))}L-QCB;IY;3gTSHt031wY$p$kVhTcs>6ck3<8!^%#<Il(7v56;@CWXR0skCrEG)es_{8UlkO*6b(t-Ryz*wK=FNlA%49>}?dXA`wsxW)AWpnweq^9)L)<;WWkO7}G79e4SlrOnmm_vd>=dSsCg@&P!5JGV<+b57JkPyONE^DnXxxv#eN_rYX6c(wa-@8xq=JwA9<gZX*9`=jG84|m!A*4Mj-7(loC^7ZaMl!Bknw+?rB>H7>_{0A?O77U@|*6!_M=voc?^83$V#)2io4yODRRCRakpLzItB`BpJXIV55SB-4b*5s$P(wIAW9?Q8Gq!w2F^mg$jvL7)_4|k{uO=-|_ZHb&gv)Eg}ULwO*xVeggMGkrqdY;h4EwKXMGh&2r06TOXoi7|PB8qRm_L7JpmWMuxQBDhg!l?U;1d&kd-0?O)ibRw%+;yzlV*5cj@@lsTC!yA(3(@U*G{rd2kFeuUo{v<{mAO0r`YRErBV^j1^?pR9C_2RHdQ(^U3yNyMK<qcb9BBzZgKNYV1#U8n(FQOuchtOZ8!q504N$9BMC8ne2ELBK*FO^Q)+$2Be+$9S=N5I*zr`zAI@m}5nysO07q@X>el{B`e7F|~3gD{kJRY7i&4kO{In8LF<Mz|c-bTRdXEaMQyHf{kBtw#5s*ofg$8ZZHH=7QaAz_ASIL#*XQcT461$wh@BD@?fVmE)wVt*2y;hw<MA4hC}3SJ*n?kesa)Ec-!=P`bN5NOP_jga{0U1uIH7ts=^VtB{W$YUPgVBnDmJbH<rZu|81Q6r*@cn<S~RI<gRM?_UI_G5h0EGd^<VkpQ_y8t(~h~<$N2k2j5$<04O(@{|ia$Qhw6Bb0^=^81S7RJDX`YOjgnM6@K!n0A{8J#BFjuKk8<&gjA>w+jee(kSl$aq>Vhm)bD_eQ638i>Y)z@Vq-D7s5NO1JC)q<2q$v97XNfafwHx>&HDJ#9@b3$JmTb9sq=n<P%y1((pZg1P+xhdUjg;KT7sVR=EJ*Q|>>cQpIpPh?Kck1_Bm3O_$oYSwRl=s!5A@pdx|*QCvH+D-PvMqYL*muMZH1+MVt_a-tTP!|aNf04jYVlve>GWLT>K;)Gh8c6hshaQaycbI)}5)%sAmWWN|@0_~Esx|R0P7-h6D;k~j{ox&B7~2h45+>b%o{3~fvv`1)QXI?6Fp4eM?A+jY7|WPHlPIvi`Q@1(%-K)jYI~jDNG!BOTU-rU$OaXDg2SMT(GJUO8$Avlo{$FFKlY{xq;@Z1@gI1zaSH1ScPZS@$U6v9kj^lSEFFQ05RLn$)4-&jeDF~offS!lDluVDvcky6Ked{IMfuy21t9W3vbR7h^QJ)dt|q8L|J#3ZPXb5S08~7Y*eHrFvuAOTxOdE)v!+}Cuqf<-06l$Dq1y}_2`uQZ;%Mp(>AJ;gZN7-W{s}aH^Ws6HIbQv;Krp<VNe$kIM&F+nE6$4m=tZ+Iy>spUEWJGGUG^}%;Eo`Ykrz)3qPZ7?ke*Y>y;GJh24Om)GX@0^7Ew!uOcpnjfWSBdF|o|}eI@fn1C#Il$~R$ivf>;ezL%(QLHLbH3W1Ee&xOuTdcS3If+P7`r>osXTu@iuLt60qGWef{kDpV14`|{9!pS)5`pI2^P*C2$kNvRcpG<;_yTZYLPm)vr{H_2#j11|Z3<-wbBmn90b(D;P37Y+PP%a`4=DkFQ8^&);Xee|fiFN{yTvNYYVnd?&-?e@rI`JMNLqh2J<8gB0iCfm*4@%+bqs8IGKF-tk&^jcfB=v?vKYp+2z5-?(bPUBH8X^(8_U<s(djiILP4)sHzp>e#;R7TxDAd{c?V9ik)Bmn#yzIq$OnC(&fjR1z95K8d9Hn-Y<22uuwYW1Y4*El1?4ZB)gDAmG<882IQ;$`N3u}eUd@B!D-iPI5<OBIRZlQSIfv*ZUt7sZ6Fj`SB<!XH~1lJz6{=f%0<NdH-<bSsT(WTNYc@C+Bk$k^s@o`@(=l9DmBYWwevm*k^ue>YRdtH2KD0TONTKJqUrDnV0wp{iZJ4U;=#MLJ+*8NUheX7yT3{wg{IgVn!ZOA)vr{l|F!*AgA3l6M1xHOvHsyx5@`=r>X;2fXl@{;8ZwiA0n=nZjzj_5#L$q1>tnZMH^%39t00sJIvCy2ODzW{MOHW=MHo~KCeE-G{Tf^wBjJf=dC0178O=1ak=4o~qd<gF!ZRg3c%?pumihiIJ>gCKGF;86$)aA_PuJ_JG5Q&CM8MPwj;!g~JD!~0I)7uaLy(c$~$7|p@YDQ>U<4Jjz!L4wf*?58uo8-q?4(RC<M97gQsS9pIG-f*TzH{2nzKw{p&(@Q7C9?p3+=iR7LQa^_2b;2LcDZI<$H@v(3;G^$u2cTWgFf2|SN#4WnAXcZ6L7m5*gr57L-Ft2Ziq_S!>F-)Mch5!&H{u7aKhQ)st}Z0NB94Pc78QmZ%{|YJ#l+YZ$pFSE!ty>}G1xaVdGpc4Pw*Ckgm&fd;I0|4#C4hKEb-+<2nRj7B?))meGm|M$51~?YK^<;rX1@=Z|r+`IfQ>3Yev+KgULzxg-9ip7mKSb0YHID?*)O5OW}@OvRF4hr1d122Gnr8yJqUAFzLn4FN$~K84&mdYQ_gKqr_A|6n=~Bs0Ee(!ZS2q1>(Y0b_5pj>815Nrgj`gJYFOEVZ5DFd}>O*J}3s1*FvQ+?BmsI^vXr-I2iXYzxa2*UvxU$zMvIhNkF?4Ys2r(_vkdec}sr&09x+QgvPq&6Nt_;I{L8*ql>)mNoO*kV=({4jXad%MRrv{R_Dbtb^5UQXwJNLlXOgXnf$NC?NX6lM<Cc@?P?aRfdECH4d{m1?BNbbW4x&ZSc~!yyFZw7?C0?^XRzFH68yj`nX~(wx1-4vP+&Vz@6=#ugOkg+nB|{pa^KIr7*pG)Xy{eMrg@B}tuMYsod03D-nw6VKDXbV(>V*fFWO(6Z#hHGgYpr$P`mbBa-S5ON-xqMS*&ETT~Fj^|M*oE^6+19=F_cnbl;Q$n)Kpenr?nl9n3;5eXIO6A-w7qUzZ7bY30!;^vGqHr0nUz!STtft*`eFwszPPc5-rXxV?4qdh2NS<mmXzoxOt-D)ED(gO?{KRBw5ieb84O0bZ+tVNOxVk5=*v9AOR}!BRNEyJKJCMfBs~ia%Rg#Y28r3~wlbC3nOUD%hA_);<D$oK8PDI@#HMw)N#cQtNQ*#SsvTzp{iEXm7CG<1b5;sgxUhJ+;|r@>KiM$PK!@ROH$BLgG7)O*2=&h7q6L?X2+J-1UwdY;9du&EMdNRoB*eu6;@423v2-n)*GA8*D{SmKQ5-U{E?wHZD(uCd^cIJtE<~$}@pAPkOTiy=PN?uog^mZ=Cp|E>An5$6}%48!?05AX!)kdiZuJO9EoB)m1YMddWH~X4=E{5?g8MY1jp}f>kL+WaMup#D^=JxlFkauz?T8h|w}Uf<RJ9BhBvzLnKpe?;es!RuDep4Z(EKG6e@^-%Lj77^I^&!^DmWAl6vRlF9S1!8&cNqzag#$DEs4j@psbhm8=+kj?m;22DmBP%lLCwalle1Sj(N;EfCSjt<-%>H!^G(@Pm49DrYzW5;D6jw@QPRJ?^Y1oJy3_Fiu{CY^>h0Qzn;J}_+OWIVR6Wm%iXh}#3LGh!>452=l_+=I9+Bduug_3bnRv)l$5&JCTO*+!N<@M5<HDrn$*L~5li`|yd@lk89_$YOe3&hN`}3%mrLX7I-6-esa6YS7!IAbfh2U<h+fgyZW4T!(^4h^`v>#>t-zW@hs9D>~GiIj+&yaez!?8IG_K*=`J)Go~9TsN|6J2xg=29{bEy3AK$xbIHiYHs@lbDYmW;88?EnrgeXa1xs^wm@HIAJABmD_EQ)#(B*`{0t)&BFC;m^m*8ZOI3Kr9B>P>HMx<1&zVA=B$5H54qwY5~(XrTviXlS{ssUPc;#cV>s$$_V7+g}>8h>_C2S(%iY#e!M^~@VDVZ`@q{5y`8*eH<Dg8{3e2O%2Z{R61^uu3<Ak?}x_{n^h{VmKR*^=}X`{s8#6uP0V2HHj{7?a?QEr9cg602<HB*`({oh)?a2YW`E6+6a<oK?vGtbx?DH5lJt+bkxA7C$S^^BM7UbV2KS1$*>px|Aq+kK??waa1bPoo<i4jax6jyh0K}6#8o<^PGp7cPGO(f=j<s5%0D-Z{<)xXR<G2unNGA!fR<3E0lAZEt&v9i(YYUQ!)&Vx!g6p4he9vm;XsM+mi}>xp|II!q;(kUIlz&8)9W<#k1#U8;iVSYX9k;qJo+SCjdCMyj$J4W8DHEV^NKXuYV4iAN)t&R!D%4b@Cqa#QYKb%R!GCtjdg~^JO3|X=;*I%0(!xJHn`fv9<#RI9cokOcoJECz~aqYo;<+Axnn<N0VFmb!Jo$_NJzSW-yUoXpn&qc;G5vB91#R`b?BWlK0Ec~IG>CiGy8>bYwWYnr~%oh%_rEYOra4CV39XX)ijeWP<l(HUo#&@mD(b#0l463-U;G}?l*YrbwMMIEB2`&UOtz}8{)?aa)J|)M(nN|L)|L>#aGqIq@bY6-p~`&l)5&?<w}!i*aKCJXUAH0tY<rA-qnB@ESDamFvOkIAk5|>XRO9_mW--zlsqJpP6<S^$N*|>DU+D%Mu~QN6~D2Cw>5nxB7&lcxtuP_B~hGeeiLtrbzy*I6%Sa4)maxgh+Wt8nvjH<PtYhZ(oF>FtR>2|u$(r@Q1uD<EPJDaT+$k7y?yJNfh|4*jh37<aGFAC0WO<=Ja6nJm@CkDBmU}m>*GF6IVrFf{(8(>etkus3t6d6>a3o}%9=q6(4a%@)?00=ib<)1q2^nh?5pe^kVGWh=e28E?N17zNEA3163Vh|Yr<q)WuaXnKt(@u+)+XRjX$*YL=-GrP|#~eD~Y*`BykVmVY(*A@XHiqpHmv>;@7(D2c`Fj*9R~S^_Y1E$Vj#!8ksg|(7FX^-iSEtq`@}RZQy3E4IS)v6FT`D^1yj=0c@UWg9ant1TC!oJaCy&0A6O>4S+>%HXu#(d<!b4pb3?4x6zM7ZD9K<D9jjGmFyZ=m1%<pt4;&WZ9EIGNOXY}SsdsmQWHSu;SstMNk$2K0E-*G#wFII|8K8oYEV{nlQj{KEa5Th)C|xaLncord{I6k?UgsDoD8|8*UHX2A!;Rhu4oXe({9rf**Iy>+;4zZXayQFzw_<n*A;wn-0TOsteriejE%grn=(`n$T3m{O0PF*z0di+1r9=ZNomU+<q9R`M#xNW&E!RFRL+ucp0f`9yV`_5HCaFJOt-+;1(vwCowb|X-)jKNd*5wnc8Mk7pD%%DI^CTB^&(5$rH|{yI{v%9TFd+$IS;=DE>~iS?*RY_^XR$u1f1|}^wtQm)++w{u&v<bcM&XTc7Y|n&EQ1N+;*@4>6uHkC&B71QUy^VG+<<V6b=|NbBQ)E7#~6nfVG>U#D$%&?Q2-A<Vq}Y7dmgNrM2bS1`*ai0?KDEaRW3%*4ij3FgLlZGVDg>YIAIM7!o&MV2O4^*cvcwXRYailzFX-K*<tIw0FYRa1ff>EVA}d>=|TaFOlnzQ+G}0Cu7sa0-@zC(T0qpetvt#0%8{sK<W>;WS~D8Hn|-g*Pf2PF~T{4D^3lOY;%C=rq}Qj)nwih`9bBBY3Wl&+Z$5DC2CXh5^fo>4%AvVE9tvOj+RyK65m@w`9c3aG{I>57<nivvv3kwn^JiY+VHHEjE}Y5lZT@+1rmILB96)I4s%N>DIZ#{wPr($o~!vID{5sU+tGw!Ze)vg&hh}=C71Xf8<)7P9L20HH^o2#rjZTwCw*;Y-2jo_o6F;7ms#TbcW!RbHuLh3RHmG)u-wv`y8t5y5VvFm$1Y)>6}Xjg>sc<U>AcV`ndQcAqZ%s#M9;;cra8ang5Z$v28>L)18Li+znMUC`<MA1*=3ga9;bW2)rMytj>yVHkf`n&DA(3#ex$g$cI%N6)pU8hf+NMXp|;&4bBk4xSwJzeC6!lPAdJ1(JUY2TOMJJDaRzGI)7{v=HRzG$IOLex+_gI*G6??`biwQaZU5%_?jzM#c!h`fzgphylPO5qF0nGVWM<(8ai)T~i&#A@+D6X6I7?Vi+<VQI#^EZo#5bf-A`)}An>I{qf7(#WTt#5``G~CAkkn?jMj}1O>XT!)HfL>ECB(!ascdNW&Yf|$Vrar6k=V*v3eLUs+?W~p_GB;EZnuzfmRjPQ@~lG>ZB0ikzek@JLfoHIEQIv^do|pmQkDlu@L6QnEVAfy2&Pd-eUV0SO%M3Ug$3l{<q8oqudC&CZM|ksY&({~jwaB@fE-lD=?eqlRSRJw_8<?(C?LgUD{no_<$eyXXacm5YfaQ#(G7Wk`BFmnCx~kXM0Y?$9;U0@5(Q2Ov&n$!jG_<|i^I#85Q4+>z$^FnM+iY}H`vh#5Bt#8lFx5~9ILwvcf%pbSXSM=z_{?IL0TU~aUK2|aj35@(@_+Dydcz_-RJE?iqob2uUC6)8LcqBS-^`Ne|2yI=}&Mp*gaX!3{#m#39Ng#zcsOfRH{{veIHZr<3I2#zvI9KJ3e}G1O)Qpst*f2j5+=R*>PcQKVZ1|6Q0TH^tYKgXDRpb6Wl&}sP<4U*d{N>KBt?GH?(~df;p4@FW4`vUdWbeKp$+QRx@@}W<VJHuL={M)di(yj!=tfj7PovBlW!f55p);s#DoV+NJi+HE*-SNt5k;(Y6blTD}+P##GyNoTl2I;~TN{N*hzPC6;}*-qy5jNNZn9Y_Z^(WVJgctLEIH_KxpU^hY|X*?v#E-dE@-%-75LBkg)GeF}20s@aZ0yVia%)!Bf|Q4Z>U21Iuf))WLj3~!Wt;$g%@t+$!fdSmrm_kh-x1eu)W^Bz+yPvp_d^9W?ZSx+Vw#_qipX>aAO_9p`QyX;d#wfr_DCL+AK+tYo&Kbz9#w1TrFL6&bzXW*TC(pNv^F(Ge)w_0F^7-B82<=(F*yx!2iMSIoI!n}=YDB{|sE&#4}sN)~rd3!qk;Uas}ylK8Oef2|Xuy9Y>K=ZL4{USGE*ab$;OM@52?-IY&ATBw%0S1>{JK~!paD>U5Hig)!#*e3h5hagbE>x#Qb*yz?74FW0asL&*3~@9?<EMI&V28}L2jh({R8W#46_4O4q7VnP0sk#AFl^pjBsgSsNQZ6!mHJ3TP;=lXHtdP`V3SI`{SgK)`R9yOr?nLxuQWlz8ryz-f1G;rimJJF%7d;>VUQ^we(KX|^yc&}b^8qpLW%jQ;#6vkm#JQAh4A-VTrNkdu-=uv6F(Pjtzz6bpHlmLCf&=>*+i+N&p)w`-%^?k_3S?WG3K}`*@lv$jH+Oj?2C>A)ca5YyNkb<nSm8%Wog=!%gs*?PKncORx0J7-^BK+5}_vV0j%As?<A`!N2auB9IAThjCuP_z2@U5CfTStg^w1;rfOu3h|0JnPOGTbO#pfgMnZjd8hUFrs~s~}=b1iVMf&C<65?2LzR2hk8uSTUatOrlwnizLS=S00d2LBJ7Z{C%VGd-Dj$tVs3tD$lG%Td3fKs!Xbrdma8`7H653Nmhm-HHuyy|D7iu?jDf$E=mV=hm*QlF4m1$ABvFXqE|fsqnCyK#}|g6vYuxioSLB(W&Vk;6cOoM;wdNc%xJSLc6?mlJX^jclL_8v=ZZn;M!f$f<Xk@YzN!-6PQ`#bVP8D-=Z7Mw^%d_Vk9Z0fiTQ6Suz=RIFueAM`K8Txj1;yd%|A+mACbZ>Tf`{4^7L-Prd|U5bNPrcSeA8@++rZ;cQzoS>>nA|n=|rNW34PEi1-K)lpQ?O<x#P98OzO0Ywby5M>!ct4AM6GdBClnS-8LKZX>Ep-L%z5-_gYDqvcLySIRa}UQFdxlb@MdIib{t<NPt1M_r7UgT_eFE$#PTBdHHu92D=gUsJin~_9CH!}_M6PY!s6^GFDn^VLDwxd1P=oypH_SQ@RvxUiIuAQwr{@b@@<MBC>+QAG_L{rU6))6kKUitC*IExAxJn^bqTK4k2c6E!8kD0_Ak;Qt$>vlfWJm0G@gGcXb!xf%4Cu&gwG7Uh2}h0=u-;1h;mX6c2knQeoLNi~(?gsuqag7+J3^lIfY?1Cb`OZHHW_THrxCs=s!4uK1jav_P3+V`?Eh4c(-bB3B(drp^io|)v{d^@Swj&-!yGT|!|5m}FJ!zD4^VZFrZ>n4@%u3~AwTmb7MAW^0B<77rWJ)&e(%zmb%j}1D$5Mzzi7%Hk#n(nVHxMarB&e4E^uWPxT;xg3=nPf<3M9(-2q~Ki8+^c4kCSpIaf^!+zi1Dhzb|B<7Z%_Kf@LVM3>84VY@3cY;-`By2=&Kbt~cAAV=B+)oYSe)C5EmB?SI+1^-}OtMOhdR|BQayjsncvmH^ju&q{MTXSkQNj|&##jCpe)++5=am{9{RocIjHe0Q^eKcwt)x!%K4jRY%$aBCCG(>euvl<I8TD){iFWus$TlvyN4x*(7yTxI*^00a7mR`EWOSf8i#A(J7{`Zmpp*W#er?edK%N8%)(o45^={)e)Bvh%5`#4{y_$4oXnE~h0_x=--qxYzq%n~w~=gCA8!S_gu(8^&-v$1OW%)~)3YCuyBIar|+I!+!&lj$t=#k)E?bQ4+6$Je36q5^Bl6<$rTgb(ecp7`^8NyT<8iI_3E3-!=57Mp%7*Az1<9(5G+0gy~#hHtsYXIL4SE+Yxh-r)Xpa~+@^KJ73MRG}nma4}3vU$3;{Sp-*&XtrimrQi&+1r@Jh6-@;}%+e|{3ynUp*J0M9P@7ym6@X*ZvnrxfQfz!wX`E1tlxW=J1BoX`L<<OtlWbY+sqjD%OZrPv;V57mb!0xQt8rzfNS9eKGxRwCg=<z5=SQ^RlDQFaPvkzY+>4T`+zA48H(ynZNQ)MwG&fvR+#aa%TpB9GTsC-L4Cp-pN4bz<oQOJKD9*dbff|!f9mvobn}XpozJ^aHUt{__zCIs2*cB_f<JW4gVWe=hjHj@+5vgVsp9B|XVLKeno*1Y8xmiI)oz>>?H<n(2zfVyOsfx`%;AUW^^Knh%XS1DCbU5-}-(zw%n6gUF35%s#lG+I{F0^_dVcq9lyr<{nn6YiutV7M3lc~&M2bLEs$|nHQ7nu?lAC-a$?V5w}qBzhQPXym(tOp5B*2DC<B6W*`<FdiRN_yCwtzNtamUNYttZJ91pf{_66$odu8jo)?>xe{qVa6HB#oj%RnkBFTf}?5aXI5hagm8wE1&ZbcqY$%Fev(8L6uZx%-;?-SaIy9b;A(BpZ0vDwFe2h}=BTQn6UsLNpiQ0o%+5L!SvK*aL8>!pCR(cm4MlrR=W@NknJi$!q(ks>B=0G#?@O`Eb4YYT>(1$5vf{n$1i!)Pz)3oz%izU~(;>yl>6ku`)03@mnDG?WFhUM(Ito6wrE*qJi!gKwWN9Kl!EQA)gV}0`TgwDjS<J>BB1R!X33*`wmdqj(ZI<d?j#0D23e;iAxj^$3dpYl2$PVHn%oRW4Z~?<AeW~-++|t~TUFL+e)oFff!r~4N7e8{kd@h+#ixokR2o<kyFfnDaG$)IiJd|fqc`ZWh_B_wL6xXO=mOKZ{=&k}f&bq|HAH#pgNH5b1jarT4>?{9ecvV7L8N(l2=iOiih%~%k0FNIkZf#?;<ekC(PhIC!a=sf<t*abUM@w0HuC<Qrpu0se!$gC+JCouIUQDuSIn55t8Ms}6C6$N`Jic=mUYP}O5hyQll=?*SD-;mOII8(&==K%uRMzxR9oH=p;gvfG;EZU;LE}vh{H_)b6xvcv;ROh&mLM{U52<%=0^Ae1I#Y?%Bc7_NbJ2##LyOBQ-9XzAsWeaX#7hm*q$5EaAuE=F7c3Hd!%6TBk|2e@Itf%8Z@xifzaf1LAv*9m#pok6V~WC(jB~i;ibiLXy;n|P8n{)&e_fgrh5}()JFXpH#T5&Ut^mYGp=g6ijg(7yvounT)9s^HIg3$DOL??+Y91BNRthnhyyR6xQBR`ACY=V(3V35sq`7N|3VzP2SqL7lQ_DxHrRUL>sK~`AfiZ|J4+ZL-%bgfBXMPtCs_Es;^KT}1+GVwaZYETWw+-Af;5Ks^r=ggUmPa|1>L$<AE_(5wMyVdN!#l`#Q(OAh78azXQB7qlK+v&EFY0iif-!|ns*($1B$J$42Bs{yEX6;LaHgj^ehLXU#FRr+La43*7eGUle}v{eYQb9Y<LKNif9yEFY`!T73yB~@++p`Lk@Uz_=D957G#bN4+2aBfAc==hC3=sH$SX0MtlL3^YS&AnIP=*k*P578HK3$6n+ziw&*%z0PHAW!ue6+{@D^%%eFIg^@XRJ6Bxd06Gku0;@mxmtGe4i+a~yPA)fQUSlf@j5Vb1F~Z4~+)^U-Du`HHVON)@4leVhjOi7mliiE~qd1O*rB0K$;kJOtKpQi7DAE9+h+VaHwRYjmbfSS}auVh2gnzmke-3hKO)YR)qi+M1xCxkVY@X%AeJqBn~v43YQQo(|zfn&qku-&@VS%m;-dKZ|ip>b$>s)+R5eD0Dwx2<Z<fVeVr9SYzS?eLZ?P70)8_H|Z`tRd^IQq7z*NB+9jsikqC8_4;p`f}#`U6cmLDC@AR5DJVV)DJb$e1yy04f)-Fb8<7=U(*;8zt;_pQI|D>O&dG1JhH~jflh+O#O~So80gWx$;H&wPuC0m;wM;DOf?<RIQE4aqfhDmv6~%K(BTyW-;I^P{2VMy=cULR$7S@s@w8wPUOIRu#|4IcEX{t`%>`;)Gb(6;40{RY>{4%vXG_}L`*2Hh2I20%ii)!>F*D@{MUT>r(Z>#UNXUVO8Xli^;19>0qqe$~`83UFM;<guZw$ul-8Z_NiDC8<6?TKV|u4S95{2WzTD&GQ_Ij261>McPVkPGy0c~cf<Ds2s#oUfgUR&J}L>4uDbO>D7hMuRLMje?|+_os<zZYDl**D?gKR?$ee>RJ*wFO#kEuQB?CUXsM_W$!4Ml{V}IzNF-Pvf)TG%NodUxRb?m4I=VmL;d3Ed57zUBTZch{SnS5b{gzB_QGULZ(t;>`s%p;^pJhVc3;-;F;9A4i@g9Q!>3C=+6lzH*7{2|V$(D`a7*vV%;ISr;BsF%!k@k$_PzSVuPF7w>z>dKF_d_Qqif`3H{w*pb6km$PY3oPb8iBmljP>#M^?6<_;~A4<rV*>a`9QwEcZEx%{ajK-{@(dag-ILPT<xoFAat7vm<YO=EX*l=oEWsruV$`#2b$h_o%Od#Po<?jE0Yd#KW7v!gnOi0z*HV`1mvnq6fck{uV#1LLg>vn;D91d%clAz4;Gj{w$%)7yiubd7?B3#2P+kxB!2~wrBB~$J#rpFm8#Q@ORpfPMoC@GaD4wGlat{?+0hGuY*A9pz$Y42@vetKl~HkoGLiNdl;yg)*|{hK!`Ihfra(vZ|K!dmPm}-JNN{j_stB8L<!v|i|^t<;jR~4L=6}40WhHkc^c6ZfWQ7{wmlAhI`grC9(859%s>wGU~YLa=I_j=<EY-FQp>PZ;@iOZ=3$UVST^=2XlgbLN@s3+X!4Lg_@lyo4<z|`ly!ds;{{7b?2Y?KCLapyCj8r@x0Z~OFzT__gXP*o%KP!nUrmCZ$Bsp^S@?Vu&`7_E;+_vI<FTiB%pEaEeWPSAnofyjp2ksl<+JUm3!}N4^rADb9~nh2V($_P{>v}^?C;s37ew_Rfi5H7MyztVbn~lT(2r_HwUO_o6K{%K=}l?I9Y}{j_1FKHl|7r5wV)RRIU7tlxBSa5{`B7h&MC0TWTKbJS_No-t(w$}oCkOaz4GlJ{oEQD$dgwIK<z*N&+0W$y~NnNjArQxXj&=W!BE)+@&*?=&9XwMoI;U($Yn5L^g^Rq|AbzXB9R3=>ve-MJz8rNp&J2c6CBHNnlH0wpz4{RCeYjnZzMr@H-FCXnPT=d(s&6=^#fd5D?0%wEXmD(gxOOCoz5tdU4Kzg!}a3kmlq~hq*b9D4?x=i<p<x-OdCd-V^|DOAjSa*z2Qukv}1pG0{9Z0cQ4>?=oxu*!vKjo{){ikE3?Nv4^&s+TS6g*_I)D@Uz<fyJT+@@oflaiZ_hMf1u2c>PiI~~*5o?!+zhk6{fj>UZi_*P5WfRq5^ro3JGnFpzLvX%)mMHz2*&K|nqA?F`0P*qD|-fP=CLoLIJkmNL7g8%EtL2kTmAmGzyGKB=2gv*Hu5cVLOXkQ-F(R0sNq;(@u|CR5Z?Uq%n!8H*1tHBchSKRgdj(NeSzs<KqIr5xYjJY0+iM_&n%>_yn+RgUwXR}coR<_G%S`~xCBy;UtGJ4qy%bovNZ;u@YL@es=W3Ckm>$}Z3B8huPRlkS<AonJdBt`pRp~lZs^%hV-C<lColi0&~u;%y@(z9G?Kh7w3e&FZ@xicr@tm!ZNV}bg7s%~051|UE*Sy|iK{#7!i0qd4e)|L5%cvY6%_<}0b5+OGm20SA!)5wY+*HFvkB{tBS0R#FtE~n6X7k05xe<YzJh_oW>a7tHbD04qrV9s+^aR{6*jYVd>9+_B92_N#Ay7WV<6V1F(Aa*j<3axUe^6I(+lVwJBc!SYArHt0637t98XwZ5ersTSn=hSaqMfjJ`+aN?hrfCTP9J*N7O55w+9l4Sb7T(Cv-R1QzDNf+QjPxH-8hcZ-4*KpfTQSFNkk`iB_Lzo;};${$gwAfIpE)C`$Rqp9EK}!$O6Z!yxAkCL}}t&A(>v!fSRGjd9rmK6*DkzXndi9+A8Tx&1EaU+XKHK%U>@qQRL=s3rgzpk!oKgbbprLG*cwkCnd*qpNEuQ-wtcdiU;p5`@<vOyGxiacyugtukE?r<Gz!<az-0?%cpfE2%hM(l1{cgM2{N@Fj^$dZ7Bdvs@u_;c^x^=L$BTf`uhcKs*oqTsfeR?0v5DJuh2fX_;{Xzv35lnG*ZQXboM72By9A`upZYZ}&~KZNQ?8(Rx7{YiV~ElB`bp&#^a|dYL4msclrCtr~ejS!D~p>ZD-9l+RxLBsoN{f|?@CyaEhNK3J=-pyqazkWiKF{^)C?o_)twWj~k%)S^^25D$I<&%{{RQIHQke3Lz(ia&tgbTt;N=sTbT;4hHs^l-D$WOjvC1xZIUPgOt-S=R<gxXKzCi%U%e3=e-urb&Xc&BJ9cx%nql+!9puxxafr&BVSJBq%o-SP@-ND?o&x*%HAdU^l-)Ll7TV)dk_F1$d}Qc?|Vnt!BMoeDe=spX@{sw=u56iHF=134wru4G@}wWcEmYaS_|DgX9kIIa3A;hX)#u-!P~po~F+f;XO<UVx<ei2uC;yx-y%8j$N*u*7NJoe~h96nt0|gb9t(kTax6Fe64+1EJY->O?0#8yvgb+f6v=A^|N<xxe`_S@U2l*ytPc)tM=G(t_-a6Mj3q-N4M=sFNo>F+{!lmK$XYLCf~M@`Y7MgfXH+!e4zG>?#$AP(9&B?vWX6A9N^OPLHdxj0zdn>mclADoA}5g0r#jxs0qF6UR>Y&{9X5w{w2v)`_$+csLEWQ;zC2ni<`eBnpKRe7Lge)L(n_}6i345CJHCOWuU&3z|fi}<O}FdPvV~FaH&6gcI^yw9}MPqc<uZ(^b0MY>zV}(`T{nb)*a0-;*t=jwU-gg7XUMo@K<@cQ|RVTkM~|2*jYF?kW$CHFK_<moBt`7-;2rk*gm}Z<Kw;U0}I6%C-o$_qRzgI&HxwWXe3%Nx%mgs{7KjAN1x^>g-$GTX!Vs>4D^}tSw!L>fq4UTv#ZGo+RvOlJcX1+96R0l^J@Exy;q-B^mqOIu-q*OKY>-8PQfGmTkaI}-A=);V38%+51)5(3kvc)2RMFwImab<=DQq%XTHN7xHTRZI|K1osV9(r7q|gm@n23aAR^N*cLVYdpjmr|M%2HPBM@wFe}HEQa!}^@0{wDd;7;rf8E6B2bnv0$t(T5389skELXRWMy2HRez)0JAItzU!AmGCb(RrCmkQ(5dt=t{hJ0(}357U5o{XXT9Cor0I$3D6Od#B4WdOi4Weo=J*ty4*;#jTVQpCAax5j#{V1@1r;eQcM1G8n1TVrSs7`hXsImrh6E3lE9(6@Ia806Nha%5Vd2(+|eIfrakBAJq@NOR&pn!U^9W2$C=@a{Vc_?hBq&>iW~6m-+ob-QE^ScX$1L1wRM)*m$w~?})z2oPRIrN3rJ*H<#<(%R2s@<N8Z4iyePN?qv+ejp9<b-wXT(V>tGU{eFB0sl@O1!n?>5&v5&pvyVyNUxC*TDvy1)&+h>LnxkyH{nATx`WgK-oqmzlu;KG7aQV>>htuy_kh0f-e_r7814TZmANf2`WqXzu`TUf(56ZBrcyXi5<!3niNY~*mzuP(dxSx;FE^?8#k30GB=nu;;qPnl|kUyt|d^Xd$+VJ%8WeW!H%wNRK7lr*2FW=&BzC--zi-NEHAWVuqd_o&In3Abj=H5HT%iF%7FSHbVEK7V@<lH;rMlHS5#C?1IJlEb9-5AbJeSgX@htZtH#f&^m+_Wio?&+;ktPd!q4AzmL&s}Ed<vV5PqbR}kYs!K|tVWQ3Noyvz@|Az@hlmWOr_m5*DPJ#HZ{+t*p-vL%s3oYVUJ~kaTzVRs8+r6Fo{c;91Tq}O1TnUpdOhGicD_s_$VJ*bpWauXWRqLqh?*6cJf()woky_G1K<nZDYm_TaJ0JvHUkk1aT9fLDgvYh{CFUorU{D%x*HEA?;YHDl+Jy4uzqkK-plCfYV5zS7f&$vVvf9{h5UF2T#A=^@sJK>Uc9g9&paQVUTRSf-cup*=ezKv*j?0xM`ESifyW!4>%k)~S-^uQ#$y}RriI*h>Qw>Vfrr;N`<fVby6^a@|0C(MV@JL>DR<magB0wP`R<NzSt|6{J<opcs7D8FCCl>I35u%nUqrf6QQ)mRns_k9yW=42!@z?w5ulhE#nEgyl7flDm9HSgIJeZRh9e3rz)QVB_V63ja3M(oRB7tu!<#9Af$PRxzui~pW=c_e!c(6CdG7QU!Fmb(F^XD9!BP@i6w(|Dn}VG|jJAlw4&z(!UUkIVqHvM34#Np~QCt>$XgSurba*Xv0wn2;(AXi#EMyDWHG;{6r>?|DM_BR2R%jzw*FrJxpF4stYB=NTSCm)kn49mGD|5<;NwH1erJlL^bIqP}`{gLH%q!=^sxCZHe36%4r&~MaP^C>H?hVlh<o3zI0tsa?P2i}Lcxr(taKatY4_RL!awq2-StmRX5fd<Ug1DV;uMYQK9&bI}-!1UJeYJJ?a_{ByLhsw&@!s~<ewp{}xeuC$hj>l7(FUtCzFNS56@p>7r~?i@7k0X#GA3LaIH2flW6I}3eiZ3^Q_+V!Qg46j<?}DMp6?#vh1HcQ=$EYGhxBiP{|1yYi1A;vOj+d{ukto~NMQc}h_QR}8vZ=}a)0aaYdoYY1NN(NbZ*_Y-1ESYiG~>dDIbJYD2NwB+qDLuz3cTx8K5y9a0dCe1YlrjLoHle0DL2h;NgV>dM>sBM&M*OOk<Ghgo<&MG^Xfx=;J{ry09Gn@<!;K30*KPBc;s;0%X$^Ut6o5oV?yT+C9lp<m7~^<sW0-7Z_J5M%1KJtUoGC`SgTp!TYd{*r)K~>hj6*5XPup(QdN+lwNxlIO7l-&j|B}Wa+;6={QKM%WoR>x63tkSFfm-4U$+!k}6iMQKU0}$rjj#M;bGV|7=Xt26;UP7_na2@nLj_xEJ(D7Vty8z`<ZZS#+F5-rvp%gt~K{OC-S%mNEL0u{21h{v`qtd;wocRiL0<tZM>#1EmmJZalRj0tOX*ivy%5WcR^d>%$MG2916nSGB4SnnI9_BocJrEeIUHfsOE&eW&>Dv3z;sT}5(DWuvm!4<d|?t$c|wPa8<%fp>*sxN_)I%AubnfK;IrfIp+yrOGik>W)YL1i@{MDZ&a?b)TS;;&vDzI*|K3h$Ftt-~1BR`3MTU^v@YyPzbp%BivH)#ZGL6mi=8}7Cwu{Aepd%ZXDp&8HV3rbd0uH2X%J*u}>|*B8MA^kR)UwiuOjMLCxUqO2oL##Iz-1oDGe?5E9B+hR+8Zb)s+lG^$+J-UzDGkcr=q@<Pfv_}S=CZOLn<NGNK+%?QFKt)BD0i}Hdf4)Y9KkzYV}5){VyAJ9U{elZJ~0L&_PAOW3U6aD8czOC7G5$U=42^>cnoIOcJy_$Kq@u#wQCX6cYDo_YD?jW357o{Nk;DYnUI%_^fmv<b}eK-Q1kb%{oynEx-uioDO$#reHW-c33Fd6J~b<4k-RrsCdMhbI`m%{~yn&%HRV49F$Equlg78WI#tBw1g*D8<nqqjVVDk%Z~rg887=fC?q@2;!0pS}6X+n@a8ElK>J{N#5&t7M08YmINBAgop@xdXDOR6h|M!CzFW;-T?Fe+bjHTKU}yo)r>=xz8%UQ_1dfp=S}WhTeTThUF)-F`n>|!z}5kozmn~$Sv%cyu<>&5DO^$hw3s6Enq@#jsrs1l_lN_aSpVWy<VcxjDv99W-SVE0_5f-SEBa4u0O6OQ@^Jv2#%?U&!IyhoIo3vT&HwcT^_mMe;ERk&ETI!r#hB3<c!%^^<Cl*H^B56qWlHDt>;ZPV4=9AeUDkV0czq5-QZC#-KZS!dw)<4B3zoogp8yHXO*MlEzopNwvLYv_nv-v%r(Tfh9(n0t$^@2O40VykDgRz-}+H+hG;c@I`iYpBM|a<q-|?Fu2$aA<_73oZ)l`Pv`*ls7YAN_jHB?j;?M>|(mdYj=U>ICy)=zcguJN`WK>r*$oQE-uDs13LgtDVo=ocd4X|vt0AA3YrG6D5*UZEDLTk&>iBI)+A$d1LdfF0eZ_vL>ybW<K=-Pg%rIzE!RM1qASYebASnEHKIVMFXhg8;AoUm#^pb8DbMW5v|ANer9<kqtK_6l7DWXFq7*)rQlmxWQ^P(kvw@lrZaA-)RIQI)hDRz*3l>YMX`>p^&xTZL7((|COU$2A31oyB%QMs2AaGU-z~<gYEr1r>R+8fH#!Vy{GJFP_dB#HeyD&+dsyxxcrwdw6p6YIplcy-xKG1vWb8)KO)WkpUR9ohAy)iw(Bg#7mb`A8dJ8cyP8uaVm$WvrzNHFsNg^`WDhKG^0Wv><a=}kwF`(Df@Xa*<xF^xUyQ>;!be$R~WWHv1dH6jyFpuTXzItN4xg>V(-x~o_qKvQVr9CX7gIs-|Lc1Hyh1$(Rj15zA9VCv!@Dykwt1}<DA&+kbvh9$UTuJ+i$Jif#%ymh=@o8__J)qz0bc^mi4~1s(O!al`Ycyg7(V^U_bWu9{rElD?jN)H-Do>fF6Y_?!W#<oNTwQI^Na>ebqI;<Ou>~_9*Uq*(94Xe539ef_Ass_0RmV)~e$3tjV^c$?cIB4&rDz*W6(+VNVfezB%Klyxm@VB~RN>wnhPmMAm40^A7+6#A)*hIz(%-?N=N)<7e(g?%1ytqoEF}+o-fOCd>LRaiIufIt_$4ZF?9`Y9n!|K<8S|->N5@Ut1CFch(f2t*hoi1(O))hx)b@3_?JB>ft?Q7|5Fh6$)zfHG$q#IP|=U3y0Sk6hcD9AXr#f0?#=4Z;!!R=~NR@-n{wHlJI;-MLPAL;Yqd}4YaES-lye=@xxsi`<FLsUsIu``UADT&@bM8Hr0RqkFtGrvg!*T?7RpVQITE5U{HpN#mLj$y4PLZn3)$lt<`cFfYBwu=W;UegIN-r!=TG{5VV8%76v_TJqVpbHooo{hnbQH|7r#kkGEXiL3cg=tm%!DO(HVW%i4T2vYX|#wWpb_J<U?Fu<yk~6v1Z+2GIk9@bfr2MqlCE=%A+V;O+L?)X-d{)D_FO6H+h1a_ak6v=Y*JG>OMHz)tCr;i+3b*$8|HUPVDEPwi#o$TMmwBI^Een-ZG1bYbxfHNFBd`3hl{%@GPWdXFixH9?OL?t<cx>aedVBxnBI`N3OvUm-7Xk&8yFT`IS>BZ}0fBVvW}`YYAIT%?Sf>2tcndfC+7zxk&w9>Yb!{Tk1p*`u;gFy~=lUw41I39=_@-~3(J3viOmFi>C35|kZ&T&Gcb0kG#Gqps3dECQ-}rnGCQtmaVJN|Jy=tUV`_93j+s?Z4OLaJ4#jW{5Dm_m~@pz-wn*ILL#zN<KXEdSLd?n;#Mf{kD619a$?~Mz(MM7GwXCEDSPGIAC00!uVbB3nO7`RBdG;m!Yu*<Of)CW@b33sd*frvuyz^teg37H!EHTAs*z~iMlaA;-eM~<da2K4T*=iQopSE{7k@2mZ&EVvR048g8^#Ih|ZZvD`QL<+3DcSwvv?#ai%!_t@8uPr+I9tFfgvCw>e^EF~%$sl86nX+qV|SM7!`_VxuN&xd&$#0eHnL2gfG3S_m0&GrY2|ZHqHQ07_=Ok$U41XnO|%)b<j^7MKx?nRGiZLJZtfv>Jbi|H~urJ*D^ay+`0myv<(OdtxVpb}92bDWco(GP{#=RQ_~xqp_kUMWgN3Ei?K{?Gh9TI>#>$YDz>z3>d}%b2T$h2Z4+*yT-zMZ}Ma&vRf{rZ(E!+JyIu4eV6IQV_(JofWy@@1`B8u^iENf7!+A|_&eO(IEAXh;UTYQk&72F;<1G8aI^95yV|D*kaF#}%iE9SjUWaE=)gc38qTX?)zT#=<(gwSvbCE|Ec^O>HWCXwIB^8fvy41%%8<VX1{t0hCYYKNWdiEu&95dt`nr5N2(H!&BSMlJVfpTxjXQj9a`o0H#_Bwu8{#3+pw^51Z3+PlfH{fj@-@rvsI<4Wb?4-a)oS4d)cjWHkIC_b-u6hdMZ+NzSJ`ErM{90U*kJ=KLJzM=@?Dge;{$vajfWm1wKgQa6eo>^eBkkvdl<CNwq-L8A;A%$NORlU-&)K=lKEf_-=M$%-GfC=f6;iMfM_+8Hq~g(aZT`R4hqOHPe=$vc$9oOCTsIB;ddz%ATn1@2u$ci5+0CA^25?x7!$I<1&i?O2k@FL(@()UL``C_(-A8`>g~t6Q*foh_&tnlYdS@b0PRcSb|gk+<Cfbp?VmwP@ARWxDTsT`+bKS$Q+;}HaD4J=>+Ai4tsT5FT>ox}J!uS;M8yIF)XMVNhKOHL4`Zdiy19@a6Edn#C|(Y?H2YES6e9q{5A<7OR2JutF@?V8BmG1#Xq&&ri-KJ>^Tx6S-yg?7Q27{<UIk0giWCQZU(}!aVIL%z1h7GG$MCGa4+b>MGnx10wC|-xi4aI2a}WKW&gd9XGwTCSKMN8%nJO-N&0!Ra5*SI)6lkTmqq`x8twEohaAPi9K3Bg`+<UP+zpCPVMI4ZqU@(__=K7rxP$GkEgC6Vb<l>ll^fZd*Hs17Vq+U8x<pFa%N35&@RRVQ_D-`rby^xOIz<ei_F-s=}E|Ug)(r3B4%1JfbG7>-*lBAQd-V|!Z-__<tFxEK@!dLQeIz9Z*2onAPgsd(~$usOVdOOFR*WkV-(f;Q}#YFxFtC}qu6J-D*ybA&$YuB2Hb^(C*=B?-%9#5asEi9tLcBK<Y$yJ#0EEw|;^6W$@k45K=?P2_NgjbZw^Y`k8vZ?#FS%nVI$1y7Cq{{!n(aFy4v#l@pvDD$#izCrz5z2NXPG>;P#OFDDjoGL3!n6&_j}oJxl^^V9uoU6ZVIflR$T=O?5a-45Tz@vf{4=ruUX&KY^Va-?o`#AzV0|D&kPsz^3H|`Vi2<Ul3ZmeA<c9<U58fx@Tx@Ta3WC>`SQ=BT%>Zwp?6W9b;tgp@g8?;qE)QTEs9;NARfQ&gvvli%4i;Yu0$o-BpfZEidD|scxxyUnbS)jK<tM#<%z@#V-tAfXsz*W*!8IEVe5n~jZWPR~`B7ec8u?%_;4j}_5ge*WhC5VU&8oVN^zt{l0RY|FIF^wYH6e<V^tm7HczB#Yliry83<(2vAB>-#6(poaAhB^J(n!>uC6`-0e${}MJc^R^(8qvW9ZYW=fb#Kz?w3fi`#ShB@i#5hIQc(o&9~XP{)+>3`m3oQCK7~{5s7h-nkgxr3D2q!1)ggugCI?w;^K(BqbGhL4xH=hsHVOE+1k#eGAWFh*2!cs6$?VEB&B*6Rw|vyrDKg~xqtzttpt=u+8NJVU(MPWdC3;Bz1V%^i0ZeYpb|<7R3@@u;m(rOv5hSFE)l2Af%`ac6%l4cEQ%??*WN2!cSWe7;!*Y(nUo%t6IC+CXPe>)yKAd)d9Q-ibQZ~Ii3;smJAs~5aGb@>lNM%CDVb23x~Sm5H;t>O{-t@uq961y+LWUHt&nCB#&6(&#rc^4^WnbFwVVw+XpnDx=%-IFUxC3;jk@0~k?CN)P=TRn_>2I({YWv$m4=Mn#ehBjIttV-erk(gh!xy=rAE9g!t4=Holrr-)C@j5LeSm>Z?#hlS&;k8@jzpe?<2)Je%y{ap5&3wsHh&uZsWkFms39)m_4NNtVE=3R*aZX6N(CS*WUXor&pF?<4o|x^Or<N{sxpcJPN&OGNR`a5N9LYw(Adr5bdq!K3<(?PP$L^+F36wn0?=$ZjYnT7gK4fzkzb?dfR>yqzg95xg$FZ@Png+myLu@Fa?9ls#zFmZWS;v%6h<)m3-vUwFWRFY}6_(NWRHdLBQFW$tW14RaKv7E3qr<KFOYoosj{B^msZ;Q;Krd$GczvO`0P92tgLCcJY*+&?jZL-JMp0XH?OSdfmPE^ZH)UbE|89j0X;}l*uS=yiAs{F|fL9a)(}JTJWAkjvCWwT9s7`M-tDfZu2|ilV@=>AwNe|Ek|^|^r#0$XO)yES*thl`?InC1!z%Qp*Oy~@=FMW?h+S)Z1TGZRLB!|CXhz*-xPs9g4b%bp`TCw%J1UcJ#F@sziC|kz4HLNcHRI>!-IY&pyMWqH}roG)bHPmLittu2*{zR?-Ck^zSqAz^66DzBGx03?Qsen2NQZ+T?!J+LY-eYI`B00i$u;*%oM($7vxgXO4;yn4AFKn8_+owG*%=ZCzq{QidB@8kT0J~m8hV9K_f1H8s&2&=bEW(x#ChS!v1lDoKu~8m*WT@!O7;1g{k&tZhWaN<^_!_h`A#~sG(=ih4$#+R27s{`_u?%rVU7r;wrzAjSnr;J4o3Z=)sNchY}6NN{vxYeUxJv3`39B;c0Bhk7=xFH}GMqH1dd9#ZYM92t>po<7wQWGgkbVv9w&|+fH$Vd})~5Za4Ax@w4E<?^oLeB`-@#W(_Kz8?~x?-5g-a{YGF{=OCb5a^#R~tYoD-j?$K+j@N0=siV8^L@P!Ws_|Bw!uwgJ<{Z_X%MkC`6N5|Jh1szl@gCQO@$@FWSS8R9!kt&<!&4JfZ<x=HcQ0=N<gx(B<Vpv!S`387sU`->1`>o|zyIiK1q#U1y;uSa&0^k#I0|4islBd82U_ThZ2IcNeq9gWYy>-82e6_8SXs3INX+VNMS-#&I|TClXaj~syPV@|_`Xyw00Cn|{nC6QKZevR?OVDm)K4vsdl1AAEuC(1INZ=4p*P<gY`1CSt=U**_hj{2t>`($m^=Knb)w2QBj~md+P&Ha!yCkA_#!dHjaCfhyI=sr=Y-?WlQV}?t(KE?>WnTuU%Z3m;b*mG-ci7jz=OJ6!Wo$H^&=!!ME8c7N&fmr#i(P$_57+@14C1`>%!W#42SZaTYgYhwUezFCF`@k+z4AaAdjj#KM4Y3cT7<(PcQfS)ry#Jbu3pgj37+Wmnr;i^Z?~#KS<Js*N57u0stx%>rkVi8PphUc;oMAmRfmPJzJYd{8Uy^yjC@zVzn^hH@rEKx?W-{?Pl4ksi_BQ>A$3H9J;{9zM4jQ@(VO);~b`;g}5|WZBpnun?*Pyi}%FR@aB-r(M8os0ZH4ZTBL{BWhOx2cGKnK^QP1B<zCo}U_uQAvsMK)UvaHz3HlL6P{H3D;DMtdK4(bY`z?`fX(@VTLt`;AoZ3rHWY9iFfL9c_6eMF!GR+~epZ3JsVSIPJWR_U6@G^uF?wsDPbs@|+nfTMKgg-e(IW+O6B=W7P8$87rS7m~6+e~D=f~oZ7o@Ic+;v?>bzAQD()Yw#W1Bud6AWMt6b6B&nKql5ZZOXDB!P8#ZjW#*muVUS3!-aZJ-ga+7!|ew;qmR)59JFHo&snu{^XGVD0IiA?9Gp{M@f`2X&+~;06|<&bZm{YdfEjA=ty<*gjQK^8SY;8-wnddD6Gf_I6rCUAtx?rXVt|d}x|yp|(?qj&?*d(^1!jxGLXdmywSua2lNVG~LsiS<6EUCcs>{F3xh^k}`aWLyxfgyzArfe9(YbL$44by;6U#QuM2@frVe)SCms<Nr>E)PjQ)I@dl0MP|HyV*kv#Xg;)w(Tzh{f9hQnyrP9Lgm<4P1a_wGg<j27Jn)WPPUZ2Fa^v>c{EjYr5}XZkL^xQn`UuEA=|s*!3=~;^viA25S19RC+^nod~`u?7duKL;0i2f9MbZz?<e<PWkUu@>e;G{0n)n6~AxAMniZH{0rsld}6!<O$<p}6>;K&Vv9ww#rur^z)jDZ{(k$=F5HrZTlvCWyKq|;Zrg>gv#Sd<Y&V~<wQ^)d$H5)|8+jhG@>VU-wrX>c6@^!p00kS_PYk5(QJIJ_;TO*=$HT7o`A@1pN$yqO{G{J_d%p%hmx@1^18evu1tfR|>vdY4yutfnT)me0?YHiZ%KXk-SKo9-=CT=VpJx~f;#Xth`dsqRo!qUJOt<k2$yIGO+O75)7<4gkNVD;vwc3V{A$>F-wDF^hkA}BbR~u@lLf#WI!<Xg39&9_}t%T^6zO9ptmN}I2TSNTOg)cNu8jLFjC`c$clPAfL4>)Gz#HUE-bC~Y~Rf^nq91`sq(EzE|axS_Poh5YtxoJFbV=x(N;t{`Gs;8zVL6HWQ<~ZXRo{-j4G4~&_7~SLpI+XD3yTkly#<fC@fI$h#7VNYYkcj>AsPEH4n3saRBsu1hcZ^WS-*~kt-d)X?Egp08dCA(kVX&syU{!Fnh(4gCnND10&QOlIhz3-}ox)BbY&T+M%xy)LFQ3X-OxgyS(^^k`Qm|2cYr8@NT6^R`#SD4F(yk~zN4nZLvXL`m1qD&8%8OxQ1m5Kv(n9w{D|&@TMRey|R2JFAzEwHZi#E412sskFoHw@XX}%T4xP?p%ycMb-+blZ<t6dQT-<vmK7jB}JS#c#>Y!nH_Bf*ZN*JMSRtAP~d1=38~1l+ph8##BK6I}Y7dkJ@S;j&ub`g%0qHKtkqat|yV9>hfWZDmdyrEVpJu|SFBr8OZF(|HzLTzE4#>c&>nZ;hN6IzL_!a_09X_}hv8&$HwWmmDV7gVlry){!Y-!>E~=**K*(mFy+KsHkgzbH~TMcI2z+t<RAY*Sa{d9d6oO;~}$4*|fUt{Px9Z{3JKWO~#fZFQWRNNC$*0=?MBaOf#87BP4!5)+UR7s-R}+XjvGGb+94N^rArKc`_?lmIC0;Z&o`|XE=mVz)wI`>!jEjISKl_cNlfXfj5G_jWLHmPk_k!wg_=!_h}A0MaWHa*Uf##<MX0%k_xB08W$h>e6YKEZ7;tj&9z_!BTmi`B^g8AsS7{>mGF6acQ*9y%;~s}x0_Y<y+n5jwIeFK`v0=`Zp&>XNuuC;eMJ`9rVA+o5CC38k&?<JN-F6zbup4vC6!FZP67!cOCW$o0wlm19h(o>$2HrrecAnleLHXaFy~L^3-%M%FL95^M3Rzv+RjW{mx#=a@QCp6@bK{POW`!wEfwrbHs@Kh*;q|h7f~uO4!U8;v;35!sw$>2BXe=rQcoL_i_M6O*(P*mHnSIt{!Jwn66<_H#WJCbd`r84&Esvv$ZEn{NI)yJg0dC1T2HI<3e;lZA8})*kJ6`wtI9I{O(gmfVYeEQky=5Ln0fUz=gVVZhW2EUuN<sOU@kpYq{y{2=^j=tSm9wcq~^{j(1=jM(3*VmAlVr4t!~F-U;qL8tF;Pldv6l4wP&j*nBeAN6uMeOkn7F0ltr9ltVOc5W6Wma#kX^_WvO5rbx*fsUN#$7q4ElJhVaqdmJ^EUebbAttMu)Nk-C{Ap>Pn!)vT!3h<3HW6Z*W_Zo4Mc-@w9gr-k`Qp|6xQ5*;8Z!Ojz8KA6HyWa?3_!YXOcMg#}T2-oPhFmKdk4AU|Pad<KQbTAol*k{MOX*x0EvWtt=*@gFRayj(gp-DZzWXG&FS=8sS>N@nBz2?l68WXxwu_{oaNpkkNduG%ncW%xIwYp38L3d?9f=1M(BA5+sluhrVOIt6Q8tr8LrPo<>VG}PyhDCsfJ^V){hnijN;Xm>j#=nRE7&Z*^J^EL^nNiL#{8zb;_LqD3kMd}ujHdXn$}~yA9}M@Zq~AxcHcY>yS;evuts2pFBO1f6G5j3EZy6QiX?otEe!K*-&lj^n(o2t^6TYyXkvKEV@)kF{v7y&AjGV2RMO(&l2PE((-MaA=P{Lo0{urMra=r?@|I#w@M6*r$Wc1qe>@mMlbP3-~G*iwqpA9sg%rX;)Nh3OIL_I5QK!3^Y%Woktn0od&J-4Q#12}^JuHnCB7k<Nk*IhRu0rNoRI2qHt3mk_51Q?}bEtaf~X$?QcaD{M+tPf#IhAX_|oxP)f-@|h<8a&4AXANFk99P4!X#`5ZMRX?u5b!V7$IGu3|9)@VOF&^N1^<XL@K4i(4zG--eapow@0n6NS<9W_g$bJZQ5SlK^U)cc`A*QDn(XK5%`<sjpZ{$(uOqP7w3$$2h2tR=d;1c7d(!5Xdz9uBx5xkt{4~{Xl_o*CJAGnzr%wR63x7=iCIcq=+Y;mtpFVne8)Z1!o8)y{2_;G>tI#|f2TSx*@)^SExr4=<G(GrxX&-(GN^+Lhp$4AM00+DFAy<eZn6~+0RG+N~zr$q=FlS4CSjBjY1rYYVdby}4x<Z9@ZwOGJE=fyRlRC7GvI+ru^e}457xeuB&%E8^NRb1UG2wnLPz6~=42tFm3fg3L!ZubQ&%7nK5R}hhZGD1++6ia*tM}x-DOVFL)hClV{ChH)HgMm8zm(~)LAeNtv+_@}9F6c!jbhqJE^V(wEC~DsDYM(QRvpIDn$Z!ot^kwl*CAzu1PiExHMK*Ro6gIwwW(7l@y162{t+M<hO8Z90FhQGDO=vhm_ab@znB>?RGb21eeX(40bP(ywhC5Y7g8p(M(M6uS&!z9UL<mr-__8@0{xhe3W40)vF(tDGn)Zz8ErG4(X(Za(}99a*G3--Fvh5cd^>CoE$~eYuZi7iV$9q)G-Ri3U{lQb<wytvJaEAdLySulu(_8M#c(k7lV9JQ0<1gHr`P~!>9r^Mk;%tqhP$6&4cYj}<YQdIDsncNbJQF^1rU7V9OM2c5b%m>!6&np%e>ho2mU-z3k;ruJp2%oMOdiF5f!SM%aCoRPPKimZS(blLNEZjn)fz!{Dtfac1jQ)0b0YL07)$x#mZP=`4SamOsE@3U$B`k-DXk0jiu=8%KN(HUP&O-$uJl$C=0B-?p$$qs8@HGjGEl~9U>VQ;?>G5PeipL%VTY?yyz--*=T_u!%f&#R3jRKF$_txEVQYOprvH=Iu5Zx9hbX8oBrSI&>tz4qtt3lzohswxKN<M-K_%Ik_5gt_9S~hmFubEfM|o`X6;rx_IM(-8Y_>eD(KI8XmDWUJy~Ssg|*MIIx&@jI9TG*F`wvEz2}(oHXBFpnkZwSKH~e>A&K!7F6d^xztkkuUkTdq*6jFdrArIyq0(5>DqV$Gpl$qTB~f7_;Rdh>nN?tYwwW>~GNx=V4~<s%a0qDVik;D9gSX(YIj-t@j;X@p=%0d&)fgZg+v;-ReaJsH)N1*VkFBSV@eLq|hp_{%`qJ@QkZXxrko507jBV4lsxZd<r1~6Q4`L3_NE4!Ga)YML+qUL&DhH)u8oZBZogk304}}UsaR-V!urr`QXcGVF#On(J4*;M(opL_I;FJjAgjO$aR^eTuM=MsA2yF_`z(Fd^hC*wthbyaxE6ZeC%}(i(6@ZWUa`c07HoVaay1A56CJYpdEg|8cSbmA*(2Dte;jZ5(-r(0FI1XKc-U^><c~XE@6`eHX@Oi1Khhjrj<H{vS&fKX%uYdv>A?2H<Egla-GIP$y%&pxrW}cUb%0B(&7SaYK0)RT=Xd*NZKAPC#%HqN2n-9a8(m}5QohJ4Re>6Q{?T-P6HzxuU62tU>5>-E*|5m^LB^kjn^n8}}yH6=i_DdAsuTPTMc{;a`{bO|Hr3x}$kfIP#K6)Sud}!+=t_&OAd|>Dw{c4Y7HE06E+_-hcYa0NWbWL=u5qutEz#lHnFRz9ex2+EEn^^b};>xDr3sN!H;UjRIERG&M(%S^}kvayYKGNtUVyNW{t;Qw$Q)*tl{A}jZohFtcKqqb9Z-_w;vyad_{ymy}v`*1<;FV}H3n3u`Ov~X|U<*D=Ou?9N3#p4Q(31Mn3=|KjntH>u_v!I?B|?yiU|Ca}GO(A^mW;?AjKL+)RG-VdFX<RF+>;fZ(gV)j<V7)=p|`hDQ=}nqZj3MhJF`o;zD#BihTvwv2*XfO=fgm}Yy}F+cglasMl{|2V+cQvnyV~0r+9&%&y|n#rIYeqF$iSD!Mihyo`{lOUz6pd1yw1;fT2xWfn;L9$-29-QXUl->vr3rHs?2JQ^a$CCbzbVn^dK`TWu*8bCXEgn5Ps|lmbRr#ZTr1fKG`6^=oc*m)00MXhQMU^(la`E(hjA^ZR_5&J(W;1|H935qj8P&qu{ay6qkoeC2QxuP$i4sn`?N(6byi>Jj<HPuT=eTdvjeA<$*oKOIsLD|I);vv}cLd+ZhjYjA>J#4`GY3Ggz@f2CN8crz+H^&@o33j_`mJZ*)NDwyEtKJ_;PmaoU{SWyiWu28><A@`@PK$d_wsOsI?E&{Z<)zF=_k}kk!fkV`qZfYfmOcI=@Zw7-roxdYFZf+zZ7dPy9(?GAy(5+(PFiI;L#x|jMn|RWJ(YQ%XQ54u|QAoyi%Tml^<A>Q`{@X2@7O`Sug>P7dg^|=T4S1_0y1B+S_0ZyDIo_IJR&jEp+Sy`5qp`g@LEb7arX;K1S+e>ab;@)2YwMHqlMlatG}WTK=HR8a(SW9mLMZ9Eg@llN_iprdmiE}!GD?@g-7I5(h%*r|TOubmJY!v?`SA1{15qa^-%VFheKCbobcEqJ(2o}vN-nfNIuOcamLAzlYLj&O-PX1fGv)Xb1}L@5wp-iV5vM6JOH*%uVy=m}6-d3daX*?&)8ay*sEgxkC(fd14$yUJ@tQ`2B3j2e6J)P3*t!w*g=IS|yx|q@UmyEY*0z+g2$UAIs0Sb2=Eg_FIE$%Eqhfu@N|dO!45?X%&Ef-yX}|kdv&q#lP5|A6axoebl4w&_q){P#;=Lx}!v#Z=_?wBP=BC9r=}9(bo?pqymd@JL*`~qa?-&=}sL<Sy&D;?`ObdvYV{=Als1FnX70nhDhtA3s(7+F-TPIE(uU7bA7=De^d+v#6o+l|Euue8SM=~BuqzRtC5iD!rlec0vMvne+JV3|372U_-i>7?DZx(&;7JXk(REI+*(*om=gE5iC&8m6!!NACY*K<tBO<KC+<YLO#smAAII-O0Hk3n#Jb<veANv76mMSNpLMq!j*L#nM&i*K4*VKKzi%YI(QLeO;reK#X<Ccld-;-=hVHo4NxfH=9?Em);W(1Q8f|3_s&x8fG%tm1buy87?XOVW#zieNnV3X0)TK~=`R^qW1s{z9e$ASf(oU3XeyL%(5!0E{}D`7o`R`ffzem>l$3{YKmKhJb!YZrC=*8m~loxt%vvc>%#GkJE!|k}exz=-z$GVXEeMxSCGphLPDX7`Yf^;f{8xj<CmfA5t~r-74^oT2`;EUQI5CPg9E%Nc}{H2TSrrqv{XHNM*}bAgbDYLe0%vemfKxiO@|R2pPvbefCrL=<!q6Kt@1(Wb&!lVOm_Ku;$h_imHm4nU;M{$!#jB_?ubsvyY3|XL(q|yNUJ4$dJ(eOIVwTyzj(m1Pl_iom(1cu4x?s9?-rK%iY8MzF%IO@cu5ATg{r<D{k$5EH|L5l~;lwzK`XObhUB@!0ebgiLaZ6RX<Osn%g2bAy#M3slC-~Fha$KaK~Iv46Pwq0|65ZCw#BO8v^h0;j2fyc!d8fd(>Z0S;0gmEEn3Xwx_8zcQzISxHU@-2yb42Fyn%KD<fhJ*om3a@k$UHZY5j(KK59Ap?Z1N1~dZd;SXLE%sTitu27+)EBI<?DNy_>O-tcOGQp#M?pQnH#J{w5P%GRb;Ph_P-L)-^WWE1ZQg06RHoNh<lL}I$>V`XOrZizM^=~*Q!j`vgI@jrqzleV|oI-+ap+R;K&{#tnmw*~;SUA_$3RW=CULihAEdMu+n$kstb-Drj@NSWC){Xy87!6QF0Lk4-z`F&|yB7Fjw99qYZONQ~tbedXcf62_{v4f5rj)ktNqU*;k6l}?hqDwXv-@I|i-croRP6Iy!PS&HpEaW28$t^h$KEN7KD_KNkLT>*Vc-AQUnN<g)Wit3zSBjIP&aO%4e(}cgID5&p*z9rRMRU3CgB<Bfv6@KNk+*$!h<)1c2%1=MdIqc=vY%xwZ*6Wwmk9D`PEw@)_`L35TS(Zrl8dZ%g{|llu|^7M(kZ{Ji38kY>m2j?=}?yihzpNQ9)tZbA9V8XE(59QCx?S(5S@^7R>RtDkbFwy59{&rPEZw7tGdh<Nbi#U`<Ks0l4^FJ1eK4n;tVs_hM>D0<y1CD4E(4|5#;GRN#cx3?JSUrJ1Um|FDyoaw{Xe)RkJ*JAE1a|3~TPaEnuy3CGl!6NOh>HLO5eyIy25Z>2=`vBvyhOVajn^X1rlVP!syj1}W;Vg9<AWy;0mbFtO9QOiv6^Ql1g*2N7U7(?<lzyE#ZZYf5$Zy<O3a=I%I;9h^2O{2%-F=d&@eZOGGmo|M^q?nP|#_r{1h2|6bfb37G$ZU=0O?I}a(tSy@5IP!aE~Q^v(Ltts3O2eC``yZ?zU{^t3P?!(#g~tCGd;?tr&Jd2!RW4VyFuP0@^q^fzS9ldL$<7&G3O?y52ed-d;<hpHw`|n!koXb+$*{b60UCqdc)Gp8{|~Xt!B!WJt!M1!*>=x)P1bUmk8Y&hI&@D+O7LrY@mfR&^1o_3cn>C#9<b9kiUjHsA<RUtYIhS^~YFMB|R$P>JBe2Kv>hoShFh1KHrq&3K?O@yx1U@hD|=m7>&sqo7Z=1;8@kH#}XiBDG!7-OXJE=oNCSs|6X~s6+Iy<gNUr0&FdF9!|@@HPiS|w&%Sxmb8e53OxS=?pPO40?xoI2S(z`iKe`Dxs1fd|d4B7*Oj8NF1>-`mQP7wW(__m+cG{BO5YoEJC8$ez%yV4;i~u%e9+LjHYUFFS#;V^3WT3KR#P@QmFe2>haiR6@X^;Fa3qKo{9l=5<8J)6a0sKL4P4jf}og-ga4z~uk5RSLorud?k_9dQ6F2#Z5GNbGk4#MHJZ?7!NOegt=O<*aPs2_P4R#Cfw(SYcsm@<PsZ!(U4d)Nj>I=@Om+;=E38TT<YFa`_cpbXQ=Xmvgr-^Cd4um&VG2R-|a)*Y5?Z@;6jbha{^FJ|!0Knr=jS5C2SZ@+088;%{7z#L-9o+FT1L6g;X6<L)#^Z8p#+79{~&fv%1n@V0gCN$&4H~`-pYKY<mYgteBhNi<drytF3LgY~Vs}i}{{I?|X01Nh|E8Ek>9BQe6wN~9!pk}&xr@lGSJJZo{k>I{4KYOl$Hs&|hGH{QkcA$5~XiL4CEY!Dez*7{7-w6DTXHku!`kMQSd&)lm?~de<{<ADAMX?P%1A^sO*gF(KHVnKOze^N4n@?KNiwT<MM#p4}98qd>kT@sjvt&BVdZ_bh9wgHUMPDGUe%3=XQ+WxYEONiMyi^brR63~WR6q`>QqXmU^j<R6E!n3}&O)%Y|6P$&qu-N~g^CTWIa9mdjbBSajtDN-lPJeSVT4#VFalS+D)_5f4i$#|wHH9R_XVDYzZ;H*WwgB2ir!4op#!N{8b@zFm2u}VJe_ULh)Odwdm-x=I%K}v_e;Fz67RXhd*gf=Fo5^8jO0GShU^Y|hbeiLEX_l3+4)&f3b!L;gD5B)QQo4gZx}{Hxjg6{BAKNp+NN-xjO!h?j+0jej$Jaj_H=gLx3&%A9DRA*#leHsE()ct2xj6e(=cfRQy8jQ;n+6Ys1h`Xk7M?oK=3VyzeY;cJ9_*;i%L)J--d_*C=nzNd6K>iUDGOuq0!_l8J%2Z`TQs`LJdz_{N;3xpHBPfd8~2o+in_`3osMT-JR(zm!X*>PL^qMs;>7~LrY3e8zo*zQq$&PM-1}(b8*@XmiD83v7NU)YuBuZm6Ng`Fku&w8L)bAmi^1LFhkB?&%Hin)r$f%eKx){JvU?oqC3&tv?vWRMgZt>M(zD&ITZg+eweQVvB!G0Z%M#!Js;biB~}sQWa;wh%r*HG9E?*To#N6v6@Hf#myE~#DDrJUBLm(Rs(D3O+-}HkMR<6ExIo$1FfZ6~FM+wPUsC`S{QnUDgPC=f%N_iv9Y7n-_c$B|&AE_JDn%w9x)W6-wZXl&AWhatn&MIc3DIP2`a%H%k<ie34SHxQc0(>>4dOWs?ujktMof%r)$@V2Sv8MMqvJypnr`Bg+jLvCY#&~YNa~v1iD;HbnH7!C;CNghvkH7(!@UC5i#J~{jx6CV6-SCN#>7ShjmUj9cHar}&~<@J)`3=F!td8X*SJ>D%~vLLr|9_WfG%t?7~#R*8lS8=csn%QHvTV;f}QY@JAc0B%<V%CZBMq8+X<h$v8`8GfBhy=m4+*Fd}(-d_G@yP(rz4be3W;<)5(<x;3piV)F!b@Vjb)Qu`R=USFJmEp=@r=#*)`KSbLdi?oI(dWfT(oQ=>@G5My66OP{~H75>XONa-RMEX-f(`h&Y1%`fq-nkfKQ^rgI&CtAB;w%87^srFi6&$Y6_rV{6QycUdA)fiU$WAN3N0UVd~&t+pw!H5(%TKVGZO%EM@Zka;AY$Lt4c|f(<n_gt1ix`a7IX%&-Y2SzT-V~7Z+lGjU?7-bGN~dY{&WHDI4ZJV!kaP5Z1&AC*e<n}oNKH(HkuS1d9woim1RjMGHP4Yc=;w<Ist%1Dxh|6O+sm=_sgfGRg1b>{C}Xy<QKkbjZHX=f<aCCyTXjTht5I}{w6EW}opDhu?1HFdc!`ciuY~`%?_Nq@lO=ui(NonL^+sx?D`8?~+R-<QjZ4WdiK;x%V~MR{UD>XNy2c|tzStV7Rm02c>84rL&FayZ?JNK1ee<Je%K7;DJ1aJB&Vh8qnF}}Sf;c<c8CPU&K#s#1=0(yGxmvz+0=|0MF(b~ar57{ZxD0)*`2p2c+DBNQrEPl;=h+G!fPqJTnT!rDHjyvdu3&czPx1|`tvk}-AIQ7YZaYye(tQ3ab@nF|yNnj@fZ);HvZ9A9Mx!GYIR-YK+%n+(G1|fi3Ngji@FUE)uVt(oC-4eplz&3euT`>ZGib^!QrAlZ#QtG+k<H(|H??@dz$}zvJ{IZY3xc;$hIv`W;xmJ6p7Q|IV7{}hnBDC{bN(2;CXAj6&k1GKXjH?J6}le_7^K+H`%Y=)m0Q^x-wUD`i~@XJ3<`#Mdd;A=6(}*=T(U>2@s-%99xDETnd|qW4>AUF|618n8_uzN=7Y+#k<7+#d-J`3$3A-a!VGk90RS!P004LW!W8{Q!bG3hYA|*5fORlo#Q9!eL8)=@lH4<vXG3QiMf%#4Kg{<$FMG!ChRIbg_B4}dm>wkfg_%UdWzl>3XT#;td-|uEAZu^lbDphIYA@b%o@FVQ!|!=-WWtQ^%p`63{HJun*{u~tk)y{R|50-=<d^)nVMMjrqkkJl2%A0nS7m&`-FJ`wG~5svdxp1_<F>V@ep%T6%|*W4J@(Wul{ZFCUtlH;A$Tw3pr9@e_k2@3$;9^}*W&Jmli+99$&j`I&C2ynsuL^=w^-%hp(JqS<;Sy&Sm)<q4p3fWayg963_ff6gYH~rdY|&*SR&SR(8ti!T;b<z94Mdlm$8`|=xrq=VM$d@-659M4O}#um{y-(7ot1>!Nk4#{HA0Q0x-<k&?70Bme457`BC4G3MMK5z?w1j{bkYA1t6GncuuPx|1C=3lhYOeZ0Yfw*>e4wV(X%4ZN?!y??(@PK4zE+oU0V5M$$|p=-oL+(<_L3cYQE|ZjfYB;6eqp6~l>C53SuFkE4K;3PHwz)vYTiPMLgl;hsI|^30Ce1G`Z8AjYZ+N3zYv$CFXkm#(*J_zw_E!VHFU2Dy%e75qOYWU*j7+X7e_3RXlcBzIfcuzQ)E5eTD?GO<W0T-%k`gDvJq1aX?|>m5kH&5YAGIh&Xz8S@)vF>&-HfEYg_GnG15c(jCxiRJWM*<T;g?8I`8?9flnZowqCr$!|g*!8cI*{HAI<K<bu<!@pJGWV>fhJl?ui6dio-V+FtuQ0jAt27z!8A<}g6zK<4p_gMW6P!d{5zuMXyW(0BW|L7)X;`$l2Dsd#fAyPWxkvvNF&PSe`eHK6t|xG=9sPDZ0&WIOtA1l1gEG62&;e6RIOkz@w%T<~f4C;-AQofXVUT|d+0wO)U~VuMLW~23&Ze!l6DyCB35I#6X+4#Xoc3?R7h#L76!!I+?UeFSi|Nrch8eX?BJhm3UXn5a8ZvGW1O@AB8)U`UMkOn($=9;MvM+$c-mfq`Tr+G*2>sT!Rn8zv>V%wP3kO^5*;-j!Hd01a6pVYKl;ix%G|j4HS39X_kDC1_n;7>Nzqq3>$2ab$QRVMVKkKbnC4prQX&JxVYn#F<cteww8~NSrWL5o4b(7On)pJzk6IAuH6G`08*7prE``&9szoutD9d^-p@|P^VqTJQb#^>2Mjq03F=;UhBe4FH$HQ*_Fk6?Z-+<-TtgJhIV(^>v4lKUdjp5sm>cUZb)$VG1-a)xsG9>e0kolVZ2;utL|@ES`$SqugkfZ6_{PCjcs!_g^ST7fhD&nJ{{-1y39D+aE<7eKeayWsJ>%zz!Z_yIYT2k<QI2P?q)VEHWAt<3JsciL|HBAscS)GE2!LvP`oU8eqNHt!A5B6D+xU-U&<xV>m|Q^kJZVC#F)2OT<P7yd=BCDy<wY49SMZ@uiN<2js^90~BkJe0{L*4Ytk=i)>ABgOuKU)$<eN5AZdw<cG*@WoN=z^lb*o}pPUX4<toLASpp-B660#WP^l_~SveML+x#8RbJd!z2u_Uu>cKK*xMRmOSvX>%8pZ%T4Fyrn*9dUMi6E;$f5^e(pq+Q7QSbMZY`rdl!n_!6xvb)1@z)0Z1I!4<U67NZSUa`xd0lGDuy9)HNXO7?3*LSpjLQ4ALe;+B6{DGa+?MNZTePEBh({4HLs#SmM)^@8kxP%hgc=XV`>ZHGmK>2f-kj*;FzR$=&X1(``2V5dbU!eXL8@5gr_^5a9j|s17kgls+&Mjml0^?g?Fx*1<qO^BSo`n;0=R#j)IhP8kJg+M6nz4!zr=N_<=#&^4J`bsb_4CzDT)=fC|tt*5KBArh5JJW^b*rOIE5qiaS`4t{6_%3!4nbYy{!S>Re1=*j}!k9KYWJB-i(r0&5A{=2qg2n{HH&|tKWt;%25;+MX9UrgVzN~Zxo-|L^h@f_>JpYq4XhA=<K{rmSdbKtsILDW@BA|viuj`$g1IzKGa#O~nF_l7<S5hPyYh45g>g^d!F4uoIhwXgv9&O6T<D9QmvIiM(aP?QsjazISJQopXnFY|1>z>eqG(g5uxa_rz>Wj49Mj`MqrZ<;TutW^R#&hIhJG(%fj&G4$RcNAy6<jZ}2B67}G;t5$Iwl5w##I2fjYL1Bz4SH7MsY6fK;;H-5XoObILN-DxZy_7GPmL^8Bb(gF!fIq;HL?gc!o7pR)6)(=t@e$@-2~j3%XVP3F|gVg1lyp_0X6c|J?n}2gMJKbv_U3-#^>3HB)eI1Q9mCY%z?5l^Wz!jxxzm-SG}avD_E+<YLDY#(obhxvGvQdqmyUvPLE$ae)>%2w&X846+50RX1%n2nTsZ@BBCn-;AL)VX}AQ)FZ}gwGUM0`1d2Z%ym|HZ<>9l_<CDiHKOe{TCJ#r2RyvzaX7$=H#}WP7tI3)Q?91_BayU81wzXE&)lHe^M1xXnJU@E;)2nB%PuAjNkV{+_<6}?_AA=j?<N11g465Q|$_E4!Ba*VLp(XQq(i@7AVI`!8btMLN2{@2^lEAS*5Iv%R#t(zy?}sm6|79(D4xyO<f&^fRA?m<79EsOhHn0#0Td&k{>NuS<8Ofgchxk1U(Oj*rPwume@&a%mFE4;6@$wRQ1TQZENAGZfB2_fr&(OhCo}ir*NG};*Cb;bSlimWIWN<c~jmTf-$?9dlUOOK(xlqj{2~iLBO7Rox9ZbgPG$S>@V&|fxvR9~HyGqZ_M_r(TKcWP-GB~g&Xag`?faH{nro&{9PtuKuvX1em=(Ev_^O2@A<NS@~_Cxx^(w^M5BT?|^Z+7u~L`YrE({T=SQm?&vc6^#Lj!)^3db-HQ^O_xSlNX+YOSx+xVQ;qap!L^3U4k@^Q;p9e0yPlZEbV3VdYGLLr)buYD5Y68jxN*QW|W))+50bn)Qy)^6W#)S2i_u42VNs3%h!u>21m#Xl3Jq0>BZ&LIQ4Lwmu5$dw?<F!EknOFyJEgJ`(nP&7qdaqOOK2`T}~)<Q8uodx<={-9=*)&MBER0ZS*JNe$Z>9KauDMLoqrO*&U(pCYF#oPo)h33Q>qCv?WY?TXpJCC>X$BExH(dCAzo_(ZywuE-r&~aT%tI;8aNRphgy_Af^?3K}*Vm$!Ibw_|8V!!4lm30ua79AEHfmQ32T1lF=yZ6@4E9&%H>dMW2^&gvH1OMc;d)Y`X6IFUhFr^EAoxvg#welsg#$V{z8f7XA>Jkt+a^CWb>_>I{W^f{i7C#qwm3K1L&8ctAsiE*`+|kz3!^wxL&7g`eocon0)pD`H2wh0*pel7)f1NtL!kRoY%*H0p~q<oi^tOI4KGK(bC42HHbz;eDM_jb-Se1w(0YC*gpOx7bwnE)_L`ZWO@V3BUtDIF1IFYKlfN5<oi)g)@K{P`EmdPXpOuAondGq7Ihy+(yDYjb{}Ji$iXD8CNt_(wTi5?Nc?WMGx?u?F%Ug1=CtTwCX<q%x%ZyM2{S#g{N3W)M#~CS5KJXgUVdTt~W3Ne!wvSZI@s8(o1IjBL7>Xat8_1sjYE<nyIEJdzZ_GVG8-77)|!j9n?Kybo}9TQR3!-i5qWdMm~_cccbGeux-E^U3PT#BD&#@w249VTa)hZql3p!qXTp^Y0A5hgJkN=x6#4Se0Re0Jwz96R3QL?i7_lOrU#D(wPfAarj1BmwaN6cyTX}wblbtw2J>js62DLUW;ay&fK<}Bgs>S3&;hHFyNaXhZj%|v4krohbZw7o!4tW?tvW($7+hT72LaqiLz0f;G%Y2w3RBkIvx3=}L2hJV8y(XIL);WkS;6$+DA=MxPR`2etSBV{MsOGlR^Z}<&dABYSqE~RC+B3Rl1}R!1bBe?ZZ!=wO&S0sZ^iyZ4Po$lt^(Y?vl}<mmeDq5y$kQT*PQq?&_j~ZX;7VA8daC_ZDGIfaNV+57hMyge$@%4QN2bDHr?oE*J+&uBr6Ib4EQYReR>WO50nIH{`C0_mMc6%r)(}P%f$q=`Fh`J>KCgi5|bq2-EH!)V|NRY+Jvd@QcT<(jDg$Q-if_xUB4R7P7~LW*uTA6o1t3mZJs-hTO3;vwV0*`gAP0H)cccp{dEI+9sAL@WZAA$wp&tm(<!^D%9^WF-5j6Hl5sv-phi97OXa(qUqsv>N31k))}zfLLhEtd$ABHE4Hq5xB@U48V3y|N6xRiMQuDsVLJ8D2q!F~G=mePSi=~DBL%bmRCD0CDo4gaP7|40C6v$~r+bFHj8r#}7P$k+~!V2-BE+6BP+4uH0^PHph82fc#o1uAmY37+lp9YaKh3)bi6e?1Nj76@J=1~*<<3I{NA5E?(F9~|U-0e+(!+vjprv;hiWEl2#l#Ej`L9bilzG7#0->N`Er{+Z<7_0J+_MW!2Dfk%d6xN4rmQ(G$M-q}2*(E9I_U<4{+jaW1WHxG)iZH`7GrsL@Vtlx`HhA~r$8K!Fp#N>yz1$_fu(g9UP?u!MEElf=h<+&ikuwaY0UtMbJJ{u3?BYEJLnI-P0&{Q3Sn~3VC4p(V%b})+1$2Wc0myeHf>jGk7$c7YVSu2VPovS|A{$Q@dDL4a<L3Ef)TeDBgjd19x-58*n6k?_!HLwpCM3raiFm-lLWHIQ{7|F=7axH^dqd-#rQ}l#Bg!u(pH@+d77U~QT^tY)J~Fba3<m#POdJmXTnF|y$e9WYat_kpk4pGr>Lna(cNJON-2L8GfUJcIL;$SbVz<k?jHJXp`w+Rk&C4kct_a->uZT9Uh_1aNy6aa2woS7ygimip+}kZ(PU{JwBgo$%1Z$0TckSbd!(g?nAYc-sxVPgnVtL>}G`BnMqFHKrY)SHu%?@Z1x?6EWoty3uH!52GxU293N7_dxJg!(6FUga?Y2)M07(1VMtze5o!FGHTVSEl72b`~>H`C;Ai!^%s<fwU=%~SZW=w}n!<V}vin$Xc%+DG>Slb(TEEmac`X+Sk4*}G7%gv0~|-BQAkKFy4AQ+@)y?Ov-I$LZ&XhOJi-yVh3hDQ=7|De2Ze43~}8Yf!}6xyJ;z8+%$MV<uVb7$vK8Cc@KTcX>6nJMu6i6btaQ31^zl_I(4G=m)GA1;rJ$Uv$c4Dj`t~vvEe@9e7OlcZg!Q$TmVN8vS~($~yr`tfM3`1vw@c^rhO4P>IGOqTPVg0<hN1IpTqY<H+qGB%#Nzc_7218|%`<;apL~CcWRhCrF_|O?V@lk#0rHvBv0rQG?rTby>>nc3r$9W==A@Ps{-%y=eWcry3M|L{4v1mjm1&hHY&En`#rV_k_&=TaN@|rj9XR?}SSUT=6Ew`p#Y23ji-p_SrJVEJs2*4gBpg=C+U~9mZU+Vk9`67G|UZsKH?6y0=bu9&_eu>#iU!^FyHBuY5ICe1jC$d47$XlrI~GaW#QG?wNZ-Kqp@|7-J$FKw<pj6;OveUZtnWd_K$0K*S8--TP+T0O@am3qt>+c^~9|t#(~_naoyr!1M2@oG(T<<(I&1mHWx;qWkSX*%jgq=;t46QvT~Q@f%(yR=hGauglDfE=#A++t}7tg$uHEcY`+gf?L7Q{|jG|1+K-stFVffU!TA5s)$tF$+;yt$T_(uP88x)U4D40e*F<{k_lkfY<Ra~lND6^!Z^oN=WE6NE%f$PmCD8HVq4MdXpTcSXLR_#iLTa?dVjReZY=Y5+jbePFWM>87YPC2hFxLx;ueeVl;qD=FN$lRt?dH!Vo(MbC^5&Slpy<&RB^C&qibq6ES*M(8hdoRbQ9`Rr)5Wj00R$b3vkfYRTN)-U8L_?)?VT8fx6Op8ctS$W3f6ovQY)+A$8!RglwJt=!i!LKdAs$np$keS$Hlb2yl1+!=JXAqRR0rL<0<|+Ue;lN$(X;O;v@)l5^4xI$U-z^15YWQI>VOVYpX%w)YKfnfaq(Gr6Y^Nmhx0Q9_BqGCqoS*Id_(JUH&@*>sxGB^3H%V>sFeGi<~xx)g8-EiWH%@+_@jxow`09D`#nV>)UEiU><<iihze?f;ZcFuJ4iSvkwbeQB5c>@pqC^EzAS#=aqQ2#VMt#coW-$f`rJ#bbqM;?j(`vs)HXa2bp!c($qxARLl#xK!zd&z9DQmHuG44RPo~3fuU#12JOUN0~ju^o^RQ7+nL9^(flxwh=0fn}7cpZBj@T!|O|T&<oA;#0YT&t9rO>z&O23GJnHxHdyoy{qce`Aj+BqgzkXrRQ4`)ldf9e?>-cIAfT`=7~gC>6ouSq0=XISH~-sg?qssZJ~bnBC|bI9fL!$vu|!57CnH#5;sXvD+~hM3dXyP2isK)ws*G>tjc-*xzISWKhb~g9(D>d3#z%vD*N9eXe9jARd@{Du`208}o1=SOZ)$UPvdTfOlLg@^6aXS=TXF02nC^H*6}N21DqGJfY(%(*F+@{5V{%k6<r9=Z%$Io0KrhJ}wyb6+R8t5_-QwsNChAck-y|5#XiGF11zyHMr-#CI1iUD?iiXSbHRMqJaAlJGaCKvPAFjgG4)058-9!<x7Tpi?sSL9U6xFAZFmmljRV+{{Tu7H`h6^<Vr4(d0*Re$lyHwDk1ou@Oh|!$b0pO&&HG$T9xfxsmYKRa`Fg=^nRjh@3w%Fj|>G9Fg<M*deet!P^*-=AF1F<en&luOrFAgoB3s?(%#$FzrK0SK;YhdGFOrgVlEuR2H_|wo~R~j;^N<#-tX>d%G21h(;$ap3Vv>m$oIZw`0NlEL5M6I>-aed90j9%%clp|D?rnIJEO;c*rw`@pXG_PsM!0IiVq98QY@W<13%XTP+O{I1OU94~C+2J#CIt{jmk#Mx*IXq#s5mPi0Qa^}LiZF~t1^evI_V%V>=kE17+<btX_qB(h2zdgve|~-Z@~79&o}RvZeNx~NSE)T21*o&bY(umkSMR{_i#JCn0q;#zy8yr0lS2~NX+(2?v8RB24)KLPdI+mi%};NC4xR|Sb5H1G(1ZFZDqM;~_gT)5R2rc3ua@0;61j~@EeoIHDub--3MoZSb{U`tRg6o;P3AsnPGrBAY{P!5*SG_P)}#H7*N**8QlzG<r|(}sekIuYcgB8JfDIgMi)bNOOpp|nnu|pi+9&WVdon><I8P@baxhNVAwp2}tU@zp`Aa-zCD6+F91cLv(4swO3$xBrsLgm)I*mqu6!Jo|ckWN!d1&6w-AOxlXYAacE;VX%qO71wav<gunemm>cb**Wq6>|=VSQ1p8+tF755{tbBCdkNOKLhT$E>d+(ejto{96~-&iB_g+MTa&+!=78o0H*uJ2K}b3L-^+wI|7t55uv)7(M2EMd2`DqTpO@UCtg+5?V|NnL%b;ZR^%*rfNGkBFT!??QcSETrsbTBiK68TcNXBCH9y!tho?7ZRh#Xr1y5hF)Pr+n~P#dRD@HPs>w!FBRy)((gZ=>*JKi~zAi|FUfnljH?Y1g2zg%Jw`^Qcq0>;%t1V0q*4IX+Q;Q8=Akg*5+8l2xe^ZTgoScnP4sOX^V7Y`_FiTz<W!_FmVJ1p7qD?w|JU@K%_@p5{{87E{`QeMXx=qK;d&BaMzqU&jbR0_Etm8;1x9PZPhFae7H+IQ_jzcMm4O+S5M5VW)6@A!PODs;&B5HwRH|xA~R=9EJjT6ke&L25N3p$U*Dt7*Mho8?nvf``9C(n*vK0Z8sd-Ux1*~zhru_*i%PV;Q^X)gk)AFm@hcw$#u|L$yJdOW(gq;G7G$`%9N?T>hBTbxs9M)VXQ^BRiN*p5Dnpo}RXr#G3;lRbPinz?tM>`nOgZr5&xZAvypV`ejGIiQ+pcV#md$$XxkLiOY#>+PA%-0#r+Fkcnkvzy_oLpDaZXEn346Ktk8nNHK$>Dg>DzD})Xgzr7~yJI)A$>zJ_O5Q@6*~~rF44NJ6X$_`1H(UD3^Iq4P8>0)`U9*{viL}nPY(`vM?**FKHscA{&3NBbGiY?6k+w}F>_pzg4T_>19*nZ-&wTTkTZcqDw)#Vkt!@OB8TjGRoha*nL>H5Oy2l0=m!da(UNyE&42~ZP_73L>@0|{(FZ04%InsZj81CW<2m>+YEi>I?VL10_gS+8GRg(Shs{T_8pIxRVFomw=2Mf%?geuyKXpm>2B`2d-ml4(=&eG9nb=uE3vJ|DswZCI>@Z!(owD-yU%(enM=mpf-wbN1H#r=CWUEp-z!jeWN3h+iMQ5f%k7r<Oc4VeLd4qaY?=sY83&~pr(RWCZ3(j7BC$P4GNvO>gc!W&omZGFx2Uri);8ZzV&C;9p{>x1MAZR~8>cau=@MOj6WY7A;_?b<c_)0uhCcLjUM<f_$AFOdYZWjZ=S@sI*5HlnUo^~!0{xEG*-+(F=W;*()%l^1puGVtJ0T+zTWf5H{3Zs;wq9eO=9PMBsDBa?<*394A9Al!sym@N*5e$|K!B`bxGdX?m#>KH*vzvoRJH{7Ss-k!WTJ$ZI~V${lV`T5}I!^6|(j}M*&zdkv9_WG$Qa5E*($=8l}8`*T$ESaP?N)t8{s!J!(T@`gf+pG9`L#tx@KJn=eZGWB3U90MMW(^v~o5MFpLYz2#^7175=SYoRzl|+TN^g?Cl@pH_YaGP6MZuaa@<0o_htUT$VN{HxHFIo8@k&N@MpG_?eaC~nO0MEY5Kd=39K7dS3#S`~;{xD85(N9Iema}{F5-cjF?}~V`S#OiKXs2DKLsiT4hGUU`6g|3z2qK9vjU16z}D=oox}BVDypc+(%6{>0dr;!xFQDjql0*GL*93?#u1M^P*J+Eu|52!fs?xzao2!5?9spU`vv`e(NL}J>2^QstfQS)^mLY72{*vI?7aAv4JjhLOvQXY(erEu{jOilvU!?w(6{I;h0dlTL;%{OejlrKX5E}Ua)kaxu55)AQ#Yh`VGspVKFgL{gUdP}tOat^$y!#0lQmgr)nX;a!;_nmWHEm;cmloY<1X=iJ&@zEC6i;KqOIUFGyK>LXJ<gR9d6_}wgy!OK&D)^SbNzDaaH(Exf!1;@v<-K#U{tMU<c!_<AUfpW`99LhOgrehsW3|u$+LS8ybg|D42{kECthz?`hYaG(|ru95zMCwJHkUx?m+z8##9I@a5}g$5hB%PWD|ktl+L#!I%^RoxSTD5$8pZBUIYyyEm<@ELo9K=DNj-G<02MD^dg8tOg3W8-jvA+O<;((DT2fD<%9ZbMYUe8vd@qae==;!E}~s*AG=4H&Ew@{(+%>M3Kn-)-sRnw;qtPJjP)`Yb43v9zTX*vjoVm0w6nsDiD<;kAz1rZVgVl{YYr^d~0ap*o?sH-#Zhpc(<Hz=8UQeP)3JRpqWP5H|>CI4SV1b-j{=yelfLJ@7*mtSbY&hIKo;0FTY?0r1MG5v2MR99PLo0QR(ex4o*c=;VTLADpM8Jd!?KvbBh#_k8nsF@2UwrA2?-S2sVg#cI%JO=OT}wgX3s`ZZ7;n#K6Tv%tPXKvAHYigN!_j7$2#n=Wry(@5e_6r;iWczIaUg#GBX8PG7xz{qymudT-a&Cns)nKisN$J~B)67NZfyDZnz%kKVjKaiGJ7B4QrXR&)YP@byoJxE<+jq@nLSc^@lk;K}2IzkF@@1!q9pbTf3ZF7Hx9dM^DzYl|MRa?5tGy8U`_L*|7E**DSHx7#m4U})5hkoABmd{{2>MF;cZ19pK}7>F~1c&G&ICf#tg0AGj7u=f;I5<^J7zzB+IIKpHyjgHJ%DgQ-#x2HWo`ilvO9&;-s<Z*hDH7PLNG?`%#3o~}4j2DSfB6ZM6Yc|Z>eWs3-JO)mQ$I~?M&HgFsn{h(SYJod{o=&6C_w^f2tu}XdC%Jgz__D2I&F1lC1lFxaV6GX<4d~0Cg+{=J!=|osPO^>*eGVl&1S;KZ0ZT)40FC~d&C&s?Xd<+I86_)6;drIK10~qD7=k5ypXJh4WFa&{_4q$dYf?ghw<kVJNnrBns@j6@>@{pi-Q@JjcP(Xw?(bG9)UHsd+oeLAo@x3wS5<h{LH}U73X8n03gI=TSJYN3It02$MMm>c)P2gKn?=x3v9O~0pDw4(9={Z6IAU=Jg*Qr~xF}tZziB?sCuJS}>&3-ib+7;Gcl)p3A`_>&U_;$AFciuLeKI-j&C+ySzgoiltl+=v25XPCw%AF6g03-8g7XPpq5lg$QI5W=m3ZQuf>+n#v18|4>#YQcjs;@d0&(8~v1x<279hG7h#d<AXA#sOwrmhr0>q{T;+_qnV}scKXk3+D(Y0=?Q<z13+^0aYJ#-%GT{&OyR<*Y>zBpNSmU~g10Nl~x$?&3<CPtK5kqiHJ)MS8nj504&GM;|#w>?A{wp5h*2AAwX(uY+$xq6W%{dx~`am};oJNoxM9A&fFJNg%X1CzIjVod&0_|Y09&NJ3?FEOD$N6+07U*^l!S$dw0-zM{+N?#5yFD94i$)v9PVSGb2DZat@u^E7gkT<Y9cknt9Yw)-C`Ww3PT~&e8EP>PX;q*om*oU0~46@Ov9v9;K>0|+XkFd@dUv?VN3jSMm;V=9rB8l~r98MTE&M7(jvWw1_9qWP_vA)9hEBif%S1}U#VTSSk%DDU$QBbyYK$(3vZC@X08OwR;`ueNDmjs7)n2yaW?|ZH72KVNU3^k(gl_x0OX#C~#+2m7tJYSI=rQrcDkz4QyC-qlxA>C>1Y#U<~s3hp=95=S7@T&e{3pTfpaW#VEY4VAPr_JlXH6pW3*<N`0Nn&U&(Bo~fYAAG;R}-{@wE~r}6EiqPO=f8cWxhqiC2&3b55Qphr$%%(ne~N6+1w)<(R7sb(*BdlGF7)-p$Q#K$jZ2Ouib`YPHT6%jD9#s@?O%<lIQ?rs2>{e2h*S>AZ`3`oSsk8=;xR4_F^)gz!|TXT7KEnq>n82p5=KyS)y@9*D_?8BjcedOp|;uOHVMH6=mRJ%LNAjnuS1>4Q}90)HRZPTAuM3fM1a|nPD`!elx;Py`_9+=4`k?S^n``TQ-;%T<ryAH^B*z&kBr`jedf|&?qIxM>yV&a3zd5q(p*2BIuetpF~rb&^#KaP>!6`MsO@nlio0z%!eXmJ1!5B+ge%9GNL)DvF{~Is!{SvreBoi7=PJL$yjoj&E1S&2Aod}<P$(JS`>!o@ZN@}W(h-}=;9wfecboTh>;?RECKo%rQtYh;lys?;ffw{cJTQTelLW9`}K-otO&*slMf?|6~lNz&j@4X#?Mi`fYK708)6u#p}s<kxiicT@nab^m|fVykTw<>owZg*aVG{bPlV3;=4ElQ<2FI@I69l9$tU;X)to4DxBUYp7IY@wLx19{J;G}v8t!pdK8HMQ(G+UCgymu%(AQ!zV77&q=|>>Dvid~wEaPI^DphCKX6^@eq7lu)COXU$12rtO9CyztzLu!X&d-v1cN-W$7q7^>9QEn`R*V;q{I#>q?#Lp@S39nS#D>szwpFx08q7Jg1>JNIf9h;?l5Ur}{HMX@;NIZO=p*t@3?YtvLymrt_4}jL8HD1p4O(i*OdEQ^n38S5=43iQB7MpAN>!0B?z!L!O$yxupp)Bibg(wPqjykq(mYBKoas?K1(Q7*4bLgfb)a;;*6rI3U`EbBio;%VK~_MP(X3$?6tH+yRen@ITl8rUO#o$Isu@8Rz<Lpa^-b&|r?)VSoZiARQVvBMM^1%xr2JwSNKP#aNxLdm-1ojIL&>RaDH)WDp;}sp9yX|(<|!miX2ks1sM0vb8^(^`XSrAnxzs4K|F36r&7{n;>abaRnYymI2CmQhA#-luLQYYS3cn@Jk>r8Z2PX9k2oO>%Feg**MSh5$EN91L)rYDoc(aA;mt(RRq}&|>-j7ioI>od0s??kuw`ilNms~whE~cXt@bXwJkh*NoT>km!<`V$&;lXeM2h&K1y~xa>1cwikKTYvUgyJR5C&GY{EgWa4nF8?)vjZ;(!NBCN@P7LjDQCW?F90YZ3KAxMD9(wd9*@s?QiWY7uxVOk6lexG^?sRW!OEBy)4bfWPqG?9>wg^YyCw|}*i9bIXhkKX36y{>4*N{`-o&*NkL!ESnLHVvAIY^i!7GfqZmAJ*upEn<K!w9}5G=1p9jy7gY={bx=u)q%_V3CnfUz-bAO94Mt>g9YqE)9dy$#pZrw>X#b3DulfO4I<`E=k1&G)4pY3OB3-KKTSe1&#T?C48sKgdU|*_*}u1LNzX$hOl6G=k<UAz5<@)emuoLh4WHzAIZn41Tm?6ERlNGXz#L-U7ZE4B#yPu2EW*A{gna#!!uV*VGqJ?`ry&>meLf9fCrXIR<)JVGwp@F$z`rR>QFD(?`#i^EJX}yM6Ee&KV1zoql@%Y{xqI1B@4wwGwO}K(yOJf*mAhTWuEz<u6;;likhT0R!3D8Vvf03xu*ct%1_p*&KB4$*$aMZ*A7}Azs}VO3Q&^ikZ~t)Xsc2;|&4hDh#!u!F+PTm)$Fv0jOt$Q{i384Fqs~vg89`y#`GD^!k*l)%0~UY%8>#)@y%Uf37vu&exhxo`V?HuXo~L;c0J<#jU7&YA4i@(|q+33uq+GWBw%UU_($yv4+Xr<T@>p`su0gYEqXi^;G5(r@)l3U7f)ZT;#vHD>kp_H%6Z}Q)g}gT#VM7i$!z}dy8_r&OXE+R?ur=GFY9?;at=&btFn1g-SURUx6+ZpqSs!N0YN;WTepAHow|O$gTz0R7q|cYS4mHxupu_k-|iZA;<fsLR5Wa#F+XB2gZ?vaTJ1aBw-wRFl-g8CmPvw=PBIn4$2<L#xx<?))2yb25KZ{6k=MgCwNthja6}pYXW#<AHcp!ld-vq3YP?jwv@QTV>5RuR-YJ~8{EklRgExhvO70lJ>8bbCHMs0HqgulNX%PFe@4RwVwWewtoMoX`G{|(klM<|WE(|1(Oo#OMX%d~c^7&)zRf0FP<Q<<ymkZg?(tzHN0mo%o4vTGc7@Hj+Gq?TSeh1Ob}%SYF<H23pnOaIUD4ko@qC2OVsmapjzx`dN`z1D!WmKkjL^z?IWAf_B}<3;hbxCV7TX_I^1}-8hmP~AM@HAn7ms0?CJ=ZO*eyb=ynvbG!m^7v*IRx8lcjg1R<ML?+dS8rve<_l<ja9E)E&df14<)lpDy871gFMNIUXoEN9mu@^GfDw6k+T0!r^sVJ6|$9;E+4crec5Jh;|C#I4B4}a!dHI0*DfFM9SA!0tQs=?(7H3yf=ge^wHigK~(o<h|&w=D7@Dw3`rsg(+Ulx!M!aUzWLVQqm@8?p>;K;qn(SHt5@0hDH5BdlmVWBA3)CTU9^z8;NjJUUpHA6)J>K~-DK(49ZxQPWsTHjmgBNCi{RNBYZ5!L;{}ttC=nVr)Qm4?6o<O5I@45RiYX!r2G2*fLX02NRuq?P@7gy?st*Q}#doJO*gQ;u-;v{q@8Sr90>4ujPUcu#cBN94WXV-{AYr~9Nbg!S9)HttJ0Hp%;cXne5;vmlEkVP0wbszBHY5wKvN3qZYfmO~IH^T^O!TCusE+Y2+EJ^;nVWx$%_}mzV>x7Un<f1$`_TTV#TyLmVQC1Sk7m%=8o@-syoqFGS6MGm2`Chrql#t&`i*Ic{}KAlbD$xXk3pXp1?o`>;L+IX+6o6cqK~3Oo3X=JIF)f{Xj>9LSFsCOl!Knia`<yqaJniyOK#tyTeyu{U2{9dr8b;WVTd#U4N(jtI7|((%1}9N$LLV*(njyygFlyguM!ieLD0^r+QVK}Je8MY(rIOBv|{ev!A^t-L5#8?2Xc!ewnPNbu*<0FrO&C=Vykp4mJ`v8FzdDGXTxZ)q1I5vqi@(03U}~XGI)#PE8Q$8vlZh)`ELuTcSQHfR)88^(Z1}p0BZ9K0qF5KyCCClj(DTmF%qwZdt|HZlf`^;Jk7?|0mQg}AvvMFYo>#<#^Ks{_@Q_N`T}-igKW;X%_oyzIGM&DP8^zW7$zs`(bM9XN98e%)`dj!VjhWx&8QuCc__jTz&}H_QQi4yl~kce%<JQO#$^ROW6cg-Ptb_&0PpT@>xf7m&i$C0;Y=?ArAVN#I?m5MVql}JG5I2RAMoz=osLE-U%ls7-x(o$l762WK7_HRa9D#y%q9sJ>39L_R?{cymm^HCl4AL%=^$B*=5<Vf6t4q0W$%Li<ZA4J)GR;_(zIC8Bdn*bvjvD&W4={FVcL4r<u^I*@PA1)yO*et2aI>-hxf*Z_f9Y)5G{mP#6dDe`TfTh^g#^eW#3pIl?IQ@ylC*GPLmjjoh)dE39uRis*!PAPMMWC98u=|Z4hCqJ9q~C)FbfW7)=xO#jg>n2boW2%RNoe9ql`n=fa5v6fFHd5ZuTq?1nOGlIijt+1ee|)1o>Zr_TEdbudH`8AAI-y%UYWmt{M|oVPvT6w%0JH_Z;k5>$7i{AiWl;9elad)sk<u?P76XZw;4zC8u%Lq4)*ZCbmLAo*Der>H!wvRL*jEtSO-7K-RoT&+qE>273IE3bDoOsRZuzyU623qDD2K2bJI>2eBV?Wd!8@?MgDN7pFcOE8_QIk&spw72-HiQ9_}>yOZ!Hh@2)Np5zT?(sxb;7<Ls5v=;&Cq#w4t(ylPVVHT8=Gk@n<}6QVXj_c7PqhW~VE}?<zvkt+nuydYcD10$Qz)OXaM*o%uz<SH`WfKC5MDG!Canp>H&dnYD)?5OU%PmfB0}I_rs(-~oQ;N)MLM6S5%o9X4x{5&51+rK&lm3T+>^hIC-axIUo^=pgp9J$7TNybL<AKmew9q8c&lrRA=;lO95Zp#HlZ521+^_;*EZFkCVf<RY<4llNgr=nP)83xPxQ|xcp~oFMqrb<70eL>*aCB9aP;RWb}PJaD-5~h3IBOw+dHN>vvd+fkQ<^&!<b3l4qtHmwx_ExM!gj=(+;zXY_1}>2^;pb{~{R;)Ugq&;<A5|_TRmC<AIu86%>AdTRWplP$+t~ca&X5sf^5KG~IAvN8T<g>k8LS*-i)g=_`GP(A{6jh+m>{Ye(flw0z;N_M$5ZY`7N<8%h%FAMVk=#+xI0b7Z_Zp*JVSn<w<<iF$)Q*yBIuyBGXU`O*mr*polxdz_v<`d8_lPA2c@if+%?P4GHY4owo%2E2~$QeCvvBAo2YIKT`C)m7`jG|RzUV_t@n$$Jyb_1J(zG`}IEyW*!iJahxd@?>&k0$3XLb)rXW`yzTymc&Jl8d1HDx)af7OfpCP#I~s8vC-J-Wbzw!+H7zYYS6Y5>xf*=h>(?7%h(W&C03bP14iPoUJcIuA{qBbY3>|jr_M1}+ssYT3;(pY$mf%b)9Gw7$VP_jAd%b>UrtFv$)W#KW9OS<#F75e-T;O1JG`e1KMkHrpi2~M8_|q@VOZ-=aBSR*YTSjIj;j1Q_Os>8Uc-V_OlRt?U(51dh6fd$Xsa%8e#AWm#Xq5oKAlm}3^la^P)CnNa3-M?n4v1fhU_2iC20KO!|oceuM!Y!iedBT5N!J5!`?IyfPr5D7U5IXLu~rhwp6u_z?<H9=mpIQY$~l$Ha#7Tl39vs3I!G3*2E-!47=@hpT5e**^{Jyo|d}qVT#>DHXm5;sJGK@NB3J>)&2DHWQ+#3vuseiwg26f^uFs@g25T7Nw>W;wd`bf<?qClgO+{ghSt|_;B0gT$UZ~op)2?gBgn3CHL}Z>IvR=TG8~Jxg-?-mEb5w$Md(z7P7?PxKyh`)qRv{!qB76cf*$_~eTcd}HhfIe!PX%80xzO7)O3^MPr2VvXmwb}1;_hmo$HS&sykjkhRe?l{C#fg?DGYFGO*jQTpAYZz2FE1?lAzSbrtfd=?%*(4J(8j?-j%w?-d6e?-fQI?|nr_8X7hK8ODx-$)RYk!2H+5(fKUv!#WBqYD^tL`OiCD(m;21j5Y18`1ZZnf{Q*6VYmo!^B#iT6tQ|WSp0@*I66BV)3<E{<u&esMT6-3_k?M7yL~oDwykPp;B#D1x3{ys+1Zk2(Dzf<B0IUv=Bwwh=qrt;y;D3I{ANX-NJgW|fV;cJfHxg95rr2+?sgDt`yL0%!J7bQUORa3+}@GRTD#_Q?xS!!+1a@#EXj9w?gM`{EXgS-H(5Ft@Nz+c1$zL$R-V}zduC@C>0}H3nx5FgmYG7EgJdfX5E%&DTP)GTOFBVRzSI<O4jWPMvYHuBQ#N<x7Av^Gy?%9JyT}yh1L**C9)Jbd+}U_Wtgk{+y5HIcDM?B~0YS*w(1fWxbPt5QEq06D^lWnv=&%&!s|%1%XDeFh6~ko+o=^~b0$SXv8t(!zE|0uww*BxIUa_H`ttX{XG2Gi^7&zKtou&N<jb0XcbiT;?DG_#w`b4`6@f5S-1%}o?T?$2$x)wCPt;9EDW0H^`Fm>~}+NS)orS#px66(M&tHw96<~O+krC%aGqnJTp`nor?(-*z<rq7x{t59I_DwzY=^!w~G87%<e(c6O;FW*MF)`tE$N|$ihj;6y^P9BBGpzjhhjn3fs9n~Kn{`&a+ag+}ySL5&FwdZiT9lw~2MiUfZrhXL1A)FUs#)nkIVzr}WmCjx`9%vv+zg}FNr89@3sPL)c9ppU=+}lYNkqhS{)ukWlyg3@3&ZP|)G9Emnitv&+52qy9I9KC@7Gh))m_YuIhQwuQLZ%jLV{bV)Ns}d-)xNUT+cSrb@%;;7Vg4`GX91E>lA{ij5xK!TW$caOH!B(trxcUJyX%a`XxN5?N>X%Iu#me+(V)Bb84yYy!x7ppiFR`orf;il$#S2@lX*^7Xeovh)w+9BljrrR)rWj4PA!xO`E75QO^@kSoxrq~a5Cm!D_go|e_w28*KR(A#X_DKN7l95_1L>cd4qSeP?}qX)sp~;QsWKO-Z_pc(>!u)Kg8D9_B<}HF}M{}a6nvl%t`Brk{f}N{aIPpI%on___giAy0%UfX%pzKevP{{6eaDACJ(!2KAKurrkmE<pr<}6O#9cd<3Ft{2^ur%0ot3Apc)Z9$yF{b4F5KplM;1<x^M^ojbnY)X*jGMFU~M<&n)f1I)sgmI7<f1k7eKp1%=|>IVhqD!U_s%*SG}a0#uq_@dA-aqMLx=U~~3zEGCtyv+j}D(%S~1j#Ea8ic%SELLr|;nGD>Fv}Fo;q)0KtZRwAneWYk)kcBk-Z8raINU?<?sl_LxG(04D%Adkma>`iLJSO?-9mBEfc$i?w`i*F7yV+0AXKAVeR&xkzqTVOC-~L$`C?AiKvqBNmBSdJ1<skOwKue*?0(NjVd2T+6=9B3cP^^J}2mLqUfC2LSyA!8E6g$93L;-pbOM>S9u4L>JDdWbb>2(AP<9bXn0mQ&qg5%H&Ft8EOeS>o&;7@1tveREoCtqXqv_x+_c#5`Q6Tg^KUISk+r6J-k>2|?V_$nO7(4G|Y8%$M(p+s`xEacj?A?RT`8LiGin1QcsR!SjphscVAWA+AAm|ckCIq;xp4qKwp!)$6_p09{qy<NI1SI)du_Q_=Kmo&1wIm0z|I(7-t2^yLT(TRpqc>HQuf>NeX(RNdnjjfQE)<H0&mclrKoce3iRCke{kadEaT}LnFsrK9Z6+{V))6=A*-#+|)z&cM1eJfvWJdEzy_aBbt1`W^3kC<jjdBCJAc2kR_-g<OeNp-L(qX8JUH>{8R+Va%@I=hoInQQq9#Wia9%PEA;&X=I`+wi-uIMmW@^p@~!rl9oj;nm$WSGS`CW&bnw?mysjg%tD9-|9eYSkCGw*DKok{UVODxxHU;wS8+r-CthL9)Fv)CY$<7hn0VHIj1u34Www{kjp3(HG9dFc6;;#?>;rOfo5nr*3x(?51?1~#AT+f5tGMWgw|NBQdN|(e;N$VHrwr5v8UEfp<Z_DhI(21ct~S}xxitpm(z=j-$+Hv4#}bXMVU;QV@?`fg_mcAuaL1wOqUGJXH8g99KD-PVlV0LmQ3PS;UsR~ViJW=gTc2s@=}ExEOaCcmcP;bZMQ_w1xhS&08%%cM)JMrfBtLqd@-9eqPNK`?Zd|Nd@=4%zN@;V#0<T{NJ$5*$ac1@`<qtLB?os2QM6O+$QO9ba!6NHs>v`PMV;N7In#!=sGG$>!l=DBApz`Y!@yQ(`f*H!Whza%9Yh5~^w6C^C~I+1wqlBWMU#!yV|9(NzO1??z+(;i#h7#E8ldS>Xd_vDJ1AahRjZc$@w8*0NESs`($U%IwA(L;6{8VidXviPHbJPjeA=>nxnV((N=#jmV2D;+QON#CgOTG+WSw^7c554WT0UWQN0Yt`*>n^Ux{An*#0(@lewFo2&9vUn+pP{A<F@SuxWwLw*o74(U}z%tVFXsEB?EZ1RutQUy6eaWSaiRlw0INYwKV5~#6v@MERcXf3^Z7#RDP*O!!E%h$KTpg{?>Y~HWbb^4Jv$6ye^-v!{IE%1%o1L;})xfw_O^3UXi??YYmGe?J-cPRN3+xwe>8sfLIk&v#9tJ1$ve*U=!K6F0Z9KZ5;|tbZ$eojTcP!LTsbJ30+)0elgS75y`g6F%HvNDMo+}<HR2Dh13yReh^&lVUZ1bp@u?MRjCpJr-or4cWzPeL-x^@mxuo02r9H({lm~Z6k#cPa7tzv-v+lNJ|@}TNB{iK5x+KFkL=hI1-ooA>(z&Fgc`0IqKO{?<Ctn~tF=q^5>{~CkVPt2Qo=oD01pTVripAwWY{g2Iq`qB;(fg|@_^+6{!Q&wLzbztH0dKRSPvBzOus3L*Bq}=^dvmM0(p_=sBDeML>t0BLEEfse11R@2x(c}n^{URVfs5GkQQGstoAG~=NX4Aok~B5&sHyo+57~s&kM}zC!Nxru2!;}z2RbJ54^LKaxyhL?#ri~tf{jpcgI^S|FR{nxPh_KOV+wBZZCOtPj4rdLR~j5Ry4dHno;8@0Tbp>5ks^?Rv82D?>p~t1s7%BRP=!bo$0<!K!ddozZ~h(v?2^S|AajDr*k@OsWnn}V~S?vifPejeadls%m_H7hk~La{x<%6;O4KjJdKz_aO>3Pg3^+YK(a7q2UEQK45!EAaWc(^FvlhcV}{EhqkszgE_pF^3hJPDFi==B%C6J5^ron#uwSe25%fJ<wMP|M>l}lKk$O39bG#Q{jM5hqjLDLWR@bQ;73F5$(}jT@{)>A4i+XMw76qrz4s&u#a=F>YMwz2ZXv^pwmVNXvvJ#Y&V24ET6VzYKtay;_Y(RZ?g0oz0rd~jp8-{0D6F?wxkf{Q_f{_1m96g_<DJCQq-u!4=+K6buW5@7@dzcFA2lQ@@V2bl7p_m730*fYr-+Qr}3RwXKl*0&Lj~<$5Ba9?gaWOuy)Mw>0aRU!_=VGEaN-m~wv`qMRT>9_Ui8>k_;2q9^q~f^0>j!r6L7=}ekr-6pB)?+%$MPxm;7rMWvy_n#A2BLI6;5IH;To;_K02TB$!u<T=_ZZn%<w}_D7s8^27mUA*b}9^%wkjgg~&FC(dJG#T}lg`BKeF~m;?axGxv#xtdOH9`us&ZaHv!)+4w2iP~N|PzaZ~khx6`L<Nk%Y__U!WMky@;_Tke<MwoG_rX<5_v^l^YBYtJq``7zwbf5Nvsp?$zLB+o@1F?1jE6nxhuNMRATk!E26cGYGEig-^rK1vT5no@rm!sEXUEN;drf?z7hW=TEeR1jx<xW9JxY*Fecqa`8AQaF5C0tl^fZR*T!;)Qeev4`_H0;C%{Q9^5fmbB>rZ3)HT-1W$y=?+}U~g<<dwf|<_7WQ;mj2#Vgjfs9kwUPBxnN2+u+QtZvKz7a3Y%0Q64*LE?Cm*8E`~a_d5(oRXQ@AQgbd=?7$FyUjFHvI`qcSoZ#76oa)ar#%XS#y${p^9=)d0^@j>*d<M&Aw2={EOyLRg<?3j@7UHT37Rjkm%2~WWXyAsR<jbMW|@ohg%>h+5(SaCyCZ2A?w!U9K%B|&El>w9RS!3-#l*MKR&WP3d(i{iDxR!k=fx)~FS7t-}ci)kN-JjV<&ee{4CVK%gz5p8+k9cv_-^EIM-J2;fCNwajPSCL{nWu5Rs1r_$9!;7Y@8$sY^L=GD|&2dBc8L<~uyS2MrbzI$&ae2``ipRCX9AT&Ou>3$H1;g5*0d-{PhKj@5EE$#;fT?g)yWMr8D(%Eph-Xl+5@?b{i>A1lDeYe&4$asn_8{nOBcfO-%??G$>uwuHA?B`^ug1M&UXE|Zqg5!fZCHA9Vj#j6H^tGH1wsrkU1xol=^Dbasgo%C#xWIn1Q)Q47aa4xSdVdopp7OHZyLGLtNX3u_T6tqKffe%$k}9+M^7@ki)ch|XDOTs^5~~zG)iY^JozLW!IwocihgFs{|!1Meb|tKkJ153Qh$85qx13nQHfu(KFDx7R#oVx;P~+6(`QGg$8Vn<9GBe|Vy-u+Wfu4E3@5pDOZ2w|VCEQz69ZD#fA|1cNt)dGhqWKj6ApmF0-s}C(jRIcf3Owl2ri~;(QJ%IGTQ?%?U5Xb5P(RgD15g%(T@>c{ngFa9dRM<S_Ed}Z2n6!VnO%Gimnz-mebJP(?@UYQwx|+p1<bA%C+8nHfqk4&#)*$H^eVaUL8gc)$;k_K|i~UsPaRu21HzY1c)%0-VYD*X)?A-jWC9JEn@6Jm-s~pgOBJHA(#T66CN<3!4D7aB3Q32w?mi7sChL@yk241Y&>1et<vMgMJ>X}NDpgca)z$q;oRsLJW;<eikta5S@LU~A>%zw7=1wB@RYv@H)}Cl`c#Jm5Oe9ff!=ypTmS$QK|jMY(+PelL(*NqlJzq9%0kZsIF+Dui6Ks}@(mCq=~$w|St!)*GrH<W!gSUo_4<R^Lt_<+tTu~_O4S7kc=d@|iy+iKIAr~?rWc#$a~~9)qx}8{VPlW}ZO8%c$sY~w@gDza$oBW-k4A(O4lhF8X=z%C8^mPxnALo?^w^>)D<U7ix`F22z2q!bzE)FJeKs|O#oeJfE9nSs5SIX4EIbK_D9%&OY5qeNzQUR76z$z|vi7}{N6kxM#UQC7<V|a2>zHpNx-1l}tKaMB98I%}Un=r^d#FTCF;f*|LnDcxI=soO&qu+h=?vt(J{dUW_WTxW4V`%vf;BAqe0YRYV~L;kOd1!87Uj6NLY3vsHNxW>@o|j+8R^iJ6;=~TkOms!Ds_89VsYV$mSRs#w#Ft;dl|@rNss|)1{{^5pQh7;(FD*_NT|*NGzjiL>+-wRnzQ({#l=vL<rqs0!_pbKH_|+FU$B~Qz6`vKVXhe%9%F6QEE!3;QE6`wZ<>b$TP;RcGC2y9z&ORcY`&=$Mp!a-Y1*JI86Jwb+y-8?l$7&OfVM9Q2CdKrt6z(%auT_7uHLw}n3aq74w+HdL9T-econMNUe0DO9AZ-XNbZn|5X3;^P{O&-&ageUqh6K{`Lku)WX@&1rfyGaO0UBK)<tc*w5wyRg_J=~6;~rzp^m3*t5C;P6$Pt^%UAdi%tXXY>SV&6O=3OVe$`at>IGrt9(qy9oD%+geP>bk(`7gvW|4zOKLd{aW8o)MvF}AzTwQEr^>rKRc#XgSVLBGc=opV|hLWF#*x*hyqQ6JZClQ2cke*Q97Pmv2S~)60@uRT?sT!3Xtv#AY4m6L03T3d<=3N^p``=Z&4KP9(>OceSP~3G~F^#oh{i$~b-&%VS@MRqcBq1p6K}cmE>H+JtEA+qzxTXgI?fMsWAdoJ>ZQr|dwG`uzYz1?f23>4UCBS6kp(K3f#`SnMOIC1npuc4{9<kZCkTP<;v59BOTxw7AArm)#Vz8Eus9I)%_0ZKEDLi$}B)5gTzH^gUX>og-h0h2>cQ@4*t`FR2qidlTE=mu2Ain-u=tT?81MU_K!4?O;n;&S(&j=`-%lm@ov&qFV0;ntbq~K)WrAZXPijN8y{qkgz<nucEGR^VVDL|R0{ZkQ*((-8nStdodCLuxEVJq<?I^opb%9?Q_(%th<AJ!$BoeBfy1M&Fg4Ab?tKBX(bp*kXzxGYh{vMY$-aRXPOa}9C1M&`#V7C*hD)3YJ)>pKVAnriuYK1U-bd4xeBNMr`EPc?WLmn!ie?QeUM8C}MOhn^~j4AGm01{Zq(#c@I(BAg@irRG^!#yCQU&z#38{XSUCC4oDWpXI-4anW}Dx8&ye_<fl>5qxh#^(NZTHdnRSsry^yy4QByY&<Qi3ZI)4unYm%HAiQovYPPOuSwy8VWcsQmv4<waRfL&KOe!G<ojP(livg0>`K2;rQgab*>#}r#?|w9N>>Y%!ybLxwkbN44qQP6=s;QPwC&dpy)ghc@WP&)V;nP(1H7|b(XmH>6Z<k8J8bOST9VOlA3d~#L6AD^Y~+~hjV3+f(0vM*U3)Va)XH<j-#FfPQJ@K1Pv>>at+o->{wb;(riF0Ss8z5jDuQgFo2`XlYC_1MD^RZn_NKO0w-i)v*&Kc{TG5BH6@i7CXIRQy4yvll+sB?wpsC7?{y9>{aSDWkp)o2r0Uz@jH-6g7W<87t0LW192-@l3Vs3AZ#=dBTw=uIQ(4qqjuN^m+Y(n4s(c4fo3UDLr=>)tg#=nab9PnbMLts&2n$|2kJ4^embd0{mxOr`C*afbV%QP?fKAC0b$wgLDq6dQD0*(d2BKD}9SwYNmfm8TUiuqm;^H2+K+EJqTP~)LOl^Tr+e~8ZGPua`b$6_Hvf-93V(E44L^K2Y?$*jND#sOy^3-Sf+r;v36evS!RfX53o!=Ro_CZjZQgj-1mA3l9lGZMmGmWyahp1rLT{G8);Ut%^cXRB2JO7~mZYZ;2SS*xJy>mi8X>o$bRvO*swOVNCDGM(ohgbIBC2;95{LF~rdgIFV^d|wvDEf6wxmHN3x9`IpEM8p~=tsEW9G5ISjs1<GZ0$H%<4@T*dw*B#BEaz1KQk{`MO94@R1Vj*>XedNQ#OctWw@Lm^7$rSNo;J*;7`_t?U*TMJeLYH}DQqlsD2s+Fh^NZJvX;AIA*L0NxvKhlIjdI=Q<8&I`z`Mp6o8-Lo=RFaSk=|%nxhQ}h2}SO09pyK=Yp4nUJBmJ2jJ^rtksU?4+!H$?CJ4nBn>VIkvvTwYbA#=1+<J|UhzGPI8>-A=oStWh^Lh7YyoHBn%i_u3shFEDoX>;USY=~KaoO{x)_s<SbIB!JR-{%*?7K|`lw_RiPsWrWPKMm6eGe8rjOxS!^tB|N)o9fwz{r4&16DT?B&x6$h1Bt?sA7*?;R1(>8nJHx>3w1E4c)zNz3&;8xh+q7i%q>p%NY<)cDoJ1q2uRc8XKYf{W^NfdoTS69<cpXnhmzgDk=*n)R`$z}A{IpHC@f&pN^tdm}}(@krNz;Sulf%hH~>CYP`W*Z|SgJqVC@3u76$pz^61;LPU8UgD8q$QexVu2<Rkh)i3}94A1B*jG%M+}$=6yKd!VX;!8T7~OWm&6gr!?QX{*V8#pts89@wCa;(dFD_^U0j#Vg)3qoI(<KZ7fxsV=C_^Q$01;SJ;I^Plvg9&^LN9h<AYAA#S$Z{{%;wR{@nC|P3C315Djo^HuCN${6oI8{PWBcJ=VcE)>DR(yFwLxoX+Vo$;rYBeETjW_m1;<OnVN3{yXIw<XK*_3g;MRuFgi{KC~^f48u0lv8C@l-{B$x+$3ku~=(e==t7JAdn#Nt^d(ohMo#h}r_NKs7hH$SzHvRwpum9~|NH+cV|MUN@6#+e=l$*x2nDea=JT5<;4<Qkr;zg}eDcGMVQhwi8ut<tl<om99l&l&Uk28ZEhL{CxG>D++MVidfX_sapHv{#}lGT&>c-=ATa@xd_HWA{R!}PqYE*5Ey((`oOx9j!*PnDYO@o1d0*YKiR?IDlbt-Pk!qE@iuc{&2TmaexHn1DdNxzYrxV~O)JY1CddSOGaz>_CHI#Bvr&SLu3iJRh-`m-1t%Ah4W`UFs$nnwOZTr&QXud!hwFi8xjuIMc^1(5UH8>6mZd1W$1+rdlbk9eBVbXh|rYwS+4UvPJhAPAb;}a%(PPlmW+QM-77E9K@yBy7hn%g!4dN3&G(4BUPYKTs9j9_4vtTS*pBM4y{coeCN%x$<pBs2z;IB$&uk)nbSr{>>y~(`H!c<hel|LEhMd3ATA(@n^<8fpcoO95KxR5R)mb0SmVf3K`1b|lh7H1%AO8psor6X_Xa_jS)XU)HFJrYt^O>@#>sga(2fCs*OPfEHL2PpGL50MIhEXlSoFlhm$ghJB&oG5Q&WkK#j=M5IvjyO?A56RuhcgJi}pvYWweaG78URarFtNn`B;Pxzk;+=y4`SHA?1;5WM_q(9#e@5yCs7PS3gWvYhpE8K$;^eZ?RQEMJ!NKFrnGFH(K;l(dCk96qt!6iadDr5I_t*CM8ycem0u)K83)`VaEyqWlKKLRP4iI6l#IdeqR+K*%(jz%@AHZkfFQ2+?q}@D1ZYI2$+K6FQ=zGcc<dLq;~xQZ@X%x7y1D^73-=G?LwZ7*4>%o#X%E`nq<UPV*$e1ouzsQzM0#w?U`*!bMu4YC(AHB>o?E~&Q)2YWxdV%*1;o%+Ucm(8>YQaY2Vn}FV#UwxTJ9V=<V@|E_c*LRPbKLy^;&VkXKk?5cZ{A7=ph03d3+O_QFuqwOJ7u@Al7!14RHQ{quA^5GqEOPXRb^^lIWsQ(gtR8uzmEs0k-o%qLBX=j9CxKb-=t46<|R*eMqZb%hyqeleNMhXtyC{usgsh9_uZpdNG&3U>jEoXR2r7;?jMYrC6hpsHX-a-%3?eAbY8OMp4^#>=er0<*HwJ>jXC*x2$p2)M-9Jm(_$l(OeMM*2R!Jg@Ub0NdI*W(EOcJgfBn-#<U^oHOQjM4A`8ETM>gZ>jNGO~1zA!}eQcM21N&?y2zh;cP$H(3*5uRK&|IX4;1xHOf+rxyg{;4A8u;K4a_iBg`Ar>9*Q_4y5|#CM6hxuH1<>(JUsQT~%n=P$9q3TBY_XqTMh$jA}9ED%z%;xY)W0hN5nv;moQyjjO;>l~jrU*tn9k0;nRyD7-W);zfA9{O};ZJdfxC>0xcNU5i*D55IS6(PfrifjsxH)`p4Lg#YiDPX0eUATL5;v7jeU_bvJ%`mIK}habuegq{1HMrUWc(Qb9SaZN-`e^~odyL~oDw&jba=uoG%Rl937c^A5i{^~xLz&x}$Gl~P?E9aBhs-Df$3-sI^QH&EMpW#NXUb3J>=@KMTw2!pZXw41lHh|gci5AEJwuaa~oLnI|ZH60Y1djYO-HMbP2;ga!|D0Q*rBfFqN4Bz+)u9WLJLh%&T%(&0`@?xM>!;(;mtF!GoAMW{FT$=F1#11M_K>3Y&fXFj!g)Gj4MEW$ut2D%QfLW$N@l%baB#C#KCe7B+j8s?#z!g~#bkD#jLk889~=Z~u0vh5e9k1H*|f|#O+~brpFsF=B<yo|RW4!ko|iYVq!qEBtJ?0B{LTzNLi>+N|C5U|v~os+suDvf-u{uuMc<1I02ms_NfkEVaQ@29$MruxH+(Q3vX71Ek4P+$J;GY_IbN3lPXNLVd!CKILYHhvZm-Dn-RxFjzf@}__7O;(7_&+gHEhag9?RIBycNYy&xv;9!jL$wX<BcVLS;cq^;$o>)Rz<5@Jz<B;Wo%@jW!@!QkdiCp**xD!f6uAy(Ha@u>GSQ-H6*EEcdcGC)hApB2;3)(&2y}sO0H%?z~9H!X<%CMYK^Xu*Y-3Nar;LvN9CgV%96_0aJAyDF7HjuV{SuZI(@u1(;yX*8=$ZffZE>jKgoXR*Q{^!C7A$nn+N>e7Lwc<A^!F*lzM)XyuR3B7lw`7sm$-`$keL3q>T#kw)Q>4>MdkUz~*s%RV{8Ip&x)gb+6bjM=<<UwXE-8ur7|GK@KF2)bW5m-|R#)}7@Umc)OZk~pna{25Ek@ItKiQ}@!&VFer_-ZYx$DnX6_pPFa$am_32#L)ep|3{#R-~o=2`cuH#JPouTh_B&iOt`fD1JcVDMuU4hn@p2)^u!z2y*Lox=dcZ*Owfy}{s+12?8)(+_PH~SDC_S<lIwkr?M5PhCsWESbCYEG!iWmKFhYVa5HiLV5Utp8!C92>qy@9U=Rk}Iv8t2l6zU!f;XqqwWcq<kxL^eo-#$fyvq$KmR!z%bFcv2^1JP3KD-hk4#HmYB0mMRV#L5d)4d59FVF~-xVUkBm5|&pI^|Q$wWx`|>2{Bz1|2_`5t`y150S{GML+k}_GJF4QImL`%vP(kOLi3kLs67Ia0ed)FIV&GZ{v}=A##r8xZ{{rD%-LWbAu91^9**-q7e@0~_QU+6ANXb7yP?(m+%ub3gwXTy8z_tTxnU9yZ5o#WK=<`pN{BVBH0+qzC9AL0t@8^*XX+hV$nWNACQpI=Qg0pd+Dy)}Q8r(_Shz=wSvpm`3S*ufrD%p?ory2PK_2X@#*7whFrpMr2sQ(MY;SOQiE$s&aSpvD!^@Z)BAvG&&GarPK!l?!dviIg(5CXiB(FB5R0Y<4Zuw%$w!K2sJT=EJ&0buQ66L3xbtBE^85$b&Pr3SOxFdmL)D_XD*$tSG{APWC8ZZ<PV|$aucphxuDMD>yLuSK+Y@R=%^CEnd571IQ)De&czsH`yUxbgvPk{^3u4k?Z4Vr_SXz1ekCJnHf%WA{1izoZa@?-XJ(Pz_ikq*)#L^Q^IF&U-nK~T{qXQJJAR?qs{Sjw(9xg4&qrY;(+s#oXp3PUE`*%g5T)>lL_aV$%+(P(`=oYY0$#KKN@li9e+6wSs!2d-fZUOKEZ{DeZyWR%Y4L9@>@7EY@Hkk*-B#o0=FuLvUbyep2$=UfJpx*%irR~NVfx~;9)$p5M=A}|K7Yv??1!HE2(2xqg^4e6zgPC3Fp^$AtccS#vNkdG=)hIRus){Y*T@zOg+aOMr&Pup(*yL<1R-Cs9FhY6i;>wA;YWJbwHZDZ8+cZ-HoL+vt|)ti!lkr3mW;l?07Q|Q;EhY3@fl&T}HSxO|bZ6Rh53#Q;;z;NaeVVP)vaJ+&)?#E8qN0p}>+ayM!XMi4^mU+K*5c_ZckHRb0u`w$4=tt4^wuhqLEStxu9IC5QTiXSQ)Cd%>C!gY)=TlBBEoRQ<63%~DDDb^v#C{qxshk@Nk9b|oEYCB(&vN0Bj#pQ8dL~bB;})k)AjvjG+$mr&&w6l1Nz%TT+b8Z~#%2eP1|C~hcr48FOqNC83oy7d8u)CrO})5~0&r^-jOIL<o<fg4#b%T$X4RS+_}M=GJItD|r9>ZK4smj6Zbb)wjM(5CCvx)1P?ibUp8XrcArA*?<&+@C7D(eOTTBTX7xB($$5>r@GXP8ow(c@jwvj5B57~1CsMLTJZG}uNj+5U=bRgi^0bfqjWiL(XKw=zn3^$3hrQx{YyLkz38HBWq<02TVsxVf?Fs`e>K)L!lj>9JKyv^YrZ+d9rvv*x#MlmTkR7g2sZA>Y%aB&bRvDH#+7hT@a)SHsrWmPS^dF#?Qf@)l~=(+g5Q7FZ-OMgjX-<qf;q4kJxtedh-UL4vV&d5N_e?JuBA8GUDlCIUfZWILI_>~b=zp^TbS+!JB*=2Dctg=%roX3HG{QT05K{3;E78kQ5(V4)Q!1vUMaP$)@y|P}k`7~0&j%<E=kj;8lU0fRZFqwvDjKw;PHbMFnSLkQ4i=loeMTt6yInItP+M!(N-EKR)txv@oqe9zlCHcrz3%v6dAZh8}u3dAq<H@z<2s}01_=FdqTmETwp3QSJMW6t32e#R$X?DT*0BimcC5@7zt^*aCWUO-?wO6YKV~)jQUyQClz6eSSoL$!2Nt$)7s|B52BfkLzD({@yV2R!Uf^~$^2AiZ><IZRfDQq}xCcukK`+`v&S19|p|G|0m#6l3+_3)LNr~U7o<U%|U-8w%9TQ>n#XrovFk{2iQBpba=W<--8Zq|l%sSC6}olSb^Y>dc@P0)NXt=WrJFm|8}vQdIFxE_pMQo-?RC@x$(d|@87rk)$G@ZvRHR(auo6nyxrTi0}6SHA0BRe56a#6xjYWOn!WNj9$6qJL&nv0C)+|MI_6qvV^-w0w$c+0%J8_3WH6Ek;JW6l!X--pMQ(=OelwlHNUPzk!`<v^p8WQh7Y?A10W^=UkgYtMw#*h((1-LEYd6a|EKSC+SIatRj?=X)ij`mZ5ZPlpxL~{gtL&>vgD8sC-Z`4a-~0l^ok*jeKdKGbq)}shDYtqASM+Ajjx?q!g=jF&AQLRDWH!E5cs|4?@Pe(H~hcRv>~l_VkhW?|w4-gjephfB)D2mmNy~^<Qe1ajPSaSREZt`e~)O8(C*}TpDnLAgzl|M1=~%YhVlZ1@xy_SMW|DpMuda{sUt;%GiY>TZ<bEUA%Uu)5v)wqb&ww)#67^|H5Gr`F9W+B?wZX8!1VUg{qP)0EHJx1=lr#Llk9houxodcyEJHLuS>^)l)uK8uQE4F*i#m((d{BVl+CQFZ$W!C${BVIk7UOPQeAJ#xj~D{a0x|JemCT_UAf)wniDmOyL+yF|!r{TpO>cpO9&T8?tV(j)Q=NIkCm5wT@V`R98XLTEx);-GcbeRv8E2)%iT>eUh1L$r4)EngJd9wGei=mgB<%>z{s!VLw^qtNI!IBZn`I-SQQeqsh-#j#FtR)|C)|Qs#xA!mA&@ApbE&s{5h#Y`S~KK(;5@1?lp~K%@KCfOXJYShDEE`D`|u%<S1N^#S5Yxy}^;*@&c$EoJH{1mQ`23Pf$go)})-vTt#q4&6pe9g?|msnN$#51`EO_hj+^cX#c*Z5v7a|9lEY2L#eZQe@dyZMjY0#A%Xi(iXPUT=S?wOH{-&MG7Px*D3tnZ)Wzveeoe#P7inJIRf`RJG(nOJ2SsrP2gv!N+;k0k<n$vp*5Wbh%9cke$(}~M}vW5anWs`ugoYo_JN}pAXc@rAee&uCz`>@qZdm49c92H<i0q$YU7pd@nb#ke~LB^ZuBCmhc18N;xcMy-XBmc)v&eO>B2pAXS6pQ?r!a)V7NUTjdu3-_qV>&8j*&%yd>OOA9*{&{hj^Mcf)<DWxdh5lxiJ{lCC!o6$_pyLF;(vcN<Oq+w&0as1a;?dM(R3M2MxsVO&RBT59h`UMrgi5iA?wyecxeA1yTFlBFXGQ~~alwzv9w1fJ>$^S<o!urQ^Chph09v#<qq!7lRHCdU04!c-OwRiYU{k<k!AxQ9xKYW#tv6VM=S5BmGi_Evvq&#cP8=Pd>aS0I8Lh9YY0rh>ecFa%3CumM)f;C}b5x+;3I%OH;j&Yo1m5iH&K21F7hE{w9M$_*BPnY-S1{axpL>xTC~h;@QN*M@r_T7Lk-kDz$h+rznp{|`TXpbpYgWLvJQQAYs@S@u6i$+-_4d_}#dkRUp5^tLcy6a2vyzKb>N8k(KSg(ze+wIh39;=G9)5i3s~OlWqX3~Sdet~qXMrMDWCHe5Ef@<Thj>6)qK-!2^+HwZCTB}~pp;Q_PMG+46By}o@wsqOyA$q@!oN-EgH3ig^*fH!j(?HMpckXilTMvm%K5D5<^gAY=CDBOqt4T^#e_e^a^<!6EAo9H+?f&ZX}oI5t3CM5V8vS~9Ap+;_wWzG&lqW{aY&mGIzfv*{+0;}*45x$acfp00)O&|DFi|lj@<ukpFFauipwU!RE`AK^Nu0Z3^Y)M%P0b;|%<W3|e=Mk)&n|A>6up*iR=N>rrc^sDtOa>p-U0;Lef1+*QNggcPOkt>U8VZ!L0wN}!M85c0q68y-^x=<>S08(Q@6*FapS$eABMldACCA5%C7l^QP^<-6=UoDGZw>k$88UnC!jx>_Q1H(0ps@m4JB+7qUzI=~(A`Q8PY`^88_F!+K!^g%Xj@c$pdr5{u^Es7Eq!f-N+m|F%bc3?N6^m+l8USG#M>8R1@fCmX#ivqO8QMqxMI(W{m~vxusapj<{UDRF8f^Fb^;5H08v5i(cXGXlydsBYuPiQ{zON5BSToa^QSY#HrTQBRrNML-IfEnES=~rN`4$6=9eSYwh`qSR-H9eaLmHImnS^|CZo<>36fr?2oC)|NE3{ey9l$4RP4fPo%@V=yjt2xy{kEJHSBeKAHn6EC#bvimeJ+sF!tc;d0$tf+kOmmp(WK(B`B+=NiWLK4$gGJ@@A~*9xbjUB6ev~ODIV<dS;M&1$zhF%<hxxut1t=DHgjdgEcJHBQXx8OC|Z+tr?6hD|P2+I1Xp9S-gWD!ya31$=`w-DQXmZl$Ti?XwMT$U?5prK?C`%IT^}}NT}d|v+t?|*%}T?DWc5magf2m`^$M2q{zXJ8J2z2As?>%>}5Ee1~IM`6Kt73fcWRf2?I$r+EMg8FupVlGIdZ?J#KxHI?S&B9lp=e<J^Ikckakr*rpA1M;zWBj*R~lTFT<fhry@*gelIB=~YNIw!xmc^Y!TgQMDzRm*<^p##*W)2bmgS9E~A%e@?%QE*P{ooN<cBXf0!P9Tr%21#2m5O)-a&-)P?Z37hL;spvc?_G!{xE4wr7x*(}8P<Z79L{3s!+c}Q|%Bg1+YQDNNTLfq_uU6~`q*~~vjh8G^*KKLe&o0M2wQa0;On<v9C|@=%yC@k>d#gFFNr$v5ZRh6PfgDG^9QCx-^n_-9$u$$yj1Dz!dH*^&J9_@(;oH}zXTKgEAHF#;3YyMs+FCFoaynCa{8)6rNkhscbpJ{ofhgv+u3JWuii}ijSSBD78S~1->M5+4z!I>&$_t)0dFnH|TSPY{bmkgf%!{;AX!cZZ;Kz$dsPUyAiJI6UPRm%`4aK`HZDr)r`S2kt9tVHsqVO?GH@FGbHi&W}4;1|?oQ`ExUF_kw7~YLU6mpwml<pg}ZM4vrH{zLFX5C#>q>l>=h%WENnc5-TKgxPuaHF*fh0RChDlA-uiN&D{r_A_3BerIiP+_DHk<})eDbS}zgu79s^P^;P!Gfxv`sZq#Y1s6h*1iX#3Cl$fvXWnT#d{#H&8;EgiKy>c)hAi@70Fjr<FJN+R3?SC$bhq@OEQK*O|2n~7&mkb{&pOmvlnde7mmSSm^R0v=NFZLCq*vefnvB$7uM4E^^#|FhiD7z!7LZN%!hm010HgTq50^HPkrrSHUa3;NLV=cs{`~G_4OdD8H1q#h@)DA9>#(E1AIr!1bjY2j{rziW&_1dKa4SK(K65iCg}OZtWmBmRc3gvQ~emJNX2P1F&AxR407(9;L=mHD@8H7={@PU%Pp(Tt%~9vri<05>{dkI#H{P8DeMj-Ca2vK<@dObjzWp$rmjmP7AuynB7n#nKa5w7j4DEcVBrq0L{7ijN?p_nBp0G_K#?*1T~$1`V^@&6USmy=yjvs>pP^E#c+BrAnUo%=dmE3RQ<f6Mc8Z9@Hs-<A)U=whIpbnfxbxqb+kw8Eg^7f|=-qlcIUAPPexut6^3Y@T2wnf+tAG{AJRVe}hZ}I!X{$8gK5>-{>zulFEGiV`^*S9#Fia~yf-x>%^_l4!f^}}HO;(?sdQLh&_5Q9J2EslnizhfHPn}$a`DCtbx>`K{CK~WMXaUViX`KsRt@+7qE=Nu8Kn6%b1H$}GbkPL#Z$cK%EU10Ah~s=xRz!OVGjp0G5uUkii7)ezLC<&~;Q47VMbCz3hezIGA+TsL%%=!}A+TsVvS%7#O6|iEkDP$&JMA4wJ>VAXTEie~ter+t80hM`f)^~UfeZoBNUdN2FIQ_SJPVn`Tj;%7F!iqlD=GHOFDD7i*c(SlvGG(`&6bGn7T*Z?pGJ34Wt0X6%Yn7#Y;=|i%A4e@nS+fEU&0VIl4@abG2c7`DW^^~bsq{IY_#8kV^*Cx$D2XSqF7Xc=%5E;8E4`_9iVP2nx180bU{AXvZSd%lI$Ey+t^K!<SI-XYE>}jEM=1VedCjH2WbF|LG9`nMvxEdVI^df^{0VrxH49Ig8`e`*87gnw>`1S`zSC&8g*5Nv1ov8(IV6eLd;;_8gkVt!&ruKv)<#Y^~sX%dH3}%tMe7Lx&~i~7CZK~ER$+h6^I2)U(Gc;nHCRw@wA}_0A#H+|L0Ye`2VoP_0@eBA(@LS^*ApZi<Y5zVdap?LcIHXe_<6si~hBb50O2z!#xn+mMFdBi2B>31BaepxhBXb!lHp$no!_wvk7_&`}LLgPpEg-(biy%w(?}Ta!XtNot@QNVn*OAH`asJhHKC;WE89@XWzn(F5wX3C~n@fON0nTudN)J^f!=}DV!s>3iN&lDfeZPhF?*+2cIK9_UMJkd*9KuWtTa_yt;0FJCScxKhP_cc_*oO$WrQ1AG65pSc+Z6Q`YzRl;se%w1=?Wfm_THfOq~9J-0fIw%7{Qa<emClJo1D<osGs&aVz~7BpkQd~Bkr4}>-u9}{u~83ezI^ETAr_3Uh2AT~bicfGw`6q!c<E2Kv~B=r*~04Wb2=!f&#RzdnIs!8hTmp!!e2deDSzskN`Ns7wxmR#9%wlD3?fc{havcc;I^7q`2X1Cz(dd5_~{DA8lI1?FitSt3AC$D>#qQ2-o*)VaF*{qq^wvIKx->^F2;5y}@eGey-B%NYx0`GzMoW(6>szeP2n8mMs8Tivi0vkru<&Si%WTp6~RPGkxlnl2J;{wFRF{*OC+?suFS=PNK;6a0^!q~bMR+s_nrqhlBi=caUT495o29jtW4ioA^s)Kfw*n2U3t5Kk>XTem2LWU+kDSko1D^+fZ9QN+csY+IXW}_yhOQSPauDsg@T~_=*i@9^4{E1lFo$|ag#y0y=ky8o6EwOOQb1Ue4Ma*t>b2Q=iYPf0*rFa#FUlYdKkWw6Pu530oYwgy^QOsq{IMA#a9RQXa89td~AjmRm{6Kc;J;Tv^@BAndxB0Gja{Ai)1#uJKVCYj1;p_8jI7wa*U=*6uYln#-DM{lTEO*uSm#Vn78+eH^+@GzWx$EkKR^vG$ki??AC4qDo?#<K4<syE!WGVt|Gfr%(NTN8~>>;^QBGGGh3nhA<_2rT)7Q2qF4nIbTpSSIr9b$?y6ny_5_Q_Rz58WyH>Wycuv%Jv+8)aPH{y4U8hGbw^sJmfZH-Ac%hC--4pDI^KWn7vjmlqq3b`_62Ct7X&psXI4Xtt~LK?A#8qiqWeck`3)cG><Gl8J%TyZND+&@#8?=nW0p!WeGEQs&Fm9Sz0ie-+yJ4mO`MeB@hkp&<h<{Pf!6VVoX#%+uTBfuFp#(0-4+rzD=Ex;sxMNz_q}Y8J!k>E<Fn6&1Qq=OTUmli4R#jb4-EB=)&$pne1Oxpu0Bwv=bEODr+&VA?Venp|<T(CDNZNle4;;`W(FJ6$bLjTxh!nXi>I#$02`NG>pM6(r1tE_02}JlAy#M+30!mvrKvu(JmdguHXcVsV0zt>c*ajkH0Kh^Iad3vVU}w$<sQP-GGE#^q@zXDT4hKHFZ*T4;@6eusm;<qF<CTW~h9YkA_e=wF<kJZjnDxo6zY*AYg+G6yCP?mod@Eb@c9VItmne6BJ$2>tc^e2i^>Bi1t7hb}RbU!vLn6W@{8I7_0bV|%deuqij2r%aU6%#X`oD_>ARBk!l+`aD4e*~uI#nOx>Dd(ZMTdidUZ#D4rPew@t1S^n^Sod^6ya6L_~;%bw;+(+3+9!Hvb4$^)m7Jp&|fe=akJbAlZ%HZc?BVa$(j?{eh^RI7DX#vYmr_cX=dU*W&(7O9#L1<|LLj|H>nV^p-p+BM4l==rFb46X(-%OY}6Hw$RnE97c-ZsvHpr0WfsaD1HRn10Rp*YZ5FC%Mr^}2Caon0#&Iyfikv3^*LtkZdz_3^cw#q~s`RhKtf67q9gmcUkh1`>4?z_&y04nDR&b&L9oSM~R_YM=SbacK%Gw@ecp$GaqrV2Pbf(g0lpTwhs!V8x?r*m=SUcdLFKE<#*6B?(;_u18OOiorRcSXl}yM-Fwb;z_cAwZPNI&ad5jZjbM=;~UFc7DQuQn!?IWgB(cnD*g}cez-%D$KSXtft3P@cgh6&H$j%cePV2X;<S>%dB@7{ZV^C<``6r)0%{Q;2X2UrjTFEJB~*ggy4Z?Pf+QgRN{RiHzE`j<49|jRStdLvO9tLn;%e$8uyyW2iSYrfG;*pmuP(wXQ_Zf%reZ=o5$qkFQn|dSl<}DCAP61rg7X)zh3$4*c@S{EESiys4(`>uf36p?s>IWoAHGOxcH2;b^6E@*aPOvrf4_gkkf|TTFLbZOf9LrkdVKG{iv44T')).decode('utf8')


def get_studio_html(mode: str = "page", initial_context: dict[str, Any] | None = None) -> str:
    """Return the complete 100% offline self-contained Studio HTML5/WebGL2 application.

    Args:
        mode: `"page"` for the wide 3-column OrcaSlicer tab, or `"dock"` for the
            compact right-side docked panel beside OrcaSlicer's 3D Plater.
        initial_context: Optional initial state dictionary (`lang`, `theme`,
            `printer`, `builtin_presets`, `user_presets`, `params`, `export_dir`).
    """
    norm_mode = "dock" if str(mode or "").strip().lower() == "dock" else "page"
    ctx: dict[str, Any] = copy.deepcopy(initial_context) if isinstance(initial_context, dict) else {}

    norm_lang = normalize_language(ctx.get("lang"))
    ctx["lang"] = norm_lang

    theme_raw = str(ctx.get("theme") or "dark").strip().lower()
    norm_theme = "light" if theme_raw == "light" else "dark"

    fallback_params = copy.deepcopy(DEFAULT_PARAMS) if isinstance(DEFAULT_PARAMS, dict) else None
    fallback_presets = copy.deepcopy(BUILTIN_PRESETS) if isinstance(BUILTIN_PRESETS, list) else []

    boot_payload: dict[str, Any] = {
        "mode": norm_mode,
        "initial_context": ctx,
        "fallback_params": fallback_params,
        "fallback_presets": fallback_presets,
    }

    html = _STUDIO_UI_HTML_TEMPLATE
    html = html.replace("__VASE_LOCALE_VOCABULARY__", _studio_ui_safe_json(locale_rows()))
    html = html.replace("__INITIAL_LANG__", norm_lang)
    html = html.replace("__INITIAL_THEME__", norm_theme)
    html = html.replace("__INITIAL_MODE__", norm_mode)
    html = html.replace("__ORCA_VASE_STUDIO_BOOT_JSON__", _studio_ui_safe_json(boot_payload))
    return html

# ===========================================================================
# MODULE: vase_studio.plugin_main
# ===========================================================================

pass  # [bundled] hoisted __future__ import

from collections.abc import Sequence
import copy
import ctypes
import json
import locale
import math
import os
import re
import sys
import threading
import time
import types
from pathlib import Path
from typing import Any, Callable
pass  # [bundled] resolved intra-package import

# Intra-package imports (stripped cleanly when bundled into single-file PEP 723 script)
if "normalize_params" not in globals():
    pass  # [bundled] resolved intra-package import
    pass  # [bundled] resolved intra-package import
    pass  # [bundled] resolved intra-package import
    pass  # [bundled] resolved intra-package import
    pass  # [bundled] resolved intra-package import
    pass  # [bundled] resolved intra-package import


# ---------------------------------------------------------------------------
# OrcaSlicer `orca` Native Binding Import (with standalone fallback stub)
# ---------------------------------------------------------------------------


def _build_fallback_orca_module() -> types.ModuleType:
    """Create a lightweight stand-in when imported outside OrcaSlicer."""
    mod = types.ModuleType("orca")
    mod._registered_capabilities = []
    mod._requested_permissions = {}
    mod._plugin_cls = None
    mod._saved_configs = {}

    class PluginType:
        PrinterConnection = "PrinterConnection"
        Pages = "Pages"
        Analysis = "Analysis"
        Importer = "Importer"
        Exporter = "Exporter"
        Visualization = "Visualization"
        Script = "Script"
        SlicingPipeline = "SlicingPipeline"
        ResourceTexture = "ResourceTexture"
        Unknown = "Unknown"

    class LifecycleEvent:
        NewProject = "NewProject"
        ProjectOpened = "ProjectOpened"
        ProjectBeforeSave = "ProjectBeforeSave"
        ProjectAfterSave = "ProjectAfterSave"
        ProjectClosed = "ProjectClosed"
        ProjectDirtyChanged = "ProjectDirtyChanged"
        SliceStarted = "SliceStarted"
        SliceGeometryFinished = "SliceGeometryFinished"
        GCodeExportStarted = "GCodeExportStarted"
        GCodeExportFinished = "GCodeExportFinished"
        SlicingJobComplete = "SlicingJobComplete"
        ObjectAdded = "ObjectAdded"
        ObjectDeleted = "ObjectDeleted"
        ObjectTransformed = "ObjectTransformed"
        ObjectChanged = "ObjectChanged"
        ObjectRenamed = "ObjectRenamed"
        PlateCreated = "PlateCreated"
        PlateDeleted = "PlateDeleted"
        PlateSelected = "PlateSelected"
        PlateRenamed = "PlateRenamed"
        PresetSelected = "PresetSelected"
        PresetSaved = "PresetSaved"

    class LifecycleEvtCode:
        Ok = 0
        Warn = 1
        Error = 2

    class PythonPluginBase:
        def __init__(self) -> None:
            pass

        def get_name(self) -> str:
            return ""

        def get_type(self) -> str:
            return PluginType.Unknown

        def on_load(self) -> None:
            pass

        def on_unload(self) -> None:
            pass

        def on_cancelled(self) -> None:
            pass

        def on_lifecycle_event(self, event: Any, ctx: Any = None) -> None:
            pass

        def has_config_ui(self) -> bool:
            return False

        def get_config_ui(self) -> str:
            return ""

        def get_default_config(self) -> dict[str, Any]:
            return {}

        def get_config(self) -> str:
            raw = mod._saved_configs.get(self.__class__.__name__)
            if raw is not None:
                return raw
            default_cfg = self.get_default_config()
            return json.dumps(default_cfg) if isinstance(default_cfg, dict) else "{}"

        def get_config_version(self) -> str:
            return "1.1.1"

        def save_config(self, config: str) -> bool:
            try:
                parsed = json.loads(config)
                if not isinstance(parsed, dict):
                    return False
            except Exception:
                return False
            mod._saved_configs[self.__class__.__name__] = str(config)
            return True

    class BasePlugin:
        def __init__(self) -> None:
            pass

        def register_capabilities(self) -> None:
            pass

    class PagesPluginCapabilityBase(PythonPluginBase):
        def get_type(self) -> str:
            return PluginType.Pages

        def get_ui(self) -> str:
            return ""

        def get_icon(self) -> str:
            return ""

        def on_message(self, data: Any) -> None:
            pass

        def post_message(self, data: Any) -> None:
            pass

    class ScriptPluginCapabilityBase(PythonPluginBase):
        def get_type(self) -> str:
            return PluginType.Script

        def execute(self) -> Any:
            return None

    class PluginResult:
        Success = 0
        Skipped = 1
        RecoverableError = 2
        FatalError = 3

    class ExecutionResult:
        def __init__(self, status: int = 0, message: str = "", data: str = "") -> None:
            self.status = status
            self.message = message
            self.data = data

        @classmethod
        def success(cls, message: str = "", data: str = "") -> "ExecutionResult":
            return cls(PluginResult.Success, message, data)

        @classmethod
        def skipped(cls, message: str = "") -> "ExecutionResult":
            return cls(PluginResult.Skipped, message, "")

        @classmethod
        def failure(cls, status: int, message: str, data: str = "") -> "ExecutionResult":
            return cls(status, message, data)

    class NotificationLevel:
        ProgressBarNotificationLevel = "ProgressBarNotificationLevel"
        HintNotificationLevel = "HintNotificationLevel"
        RegularNotificationLevel = "RegularNotificationLevel"
        PrintInfoNotificationLevel = "PrintInfoNotificationLevel"
        PrintInfoShortNotificationLevel = "PrintInfoShortNotificationLevel"
        ImportantNotificationLevel = "ImportantNotificationLevel"
        WarningNotificationLevel = "WarningNotificationLevel"
        SeriousWarningNotificationLevel = "SeriousWarningNotificationLevel"
        ErrorNotificationLevel = "ErrorNotificationLevel"

    def plugin_decorator(cls: type) -> type:
        mod._plugin_cls = cls
        return cls

    def register_capability(cap_cls: type) -> None:
        mod._registered_capabilities.append(cap_cls)

    def request_permissions(**kwargs: Any) -> None:
        mod._requested_permissions.update(kwargs)

    pages_mod = types.ModuleType("orca.pages")
    pages_mod.PagesPluginCapabilityBase = PagesPluginCapabilityBase

    script_mod = types.ModuleType("orca.script")
    script_mod.ScriptPluginCapabilityBase = ScriptPluginCapabilityBase

    plugin_sub = types.ModuleType("orca.host.plugin")
    plugin_sub.storage = lambda: str(Path(__file__).resolve().parent)

    host_mod = types.ModuleType("orca.host")
    host_mod.app_info = lambda: {"version": "2.5.1", "language": "pt_BR"}
    host_mod.app_language = lambda: "pt_BR"
    host_mod.preset_bundle = lambda: None
    host_mod.plater = lambda: None
    host_mod.model = lambda: None
    host_mod.selected_printer = lambda: None
    host_mod.plugin = plugin_sub
    host_mod.ui = types.SimpleNamespace(
        NotificationLevel=NotificationLevel,
        create_dock_panel=None,
        create_window=None,
        push_notification=None,
        message=None,
    )
    host_mod.preset = types.SimpleNamespace(
        process=None,
        printer=None,
        filament=None,
    )

    mod.base = BasePlugin
    mod.PythonPluginBase = PythonPluginBase
    mod.PluginType = PluginType
    mod.PluginResult = PluginResult
    mod.LifecycleEvent = LifecycleEvent
    mod.LifecycleEvtCode = LifecycleEvtCode
    mod.ExecutionResult = ExecutionResult
    mod.plugin = plugin_decorator
    mod.register_capability = register_capability
    mod.request_permissions = request_permissions
    mod.pages = pages_mod
    mod.script = script_mod
    mod.host = host_mod

    return mod


try:
    import orca  # type: ignore[import-not-found]
except ImportError:
    orca = _build_fallback_orca_module()


PLUGIN_SLUG = "orca_vase_generator"
WM_COPYDATA = 0x004A
SMTO_ABORTIFHUNG = 0x0002
ORCA_OTHER_INSTANCE_DWDATA = 1

ICON_SVG_CONTENT: str = """\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64" fill="none">
  <defs>
    <linearGradient id="orcaBodyFill" x1="13" y1="10" x2="50" y2="55" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="46%" stop-color="#00BFA5"/>
      <stop offset="100%" stop-color="#00897B"/>
    </linearGradient>
    <linearGradient id="orcaBodyShade" x1="12" y1="32" x2="52" y2="36" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="0.32"/>
      <stop offset="45%" stop-color="#00BFA5" stop-opacity="0.0"/>
      <stop offset="100%" stop-color="#004D40" stop-opacity="0.46"/>
    </linearGradient>
    <linearGradient id="orcaRimStroke" x1="14" y1="9" x2="50" y2="56" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="55%" stop-color="#00BFA5"/>
      <stop offset="100%" stop-color="#00897B"/>
    </linearGradient>
    <linearGradient id="orcaWaveLight" x1="16" y1="14" x2="46" y2="53" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#B2FFFC" stop-opacity="0.92"/>
      <stop offset="50%" stop-color="#00E5FF" stop-opacity="0.78"/>
      <stop offset="100%" stop-color="#00BFA5" stop-opacity="0.35"/>
    </linearGradient>
    <linearGradient id="orcaMouthWall" x1="18" y1="8" x2="46" y2="15" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FFE082"/>
      <stop offset="52%" stop-color="#FFB74D"/>
      <stop offset="100%" stop-color="#F57C00"/>
    </linearGradient>
    <linearGradient id="orcaMouthCavity" x1="22" y1="9" x2="42" y2="15" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#6D3605"/>
      <stop offset="48%" stop-color="#B45309"/>
      <stop offset="85%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#FFB74D"/>
    </linearGradient>
    <clipPath id="orcaVaseClip">
      <path d="M18.5 11.5 C18.5 15.2 20.4 18.2 19.6 21.6 C18.4 26.5 12.6 31.2 13.0 38.0 C13.4 45.0 17.6 50.6 21.8 53.2 C24.8 55.0 28.2 55.8 32.0 55.8 C35.8 55.8 39.2 55.0 42.2 53.2 C46.4 50.6 50.6 45.0 51.0 38.0 C51.4 31.2 45.6 26.5 44.4 21.6 C43.6 18.2 45.5 15.2 45.5 11.5 Z"/>
    </clipPath>
  </defs>

  <!-- Subtle CAD Plater Base Ring -->
  <ellipse cx="32" cy="54.2" rx="22.5" ry="5.6" stroke="#00BFA5" stroke-width="1.25" stroke-opacity="0.48"/>
  <path d="M13.5 54.2 H50.5 M21.0 50.0 L43.0 58.2 M43.0 50.0 L21.0 58.2" stroke="#00E5FF" stroke-width="0.75" stroke-opacity="0.26" stroke-linecap="round"/>

  <!-- Sculpted Organic-Wave Vase Silhouette -->
  <path d="M18.5 11.5 C18.5 15.2 20.4 18.2 19.6 21.6 C18.4 26.5 12.6 31.2 13.0 38.0 C13.4 45.0 17.6 50.6 21.8 53.2 C24.8 55.0 28.2 55.8 32.0 55.8 C35.8 55.8 39.2 55.0 42.2 53.2 C46.4 50.6 50.6 45.0 51.0 38.0 C51.4 31.2 45.6 26.5 44.4 21.6 C43.6 18.2 45.5 15.2 45.5 11.5 Z"
        fill="url(#orcaBodyFill)"/>
  <path d="M18.5 11.5 C18.5 15.2 20.4 18.2 19.6 21.6 C18.4 26.5 12.6 31.2 13.0 38.0 C13.4 45.0 17.6 50.6 21.8 53.2 C24.8 55.0 28.2 55.8 32.0 55.8 C35.8 55.8 39.2 55.0 42.2 53.2 C46.4 50.6 50.6 45.0 51.0 38.0 C51.4 31.2 45.6 26.5 44.4 21.6 C43.6 18.2 45.5 15.2 45.5 11.5 Z"
        fill="url(#orcaBodyShade)"/>

  <!-- Helical Spiral Wave Ribs (Clipped Inside Vase Body) -->
  <g clip-path="url(#orcaVaseClip)">
    <!-- Deep sculpted wave valleys -->
    <path d="M15.0 14.0 C13.5 24.5 21.5 34.0 26.5 44.5 C29.0 49.8 31.8 54.0 34.5 57.0"
          stroke="#00695C" stroke-width="2.4" stroke-linecap="round" stroke-opacity="0.45"/>
    <path d="M23.5 13.0 C21.0 23.5 30.5 33.5 36.0 44.5 C38.8 50.0 41.0 53.8 43.2 56.5"
          stroke="#00695C" stroke-width="2.4" stroke-linecap="round" stroke-opacity="0.48"/>
    <path d="M33.0 13.0 C31.0 23.5 40.0 33.0 45.5 43.8 C47.8 48.2 49.5 51.5 51.0 54.0"
          stroke="#004D40" stroke-width="2.4" stroke-linecap="round" stroke-opacity="0.50"/>

    <!-- Crisp specular spiral wave crests -->
    <path d="M17.2 14.0 C15.2 24.2 23.5 33.8 28.6 44.5 C31.2 49.8 33.8 53.8 36.2 56.8"
          stroke="url(#orcaWaveLight)" stroke-width="1.75" stroke-linecap="round"/>
    <path d="M25.8 13.2 C23.6 23.4 32.8 33.4 38.2 44.2 C40.8 49.5 42.8 53.2 44.8 55.8"
          stroke="url(#orcaWaveLight)" stroke-width="1.85" stroke-linecap="round"/>
    <path d="M35.2 13.5 C33.2 23.2 42.0 32.6 47.2 43.2 C49.2 47.4 50.6 50.5 52.0 53.0"
          stroke="#00E5FF" stroke-width="1.55" stroke-linecap="round" stroke-opacity="0.68"/>
    <path d="M12.2 28.0 C15.0 35.5 19.8 43.2 24.8 51.8 C26.2 54.2 27.6 55.6 29.0 56.8"
          stroke="#80FFEA" stroke-width="1.45" stroke-linecap="round" stroke-opacity="0.65"/>
  </g>

  <!-- Crisp Outer Silhouette Contour (Native Contrast on Light & Dark Tabs) -->
  <path d="M18.5 11.5 C18.5 15.2 20.4 18.2 19.6 21.6 C18.4 26.5 12.6 31.2 13.0 38.0 C13.4 45.0 17.6 50.6 21.8 53.2 C24.8 55.0 28.2 55.8 32.0 55.8 C35.8 55.8 39.2 55.0 42.2 53.2 C46.4 50.6 50.6 45.0 51.0 38.0 C51.4 31.2 45.6 26.5 44.4 21.6 C43.6 18.2 45.5 15.2 45.5 11.5"
        stroke="url(#orcaRimStroke)" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Warm Amber-Gold Open Mouth Wall Rim & Hollow Interior -->
  <ellipse cx="32" cy="11.5" rx="13.5" ry="4.5" fill="url(#orcaMouthWall)" stroke="#FFB74D" stroke-width="1.1"/>
  <ellipse cx="32" cy="11.6" rx="10.1" ry="3.05" fill="url(#orcaMouthCavity)" stroke="#FFF3E0" stroke-width="0.65" stroke-opacity="0.65"/>
  <!-- Inner Cavity Spiral Depth Hint -->
  <path d="M25.5 10.2 C26.8 11.8 28.8 13.1 31.2 14.3 M32.8 9.0 C34.2 10.9 36.2 12.5 38.4 13.8"
        stroke="#FFE082" stroke-width="0.9" stroke-linecap="round" stroke-opacity="0.45"/>
</svg>
"""


# ---------------------------------------------------------------------------
# Environment, Host Inspection & In-Process Win32 `WM_COPYDATA` IPC Helpers
# ---------------------------------------------------------------------------


def _is_native_orca_host() -> bool:
    """Return True only when running inside the real C++ pybind11 OrcaSlicer host."""
    base_cls = getattr(orca, "base", None)
    return base_cls is not None and type(base_cls).__name__ == "pybind11_type"


def _is_mock_callable(obj: Any) -> bool:
    """Detect unittest.mock objects without importing unittest.mock eagerly."""
    cls_mod = getattr(type(obj), "__module__", "")
    return cls_mod.startswith("unittest.mock")


def _orca_os_default_data_dir() -> Path:
    """Resolve OrcaSlicer's default `data_dir()` across Windows, macOS, and Linux."""
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA", "").strip()
        if appdata:
            return Path(appdata) / "OrcaSlicer"
        return Path.home() / "AppData" / "Roaming" / "OrcaSlicer"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "OrcaSlicer"
    xdg_cfg = os.environ.get("XDG_CONFIG_HOME", "").strip()
    if xdg_cfg:
        return Path(xdg_cfg) / "OrcaSlicer"
    return Path.home() / ".config" / "OrcaSlicer"


def _orca_data_dir() -> Path:
    """Resolve OrcaSlicer's active `data_dir()`, honoring custom/portable `--datadir` or Flatpak
    installations whenever `__file__` resides inside an `orca_plugins` directory tree on the host OS.
    """
    platform_matches_host = (sys.platform == "win32") == (os.name == "nt")
    if platform_matches_host:
        try:
            here = Path(__file__).resolve()
            for parent in here.parents:
                if parent.name == "orca_plugins" and parent.parent != parent:
                    return parent.parent
        except Exception:
            pass
    return _orca_os_default_data_dir()


def _default_installed_plugin_dir() -> Path:
    return _orca_data_dir() / "orca_plugins" / PLUGIN_SLUG


def _default_plugin_data_dir() -> Path:
    return _orca_data_dir() / "orca_plugins" / "plugin_data" / PLUGIN_SLUG


def _resolve_storage_dir(*, in_callback: bool = True) -> Path:
    """Resolve current plugin storage folder safely (`orca.host.plugin.storage()` inside callbacks)."""
    # 1. Inside capability callbacks, query canonical `orca.host.plugin.storage()` first
    if in_callback:
        host_plugin = getattr(getattr(orca, "host", None), "plugin", None)
        top_plugin = getattr(orca, "plugin", None)
        holders = [host_plugin]
        if isinstance(top_plugin, types.ModuleType):
            holders.append(top_plugin)
        for holder in holders:
            storage_fn = getattr(holder, "storage", None)
            if callable(storage_fn):
                try:
                    raw = storage_fn()
                    if isinstance(raw, (str, os.PathLike)) and str(raw).strip():
                        return Path(raw)
                except Exception:
                    pass

    # 2. In native OrcaSlicer, prefer `plugin_data/orca_vase_generator`
    if _is_native_orca_host():
        data_dir = _default_plugin_data_dir()
        try:
            data_dir.mkdir(parents=True, exist_ok=True)
            return data_dir
        except Exception:
            pass

    # 3. Fallback to __file__ parent if available
    try:
        here = Path(__file__).resolve().parent
        if here.exists():
            return here
    except Exception:
        pass

    return _default_installed_plugin_dir()


def _format_other_instance_payload(file_paths: Sequence[str | Path]) -> str:
    """Format Win32 `WM_COPYDATA` payload matching `OrcaSlicer.dll` `unescape_strings_cstyle`.

    Produces `"orca-slicer.exe";"<resolved_path_1>";...` where every token escapes
    `\\` -> `\\\\`, `"` -> `\\"`, `\\r` -> `\\r`, `\\n` -> `\\n`, wrapped in double quotes and
    joined by `;` with NO trailing `;` (`OtherInstanceMessageHandler::handle_message` skips `args[0]`).
    """
    resolved_files = [str(Path(p).resolve()) for p in file_paths if str(p).strip()]
    if not resolved_files:
        raise ValueError("file_paths must contain at least one model path")

    tokens = ["orca-slicer.exe", *resolved_files]
    escaped: list[str] = []
    for tok in tokens:
        s = (
            tok.replace("\\", "\\\\")
            .replace('"', '\\"')
            .replace("\r", "\\r")
            .replace("\n", "\\n")
        )
        escaped.append(f'"{s}"')
    return ";".join(escaped)


def _find_orca_mainframe_hwnd(target_pid: int | None = None) -> int | None:
    """Locate OrcaSlicer's `MainFrame` `wxWindowNR` `HWND` in `target_pid` (`os.getpid()` by default).

    Prefers `wxWindowNR` windows marked with OrcaSlicer's `Instance_Hash_Minor` or
    `Instance_Hash_Major` properties, falling back to a visible top-level `wxWindowNR` of that PID.
    """
    if sys.platform != "win32":
        return None

    from ctypes import wintypes

    pid = int(target_pid) if target_pid is not None else os.getpid()
    user32 = ctypes.windll.user32

    WNDENUMPROC = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)

    enum_windows = user32.EnumWindows
    if not _is_mock_callable(enum_windows):
        enum_windows.argtypes = [WNDENUMPROC, wintypes.LPARAM]
        enum_windows.restype = wintypes.BOOL

    get_pid = user32.GetWindowThreadProcessId
    if not _is_mock_callable(get_pid):
        get_pid.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.DWORD)]
        get_pid.restype = wintypes.DWORD

    get_class = user32.GetClassNameW
    if not _is_mock_callable(get_class):
        get_class.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
        get_class.restype = ctypes.c_int

    get_prop = user32.GetPropW
    if not _is_mock_callable(get_prop):
        get_prop.argtypes = [wintypes.HWND, wintypes.LPCWSTR]
        get_prop.restype = wintypes.HANDLE

    is_visible = user32.IsWindowVisible
    if not _is_mock_callable(is_visible):
        is_visible.argtypes = [wintypes.HWND]
        is_visible.restype = wintypes.BOOL

    get_parent = user32.GetParent
    if not _is_mock_callable(get_parent):
        get_parent.argtypes = [wintypes.HWND]
        get_parent.restype = wintypes.HWND

    hash_visible: list[int] = []
    hash_any: list[int] = []
    fallback_visible: list[int] = []

    def _enum_cb(hwnd: int, _lparam: int) -> bool:
        if not hwnd:
            return True
        win_pid = wintypes.DWORD(0)
        get_pid(hwnd, ctypes.byref(win_pid))
        if int(win_pid.value) != pid:
            return True

        cls_buf = ctypes.create_unicode_buffer(64)
        cls_len = get_class(hwnd, cls_buf, 64)
        if cls_len <= 0 or cls_buf.value != "wxWindowNR":
            return True

        minor = get_prop(hwnd, "Instance_Hash_Minor")
        major = get_prop(hwnd, "Instance_Hash_Major")
        vis = bool(is_visible(hwnd))
        hwnd_int = int(hwnd)

        if bool(minor) or bool(major):
            if vis:
                hash_visible.append(hwnd_int)
            else:
                hash_any.append(hwnd_int)
        elif vis and not get_parent(hwnd):
            fallback_visible.append(hwnd_int)
        return True

    cb_ref = WNDENUMPROC(_enum_cb)
    enum_windows(cb_ref, 0)

    if hash_visible:
        return hash_visible[0]
    if hash_any:
        return hash_any[0]
    if fallback_visible:
        return fallback_visible[0]
    return None


class _COPYDATASTRUCT(ctypes.Structure):
    _fields_ = [
        ("dwData", ctypes.c_size_t),
        ("cbData", ctypes.c_uint32),
        ("lpData", ctypes.c_void_p),
    ]


def _dispatch_copydata_to_hwnd(
    hwnd: int,
    payload_str: str,
    timeout_ms: int = 5000,
) -> tuple[bool, str]:
    """Send UTF-16LE `WM_COPYDATA` (`dwData = 1`) to `hwnd` via `SendMessageTimeoutW` (`0x0002`)."""
    if not hwnd or int(hwnd) <= 0:
        return (False, "OrcaSlicer MainFrame HWND not found")
    if not payload_str:
        return (False, "Empty WM_COPYDATA payload")
    if sys.platform != "win32":
        return (False, "WM_COPYDATA requires win32")

    from ctypes import wintypes

    wchar_buf = ctypes.create_unicode_buffer(payload_str)
    cds = _COPYDATASTRUCT(
        dwData=ORCA_OTHER_INSTANCE_DWDATA,
        cbData=ctypes.sizeof(wchar_buf),
        lpData=ctypes.cast(wchar_buf, ctypes.c_void_p),
    )
    result = ctypes.c_size_t(0)

    user32 = ctypes.windll.user32
    send_msg = user32.SendMessageTimeoutW
    if not _is_mock_callable(send_msg):
        send_msg.argtypes = [
            wintypes.HWND,
            wintypes.UINT,
            wintypes.WPARAM,
            ctypes.c_void_p,
            wintypes.UINT,
            wintypes.UINT,
            ctypes.POINTER(ctypes.c_size_t),
        ]
        send_msg.restype = ctypes.c_size_t

    ret = send_msg(
        int(hwnd),
        WM_COPYDATA,
        0,
        ctypes.byref(cds),
        SMTO_ABORTIFHUNG,
        max(100, int(timeout_ms)),
        ctypes.byref(result),
    )
    if not ret:
        err = ctypes.windll.kernel32.GetLastError()
        return (False, f"SendMessageTimeoutW failed (GetLastError={err})")
    return (True, "ok")


def _dispatch_non_win32_plater_open(file_paths: Sequence[str | Path]) -> tuple[bool, str]:
    """Graceful macOS / Linux Plater open fallback when running outside Win32 (`WM_COPYDATA`)."""
    resolved = [str(Path(p).resolve()) for p in file_paths if str(p).strip()]
    if not resolved:
        return (False, "No model files to open")
    if not _is_native_orca_host():
        return (False, f"WM_COPYDATA requires win32 (platform={sys.platform})")
    try:
        import subprocess

        if sys.platform == "darwin":
            subprocess.Popen(
                ["open", "-a", "OrcaSlicer", *resolved],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return (True, "darwin_open_ok")
        # Linux / POSIX: try sibling `orca-slicer` binary with `--single-instance`, else `xdg-open`
        exe_dir = Path(sys.executable).resolve().parent
        for cand_bin in (exe_dir / "orca-slicer", exe_dir.parent / "orca-slicer", exe_dir.parent / "bin" / "orca-slicer"):
            if cand_bin.is_file():
                subprocess.Popen(
                    [str(cand_bin), "--single-instance", *resolved],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
                return (True, "linux_single_instance_ok")
        subprocess.Popen(
            ["xdg-open", resolved[0]],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return (True, "xdg_open_ok")
    except Exception as exc:
        return (False, f"Non-win32 Plater open fallback skipped: {exc}")


def _slugify_filename(name: str, fallback: str = "vaso") -> str:
    cleaned = re.sub(r"[^\w\-. ]+", "", str(name or "").strip(), flags=re.ASCII)
    cleaned = re.sub(r"\s+", "_", cleaned).strip("._-")
    if not cleaned:
        return fallback
    return cleaned[:64]


def _extract_first_float(val: Any, default: float) -> float:
    if val is None:
        return default
    if isinstance(val, (int, float)) and not isinstance(val, bool):
        f = float(val)
        return f if f == f else default
    if isinstance(val, (list, tuple)):
        for item in val:
            res = _extract_first_float(item, float("nan"))
            if res == res:
                return res
        return default
    s = str(val).strip()
    if not s:
        return default
    m = re.search(r"[-+]?\d*\.?\d+", s)
    if not m:
        return default
    try:
        return float(m.group(0))
    except ValueError:
        return default


def _parse_bed_geometry(
    raw: Any,
    default_x: float = 220.0,
    default_y: float = 220.0,
) -> dict[str, Any]:
    """Parse OrcaSlicer `printable_area` / `bed_shape` polygon into bed dimensions and shape.

    Supports:
    - `['0x0', '220x0', '220x220', '0x220']`
    - `'0x0,220x0,220x220,0x220'` or semicolon-separated strings
    - `[[0, 0], [220, 0], [220, 220], [0, 220]]` or numpy arrays
    - `orca.host.Point` / `Pointf` objects exposing `.x` / `.y` or dicts `{'x': ..., 'y': ...}`
    - Circular / delta beds with `> 6` polygon vertices around origin or bed center
    """
    fallback = {
        "bed_x": float(default_x),
        "bed_y": float(default_y),
        "bed_shape": "rectangular",
        "bed_center": [round(float(default_x) * 0.5, 2), round(float(default_y) * 0.5, 2)],
    }
    if raw is None:
        return fallback

    xs: list[float] = []
    ys: list[float] = []

    tokens: list[Any]
    if isinstance(raw, str):
        s = raw.strip()
        if not s:
            return fallback
        if s.startswith("["):
            try:
                parsed = json.loads(s)
                tokens = parsed if isinstance(parsed, list) else [s]
            except Exception:
                tokens = re.split(r"[;,]+", s)
        else:
            tokens = re.split(r"[;,]+", s)
    elif isinstance(raw, Sequence) and not isinstance(raw, (bytes, bytearray)):
        tokens = list(raw)
    elif hasattr(raw, "__iter__"):
        try:
            tokens = list(raw)
        except Exception:
            return fallback
    else:
        return fallback

    for tok in tokens:
        if tok is None:
            continue
        if isinstance(tok, str):
            m = re.search(r"([-+]?\d*\.?\d+)\s*[xX:,]\s*([-+]?\d*\.?\d+)", tok.strip())
            if m:
                try:
                    xs.append(float(m.group(1)))
                    ys.append(float(m.group(2)))
                except ValueError:
                    continue
        elif isinstance(tok, dict):
            if "x" in tok and "y" in tok:
                try:
                    xs.append(float(tok["x"]))
                    ys.append(float(tok["y"]))
                except (TypeError, ValueError):
                    continue
        elif hasattr(tok, "x") and hasattr(tok, "y"):
            try:
                xv = tok.x() if callable(tok.x) else tok.x
                yv = tok.y() if callable(tok.y) else tok.y
                xs.append(float(xv))
                ys.append(float(yv))
            except Exception:
                continue
        elif hasattr(tok, "__len__") and hasattr(tok, "__getitem__"):
            try:
                if len(tok) >= 2:
                    xs.append(float(tok[0]))
                    ys.append(float(tok[1]))
            except Exception:
                continue

    if len(xs) >= 2 and len(ys) >= 2:
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        dx = max_x - min_x
        dy = max_y - min_y
        cx = 0.5 * (min_x + max_x)
        cy = 0.5 * (min_y + max_y)

        if dx >= 30.0 and dy >= 30.0:
            if len(xs) > 6:
                mean_x = sum(xs) / len(xs)
                mean_y = sum(ys) / len(ys)
                best_cx, best_cy = cx, cy
                best_radii = [math.hypot(x - cx, y - cy) for x, y in zip(xs, ys)]
                mean_radii = [math.hypot(x - mean_x, y - mean_y) for x, y in zip(xs, ys)]
                if (max(mean_radii) - min(mean_radii)) < (max(best_radii) - min(best_radii)):
                    best_cx, best_cy = mean_x, mean_y
                    best_radii = mean_radii

                r_max = max(best_radii)
                r_min = min(best_radii)
                if r_max >= 15.0 and (r_max - r_min) / r_max <= 0.12:
                    r_avg = sum(best_radii) / len(best_radii)
                    diam = round(2.0 * r_avg, 2)
                    if abs(diam - round(diam)) < 0.08:
                        diam = float(round(diam))
                    return {
                        "bed_x": float(diam),
                        "bed_y": float(diam),
                        "bed_shape": "circular",
                        "bed_center": [round(best_cx, 2), round(best_cy, 2)],
                    }

            bx = round(dx, 2)
            by = round(dy, 2)
            return {
                "bed_x": float(bx),
                "bed_y": float(by),
                "bed_shape": "rectangular",
                "bed_center": [round(cx, 2), round(cy, 2)],
            }

    return fallback


def _parse_printable_area(raw: Any, default_x: float = 220.0, default_y: float = 220.0) -> tuple[float, float]:
    """Parse OrcaSlicer `printable_area` into `(bed_x_mm, bed_y_mm)`."""
    geom = _parse_bed_geometry(raw, default_x=default_x, default_y=default_y)
    return (float(geom["bed_x"]), float(geom["bed_y"]))


def _parse_line_width(raw: Any, nozzle_mm: float, fallback_raw: Any = None) -> float:
    """Parse OrcaSlicer line width (`'0.42'`, `'105%'`, `'0'`, `['110%']`) relative to `nozzle_mm`."""
    default_lw = round(max(0.15, min(3.0, float(nozzle_mm) * 1.05)), 3)

    def _parse_single(candidate: Any) -> float | None:
        if candidate is None or isinstance(candidate, bool):
            return None
        if isinstance(candidate, (list, tuple)):
            return _parse_single(candidate[0] if candidate else None)
        s = str(candidate).strip()
        if not s:
            return None
        if s.endswith("%"):
            pct = _extract_first_float(s[:-1], 0.0)
            if pct > 10.0:
                return round(max(0.15, min(3.0, float(nozzle_mm) * (pct / 100.0))), 3)
            return None
        val = _extract_first_float(s, 0.0)
        if val <= 0.05:
            return None
        return round(max(0.15, min(3.0, val)), 3)

    parsed = _parse_single(raw)
    if parsed is not None:
        return parsed
    if fallback_raw is not None:
        parsed_fb = _parse_single(fallback_raw)
        if parsed_fb is not None:
            return parsed_fb
    return default_lw


def _resolve_attr_or_call(obj: Any, attr_name: str) -> Any:
    """Read an attribute on a pybind11/mock object whether exposed as a property or 0-arg method."""
    if obj is None:
        return None
    try:
        val = getattr(obj, attr_name, None)
    except Exception:
        return None
    if val is None:
        return None
    if callable(val):
        try:
            return val()
        except Exception:
            return None
    return val


def _extract_preset_name(obj: Any, fallback: str = "") -> str:
    if obj is None:
        return fallback
    if isinstance(obj, str):
        return obj.strip() or fallback
    if isinstance(obj, (list, tuple)):
        for item in obj:
            got = _extract_preset_name(item, "")
            if got:
                return got
        return fallback
    if isinstance(obj, dict):
        for k in ("name", "preset_name", "printer_name", "id"):
            v = obj.get(k)
            if isinstance(v, str) and v.strip():
                return v.strip()
        return fallback
    for attr in ("name", "preset_name", "selected_preset_name"):
        val = _resolve_attr_or_call(obj, attr)
        if isinstance(val, str) and val.strip():
            return val.strip()
    return fallback


def _preset_get_value(preset_obj: Any, key: str) -> Any:
    """Read `config_value(key)` directly from an `orca.host.Preset` instance if available."""
    if preset_obj is None or isinstance(preset_obj, (str, bytes, dict, list, tuple)):
        return None
    for method_name in ("config_value", "full_config_value", "get"):
        fn = getattr(preset_obj, method_name, None)
        if callable(fn):
            try:
                val = fn(key)
                if val is not None and val != "" and val != []:
                    return val
            except Exception:
                continue
    return None


def _bundle_get_value(bundle: Any, key: str, preset_obj: Any = None) -> Any:
    from_preset = _preset_get_value(preset_obj, key)
    if from_preset is not None:
        return from_preset
    if bundle is None:
        return None
    for method_name in ("full_config_value", "config_value", "get"):
        fn = getattr(bundle, method_name, None)
        if callable(fn):
            try:
                val = fn(key)
                if val is not None and val != "" and val != []:
                    return val
            except Exception:
                continue
    return None


def _detect_language(app_info: dict[str, Any]) -> str:
    raw = app_info.get("language") or app_info.get("lang")
    if raw:
        return normalize_language(raw)
    try:
        detected = locale.getlocale()[0]
        if detected:
            return normalize_language(detected)
    except Exception:
        pass
    return "pt"


def _detect_theme(app_info: dict[str, Any]) -> str:
    theme_raw = str(app_info.get("theme") or app_info.get("color_mode") or "").strip().lower()
    if theme_raw == "light":
        return "light"
    if theme_raw == "dark":
        return "dark"
    if app_info.get("dark_mode") is False:
        return "light"
    return "dark"


def _make_execution_result_success(message: str) -> Any:
    exec_cls = getattr(orca, "ExecutionResult", None)
    if exec_cls is not None:
        success_fn = getattr(exec_cls, "success", None)
        if callable(success_fn):
            try:
                return success_fn(message)
            except TypeError:
                return success_fn(message, "")
        try:
            ok_code = getattr(getattr(orca, "PluginResult", None), "Success", 0)
            return exec_cls(ok_code, message, "")
        except Exception:
            pass
    return {"status": "Success", "message": message}


# ---------------------------------------------------------------------------
# Shared Studio Session & Message Router
# ---------------------------------------------------------------------------


class VaseStudioController:
    """Coordinates live host reading, mesh generation, exports, and Plater IPC."""

    def __init__(self) -> None:
        self._lock = threading.RLock()
        self._current_params: dict[str, Any] = normalize_params(DEFAULT_PARAMS)
        self._listeners: dict[str, Callable[[dict[str, Any]], None]] = {}
        self._manual_language: str | None = None
        self._language_loaded = False
        self._language_revision = 0
        self._last_language_requests: dict[str, int] = {}
        self._last_plater_worker: threading.Thread | None = None
        self._last_plater_outcome: dict[str, Any] = {}

    def _load_language_preferences(self) -> None:
        # Storage is callback-only in Orca: never consult it while importing or
        # registering capabilities. The first context read is a UI callback.
        with self._lock:
            if self._language_loaded:
                return
            self._language_loaded = True
            try:
                prefs = json.loads((_resolve_storage_dir() / "ui_preferences.json").read_text(encoding="utf8"))
                if isinstance(prefs, dict) and prefs.get("language"):
                    self._manual_language = normalize_language(prefs["language"])
            except (OSError, ValueError, TypeError):
                pass

    @property
    def current_params(self) -> dict[str, Any]:
        with self._lock:
            return copy.deepcopy(self._current_params)

    def set_current_params(self, raw: dict[str, Any] | None) -> dict[str, Any]:
        norm = normalize_params(raw)
        with self._lock:
            self._current_params = norm
            return copy.deepcopy(norm)

    def get_presets_dir(self) -> Path:
        base = _resolve_storage_dir()
        target = base / "presets"
        try:
            target.mkdir(parents=True, exist_ok=True)
            return target
        except Exception:
            return base

    def get_export_dir(self) -> Path:
        base = _resolve_storage_dir()
        target = base / "exports"
        try:
            target.mkdir(parents=True, exist_ok=True)
            return target
        except Exception:
            fallback = Path.home() / "Documents" / "OrcaVaseStudio"
            try:
                fallback.mkdir(parents=True, exist_ok=True)
                return fallback
            except Exception:
                return base

    def read_host_context(self) -> dict[str, Any]:
        """Defensively inspect `orca.host.app_info()`, `orca.host.app_language()`, and `orca.host.preset_bundle()`."""
        self._load_language_preferences()
        app_info: dict[str, Any] = {}
        host = getattr(orca, "host", None)
        if host is not None:
            app_info_fn = getattr(host, "app_info", None)
            if callable(app_info_fn):
                try:
                    info = app_info_fn()
                    if isinstance(info, dict):
                        app_info = dict(info)
                except Exception:
                    app_info = {}

            # Official Wiki API (`orca.host.app_language()` -> e.g. "en_US", "pt_BR")
            if not str(app_info.get("language") or app_info.get("lang") or "").strip():
                app_lang_fn = getattr(host, "app_language", None)
                if callable(app_lang_fn):
                    try:
                        lang_val = app_lang_fn()
                        if isinstance(lang_val, str) and lang_val.strip():
                            app_info["language"] = lang_val.strip()
                    except Exception:
                        pass

        lang = self._manual_language or _detect_language(app_info)
        theme = _detect_theme(app_info)
        theme_explicit = any(k in app_info for k in ("theme", "color_mode", "dark_mode"))
        orca_version = str(app_info.get("version") or "2.5.1")

        bundle = _resolve_attr_or_call(host, "preset_bundle") if host is not None else None

        printer_name = ""
        process_name = "0.20mm Standard"
        filament_name = "Generic PLA"

        active_printer_preset: Any = None
        active_process_preset: Any = None

        if bundle is not None:
            # 1. Inspect `bundle.printers` (`PresetCollection` on OrcaSlicer.dll v2.5.1)
            printers_col = _resolve_attr_or_call(bundle, "printers")
            if printers_col is not None:
                for attr in ("edited_preset", "get_edited_preset", "selected_preset", "get_selected_preset"):
                    cand = _resolve_attr_or_call(printers_col, attr)
                    if cand is not None:
                        if active_printer_preset is None:
                            active_printer_preset = cand
                        got = _extract_preset_name(cand, "")
                        if got:
                            printer_name = got
                            break
                if not printer_name:
                    for attr in ("selected_preset_name", "get_selected_preset_name"):
                        got = _extract_preset_name(_resolve_attr_or_call(printers_col, attr), "")
                        if got:
                            printer_name = got
                            break

            # 2. Inspect `bundle.current_printer_preset` (property or 0-arg method)
            cur_pr = _resolve_attr_or_call(bundle, "current_printer_preset")
            if cur_pr is not None:
                if active_printer_preset is None:
                    active_printer_preset = cur_pr
                if not printer_name:
                    printer_name = _extract_preset_name(cur_pr, "")

            # 3. Inspect `bundle.prints` (`PresetCollection`) & `current_process_preset` / `current_print_preset`
            prints_col = _resolve_attr_or_call(bundle, "prints")
            if prints_col is not None:
                for attr in ("edited_preset", "get_edited_preset", "selected_preset", "get_selected_preset"):
                    cand = _resolve_attr_or_call(prints_col, attr)
                    if cand is not None:
                        if active_process_preset is None:
                            active_process_preset = cand
                        got = _extract_preset_name(cand, "")
                        if got:
                            process_name = got
                            break

            for m in ("current_process_preset", "current_print_preset"):
                cand = _resolve_attr_or_call(bundle, m)
                if cand is not None:
                    if active_process_preset is None:
                        active_process_preset = cand
                    got = _extract_preset_name(cand, "")
                    if got:
                        process_name = got
                        break

            # 4. Inspect filament presets (`current_filament_preset_names`, `current_filament_presets`, `filaments`)
            got_fil = ""
            for m in ("current_filament_preset_names", "current_filament_presets"):
                fils = _resolve_attr_or_call(bundle, m)
                if isinstance(fils, (list, tuple)) and fils:
                    got_fil = _extract_preset_name(fils[0], "")
                    if got_fil:
                        filament_name = got_fil
                        break
            if not got_fil:
                fil_col = _resolve_attr_or_call(bundle, "filaments")
                if fil_col is not None:
                    for attr in ("edited_preset", "get_edited_preset", "selected_preset", "get_selected_preset"):
                        got_fil = _extract_preset_name(_resolve_attr_or_call(fil_col, attr), "")
                        if got_fil:
                            filament_name = got_fil
                            break

            # 5. Fallback preset IDs from resolved config keys
            if not printer_name:
                for key_id in ("printer_settings_id", "printer_model"):
                    p_id = _bundle_get_value(bundle, key_id, active_printer_preset)
                    got = _extract_preset_name(p_id, "")
                    if got:
                        printer_name = got
                        break

            if process_name == "0.20mm Standard":
                pr_id = _bundle_get_value(bundle, "print_settings_id", active_process_preset)
                got_pr = _extract_preset_name(pr_id, "")
                if got_pr:
                    process_name = got_pr

        # Optional fallback to `orca.host.selected_printer` if bundle had no printer name
        if not printer_name and host is not None:
            sel_pr = _resolve_attr_or_call(host, "selected_printer")
            printer_name = _extract_preset_name(sel_pr, "")

        if not printer_name:
            printer_name = "Default Printer"

        raw_area = _bundle_get_value(bundle, "printable_area", active_printer_preset)
        if raw_area is None or raw_area == "" or raw_area == []:
            raw_area = _bundle_get_value(bundle, "bed_shape", active_printer_preset)

        bed_geom = _parse_bed_geometry(raw_area, default_x=220.0, default_y=220.0)
        bed_x = float(bed_geom["bed_x"])
        bed_y = float(bed_geom["bed_y"])
        bed_shape = str(bed_geom["bed_shape"])
        bed_center = list(bed_geom["bed_center"])

        max_z = max(
            50.0,
            min(
                1000.0,
                _extract_first_float(
                    _bundle_get_value(bundle, "printable_height", active_printer_preset),
                    250.0,
                ),
            ),
        )
        nozzle_mm = max(
            0.15,
            min(
                2.0,
                _extract_first_float(
                    _bundle_get_value(bundle, "nozzle_diameter", active_printer_preset),
                    0.4,
                ),
            ),
        )
        layer_height_mm = max(
            0.04,
            min(
                1.2,
                _extract_first_float(
                    _bundle_get_value(bundle, "layer_height", active_process_preset),
                    0.2,
                ),
            ),
        )
        line_width_mm = _parse_line_width(
            _bundle_get_value(bundle, "outer_wall_line_width", active_process_preset),
            nozzle_mm=nozzle_mm,
            fallback_raw=_bundle_get_value(bundle, "line_width", active_process_preset),
        )
        top_shell_layers = int(
            round(
                _extract_first_float(
                    _bundle_get_value(bundle, "top_shell_layers", active_process_preset),
                    4.0,
                )
            )
        )
        raw_infill = _bundle_get_value(bundle, "sparse_infill_density", active_process_preset)
        if isinstance(raw_infill, (list, tuple)):
            raw_infill = raw_infill[0] if raw_infill else "15%"
        sparse_infill_density = str(raw_infill if raw_infill is not None else "15%").strip() or "15%"

        return {
            "lang": lang,
            "theme": theme,
            "theme_explicit": theme_explicit,
            "orca_version": orca_version,
            "printer_name": printer_name,
            "process_name": process_name,
            "filament_name": filament_name,
            "bed_x": float(bed_x),
            "bed_y": float(bed_y),
            "bed_shape": bed_shape,
            "bed_center": bed_center,
            "max_z": float(max_z),
            "nozzle_mm": float(nozzle_mm),
            "layer_height_mm": float(layer_height_mm),
            "line_width_mm": float(line_width_mm),
            "top_shell_layers": top_shell_layers,
            "sparse_infill_density": sparse_infill_density,
        }

    def read_full_host_config_snapshot(self, host_ctx: dict[str, Any] | None = None) -> dict[str, Any]:
        """Collect full resolved `project_settings` snapshot from `preset_bundle()` for `.3mf` export."""
        ctx = dict(host_ctx) if host_ctx is not None else self.read_host_context()
        project_settings: dict[str, Any] = {}

        host = getattr(orca, "host", None)
        bundle = None
        if host is not None:
            bundle_fn = getattr(host, "preset_bundle", None)
            if callable(bundle_fn):
                try:
                    bundle = bundle_fn()
                except Exception:
                    bundle = None

        if bundle is not None:
            keys_fn = getattr(bundle, "full_config_keys", None)
            val_fn = getattr(bundle, "full_config_value", None) or getattr(bundle, "config_value", None)
            if callable(keys_fn) and callable(val_fn):
                try:
                    keys = keys_fn()
                    if isinstance(keys, (list, tuple, set)):
                        for k in keys:
                            ks = str(k)
                            if not ks:
                                continue
                            try:
                                v = val_fn(ks)
                                if v is not None:
                                    project_settings[ks] = v
                            except Exception:
                                continue
                except Exception:
                    pass

        ctx["project_settings"] = project_settings
        return ctx

    def build_printer_payload(self, host_ctx: dict[str, Any] | None = None) -> dict[str, Any]:
        """Construct the UI-facing `printer` metadata dictionary from `host_ctx`."""
        ctx = host_ctx if isinstance(host_ctx, dict) else self.read_host_context()
        return {
            "name": ctx["printer_name"],
            "process_name": ctx["process_name"],
            "filament_name": ctx["filament_name"],
            "orca_version": ctx["orca_version"],
            "bed_x": ctx["bed_x"],
            "bed_y": ctx["bed_y"],
            "bed_shape": ctx.get("bed_shape", "rectangular"),
            "bed_center": ctx.get("bed_center", [round(ctx["bed_x"] * 0.5, 2), round(ctx["bed_y"] * 0.5, 2)]),
            "max_z": ctx["max_z"],
            "nozzle_mm": ctx["nozzle_mm"],
            "layer_height_mm": ctx["layer_height_mm"],
            "line_width_mm": ctx["line_width_mm"],
        }

    def build_initial_context(self, mode: str = "page") -> dict[str, Any]:
        host_ctx = self.read_host_context()
        presets_dir = self.get_presets_dir()
        export_dir = self.get_export_dir()
        params = self.current_params
        return {
            "mode": mode,
            "lang": host_ctx["lang"],
            "language_override": self._manual_language is not None,
            "language_revision": self._language_revision,
            "theme": host_ctx["theme"],
            "theme_explicit": bool(host_ctx.get("theme_explicit", False)),
            "printer": self.build_printer_payload(host_ctx),
            "builtin_presets": BUILTIN_PRESETS,
            "user_presets": load_user_presets(presets_dir),
            "params": params,
            "export_dir": str(export_dir),
        }

    def _prepare_effective_vase_params(
        self,
        params: dict[str, Any],
        *,
        is_stl_export: bool,
        include_saucer: bool,
    ) -> dict[str, Any]:
        """Ensure `.STL` exports (when `stl_always_open_hollow` is True) and Vase+Saucer combos
        never generate a sealed top-capped Spiral Vase solid block.
        """
        effective = copy.deepcopy(params)
        if str(effective.get("print_mode", "shelled_hollow")) == "spiral_vase":
            force_open_hollow = bool(include_saucer) or (
                bool(is_stl_export) and bool(effective.get("stl_always_open_hollow", True))
            )
            if force_open_hollow:
                effective["print_mode"] = "shelled_hollow"
                effective["wall_thickness_mm"] = max(
                    0.8,
                    float(effective.get("wall_thickness_mm", 2.4)),
                )
                effective["bottom_thickness_mm"] = max(
                    1.0,
                    float(effective.get("bottom_thickness_mm", 3.2)),
                )
        return effective

    def _compute_process_preset_updates(
        self,
        params: dict[str, Any],
        host_ctx: dict[str, Any],
        include_saucer: bool,
    ) -> dict[str, str]:
        """Build key/value strings for `orca.host.preset.process.begin_update()`."""
        print_mode = str(params.get("print_mode", "shelled_hollow"))
        use_spiral = (print_mode == "spiral_vase") and (not include_saucer)

        if use_spiral:
            smooth = bool(params.get("spiral_smooth", True))
            bottom_layers = max(2, min(15, int(params.get("spiral_bottom_layers", 5))))
            spiral_lw = max(0.40, min(1.20, float(params.get("spiral_line_width_mm", 0.65))))
            return {
                "spiral_mode": "1",
                "spiral_mode_smooth": "1" if smooth else "0",
                "wall_loops": "1",
                "top_shell_layers": "0",
                "sparse_infill_density": "0%",
                "bottom_shell_layers": str(bottom_layers),
                "outer_wall_line_width": f"{spiral_lw:.2f}",
            }

        # Shelled hollow mode OR multi-object plate (vase + saucer)
        lw = max(0.25, float(host_ctx.get("line_width_mm", 0.42)))
        lh = max(0.08, float(host_ctx.get("layer_height_mm", 0.20)))

        wall_mm = max(0.8, float(params.get("wall_thickness_mm", 2.4)))
        bot_mm = max(1.0, float(params.get("bottom_thickness_mm", 3.2)))
        wall_loops = max(2, min(15, int(round(wall_mm / (2.0 * lw)))))
        bottom_layers = max(3, min(125, int(round(bot_mm / lh))))

        updates: dict[str, str] = {
            "spiral_mode": "0",
            "spiral_mode_smooth": "0",
            "wall_loops": str(wall_loops),
            "bottom_shell_layers": str(bottom_layers),
        }
        if int(host_ctx.get("top_shell_layers", 4)) <= 0:
            updates["top_shell_layers"] = "4"
        if str(host_ctx.get("sparse_infill_density", "15%")).strip() in ("", "0", "0%"):
            updates["sparse_infill_density"] = "15%"
        return updates

    def _apply_process_presets(self, updates: dict[str, str]) -> dict[str, Any]:
        """Apply process preset changes on the calling background worker thread.

        NEVER call `orca.host.preset.process.begin_update()` on the wxWidgets UI thread!
        """
        outcome: dict[str, Any] = {"applied": False, "error": None}
        if not updates:
            return outcome
        try:
            host = getattr(orca, "host", None)
            preset_ns = getattr(host, "preset", None) if host is not None else None
            process_ed = getattr(preset_ns, "process", None) if preset_ns is not None else None
            begin_fn = getattr(process_ed, "begin_update", None) if process_ed is not None else None
            if not callable(begin_fn):
                return outcome

            tx = begin_fn()
            if tx is None:
                return outcome

            staged_any = False
            for key, val in updates.items():
                try:
                    tx.set(str(key), str(val))
                    staged_any = True
                except Exception:
                    continue

            if staged_any:
                commit_fn = getattr(tx, "commit", None)
                if callable(commit_fn):
                    commit_fn()
                outcome["applied"] = True
        except Exception as exc:
            outcome["error"] = str(exc)
        return outcome

    def _apply_process_presets_async(
        self,
        updates: dict[str, str],
        delay_sec: float = 0.0,
    ) -> tuple[threading.Thread, dict[str, Any]]:
        """Apply process preset changes strictly on a background daemon thread."""
        outcome: dict[str, Any] = {"applied": False, "error": None}

        def _worker() -> None:
            if delay_sec > 0.0:
                time.sleep(delay_sec)
            res = self._apply_process_presets(updates)
            outcome.update(res)

        thread = threading.Thread(
            target=_worker,
            name="OrcaVaseStudio-PresetUpdater",
            daemon=True,
        )
        thread.start()
        return thread, outcome

    def _write_stl_resilient(self, directory: Path, stem: str, mesh: Any, header: str) -> Path:
        target = directory / f"{stem}.stl"
        try:
            return Path(write_binary_stl(target, mesh, header_name=header))
        except PermissionError:
            alt = directory / f"{stem}_{int(time.time() * 1000)}.stl"
            return Path(write_binary_stl(alt, mesh, header_name=header))

    def _notify_host_toast(
        self,
        text: str,
        level_name: str = "RegularNotificationLevel",
    ) -> None:
        host = getattr(orca, "host", None)
        ui = getattr(host, "ui", None) if host is not None else None
        push_fn = getattr(ui, "push_notification", None) if ui is not None else None
        if not callable(push_fn):
            return
        lvl_enum = getattr(ui, "NotificationLevel", None)
        level = None
        if lvl_enum is not None:
            level = getattr(
                lvl_enum,
                level_name,
                getattr(lvl_enum, "RegularNotificationLevel", None),
            )
        try:
            if level is not None:
                try:
                    push_fn(level, text)
                    return
                except TypeError:
                    push_fn(text)
                    return
            push_fn(text)
        except Exception:
            pass

    def handle_message(
        self,
        raw_data: Any,
        send_fn: Callable[[dict[str, Any]], None],
        default_mode: str = "page",
    ) -> None:
        """Process incoming WebView2 bridge payload and send responses via `send_fn`."""
        try:
            msg = json.loads(raw_data) if isinstance(raw_data, str) else raw_data
        except Exception as exc:
            send_fn(
                {
                    "type": "action_result",
                    "ok": False,
                    "action": "parse_error",
                    "message": f"Invalid JSON message: {exc}",
                    "paths": [],
                }
            )
            return

        if not isinstance(msg, dict):
            return

        msg_type = str(msg.get("type") or "").strip()

        try:
            if msg_type == "set_language":
                language = normalize_language(msg.get("lang"))
                origin_mode = "dock" if str(msg.get("mode") or default_mode) == "dock" else "page"
                request_id = int(msg.get("request_id") or 0)
                with self._lock:
                    if request_id > 0 and request_id < self._last_language_requests.get(origin_mode, 0):
                        return
                    if request_id > 0:
                        self._last_language_requests[origin_mode] = request_id
                    self._language_revision += 1
                    revision = self._language_revision
                    self._manual_language = language
                    self._language_loaded = True
                    target = _resolve_storage_dir() / "ui_preferences.json"
                    target.parent.mkdir(parents=True, exist_ok=True)
                    temporary = target.with_suffix(".tmp")
                    temporary.write_text(json.dumps({"language": language}), encoding="utf8")
                    temporary.replace(target)
                    callbacks = list(self._listeners.values())
                if send_fn not in callbacks:
                    callbacks.append(send_fn)
                for callback in callbacks:
                    try:
                        callback({"type":"preferences_updated", "lang":language, "language_revision":revision, "request_id":request_id, "source_mode":origin_mode})
                    except Exception:
                        pass
                return

            if msg_type == "ready":
                mode = str(msg.get("mode") or default_mode)
                with self._lock:
                    view_mode = "dock" if mode == "dock" else "page"
                    self._listeners[view_mode] = send_fn
                    self._last_language_requests.pop(view_mode, None)
                init_ctx = self.build_initial_context(mode=mode)
                host_ctx = self.read_host_context()
                params = init_ctx["params"]
                vase_mesh = generate_vase_mesh(params, layer_height_mm=host_ctx["layer_height_mm"])
                report = analyze_printability(vase_mesh, params, host_context=host_ctx)

                send_fn({"type": "init_state", **init_ctx})
                send_fn({"type": "analysis_result", "report": report})
                return

            if msg_type == "sync_printer":
                host_ctx = self.read_host_context()
                printer_info = self.build_printer_payload(host_ctx)
                send_fn(
                    {
                        "type": "printer_updated",
                        "printer": printer_info,
                        "lang": host_ctx["lang"],
                        "theme": host_ctx["theme"],
                        "theme_explicit": bool(host_ctx.get("theme_explicit", False)),
                    }
                )
                raw_params = msg.get("params")
                if isinstance(raw_params, dict):
                    params = self.set_current_params(raw_params)
                    vase_mesh = generate_vase_mesh(params, layer_height_mm=host_ctx["layer_height_mm"])
                    report = analyze_printability(vase_mesh, params, host_context=host_ctx)
                    send_fn({"type": "analysis_result", "report": report})
                return

            if msg_type == "analyze":
                params = self.set_current_params(msg.get("params") or self.current_params)
                host_ctx = self.read_host_context()
                vase_mesh = generate_vase_mesh(params, layer_height_mm=host_ctx["layer_height_mm"])
                report = analyze_printability(vase_mesh, params, host_context=host_ctx)
                send_fn({"type": "analysis_result", "report": report})
                return

            if msg_type == "randomize":
                raw_seed = msg.get("seed")
                seed_val: int | None = None
                if raw_seed is not None and raw_seed != "":
                    try:
                        seed_val = int(raw_seed)
                    except (TypeError, ValueError):
                        seed_val = None
                base_params = normalize_params(msg.get("params") or self.current_params)
                randomized = generate_random_printable_params(seed=seed_val, current_params=base_params)
                params = self.set_current_params(randomized)
                send_fn(
                    {
                        "type": "params_updated",
                        "params": params,
                        "source": "randomize",
                    }
                )
                return

            if msg_type == "preset_save":
                params = self.set_current_params(msg.get("params") or self.current_params)
                preset_name = str(msg.get("name") or params.get("name") or "Meu Vaso").strip() or "Meu Vaso"
                preset_id = msg.get("id") or msg.get("preset_id")
                preset_id_str = str(preset_id).strip() if preset_id else None
                user_presets = save_user_preset(
                    self.get_presets_dir(),
                    name=preset_name,
                    params=params,
                    preset_id=preset_id_str,
                )
                send_fn(
                    {
                        "type": "presets_updated",
                        "user_presets": user_presets,
                    }
                )
                return

            if msg_type == "preset_delete":
                preset_id = str(msg.get("id") or msg.get("preset_id") or "").strip()
                user_presets = delete_user_preset(self.get_presets_dir(), preset_id=preset_id)
                send_fn(
                    {
                        "type": "presets_updated",
                        "user_presets": user_presets,
                    }
                )
                return

            if msg_type == "export_file":
                params = self.set_current_params(msg.get("params") or self.current_params)
                fmt = str(msg.get("format") or "3mf").strip().lower().lstrip(".")
                if fmt not in ("3mf", "stl"):
                    fmt = "3mf"
                include_saucer = bool(msg.get("include_saucer", False))

                host_ctx = self.read_host_context()
                lang = host_ctx["lang"]
                export_dir = self.get_export_dir()

                effective_params = self._prepare_effective_vase_params(
                    params,
                    is_stl_export=(fmt == "stl"),
                    include_saucer=include_saucer,
                )
                vase_mesh = generate_vase_mesh(
                    effective_params,
                    layer_height_mm=host_ctx["layer_height_mm"],
                )
                report = analyze_printability(vase_mesh, effective_params, host_context=host_ctx)

                raw_filename = str(msg.get("filename") or "").strip()
                if raw_filename:
                    base_stem = _slugify_filename(Path(raw_filename).stem, fallback="vaso")
                else:
                    base_stem = _slugify_filename(params.get("name", "vaso"), fallback="vaso")

                paths: list[str] = []
                if fmt == "3mf":
                    target_3mf = export_dir / f"{base_stem}.3mf"
                    host_cfg = self.read_full_host_config_snapshot(host_ctx)
                    cx = host_ctx["bed_x"] / 2.0
                    cy = host_ctx["bed_y"] / 2.0

                    vase_label = str(params.get("name") or ("Vaso" if lang == "pt" else "Vase"))

                    if include_saucer:
                        saucer_mesh = generate_saucer_mesh(effective_params)
                        vase_rx = float(vase_mesh.bounds_mm["size"][0]) / 2.0
                        saucer_rx = float(saucer_mesh.bounds_mm["size"][0]) / 2.0
                        gap_mm = 10.0
                        total_w = 2.0 * vase_rx + gap_mm + 2.0 * saucer_rx
                        vase_pos = (round(cx - total_w / 2.0 + vase_rx, 2), round(cy, 2), 0.0)
                        saucer_pos = (round(cx + total_w / 2.0 - saucer_rx, 2), round(cy, 2), 0.0)
                        saucer_label = "Prato" if lang == "pt" else translate_text("Saucer", lang)
                        items = [
                            (vase_label, vase_mesh, vase_pos),
                            (saucer_label, saucer_mesh, saucer_pos),
                        ]
                    else:
                        items = [(vase_label, vase_mesh, (round(cx, 2), round(cy, 2), 0.0))]

                    written_3mf = Path(
                        write_orca_3mf(target_3mf, items, effective_params, host_config=host_cfg)
                    )
                    paths.append(str(written_3mf))
                else:
                    vase_stl = self._write_stl_resilient(
                        export_dir,
                        base_stem,
                        vase_mesh,
                        header=f"OrcaVaseStudio:{base_stem}",
                    )
                    paths.append(str(vase_stl))
                    if include_saucer:
                        saucer_mesh = generate_saucer_mesh(effective_params)
                        saucer_suffix = "prato" if lang == "pt" else "saucer"
                        saucer_stl = self._write_stl_resilient(
                            export_dir,
                            f"{base_stem}_{saucer_suffix}",
                            saucer_mesh,
                            header=f"OrcaVaseStudio:{base_stem}_{saucer_suffix}",
                        )
                        paths.append(str(saucer_stl))

                open_mouth_note = ""
                if (
                    fmt == "stl"
                    and params.get("print_mode") == "spiral_vase"
                    and effective_params.get("print_mode") == "shelled_hollow"
                ):
                    open_mouth_note = (
                        f" (boca aberta oca {effective_params['wall_thickness_mm']:.1f} mm)"
                        if lang == "pt"
                        else f" (open-mouthed {effective_params['wall_thickness_mm']:.1f} mm shell)"
                    )

                ok_msg = (
                    f"Arquivo exportado com sucesso: {Path(paths[0]).name}{open_mouth_note}"
                    if lang == "pt"
                    else f"Exported successfully: {Path(paths[0]).name}{open_mouth_note}"
                )
                if lang not in ("pt", "en"):
                    note = ""
                    if open_mouth_note:
                        note = translate_text(" (open-mouthed {mm} mm shell)", lang).replace("{mm}", f"{effective_params['wall_thickness_mm']:.1f}")
                    ok_msg = translate_text("Exported successfully: {name}", lang).replace("{name}", Path(paths[0]).name) + note
                send_fn(
                    {
                        "type": "action_result",
                        "ok": True,
                        "action": "export_file",
                        "format": fmt,
                        "path": paths[0],
                        "paths": paths,
                        "message": ok_msg,
                        "report": report,
                    }
                )
                return

            if msg_type == "send_to_plater":
                params = self.set_current_params(msg.get("params") or self.current_params)
                include_saucer = bool(msg.get("include_saucer", False))
                auto_cfg = bool(params.get("auto_configure_slicer", True))

                host_ctx = self.read_host_context()
                lang = host_ctx["lang"]
                export_dir = self.get_export_dir()

                effective_params = self._prepare_effective_vase_params(
                    params,
                    is_stl_export=False,
                    include_saucer=include_saucer,
                )
                vase_mesh = generate_vase_mesh(
                    effective_params,
                    layer_height_mm=host_ctx["layer_height_mm"],
                )
                report = analyze_printability(vase_mesh, effective_params, host_context=host_ctx)

                base_stem = _slugify_filename(params.get("name", "vaso"), fallback="vaso")
                vase_stl = self._write_stl_resilient(
                    export_dir,
                    f"{base_stem}_plater",
                    vase_mesh,
                    header=f"OrcaVaseStudio:{base_stem}",
                )
                stl_paths = [str(vase_stl)]

                if include_saucer:
                    saucer_mesh = generate_saucer_mesh(effective_params)
                    saucer_suffix = "prato" if lang == "pt" else "saucer"
                    saucer_stl = self._write_stl_resilient(
                        export_dir,
                        f"{base_stem}_{saucer_suffix}_plater",
                        saucer_mesh,
                        header=f"OrcaVaseStudio:{base_stem}_{saucer_suffix}",
                    )
                    stl_paths.append(str(saucer_stl))

                copydata_payload = _format_other_instance_payload(stl_paths)
                updates: dict[str, str] = {}
                if auto_cfg:
                    updates = self._compute_process_preset_updates(
                        params=effective_params,
                        host_ctx=host_ctx,
                        include_saucer=include_saucer,
                    )

                native_host = _is_native_orca_host()
                copydata_delay = 0.06 if native_host else 0.01
                preset_delay = 0.45 if native_host else 0.01
                dispatch_outcome: dict[str, Any] = {
                    "ipc_ok": False,
                    "ipc_message": "",
                    "hwnd": None,
                    "thread_id": None,
                    "preset_applied": False,
                    "preset_error": None,
                }
                self._last_plater_outcome = dispatch_outcome

                def _plater_bg_worker() -> None:
                    dispatch_outcome["thread_id"] = threading.get_ident()
                    if copydata_delay > 0.0:
                        time.sleep(copydata_delay)

                    hwnd = _find_orca_mainframe_hwnd()
                    dispatch_outcome["hwnd"] = hwnd
                    ipc_ok, ipc_msg = _dispatch_copydata_to_hwnd(hwnd or 0, copydata_payload)
                    if not ipc_ok and sys.platform != "win32":
                        ipc_ok, ipc_msg = _dispatch_non_win32_plater_open(stl_paths)
                    dispatch_outcome["ipc_ok"] = ipc_ok
                    dispatch_outcome["ipc_message"] = ipc_msg

                    if auto_cfg and updates:
                        if preset_delay > 0.0:
                            time.sleep(preset_delay)
                        preset_res = self._apply_process_presets(updates)
                        dispatch_outcome["preset_applied"] = bool(preset_res.get("applied", False))
                        dispatch_outcome["preset_error"] = preset_res.get("error")

                worker = threading.Thread(
                    target=_plater_bg_worker,
                    name="OrcaVaseStudio-PlaterDispatch",
                    daemon=True,
                )
                self._last_plater_worker = worker
                worker.start()

                if not native_host:
                    # Safe to join in standalone/test harness; NEVER join on native wxWidgets UI thread!
                    worker.join(timeout=4.0)
                    slicer_configured = bool(dispatch_outcome.get("preset_applied", False))
                else:
                    process_ed = getattr(
                        getattr(getattr(orca, "host", None), "preset", None),
                        "process",
                        None,
                    )
                    slicer_configured = bool(auto_cfg and hasattr(process_ed, "begin_update"))

                saucer_spiral_note = ""
                if include_saucer and params.get("print_mode") == "spiral_vase":
                    saucer_spiral_note = (
                        " (Convertido para Vaso Oco Aberto para fatiar vaso + prato juntos.)"
                        if lang == "pt"
                        else " (Converted to open hollow shell to slice vase + saucer together.)"
                    )

                msg_text = (
                    f"Enviado para a mesa do OrcaSlicer ({len(stl_paths)} objeto(s)).{saucer_spiral_note}"
                    if lang == "pt"
                    else f"Sent to OrcaSlicer Plater ({len(stl_paths)} object(s)).{saucer_spiral_note}"
                )
                if lang not in ("pt", "en"):
                    msg_text = translate_text("Sent to OrcaSlicer Plater ({n} object(s)).", lang).replace("{n}", str(len(stl_paths)))
                    if saucer_spiral_note:
                        msg_text += translate_text(" (Converted to open hollow shell to slice vase + saucer together.)", lang)
                self._notify_host_toast(msg_text)

                send_fn(
                    {
                        "type": "action_result",
                        "ok": True,
                        "action": "send_to_plater",
                        "path": stl_paths[0],
                        "paths": stl_paths,
                        "message": msg_text,
                        "report": report,
                        "slicer_configured": slicer_configured,
                    }
                )
                return

            if msg_type == "open_exports_folder":
                export_dir = self.get_export_dir()
                lang = self.read_host_context()["lang"]
                startfile_fn = getattr(os, "startfile", None)
                if callable(startfile_fn) and (_is_native_orca_host() or _is_mock_callable(startfile_fn)):
                    try:
                        startfile_fn(str(export_dir))
                    except Exception:
                        pass
                elif sys.platform != "win32" and _is_native_orca_host():
                    try:
                        import subprocess

                        opener = "open" if sys.platform == "darwin" else "xdg-open"
                        subprocess.Popen(
                            [opener, str(export_dir)],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL,
                        )
                    except Exception:
                        pass

                msg_text = (
                    f"Pasta de exportação: {export_dir}"
                    if lang == "pt"
                    else f"Exports folder: {export_dir}"
                )
                if lang not in ("pt", "en"):
                    msg_text = translate_text("Exports folder: {path}", lang).replace("{path}", str(export_dir))
                send_fn(
                    {
                        "type": "action_result",
                        "ok": True,
                        "action": "open_exports_folder",
                        "path": str(export_dir),
                        "paths": [str(export_dir)],
                        "message": msg_text,
                    }
                )
                return

            send_fn(
                {
                    "type": "action_result",
                    "ok": False,
                    "action": msg_type or "unknown",
                    "message": f"Unsupported message type: {msg_type!r}",
                    "paths": [],
                }
            )
        except Exception as exc:
            send_fn(
                {
                    "type": "action_result",
                    "ok": False,
                    "action": msg_type or "error",
                    "message": str(exc),
                    "paths": [],
                }
            )


_SHARED_CONTROLLER = VaseStudioController()

_SYNC_LIFECYCLE_EVENT_NAMES: frozenset[str] = frozenset(
    {"PresetSelected", "PresetSaved", "NewProject", "ProjectOpened"}
)
_VALID_DOCK_SIDES: frozenset[str] = frozenset({"left", "right", "bottom", "float"})


def _is_sync_lifecycle_event(event: Any) -> bool:
    """Match `orca.LifecycleEvent` enum values or names for preset/project changes."""
    ev_cls = getattr(orca, "LifecycleEvent", None)
    if ev_cls is not None:
        for nm in _SYNC_LIFECYCLE_EVENT_NAMES:
            cand = getattr(ev_cls, nm, None)
            if cand is not None and event == cand:
                return True
    ev_name = str(getattr(event, "name", event) or "")
    return any(k in ev_name for k in _SYNC_LIFECYCLE_EVENT_NAMES)


def _read_capability_config(cap: Any) -> dict[str, Any]:
    """Read `PythonPluginBase.get_config()` JSON string merged over `get_default_config()`."""
    defaults: dict[str, Any] = {}
    def_fn = getattr(cap, "get_default_config", None)
    if callable(def_fn):
        try:
            got_def = def_fn()
            if isinstance(got_def, dict):
                defaults = dict(got_def)
        except Exception:
            defaults = {}

    get_fn = getattr(cap, "get_config", None)
    if not callable(get_fn):
        return defaults
    try:
        raw = get_fn()
        if isinstance(raw, str) and raw.strip():
            parsed = json.loads(raw)
            if isinstance(parsed, dict):
                merged = dict(defaults)
                merged.update(parsed)
                return merged
        elif isinstance(raw, dict):
            merged = dict(defaults)
            merged.update(raw)
            return merged
    except Exception:
        pass
    return defaults


def _apply_capability_config_to_controller(
    controller: VaseStudioController,
    cfg: dict[str, Any],
) -> None:
    """Apply user-saved capability configuration overrides onto controller parameters."""
    if not cfg:
        return
    updates: dict[str, Any] = {}
    mode_val = cfg.get("default_print_mode")
    if mode_val in ("shelled_hollow", "spiral_vase"):
        updates["print_mode"] = mode_val
    if isinstance(cfg.get("auto_configure_slicer"), bool):
        updates["auto_configure_slicer"] = cfg["auto_configure_slicer"]
    if isinstance(cfg.get("stl_always_open_hollow"), bool):
        updates["stl_always_open_hollow"] = cfg["stl_always_open_hollow"]
    if updates:
        cur = controller.current_params
        cur.update(updates)
        controller.set_current_params(cur)


# ---------------------------------------------------------------------------
# OrcaSlicer Plugin Capabilities (Top-Bar Page + Docked Side Panel)
# ---------------------------------------------------------------------------


class VaseStudioPageCapability(orca.pages.PagesPluginCapabilityBase):
    """Full-screen top-bar tab (`Gerador de Vasos`) beside Prepare / Preview / Device."""

    def __init__(self, controller: VaseStudioController | None = None) -> None:
        super().__init__()
        self._controller = controller or _SHARED_CONTROLLER

    def get_name(self) -> str:
        return "Gerador de Vasos"

    def get_default_config(self) -> dict[str, Any]:
        return {
            "default_print_mode": "shelled_hollow",
            "auto_configure_slicer": True,
            "stl_always_open_hollow": True,
        }

    def on_load(self) -> None:
        _apply_capability_config_to_controller(
            self._controller,
            _read_capability_config(self),
        )

    def on_unload(self) -> None:
        with self._controller._lock:
            self._controller._listeners.pop("page", None)

    def get_icon(self) -> str:
        storage_dir = _resolve_storage_dir(in_callback=True)
        existing_candidates: list[Path] = []
        try:
            existing_candidates.append(Path(__file__).resolve().parent / "icon.svg")
        except Exception:
            pass
        existing_candidates.extend(
            [
                storage_dir / "icon.svg",
                _default_installed_plugin_dir() / "icon.svg",
            ]
        )
        for cand in existing_candidates:
            try:
                if cand.is_file() and cand.stat().st_size > 0:
                    return str(cand)
            except Exception:
                continue

        # Auto-materialize embedded `icon.svg` when user side-loaded only `orca_vase_generator.py`
        write_targets: list[Path] = [
            storage_dir / "icon.svg",
            _default_plugin_data_dir() / "icon.svg",
        ]
        try:
            write_targets.append(Path(__file__).resolve().parent / "icon.svg")
        except Exception:
            pass
        write_targets.append(Path.home() / "Documents" / "OrcaVaseStudio" / "icon.svg")

        seen_dirs: set[str] = set()
        for target in write_targets:
            key = str(target)
            if key in seen_dirs:
                continue
            seen_dirs.add(key)
            try:
                target.parent.mkdir(parents=True, exist_ok=True)
                with open(target, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(ICON_SVG_CONTENT)
                if target.is_file() and target.stat().st_size > 0:
                    return str(target)
            except Exception:
                continue
        return ""

    def get_ui(self) -> str:
        initial_ctx = self._controller.build_initial_context(mode="page")
        return get_studio_html(mode="page", initial_context=initial_ctx)

    def post_message(self, data: Any) -> None:
        super_post = getattr(super(), "post_message", None)
        if callable(super_post):
            super_post(data)

    def on_message(self, data: Any) -> None:
        self._controller.handle_message(
            raw_data=data,
            send_fn=self.post_message,
            default_mode="page",
        )

    def on_lifecycle_event(self, event: Any, ctx: Any = None) -> None:
        """Push live `printer_updated` + `analysis_result` whenever OrcaSlicer switches presets or projects."""
        if not _is_sync_lifecycle_event(event):
            return
        try:
            host_ctx = self._controller.read_host_context()
            printer_info = self._controller.build_printer_payload(host_ctx)
            self.post_message(
                {
                    "type": "printer_updated",
                    "printer": printer_info,
                    "lang": host_ctx["lang"],
                    "theme": host_ctx["theme"],
                    "theme_explicit": bool(host_ctx.get("theme_explicit", False)),
                }
            )
            params = self._controller.current_params
            vase_mesh = generate_vase_mesh(params, layer_height_mm=host_ctx["layer_height_mm"])
            report = analyze_printability(vase_mesh, params, host_context=host_ctx)
            self.post_message({"type": "analysis_result", "report": report})
        except Exception:
            pass


class VaseStudioDockCapability(orca.script.ScriptPluginCapabilityBase):
    """Opens/shows a docked right-hand Vase Studio panel directly beside the 3D Plater."""

    _active_panel: Any = None
    _panel_lock = threading.RLock()

    def __init__(self, controller: VaseStudioController | None = None) -> None:
        super().__init__()
        self._controller = controller or _SHARED_CONTROLLER

    def get_name(self) -> str:
        return "Orca Vase Studio - Painel Lateral"

    def get_default_config(self) -> dict[str, Any]:
        return {
            "dock": "right",
            "width": 420,
            "height": 780,
            "auto_configure_slicer": True,
            "stl_always_open_hollow": True,
        }

    def on_load(self) -> None:
        _apply_capability_config_to_controller(
            self._controller,
            _read_capability_config(self),
        )

    def on_unload(self) -> None:
        with self._controller._lock:
            self._controller._listeners.pop("dock", None)
        with self._panel_lock:
            VaseStudioDockCapability._active_panel = None

    def get_ui(self) -> str:
        initial_ctx = self._controller.build_initial_context(mode="dock")
        return get_studio_html(mode="dock", initial_context=initial_ctx)

    def _post_to_panel(self, payload: dict[str, Any]) -> None:
        with self._panel_lock:
            panel = VaseStudioDockCapability._active_panel
        if panel is None:
            return
        try:
            is_open_fn = getattr(panel, "is_open", None)
            if callable(is_open_fn) and not is_open_fn():
                return
            post_fn = getattr(panel, "post", None)
            if callable(post_fn):
                post_fn(payload)
        except Exception:
            pass

    def _on_panel_message(self, data: Any) -> None:
        self._controller.handle_message(
            raw_data=data,
            send_fn=self._post_to_panel,
            default_mode="dock",
        )

    def _on_panel_close(self) -> None:
        with self._controller._lock:
            self._controller._listeners.pop("dock", None)
        with self._panel_lock:
            VaseStudioDockCapability._active_panel = None

    def on_message(self, data: Any) -> None:
        """Direct message entry point for testing or programmatic invocation."""
        self._on_panel_message(data)

    def on_lifecycle_event(self, event: Any, ctx: Any = None) -> None:
        """Keep any open docked side panel synced when OrcaSlicer switches presets or projects."""
        if not _is_sync_lifecycle_event(event):
            return
        with self._panel_lock:
            panel = VaseStudioDockCapability._active_panel
        if panel is None:
            return
        try:
            host_ctx = self._controller.read_host_context()
            printer_info = self._controller.build_printer_payload(host_ctx)
            self._post_to_panel(
                {
                    "type": "printer_updated",
                    "printer": printer_info,
                    "lang": host_ctx["lang"],
                    "theme": host_ctx["theme"],
                    "theme_explicit": bool(host_ctx.get("theme_explicit", False)),
                }
            )
            params = self._controller.current_params
            vase_mesh = generate_vase_mesh(params, layer_height_mm=host_ctx["layer_height_mm"])
            report = analyze_printability(vase_mesh, params, host_context=host_ctx)
            self._post_to_panel({"type": "analysis_result", "report": report})
        except Exception:
            pass

    def execute(self) -> Any:
        """Open or focus the docked Vase Studio panel beside the 3D Plater.

        Safe whether invoked on the main/UI thread (documented Wiki contract) or on
        `ScriptAsyncRuntime`'s background worker (`OrcaSlicer.dll` v2.5.1), as
        `orca.host.ui.create_dock_panel` marshals panel creation onto the UI thread.
        """
        cfg = _read_capability_config(self)
        _apply_capability_config_to_controller(self._controller, cfg)
        dock_side = str(cfg.get("dock") or "right").strip().lower()
        if dock_side not in _VALID_DOCK_SIDES:
            dock_side = "right"
        dock_w = max(280, min(960, int(_extract_first_float(cfg.get("width"), 420.0))))
        dock_h = max(360, min(1600, int(_extract_first_float(cfg.get("height"), 780.0))))

        with self._panel_lock:
            existing = VaseStudioDockCapability._active_panel

        if existing is not None:
            try:
                is_open_fn = getattr(existing, "is_open", None)
                if not callable(is_open_fn) or is_open_fn():
                    show_fn = getattr(existing, "show", None)
                    if callable(show_fn):
                        show_fn()
                    init_ctx = self._controller.build_initial_context(mode="dock")
                    self._post_to_panel({"type": "init_state", **init_ctx})
                    return _make_execution_result_success("Painel lateral Orca Vase Studio exibido.")
            except Exception:
                with self._panel_lock:
                    VaseStudioDockCapability._active_panel = None

        html = self.get_ui()
        host = getattr(orca, "host", None)
        ui = getattr(host, "ui", None) if host is not None else None
        create_dock_fn = getattr(ui, "create_dock_panel", None) if ui is not None else None

        if callable(create_dock_fn):
            panel = create_dock_fn(
                html,
                title="Orca Vase Studio",
                width=dock_w,
                height=dock_h,
                on_message=self._on_panel_message,
                on_close=self._on_panel_close,
                dock=dock_side,
            )
            with self._panel_lock:
                VaseStudioDockCapability._active_panel = panel
            if panel is not None:
                show_fn = getattr(panel, "show", None)
                if callable(show_fn):
                    try:
                        show_fn()
                    except Exception:
                        pass
            return _make_execution_result_success("Painel lateral Orca Vase Studio aberto.")

        # Fallback if `create_dock_panel` is unavailable in an older/mocked environment
        create_win_fn = getattr(ui, "create_window", None) if ui is not None else None
        if callable(create_win_fn):
            panel = create_win_fn(
                html,
                title="Orca Vase Studio",
                width=max(440, dock_w),
                height=max(800, dock_h),
                on_message=self._on_panel_message,
                on_close=self._on_panel_close,
            )
            with self._panel_lock:
                VaseStudioDockCapability._active_panel = panel
            return _make_execution_result_success("Janela Orca Vase Studio aberta.")

        return _make_execution_result_success("Orca Vase Studio pronto.")


# ---------------------------------------------------------------------------
# Single `@orca.plugin` Entry Point Class
# ---------------------------------------------------------------------------


@orca.plugin
class OrcaVaseStudioPlugin(orca.base):
    """OrcaSlicer 2.5.1+ Native Plugin Entry Point for Orca Vase Studio."""

    def __init__(self) -> None:
        super().__init__()

    def register_capabilities(self) -> None:
        plugin_dir = _default_installed_plugin_dir()
        plugin_data_dir = _default_plugin_data_dir()
        docs_dir = Path.home() / "Documents" / "OrcaVaseStudio"

        candidate_dirs: list[Path] = [
            plugin_dir,
            plugin_data_dir,
            docs_dir,
        ]
        for extra_fn in (
            lambda: Path(__file__).resolve().parent,
            lambda: _resolve_storage_dir(in_callback=False),
        ):
            try:
                extra_dir = extra_fn()
                if str(extra_dir).strip():
                    candidate_dirs.append(extra_dir)
            except Exception:
                continue

        fs_targets: list[str] = []
        for d in candidate_dirs:
            d_str = str(d).strip()
            if not d_str:
                continue
            cand = f"{d_str}/*"
            if cand not in fs_targets:
                fs_targets.append(cand)

        req_fn = getattr(orca, "request_permissions", None)
        if callable(req_fn):
            req_fn(
                fs_read=list(fs_targets),
                fs_readwrite=list(fs_targets),
                threading=True,
            )

        orca.register_capability(VaseStudioPageCapability)
        orca.register_capability(VaseStudioDockCapability)
