#!/usr/bin/env python3
"""9 láminas de ecommerce de Cero (1500x1500), estilo Instagram. Uso: python3 make_cero.py && node to_png.js /tmp/ecom/cero cero"""
import os
from PIL import Image
B='/home/user/elvo-creating/brands/elvo/'; T='/tmp/ecom/'; F=B+'content/ecommerce/fotos/'; L=B+'content/lote11/'
os.makedirs(T+'cero',exist_ok=True)
def sq(path,out,y0=0.0):   # recorte cuadrado de una foto vertical o cuadrada
    im=Image.open(path).convert('RGB'); W,H=im.size
    if W==H: c=im
    else: y=int(y0*H); c=im.crop((0,y,W,y+W))
    c.resize((1500,1500),Image.LANCZOS).save(T+out)
def port(path,out,box):      # recorte vertical para los 3 pasos
    im=Image.open(path).convert('RGB'); W,H=im.size
    x0,y0,x1,y1=[int(v) for v in (box[0]*W,box[1]*H,box[2]*W,box[3]*H)]
    im.crop((x0,y0,x1,y1)).resize((460,820),Image.LANCZOS).save(T+out)
sq(L+'c1-hook_v1.png','c01.png',0.10)
sq(F+'cero-02-fria-caliente.png','c02.png')
sq(L+'c3-llenado_v1.png','c04.png',0.08)
sq(F+'cero-05-jarra-mesa.png','c05.png')
sq(F+'cero-02-fria-caliente.png','c06.png')
sq(F+'cero-07-filtros-b.png' if os.path.exists(F+'cero-07-filtros-b.png') else F+'cero-07-filtros.png','c07.png')
sq(F+'cero-08-caja-b.png' if os.path.exists(F+'cero-08-caja-b.png') else F+'cero-08-caja.png','c08.png')
sq(F+'cero-09-oficina.png','c09.png')
port(L+'c3-llenado_v1.png','p1.png',(0.02,0.08,0.98,0.08+0.96*1152/2048*820/460*0+0.50))
port(L+'c6-ml_v1.png','p2.png',(0.08,0.30,0.92,0.80))
port(L+'c4-fria-b_v1.png','p3.png',(0.10,0.12,0.90,0.62))
CSS="""*{box-sizing:border-box;margin:0}body{width:1500px;height:1500px;font-family:'Inter',sans-serif;color:#010A21;position:relative;overflow:hidden;background:#dbe7f0}
.photo{position:absolute;inset:0;background-size:cover;background-position:center}
.scrim{position:absolute;left:0;right:0;bottom:0;height:40%;background:linear-gradient(to top,rgba(1,10,33,.74),rgba(1,10,33,0))}
.mark{position:absolute;left:90px;top:80px;font-weight:600;font-size:54px;color:#fff;text-shadow:0 2px 14px rgba(1,10,33,.35)}
.cap{position:absolute;left:90px;right:90px;bottom:84px;color:#fff}
.cap h1{font-weight:500;font-size:92px;line-height:1.08;letter-spacing:-1.5px}.cap p{font-size:42px;margin-top:18px;color:#dfe9ff}
.steps{position:absolute;left:60px;right:60px;top:300px;display:flex;gap:30px}
.step{flex:1}.step .img{height:820px;border-radius:230px 230px 30px 30px;background-size:cover;background-position:center;box-shadow:0 24px 60px rgba(1,10,33,.18)}
.step b{display:flex;margin-top:26px;gap:18px;align-items:center;font-size:40px;font-weight:500}.step b i{font-style:normal;flex:0 0 62px;height:62px;border-radius:50%;background:#3355FF;color:#fff;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:600}
.top{position:absolute;left:90px;top:90px}.top .k{font-size:34px;font-weight:600;color:#3355FF;text-transform:uppercase;letter-spacing:.5px}.top h1{font-weight:500;font-size:84px;letter-spacing:-1.2px;margin-top:14px}
.dim{position:absolute;background:#fff;border-radius:99px;padding:14px 30px;font-size:38px;font-weight:600;box-shadow:0 10px 30px rgba(1,10,33,.2);color:#010A21}
.line{position:absolute;background:#fff;box-shadow:0 0 0 2px rgba(1,10,33,.25)}
"""
def life(img,title,sub='',extra=''):
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='photo' style=\"background-image:url('file://{T}{img}')\"></div><div class='scrim'></div><div class='mark'>elvo·</div>{extra}<div class='cap'><h1>{title}</h1><p>{sub}</p></div></body></html>"
def plain(img,extra=''):
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='photo' style=\"background-image:url('file://{T}{img}')\"></div><div class='mark'>elvo·</div>{extra}</body></html>"
steps=''.join(f"<div class='step'><div class='img' style=\"background-image:url('file://{T}{p}')\"></div><b><i>{n}</i>{t}</b></div>" for n,p,t in ((1,'p1.png','Llenas el tanque'),(2,'p2.png','Eliges temperatura y ml'),(3,'p3.png','Sirves')))
H={}
H['cero-01-principal']=plain('c01.png')
H['cero-02-fria-caliente']=life('c02.png','Fría o caliente.','Desde 6 °C hasta 85 °C.')
H['cero-03-como-se-usa']=f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='top'><div class='k'>Así se usa</div><h1>Tres pasos, sin instalación</h1></div><div class='steps'>{steps}</div><div style='position:absolute;left:90px;bottom:70px;font-weight:600;font-size:48px'>elvo·</div></body></html>"
H['cero-04-sin-instalacion']=life('c04.png','Sin instalación.','Solo llenas el tanque trasero.')
H['cero-05-jarra-extraible']=life('c05.png','La jarra va a la mesa.','2 litros de agua purificada.')
dims="<div class='line' style='left:392px;top:345px;width:6px;height:885px'></div><div class='dim' style='left:150px;top:690px'>37,6 cm</div><div class='line' style='left:450px;top:1290px;width:780px;height:6px'></div><div class='dim' style='left:690px;top:1330px'>47,9 cm</div><div class='dim' style='left:1190px;top:560px'>22,5 cm fondo</div>"
H['cero-06-medidas']=plain('c06.png',dims)
H['cero-07-filtros']=life('c07.png','Te avisa cuándo<br>cambiar los filtros.','Y tiene autolimpieza.')
H['cero-08-en-la-caja']=life('c08.png','En la caja.','Equipo · Jarra de 2 L · Manual · Garantía')
H['cero-09-oficina']=life('c09.png','Para la oficina también.','Menos pedidos de bidones.')
os.makedirs('/tmp/ecom/cero',exist_ok=True)
for k,h in H.items(): open(f'/tmp/ecom/cero/{k}.html','w').write(h)
print(len(H))
