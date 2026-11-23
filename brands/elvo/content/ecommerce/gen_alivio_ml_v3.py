import sys,threading;sys.path.insert(0,'.')
import gen_ml_vivo_v2 as v
def cap(l,ref):
    return ("BACKGROUND: very light steel-blue gradient, clean. ONLY the elvo· Alivio %s L purifier from the reference, exactly as it is (same shape, scale, logo), large at the left, soft shadow. NO other objects anywhere: no loose filters, no bottles, no boxes, no hands. At the right a clean white rounded panel with navy text: headline \"En la caja\" and a checklist with electric-blue check marks: \"Filtro cerámico\", \"Filtro multietapa\", \"Piedra mineral\", \"Gotas medidoras de pH\", \"Manual de uso\". Small 'elvo·' wordmark bottom-right. No warranty, no shipping, no prices, no contact info."%l)
def med(l,ref):
    return ("BACKGROUND: vivid electric blue (#3355FF) with a soft light glow. ONLY the elvo· Alivio %s L purifier from the reference, exactly as it is, large and centered-left. NO other objects: no dropper, no glass, no bottles. Headline white, huge, top: \"Incluye medidor de pH.\" Under it in light blue: \"Mide tu agua en casa.\" Small 'elvo·' wordmark bottom-right. No warranty, no shipping, no prices."%l)
J=[]
for l in ('16','22'):
    ref='ml-portadas/elvo-alivio%s-portada.jpg'%l
    J.append(('al%s-caja-v3'%l,[ref],cap(l,ref)));J.append(('al%s-med-v3'%l,[ref],med(l,ref)))
ths=[threading.Thread(target=v.call,args=j) for j in J]
[t.start() for t in ths];[t.join() for t in ths]
