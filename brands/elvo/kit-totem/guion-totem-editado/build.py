from PIL import Image
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
.cap div{margin-bottom:5px}.k{color:#1A22C4;font-weight:700}.cap{position:absolute;font-size:16.5px;line-height:1.3;color:#111;font-weight:500}
.cap b{font-weight:700;color:#111}
.tag{position:absolute;font-size:10.5px;font-weight:700;color:#1A22C4;letter-spacing:.06em;text-transform:uppercase}
'''
# (page, bbox x0,y0,x1,y1, html, tag)
EDITS={
3:[((151,597,699,662),'<div><b>Nativo.</b> Directo en tu caño: lo instalas tú en 5 minutos.</div><div>Núcleo de 18 meses: hasta 20.000 litros.</div><div class="k">Agua rica, sin sabor a cloro. Retiene plomo y metales pesados*.</div>'),
   ((788,598,1332,642),'<div><b>Alivio.</b> Llenas con una jarra, baja por los filtros y sirves.</div><div>Agua de reserva lista en casa, sin luz ni instalación.</div><div class="k">¿Poca presión de agua? Funciona sin depender del caño.</div>')],
4:[((288,623,836,667),'<div><b>Cero.</b> Fría desde 6 °C, caliente hasta 98 °C, al instante. Perfecto para tu casa o oficina.</div><div>Jarra extraíble de 2 L, autolimpieza y aviso de cambio de filtros.</div><div class="k">Máxima purificación: ósmosis inversa y luz UV.</div>'),
   ((895,612,1165,698),'<b>30 días de prueba</b> y <b>1 año de garantía</b> en los tres.')],
5:[((404,632,675,739),'<b>Haz clic en este video</b> y te asesoramos por WhatsApp para tu compra.')]}
pages=[]
for pg in range(1,6):
    im=Image.open(D+f'/bg/pg-{pg}.jpg').convert('RGB')
    h=f'<img class="bg" src="bg/pg-{pg}.jpg">'
    for (x0,y0,x1,y1),t in EDITS.get(pg,[]):
        c=im.getpixel((int((x0-18)*2),int(((y0+y1)/2)*2))); col='#%02x%02x%02x'%c
        h+=f'<div class="cov" style="left:{x0-10}px;top:{y0-6}px;width:{x1-x0+20}px;height:{max(y1-y0+16,140 if (pg in (3,4) and (x1-x0)>400) else 0)}px;background:{col}"></div>'
        h+=f'<div class="cap" style="left:{x0}px;top:{y0}px;width:{x1-x0}px">{t}</div>'
    if pg==3: h+='<div style="position:absolute;left:151px;bottom:40px;font-size:11px;color:#555">*Según la ficha técnica del núcleo PureCore. Los resultados dependen de la calidad del agua de entrada.</div>'
    pages.append(f'<section class="pg">{h}</section>')
# página 6: notas de ELVO
side='<img src="bg/sidebar.png" style="position:absolute;left:0;top:0;width:67px;height:810px">'
body='''<div style="position:absolute;left:107px;top:42px;font-size:34px;font-weight:700;color:#2A2E9E;letter-spacing:.01em">Notas de ELVO</div>
<div style="position:absolute;left:107px;top:112px;width:1230px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:34px;font-size:14px;line-height:1.42;color:#222">
<div><div class="h">Lo que decide la compra</div><ul>
<li><b>Nativo:</b> agua rica y metales pesados retenidos*, con practicidad y durabilidad como apoyo.</li>
<li><b>Alivio:</b> para quien tiene poca presión de agua y quiere agua reservada en casa.</li>
<li><b>Cero:</b> la máxima purificación: ósmosis inversa y luz UV.</li>
<li>Un solo CTA: WhatsApp.</li></ul></div>
<div><div class="h">Detalle para quien lo necesite</div><ul>
<li><b>Nativo:</b> derivador y manguera conectados, palanca en “filtrada”; adaptador para cualquier caño. Si no encaja, se devuelve el dinero.</li>
<li><b>Alivio:</b> sin logo en el cuerpo; funciona con agua de tanque o cisterna. Filtros: 10.000 litros o 1 año.</li>
<li><b>Cero:</b> taza bajo el botón plateado; puede quedar enchufado.</li></ul></div>
<div><div class="h">Video de 20 s</div><ul>
<li><b>0 a 3 s:</b> gancho con el agua cayendo al vaso.</li>
<li><b>3 a 14 s:</b> cómo se usa, en 3 pasos.</li>
<li><b>14 a 18 s:</b> respuesta a la duda del producto.</li>
<li><b>18 a 20 s:</b> “Escríbenos por WhatsApp”.</li>
<li>En el video final deben verse los equipos de ELVO.</li></ul></div></div>
<div style="position:absolute;left:107px;bottom:46px;width:1230px;font-size:12px;color:#666">Tono cercano y amigable. Más detalle en el guion por producto y en la guía de grabación del paquete.</div>
<style>.h{font-size:11.5px;font-weight:700;color:#1A22C4;letter-spacing:.08em;text-transform:uppercase;margin-bottom:10px}ul{list-style:none}li{padding-left:16px;position:relative;margin-bottom:9px}li:before{content:"";position:absolute;left:0;top:6px;width:6px;height:6px;border-radius:50%;background:#1A22C4}</style>'''
pages.append(f'<section class="pg">{side}{body}</section>')
open(D+'/guion.html','w').write('<!doctype html><meta charset=utf-8><style>'+CSS+'</style>'+''.join(pages))
print(len(pages))
