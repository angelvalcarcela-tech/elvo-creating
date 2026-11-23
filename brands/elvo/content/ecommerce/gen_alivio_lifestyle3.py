import sys,threading;sys.path.insert(0,'.')
import gen_ml_vivo_v2 as v
RULE=(" CRITICAL: the purifier must look EXACTLY like the reference (a plain white-and-clear plastic purifier). It has NO logo and NO text of any kind printed on it: keep every surface of the purifier completely blank. The tap is the small white-and-chrome spigot at the front of the base. Whenever water is poured, a real continuous stream of water visibly falls from the spigot straight down into the glass, and the glass is held directly under the spigot; never pour from empty air. No box, no other products, no droppers, no loose parts.")
def med(l): return ("Photorealistic lifestyle photo, warm natural morning light, shallow depth of field, bright modern Peruvian home kitchen. The Alivio %s L purifier from the reference on the counter, full and sharp. A smiling Latina woman in her 30s holds a clear glass of water in her hand, relaxed, next to it (she is NOT pouring)."%l+RULE+" Text over a soft navy gradient band at the bottom: big bold white \"Incluye medidor de pureza.\" and smaller light-blue under it: \"Mide tu agua en casa.\" Tiny 'elvo·' wordmark bottom-right on the band only. No warranty, no shipping, no prices, no contact info.")
def caja(l): return ("Photorealistic lifestyle photo, warm natural light, shallow depth of field, bright modern home kitchen. The Alivio %s L purifier from the reference on the counter at left, full and sharp. A smiling man in his 40s holds a glass under the spigot and the water visibly flows from the spigot into the glass."%l+RULE+" At the right a clean semi-transparent white rounded panel with navy text: headline \"En la caja\" and a checklist with electric-blue check marks: \"Filtro cerámico\", \"Filtro multietapa\", \"Piedra mineral\", \"Medidor de pureza (gotas)\", \"Manual de uso\". The panel must not cover the man's face or the purifier. Tiny 'elvo·' wordmark bottom-right. No warranty, no shipping, no prices, no contact info.")
import os
J=[]
for l in ('16','22'):
    ref='/tmp/ref-al%s.jpg'%l
    for k,f in (('med',med),('caja',caja)):
        n='al%s-life3-%s'%(l,k)
        if not os.path.exists('fotos/'+n+'.png'): J.append((n,[ref],f(l)))
ths=[threading.Thread(target=v.call,args=j) for j in J]
[t.start() for t in ths];[t.join() for t in ths]
