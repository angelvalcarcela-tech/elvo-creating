import os
F='/home/user/elvo-creating/brands/elvo/content/ecommerce/fotos/'; OUT='/tmp/ml/tamh'; os.makedirs(OUT,exist_ok=True)
for f in os.listdir(OUT): os.remove(OUT+'/'+f)
CSS="""*{box-sizing:border-box;margin:0}body{width:1500px;height:1500px;font-family:'Inter',sans-serif;color:#010A21;position:relative;overflow:hidden}
.ph{position:absolute;inset:0;background-size:cover;background-position:center}
.ts{position:absolute;left:0;right:0;top:0;height:300px;background:linear-gradient(to bottom,rgba(255,255,255,.93),rgba(255,255,255,0))}
.top{position:absolute;left:70px;right:70px;top:70px}.top h1{font-weight:500;font-size:84px;letter-spacing:-1.8px;white-space:nowrap}
.mark{position:absolute;right:70px;top:78px;font-weight:600;font-size:54px}
.v{position:absolute;width:4px;background:#010A21;box-shadow:0 0 0 2px rgba(255,255,255,.75)}.h{position:absolute;height:4px;background:#010A21;box-shadow:0 0 0 2px rgba(255,255,255,.75)}
.tv{position:absolute;width:34px;height:4px;background:#010A21;box-shadow:0 0 0 2px rgba(255,255,255,.75)}.th{position:absolute;width:4px;height:34px;background:#010A21;box-shadow:0 0 0 2px rgba(255,255,255,.75)}
.dm{position:absolute;background:#fff;border-radius:99px;padding:12px 26px;font-size:38px;font-weight:700;box-shadow:0 8px 24px rgba(1,10,33,.3);white-space:nowrap}.dm small{font-size:26px;font-weight:500;color:#46566f;margin-right:8px}
.pill{position:absolute;left:70px;top:178px;background:#fff;border-radius:99px;padding:16px 38px;box-shadow:0 14px 40px rgba(1,10,33,.28);font-size:44px;font-weight:600;white-space:nowrap}.pill b{color:#3355FF}.pill span{font-weight:500;font-size:34px;margin-left:10px}
"""
def page(img,x0,x1,y0,y1,lit,pers,alto,base,labx):
    vx=x0-60
    cot=(f"<div class='v' style='left:{vx}px;top:{y0}px;height:{y1-y0}px'></div><div class='tv' style='left:{vx-15}px;top:{y0}px'></div><div class='tv' style='left:{vx-15}px;top:{y1}px'></div>"
         f"<div class='dm' style='left:{labx}px;top:{(y0+y1)//2-30}px'><small>Alto</small>{alto}</div>"
         f"<div class='h' style='left:{x0}px;top:{y1+44}px;width:{x1-x0}px'></div><div class='th' style='left:{x0}px;top:{y1+29}px'></div><div class='th' style='left:{x1}px;top:{y1+29}px'></div>"
         f"<div class='dm' style='left:{(x0+x1)//2-190}px;top:{y1+66}px;width:380px;text-align:center'><small>Base</small>{base}</div>")
    return (f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='ph' style=\"background-image:url('file://{F}{img}.png')\"></div><div class='ts'></div>"
            f"<div class='top'><h1>Mira si cabe en tu cocina.</h1></div><div class='mark' style='display:none'>elvo·</div>{cot}<div class='pill'><b>{lit} litros</b><span>{pers}</span></div></body></html>")
open(OUT+'/tamano-16.html','w').write(page('tam-16',533,917,300,1180,'16','· para 1 o 2 personas','62 cm','35 × 31 cm',215))
open(OUT+'/tamano-22.html','w').write(page('tam-22',538,1015,322,1300,'22','· para 3 o más personas','61 cm','35 × 23,5 cm',195))
