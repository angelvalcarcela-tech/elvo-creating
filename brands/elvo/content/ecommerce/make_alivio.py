#!/usr/bin/env python3
"""Sets de ecommerce de Alivio (16 L y 22 L), armados con fotos que ya existen (tienda + nuestras). Sin generar nada.
Uso: python3 make_alivio.py 16|22  &&  node to_png.js /tmp/ecom/alivioNN alivioNN"""
import os,sys,glob
import numpy as np
from PIL import Image
M=sys.argv[1]
MED22=(447,265,1033,1333)
B='/home/user/elvo-creating/brands/elvo/'; T=f'/tmp/ecom/a{M}/'; os.makedirs(T,exist_ok=True)
S=f'/tmp/ali/src{M}/'
def src(n):
    return glob.glob(S+n+'.*')[0]
def sq(path,out,box=None,size=1500):
    im=Image.open(path).convert('RGB')
    if box: im=im.crop(box)
    im=im.resize((size,size),Image.LANCZOS); im.save(T+out)
def crop(path,out,box,size):
    Image.open(path).convert('RGB').crop(box).resize(size,Image.LANCZOS).save(T+out)
# ---------- recortes por modelo ----------
X0 = 105 if M=='22' else None
def sqx(n,out,x0):   # foto de uso de la tienda sin banda: 990x990 desde x0
    sq(src(n),out,(x0,0,x0+990,990))
if M=='16':
    sq(B+'content/lote11/a1b-hook_v1.png','p01.png',(0,380,1152,1532))
    sq(B+'content/lote11/a4-sin-presion_v1.png','p03.png',(0,420,1152,1572))
    sqx('04','u1.png',105); sqx('06','u3.png',130); sqx('10','p05.png',0); sqx('13','p06.png',60); sqx('05','p07.png',80)
    sq(B+'content/lote10/a-sirve-llave_v1.png','p10.png',(0,520,1152,1672))
    crop(src('04'),'s1.png',(480,0,1080,600),(600,880)) if False else crop(src('04'),'s1.png',(480,0,1080,880),(600,880)); crop(src('04'),'s2.png',(0,0,600,880),(600,880)); crop(src('06'),'s3.png',(330,110,930,990),(600,880))
else:
    sq(src('06'),'p01.png',(105,0,1095,990)); sqx('07','p03.png',105)
    sqx('10','p05.png',105); sqx('13','p06.png',105); sqx('05','p07.png',105); sqx('04','p10.png',105)
    crop(src('04'),'s1.png',(560,0,1160,880),(600,880)); crop(src('04'),'s2.png',(105,0,705,880),(600,880)); crop(src('06'),'s3.png',(540,110,1140,990),(600,880))
# pasos (cuadrados): llenar, filtros, servir
if M=='16':
    sq(src('04'),'r1.png',(105,0,1095,990),size=700); sq(src('05'),'r2.png',(80,0,1070,990),size=700); sq(src('06'),'r3.png',(130,0,1120,990),size=700)
else:
    sq(src('04'),'r1.png',(105,0,1095,990),size=700); sq(src('05'),'r2.png',(105,0,1095,990),size=700); sq(src('06'),'r3.png',(105,0,1095,990),size=700)
# ilustración de componentes (foto 8 de la tienda)
im8=Image.open(src('08')).convert('RGB'); _c=im8.crop((255,215,553,1012)).resize((596,1594),Image.LANCZOS); _a=np.array(_c).astype(int)
_m=(_a[...,2]>170)&(_a[...,0]<110)&(_a[...,1]<140); _a[_m]=255; Image.fromarray(_a.astype('uint8')).save(T+'comp.png')
# medidas
if M=='16':
    im=Image.open(src('16')).convert('RGB'); W,H=im.size; side=max(W,H); a=np.array(im).astype(int)
    bgcol=tuple(a[:,:30].reshape(-1,3).mean(axis=0).astype(int)); cv=Image.new('RGB',(side,side),bgcol); cv.paste(im,((side-W)//2,(side-H)//2)); cv=cv.resize((1500,1500),Image.LANCZOS)
    def bbox_of(cvimg):
        from PIL import ImageFilter
        g=np.array(cvimg.convert('L').filter(ImageFilter.GaussianBlur(2))).astype(float)
        gy,gx=np.gradient(g); mag=np.hypot(gx,gy); mask=mag>9
        rows=np.where(mask[:,150:1350].sum(axis=1)>8)[0]; cols=np.where(mask[100:1400].sum(axis=0)>8)[0]
        return int(cols.min()),int(rows.min()),int(cols.max()),int(rows.max())
    bx=bbox_of(cv); cx,cy=(bx[0]+bx[2])//2,(bx[1]+bx[3])//2; side2=min(1500,int(max(bx[2]-bx[0],bx[3]-bx[1])*1.5))
    x0c=max(0,min(1500-side2,cx-side2//2)); y0c=max(0,min(1500-side2,cy-side2//2))
    cv=cv.crop((x0c,y0c,x0c+side2,y0c+side2)).resize((1500,1500),Image.LANCZOS); cv.save(T+'med.png'); BB=bbox_of(cv)
else:
    sq(src('04'),'med.png',(105,0,1095,990)); BB=MED22
print('bbox equipo',BB,file=sys.stderr)
# caja: foto 11 sin su título
c11=Image.open(src('11')).convert('RGB'); w,h=c11.size
hdr=int(h*0.17); body=c11.crop((0,hdr,w,h)); bgc=c11.getpixel((8,8)); 
cv=Image.new('RGB',(w,h),bgc); cv.paste(body,(0,int(h*0.17))); cv=cv.resize((1500,1500),Image.LANCZOS); cv.save(T+'caja.png')
CSS="""*{box-sizing:border-box;margin:0}body{width:1500px;height:1500px;font-family:'Inter',sans-serif;color:#010A21;position:relative;overflow:hidden;background:#dbe7f0}
.photo{position:absolute;inset:0;background-size:cover;background-position:center}
.scrim{position:absolute;left:0;right:0;bottom:0;height:42%;background:linear-gradient(to top,rgba(1,10,33,.78),rgba(1,10,33,0))}
.tscrim{position:absolute;left:0;right:0;top:0;height:42%;background:linear-gradient(to bottom,rgba(255,255,255,.88),rgba(255,255,255,0))}
.mark{position:absolute;left:90px;top:80px;font-weight:600;font-size:54px;color:#fff;text-shadow:0 2px 14px rgba(1,10,33,.35)}
.mark.d{color:#010A21;text-shadow:none}.mark.b{top:auto;bottom:60px}
.cap{position:absolute;left:90px;right:90px;bottom:84px;color:#fff}.cap h1{font-weight:500;font-size:88px;line-height:1.08;letter-spacing:-1.5px}.cap p{font-size:40px;margin-top:16px;color:#dfe9ff}
.cap.n{right:auto;width:640px}.cap.n h1{font-size:72px}.cap.n p{font-size:36px}
.top{position:absolute;left:90px;top:80px;right:90px}.top h1{font-weight:500;font-size:92px;line-height:1.05;letter-spacing:-1.5px}.top p{font-size:42px;margin-top:14px;color:#2b3b55}
.k{font-size:34px;font-weight:600;color:#3355FF;letter-spacing:.5px;text-transform:uppercase}
.steps{position:absolute;left:60px;right:60px;top:290px;display:flex;gap:30px}.step{flex:1}.step .img{height:880px;border-radius:230px 230px 30px 30px;background-size:cover;background-position:center;box-shadow:0 24px 60px rgba(1,10,33,.18)}
.step b{display:flex;margin-top:26px;gap:18px;align-items:center;font-size:38px;font-weight:500;line-height:1.1}.step b i{font-style:normal;flex:0 0 62px;height:62px;border-radius:50%;background:#3355FF;color:#fff;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:600}
.foot{position:absolute;left:90px;bottom:60px;font-weight:600;font-size:48px}
.list{position:absolute;left:90px;top:300px;width:660px}.item{display:flex;gap:22px;margin:0 0 20px;align-items:center}.item b{flex:0 0 58px;height:58px;border-radius:50%;background:#3355FF;color:#fff;font-size:30px;display:flex;align-items:center;justify-content:center}.item div{font-size:38px;line-height:1.1;font-weight:500}.item .s{display:block;font-size:27px;font-weight:400;color:#46566f;margin-top:4px;line-height:1.2}
.arch{position:absolute;right:60px;top:150px;width:560px;height:1220px;border-radius:300px 300px 40px 40px;background:#fff;box-shadow:0 30px 80px rgba(1,10,33,.18);display:flex;align-items:center;justify-content:center}.arch img{height:1000px;width:auto}
.dim{position:absolute;background:#fff;border-radius:99px;padding:14px 30px;font-size:38px;font-weight:600;box-shadow:0 10px 30px rgba(1,10,33,.2);white-space:nowrap}.line{position:absolute;background:#010A21}
.fn{position:absolute;left:90px;right:90px;bottom:34px;font-size:24px;color:#46566f}
"""
def page(body,extra=''): return f"<html><head><meta charset='utf-8'><style>{CSS}{extra}</style></head><body>{body}</body></html>"
def bgp(img): return f"<div class='photo' style=\"background-image:url('file://{T}{img}')\"></div>"
def life(img,t,s='',n=False): return page(bgp(img)+f"<div class='scrim'></div><div class='mark'>elvo·</div><div class='cap{' n' if n else ''}'><h1>{t}</h1><p>{s}</p></div>")
def band(img,t,s='',pos='center'):
    return page(f"<div class='photo' style=\"background-image:url('file://{T}{img}');bottom:370px;background-position:{pos}\"></div><div class='mark'>elvo·</div><div style='position:absolute;left:0;right:0;bottom:0;height:370px;background:#010A21;color:#fff;padding:52px 90px'><h1 style='font-weight:500;font-size:84px;line-height:1.05;letter-spacing:-1.5px'>{t}</h1><p style='font-size:38px;margin-top:16px;color:#9EBACE;line-height:1.25'>{s}</p></div>")
def lifetop(img,t,s=''): return page(bgp(img)+f"<div class='tscrim'></div><div class='top'><h1>{t}</h1><p>{s}</p></div><div class='mark b d'>elvo·</div>")
L16=(M=='16'); lit='16' if L16 else '22'; pers='Para 1 o 2 personas' if L16 else 'Para 3 o más personas'
dims_h=('62 cm','35 × 31 cm') if L16 else ('61 cm','35 × 23,5 cm')
H={}
H['01-principal']=page(bgp('p01.png')+"<div class='mark'>elvo·</div>")
etapas=[('Filtro cerámico','Barrera de microporos: retiene sedimentos y partículas.'),
 ('Carbón activado y de plata','Reduce cloro, olores y mal sabor. La plata inhibe microorganismos.'),
 ('WMSM-300','Medio filtrante del filtro multimedia.'),
 ('Arena de sílice','Filtro mecánico: retiene partículas finas.'),
 ('Zeolita','Mineral de intercambio iónico: ayuda a retener impurezas disueltas.'),
 ('Arena mineral','Mineral que ayuda a equilibrar el pH.'),
 ('Piedra mineral','Aporta minerales al agua.'),
 ('Llave','Sirves cuando quieras.')]
its=''.join(f"<div class='item'><b>{i+1}</b><div>{n}<span class='s'>{d}</span></div></div>" for i,(n,d) in enumerate(etapas))
FL=[('Retiene sedimentos y partículas','Filtro cerámico',395),
 ('Reduce cloro, olores y mal sabor','Carbón activado y de plata',634),
 ('Complementa el filtrado','WMSM-300',718),
 ('Retiene partículas finas','Arena de sílice',802),
 ('Ayuda a retener impurezas disueltas','Zeolita',886),
 ('Ayuda a equilibrar el pH','Arena mineral',970),
 ('Aporta minerales al agua','Piedra mineral',1143),
 ('Sirves cuando quieras','Llave',1335)]
rowsf=''
for i,(big,small,cy) in enumerate(FL):
    rowsf+=f"<div class='fr' style='top:{cy-40}px'><b>{i+1}</b><div><span class='fb'>{big}</span><span class='fs'>{small}</span></div></div>"
FLCSS=".fr{position:absolute;left:86px;width:760px;height:80px;display:flex;align-items:center;gap:22px}.fr b{flex:0 0 54px;height:54px;border-radius:50%;background:#3355FF;color:#fff;font-size:30px;display:flex;align-items:center;justify-content:center;position:relative;z-index:2;box-shadow:0 0 0 8px #dbe7f0}.fr .fb{display:block;font-size:35px;font-weight:500;line-height:1.08;letter-spacing:-.4px}.fr .fs{display:block;font-size:20px;font-weight:600;letter-spacing:1.6px;text-transform:uppercase;color:#5a6f8a;margin-top:5px}.flow{position:absolute;left:111px;top:300px;width:4px;height:1040px;background:linear-gradient(#3355FF,rgba(51,85,255,.25))}.lk{position:absolute;height:3px;background:#9EBACE}.br{position:absolute;left:1015px;top:592px;width:16px;height:421px;border:3px solid #3355FF;border-left:0;border-radius:0 14px 14px 0}.brl2{position:absolute;left:968px;top:1000px;font-size:20px;font-weight:600;color:#3355FF;white-space:nowrap;letter-spacing:1.4px;transform-origin:left top;transform:rotate(-90deg)}"
links=''.join(f"<div class='lk' style='left:600px;width:{ (1000 if 2<=i+1<=6 else 1030) - 600 }px;top:{cy-1}px;opacity:.0'></div>" for i,(_,_,cy) in enumerate(FL))
conn=f"<div class='lk' style='left:800px;top:394px;width:210px'></div><div class='lk' style='left:800px;top:1142px;width:210px'></div>"+"<div class='lk' style='left:800px;top:633px;width:215px'></div>"
Image.open(B+'content/ecommerce/fotos/etapas-fal-a.png').convert('RGB').resize((1500,1500),Image.LANCZOS).save(T+'etapas-fal.png')
H['02-ocho-etapas']=page(f"<div class='photo' style=\"background-image:url('file://{T}etapas-fal.png');background-size:100% 100%\"></div>")
H['03-sin-electricidad']=band('p03.png','Sin electricidad. Sin presión de caño.','Se llena con una jarra y purifica por gravedad.','center 30%')
rows=[(1,'r1.png','Quitas la tapa y llenas el tanque superior.'),(2,'r2.png','El agua se filtra por gravedad, a través de los filtros.'),(3,'r3.png','Sirves por la llave.')]
rr=''.join(f"<div class='row'><div class='rimg' style=\"background-image:url('file://{T}{p}')\"></div><div class='rn'>{n}</div><div class='rt'>{tx}</div></div>" for n,p,tx in rows)
EXTRA=".rows{position:absolute;left:70px;right:70px;top:270px}.row{display:flex;align-items:center;gap:40px;height:380px;margin-bottom:24px}.rimg{flex:0 0 560px;height:380px;border-radius:36px;background-size:cover;background-position:center;box-shadow:0 20px 50px rgba(1,10,33,.16)}.rn{flex:0 0 96px;height:96px;border-radius:50%;background:#3355FF;color:#fff;font-size:56px;font-weight:600;display:flex;align-items:center;justify-content:center}.rt{flex:1;font-size:50px;font-weight:500;line-height:1.12;letter-spacing:-.5px}"
H['04-asi-se-usa']=page(f"<div class='top'><div class='k'>Así se usa</div><h1>Tú, en 3 pasos</h1></div><div class='rows'>{rr}</div><div class='mark d' style='left:auto;right:90px'>elvo·</div>",EXTRA)
H['05-gotas-de-ph']=band('p05.png','Gotas de pH incluidas','Una gota en el vaso y comparas.','center 40%')
H['06-kit-de-filtros']=band('p06.png','10.000 litros o 1 año','El equipo ya trae su filtro. El kit de repuesto se vende aparte.','center 20%')
H['07-capacidad']=band('p07.png',f'{lit} litros',pers,'center 35%')
d1,d2=dims_h
x0,y0,x1,y1=BB
H['08-medidas']=page(bgp('med.png')+f"<div class='top' style='top:150px'><div class='k'>Medidas</div></div><div class='mark d'>elvo·</div><div class='line' style='left:{x1+50}px;top:{y0}px;width:6px;height:{y1-y0}px'></div><div class='dim' style='left:{x1+75}px;top:{(y0+y1)//2-30}px'>{d1}</div><div class='line' style='left:{x0}px;top:{y1+34}px;width:{x1-x0}px;height:6px'></div><div class='dim' style='left:{(x0+x1)//2-130}px;top:{y1+60}px'>{d2}</div>")
H['09-en-la-caja']=page(bgp('caja.png')+"<div class='top'><h1>En la caja</h1></div>")
H['10-agua-de-resguardo']=band('p10.png','Agua de resguardo en casa.','Sin electricidad y sin conexión al caño.','center 30%')
out=f'/tmp/ecom/alivio{M}'; os.makedirs(out,exist_ok=True)
for f in os.listdir(out): os.remove(out+'/'+f)
for k,h in H.items(): open(f'{out}/alivio{M}-{k}.html','w').write(h)
print(len(H))
