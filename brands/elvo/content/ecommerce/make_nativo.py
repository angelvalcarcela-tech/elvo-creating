#!/usr/bin/env python3
"""10 láminas de ecommerce de Nativo (1500x1500). Uso: python3 make_nativo.py && node to_png.js /tmp/ecom/nativo nativo"""
import os
from PIL import Image
B='/home/user/elvo-creating/brands/elvo/'; T='/tmp/ecom/'; F=B+'content/ecommerce/fotos/'; L=B+'content/lote11/'
os.makedirs(T+'nativo',exist_ok=True)
def sq(path,out,y0=0.0):
    im=Image.open(path).convert('RGB'); W,H=im.size
    c=im if W==H else im.crop((0,int(y0*H),W,int(y0*H)+W))
    c.resize((1500,1500),Image.LANCZOS).save(T+out)
def port(path,out,box,size=(460,960)):
    im=Image.open(path).convert('RGB'); W,H=im.size
    x0,y0,x1,y1=[int(v) for v in (box[0]*W,box[1]*H,box[2]*W,box[3]*H)]
    im.crop((x0,y0,x1,y1)).resize(size,Image.LANCZOS).save(T+out)
for src,out in (('n2-hero','n01.png'),('n2-servir','n03.png'),('n2-sin-obras','n05.png'),('n2-nucleo','n06.png'),('generico','cmp-lav.png'),('n2-servir','cmp-nat.png')):
    sq(F+src+'.png',out)
port(F+'n2-conecta.png' if os.path.exists(F+'n2-conecta.png') else L+'n6-conecta_v1.png','p1.png',(0.12,0.0,0.62,1.0) if os.path.exists(F+'n2-conecta.png') else (0.0,0.10,1.0,0.78))
port(F+'n2-servir.png','p2.png',(0.10,0.0,0.62,1.0))
port(L+'n7b-palanca_v1.png','p3.png',(0.0,0.10,1.0,0.78))
Image.open(F+'despiece-b.png').convert('RGB').resize((1500,1500),Image.LANCZOS).save(T+'n02.png')
# medidas: foto oficial del producto
Image.open(B+'brand-identity/product-images/nativo-front.png').convert('RGB').resize((1500,1500),Image.LANCZOS).save(T+'n08.png')
for n,o in (('nativo-09-caja','n09.png'),('nativo-10-grifos','n10.png')):
    if os.path.exists(F+n+'.png'): sq(F+n+'.png',o)
CSS="""*{box-sizing:border-box;margin:0}body{width:1500px;height:1500px;font-family:'Inter',sans-serif;color:#010A21;position:relative;overflow:hidden;background:#dbe7f0}
.photo{position:absolute;inset:0;background-size:cover;background-position:center}
.scrim{position:absolute;left:0;right:0;bottom:0;height:40%;background:linear-gradient(to top,rgba(1,10,33,.74),rgba(1,10,33,0))}
.mark{position:absolute;left:90px;top:80px;font-weight:600;font-size:54px;color:#fff;text-shadow:0 2px 14px rgba(1,10,33,.35)}
.cap{position:absolute;left:90px;right:90px;bottom:84px;color:#fff}.cap h1{font-weight:500;font-size:92px;line-height:1.08;letter-spacing:-1.5px}.cap p{font-size:42px;margin-top:18px;color:#dfe9ff}
.steps{position:absolute;left:60px;right:60px;top:250px;display:flex;gap:30px}.step{flex:1}.step .img{height:960px;border-radius:230px 230px 30px 30px;background-size:cover;background-position:center;box-shadow:0 24px 60px rgba(1,10,33,.18)}
.step b{display:flex;margin-top:26px;gap:18px;align-items:center;font-size:38px;font-weight:500;line-height:1.1}.step b i{font-style:normal;flex:0 0 62px;height:62px;border-radius:50%;background:#3355FF;color:#fff;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:600}
.top{position:absolute;left:90px;top:90px}.top .k{font-size:34px;font-weight:600;color:#3355FF;text-transform:uppercase;letter-spacing:.5px}.top h1{font-weight:500;font-size:84px;letter-spacing:-1.2px;margin-top:14px;line-height:1.05}
.arch{position:absolute;right:90px;top:150px;width:640px;height:1200px;border-radius:320px 320px 40px 40px;background-size:cover;background-position:center;box-shadow:0 30px 80px rgba(1,10,33,.18)}
.txt{position:absolute;left:90px;top:150px;width:640px}.txt .k{font-size:34px;font-weight:600;color:#3355FF;letter-spacing:.5px;text-transform:uppercase}.txt h1{font-weight:500;font-size:80px;line-height:1.08;letter-spacing:-1.2px;margin:22px 0 40px}
.item{display:flex;gap:24px;margin:0 0 26px;align-items:center}.item b{flex:0 0 62px;height:62px;border-radius:50%;background:#3355FF;color:#fff;font-size:32px;display:flex;align-items:center;justify-content:center}.item div{font-size:38px;line-height:1.15;font-weight:500}.item small{display:block;font-size:28px;font-weight:400;color:#46566f;margin-top:4px}
.foot{position:absolute;left:90px;bottom:60px;font-weight:600;font-size:48px}.fn{position:absolute;left:90px;right:90px;bottom:50px;font-size:26px;color:#46566f}
.dim{position:absolute;background:#fff;border-radius:99px;padding:14px 30px;font-size:38px;font-weight:600;box-shadow:0 10px 30px rgba(1,10,33,.2);white-space:nowrap}.line{position:absolute;background:#fff;box-shadow:0 0 0 2px rgba(1,10,33,.25)}
.plans{position:absolute;left:60px;right:60px;top:470px;display:flex;gap:26px}.plan{flex:1;background:#fff;border-radius:36px;padding:70px 28px 80px;text-align:center;box-shadow:0 20px 50px rgba(1,10,33,.10)}.plan.m{background:#3355FF;color:#fff}.plan h2{font-size:60px;font-weight:600;letter-spacing:-1px;margin-bottom:6px}.plan p{font-size:34px;margin-bottom:30px;opacity:.85}.cores{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;min-height:430px;align-items:flex-end;align-content:flex-end}.core{width:78px;height:190px;border-radius:14px 14px 10px 10px;background:linear-gradient(#eef3f7,#c7d5e0);border:3px solid #9EBACE;position:relative}.plan.m .core{background:linear-gradient(#fff,#dfe8ff);border-color:#fff}.core:before{content:'';position:absolute;left:10px;right:10px;top:46px;height:96px;border-radius:6px;background:rgba(51,85,255,.25)}

.cmp{position:absolute;left:60px;right:60px;top:150px;display:flex;gap:30px}.col{flex:1;border-radius:36px;overflow:hidden}.col.us{background:#3355FF}.col.them{background:#fff;box-shadow:0 0 0 3px #c9d7e3 inset}.pic{height:600px;background-size:cover;background-position:center}.clab{padding:22px 30px 10px;font-size:42px;font-weight:600;color:#fff}.col.them .clab{color:#46566f;font-size:36px}.r{display:flex;align-items:center;gap:20px;padding:0 30px;height:190px;font-size:42px;font-weight:500;line-height:1.1;color:#fff}.col.them .r{color:#46566f}.r+.r{border-top:2px solid rgba(255,255,255,.28)}.col.them .r+.r{border-top-color:#dbe3ea}.ic{flex:0 0 64px;height:64px;border-radius:50%;background:rgba(255,255,255,.2);display:flex;align-items:center;justify-content:center}.col.them .ic{background:#e8eef3}.ic svg{width:34px;height:34px;stroke:#fff;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}.col.them .ic svg{stroke:#6b7b90}
.pan{position:absolute;left:0;right:0;bottom:0;height:440px;background:#010A21;color:#fff;padding:44px 80px}.pan h1{font-weight:500;font-size:70px;letter-spacing:-1px;margin-bottom:30px}.chips{display:grid;grid-template-columns:repeat(3,1fr);gap:18px 22px}.chip{display:flex;align-items:center;gap:16px;font-size:38px;font-weight:500;line-height:1.1}.chip i{font-style:normal;flex:0 0 52px;height:52px;border-radius:50%;background:#3355FF;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:700}.pan .fn2{position:absolute;left:80px;bottom:28px;font-size:27px;color:#9EBACE}

.ret{display:grid;grid-template-columns:1fr 1fr;gap:26px 34px;margin-top:6px}.rt{display:flex;gap:18px;align-items:flex-start;font-size:37px;font-weight:500;line-height:1.15}.rt i{font-style:normal;flex:0 0 54px;height:54px;border-radius:50%;background:#3355FF;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:700;margin-top:2px}
"""
def life(img,title,sub='',narrow=False):
    if narrow: return f"<html><head><meta charset='utf-8'><style>{CSS}.cap{{right:auto;width:600px}}.cap h1{{font-size:72px}}.cap p{{font-size:36px}}</style></head><body><div class='photo' style=\"background-image:url('file://{T}{img}')\"></div><div class='scrim'></div><div class='mark'>elvo·</div><div class='cap'><h1>{title}</h1><p>{sub}</p></div></body></html>"
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='photo' style=\"background-image:url('file://{T}{img}')\"></div><div class='scrim'></div><div class='mark'>elvo·</div><div class='cap'><h1>{title}</h1><p>{sub}</p></div></body></html>"
def plain(img,extra=''): return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='photo' style=\"background-image:url('file://{T}{img}')\"></div><div class='mark'>elvo·</div>{extra}</body></html>"
def toptext(img,title,sub=''): return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='photo' style=\"background-image:url('file://{T}{img}')\"></div><div style='position:absolute;left:0;right:0;top:0;height:42%;background:linear-gradient(to bottom,rgba(255,255,255,.85),rgba(255,255,255,0))'></div><div style='position:absolute;left:90px;right:90px;top:80px;color:#010A21'><h1 style='font-weight:500;font-size:88px;letter-spacing:-1.5px'>{title}</h1><p style='font-size:40px;margin-top:14px;color:#2b3b55'>{sub}</p></div><div class='mark' style='top:auto;bottom:70px'>elvo·</div></body></html>"
H={}
H['nativo-01-principal']=plain('n01.png')
H['nativo-02-que-elimina']=f"<html><head><meta charset='utf-8'><style>{CSS}body{{background:#fff}}</style></head><body><div class='photo' style=\"background-image:url('file://{T}n02.png');background-size:100% 100%\"></div></body></html>"
H['nativo-03-agua-pura']=life('n03.png','Agua pura<br>desde tu caño.')
steps=''.join(f"<div class='step'><div class='img' style=\"background-image:url('file://{T}{p}')\"></div><b><i>{n}</i>{t}</b></div>" for n,p,t in ((1,'p1.png','Conectas el derivador'),(2,'p2.png','Dejas correr el agua 5 min'),(3,'p3.png','Mueves la palanca y sirves')))
H['nativo-04-asi-se-instala']=f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='top'><div class='k'>Así se instala</div><h1>Tú, en 5 minutos</h1></div><div class='steps'>{steps}</div><div class='foot'>elvo·</div></body></html>"
H['nativo-05-sin-electricidad']=life('n05.png','Sin electricidad.<br>Sin obras.','Sin gasfitero.',narrow=True).replace('.cap h1{font-size:72px}','.cap h1{font-size:62px}').replace('width:600px','width:520px')
H['nativo-06-cambio-de-nucleo']=life('n06.png','El núcleo<br>lo cambias tú.','Cada 18 meses.',narrow=True)
ic={'e':"<svg viewBox='0 0 24 24'><path d='M12 2.7l5.7 5.7a8 8 0 1 1-11.3 0z'/></svg>",'d':"<svg viewBox='0 0 24 24'><circle cx='12' cy='12' r='10'/><polyline points='12 6 12 12 16 14'/></svg>",'u':"<svg viewBox='0 0 24 24'><path d='M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z'/></svg>",'l':"<svg viewBox='0 0 24 24'><path d='M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z'/><path d='M9 22V12h6v10'/></svg>",'m':"<svg viewBox='0 0 24 24'><path d='M12 3c4 4 6 7 6 10a6 6 0 0 1-12 0c0-3 2-6 6-10z'/><path d='M9 14a3 3 0 0 0 3 3'/></svg>",'k':"<svg viewBox='0 0 24 24'><path d='M20 12v8H4v-8'/><path d='M2 7h20v5H2z'/><path d='M12 22V7'/><path d='M12 7H7.5a2.5 2.5 0 1 1 0-5C11 2 12 7 12 7z'/><path d='M12 7h4.5a2.5 2.5 0 1 0 0-5C13 2 12 7 12 7z'/></svg>",'c':"<svg viewBox='0 0 24 24'><rect x='1' y='3' width='15' height='13'/><path d='M16 8h4l3 3v5h-7z'/><circle cx='5.5' cy='18.5' r='2.5'/><circle cx='18.5' cy='18.5' r='2.5'/></svg>"}
rows=[('d','Núcleo de 18 meses','Cartucho de 6 a 12 meses*'),('u','Etapa antimetales: plomo y metales pesados**','No siempre incluida'),('e','6 etapas de filtración','Etapas según el modelo'),('l','Pico propio sobre la mesada','Directo a la salida del grifo'),('m','Conserva minerales · pH ~8,5','Según el modelo'),('k','Derivador y adaptador de jebe incluidos','Según el modelo'),('c','Envío gratis · pago contra entrega · hasta 6 cuotas','Según la tienda')]
us=''.join(f"<div class='r'><div class='ic'>{ic[k]}</div>{a}</div>" for k,a,b in rows)
th=''.join(f"<div class='r'><div class='ic'>{ic[k]}</div>{b}</div>" for k,a,b in rows)
EXTRA=".cmp{top:130px}.pic{height:340px!important;background-position:center 18%!important;background-size:cover!important}.r{height:112px!important;font-size:31px!important;padding:0 24px!important;gap:16px!important}.ic{flex:0 0 52px!important;height:52px!important}.ic svg{width:28px!important;height:28px!important}.clab{font-size:38px!important;padding:16px 24px 8px!important}"
H['nativo-07-comparacion']=f"<html><head><meta charset='utf-8'><style>{CSS}{EXTRA}</style></head><body><div class='top' style='top:36px'><h1 style='font-size:58px;margin:0'>Por qué elegir Nativo</h1></div><div class='cmp'><div class='col us'><div class='pic' style=\"background-image:url('file://{T}cmp-nat.png')\"></div><div class='clab'>elvo· Nativo</div>{us}</div><div class='col them'><div class='pic' style=\"background-image:url('file://{T}cmp-lav.png')\"></div><div class='clab'>Otro purificador de caño (genérico)</div>{th}</div></div><div style='position:absolute;left:60px;right:60px;bottom:14px;font-size:21px;line-height:1.25;color:#46566f'>*Según fichas de mini filtros directos al grifo vendidos en Perú (nov-2026). **Según la ficha técnica del núcleo PureCore. Comparación con purificadores genéricos del mismo tipo; revisa la ficha de cada modelo.</div></body></html>"
dims="<div class='line' style='left:1100px;top:125px;width:6px;height:1212px;background:#010A21;box-shadow:none'></div><div class='dim' style='left:1140px;top:690px'>30 cm</div><div class='line' style='left:588px;top:1385px;width:474px;height:6px;background:#010A21;box-shadow:none'></div><div class='dim' style='left:640px;top:1405px;padding:10px 26px;font-size:34px'>16 × 16 cm</div>"
H['nativo-08-medidas']=plain('n08.png',dims).replace('</style>','.mark{color:#010A21!important;text-shadow:none!important}</style>')
H['nativo-09-en-la-caja']=toptext('n09.png','En la caja.','Purificador con núcleo · Derivador · Manguera · Adaptador · Llave plástica · Manual')
H['nativo-10-grifos']=f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='top'><div class='k'>Compatibilidad</div><h1>Se adapta a tu grifo</h1></div><div class='photo' style=\"background-image:url('file://{T}n10.png');top:300px;bottom:230px;left:60px;right:60px;border-radius:36px\"></div><div style='position:absolute;left:90px;right:90px;bottom:70px;font-size:42px;font-weight:500'>Incluye derivador y adaptador universal de jebe.<br><span style='color:#46566f;font-size:36px;font-weight:400'>Compatible con la mayoría de grifos estándar.</span></div></body></html>"

def full(name):
    Image.open(F+name+'.png').convert('RGB').resize((1500,1500),Image.LANCZOS).save(T+name+'.png')
    return f"<html><head><meta charset='utf-8'><style>{CSS}body{{background:#fff}}</style></head><body><div class='photo' style=\"background-image:url('file://{T}{name}.png');background-size:100% 100%\"></div></body></html>"
def full2(name):
    Image.open(F+name+'.png').convert('RGB').resize((1500,1500),Image.LANCZOS).save(T+name+'.png')
    return f"<html><head><meta charset='utf-8'><style>{CSS}body{{background:#fff}}</style></head><body><div class='photo' style=\"background-image:url('file://{T}{name}.png');background-size:100% 100%\"></div></body></html>"
H['nativo-04-asi-se-instala']=full2('instala6-b')
H['nativo-09-en-la-caja']=toptext('n09.png','En la caja.','Purificador con núcleo · Derivador · Manguera · Adaptador · Llave plástica · Manual')
H['nativo-10-grifos']=f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='top'><div class='k'>Compatibilidad</div><h1>Se adapta a tu grifo</h1></div><div class='photo' style=\"background-image:url('file://{T}n10.png');top:300px;bottom:230px;left:60px;right:60px;border-radius:36px\"></div><div style='position:absolute;left:90px;right:90px;bottom:70px;font-size:42px;font-weight:500'>Incluye derivador y adaptador universal de jebe.<br><span style='color:#46566f;font-size:36px;font-weight:400'>Compatible con la mayoría de grifos estándar.</span></div></body></html>"

def full(name):
    Image.open(F+name+'.png').convert('RGB').resize((1500,1500),Image.LANCZOS).save(T+name+'.png')
    return f"<html><head><meta charset='utf-8'><style>{CSS}body{{background:#fff}}</style></head><body><div class='photo' style=\"background-image:url('file://{T}{name}.png');background-size:100% 100%\"></div></body></html>"
H['nativo-09-en-la-caja']=toptext('n09.png','En la caja.','Purificador con núcleo · Derivador · Manguera · Adaptador · Llave plástica · Manual')
H['nativo-10-grifos']=f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='top'><div class='k'>Compatibilidad</div><h1>Se adapta a tu grifo</h1></div><div class='photo' style=\"background-image:url('file://{T}n10.png');top:300px;bottom:230px;left:60px;right:60px;border-radius:36px\"></div><div style='position:absolute;left:90px;right:90px;bottom:70px;font-size:42px;font-weight:500'>Incluye derivador y adaptador universal de jebe.<br><span style='color:#46566f;font-size:36px;font-weight:400'>Compatible con la mayoría de grifos estándar.</span></div></body></html>"

def full(name):
    Image.open(F+name+'.png').convert('RGB').resize((1500,1500),Image.LANCZOS).save(T+name+'.png')
    return f"<html><head><meta charset='utf-8'><style>{CSS}body{{background:#fff}}</style></head><body><div class='photo' style=\"background-image:url('file://{T}{name}.png');background-size:100% 100%\"></div></body></html>"
H['nativo-09-en-la-caja']=full('real2-caja')
H['nativo-10-grifos']=full('real2-grifos')
DK="<style>.mark{color:#010A21!important;text-shadow:none!important}</style>"
for k in ('nativo-01-principal','nativo-05-sin-electricidad'):
    H[k]=H[k].replace('</head>',DK+'</head>')
os.makedirs('/tmp/ecom/nativo',exist_ok=True)
for f in os.listdir('/tmp/ecom/nativo'): os.remove('/tmp/ecom/nativo/'+f)
for k,h in H.items(): open(f'/tmp/ecom/nativo/{k}.html','w').write(h)
print(len(H))
