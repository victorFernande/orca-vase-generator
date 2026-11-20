"""Offline interface vocabulary. Geometry and user-supplied names are never translated.

Rows use English as a stable source and contain Spanish, Italian, French, German
and Japanese in that order. Original Portuguese/English vocabulary stays in the UI.
"""

from __future__ import annotations

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
