#!/usr/bin/env python3
"""6 imágenes de respuesta (Q&A) de Alivio, válidas para 16 L y 22 L. Reusa assets de /tmp/ecom/a16 y a22.
Uso: python3 make_alivio_qa.py && node to_png.js /tmp/ecom/aliviocQA alivio-qa"""
import os,shutil
from PIL import Image
B='/home/user/elvo-creating/brands/elvo/'; A16='/tmp/ecom/a16/'; A22='/tmp/ecom/a22/'
OUT='/tmp/ecom/alivioqa'; os.makedirs(OUT,exist_ok=True)
for f in os.listdir(OUT): os.remove(OUT+'/'+f)
Image.open(B+'content/ecommerce/fotos/etapas7-fal.png').convert('RGB').resize((1500,1500),Image.LANCZOS).save(OUT+'/etapas.png')
CSS="""*{box-sizing:border-box;margin:0}body{width:1500px;height:1500px;font-family:'Inter',sans-serif;color:#010A21;position:relative;overflow:hidden;background:#dbe7f0}
.mark{position:absolute;font-weight:600;font-size:54px;color:#010A21}
.k{font-size:34px;font-weight:600;color:#3355FF;letter-spacing:.5px;text-transform:uppercase}
.top{position:absolute;left:90px;top:80px;right:90px}.top h1{font-weight:500;font-size:92px;line-height:1.05;letter-spacing:-1.5px;margin-top:6px}
.band{position:absolute;left:0;right:0;bottom:0;background:#010A21;color:#fff;padding:44px 90px}.band h1{font-weight:500;font-size:76px;line-height:1.05;letter-spacing:-1.5px}.band p{font-size:36px;margin-top:12px;color:#9EBACE;line-height:1.25}
.ph{background-size:cover;background-position:center}
"""
def page(body,extra=''): return f"<html><head><meta charset='utf-8'><style>{CSS}{extra}</style></head><body>{body}</body></html>"
H={}
# 1 filtración
H['01-filtracion']=page("<div style=\"position:absolute;inset:0;background:url('file://"+OUT+"/etapas.png') 0 0/100% 100%\"></div>")
# 2 uso
rows=[(1,A16+'r1.png','Quitas la tapa y llenas el tanque superior.'),(2,A16+'r2.png','El agua se filtra por gravedad, a través de los filtros.'),(3,A16+'r3.png','Sirves por la llave.')]
rr=''.join(f"<div class='row'><div class='rimg ph' style=\"background-image:url('file://{p}')\"></div><div class='rn'>{n}</div><div class='rt'>{t}</div></div>" for n,p,t in rows)
X=".rows{position:absolute;left:70px;right:70px;top:300px}.row{display:flex;align-items:center;gap:40px;height:320px;margin-bottom:18px}.rimg{flex:0 0 500px;height:330px;border-radius:36px;box-shadow:0 20px 50px rgba(1,10,33,.16)}.rn{flex:0 0 90px;height:90px;border-radius:50%;background:#3355FF;color:#fff;font-size:52px;font-weight:600;display:flex;align-items:center;justify-content:center}.rt{flex:1;font-size:48px;font-weight:500;line-height:1.12;letter-spacing:-.5px}.chip{position:absolute;left:90px;right:90px;bottom:40px;background:#010A21;color:#fff;border-radius:99px;padding:22px 44px;font-size:42px;font-weight:500;text-align:center}"
H['02-uso']=page(f"<div class='top'><div class='k'>Así se usa</div><h1>Tú, en 3 pasos</h1></div><div class='rows'>{rr}</div><div class='chip'>Sin electricidad · Sin instalación</div><div class='mark' style='right:90px;top:80px'>elvo·</div>",X)
# 3 tamaño
def card(img,lit,pers,alto,base,left):
    return f"<div class='cd' style='left:{left}px'><div class='ph cimg' style=\"background-image:url('file://{img}')\"></div><div class='ct'><div class='cl'>{lit} litros</div><div class='cp'>{pers}</div><div class='cm'><b>{alto}</b> de alto · base <b>{base}</b></div></div></div>"
X3=".cd{position:absolute;top:290px;width:640px;height:880px;background:#fff;border-radius:300px 300px 40px 40px;overflow:hidden;box-shadow:0 30px 80px rgba(1,10,33,.16)}.cimg{height:640px}.ct{padding:30px 30px;text-align:center}.cl{font-size:76px;font-weight:600;letter-spacing:-1.5px;color:#3355FF}.cp{font-size:38px;font-weight:500;margin-top:6px}.cm{font-size:32px;color:#46566f;margin-top:16px;line-height:1.3}.cm b{color:#010A21;font-weight:600}"
H['03-tamano']=page("<div class='top'><div class='k'>Modelo Alivio</div><h1>Dos tamaños</h1></div>"+card(A16+'p07.png','16','Para 1 o 2 personas','62 cm','35 × 31 cm',90)+card(A22+'p07.png','22','Para 3 o más personas','61 cm','35 × 23,5 cm',770)+"<div class='mark' style='right:90px;top:80px'>elvo·</div>",X3)
# 4 filtros (dos fotos completas, lado a lado)
X4=".sq{position:absolute;top:400px;width:660px;height:660px;border-radius:44px;box-shadow:0 24px 60px rgba(1,10,33,.2)}.cp{position:absolute;top:1100px;width:660px}.cp h2{font-weight:600;font-size:54px;letter-spacing:-1px;line-height:1.05;color:#3355FF}.cp p{font-size:36px;margin-top:12px;line-height:1.25;color:#2b3b55}.band2{position:absolute;left:0;right:0;bottom:0;height:90px;background:#010A21;color:#fff;font-size:40px;font-weight:600;display:flex;align-items:center;justify-content:center}"
H['04-filtros']=page("<div class='top'><div class='k'>Filtros y gotas de pH</div><h1>Cada filtro rinde<br>10.000 litros o 1 año</h1></div><div class='sq ph' style=\"left:70px;background-image:url('file://"+A16+"p06.png')\"></div><div class='sq ph' style=\"left:770px;background-image:url('file://"+A16+"p05.png')\"></div><div class='cp' style='left:70px'><h2>Tu primer filtro ya viene en el equipo</h2><p>El kit de repuesto se vende aparte.</p></div><div class='cp' style='left:770px'><h2>Gotas de pH incluidas</h2><p>Una gota en el vaso y comparas.</p></div><div class='band2'>elvo·</div>",X4)
# 5 entrega y pago
X5=".sec{position:absolute;left:90px;right:90px;border-radius:44px;padding:44px 54px}.sec h2{font-size:64px;font-weight:600;letter-spacing:-1px}.sec .s{font-size:36px;margin-top:8px}.opt{display:flex;gap:22px;align-items:flex-start;margin-top:40px}.opt i{flex:0 0 18px;height:18px;border-radius:50%;background:#3355FF;margin-top:20px}.opt div{font-size:44px;font-weight:500;line-height:1.15}.opt span{display:block;font-size:34px;font-weight:400;color:#46566f;margin-top:4px}.lima{top:270px;height:330px;background:#010A21;color:#fff}.lima .s{color:#9EBACE}.prov{top:630px;height:760px;background:#fff;box-shadow:0 24px 60px rgba(1,10,33,.12)}.prov h2{color:#3355FF}"
lima="<div class='sec lima'><h2>Lima y Callao</h2><div class='s'>Envío gratis a domicilio.</div><div class='opt' style='margin-top:24px'><i style='background:#9EBACE'></i><div style='color:#fff'>Pagas al recibir</div></div></div>"
prov="<div class='sec prov'><h2>Provincia</h2><div class='s' style='color:#46566f'>Envío S/15. Elige cómo recibirlo:</div>"+"".join(f"<div class='opt'><i></i><div>{a}<span>{b}</span></div></div>" for a,b in [('Recojo en agencia Shalom','Adelanto de S/20 y pagas el saldo al recoger'),('Envío a domicilio','Pago completo por adelantado'),('Pago con tarjeta','Te enviamos un link de pago'),])+"</div>"
H['05-entrega-y-pago']=page("<div class='top'><div class='k'>Entrega y pago</div><h1>Cómo recibes tu Alivio</h1></div>"+lima+prov+"<div class='mark' style='left:90px;bottom:36px'>elvo·</div>",X5)
# 6 caja + garantía
H['06-caja-y-garantia']=page(f"<div style=\"position:absolute;inset:0;background:url('file://{A16}caja.png') 0 0/100% 100%\"></div><div class='top'><h1>En la caja</h1></div><div style='position:absolute;right:90px;top:92px;background:#3355FF;color:#fff;border-radius:99px;padding:20px 36px;font-size:34px;font-weight:500;text-align:center;line-height:1.15'>Garantía de<br>satisfacción de 30 días</div>")
for k,h in H.items(): open(f'{OUT}/alivio-{k}.html','w').write(h)
print(len(H))
