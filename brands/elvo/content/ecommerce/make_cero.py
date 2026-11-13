#!/usr/bin/env python3
"""10 láminas de ecommerce de Cero (1500x1500), estilo Instagram. Uso: python3 make_cero.py && node to_png.js /tmp/ecom/cero cero"""
import os
from PIL import Image,ImageFilter
B='/home/user/elvo-creating/brands/elvo/'; T='/tmp/ecom/'; F=B+'content/ecommerce/fotos/'; L=B+'content/lote11/'
os.makedirs(T+'cero',exist_ok=True)
def sq(path,out,y0=0.0):
    im=Image.open(path).convert('RGB'); W,H=im.size
    c=im if W==H else im.crop((0,int(y0*H),W,int(y0*H)+W))
    c.resize((1500,1500),Image.LANCZOS).save(T+out)
def port(path,out,box):
    im=Image.open(path).convert('RGB'); W,H=im.size
    x0,y0,x1,y1=[int(v) for v in (box[0]*W,box[1]*H,box[2]*W,box[3]*H)]
    im.crop((x0,y0,x1,y1)).resize((460,960),Image.LANCZOS).save(T+out)
sq(L+'c1-hook_v1.png','c01.png',0.10)
sq(F+'cero-02-fria-caliente-e.png','c02.png')
sq(L+'c6-ml_v1.png','c03.png',0.22)
sq(F+'cero-05-jarra-mesa.png','c05.png')
im=Image.open(F+'cero-06-aviso-retoque.png').convert('RGB'); im.resize((1500,1500),Image.LANCZOS).save(T+'c06.png')
im=Image.open(F+'cero-06-aviso-d.png').convert('RGB'); im.crop((80,240,1450,1400)).resize((1370,1160),Image.LANCZOS).save(T+'cmp-cero.png')
im=Image.open(F+'osmosis-lavadero.png').convert('RGB'); im.crop((60,200,1470,1400)).resize((1410,1200),Image.LANCZOS).save(T+'cmp-lav.png')
sq(F+'cero-08-caja-d.png','c09.png')
sq(F+'cero-10-oficina-b.png','c10.png')
# medidas: foto vertical completa sobre fondo azul noche con bordes suaves
import numpy as np
im=Image.open(L+'c2-presenta_v1.png').convert('RGB')
fg=im.resize((int(im.width*1500/im.height),1500),Image.LANCZOS)
edge=np.array(fg)[40:200,5:40].reshape(-1,3).mean(axis=0).astype(int)
bg=Image.new('RGB',(1500,1500),tuple(edge))
a=np.ones((1500,fg.width)); r=140
for i in range(r): a[:,i]=i/r; a[:,fg.width-1-i]=i/r
mask=Image.fromarray((a*255).astype('uint8'))
bg.paste(fg,((1500-fg.width)//2,0),mask); bg.save(T+'c08.png')
port(L+'c3-llenado_v1.png','p1.png',(0.10,0.05,0.92,0.05+0.82*960/820*0.60/0.60*0.55))
port(L+'c6-ml_v1.png','p2.png',(0.05,0.25,0.95,0.80))
im=Image.open(F+'cero-boton-presionando.png').convert('RGB'); im.crop((360,242,980,1536)).resize((460,960),Image.LANCZOS).save(T+'p3.png')
CSS="""*{box-sizing:border-box;margin:0}body{width:1500px;height:1500px;font-family:'Inter',sans-serif;color:#010A21;position:relative;overflow:hidden;background:#dbe7f0}
.photo{position:absolute;inset:0;background-size:cover;background-position:center}
.scrim{position:absolute;left:0;right:0;bottom:0;height:40%;background:linear-gradient(to top,rgba(1,10,33,.74),rgba(1,10,33,0))}
.mark{position:absolute;left:90px;top:80px;font-weight:600;font-size:54px;color:#fff;text-shadow:0 2px 14px rgba(1,10,33,.35)}
.cap{position:absolute;left:90px;right:90px;bottom:84px;color:#fff}
.cap h1{font-weight:500;font-size:92px;line-height:1.08;letter-spacing:-1.5px}.cap p{font-size:42px;margin-top:18px;color:#dfe9ff}
.steps{position:absolute;left:60px;right:60px;top:250px;display:flex;gap:30px}
.step{flex:1}.step .img{height:960px;border-radius:230px 230px 30px 30px;background-size:cover;background-position:center;box-shadow:0 24px 60px rgba(1,10,33,.18)}
.step b{display:flex;margin-top:26px;gap:18px;align-items:center;font-size:40px;font-weight:500}.step b i{font-style:normal;flex:0 0 62px;height:62px;border-radius:50%;background:#3355FF;color:#fff;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:600}
.top{position:absolute;left:90px;top:90px}.top .k{font-size:34px;font-weight:600;color:#3355FF;text-transform:uppercase;letter-spacing:.5px}.top h1{font-weight:500;font-size:84px;letter-spacing:-1.2px;margin-top:14px}
.dim{position:absolute;background:#fff;border-radius:99px;padding:14px 30px;font-size:38px;font-weight:600;box-shadow:0 10px 30px rgba(1,10,33,.2);color:#010A21;white-space:nowrap}
.line{position:absolute;background:#fff;box-shadow:0 0 0 2px rgba(1,10,33,.25)}
.tbl{position:absolute;left:90px;right:90px;top:270px}.row{display:flex;gap:22px;margin-bottom:18px}.row>div{flex:1;border-radius:26px;padding:22px 32px;font-size:38px;font-weight:500;min-height:118px;display:flex;align-items:center;line-height:1.15}.why{position:absolute;left:90px;right:90px;bottom:150px;background:#010A21;color:#fff;border-radius:30px;padding:34px 42px;font-size:40px;line-height:1.25;font-weight:500}.why b{color:#9EBACE;font-weight:600}
.lab{flex:0 0 250px!important;background:transparent;color:#46566f;font-size:32px!important;font-weight:600!important;text-transform:uppercase;letter-spacing:.5px;padding:0!important}
.us{background:#3355FF;color:#fff}.them{background:#fff;color:#46566f}.hd>div{font-size:46px;font-weight:600;min-height:110px;background:transparent;padding:0 36px}.hd .us{background:transparent;color:#3355FF}.hd .them{background:transparent;color:#46566f;font-size:36px}
.cmp{position:absolute;left:60px;right:60px;top:150px;display:flex;gap:30px}.col{flex:1;border-radius:36px;overflow:hidden}.col.us{background:#3355FF}.col.them{background:#fff;box-shadow:0 0 0 3px #c9d7e3 inset}.pic{height:560px;background-size:cover;background-position:center}.clab{padding:22px 30px 10px;font-size:42px;font-weight:600;color:#fff}.col.them .clab{color:#46566f;font-size:36px}.r{display:flex;align-items:center;gap:20px;padding:0 30px;height:130px;font-size:37px;font-weight:500;line-height:1.1;color:#fff}.col.them .r{color:#46566f}.r+.r{border-top:2px solid rgba(255,255,255,.28)}.col.them .r+.r{border-top-color:#dbe3ea}.ic{flex:0 0 64px;height:64px;border-radius:50%;background:rgba(255,255,255,.2);display:flex;align-items:center;justify-content:center}.col.them .ic{background:#e8eef3}.ic svg{width:34px;height:34px;stroke:#fff;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}.col.them .ic svg{stroke:#6b7b90}
.bd{position:absolute;width:74px;height:74px;border-radius:50%;background:#3355FF;color:#fff;font-size:42px;font-weight:700;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 6px rgba(255,255,255,.9)}
.band3{position:absolute;left:0;right:0;bottom:0;background:rgba(1,10,33,.92);padding:42px 80px 50px;color:#fff}.band3 h1{font-weight:500;font-size:62px;letter-spacing:-1px;margin-bottom:22px}.band3 .it{display:flex;align-items:center;gap:22px;font-size:46px;font-weight:500;margin:12px 0}.band3 .it i{font-style:normal;flex:0 0 58px;height:58px;border-radius:50%;background:#3355FF;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:700}
"""
def life(img,title,sub=''):
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='photo' style=\"background-image:url('file://{T}{img}')\"></div><div class='scrim'></div><div class='mark'>elvo·</div><div class='cap'><h1>{title}</h1><p>{sub}</p></div></body></html>"
def band(img,title,sub=''):
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body style='background:#010A21'><div class='photo' style=\"background-image:url('file://{T}{img}');bottom:330px;background-position:center 38%\"></div><div class='mark'>elvo·</div><div style='position:absolute;left:90px;right:90px;bottom:70px;color:#fff'><h1 style='font-weight:500;font-size:76px;line-height:1.08;letter-spacing:-1.2px'>{title}</h1><p style='font-size:38px;margin-top:12px;color:#9EBACE'>{sub}</p></div></body></html>"
def toptext(img,title,sub=''):
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='photo' style=\"background-image:url('file://{T}{img}')\"></div><div style='position:absolute;left:0;right:0;top:0;height:42%;background:linear-gradient(to bottom,rgba(255,255,255,.85),rgba(255,255,255,0))'></div><div style='position:absolute;left:90px;top:80px;color:#010A21'><h1 style='font-weight:500;font-size:92px;letter-spacing:-1.5px'>{title}</h1><p style='font-size:42px;margin-top:14px;color:#2b3b55'>{sub}</p></div><div class='mark' style='top:auto;bottom:70px;color:#fff'>elvo·</div></body></html>"
def plain(img,extra=''):
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='photo' style=\"background-image:url('file://{T}{img}')\"></div><div class='mark'>elvo·</div>{extra}</body></html>"
steps=''.join(f"<div class='step'><div class='img' style=\"background-image:url('file://{T}{p}')\"></div><b><i>{n}</i>{t}</b></div>" for n,p,t in ((1,'p1.png','Llenas el tanque'),(2,'p2.png','Eliges temperatura y ml'),(3,'p3.png','Presionas y sirves')))
rows=[('Purificación','Ósmosis inversa + desinfección UV','Ósmosis inversa'),('Instalación','Sin instalación','Con gasfitero'),('Agua','Fría y caliente','Una sola temperatura'),('Jarra','Extraíble, de 2 L','No incluye'),('Ubicación','Sobre la mesada','Debajo del lavadero')]
tbl="<div class='row hd'><div class='lab'></div><div class='us'>elvo· Cero</div><div class='them'>Ósmosis de lavadero (típica)</div></div>"+''.join(f"<div class='row'><div class='lab'>{a}</div><div class='us'>{b}</div><div class='them'>{c}</div></div>" for a,b,c in rows)
H={}
H['cero-01-principal']=plain('c01.png')
H['cero-02-fria-caliente']=life('c02.png','Fría o caliente.','De 6 °C a 85 °C.')
H['cero-03-temperatura-y-ml']=life('c03.png','Elige la temperatura<br>y los ml.','Para tus recetas.')
H['cero-04-asi-se-usa']=f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='top'><div class='k'>Así se usa</div><h1>Tres pasos, sin instalación</h1></div><div class='steps'>{steps}</div><div style='position:absolute;left:90px;bottom:70px;font-weight:600;font-size:48px'>elvo·</div></body></html>"
H['cero-05-jarra-a-la-mesa']=life('c05.png','La jarra va a la mesa.','2 litros de agua purificada.')
svg="<svg style='position:absolute;inset:0' width='1500' height='1500'><g stroke='#fff' stroke-width='5' fill='none' stroke-linecap='round'><line x1='405' y1='290' x2='450' y2='335'/><line x1='650' y1='470' x2='598' y2='516'/><line x1='290' y1='598' x2='372' y2='600'/></g></svg>"
badges="<div class='bd' style='left:335px;top:215px'>1</div><div class='bd' style='left:640px;top:432px'>2</div><div class='bd' style='left:215px;top:560px'>3</div>"
H['cero-06-filtros']=f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='photo' style=\"background-image:url('file://{T}c06.png')\"></div>{svg}{badges}<div class='band3'><h1>Te avisa cuándo:</h1><div class='it'><i>1</i>cambiar los filtros</div><div class='it'><i>2</i>llenar el tanque</div><div class='it'><i>3</i>la jarra tiene agua</div></div></body></html>"
ic={'p':"<svg viewBox='0 0 24 24'><path d='M12 2.7l5.7 5.7a8 8 0 1 1-11.3 0z'/></svg>",'i':"<svg viewBox='0 0 24 24'><path d='M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z'/></svg>",'a':"<svg viewBox='0 0 24 24'><path d='M14 14.76V3.5a2.5 2.5 0 0 0-5 0v11.26a4.5 4.5 0 1 0 5 0z'/></svg>",'j':"<svg viewBox='0 0 24 24'><path d='M6 4h9v4l1 1v10a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V9l1-1z'/><path d='M16 10h2a2 2 0 0 1 0 5h-2'/></svg>",'u':"<svg viewBox='0 0 24 24'><path d='M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z'/><path d='M9 22V12h6v10'/></svg>"}
rows=[('p','Ósmosis inversa + desinfección UV','Ósmosis inversa'),('i','Sin instalación','Con gasfitero'),('a','Fría y caliente','Una sola temperatura'),('j','Jarra extraíble de 2 L','Sin jarra'),('u','Sobre la mesada','Debajo del lavadero')]
us=''.join(f"<div class='r'><div class='ic'>{ic[k]}</div>{a}</div>" for k,a,b in rows)
th=''.join(f"<div class='r'><div class='ic'>{ic[k]}</div>{b}</div>" for k,a,b in rows)
H['cero-07-comparacion']=f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='top' style='top:50px'><h1 style='font-size:68px;margin:0'>Cero vs. ósmosis de lavadero</h1></div><div class='cmp'><div class='col us'><div class='pic' style=\"background-image:url('file://{T}cmp-cero.png')\"></div><div class='clab'>elvo· Cero</div>{us}</div><div class='col them'><div class='pic' style=\"background-image:url('file://{T}cmp-lav.png')\"></div><div class='clab'>Ósmosis de lavadero (típica)</div>{th}</div></div></body></html>"
dims="<div class='line' style='left:440px;top:438px;width:6px;height:711px'></div><div class='dim' style='left:150px;top:760px'>37,6 cm</div><div class='line' style='left:479px;top:1190px;width:525px;height:6px'></div><div class='dim' style='left:560px;top:1230px'>47,9 cm</div><div class='dim' style='left:1030px;top:760px'>22,5 cm</div>"
H['cero-08-medidas']=plain('c08.png',dims)
H['cero-09-en-la-caja']=toptext('c09.png','En la caja.','Purificador con jarra · Manual · Garantía')
H['cero-10-oficina']=life('c10.png','Para la oficina también.')
os.makedirs('/tmp/ecom/cero',exist_ok=True)
for f in os.listdir('/tmp/ecom/cero'): os.remove('/tmp/ecom/cero/'+f)
for k,h in H.items(): open(f'/tmp/ecom/cero/{k}.html','w').write(h)
print(len(H))
