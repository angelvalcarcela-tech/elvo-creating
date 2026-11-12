#!/usr/bin/env python3
"""Imágenes de ecommerce 1500x1500 en estilo Instagram elvo· (luz azul acero, foto primero, poco texto).
Uso: python3 make_ecommerce.py  -> escribe HTML en /tmp/ecom y luego node to_png.js"""
import os
from PIL import Image
B='/home/user/elvo-creating/brands/elvo/'
T='/tmp/ecom/'
def crop(src,out,box):
    im=Image.open(B+src).convert('RGB'); W,H=im.size
    x0,y0,x1,y1=[int(v) for v in (box[0]*W,box[1]*H,box[2]*W,box[3]*H)]
    im.crop((x0,y0,x1,y1)).resize((1500,1500),Image.LANCZOS).save(T+out)
# recortes cuadrados
crop('content/lote7/h2b-vivo-limon_v1.png','v-limon.png',(0,0.13,1,0.93))
crop('content/lote2/f6-vivo-cafe_v1.png','v-cafe.png',(0,0.13,1,0.93))
crop('content/lote1/r2d-vivo-cafe_v1.png','v-balcon.png',(0,0.18,1,0.98))
im=Image.open(B+'content/lote11/n6-conecta_v1.png').convert('RGB'); im.crop((0,int(0.05*im.height),im.width,int(0.88*im.height))).save(T+'v-conecta.png')
im=Image.open(B+'content/lote1/r2d-vivo-cafe_v1.png').convert('RGB'); W,H=im.size; im.crop((int(0.22*W),0,int(0.22*W)+int(0.60*H*0.9),int(0.9*H))).save(T+'v-balcon.png')
CSS="""*{box-sizing:border-box;margin:0}body{width:1500px;height:1500px;font-family:'Inter',sans-serif;color:#010A21;position:relative;overflow:hidden;background:#eef3f7}
.photo{position:absolute;inset:0;background-size:cover;background-position:center}
.scrim{position:absolute;left:0;right:0;bottom:0;height:46%;background:linear-gradient(to top,rgba(1,10,33,.78),rgba(1,10,33,0))}
.mark{position:absolute;left:90px;top:80px;font-weight:600;font-size:54px;color:#fff;text-shadow:0 2px 14px rgba(1,10,33,.35)}
.cap{position:absolute;left:90px;right:90px;bottom:90px;color:#fff}
.cap h1{font-weight:500;font-size:96px;line-height:1.08;letter-spacing:-1.5px}
.cap p{font-size:44px;margin-top:22px;color:#dfe9ff;font-weight:400}
.panel{position:absolute;inset:0;background:#dbe7f0}
.arch{position:absolute;right:90px;top:150px;width:640px;height:1200px;border-radius:320px 320px 40px 40px;background-size:cover;background-position:center;box-shadow:0 30px 80px rgba(1,10,33,.18)}
.txt{position:absolute;left:90px;top:150px;width:660px}
.txt .k{font-size:34px;font-weight:600;color:#3355FF;letter-spacing:.5px;text-transform:uppercase}
.txt h1{font-weight:500;font-size:84px;line-height:1.08;letter-spacing:-1.2px;margin:24px 0 50px}
.item{display:flex;gap:26px;margin:0 0 34px}.item b{flex:0 0 66px;height:66px;border-radius:50%;background:#3355FF;color:#fff;font-size:34px;display:flex;align-items:center;justify-content:center}
.item div{font-size:40px;line-height:1.2;font-weight:500}.item small{display:block;font-size:30px;font-weight:400;color:#46566f;margin-top:6px}
.foot{position:absolute;left:90px;bottom:70px;font-weight:600;font-size:48px;color:#010A21}
"""
def life(name,img,title,sub):
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='photo' style=\"background-image:url('file://{T}{img}')\"></div><div class='scrim'></div><div class='mark'>elvo·</div><div class='cap'><h1>{title}</h1><p>{sub}</p></div></body></html>"
def panel(name,img,kicker,title,items):
    its=''.join(f"<div class='item'><b>{i+1}</b><div>{a}<small>{b}</small></div></div>" for i,(a,b) in enumerate(items))
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='panel'></div><div class='txt'><div class='k'>{kicker}</div><h1>{title}</h1>{its}</div><div class='arch' style=\"background-image:url('file://{T}{img}')\"></div><div class='foot'>elvo·</div></body></html>"
P={}
P['vivo-01-limon']=life('a','v-limon.png','Agua más rica,<br>sin sabor a cloro.','Directo de tu caño.')
P['vivo-02-cafe']=life('b','v-cafe.png','Con magnesio y<br>tendencia alcalina.','pH ~8.5 · el sabor de cada día.')
P['vivo-03-etapas']=panel('c','v-balcon.png','4 etapas','Cómo filtra<br>elvo· Vivo',[('Ultrafiltración','cloro, sedimentos, olores y sabor'),('Carbón activado','contra cloro y mal sabor'),('Aporte de magnesio','mineraliza y deja el agua alcalina'),('Microfiltración','microplásticos y partículas finas')])
P['vivo-04-instalacion']=panel('d','v-conecta.png','Instalación','La instalas tú<br>en 5 minutos',[('Conecta el derivador','al caño, con el kit de adaptadores'),('Deja correr 5 minutos','solo la primera vez'),('Mueve la palanca','y sirve por el pico')])
os.makedirs('/tmp/ecom/html',exist_ok=True)
for k,h in P.items(): open(f'/tmp/ecom/html/{k}.html','w').write(h)
print(list(P))
