import os
F='/home/user/elvo-creating/brands/elvo/content/ecommerce/fotos/'; OUT='/tmp/nat9/h2'; os.makedirs(OUT,exist_ok=True)
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

body="<div class='ph' style=\"background-image:url('file://"+F+"aqa5-entrega.png')\"></div><div class='ts'></div><div class='top'><h1>Te llega a casa.</h1><p style='max-width:900px'>Lima: el mismo día si confirmas antes de las 4 p. m. Envío gratis a todo el Perú.</p></div><div class='mark'>elvo·</div><div class='bs'></div><div class='cap'>Yape, Plin, tarjeta en hasta 6 cuotas o al recibir (Lima)<small>Si no te convence, 30 días de prueba y te devolvemos tu dinero</small></div>"
open(OUT+'/nativo-p7.html','w').write("<html><head><meta charset='utf-8'><style>"+CSS+"</style></head><body>"+body+"</body></html>")
