import sys,threading;sys.path.insert(0,'.')
import gen_ml_vivo_v2 as v
def med(l): return ("Photorealistic lifestyle photo, warm natural morning light, shallow depth of field, bright modern Peruvian home kitchen. The elvo· Alivio %s L bottle purifier from the reference, EXACTLY as it is (same shape, proportions, logo), on the counter, full and sharp. A smiling Latina woman in her 30s holds a clear glass of water up with satisfaction next to it. No other products, no bottles, no droppers, no boxes. Clear readable text over a soft navy gradient band at the bottom: big bold white \"Incluye medidor de pureza.\" and smaller light-blue under it: \"Mide tu agua en casa.\" Tiny 'elvo·' wordmark bottom-right. No warranty, no shipping, no prices, no contact info."%l)
def caja(l): return ("Photorealistic lifestyle photo, warm natural light, shallow depth of field, bright modern home kitchen. The elvo· Alivio %s L bottle purifier from the reference, EXACTLY as it is (same shape, proportions, logo), on the counter at left, full and sharp. A smiling man in his 40s pours a glass of water from its tap. No other products, no loose parts, no boxes. At the right a clean semi-transparent white rounded panel with navy text: headline \"En la caja\" and a checklist with electric-blue check marks: \"Filtro cerámico\", \"Filtro multietapa\", \"Piedra mineral\", \"Medidor de pureza (gotas)\", \"Manual de uso\". Tiny 'elvo·' wordmark bottom-right. No warranty, no shipping, no prices, no contact info."%l)
J=[]
for l in ('16','22'):
    ref='ml-portadas/elvo-alivio%s-portada.jpg'%l
    J.append(('al%s-life2-med'%l,[ref],med(l)));J.append(('al%s-life2-caja'%l,[ref],caja(l)))
ths=[threading.Thread(target=v.call,args=j) for j in J]
[t.start() for t in ths];[t.join() for t in ths]
