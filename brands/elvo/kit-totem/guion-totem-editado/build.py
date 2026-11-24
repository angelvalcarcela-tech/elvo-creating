import os
D=os.path.dirname(os.path.abspath(__file__))
CSS='''
@font-face{font-family:Mont;font-weight:400;src:url(fonts/montserrat-latin-400-normal.woff2)}
@font-face{font-family:Mont;font-weight:500;src:url(fonts/montserrat-latin-500-normal.woff2)}
@font-face{font-family:Mont;font-weight:600;src:url(fonts/montserrat-latin-600-normal.woff2)}
@font-face{font-family:Mont;font-weight:700;src:url(fonts/montserrat-latin-700-normal.woff2)}
@page{size:1440px 810px;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Mont,sans-serif}
.pg{width:1440px;height:810px;position:relative;overflow:hidden;page-break-after:always;background:#FAFAFA}
.bg{position:absolute;left:0;top:0;width:1440px;height:810px}
.cov{position:absolute;background:#FAFAFA}
.cap{position:absolute;font-size:13.4px;line-height:1.3;color:#111;font-weight:500}
.cap b{font-weight:700;color:#111}
.tag{position:absolute;font-size:10.5px;font-weight:700;color:#1A22C4;letter-spacing:.06em;text-transform:uppercase}
'''
# (page, bbox x0,y0,x1,y1, html, tag)
EDITS={
2:[((265,600,535,729),'<b>Hola.</b> En casa hay tres formas de tener agua pura. Te cuento cómo funciona cada una.'),
   ((594,602,864,667),'Nativo, Alivio y Cero: agua lista para tomar, de forma práctica y sencilla.'),
   ((936,598,1207,663),'Cada una resuelve una necesidad distinta de tu hogar.')],
3:[((151,597,699,662),'<b>Nativo</b> va directo a tu caño: conectas el derivador, mueves la palanca a “filtrada” y sirves por el pico. Lo instalas tú, en 5 minutos, sin gasfitero. Trae adaptador para cualquier caño y el núcleo rinde hasta 20.000 litros en 18 meses; te avisamos por WhatsApp cuando toca cambiarlo.'),
   ((788,598,1332,642),'<b>Alivio</b> es agua de reserva sin depender del caño: quitas la tapa, llenas con una jarra y sirves por la llave. Sin luz ni instalación, y funciona también con agua de tanque o cisterna. Los filtros rinden hasta 10.000 litros o 1 año.')],
4:[((288,623,836,667),'<b>Cero</b> te da agua fría y caliente al instante: llenas el tanque, eliges la temperatura en la pantalla (desde 6 °C hasta 98 °C) y presionas el botón. Sin instalación ni plomero; puede quedar enchufado.'),
   ((895,612,1165,698),'Los tres tienen 30 días de prueba: si no te convence, te devolvemos tu dinero.')],
5:[((404,632,675,739),'<b>Escríbenos por WhatsApp</b> y te ayudamos a elegir el equipo que va con tu casa.'),
   ((786,625,1057,732),'<b>Black Days de ELVO:</b> una forma más práctica de tener agua en casa. Escríbenos por WhatsApp.')]}
from PIL import Image
pages=[]
for pg in range(1,6):
    im=Image.open(D+f'/bg/pg-{pg}.jpg').convert('RGB')
    h=f'<img class="bg" src="bg/pg-{pg}.jpg">'
    for (x0,y0,x1,y1),t in EDITS.get(pg,[]):
        c=im.getpixel((int((x0-18)*2),int(((y0+y1)/2)*2))); col='#%02x%02x%02x'%c
        h+=f'<div class="cov" style="left:{x0-10}px;top:{y0-6}px;width:{x1-x0+20}px;height:{y1-y0+16}px;background:{col}"></div>'
        h+=f'<div class="cap" style="left:{x0}px;top:{y0}px;width:{x1-x0}px">{t}</div>'
    pages.append(f'<section class="pg">{h}</section>')
# página 6: notas de ELVO
side='<img src="bg/sidebar.png" style="position:absolute;left:0;top:0;width:67px;height:810px">'
body='''<div style="position:absolute;left:107px;top:42px;font-size:34px;font-weight:700;color:#2A2E9E;letter-spacing:.01em">Notas de ELVO</div>
<div style="position:absolute;left:107px;top:112px;width:1230px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:34px;font-size:13.4px;line-height:1.42;color:#222">
<div><div class="h">Lo que cambiamos</div><ul>
<li>Sin signos de exclamación ni “hasta 55 % de descuento”: no hay precios en el video.</li>
<li>Cada producto responde su duda principal: cómo se usa, instalación y duración del filtro.</li>
<li>Un solo CTA: escribir por WhatsApp (“wpp” y “asesor” pasan a “WhatsApp” y “te ayudamos”).</li>
<li>Los 20.000 litros del Nativo van siempre con los 18 meses.</li></ul></div>
<div><div class="h">Para la grabación</div><ul>
<li><b>Nativo:</b> con derivador y manguera conectados; la palanca en “filtrada”; el agua sale solo por el pico del purificador.</li>
<li><b>Alivio:</b> sin logo en el cuerpo; se quita la tapa y se llena con jarra. Es el más alto, se verá más grande.</li>
<li><b>Cero:</b> servir con una taza bajo el botón plateado; sin mangueras.</li>
<li>En los cuadros de ejemplo aparece un purificador de otra marca: en el video final deben verse los equipos de ELVO.</li></ul></div>
<div><div class="h">Estructura sugerida (20 s)</div><ul>
<li><b>0 a 3 s:</b> gancho, con el agua cayendo al vaso (un problema o beneficio concreto).</li>
<li><b>3 a 14 s:</b> cómo se usa, en 3 pasos cortos.</li>
<li><b>14 a 18 s:</b> la respuesta a la objeción del producto.</li>
<li><b>18 a 20 s:</b> “Escríbenos por WhatsApp”, con el botón en pantalla.</li>
<li>Un video por producto, más uno corto de marca con los tres.</li></ul></div></div>
<div style="position:absolute;left:107px;bottom:46px;width:1230px;font-size:12px;color:#666">Tono: cercano y amigable, la persona habla como contándole a un amigo. Más detalle en la guía de grabación y en el guion por producto del paquete.</div>
<style>.h{font-size:11.5px;font-weight:700;color:#1A22C4;letter-spacing:.08em;text-transform:uppercase;margin-bottom:10px}ul{list-style:none}li{padding-left:16px;position:relative;margin-bottom:9px}li:before{content:"";position:absolute;left:0;top:6px;width:6px;height:6px;border-radius:50%;background:#1A22C4}</style>'''
pages.append(f'<section class="pg">{side}{body}</section>')
open(D+'/guion.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS+'</style>'+''.join(pages))
print(len(pages))
