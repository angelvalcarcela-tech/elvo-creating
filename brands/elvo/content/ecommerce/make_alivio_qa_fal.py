import os
F='/home/user/elvo-creating/brands/elvo/content/ecommerce/fotos/'; OUT='/tmp/ecom/aqafal'; os.makedirs(OUT,exist_ok=True)
for f in os.listdir(OUT): os.remove(OUT+'/'+f)
CSS="""*{box-sizing:border-box;margin:0}body{width:1500px;height:1500px;font-family:'Inter',sans-serif;color:#010A21;position:relative;overflow:hidden}
.ph{position:absolute;inset:0;background-size:cover;background-position:center}
.ts{position:absolute;left:0;right:0;top:0;height:46%;background:linear-gradient(to bottom,rgba(255,255,255,.93),rgba(255,255,255,0))}
.bs{position:absolute;left:0;right:0;bottom:0;height:38%;background:linear-gradient(to top,rgba(1,10,33,.82),rgba(1,10,33,0))}
.top{position:absolute;left:90px;right:90px;top:80px}.top h1{font-weight:500;font-size:96px;line-height:1.04;letter-spacing:-2px}.top p{font-size:44px;margin-top:14px;color:#2b3b55}
.mark{position:absolute;right:90px;top:84px;font-weight:600;font-size:54px}
.pills{position:absolute;left:70px;right:70px;bottom:70px;display:flex;gap:20px}.pill{flex:1;background:#fff;border-radius:34px;padding:26px 28px;box-shadow:0 14px 40px rgba(1,10,33,.25)}.pill b{display:flex;align-items:center;gap:16px;font-size:36px;font-weight:600;line-height:1.1}.pill i{flex:0 0 52px;height:52px;border-radius:50%;background:#3355FF;color:#fff;font-style:normal;font-size:30px;display:flex;align-items:center;justify-content:center}
.card b{display:block;font-size:68px;font-weight:600;color:#3355FF;letter-spacing:-1.5px}.card span{font-size:36px;font-weight:500}
.cap{position:absolute;left:90px;right:90px;bottom:70px;color:#fff;font-size:44px;font-weight:500;line-height:1.2}.cap small{display:block;font-size:34px;color:#cfe0f5;font-weight:400;margin-top:12px}
.chip{position:absolute;right:90px;top:100px;background:#3355FF;color:#fff;border-radius:99px;padding:20px 36px;font-size:34px;font-weight:500;text-align:center;line-height:1.15}
"""
def page(img,body): return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='ph' style=\"background-image:url('file://{F}{img}.png')\"></div>{body}</body></html>"
H={}
H['02-uso']=page('aqa2-uso-b',"<div class='ts'></div><div class='top'><h1>Sin luz.<br>Sin instalación.</h1><p>Llenas con una jarra y listo.</p></div><div class='mark'>elvo·</div><div class='bs'></div><div class='pills'>"+"".join(f"<div class='pill'><b><i>{n}</i>{t}</b></div>" for n,t in [(1,'Llenas el tanque'),(2,'Se filtra por gravedad'),(3,'Sirves por la llave')])+"</div>")
CT=".v{position:absolute;width:4px;background:#010A21;box-shadow:0 0 0 2px rgba(255,255,255,.7)}.h{position:absolute;height:4px;background:#010A21;box-shadow:0 0 0 2px rgba(255,255,255,.7)}.tv{position:absolute;width:34px;height:4px;background:#010A21;box-shadow:0 0 0 2px rgba(255,255,255,.7)}.th{position:absolute;width:4px;height:34px;background:#010A21;box-shadow:0 0 0 2px rgba(255,255,255,.7)}.dm{position:absolute;background:#fff;border-radius:99px;padding:12px 26px;font-size:36px;font-weight:700;box-shadow:0 8px 24px rgba(1,10,33,.3);white-space:nowrap;color:#010A21}.dm small{font-size:26px;font-weight:500;color:#46566f;margin-right:8px}"
def vcota(x,y0,y1,label,lx):
    return f"<div class='v' style='left:{x}px;top:{y0}px;height:{y1-y0}px'></div><div class='tv' style='left:{x-15}px;top:{y0}px'></div><div class='tv' style='left:{x-15}px;top:{y1}px'></div><div class='dm' style='left:{lx}px;top:{(y0+y1)//2-30}px'><small>Alto</small>{label}</div>"
def hcota(x0,x1,y,label):
    cx=(x0+x1)//2
    return f"<div class='h' style='left:{x0}px;top:{y}px;width:{x1-x0}px'></div><div class='th' style='left:{x0}px;top:{y-15}px'></div><div class='th' style='left:{x1}px;top:{y-15}px'></div><div class='dm' style='left:{cx-150}px;top:{y+16}px;width:300px;text-align:center'><small>Base</small>{label}</div>"
cotas=vcota(350,510,1255,'62 cm',205)+hcota(395,717,1272,'35 × 31 cm')+vcota(1225,500,1245,'61 cm',1245)+hcota(798,1178,1272,'35 × 23,5 cm')
pills="<div class='pills' style='bottom:24px'><div class='pill card' style='padding:14px 28px'><b style='font-size:48px;display:inline'>16 litros</b> <span style='font-size:32px'>· 1 o 2 personas</span></div><div class='pill card' style='padding:14px 28px'><b style='font-size:48px;display:inline'>22 litros</b> <span style='font-size:32px'>· 3 o más personas</span></div></div>"
H['03-tamano']=page('aqa3-tamano-d',"<div class='ts'></div><div class='top'><h1>Mira si cabe<br>en tu cocina.</h1></div>"+cotas+pills).replace("</style>",CT+"</style>")
H['05-entrega']=page('aqa5-entrega-c',"<div class='ts'></div><div class='top'><h1>Te llega a casa.</h1><p>Lima y Callao: envío gratis y pagas al recibir.</p></div><div class='mark'>elvo·</div><div class='bs'></div><div class='cap'>Provincia: recojo en Shalom, envío a domicilio o tarjeta<small>Envío S/15 · Shalom con adelanto de S/20</small></div>")
H['06-caja']=page('aqa6-caja-c',"<div class='ts'></div><div class='top'><h1>Todo en la caja.</h1><p style='max-width:900px;font-size:38px'>Equipo, filtro cerámico, filtro multietapa, piedra mineral, gotas de pH y manual.</p></div><div class='chip'>Garantía de<br>satisfacción de 30 días</div>")
for k,h in H.items(): open(f'{OUT}/aqafal-{k}.html','w').write(h)
