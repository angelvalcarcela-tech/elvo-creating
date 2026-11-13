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
sq(L+'n1c-hook_v1.png','n01.png',0.20)
port(L+'n3b-etapas_v1.png','n02.png',(0.05,0.18,0.95,0.18+0.90*1.0*1152/2048*0+0.62),(640,1200))
sq(L+'n4-agua_v1.png','n03.png',0.18)
port(L+'n6-conecta_v1.png','p1.png',(0.0,0.10,1.0,0.78))
port(L+'n3b-etapas_v1.png','p2.png',(0.05,0.12,0.95,0.80))
port(L+'n7b-palanca_v1.png','p3.png',(0.0,0.10,1.0,0.78))
sq(L+'n9b-sin-obras_v1.png','n05.png',0.20)
sq(L+'n8-nucleo_v1.png','n06.png',0.15)
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
"""
def life(img,title,sub=''): return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='photo' style=\"background-image:url('file://{T}{img}')\"></div><div class='scrim'></div><div class='mark'>elvo·</div><div class='cap'><h1>{title}</h1><p>{sub}</p></div></body></html>"
def plain(img,extra=''): return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='photo' style=\"background-image:url('file://{T}{img}')\"></div><div class='mark'>elvo·</div>{extra}</body></html>"
def toptext(img,title,sub=''): return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='photo' style=\"background-image:url('file://{T}{img}')\"></div><div style='position:absolute;left:0;right:0;top:0;height:42%;background:linear-gradient(to bottom,rgba(255,255,255,.85),rgba(255,255,255,0))'></div><div style='position:absolute;left:90px;right:90px;top:80px;color:#010A21'><h1 style='font-weight:500;font-size:88px;letter-spacing:-1.5px'>{title}</h1><p style='font-size:40px;margin-top:14px;color:#2b3b55'>{sub}</p></div><div class='mark' style='top:auto;bottom:70px'>elvo·</div></body></html>"
H={}
H['nativo-01-principal']=plain('n01.png')
stages=[('Carbón activado','cloro, olores y mal sabor'),('Etapa antimetales','retiene metales pesados*'),('Plata coloidal','inhibe microorganismos'),('Nanotecnología','microplásticos y partículas finas'),('Aluminosilicato','mejora la claridad del agua'),('Plata iónica','agua más pura por más tiempo')]
its=''.join(f"<div class='item'><b>{i+1}</b><div>{a}<small>{b}</small></div></div>" for i,(a,b) in enumerate(stages))
H['nativo-02-seis-etapas']=f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='txt'><div class='k'>Antimetales</div><h1>6 etapas<br>de filtración</h1>{its}</div><div class='arch' style=\"background-image:url('file://{T}n02.png')\"></div><div class='fn'>*Según la ficha técnica del núcleo PureCore. Pensado para agua de red potable.</div></body></html>"
H['nativo-03-agua-con-minerales']=life('n03.png','Agua más rica,<br>con sus minerales.')
steps=''.join(f"<div class='step'><div class='img' style=\"background-image:url('file://{T}{p}')\"></div><b><i>{n}</i>{t}</b></div>" for n,p,t in ((1,'p1.png','Conectas el derivador'),(2,'p2.png','Dejas correr el agua 5 min'),(3,'p3.png','Mueves la palanca y sirves')))
H['nativo-04-asi-se-instala']=f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='top'><div class='k'>Así se instala</div><h1>Tú, en 5 minutos</h1></div><div class='steps'>{steps}</div><div class='foot'>elvo·</div></body></html>"
H['nativo-05-sin-electricidad']=life('n05.png','Sin electricidad.<br>Sin obras.','Sin gasfitero.')
H['nativo-06-cambio-de-nucleo']=life('n06.png','El núcleo lo cambias tú.','Cada 18 meses. Te avisamos por WhatsApp.')
cores=lambda n:''.join("<div class='core'></div>" for _ in range(n))
H['nativo-07-planes']=f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='top'><div class='k'>Elige tu plan</div><h1>Cuánto tiempo<br>te despreocupas</h1></div><div class='plans'><div class='plan'><h2>18 meses</h2><p>1 núcleo</p><div class='cores'>{cores(1)}</div></div><div class='plan m'><h2>3 años</h2><p>2 núcleos</p><div class='cores'>{cores(2)}</div></div><div class='plan'><h2>6 años</h2><p>4 núcleos</p><div class='cores'>{cores(4)}</div></div></div><div class='foot'>elvo·</div><div class='fn' style='left:auto;right:90px;width:900px;text-align:right;bottom:70px'>Cada núcleo dura 18 meses de uso normal.</div></body></html>"
dims="<div class='line' style='left:1100px;top:125px;width:6px;height:1212px;background:#010A21;box-shadow:none'></div><div class='dim' style='left:1140px;top:690px'>30 cm</div><div class='line' style='left:588px;top:1385px;width:474px;height:6px;background:#010A21;box-shadow:none'></div><div class='dim' style='left:640px;top:1405px;padding:10px 26px;font-size:34px'>16 × 16 cm</div>"
H['nativo-08-medidas']=plain('n08.png',dims).replace('</style>','.mark{color:#010A21!important;text-shadow:none!important}</style>')
H['nativo-09-en-la-caja']=toptext('n09.png','En la caja.','Purificador con núcleo · Derivador · Manguera · Adaptador · Llave plástica · Manual')
H['nativo-10-grifos']=f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='top'><div class='k'>Compatibilidad</div><h1>Se adapta a tu grifo</h1></div><div class='photo' style=\"background-image:url('file://{T}n10.png');top:330px;bottom:250px;left:60px;right:60px;border-radius:36px\"></div><div style='position:absolute;left:90px;right:90px;bottom:70px;font-size:42px;font-weight:500'>Kit de adaptadores incluido.<br><span style='color:#46566f;font-size:36px;font-weight:400'>Compatible con la mayoría de grifos estándar.</span></div></body></html>"
os.makedirs('/tmp/ecom/nativo',exist_ok=True)
for f in os.listdir('/tmp/ecom/nativo'): os.remove('/tmp/ecom/nativo/'+f)
for k,h in H.items(): open(f'/tmp/ecom/nativo/{k}.html','w').write(h)
print(len(H))
