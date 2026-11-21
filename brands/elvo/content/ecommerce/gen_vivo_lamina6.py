import sys;sys.path.insert(0,'.')
import gen_ml_vivo_v2 as v
from gen_ml_nativo_fal import R
p=("BACKGROUND: dramatic dark navy (#010A21) kitchen, softly blurred, with a cool electric-blue rim light. Premium macro product photo, 3/4 side view, of a modern straight chrome single-lever kitchen faucet spout (a DIFFERENT faucet from any previous: short straight spout, matte-chrome). "
"The elvo diverter valve is screwed directly onto the tip of the spout with NO gap, EXACTLY as in the references: the knurled ring on top is threaded onto the spout, the chrome body hangs below it, the BLACK teardrop lever on the front of the body, the hex hose fitting on the right side with a thin white tube leaving it. Only the lever is black, everything else chrome. "
"A hand turns the black lever with two fingers. Tiny sparkling water drops. No purifier and no other product in the scene. "
"TEXT on the left in white, huge and bold: \"Un giro.\" and below, smaller, electric blue: \"Del agua del caño al agua purificada.\" Small 'elvo·' wordmark bottom-right. Spanish spelled exactly, sharp. No competitor logos, no other text.")
v.call('v2-6f',[R+'derivador-colgado.jpg',R+'derivador-limpio.jpg'],p)
