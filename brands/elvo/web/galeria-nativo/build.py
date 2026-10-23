from pathlib import Path
import textwrap
D=Path(__file__).parent
HEAD='''<!doctype html><html lang="es"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Plus+Jakarta+Sans:wght@500;600;700&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1200px;height:1200px;overflow:hidden}
body{font-family:'Inter',Arial,sans-serif;color:#050607;position:relative;background:#DCE6EE}
h1,h2,h3,.pj{font-family:'Plus Jakarta Sans',Arial,sans-serif;letter-spacing:-.025em}
.k{font-size:20px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:#3355FF}
.ic{width:84px;height:84px;color:#3355FF;flex:none}
.ic svg{width:100%;height:100%;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.fn{position:absolute;left:72px;bottom:44px;font-size:19px;color:#6B7480}
.brand{position:absolute;right:72px;bottom:40px;font-family:'Plus Jakarta Sans';font-weight:700;font-size:34px;letter-spacing:-.04em}
'''
def page(name,body,css='',bg=None):
    style=f'<style>{css}</style>'
    b=f'<body style="background:{bg}">' if bg else '<body>'
    (D/f'{name}.html').write_text(HEAD+style+'</head>'+b+body+'</body></html>',encoding='utf-8')

# 1 principal
page('s1','''<img src="assets/producto.webp" style="position:absolute;inset:0;width:1200px;height:1200px">
<div style="position:absolute;left:56px;top:52px;display:flex;gap:14px;align-items:center">
<span class="pj" style="background:#3355FF;color:#fff;font-weight:700;font-size:23px;letter-spacing:.1em;padding:13px 26px;border-radius:999px">BESTSELLER</span>
<span style="background:#fff;border-radius:999px;padding:12px 24px;font-size:24px;font-weight:500;display:flex;gap:10px;align-items:center"><span style="color:#F2B01E;letter-spacing:2px;font-size:26px">★★★★☆</span> 4,2 · 124 reseñas en Falabella</span></div>''')
# 2 beneficios
ICON_SHIELD='<svg viewBox="0 0 48 48"><path d="M24 4l16 6v12c0 10-6.500 18-16 22C14.500 40 8 32 8 22V10z"/><path d="M17 24l5 5 9-10"/></svg>'
ICON_DROP='<svg viewBox="0 0 48 48"><path d="M24 5c7 9 12 15 12 21a12 12 0 0 1-24 0c0-6 5-12 12-21z"/><path d="M18 28a6 6 0 0 0 6 6"/></svg>'
ICON_LEAF='<svg viewBox="0 0 48 48"><path d="M38 8C20 8 10 17 10 30c0 4 2 8 6 10 14 2 22-8 22-32z"/><path d="M10 40c6-10 12-16 22-22"/></svg>'
page('s2',f'''<div style="position:absolute;right:-60px;bottom:0;width:820px;height:820px;-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 22%)"><img src="assets/producto.webp" style="width:100%"></div>
<div style="position:absolute;left:72px;top:84px;width:760px"><span class="k">Nativo</span>
<h1 style="font-size:74px;line-height:1.04;font-weight:600;margin-top:18px">Agua más limpia, directo de tu caño.</h1></div>
<div style="position:absolute;left:72px;top:470px;width:600px;display:flex;flex-direction:column;gap:46px">
<div style="display:flex;gap:26px;align-items:center"><div class="ic">{ICON_SHIELD}</div><h3 style="font-size:40px;line-height:1.12;font-weight:600">Retiene metales pesados*</h3></div>
<div style="display:flex;gap:26px;align-items:center"><div class="ic">{ICON_DROP}</div><h3 style="font-size:40px;line-height:1.12;font-weight:600">Reduce cloro, olores y sabores</h3></div>
<div style="display:flex;gap:26px;align-items:center"><div class="ic">{ICON_LEAF}</div><h3 style="font-size:40px;line-height:1.12;font-weight:600">Conserva los minerales del agua</h3></div></div>
<div class="fn">*Según ficha técnica del núcleo PureCore.</div>''')
# 3 etapas
etapas=[('Carbón activado','Reduce cloro, olores y sabores.','#1b1d20'),('KDF-F','Retiene plomo y metales pesados*.','#B7793C'),('Nanotecnología','Etapa adicional del núcleo PureCore.','#E6EAEE'),('Aluminosilicato sintético','Cuida la calidad del agua.','#D9C9A8'),('Plata coloidal','Protege el núcleo por dentro.','#BFC5CC'),('Plata iónica','Protege el núcleo por dentro.','#F4F6F8')]
bands=''; y=180; h=120
for i,(n,t,c) in enumerate(etapas):
    pat=''
    if i in(0,2,4):
        dots=''.join(f'<circle cx="{26+ (k%5)*32+(14 if (k//5)%2 else 0)}" cy="{y+14+(k//5)*28}" r="7" fill="{"#3a3d42" if i==0 else "#ffffff" if i==2 else "#e8ecef"}" opacity=".9"/>' for k in range(20))
        pat=dots
    bands+=f'<rect x="10" y="{y}" width="180" height="{h}" fill="{c}"/>{pat}'
    y+=h
core=f'''<svg width="200" height="1010" viewBox="0 0 200 1010" style="position:absolute;left:96px;top:128px"><defs><clipPath id="cc"><rect x="10" y="180" width="180" height="720" rx="6"/></clipPath></defs>
<rect x="55" y="80" width="90" height="40" rx="10" fill="#EEF2F6"/><rect x="0" y="118" width="200" height="64" rx="16" fill="#F5F7FA"/>
<g clip-path="url(#cc)">{bands}</g><rect x="0" y="898" width="200" height="64" rx="16" fill="#F5F7FA"/><rect x="62" y="950" width="76" height="30" rx="8" fill="#EEF2F6"/></svg>'''
rows=''
for i,(n,t,c) in enumerate(etapas):
    rows+=f'<div style="display:flex;gap:24px;align-items:center;height:120px"><div style="width:62px;height:62px;border-radius:50%;background:#3355FF;color:#fff;font-family:Plus Jakarta Sans;font-weight:700;font-size:30px;display:grid;place-items:center;flex:none">{i+1}</div><div><h3 style="font-size:34px;font-weight:600;color:#fff">{n}</h3><p style="font-size:24px;color:#BED0DF;margin-top:4px">{t}</p></div></div>'
page('s3',f'''<div style="position:absolute;left:72px;top:60px"><span class="k" style="color:#8FA5FF">Nativo · Núcleo PureCore</span><h1 style="font-size:76px;color:#fff;font-weight:600;margin-top:12px">6 etapas por dentro</h1></div>
{core}<div style="position:absolute;left:420px;top:316px;width:720px">{rows}</div>
<div class="fn" style="color:#8FA5C0">*Según ficha técnica del núcleo PureCore. Esquema ilustrativo.</div>''',bg='#010A21')
# 4 instalacion
def card(n,img,t,extra='',zoom=''):
    return f'''<div style="width:500px"><div style="position:relative;width:500px;height:500px;border-radius:30px;overflow:hidden;{extra}"><img src="{img}" style="width:100%;height:100%;object-fit:cover;{zoom}"><div style="position:absolute;left:22px;top:22px;width:62px;height:62px;border-radius:50%;background:#3355FF;color:#fff;font-family:Plus Jakarta Sans;font-weight:700;font-size:32px;display:grid;place-items:center">{n}</div></div><h3 style="font-size:36px;font-weight:600;margin-top:26px;line-height:1.15">{t}</h3></div>'''
page('s4',f'''<div style="position:absolute;left:72px;top:84px"><span class="k">Instalación</span><h1 style="font-size:84px;font-weight:600;margin-top:14px;line-height:1.04">Lo instalas tú<br>en 5 minutos</h1></div>
<div style="position:absolute;left:72px;top:430px;display:flex;gap:56px">{card(1,"assets/gal-adaptador2.png","Enrosca el adaptador universal de jebe a tu caño")}{card(2,"assets/producto.webp","¡Listo! Agua filtrada al instante","background:#DCE6EE","transform:scale(1.45) translate(-2%,8%);transform-origin:55% 60%")}</div>
<div style="position:absolute;left:72px;bottom:60px;display:flex;gap:16px">{"".join(f'<span style="background:#fff;border-radius:999px;padding:14px 26px;font-size:25px;font-weight:500">{x}</span>' for x in ["Sin gasfitero","Sin electricidad","Adaptador ajustable incluido"])}</div>''',bg='#EEF3F7')
# 5 comparativa
CHECK='<svg viewBox="0 0 40 40" width="52" height="52"><circle cx="20" cy="20" r="19" fill="#3355FF"/><path d="M11 21l6 6 12-13" stroke="#fff" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CROSS='<svg viewBox="0 0 40 40" width="52" height="52"><circle cx="20" cy="20" r="19" fill="#E4EAF0"/><path d="M13 13l14 14M27 13L13 27" stroke="#7C8794" stroke-width="3.2" stroke-linecap="round"/></svg>'
VAR='<span style="font-size:24px;color:#6B7480;font-weight:500">Varía</span>'
POT='<svg viewBox="0 0 100 80" width="120" height="96" fill="none" stroke="#5B6470" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M16 34h68v26a14 14 0 0 1-14 14H30a14 14 0 0 1-14-14z"/><path d="M8 40h8M84 40h8M34 34v-6h32v6M44 22c0-6 8-8 6-16M58 22c0-6 8-8 6-16"/></svg>'
JUG='<svg viewBox="0 0 80 110" width="96" height="132" fill="none" stroke="#5B6470" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><rect x="26" y="4" width="28" height="14" rx="3"/><path d="M26 18c-12 8-18 18-18 34v40a10 10 0 0 0 10 10h44a10 10 0 0 0 10-10V52c0-16-6-26-18-34M8 60h64M8 78h64"/></svg>'
rowsd=[('Retiene metales pesados*',CROSS,VAR,CHECK),('Sin cargar ni almacenar',CHECK,CROSS,CHECK),('Sin gas ni esperar',CROSS,CHECK,CHECK),('Directo de tu caño',CROSS,CROSS,CHECK)]
tr=''.join(f'<div style="display:grid;grid-template-columns:360px 1fr 1fr 1fr;height:116px;align-items:center;border-top:2px solid #DCE6EE"><div style="font-size:30px;font-weight:500;padding-left:12px;line-height:1.15">{a}</div><div style="display:grid;place-items:center">{b}</div><div style="display:grid;place-items:center">{c}</div><div style="display:grid;place-items:center;height:100%;background:#EEF2FF">{d}</div></div>' for a,b,c,d in rowsd)
page('s5',f'''<div style="position:absolute;left:72px;top:70px"><span class="k">Comparar</span><h1 style="font-size:84px;font-weight:600;margin-top:14px">¿Hervir, bidón o elvo·?</h1></div>
<div style="position:absolute;left:72px;top:290px;width:1056px">
<div style="display:grid;grid-template-columns:360px 1fr 1fr 1fr;height:230px;align-items:end;padding-bottom:14px"><div></div><div style="display:grid;place-items:center;gap:6px">{POT}<h3 style="font-size:30px;font-weight:600;color:#5B6470">Hervir</h3></div><div style="display:grid;place-items:center;gap:6px">{JUG}<h3 style="font-size:30px;font-weight:600;color:#5B6470">Bidón</h3></div><div style="display:grid;place-items:center;height:100%;background:#EEF2FF;border-radius:24px 24px 0 0;gap:2px;align-content:end;padding-bottom:14px"><img src="assets/producto.webp" style="width:170px;height:170px;object-fit:cover;object-position:60% 40%;border-radius:20px"><h3 style="font-size:32px;font-weight:700;color:#3355FF">elvo· Nativo</h3></div></div>{tr}</div>
<div class="fn">*Según ficha técnica del núcleo PureCore. Los resultados dependen de la calidad del agua de entrada.</div>''',bg='#fff')
# 6 incluye
li=''.join(f'<div style="display:flex;gap:22px;align-items:center"><span style="width:46px;height:46px;border-radius:50%;background:#3355FF;display:grid;place-items:center;flex:none"><svg viewBox="0 0 24 24" width="26" height="26"><path d="M5 12.5l4.500 4.500L19 7.500" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span style="font-size:36px;font-weight:500;line-height:1.1">{x}</span></div>' for x in ['Purificador elvo· Nativo','Núcleo PureCore de 6 etapas','Adaptador universal de jebe','Derivador'])
page('s6',f'''<div style="position:absolute;left:72px;top:84px"><span class="k">En la caja</span><h1 style="font-size:82px;font-weight:600;margin-top:14px;line-height:1.04">Todo lo que<br>necesitas</h1></div>
<div style="position:absolute;left:72px;top:440px;display:flex;flex-direction:column;gap:40px">{li}</div>
<div style="position:absolute;left:72px;bottom:96px;display:flex;gap:20px"><div style="background:#fff;border-radius:24px;padding:22px 34px"><div style="font-size:22px;color:#6B7480;font-weight:500">Alto</div><div class="pj" style="font-size:50px;font-weight:700">25 cm</div></div><div style="background:#fff;border-radius:24px;padding:22px 34px"><div style="font-size:22px;color:#6B7480;font-weight:500">Ancho</div><div class="pj" style="font-size:50px;font-weight:700">6 cm</div></div></div>
<div style="position:absolute;right:-150px;bottom:0;width:720px;height:720px;-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 30%)"><img src="assets/producto.webp" style="width:100%"></div>''')
# 7 confianza
def tile(icon,t,s=''):
    return f'<div style="background:#fff;border-radius:30px;padding:34px 36px;height:250px;display:flex;flex-direction:column;justify-content:space-between"><div class="ic" style="width:68px;height:68px">{icon}</div><div><h3 style="font-size:38px;font-weight:600;line-height:1.1">{t}</h3><p style="font-size:24px;color:#6B7480;margin-top:8px">{s}</p></div></div>'
I_30='<svg viewBox="0 0 48 48"><circle cx="24" cy="24" r="17"/><path d="M24 14v10l7 4"/></svg>'
I_G='<svg viewBox="0 0 48 48"><path d="M24 4l16 6v12c0 10-6.500 18-16 22C14.500 40 8 32 8 22V10z"/><path d="M17 24l5 5 9-10"/></svg>'
I_T='<svg viewBox="0 0 48 48"><path d="M4 14h26v18H4zM30 20h9l6 7v5H30z"/><circle cx="13" cy="35" r="3.500"/><circle cx="37" cy="35" r="3.500"/></svg>'
I_P='<svg viewBox="0 0 48 48"><rect x="5" y="12" width="38" height="24" rx="4"/><circle cx="24" cy="24" r="6"/><path d="M10 18v0M38 30v0"/></svg>'
I_C='<svg viewBox="0 0 48 48"><rect x="4" y="10" width="40" height="28" rx="5"/><path d="M4 19h40M10 30h10"/></svg>'
I_R='<svg viewBox="0 0 48 48"><path d="M10 22a15 15 0 0 1 27-7M38 10v7h-7M38 26a15 15 0 0 1-27 7M10 38v-7h7"/></svg>'
page('s7',f'''<div style="position:absolute;left:72px;top:84px"><span class="k">Compra con tranquilidad</span><h1 style="font-size:80px;font-weight:600;margin-top:14px;line-height:1.04">Pruébalo sin riesgo</h1></div>
<div style="position:absolute;left:72px;top:330px;width:1056px;display:grid;grid-template-columns:1fr 1fr;gap:26px">{tile(I_30,"30 días de prueba","Pruébalo en casa")}{tile(I_G,"1 año de garantía","En tu equipo")}{tile(I_R,"Si no encaja, te devolvemos tu dinero","En tu caño")}{tile(I_T,"Envío gratis","A todo el Perú")}{tile(I_P,"Pago contra entrega","Paga al recibir")}{tile(I_C,"Hasta 6 cuotas","Sin intereses con tarjeta de crédito")}</div>''',bg='#EEF3F7')
# 8 ambiente
page('s8','''<img src="assets/ambiente.png" style="position:absolute;inset:0;width:1200px;height:1200px">
<div style="position:absolute;left:64px;top:56px;background:rgba(255,255,255,.88);border-radius:999px;padding:16px 34px;font-family:'Plus Jakarta Sans';font-weight:600;font-size:38px;letter-spacing:-.02em">Agua lista, directo de tu caño</div>''')
# 9 canales
def t(inner): return f'<div style="background:#fff;border-radius:28px;height:150px;display:flex;align-items:center;justify-content:center;gap:12px">{inner}</div>'
WA='<svg viewBox="0 0 24 24" width="64" height="64"><rect width="24" height="24" rx="6" fill="#25D366"/><path fill="#fff" d="M12 4.500a7.500 7.500 0 0 0-6.400 11.300L4.500 19.500l3.800-1A7.500 7.500 0 1 0 12 4.500zm4 10.400c-.2.5-1 .9-1.400.9-.4.1-.8.1-2.500-.5-2.100-.9-3.400-3-3.500-3.100-.1-.2-.8-1.100-.8-2.100s.5-1.500.7-1.700c.2-.2.400-.2.500-.2h.4c.1 0 .3 0 .4.4l.6 1.400c.1.100.1.300 0 .4l-.3.5c-.1.100-.2.300-.1.500.2.300.6 1 1.300 1.600.9.8 1.600 1 1.800 1.100.2.100.4.100.5-.1l.7-.8c.1-.2.3-.2.5-.1l1.400.7c.2.1.3.2.3.3.1.100.1.600-.1 1z"/></svg>'
IG='<svg viewBox="0 0 24 24" width="64" height="64"><defs><linearGradient id="g" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#FEDA75"/><stop offset=".35" stop-color="#FA7E1E"/><stop offset=".6" stop-color="#D62976"/><stop offset="1" stop-color="#4F5BD5"/></linearGradient></defs><rect width="24" height="24" rx="6" fill="url(#g)"/><rect x="5.500" y="5.500" width="13" height="13" rx="4" fill="none" stroke="#fff" stroke-width="1.600"/><circle cx="12" cy="12" r="3.100" fill="none" stroke="#fff" stroke-width="1.600"/><circle cx="16" cy="8" r="1" fill="#fff"/></svg>'
def img(f,h=62): return f'<img src="assets/{f}" style="height:{h}px;max-width:230px;object-fit:contain">'
tiles=[t('<span class="pj" style="font-weight:700;font-size:56px;letter-spacing:-.04em">elvo·<span style="font-size:30px;font-weight:500;color:#6B7480">.pe</span></span>'),t(WA+'<b class="pj" style="font-size:36px;font-weight:600">WhatsApp</b>'),t(IG+'<b class="pj" style="font-size:36px;font-weight:600">Instagram</b>'),t(img('elvo-logo-falabella.svg')),t(img('elvo-logo-sodimac.svg')),t(img('elvo-logo-plazavea.svg')),t(img('elvo-logo-promart.png',54)),t(img('elvo-logo-oechsle.svg'))]
page('s9',f'''<div style="position:absolute;left:72px;top:84px"><span class="k">Dónde comprar</span><h1 style="font-size:78px;font-weight:600;margin-top:14px;line-height:1.04">Estamos en todos<br>los canales</h1></div>
<div style="position:absolute;left:72px;top:420px;width:1056px;display:grid;grid-template-columns:repeat(2,1fr);gap:22px">{"".join(tiles)}</div>
<div class="fn" style="bottom:56px">Compra donde te quede más cómodo: en la web, por WhatsApp o en las principales tiendas del Perú.</div>''',bg='#EEF3F7')
print('ok')

# 10 ¿Sirve para tu caño?
def foto(src,pos='50% 50%'): return f'<div style="width:326px;height:360px;border-radius:26px;overflow:hidden"><img src="assets/{src}" style="width:100%;height:100%;object-fit:cover;object-position:{pos}"></div>'
chk=lambda x:f'<div style="display:flex;gap:20px;align-items:center"><span style="width:44px;height:44px;border-radius:50%;background:#3355FF;display:grid;place-items:center;flex:none"><svg viewBox="0 0 24 24" width="25" height="25"><path d="M5 12.500l4.500 4.500L19 7.500" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span style="font-size:33px;font-weight:500;line-height:1.15">{x}</span></div>'
page('s10',f'''<div style="position:absolute;left:72px;top:72px"><span class="k">Compatibilidad</span><h1 style="font-size:78px;font-weight:600;margin-top:14px;line-height:1.04">¿Sirve para tu caño?</h1></div>
<div style="position:absolute;left:72px;top:260px;display:flex;gap:26px">{foto("r_carmen.png","40% 45%")}{foto("r_maria.webp","50% 40%")}{foto("r_lucia.webp","55% 55%")}</div>
<div style="position:absolute;left:72px;top:690px;display:flex;flex-direction:column;gap:26px">{chk("Incluye adaptador universal de jebe ajustable y derivador")}{chk("Para grifos estándar")}{chk("Si no encaja, te devolvemos tu dinero")}</div>
<div style="position:absolute;left:72px;bottom:60px;background:#fff;border-radius:999px;padding:18px 34px;font-size:27px;font-weight:500">¿Dudas? Mándanos una foto de tu caño por WhatsApp</div>
''',bg='#EEF3F7')
# 11 nucleo
step=lambda n,t,s:f'<div style="display:flex;gap:26px;align-items:center"><div style="width:68px;height:68px;border-radius:50%;background:#3355FF;color:#fff;font-family:Plus Jakarta Sans;font-weight:700;font-size:32px;display:grid;place-items:center;flex:none">{n}</div><div><h3 style="font-size:38px;font-weight:600;line-height:1.1">{t}</h3><p style="font-size:26px;color:#5B6470;margin-top:6px">{s}</p></div></div>'
page('s11',f'''<div style="position:absolute;left:72px;top:72px"><span class="k">Tu núcleo PureCore</span><h1 style="font-size:78px;font-weight:600;margin-top:14px;line-height:1.04">Dura unos 18 meses</h1><p style="font-size:30px;color:#5B6470;margin-top:16px">Unos 20,000 litros de uso normal para una familia.</p></div>
<div style="position:absolute;right:30px;top:300px;width:520px;height:520px;-webkit-mask-image:radial-gradient(circle at 50% 50%,#000 55%,transparent 72%)"><img src="assets/nucleo.webp" style="width:100%"></div>
<div style="position:absolute;left:72px;top:440px;display:flex;flex-direction:column;gap:56px;width:600px">{step(1,"Hoy","Lo instalas en 5 minutos.")}{step(2,"Cerca de los 18 meses","Te avisamos por WhatsApp.")}{step(3,"Cambias el núcleo","Repuestos originales en elvo.pe.")}</div>
<div class="fn" style="bottom:56px">El tiempo depende del uso y de la calidad del agua de entrada.</div>''')
# 12 reseñas
def rv(img,txt,name,pos='50% 50%'):
    return f'<div style="background:#fff;border-radius:30px;padding:26px;display:flex;gap:26px;height:350px"><div style="width:228px;height:100%;border-radius:20px;overflow:hidden;flex:none"><img src="assets/{img}" style="width:100%;height:100%;object-fit:cover;object-position:{pos}"></div><div style="display:flex;flex-direction:column;justify-content:space-between"><div><div style="color:#F2B01E;font-size:26px;letter-spacing:2px">★★★★★</div><p style="font-family:Plus Jakarta Sans;font-weight:500;font-size:24px;line-height:1.25;margin-top:10px;letter-spacing:-.01em">“{txt}”</p></div><div style="font-size:20px;color:#5B6470"><b style="color:#050607;font-weight:600">{name}</b><br>Compra verificada</div></div></div>'
page('s12',f'''<div style="position:absolute;left:72px;top:64px"><span class="k">Reseñas</span><h1 style="font-size:70px;font-weight:600;margin-top:12px;line-height:1.04">Lo que cuentan nuestros clientes</h1><div style="margin-top:14px;font-size:27px;font-weight:500"><span style="color:#F2B01E;letter-spacing:2px">★★★★☆</span> 4,2 · 124 reseñas en Falabella</div></div>
<div style="position:absolute;left:56px;top:370px;width:1088px;display:grid;grid-template-columns:1fr 1fr;gap:22px">{rv("r_carmen.png","El agua sale cristalina, sin sabor ni olor.","Carmen S. · Trujillo","40% 45%")}{rv("r_maria.webp","El agua sale transparente, sin sabor y sin ningún residuo.","María G. · Lima","50% 40%")}{rv("r_roberto.webp","Le consulté a un amigo químico y me dijo que era muy buena compra y a buen precio.","Roberto M. · Piura")}{rv("r_lucia.webp","Lo instalé en menos de 5 minutos, funciona perfecto y tiene muy buen caudal.","Lucía P. · Ica","55% 55%")}</div>''',bg='#EEF3F7')
