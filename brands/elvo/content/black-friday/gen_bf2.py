import sys;sys.path.insert(0,'.')
import threading
import importlib.util
spec=importlib.util.spec_from_file_location('g','gen_bf.py')
src=open('gen_bf.py').read().split("E='../ecommerce/'")[0]
exec(src)
RULE=(" 4:5 vertical Instagram slide. The PHOTO is the hero and fills the ENTIRE frame edge to edge, full-bleed; the product is large, sharp and clearly the first thing you see. Keep the photo, the product and the scene EXACTLY as in the reference image (same composition, same product, same water stream, same light). REMOVE the large navy band and the huge headline. Text must be secondary and small: only ONE discreet line in the bottom-left corner over a very soft dark gradient that covers no more than 9% of the image height, in clean white sans-serif at small size (about 3% of the image height), no big numbers, no coloured panels. Text spelled exactly. A tiny 'elvo·' wordmark bottom-right in white. No exclamation marks, no extra text. ")
J2=[
('bf1b',['fotos/bf1.png'],"COVER. Keep the three products on the stone counter with their glasses and the navy-blue glow EXACTLY as in the reference, products large and dominant. Make the text much smaller: replace the huge \"Black Days\" headline with a small white title top-left at about 4% of image height: \"Black Days\", and under it in smaller light-blue text \"Tres formas de tener agua pura en casa.\" No pill, no big text. The products must clearly dominate the image. A tiny 'elvo·' bottom-right. Spanish spelled exactly."),
('bf2b',['fotos/bf2.png'],"SLIDE Nativo."+RULE+"The one line reads: \"Nativo · desde S/ 299\"."),
('bf3b',['fotos/bf3.png'],"SLIDE Alivio."+RULE+"The one line reads: \"Alivio · desde S/ 159\". The purifier stays completely blank with no logo."),
('bf4b',['fotos/bf4.png'],"SLIDE Cero."+RULE+"The one line reads: \"Cero · S/ 1,990\"."),
]
ths=[threading.Thread(target=call,args=j) for j in J2]
[t.start() for t in ths];[t.join() for t in ths]
