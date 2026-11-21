import sys;sys.path.insert(0,'.')
import gen_ml_vivo_v2 as v
from gen_ml_nativo_fal import R
p=("Recreate EXACTLY the composition of the FIRST reference photo: macro photo of a chrome gooseneck kitchen faucet with a small chrome diverter valve attached under the spout, lever pointing left, a thin white hose leaving it to the right and another white hose sweeping down-left. Same camera angle, bright soft airy background. Keep the same layout: a solid electric blue (#3355FF) banner across the top with white text \"¡Cambia fácilmente a agua purificada!\", a curved electric-blue arrow pointing down at the lever, and at the bottom-left in electric blue bold text: \"PD: La primera vez que giras el derivador requiere un poco de fuerza para moverlo.\" "
"IMPORTANT: the diverter must be the elvo diverter shown in the SECOND reference (same shape) with NO 'pura' logo or any competitor text anywhere; engrave nothing, or a tiny 'elvo·'. Small 'elvo·' wordmark bottom-right. Spanish text spelled exactly, sharp and legible.")
v.call('v2-6c',['/tmp/ref-cambia.jpg',R+'derivador-limpio.jpg'],p)
