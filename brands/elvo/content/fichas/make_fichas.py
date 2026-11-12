#!/usr/bin/env python3
"""Genera 8 PDF: ficha técnica + ficha de ventas de Nativo, Vivo, Alivio y Cero.
Datos: tienda elvo.pe (12-nov-2026) + repo. Uso: python3 make_fichas.py"""
import os, html

ROOT = '/home/user/elvo-creating/brands/elvo/'
OUT = ROOT + 'content/fichas/'
FECHA = '12 de noviembre de 2026'
PIE = 'www.elvo.pe · @elvo_filtros'

def img(p): return 'file://' + ROOT + p

P = {}

P['nativo'] = dict(
    nombre='elvo· Nativo', tag='Purificador antimetales para el caño',
    foto=img('brand-identity/product-images/nativo-front.png'),
    resumen='El purificador que va directo a tu caño. Retiene plomo y metales pesados* y reduce el cloro, los olores y los sabores, en el último punto antes de tu vaso. Sin electricidad, sin obras y sin gasfitero.',
    tecnica=[
        ('Tipo', 'Purificador de mesada conectado al caño'),
        ('Etapas de filtración', '6'),
        ('Núcleo', 'PureCore, dura 18 meses de uso normal'),
        ('Tendencia del agua', 'Alcalina (pH ~8.5)'),
        ('Minerales naturales', 'Se conservan'),
        ('Medidas', '30 cm de alto · 16 × 16 cm (cuerpo, pico y base) · 1,5 kg'),
        ('Conexión', 'Derivador metálico con palanca + manguera blanca + adaptador universal de jebe'),
        ('Energía', 'No usa electricidad'),
        ('Instalación', 'La haces tú en 5 minutos, sin herramientas ni gasfitero'),
        ('Garantía', '1 año del equipo · 30 días de prueba'),
    ],
    etapas=[('Carbón activado', 'reduce cloro, olores y mal sabor'),
            ('Etapa antimetales', 'retiene plomo y metales pesados*'),
            ('Plata coloidal', 'inhibe el crecimiento de microorganismos'),
            ('Nanotecnología', 'atrapa microplásticos y partículas finas'),
            ('Aluminosilicato', 'mejora la claridad del agua'),
            ('Plata iónica', 'mantiene el agua más pura por más tiempo')],
    incluye=['Purificador elvo· Nativo con núcleo instalado', 'Derivador metálico con palanca', 'Manguera blanca', 'Adaptador universal de jebe ajustable', 'Llave plástica para cambiar el núcleo', 'Núcleos según tu plan (1, 2 o 4)', 'Manual en español'],
    mantenimiento='El núcleo dura 18 meses de uso normal. Te avisamos por WhatsApp cuando toque cambiarlo. Con la llave plástica desenroscas la base, cambias el núcleo, enroscas a mano y dejas correr el agua 5 minutos antes de usar.',
    planes=[('18 meses', '1 núcleo', 'S/ 299'), ('3 años', '2 núcleos', 'S/ 349'), ('6 años', '4 núcleos', 'S/ 489')],
    repuesto='Repuesto de núcleo: S/ 249',
    para=['Quien quiere agua más segura directo del caño de su casa', 'Familias que cuidan lo que toman y cocinan', 'Casas y departamentos donde no se pueden hacer obras'],
    pasos=['Conecta el derivador al caño del grifo', 'Deja correr el agua 5 minutos (primer uso)', 'Mueve la palanca a "filtrada" y sirve por el pico del purificador'],
    faq=[('¿Necesito gasfitero?', 'No. Lo instalas tú en 5 minutos, sin herramientas.'),
         ('¿Qué pasa si no encaja en mi caño?', 'Te devolvemos tu dinero.'),
         ('¿Puedo seguir usando el caño normal?', 'Sí. La palanca del derivador cambia entre agua normal y agua filtrada.'),
         ('¿Dónde lo pongo?', 'En la mesada. La manguera es de buen largo, así que puede quedar lejos del caño.'),
         ('¿Cuánto dura el núcleo?', '18 meses de uso normal. Te avisamos cuándo cambiarlo.')],
    envio=['Envío gratis a todo el Perú', 'Pago contra entrega', 'Hasta 6 cuotas sin intereses con tarjeta de crédito', '30 días de prueba'],
    nota='*Según la ficha técnica del núcleo PureCore. Pensado para agua de red potable (clorada). Los resultados dependen de la calidad del agua de entrada. Cambia el núcleo a tiempo para mantener el mejor resultado.',
)

P['vivo'] = dict(
    nombre='elvo· Vivo', tag='Purificador con magnesio para el caño',
    foto=img('brand-identity/product-images/vivo-front.png'),
    resumen='Agua más rica y sin sabor a cloro, directo de tu caño. Filtra el agua, le aporta magnesio y la deja con tendencia alcalina. Sin electricidad, sin obras y sin gasfitero.',
    tecnica=[
        ('Tipo', 'Purificador de mesada conectado al caño'),
        ('Etapas de filtración', '4'),
        ('Núcleo', 'Dura 18 meses de uso normal'),
        ('Aporta', 'Magnesio · tendencia alcalina (pH ~8.5)'),
        ('Materiales', 'Piezas principales de acero inoxidable; componentes de grado alimenticio, libres de BPA'),
        ('Medidas', '30 cm de alto · 16 × 16 cm (cuerpo, pico y base) · 1,5 kg'),
        ('Conexión', 'Kit de adaptadores incluido, compatible con la mayoría de caños estándar'),
        ('Energía', 'No usa electricidad'),
        ('Llenado', 'Un vaso en 5 segundos'),
        ('Instalación', 'La haces tú en 5 minutos, sin herramientas ni gasfitero'),
        ('Garantía', '1 año'),
    ],
    etapas=[('Ultrafiltración', 'impurezas como cloro, sedimentos, malos olores y sabor'),
            ('Bloque sólido de carbón activado', 'cloro, sedimentos, mal sabor y olor'),
            ('Aporte de magnesio', 'mineraliza el agua y aporta tendencia alcalina'),
            ('Microfiltración', 'atrapa microplásticos, turbiedad y partículas finas')],
    incluye=['Purificador elvo· Vivo con núcleo instalado', 'Kit de adaptadores', 'Derivador y manguera', 'Manual en español'],
    mantenimiento='El núcleo dura 18 meses de uso normal. Te avisamos por WhatsApp cuando toque cambiarlo. Cambio sencillo: con la llave plástica abres la base, cambias el núcleo, enroscas a mano y dejas correr el agua 5 minutos.',
    planes=[('18 meses', '', 'S/ 259'), ('3 años', '', 'S/ 289'), ('6 años', '', 'S/ 359')],
    repuesto='Repuesto de núcleo: S/ 129',
    para=['Quien quiere un agua más rica, sin sabor a cloro', 'Quien prepara café, té e infusiones todos los días', 'Casas que quieren una solución simple, sin obras'],
    pasos=['Conecta el derivador al caño del grifo', 'Deja correr el agua 5 minutos (primer uso)', 'Mueve la palanca a "filtrada" y sirve por el pico del purificador'],
    faq=[('¿Vivo y Nativo son iguales?', 'Se ven iguales por fuera. Nativo suma 2 etapas antimetales a lo que ya hace Vivo.'),
         ('¿Necesito gasfitero?', 'No. Lo instalas tú en 5 minutos.'),
         ('¿Aporta minerales?', 'Sí, aporta magnesio y deja el agua con tendencia alcalina (pH ~8.5).'),
         ('¿Cuánto dura el núcleo?', '18 meses de uso normal. Te avisamos cuándo cambiarlo.')],
    envio=['Envío gratis a todo el Perú', 'Pago contra entrega', 'Hasta 6 cuotas sin intereses con tarjeta de crédito'],
    nota='Pensado para agua de red potable (clorada). Los resultados dependen de la calidad del agua de entrada y del cambio oportuno del núcleo.',
)

P['alivio'] = dict(
    nombre='elvo· Alivio', tag='Bidón purificador por gravedad · 16 y 22 litros',
    foto=img('content/lote5/k2-alivio-acero_v1.png'),
    resumen='Agua de resguardo en casa. Se llena con una jarra y purifica por gravedad: sin electricidad, sin conexión al caño y sin necesitar presión de agua.',
    tecnica=[
        ('Tipo', 'Purificador de gravedad con tanque de reserva'),
        ('Capacidades', '16 L y 22 L'),
        ('Etapas de filtración', '8'),
        ('Medidas 16 L', '62 cm de alto × 35 cm de largo × 31 cm de ancho'),
        ('Medidas 22 L', '61 cm de alto × 35 cm de largo × 23,5 cm de ancho'),
        ('Energía', 'No usa electricidad'),
        ('Conexión', 'Ninguna. No necesita caño ni presión de agua'),
        ('Llenado', 'Quitas la tapa domo y llenas el tanque superior con una jarra'),
        ('Servicio', 'Llave en la parte inferior, para vaso, jarra o botella'),
        ('Incluye', 'Gotas de pH para medir el pH de tu agua'),
        ('Kit de filtros', 'Rinde 10.000 litros o 1 año, lo que ocurra primero'),
        ('Garantía', '6 meses'),
    ],
    etapas=[('Filtro cerámico', 'primera barrera del agua'),
            ('Filtro multimedia', 'carbón activado, carbón de plata, WMSM-300, arena de sílice, zeolita y arena mineral'),
            ('Piedra mineral', 'cierra el proceso y mineraliza el agua')],
    incluye=['Purificador elvo· Alivio (16 L o 22 L) con su filtro instalado', 'Gotas de pH', 'Tapa domo y llave', 'Opción "Equipo + kit de repuesto": suma un segundo kit de filtros'],
    mantenimiento='El kit de repuesto (S/ 99) trae 1 filtro cerámico, 1 filtro multicapa y 1 filtro mineralizador. Rinde 10.000 litros o 1 año, lo que ocurra primero. Compatible con todos los purificadores de la línea.',
    planes=[('Alivio 16 L · solo el equipo', '', 'S/ 159'), ('Alivio 16 L · equipo + kit de repuesto', '', 'S/ 249'),
            ('Alivio 22 L · solo el equipo', '', 'S/ 198'), ('Alivio 22 L · equipo + kit de repuesto', '', 'S/ 288')],
    repuesto='Kit de filtros de repuesto: S/ 99',
    para=['Casas que quieren agua guardada y lista, sin depender del caño', 'Zonas donde la presión del agua es baja', 'Quien busca una solución sin electricidad ni instalación', 'Familias grandes (el de 22 L) o casas medianas (el de 16 L)'],
    pasos=['Quita la tapa domo', 'Llena el tanque superior con una jarra', 'El agua baja sola por gravedad y se sirve por la llave'],
    faq=[('¿Necesita electricidad?', 'No. Purifica por gravedad.'),
         ('¿Necesito conectarlo al caño?', 'No. Se llena con una jarra.'),
         ('¿Cuál elijo, 16 o 22 litros?', 'Más litros, más alivio: el de 22 L rinde más para toda la casa; el de 16 L es suficiente para casas medianas.'),
         ('¿Cada cuánto cambio los filtros?', 'El kit rinde 10.000 litros o 1 año, lo que ocurra primero.')],
    envio=['Envío gratis a todo el Perú', 'Lima: entrega al día siguiente, coordinamos el horario contigo', 'Provincias: envío por Shalom a tu oficina más cercana', 'Garantía de satisfacción'],
    nota='Cambia el kit de filtros a tiempo para mantener el mejor resultado. Los resultados dependen de la calidad del agua de entrada.',
)

P['cero'] = dict(
    nombre='elvo· Cero', tag='Purificador de ósmosis inversa con agua fría y caliente',
    foto=img('content/video-cero/v1-cero-solo.png'),
    resumen='Esto no es un filtro. Agua purificada fría a 6 °C o caliente al instante, sin instalación de cañerías: solo enchufas y llenas el tanque.',
    tecnica=[
        ('Tipo', 'Purificador de ósmosis inversa de mesada'),
        ('Tecnología', 'Ósmosis inversa + desinfección UV'),
        ('Agua fría', '6 – 7 °C'),
        ('Agua caliente', '7 ajustes de temperatura hasta ~85 °C, lista en 2 segundos'),
        ('Pantalla', 'Táctil, con atajos de temperatura y volumen programable en ml (botones − y +)'),
        ('Jarra extraíble', '2 litros de agua purificada, con asa'),
        ('Medidas', '37,6 cm de alto × 47,9 cm de largo × 22,5 cm de fondo'),
        ('Alimentación eléctrica', '110 a 240 V'),
        ('Llenado', 'Se llena por la tapa superior trasera con una jarra'),
        ('Instalación', 'Sin cañerías, sin plomero, sin obras'),
        ('Mantenimiento', 'Aviso en pantalla de cambio de filtros (los dos círculos pasan a rojo) · autolimpieza de tuberías (Pipe Cleaning)'),
        ('Filtros', 'PAC cada 8 a 12 meses · ROC cada 12 a 36 meses'),
        ('Garantía', '1 año'),
    ],
    etapas=[('Ósmosis inversa', 'la barrera más fina para el agua que bebes'),
            ('Filtros PAC y ROC', 'se cambian en kit cuando la pantalla avisa'),
            ('Desinfección UV', 'cuida el agua dentro del equipo')],
    incluye=['Purificador elvo· Cero', 'Jarra extraíble de 2 L', 'Manual en español', 'Garantía de 1 año'],
    mantenimiento='La pantalla te avisa cuándo cambiar los filtros: los dos círculos del diagrama pasan a rojo. Los filtros PAC duran de 8 a 12 meses y los ROC de 12 a 36 meses. El botón Pipe Cleaning hace la autolimpieza, y Filter Reset reinicia el contador después del cambio. Kit de filtros PAC + ROC: S/ 329.',
    planes=[('elvo· Cero', 'Equipo con jarra extraíble de 2 L', 'S/ 2.199')],
    repuesto='Kit de filtros PAC + ROC: S/ 329',
    para=['Casas con cocina moderna que quieren agua fría y caliente al instante', 'Oficinas, coworkings y consultorios que quieren dejar los bidones', 'Quien prepara té, café, fórmulas o recetas con agua a la temperatura exacta'],
    pasos=['Quita la tapa superior trasera y llena el tanque con una jarra', 'Elige la temperatura y los ml en la pantalla', 'Apoya el vaso y presiona el botón plateado para servir, o saca la jarra de 2 L y llévala a la mesa'],
    faq=[('¿Necesito instalación?', 'No. Solo enchufas (110 a 240 V) y llenas el tanque trasero.'),
         ('¿Cuánto tarda el agua caliente?', 'Está lista en 2 segundos, en 7 ajustes de temperatura hasta ~85 °C.'),
         ('¿Cómo sé cuándo cambiar los filtros?', 'La pantalla te avisa: los dos círculos del diagrama pasan a rojo.'),
         ('¿Qué hago con la jarra?', 'Se extrae del equipo con agua purificada y se lleva a la mesa. Tiene 2 litros.'),
         ('¿Sirve para la oficina?', 'Sí. Es la forma de dejar los bidones: más agua a la mano y menos pedidos.')],
    envio=['Envío a todo el Perú', 'Coordinamos la entrega y te explicamos el uso', 'Garantía de 1 año'],
    nota='Pensado para agua de red potable. Cambia los filtros a tiempo para mantener el mejor resultado.',
)

CSS = """
@page{size:A4;margin:0}
*{box-sizing:border-box}
body{margin:0;font-family:'Inter',sans-serif;color:#010A21;font-size:10.5pt;line-height:1.4}
.page{width:210mm;height:296mm;overflow:hidden;padding:12mm 14mm 12mm;position:relative;page-break-after:always;background:#fff}
.hero{background:#010A21;color:#fff;border-radius:14px;display:flex;gap:6mm;align-items:center;padding:8mm;overflow:hidden}
.hero .t{flex:1}.hero .tag{color:#9EBACE;font-size:10pt;letter-spacing:.3px;text-transform:uppercase;font-weight:500}
.hero h1{font-size:26pt;margin:2mm 0;font-weight:600;letter-spacing:-.5px}
.hero p{font-size:10.5pt;color:#dfe8ff;margin:0}
.hero img{height:50mm;width:50mm;border-radius:10px;object-fit:cover;background:#fff}
.tipo{display:inline-block;background:#3355FF;color:#fff;border-radius:99px;padding:1mm 4mm;font-size:8.5pt;font-weight:600;margin-bottom:3mm}
h2{font-size:12pt;color:#3355FF;margin:4.5mm 0 2mm;font-weight:600;border-bottom:1.5px solid #3355FF;padding-bottom:1mm}
table{width:100%;border-collapse:collapse}
td{padding:1.3mm 3mm;vertical-align:top;border-bottom:1px solid #dde4f0;font-size:9.3pt}
td:first-child{width:38%;font-weight:600;background:#f3f6ff;color:#010A21}
.cols{display:flex;gap:6mm}.cols>div{flex:1}
ul{margin:0;padding-left:5mm}li{margin:1mm 0}
.step{display:flex;gap:3mm;align-items:flex-start;margin:2mm 0}
.step b{background:#3355FF;color:#fff;border-radius:50%;width:7mm;height:7mm;min-width:7mm;display:flex;align-items:center;justify-content:center;font-size:9pt}
.plan{display:flex;justify-content:space-between;align-items:center;border:1.5px solid #3355FF;border-radius:10px;padding:3mm 4mm;margin:2mm 0}
.plan .n{font-weight:600}.plan .s{font-size:9pt;color:#4a5878}.plan .p{font-size:16pt;font-weight:700;color:#3355FF}
.faq p{margin:0 0 .5mm}.faq .q{font-weight:600}.faq div{margin-bottom:2.5mm}
.nota{font-size:8pt;color:#4a5878;margin-top:5mm}
.foot{position:absolute;left:14mm;right:14mm;bottom:8mm;display:flex;justify-content:space-between;font-size:8.5pt;color:#4a5878;border-top:1px solid #dde4f0;padding-top:2mm}
.foot b{color:#3355FF}
.box{background:#f3f6ff;border-radius:10px;padding:4mm}
.page:last-child{page-break-after:auto}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm}.kpi{background:#f3f6ff;border-radius:10px;padding:3mm}.kpi small{display:block;color:#4a5878;font-size:8pt;text-transform:uppercase;letter-spacing:.3px}.kpi b{font-size:10.5pt;color:#010A21}
"""

def esc(s): return html.escape(s)

def foot(extra=''):
    return f"<div class='foot'><span><b>elvo·</b> Agua pura. Simplificada.</span><span>{PIE}{extra}</span></div>"

def hero(d, tipo):
    return f"""<div class='hero'><div class='t'><div class='tipo'>{tipo}</div><div class='tag'>{esc(d['tag'])}</div>
    <h1>{esc(d['nombre'])}</h1><p>{esc(d['resumen'])}</p></div><img src='{d['foto']}'></div>"""

def tecnica_html(d):
    rows = ''.join(f"<tr><td>{esc(a)}</td><td>{esc(b)}</td></tr>" for a, b in d['tecnica'])
    et = ''.join(f"<tr><td>{i+1}. {esc(a)}</td><td>{esc(b)}</td></tr>" for i, (a, b) in enumerate(d['etapas']))
    inc = ''.join(f"<li>{esc(x)}</li>" for x in d['incluye'])
    return f"""<div class='page'>{hero(d,'Ficha técnica')}
    <h2>Especificaciones</h2><table>{rows}</table>
    <h2>Etapas de filtración</h2><table>{et}</table>
    <div class='cols'><div><h2>Qué incluye</h2><ul>{inc}</ul></div>
    <div><h2>Mantenimiento</h2><p style='margin:0;font-size:10pt'>{esc(d['mantenimiento'])}</p></div></div>
    <div class='nota'>{esc(d['nota'])}</div>{foot()}</div>"""

def ventas_html(d):
    para = ''.join(f"<li>{esc(x)}</li>" for x in d['para'])
    pasos = ''.join(f"<div class='step'><b>{i+1}</b><span>{esc(x)}</span></div>" for i, x in enumerate(d['pasos']))
    planes = ''.join(f"<div class='plan'><div><div class='n'>{esc(a)}</div><div class='s'>{esc(b)}</div></div><div class='p'>{esc(c)}</div></div>" for a, b, c in d['planes'])
    inc = ''.join(f"<li>{esc(x)}</li>" for x in d['incluye'])
    envio = ''.join(f"<li>{esc(x)}</li>" for x in d['envio'])
    faq = ''.join(f"<div><p class='q'>{esc(q)}</p><p>{esc(a)}</p></div>" for q, a in d['faq'])
    quick = ''.join(f"<div class='kpi'><small>{esc(a)}</small><b>{esc(b)}</b></div>" for a, b in d['tecnica'][:4])
    return f"""<div class='page'>{hero(d,'Ficha de ventas')}
    <div class='cols'><div><h2>¿Para quién es?</h2><ul>{para}</ul></div>
    <div><h2>Cómo se usa</h2>{pasos}</div></div>
    <h2>En pocas palabras</h2><div class='kpis'>{quick}</div>
    <h2>Qué incluye</h2><ul>{inc}</ul>
    <div class='nota'>Precios vigentes al {FECHA}. Confirma siempre en elvo.pe.</div>{foot(' · 1/2')}</div>
    <div class='page'><h2 style='margin-top:0'>Precios y planes</h2>{planes}<p style='font-size:10pt;margin:2mm 0'>{esc(d['repuesto'])}</p>
    <div class='cols'><div><h2>Mantenimiento y repuestos</h2><p style='margin:0;font-size:10pt'>{esc(d['mantenimiento'])}</p></div>
    <div><h2>Envío, pago y garantía</h2><ul>{envio}</ul><p style='font-size:10pt;margin:2mm 0'><b>Garantía:</b> {esc([b for a,b in d['tecnica'] if a=='Garantía'][0])}</p></div></div>
    <h2>Preguntas frecuentes</h2><div class='faq'>{faq}</div>
    <h2>Cómo comprar</h2><div class='box'>Compra en <b>www.elvo.pe</b> o escríbenos desde la web. Te ayudamos a elegir el plan y a dejar tu equipo funcionando.</div>
    <div class='nota'>{esc(d['nota'])}</div>{foot(' · 2/2')}</div>"""

def main():
    os.makedirs(OUT, exist_ok=True)
    for k, d in P.items():
        for kind, fn in (('ficha-tecnica', tecnica_html), ('ficha-ventas', ventas_html)):
            h = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{fn(d)}</body></html>"
            open(f"/tmp/fichas/{k}-{kind}.html", 'w').write(h)
main()
