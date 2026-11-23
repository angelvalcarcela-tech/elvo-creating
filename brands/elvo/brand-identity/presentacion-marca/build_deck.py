import os,json
LP=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'assets/logo-path.json')))
DP=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'assets/drop-path.json')))
D=os.path.dirname(os.path.abspath(__file__))
DROP='<path d="M0,-10 C5,-3 8,1 8,5 a8,8 0 1 1 -16,0 C-8,1 -5,-3 0,-10z" fill="currentColor"/>'
def logo(size=120,color='#5891CB'):
    w=size*2.7
    return f'<svg viewBox="0 0 {LP["w"]} {LP["h"]}" style="width:{w}px;height:{w*LP["h"]/LP["w"]}px;color:{color};display:inline-block;vertical-align:middle"><path d="{LP["d"]}" fill="currentColor" fill-rule="evenodd"/></svg>'
def drop(size=80,color='#5891CB'):
    return f'<svg viewBox="0 0 {DP["w"]} {DP["h"]}" style="width:{size}px;height:{size*DP["h"]/DP["w"]}px;color:{color}"><path d="{DP["d"]}" fill="currentColor" fill-rule="evenodd"/></svg>'
def hdr(n,t,dark=False):
    return f'<div class="hd {"dk" if dark else ""}"><span>{n}</span>{logo(34,"#fff" if dark else "#5891CB")}<span>{t}</span></div>'
CSS='''
@font-face{font-family:Inter;font-weight:400;src:url(fonts/inter-latin-400-normal.woff2)}
@font-face{font-family:Inter;font-weight:500;src:url(fonts/inter-latin-500-normal.woff2)}
@font-face{font-family:Inter;font-weight:600;src:url(fonts/inter-latin-600-normal.woff2)}
@font-face{font-family:Inter;font-weight:700;src:url(fonts/inter-latin-700-normal.woff2)}
@font-face{font-family:Inter;font-weight:800;src:url(fonts/inter-latin-800-normal.woff2)}
@font-face{font-family:Nunito;font-weight:700;src:url(fonts/nunito-latin-700-normal.woff2)}
@font-face{font-family:Nunito;font-weight:800;src:url(fonts/nunito-latin-800-normal.woff2)}
@page{size:1920px 1080px;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,sans-serif;color:#010A21;background:#fff}
.pg{width:1920px;height:1080px;position:relative;overflow:hidden;page-break-after:always;background:#FAFAFA}
.logo{text-transform:none;display:inline-flex;align-items:flex-start;font-family:Nunito;font-weight:700;letter-spacing:-.04em;line-height:1}
.hd{position:absolute;left:90px;right:90px;top:46px;display:flex;justify-content:space-between;align-items:center;font-size:15px;letter-spacing:.18em;text-transform:uppercase;color:#5E6B80;font-weight:600}
.hd.dk{color:#9EBACE}
h1{font-size:92px;line-height:1.02;letter-spacing:-.035em;font-weight:700}
h2{font-size:64px;line-height:1.05;letter-spacing:-.03em;font-weight:700}
h3{font-size:22px;letter-spacing:.14em;text-transform:uppercase;font-weight:700;color:#3355FF;margin-bottom:14px}
p{font-size:27px;line-height:1.5;color:#2A3750}
.sm{font-size:21px;line-height:1.5}
.abs{position:absolute}
.pill{display:inline-block;border:2px solid currentColor;border-radius:40px;padding:10px 26px;font-size:20px;font-weight:600}
.card{background:#fff;border-radius:28px;box-shadow:0 2px 0 #E4EAF1}
.img{background-size:cover;background-position:center;position:absolute}
.rule{height:2px;background:#C8D3E0}
ul{list-style:none}li{font-size:25px;line-height:1.45;color:#2A3750;padding-left:30px;position:relative;margin-bottom:10px}
li:before{content:"";position:absolute;left:0;top:14px;width:10px;height:10px;border-radius:50%;background:#3355FF}
'''
pages=[]
def P(html,style=''): pages.append(f'<section class="pg" style="{style}">{html}</section>')
def IMG(src,x,y,w,h,r=0,pos='center',fit='cover'):
    return f'<div class="img" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{r}px;background-image:url({src});background-size:{fit};background-position:{pos};background-repeat:no-repeat"></div>'

# 1 cover
P(IMG('mock/cover-wall.jpg',0,0,1920,1080)+'<div class="abs" style="left:0;right:0;bottom:0;height:300px;background:linear-gradient(transparent,rgba(1,10,33,.82))"></div>'
  +f'<div class="abs" style="left:90px;bottom:70px;color:#fff">{logo(130,"#fff")}<div style="font-size:34px;margin-top:20px;font-weight:500">Identidad de marca y sistema visual</div></div>'
  +'<div class="abs" style="right:90px;bottom:80px;color:#9EBACE;font-size:20px;letter-spacing:.2em;font-weight:600">AGUA PURA. SIMPLIFICADA. &nbsp; // 2026</div>')

# 2 concept
P(hdr('01','Concepto de marca')+f'''
<div class="abs" style="left:90px;top:150px;width:1000px"><h1>Concepto<br>de marca</h1></div>
<div class="abs" style="left:90px;top:420px;width:860px"><p>elvo es una marca de purificadores de agua pensada para la casa moderna. Reúne tecnología de filtración, diseño cuidado y una simplicidad cotidiana para cambiar cómo se vive el agua en casa.</p><p style="margin-top:26px">En vez de tratar la purificación como un aparato puramente funcional, elvo la ve como parte esencial de la vida en casa: simple de usar, agradable de ver y tranquila de tener.</p></div>
<div class="abs card" style="left:1060px;top:150px;width:770px;height:780px;padding:56px">
<h3>Idea de marca</h3><div style="font-size:40px;line-height:1.25;font-weight:600;letter-spacing:-.02em">Mejor agua no debería exigir tecnología complicada ni aparatos feos.<br><span style="color:#3355FF">elvo la vuelve simple.</span></div>
<div class="rule" style="margin:44px 0 36px"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:36px"><div><h3>Esencia</h3><p class="sm">Agua · Simple · Cuidada</p></div><div><h3>Promesa</h3><p class="sm">Una experiencia de agua más tranquila, pensada para la vida diaria.</p></div><div style="grid-column:1/3"><h3>Principio rector</h3><p class="sm">Purificación × Diseño × Simplicidad</p></div></div>
</div>''')

# 3 problem
P(hdr('02','El problema de marca')+f'''
<div class="abs" style="left:90px;top:150px;width:1100px"><h1>El problema</h1></div>
<div class="abs" style="left:90px;top:300px;width:1050px"><p>Muchos purificadores priorizan la función sobre la experiencia: formas voluminosas, lenguaje técnico y mensajes que meten miedo. Resultado: el agua se vive como un trámite, no como un cuidado.</p></div>
<div class="abs" style="left:90px;top:520px;width:850px"><h3>El desafío</h3><ul><li>Lenguaje técnico que intimida</li><li>Aparatos que se esconden bajo el lavadero</li><li>Mensajes basados en el miedo y en la alarma</li><li>Poca conexión emocional con quien lo usa</li><li>Identidades genéricas o puramente funcionales</li></ul></div>
<div class="abs" style="left:1040px;top:520px;width:790px"><h3>La oportunidad</h3><p class="sm" style="font-size:25px">Hacer que purificar el agua se sienta intuitivo, cuidado y cercano a los espacios donde la gente vive.</p><h3 style="margin-top:36px">Posicionamiento</h3><p class="sm" style="font-size:25px">elvo es una marca de purificación para el hogar: rendimiento real, diseño limpio y una simplicidad que se nota desde el primer vaso.</p></div>
<div class="abs" style="left:1250px;top:140px;width:580px;height:300px;background:#3355FF;border-radius:28px;color:#fff;padding:44px"><h3 style="color:#C4D6E4">El giro</h3><div style="font-size:42px;font-weight:700;line-height:1.15;letter-spacing:-.02em">De aparato escondido a esencial de casa.</div></div>''')

# 4 primary logo
P('<div class="abs" style="inset:0;background:radial-gradient(900px 600px at 15% 20%,#C9D9FF 0,transparent 60%),radial-gradient(800px 600px at 90% 95%,#DCE6EE 0,transparent 60%),#FAFAFA"></div>'
  +hdr('03','Logotipo principal')+f'<div class="abs" style="left:0;right:0;top:260px;text-align:center">{logo(330,"#5891CB")}</div><div class="abs" style="left:240px;right:240px;top:760px;display:flex;gap:30px"><div style="flex:1;height:200px;border-radius:24px;background:#fff;border:2px solid #E1E7EE;display:flex;align-items:center;justify-content:center">{logo(70,"#010A21")}</div><div style="flex:1;height:200px;border-radius:24px;background:#010A21;display:flex;align-items:center;justify-content:center">{logo(70,"#fff")}</div><div style="flex:1;height:200px;border-radius:24px;background:#3355FF;display:flex;align-items:center;justify-content:center">{logo(70,"#fff")}</div></div>')

# 5 construction
P(hdr('04','Construcción y símbolo')+f'''
<div class="abs card" style="left:90px;top:130px;width:1040px;height:830px;overflow:hidden">
<div class="abs" style="left:0;right:0;top:130px;height:2px;background:#C8D3E0"></div><div class="abs" style="left:0;right:0;top:300px;height:2px;background:#C8D3E0"></div><div class="abs" style="left:0;right:0;top:420px;height:2px;background:#3355FF"></div><div class="abs" style="left:0;right:0;top:610px;height:2px;background:#C8D3E0"></div><div class="abs" style="left:0;right:0;top:700px;height:2px;background:#C8D3E0"></div>
<div class="abs" style="left:100px;top:300px">{logo(300,"#5891CB")}</div>
<div class="abs" style="left:30px;top:116px;font-size:15px;color:#5E6B80;letter-spacing:.12em">ASCENDENTE</div><div class="abs" style="left:30px;top:406px;font-size:15px;color:#3355FF;letter-spacing:.12em">ALTURA X</div><div class="abs" style="left:30px;top:596px;font-size:15px;color:#5E6B80;letter-spacing:.12em">BASE</div></div>
<div class="abs card" style="left:1170px;top:130px;width:660px;height:830px;padding:50px;background:#E9EEF4">
<div style="display:flex;gap:28px;align-items:center;margin-bottom:60px">{drop(60,"#5891CB")}<div><h3 style="margin:0 0 6px">01 / La gota</h3><p class="sm">Pureza, hidratación y esencia natural del agua.</p></div></div>
<div style="display:flex;gap:28px;align-items:center;margin-bottom:60px"><div style="width:70px;height:70px;border:16px solid #5891CB;border-radius:50%;flex:none"></div><div><h3 style="margin:0 0 6px">02 / La “o”</h3><p class="sm">El núcleo: el corazón del filtro, redondo y sin aristas.</p></div></div>
<div style="display:flex;gap:28px;align-items:center"><div style="width:70px;height:70px;flex:none;display:flex;align-items:center;justify-content:center"><div style="width:16px;height:34px;border-radius:40px 40px 40px 40px;background:#5891CB;transform:rotate(12deg)"></div></div><div><h3 style="margin:0 0 6px">03 / El brillo</h3><p class="sm">La rayita interior de la gota: el reflejo de luz del agua limpia.</p></div></div></div>''')

# 6 palette
sw=[('Azul vivo','#3355FF','51 85 255'),('Azul logo','#5891CB','88 145 203'),('Acero','#9EBACE','158 186 206'),('Niebla','#C4D6E4','196 214 228'),('Hielo','#DCE6EE','220 230 238')]
sws=''.join(f'<div style="flex:1;background:{c};padding:26px;color:{"#fff" if i<3 else "#010A21"};display:flex;flex-direction:column;justify-content:flex-end;font-size:19px;line-height:1.5"><b style="font-size:24px">{n}</b>HEX {c.upper()}<br>RGB {r}</div>' for i,(n,c,r) in enumerate(sw))
P(hdr('05','Paleta de color')+f'''
<div class="abs" style="left:90px;top:130px;width:620px"><h2>Paleta</h2><p class="sm" style="margin-top:20px">Un azul vivo para la energía del agua, azules acero para la calma, y neutros limpios para dar aire. El marino profundo ancla los textos y los fondos oscuros.</p></div>
<div class="abs" style="left:90px;top:400px;right:90px;height:300px;display:flex;border-radius:28px;overflow:hidden">{sws}</div>
<div class="abs" style="left:90px;top:720px;right:90px;height:240px;display:flex;border-radius:28px;overflow:hidden">
<div style="flex:1.4;background:#FAFAFA;border:2px solid #E1E7EE;padding:26px;font-size:19px;line-height:1.5"><b style="font-size:24px">Blanco</b>HEX #FAFAFA<br>RGB 250 250 250</div><div style="flex:.7;background:#D9D9D9"></div><div style="flex:.7;background:#B4B4B4"></div><div style="flex:.7;background:#8A8A8A"></div><div style="flex:.7;background:#5E5E5E"></div>
<div style="flex:1.4;background:#010A21;padding:26px;color:#fff;font-size:19px;line-height:1.5"><b style="font-size:24px">Marino</b>HEX #010A21<br>RGB 1 10 33</div></div>''')

# 7 type
P('<div class="abs" style="inset:0;background:#010A21"></div>'+hdr('06','Tipografía',True)+f'''
<div class="abs" style="left:90px;top:130px;color:#fff;width:880px"><div style="font-size:300px;font-weight:700;letter-spacing:-.06em;line-height:1">Aa</div><h3 style="color:#9EBACE">01 / Tipografía principal</h3><div style="font-size:64px;font-weight:700;color:#fff">Inter</div><p style="color:#9EBACE;font-size:23px;margin-top:10px">Para titulares, textos y datos. Clara, neutra y legible en pantalla, empaque y catálogo. Pesos: Regular · Medium · Semibold · Bold.</p><p style="color:#fff;font-size:30px;margin-top:30px;letter-spacing:.04em">Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj Kk Ll Mm Nn Oo Pp Qq Rr Ss Tt Uu Vv Ww Xx Yy Zz</p></div>
<div class="abs" style="left:1010px;top:130px;width:820px;color:#fff"><div style="height:300px;display:flex;align-items:center">{logo(150,"#fff")}</div><h3 style="color:#9EBACE;margin-top:60px">02 / Logotipo</h3><div style="font-size:64px;font-weight:700;color:#fff">Dibujado a medida</div><p style="color:#9EBACE;font-size:23px;margin-top:10px">Letras finas y redondeadas, con la gota y su brillo interior. El logotipo es un dibujo, no una fuente: no se reescribe ni se reemplaza por texto.</p></div>''')

# 8 voice
P(hdr('07','Voz y mensajes')+f'''
<div class="abs" style="left:90px;top:140px;width:1000px"><h1>Agua pura.<br><span style="color:#3355FF">Simplificada.</span></h1></div>
<div class="abs" style="left:90px;top:470px;display:flex;gap:18px"><span class="pill" style="color:#3355FF">Núcleo de 18 meses</span><span class="pill" style="color:#3355FF">Instalación en 5 minutos</span><span class="pill" style="color:#3355FF">Para todo caño</span></div>
<div class="abs" style="left:90px;top:600px;width:820px"><h3>Cómo hablamos</h3><ul><li>Observación, no alarma: nombramos el problema y nos quedamos en calma.</li><li>La cifra antes que el superlativo.</li><li>Transparencia: decimos cuánto dura el núcleo y cuándo cambiarlo.</li></ul></div>
<div class="abs" style="left:1000px;top:600px;width:830px"><h3>Cómo no hablamos</h3><ul><li>Sin miedo, sin agua sucia como amenaza.</li><li>Sin urgencia inventada ni descuentos gritados.</li><li>Sin comparar con marcas por su nombre.</li></ul></div>
<div class="abs card" style="left:1130px;top:140px;width:700px;height:400px;background:#3355FF;color:#fff;padding:50px"><h3 style="color:#C4D6E4">Línea de casa</h3><div style="font-size:46px;line-height:1.2;font-weight:700;letter-spacing:-.02em">El agua es el primer ingrediente de tu día.</div><p class="sm" style="color:#DCE6EE;margin-top:24px">Con elvo, ese primer vaso se vuelve simple.</p></div>''')

# 9 photography
P(hdr('08','Dirección fotográfica')+f'''
<div class="abs" style="left:90px;top:130px;width:540px"><h2>Fotografía</h2><p class="sm" style="margin-top:20px">Luz natural de mañana, cocinas reales y personas tranquilas. El producto vive a la vista, sobre la mesada, nunca escondido. El texto acompaña; la imagen manda.</p><ul style="margin-top:30px"><li>Gente real, gestos simples</li><li>Mesadas claras, luz suave</li><li>El agua siempre cayendo del grifo</li></ul></div>
{IMG('img/crop-a1.jpg',680,130,560,830,28,'center top')}{IMG('img/crop-k.jpg',1270,130,560,400,28)}{IMG('img/crop-a2.jpg',1270,560,560,400,28,'left center')}''')

# 10 products
def prod(src,x,name,desc,fit='contain'):
    return f'<div class="abs card" style="left:{x}px;top:200px;width:540px;height:640px;overflow:hidden">{IMG(src,0,0,540,470,0,"center",fit)}<div style="position:absolute;left:30px;top:490px;right:30px"><div style="font-size:34px;font-weight:700;letter-spacing:-.02em">{logo(36,"#010A21") if False else ""}{name}</div><p class="sm" style="margin-top:12px;font-size:20px">{desc}</p></div></div>'
P(hdr('09','Línea de productos')+'<div class="abs" style="left:90px;top:110px"><h2>Tres formas de purificar</h2></div>'
  +prod('img/alivio16.jpg',90,'elvo Alivio','Bidón purificador de 16 y 22 L. Sin luz, sin instalación.')
  +prod('img/nativo.jpg',690,'elvo Nativo','Purificador de caño con núcleo de 18 meses.')
  +prod('img/cero.jpg',1290,'elvo Cero','Ósmosis inversa, agua fría y caliente.'))

# 11 system
P('<div class="abs" style="inset:0;background:#010A21"></div>'+hdr('10','Sistema: caño → núcleo → vaso',True)+f'''
<div class="abs" style="left:90px;top:130px;width:700px;color:#fff"><h2>Caño → Núcleo → Vaso</h2><p style="color:#9EBACE;margin-top:24px;font-size:24px">Todo el sistema se explica en tres pasos. El agua entra por el caño, pasa por el núcleo y llega al vaso. Esa secuencia es el hilo visual de toda la marca.</p>
<div style="display:flex;gap:14px;margin-top:50px;align-items:center;font-size:22px;font-weight:600;color:#fff"><span class="pill" style="color:#9EBACE">Caño</span>→<span class="pill" style="color:#6F8BFF">Núcleo</span>→<span class="pill" style="color:#fff">Vaso</span></div></div>
{IMG('img/nucleo.jpg',900,90,900,900,28,'center','cover')}''')

# 12 social (perfil actual @elvo_filtros)
P(hdr('11','Redes sociales')+f'''
<div class="abs" style="left:90px;top:130px;width:600px"><h2>Instagram</h2><p style="color:#5891CB;font-weight:700;font-size:30px;margin-top:10px">@elvo_filtros</p><p class="sm" style="margin-top:24px">El perfil cuenta un solo mundo: casas luminosas, luz fría de ventana, agua que se sirve y el producto a la vista. Cada fila presenta una línea, y el texto vive en el pie de foto, no en la imagen.</p><ul style="margin-top:30px"><li>Bio: Agua pura. Simplificada. · Caño → Núcleo → Vaso</li><li>Destacados: Nativo, Alivio, Cero, Reseñas, Dónde</li><li>Un producto por fila, nunca dos pegados</li></ul></div>
<div class="abs card" style="left:760px;top:110px;width:530px;height:880px;overflow:hidden;padding:0">{IMG('img/ig-a.jpg',0,0,530,880,0,'center top','cover')}</div>
<div class="abs card" style="left:1320px;top:110px;width:530px;height:880px;overflow:hidden;padding:0">{IMG('img/ig-b.jpg',0,0,530,880,0,'center top','cover')}</div>''')

# 13 web
P(hdr('12','Catálogo y tienda en línea')+f'''
<div class="abs" style="left:90px;top:130px;width:560px"><h2>Mismo lenguaje, en cada pantalla</h2><p class="sm" style="margin-top:24px">Cada publicación sigue el mismo sistema: un hero con una sola idea, una lámina por pregunta del cliente y fotos de cocina reales. Así la tienda, el catálogo y las redes se sienten una sola marca.</p></div>
<div class="abs" style="left:700px;top:130px;display:grid;grid-template-columns:repeat(3,1fr);gap:20px;width:1130px">{''.join(f'<div style="aspect-ratio:1;border-radius:20px;background:url({s}) center/cover"></div>' for s in ['img/hero-nativo.jpg','img/nucleo.jpg','img/giro.jpg','img/nativo-18m.jpg','img/nativo-contaminantes.jpg','img/nativo-20000.jpg'])}</div>''')

# 14 packaging
P(IMG('mock/packaging.jpg',0,0,1920,1080)+hdr('13','Empaque',True).replace('class="hd dk"','class="hd dk" style="color:#fff"'))
# 15 stationery
P(IMG('mock/cards.jpg',0,0,960,1080)+IMG('mock/tote.jpg',960,0,960,1080)+hdr('14','Papelería y merchandising',True).replace('class="hd dk"','class="hd dk" style="color:#fff"'))
# 16 applications
P('<div class="abs" style="inset:0;background:#010A21"></div>'+IMG('mock/billboard.jpg',0,0,1100,733)+IMG('mock/van.jpg',820,347,1100,733)+'<div class="abs" style="right:90px;top:200px;width:560px;color:#fff"><h2>En la calle,<br>en la casa.</h2><p style="color:#9EBACE;margin-top:20px;font-size:23px">La misma calma y la misma claridad, desde un cartel hasta la puerta de tu casa.</p></div>'+hdr('15','Aplicaciones',True).replace('class="hd dk"','class="hd dk" style="color:#fff"'))
# 17 close
P('<div class="abs" style="inset:0;background:#3355FF"></div><div class="abs" style="left:-200px;top:200px;width:1100px;height:1100px;border-radius:50%;background:radial-gradient(circle,#fff 0,#C9D9FF 55%,transparent 72%);opacity:.9"></div>'
  +f'<div class="abs" style="left:0;right:0;top:340px;text-align:center">{logo(260,"#010A21")}<div style="font-size:40px;margin-top:40px;color:#fff;font-weight:600;letter-spacing:-.01em">Agua pura. Simplificada.</div><div style="font-size:22px;margin-top:30px;color:#DCE6EE;letter-spacing:.2em;font-weight:600">ELVO.PE &nbsp;//&nbsp; 2026</div></div>')

html='<!doctype html><meta charset=utf-8><style>'+CSS+'</style>'+''.join(pages)
open(os.path.join(D,'deck.html'),'w').write(html)
print(len(pages),'páginas')
