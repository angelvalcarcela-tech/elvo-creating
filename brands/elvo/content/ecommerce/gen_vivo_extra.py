import sys,threading;sys.path.insert(0,'.')
import gen_ml_vivo_v2 as v
from gen_ml_nativo_fal import R
SP=" The purifier's chrome spout rises IN FRONT of the white body from the lower-front base and arcs to the LEFT, tip pointing left and down, as in the reference."
j8=("BACKGROUND: deep navy. The giant numeral \"36\" in white, enormous, at the center-left, with \"meses\" in electric blue next to it. At the right ONLY the purifier standing alone (no filter core, no spare part anywhere in the image)."+SP+" Headline at the bottom white: \"Un solo cambio de núcleo cada 3 años.\" Small line: \"Sin herramientas, lo cambias tú.\" Footnote small: \"36 meses de uso normal. Depende de la calidad del agua de entrada.\"")
jk=("BACKGROUND: bright, warm, real Peruvian home kitchen photo, soft morning light, shallow depth of field. The white elvo Vivo purifier stands on the kitchen counter next to the sink and a common chrome faucet; a thin white hose runs from the faucet diverter to the purifier."+SP+" A glass is being filled with water from the purifier spout (water falling at the left of the body). A jug and a bowl of fruit in the soft background. Top-left headline in navy, big: \"Agua purificada, en tu cocina.\" Small line under it in electric blue: \"Sin obras. Sin instalación.\" Small 'elvo·' wordmark bottom-right. No other text, no competitor logos.")
ths=[threading.Thread(target=v.call,args=('v2-8b',[v.P],j8)),threading.Thread(target=v.call,args=('v2-10',[v.P,R+'derivador-colgado.jpg'],jk))]
[t.start() for t in ths];[t.join() for t in ths]
