import os
OUT='/tmp/ml/rieg'
CSS="""*{box-sizing:border-box;margin:0}body{width:1500px;height:1500px;font-family:'Inter',sans-serif;color:#010A21;background:#dbe7f0;position:relative;overflow:hidden}
.k{position:absolute;left:90px;top:84px;font-size:34px;font-weight:600;color:#3355FF;letter-spacing:.5px;text-transform:uppercase}
h1{position:absolute;left:90px;top:130px;font-weight:500;font-size:112px;line-height:1.02;letter-spacing:-2.5px}
.mark{position:absolute;right:90px;top:84px;font-weight:600;font-size:54px}
.grid{position:absolute;left:70px;right:70px;top:430px;display:grid;grid-template-columns:1fr 1fr;gap:28px;grid-auto-rows:480px}
.c{background:#fff;border-radius:40px;padding:44px 42px;box-shadow:0 20px 50px rgba(1,10,33,.12);min-height:0}
.c i{display:flex;width:96px;height:96px;border-radius:50%;background:#3355FF;color:#fff;font-style:normal;font-size:54px;font-weight:600;align-items:center;justify-content:center;margin-bottom:34px}
.c b{display:block;font-size:60px;font-weight:600;letter-spacing:-1px;line-height:1.05}.c span{display:block;font-size:38px;margin-top:14px;color:#46566f;line-height:1.25}
"""
def page(title,cards):
    c=''.join(f"<div class='c'><i>✓</i><b>{a}</b><span>{b}</span></div>" for a,b in cards)
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='k'>Compra tranquilo</div><div class='mark'>elvo·</div><h1>{title}</h1><div class='grid'>{c}</div></body></html>"
alivio=[('30 días de prueba','Si no te convence, te devolvemos tu dinero.'),('6 meses de garantía','Cubre fallas de fábrica del equipo.'),('Pagas al recibir','En Lima y Callao. También Yape o tarjeta.'),('Te llega rápido','Lima: hoy si confirmas antes de las 4 p. m. (lun. a sáb.).')]
nativo=[('30 días de prueba','Si no te convence, te devolvemos tu dinero.'),('1 año de garantía','Cubre fallas de fábrica del equipo.'),('Si no encaja, devolución','Si no se adapta a tu caño, te devolvemos tu dinero.'),('Pagas como prefieras','Al recibir en Lima, Yape, Plin o tarjeta en cuotas.')]
open(OUT+'/compra-alivio.html','w').write(page('Compra<br>sin riesgo.',alivio))
open(OUT+'/compra-nativo.html','w').write(page('Compra<br>sin riesgo.',nativo))
