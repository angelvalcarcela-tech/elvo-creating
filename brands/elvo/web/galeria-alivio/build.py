from pathlib import Path
D=Path(__file__).parent
HEAD='''<!doctype html><html lang="es"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Plus+Jakarta+Sans:wght@500;600;700&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1200px;height:1200px;overflow:hidden}
body{font-family:'Inter',Arial,sans-serif;color:#050607;position:relative;background:#DCE6EE}
h1,h2,h3,.pj{font-family:'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:-.025em}
.k{font-size:30px;font-weight:600;letter-spacing:.13em;text-transform:uppercase;color:#3355FF}
.ic{width:84px;height:84px;color:#3355FF;flex:none}
.ic svg{width:100%;height:100%;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.fn{position:absolute;left:72px;right:72px;bottom:38px;font-size:26px;line-height:1.25;color:#5B6470}
.num{width:70px;height:70px;border-radius:50%;background:#3355FF;color:#fff;font-family:'Plus Jakarta Sans';font-weight:700;font-size:36px;display:grid;place-items:center;flex:none}
'''
def page(name,body,css='',bg=None):
    b=f'<body style="background:{bg}">' if bg else '<body>'
    (D/f'{name}.html').write_text(HEAD+f'<style>{css}</style></head>'+b+body+'</body></html>',encoding='utf-8')
def pill(t,solid=False):
    s='background:#3355FF;color:#fff' if solid else 'background:#fff'
    return f'<span style="{s};border-radius:999px;padding:14px 28px;font-size:32px;font-weight:600;white-space:nowrap">{t}</span>'
JARRA='<svg viewBox="0 0 48 48"><path d="M12 14h22v22a4 4 0 0 1-4 4H16a4 4 0 0 1-4-4z"/><path d="M34 18h4a3 3 0 0 1 3 3v6a3 3 0 0 1-3 3h-4M12 14l-2-4h26l-2 4"/><path d="M18 26c2 2 4 2 6 0s4-2 6 0"/></svg>'
RAYO='<svg viewBox="0 0 48 48"><path d="M27 4L10 27h12l-3 17 19-25H26z"/><path d="M6 6l36 36"/></svg>'
CANO='<svg viewBox="0 0 48 48"><path d="M8 12h14a8 8 0 0 1 8 8v4M8 8v8M30 24v4"/><path d="M30 33c-3 4-4 6-4 8a4 4 0 0 0 8 0c0-2-1-4-4-8z"/><path d="M6 6l36 36"/></svg>'
GOTA='<svg viewBox="0 0 48 48"><path d="M24 5c7 9 12 15 12 21a12 12 0 0 1-24 0c0-6 5-12 12-21z"/><path d="M18 28a6 6 0 0 0 6 6"/></svg>'
EQUIPO='<svg viewBox="0 0 48 48"><rect x="12" y="4" width="24" height="10" rx="5"/><rect x="10" y="14" width="28" height="12" rx="2"/><rect x="10" y="26" width="28" height="10" rx="2"/><path d="M8 44h32l-3-8H11z"/></svg>'
FILTRO='<svg viewBox="0 0 48 48"><rect x="14" y="6" width="20" height="36" rx="4"/><path d="M14 16h20M14 26h20M14 34h20"/></svg>'
# 1 principal
page('s1','''<img src="assets/producto.png" style="position:absolute;inset:0;width:1200px;height:1200px;transform:scale(1.16);transform-origin:50% 60%">
<div style="position:absolute;left:40px;top:48px;display:flex;gap:12px;align-items:center">'''+pill('Alivio 16 · Alivio 22',True)+pill('Purificador de bidón')+'</div>')
# 2 beneficios
def row(ic,t): return f'<div style="display:flex;gap:26px;align-items:center"><div class="ic">{ic}</div><h3 style="font-size:46px;line-height:1.12;font-weight:600">{t}</h3></div>'
page('s2',f'''<div style="position:absolute;right:-110px;bottom:0;width:820px;height:820px;-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 24%)"><img src="assets/producto.png" style="width:100%"></div>
<div style="position:absolute;left:72px;top:84px;width:760px"><span class="k">Alivio</span>
<h1 style="font-size:74px;line-height:1.04;font-weight:600;margin-top:18px">Agua de reserva en casa.</h1></div>
<div style="position:absolute;left:72px;top:430px;width:660px;display:flex;flex-direction:column;gap:46px">{row(JARRA,"Se llena con una jarra")}{row(RAYO,"Sin electricidad")}{row(CANO,"Sin conexión al caño")}</div>''')
# 3 cómo funciona
def step(n,t,s): return f'<div style="display:flex;gap:28px;align-items:center"><div class="num" style="width:86px;height:86px;font-size:44px">{n}</div><div><h3 style="font-size:56px;font-weight:600;line-height:1.05">{t}</h3><p style="font-size:38px;color:#5B6470;margin-top:6px;line-height:1.15">{s}</p></div></div>'
page('_drop',f'''<div style="position:absolute;right:0;top:380px;width:520px;height:760px;overflow:hidden;border-radius:40px 0 0 40px"><img src="assets/producto.png" style="width:760px;margin:-60px 0 0 -120px"></div>
<div style="position:absolute;left:72px;top:84px"><span class="k">Cómo funciona</span><h1 style="font-size:84px;font-weight:600;margin-top:14px;line-height:1.04">Tres pasos,<br>sin instalación</h1></div>
<div style="position:absolute;left:72px;top:470px;width:640px;display:flex;flex-direction:column;gap:54px">{step(1,"Llénalo","con una jarra")}{step(2,"Purifica","por gravedad")}{step(3,"Sirve","directo de la llave")}</div>''',bg='#EEF3F7')

def foto(name,img,kick,title,sub,pos='50% 55%'):
    page(name,f'''<img src="assets/{img}" style="position:absolute;left:0;top:0;width:1200px;height:990px;object-fit:cover;object-position:{pos}">
<div style="position:absolute;left:0;right:0;bottom:0;height:210px;background:#010A21;color:#fff;padding:26px 72px 0"><span class="k" style="color:#BFD0FF;font-size:30px">{kick}</span>
<h1 style="font-size:70px;line-height:1.04;font-weight:600;margin-top:6px">{title}</h1><p style="font-size:38px;line-height:1.15;margin-top:6px;color:#C9D6EA">{sub}</p></div>''')
foto('s3','g2-jarra.png','Paso 1','Llénalo con una jarra','Sin conexión al caño y sin electricidad.','30% 50%')
foto('s4','g8-filtro.png','Paso 2','Purifica por gravedad','El agua baja sola por los filtros.')
foto('s5','g3-vaso.png','Paso 3','Sirve cuando quieras','Directo de la llave a tu vaso.','50% 55%')
foto('s6','g4-botella.png','Para llevar','Llena tu botella','O tu jarra, o tu vaso.','50% 55%')
foto('s7','g5-armado.png','Armado','Lo armas tú, en casa','Coloca el filtro y listo.')
foto('s9','g6-ph.png','Gotas de pH incluidas','Mide el pH de tu agua','Una gota en el vaso y comparas.')

# 4 tamaños
def size(n,p,img=None):
    return f'''<div style="width:500px;background:#fff;border-radius:34px;padding:40px 40px 44px;text-align:center"><span class="k">Alivio {n}</span>
<div style="width:300px;height:300px;margin:18px auto 8px;overflow:hidden;border-radius:24px">{img or '<img src="assets/producto.png" style="width:520px;margin:-80px 0 0 -110px">'}</div>
<h2 style="font-size:92px;font-weight:700;line-height:1">{n}<span style="font-size:48px;font-weight:600;margin-left:10px">litros</span></h2>
<p style="font-size:44px;font-weight:600;color:#3355FF;margin-top:18px">S/ {p}</p></div>'''
page('s10',f'''<div style="position:absolute;left:72px;top:72px"><span class="k">Tamaños</span><h1 style="font-size:78px;font-weight:600;margin-top:14px;line-height:1.04">Elige cuánto alivio<br>quieres tener</h1></div>
<div style="position:absolute;left:72px;top:330px;display:flex;gap:56px">{size(16,159)}{size(22,198,'<img src="assets/producto22.png" style="width:360px;margin:-30px 0 0 -30px">')}</div>
<div style="position:absolute;left:72px;top:1040px;font-size:42px;font-weight:500">Más litros, más alivio. <span style="color:#5B6470">Alivio 22, para toda la casa.</span></div>
<div class="fn">Capacidad total del recipiente.</div>''',bg='#EEF3F7')
# 5 por dentro
def lab(y,n,t,sub='',h=''):
    s_=f'<p style="font-size:30px;line-height:1.2;color:#5B6470;margin-top:8px">{sub}</p>' if sub else ''
    return f'''<div style="position:absolute;left:760px;top:{y}px;width:380px;transform:translateY(-50%)"><div style="display:flex;gap:18px;align-items:center"><div class="num">{n}</div><h3 style="font-size:42px;font-weight:600;line-height:1.1">{t}</h3></div>{s_}</div>
<div style="position:absolute;left:560px;top:{y}px;width:160px;height:3px;background:#3355FF"></div><div style="position:absolute;left:552px;top:{y-7}px;width:16px;height:16px;border-radius:50%;background:#3355FF"></div>'''
page('s8',f'''<div style="position:absolute;left:72px;top:60px"><span class="k">Alivio · Por dentro</span><h1 style="font-size:76px;font-weight:600;margin-top:12px">Tres etapas de filtrado</h1></div>
<img src="assets/explosionado.png" style="position:absolute;left:-40px;top:200px;width:900px;height:900px">
{lab(335,1,"Filtro cerámico")}{lab(640,2,"Filtro multimedia","5 capas: carbón activado y de plata, WMSM-300, arena de sílice, zeolita y arena mineral")}{lab(960,3,"Piedra mineral")}
<div class="fn">Esquema ilustrativo. Los resultados dependen de la calidad del agua de entrada.</div>''',bg='#fff')
# 6 repuesto
page('s11',f'''<div style="position:absolute;left:72px;top:72px"><span class="k">Kit de repuesto</span><h1 style="font-size:78px;font-weight:600;margin-top:14px;line-height:1.04">Un kit, hasta<br>un año de uso</h1></div>
<div style="position:absolute;left:72px;top:380px;width:1056px;height:420px;border-radius:34px;overflow:hidden"><img src="assets/repuesto.webp" style="width:900px;margin:-350px 0 0 78px;display:block"></div>
<div style="position:absolute;left:72px;top:850px;width:1056px;display:flex;flex-direction:column;gap:22px;font-size:44px;font-weight:500;line-height:1.15">
<div>Rinde <b>10,000 litros o 1 año</b>, lo que ocurra primero.</div><div>Tu equipo ya trae su filtro. El kit de repuesto es <b>S/95</b>, aparte.</div></div>''',bg='#EEF3F7')
# 7 incluye
li=''.join(f'<div style="display:flex;gap:26px;align-items:center"><div class="ic">{i}</div><span style="font-size:48px;font-weight:600;line-height:1.1">{t}</span></div>' for i,t in [(EQUIPO,'Purificador elvo· Alivio'),(FILTRO,'Filtro interno incluido'),(GOTA,'Gotas de pH para medir tu agua')])
page('s12',f'''<div style="position:absolute;left:72px;top:72px"><span class="k">En la caja</span><h1 style="font-size:78px;font-weight:600;margin-top:14px;line-height:1.04">Todo viene<br>incluido</h1></div>
<div style="position:absolute;right:60px;top:72px;width:520px;height:520px"><img src="assets/producto.png" style="width:100%;border-radius:34px"></div>
<div style="position:absolute;left:72px;top:680px;display:flex;flex-direction:column;gap:56px;width:1000px">{li}</div>''',bg='#fff')
# 8 cierre
page('s13',f'''<div style="position:absolute;left:72px;top:84px;width:1000px"><span class="k">Alivio</span>
<h1 style="font-size:84px;line-height:1.05;font-weight:600;margin-top:18px">Dejas de estar pendiente del caño.</h1></div>
<div style="position:absolute;left:72px;top:520px;display:flex;gap:16px;flex-wrap:wrap;width:1000px">{pill("Garantía de 6 meses")}{pill("Soporte por WhatsApp")}</div>
<div style="position:absolute;left:72px;top:690px;width:640px;font-size:50px;font-weight:600;line-height:1.15">Escríbenos y te acompañamos a elegir: 16 o 22.</div>
<div style="position:absolute;right:-40px;bottom:-20px;width:520px"><img src="assets/producto.png" style="width:100%;border-radius:40px"></div>''',bg='#EEF3F7')
print('ok')
