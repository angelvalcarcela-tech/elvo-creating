import sys,threading;sys.path.insert(0,'.')
import gen_ml_vivo_v2 as v
def a(l): return ("Photorealistic lifestyle photo, warm natural morning light, shallow depth of field, bright modern Peruvian home kitchen. The elvo· Alivio %s L bottle purifier from the reference, EXACTLY as it is (same shape, proportions, logo), standing on the kitchen counter in the foreground-left, full and sharp. A smiling Latina woman in her 30s fills a clear glass from its tap, a child in the soft background reaching for a glass. No other products, no boxes, no loose parts. Small complementary text, elegant white or navy sans-serif, bottom-left: \"Agua pura para toda la familia.\" and a small line under it: \"Incluye filtros y medidor de pH.\" Tiny 'elvo·' wordmark bottom-right. No warranty, no shipping, no prices, no contact info."%l)
def b(l): return ("Photorealistic lifestyle photo, golden morning light, shallow depth of field, cozy modern home kitchen. The elvo· Alivio %s L bottle purifier from the reference, EXACTLY as it is (same shape, proportions, logo), on the counter at right, full and sharp. A relaxed man in his 40s leaning on the counter drinking a glass of clear water with a satisfied smile, a bowl of fruit nearby. No other products, no bottles, no boxes. Small complementary text, white sans-serif, top-left: \"Sin luz. Sin instalación.\" and under it: \"Con piedra mineral y medidor de pH.\" Tiny 'elvo·' wordmark bottom-right. No warranty, no shipping, no prices, no contact info."%l)
J=[]
for l in ('16','22'):
    ref='ml-portadas/elvo-alivio%s-portada.jpg'%l
    J.append(('al%s-life-a'%l,[ref],a(l)));J.append(('al%s-life-b'%l,[ref],b(l)))
ths=[threading.Thread(target=v.call,args=j) for j in J]
[t.start() for t in ths];[t.join() for t in ths]
