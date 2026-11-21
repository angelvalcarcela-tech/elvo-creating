import sys,threading;sys.path.insert(0,'.')
import gen_ml_vivo_v2 as v
R='refs-reales/'
def p(l): return ("BACKGROUND: vivid electric blue (#3355FF) with a soft light glow. The elvo· Alivio %s L bottle purifier from the FIRST reference, exactly as it is (same shape, scale and logo), large at the left. At the right, in front, the dropper bottle with black rubber cap and white label and a glass of clear water, like the SECOND reference, with a few small round color test swatches (yellow to teal) beside them. Headline white, huge, top-left: \"Incluye medidor de pureza.\" Under it in light blue: \"Gotas para medir tu agua, en la caja.\" Small 'elvo·' wordmark bottom-right. No other text, no warranty, no shipping."%l)
ths=[threading.Thread(target=v.call,args=('al16-medidor',['ml-portadas/elvo-alivio16-portada.jpg',R+'alivio-medidor-ph-tienda.png'],p('16'))),threading.Thread(target=v.call,args=('al22-medidor',['ml-portadas/elvo-alivio22-portada.jpg',R+'alivio-medidor-ph-tienda.png'],p('22')))]
[t.start() for t in ths];[t.join() for t in ths]
