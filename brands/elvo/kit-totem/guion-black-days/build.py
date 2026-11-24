import json,os
D=os.path.dirname(os.path.abspath(__file__))
LP=json.load(open(D+'/logo-path.json'))
def logo(w,color):
    return f'<svg viewBox="0 0 {LP["w"]} {LP["h"]}" style="width:{w}px;height:{w*LP["h"]/LP["w"]}px;color:{color}"><path d="{LP["d"]}" fill="currentColor" fill-rule="evenodd"/></svg>'
CSS='''
@font-face{font-family:Inter;font-weight:400;src:url(fonts/inter-latin-400-normal.woff2)}
@font-face{font-family:Inter;font-weight:500;src:url(fonts/inter-latin-500-normal.woff2)}
@font-face{font-family:Inter;font-weight:600;src:url(fonts/inter-latin-600-normal.woff2)}
@font-face{font-family:Inter;font-weight:700;src:url(fonts/inter-latin-700-normal.woff2)}
@page{size:1600px 900px;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,sans-serif;color:#010A21}
.pg{width:1600px;height:900px;position:relative;overflow:hidden;page-break-after:always;background:#FAFAFA;padding:70px 90px}
.hd{position:absolute;left:90px;right:90px;top:34px;display:flex;justify-content:space-between;align-items:center;font-size:14px;letter-spacing:.16em;text-transform:uppercase;color:#5E6B80;font-weight:600}
h1{font-size:84px;line-height:1.03;letter-spacing:-.035em;font-weight:700}
h2{font-size:48px;letter-spacing:-.03em;font-weight:700;margin:26px 0 18px}
h3{font-size:16px;letter-spacing:.14em;text-transform:uppercase;font-weight:700;color:#3355FF;margin-bottom:8px}
p,li{font-size:21px;line-height:1.45;color:#2A3750}
ul{list-style:none}li{padding-left:24px;position:relative;margin-bottom:8px}li:before{content:"";position:absolute;left:0;top:11px;width:8px;height:8px;border-radius:50%;background:#3355FF}
table{border-collapse:collapse;width:100%}
th{background:#010A21;color:#fff;font-size:15px;letter-spacing:.08em;text-transform:uppercase;text-align:left;padding:12px 14px}
td{padding:12px 14px;font-size:17px;line-height:1.38;vertical-align:top;border-bottom:1.5px solid #DDE5EE;color:#2A3750}
td b{color:#010A21}
td.t{width:92px;font-weight:700;color:#3355FF;white-space:nowrap}
tr:nth-child(even) td{background:#F1F5FA}
.foot{position:absolute;left:90px;right:90px;bottom:26px;font-size:13px;color:#7C8AA0}
.card{background:#fff;border-radius:22px;border:1.5px solid #DDE5EE;padding:26px}
.pill{display:inline-block;background:#3355FF;color:#fff;border-radius:30px;padding:6px 16px;font-size:14px;font-weight:700;letter-spacing:.06em;margin-right:8px}
.badge{display:inline-block;border:2px solid #3355FF;color:#3355FF;border-radius:30px;padding:5px 14px;font-size:14px;font-weight:700;margin-right:6px}
'''
pages=[]
def P(h,bg=None):
    st=f' style="background:{bg}"' if bg else ''
    pages.append(f'<section class="pg"{st}>{h}</section>')
def HD(t,dark=False):
    c='#9EBACE' if dark else '#5E6B80'
    return f'<div class="hd" style="color:{c}"><span>{t}</span>{logo(90,"#fff" if dark else "#5891CB")}<span>ELVO × TOTEM</span></div>'
FOOT='<div class="foot">*Según la ficha técnica del núcleo PureCore. Los resultados dependen de la calidad del agua de entrada y del cambio oportuno del núcleo.</div>'
def beats(rows):
    h='<table><tr><th>Seg.</th><th>Imagen</th><th>Diálogo (voz en cámara)</th><th>Texto en pantalla</th></tr>'
    for t,i,d,x in rows: h+=f'<tr><td class="t">{t}</td><td>{i}</td><td><b>{d}</b></td><td>{x}</td></tr>'
    return h+'</table>'
# 1 portada
P(f'<div style="position:absolute;inset:0;background:#010A21"></div><div style="position:absolute;left:90px;top:80px">{logo(190,"#fff")}</div><div style="position:absolute;left:90px;top:330px;color:#fff"><div style="font-size:20px;letter-spacing:.18em;color:#9EBACE;font-weight:600;margin-bottom:20px">GUION · BLACK DAYS</div><h1>Videos que responden<br>las dudas de compra</h1><p style="color:#C4D6E4;font-size:26px;margin-top:28px">Un video por producto: gancho, cómo se usa, respuesta a la objeción y un solo CTA a WhatsApp.</p></div><div style="position:absolute;left:90px;bottom:60px;color:#9EBACE;font-size:18px">Propuesta de ELVO para el equipo de TOTEM · versión con objeciones</div>',bg='#010A21')
# 2 estructura
P(HD('Estructura')+'''<h2 style="margin-top:50px">Cada video dura unos 20 segundos y sigue 4 bloques</h2>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:22px;margin-top:36px">
<div class="card"><h3>1 · Gancho</h3><p style="font-size:30px;font-weight:700;color:#010A21;margin:6px 0 10px">0 a 3 s</p><p>Un problema o un beneficio concreto, con el agua cayendo al vaso. Sin “llegaron los Black Days”.</p></div>
<div class="card"><h3>2 · Cómo se usa</h3><p style="font-size:30px;font-weight:700;color:#010A21;margin:6px 0 10px">3 a 14 s</p><p>El gesto real del producto, en 3 pasos cortos. Es lo que más preguntan los clientes.</p></div>
<div class="card"><h3>3 · Objeción</h3><p style="font-size:30px;font-weight:700;color:#010A21;margin:6px 0 10px">14 a 18 s</p><p>Una línea que responde la duda que más frena la compra de ese producto.</p></div>
<div class="card"><h3>4 · CTA</h3><p style="font-size:30px;font-weight:700;color:#010A21;margin:6px 0 10px">18 a 20 s</p><p>Un solo llamado: “Escríbenos por WhatsApp”. Botón de anuncio que abre la conversación.</p></div></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;margin-top:40px"><div><h3>Formato</h3><ul><li>Vertical 9:16, con subtítulos.</li><li>Tono cercano y amigable; la persona habla como contándole a un amigo.</li><li>Sin precios en el video: el tiempo se usa para explicar cómo se usa.</li></ul></div><div><h3>Por qué WhatsApp y no la web</h3><ul><li>Desde redes, la web convierte 0,26 %; las conversaciones de WhatsApp, entre 2 % y 8 %.</li><li>Cada video con su propio anuncio permite medir qué producto y qué gancho venden.</li></ul></div></div>'''+FOOT)
# 3 mapa de objeciones
rows=[('“¿Cada cuánto cambio el filtro? ¿Cuánto rinde?”','Nativo, Alivio','Muy alta','Nativo: 18 meses o hasta 20.000 litros, con aviso por WhatsApp. Alivio: kit de 10.000 litros o 1 año.'),
('“¿Se adapta a mi caño? ¿Es difícil de instalar?”','Nativo','Muy alta','Lo instalas tú en 5 minutos; adaptador para cualquier caño. Si no encaja, devolvemos el dinero.'),
('“¿Cómo se usa? ¿Necesita luz o instalación?”','Alivio','Muy alta','Se quita la tapa, se llena con jarra y sirve por la llave. Sin luz ni instalación.'),
('“¿Y si no me convence? ¿Qué garantía tiene?”','Todos','Alta','30 días de prueba con devolución del dinero. Pago contraentrega en Lima.'),
('“¿Qué filtra? ¿Metales pesados?”','Nativo','Alta','Retiene plomo y metales pesados*, reduce cloro, olores y sabores.'),
('“¿Funciona con agua de tanque o cisterna?”','Alivio','Alta','Sí, se llena con jarra, funciona con el agua que tengas en casa.'),
('“¿Debe estar enchufado todo el día? ¿Necesita instalación?”','Cero','Alta','Puede quedar enchufado (220 V). Sin cañerías ni plomero: solo llenas el tanque.'),
('“¿Cómo sé cuándo cambiar los filtros?”','Cero','Ocasional','La pantalla avisa cuándo cambiarlos.')]
h='<table><tr><th>Lo que pregunta el cliente</th><th>Video</th><th>Frecuencia</th><th>Respuesta en el video</th></tr>'
for a,b,c,d in rows: h+=f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td><td>{d}</td></tr>'
P(HD('Objeciones')+f'<h2 style="margin-top:44px">Las dudas reales que cada video responde</h2><p style="margin-bottom:18px">Salen de las conversaciones de WhatsApp (YaVendio) de octubre y noviembre.</p>{h}</table>'+FOOT)
# 4 Nativo
P(HD('Video 1 · Nativo')+'<h2 style="margin-top:44px"><span class="pill">NATIVO</span>Agua del caño, lista para tomar</h2><p style="margin-bottom:16px">Objeción principal: ¿se adapta a mi caño y cuánto dura el núcleo?</p>'+beats([
('0 – 3','Primer plano: el agua cae al vaso desde el pico del purificador.','Hola. ¿Y si el agua de tu caño llegara lista para tomar?','Agua lista para tomar'),
('3 – 6','Manos enroscan el derivador en la boca del caño.','Primero conectas el derivador a tu caño.','1 · Conecta el derivador'),
('6 – 9','Manos mueven la palanca del derivador a la posición horizontal (“filtrada”).','Luego mueves la palanca a “filtrada”.','2 · Palanca en filtrada'),
('9 – 14','Vaso llenándose por el pico cromado del purificador; la manguera blanca se ve conectada.','Y sirves por el pico del purificador. Lo instalas tú, en 5 minutos, sin gasfitero.','3 · Sirve el agua'),
('14 – 18','El adaptador de goma ajustable en primer plano; luego el núcleo.','Trae adaptador para cualquier caño. El núcleo rinde hasta 20.000 litros en 18 meses, y te avisamos por WhatsApp cuando toca cambiarlo.','Hasta 20.000 litros en 18 meses · Retiene plomo y metales pesados*'),
('18 – 20','La persona sonríe y toca el botón de WhatsApp.','Si no encaja en tu caño, te devolvemos tu dinero. Escríbenos por WhatsApp y te ayudamos.','Escríbenos por WhatsApp')])+FOOT)
# 5 Alivio
P(HD('Video 2 · Alivio')+'<h2 style="margin-top:44px"><span class="pill">ALIVIO</span>Agua de reserva, sin depender del caño</h2><p style="margin-bottom:16px">Objeción principal: ¿cómo se usa, necesita instalación y cuánto duran los filtros?</p>'+beats([
('0 – 3','El grifo de la cocina sin agua; la persona se acerca al bidón y abre la llave.','Hola. ¿Y si tuvieras agua lista en casa aunque el caño no esté?','Agua de reserva en casa'),
('3 – 6','Manos quitan la tapa domo del bidón.','Quitas la tapa.','1 · Quita la tapa'),
('6 – 9','Se vierte agua de una jarra en el tanque superior.','Llenas el tanque con una jarra.','2 · Llena con una jarra'),
('9 – 14','El agua baja por los filtros; la persona abre la llave y llena un vaso (el agua cae del grifo de la llave).','El agua baja sola, sin luz ni instalación, y la sirves por la llave.','3 · Sirve por la llave'),
('14 – 18','Primer plano de las gotas medidoras de pH; luego el kit de repuesto.','Funciona también con agua de tanque o cisterna. Los filtros rinden hasta 10.000 litros o 1 año, y el equipo trae gotas para medir el pH.','Filtración de 7 etapas'),
('18 – 20','La persona levanta el vaso y toca el botón de WhatsApp.','Tienes 30 días para probarlo. Escríbenos por WhatsApp.','Escríbenos por WhatsApp')])+FOOT)
# 6 Cero
P(HD('Video 3 · Cero')+'<h2 style="margin-top:44px"><span class="pill">CERO</span>Agua fría o caliente, al instante</h2><p style="margin-bottom:16px">Objeción principal: ¿necesita instalación? ¿Debe estar enchufado?</p>'+beats([
('0 – 3','Una taza bajo el equipo; sale agua caliente con vapor suave.','Hola. ¿Agua fría o caliente? Tú eliges, al instante.','Fría desde 6 °C · caliente hasta 98 °C'),
('3 – 6','Manos quitan la tapa trasera superior y llenan el tanque con una jarra.','Primero llenas el tanque por atrás, con una jarra.','1 · Llena el tanque'),
('6 – 9','Dedo toca la pantalla y elige la temperatura.','Eliges la temperatura en la pantalla.','2 · Elige la temperatura'),
('9 – 14','Una taza bajo el equipo; el dedo presiona el botón plateado; sale el agua. Después se saca la jarra de 2 litros y se lleva a la mesa.','Pones tu taza, presionas el botón y listo. O sacas la jarra de 2 litros y la llevas a la mesa.','3 · Presiona el botón'),
('14 – 18','Plano general del equipo sobre la mesada, sin mangueras ni conexiones al caño.','No necesita instalación ni plomero: solo lo enchufas. Puede quedar enchufado, y la pantalla te avisa cuándo cambiar los filtros.','Sin instalación · 220 V'),
('18 – 20','La persona sonríe y toca el botón de WhatsApp.','Tienes 30 días para probarlo. Escríbenos por WhatsApp.','Escríbenos por WhatsApp')])+FOOT)
# 7 marca
P(HD('Video de marca')+'<h2 style="margin-top:44px"><span class="pill">LOS TRES</span>Tres formas de tener agua pura</h2><p style="margin-bottom:16px">Video corto (15 s) para abrir la campaña. Dirige a cada video de producto.</p>'+beats([
('0 – 3','Los tres equipos en la mesa, con la persona al centro.','Hola. En casa hay tres formas de tener agua pura.','Agua pura. Simplificada.'),
('3 – 7','Plano del Nativo con derivador y manguera; sirve un vaso.','Nativo: va directo a tu caño.','Nativo · Para tu caño'),
('7 – 10','Plano del Alivio; se llena con una jarra.','Alivio: agua de reserva, sin depender del caño.','Alivio · Agua de reserva'),
('10 – 13','Plano del Cero; la taza se llena de agua caliente.','Cero: agua fría y caliente al instante.','Cero · Fría y caliente'),
('13 – 15','La persona sonríe y señala el botón de WhatsApp.','Cuéntanos cómo es tu casa y te ayudamos a elegir. Escríbenos por WhatsApp.','Escríbenos por WhatsApp')])+'<div style="margin-top:26px"><h3>Cómo medirlo</h3><p>Cada video sale con su propio anuncio que abre WhatsApp; YaVendio registra las conversaciones y ventas por anuncio.</p></div>'+FOOT)
# 8 cuidados
P(HD('Cuidados')+'''<h2 style="margin-top:44px">Cuidados de grabación y de texto</h2>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:34px;margin-top:20px">
<div><h3>Producto</h3><ul><li><b>Nativo:</b> siempre con derivador y manguera conectados; el agua sale solo por el pico del purificador.</li><li><b>Alivio:</b> sin logo en el cuerpo; se quita la tapa y se llena con jarra; es el más alto (unos 60 cm).</li><li><b>Cero:</b> servir con una taza bajo el botón plateado; sin mangueras.</li></ul></div>
<div><h3>Texto y claims</h3><ul><li>Sin signos de exclamación ni urgencia inventada.</li><li>Los litros siempre junto a los meses.</li><li>“Plomo y metales pesados” siempre con asterisco y nota al pie.</li><li>No nombrar marcas competidoras.</li><li>Sin precios en estos videos.</li></ul></div>
<div><h3>Imagen</h3><ul><li>Agua incolora, sin chorros dramáticos ni burbujas exageradas.</li><li>Los equipos de ELVO a la vista, nunca escondidos.</li><li>Solo clips propios: no usar material de otras marcas.</li><li>Cada video termina con el botón de WhatsApp en pantalla.</li></ul></div></div>
<p style="margin-top:36px;color:#5E6B80">Más detalle en la guía de grabación del paquete: <b>06_Black_Days/Guia_de_grabacion</b>.</p>'''+FOOT)
open(D+'/guion.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS+'</style>'+''.join(pages))
print(len(pages))
