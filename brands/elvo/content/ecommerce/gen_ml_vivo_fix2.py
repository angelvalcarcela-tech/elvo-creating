import sys
sys.path.insert(0,'.')
from gen_ml_vivo_v2 import call,P,F
call('v2-5b',[P,F+'v2-5.png'],"Keep the same bold style as the second reference image (vivid electric blue background, faint large elvo· water-drop watermark, tower of translucent blue 20-liter jugs on the left, the purifier with a glass of water on the right, a bold white \"VS\" between them) but CHANGE THE LAYOUT AND TEXT exactly like this: the HUGE white headline at the top, very large, on two lines: \"Un núcleo rinde\" / \"40.000 litros.\" Directly under the tower of jugs, a clear white caption in two lines: \"2.000 bidones\" (bold, large) and \"de 20 litros\". Directly under the purifier, a clear white caption: \"1\" (very large, bold) and \"elvo· Vivo\" next to it. Footnote small at the bottom-left: \"En 36 meses de uso normal. Depende del consumo y de la calidad del agua.\" Small elvo· wordmark bottom-right. Do NOT show \"x2.000\" or \"x1\" anywhere.")
from PIL import Image
Image.open(F+'v2-5b.png').convert('RGB').resize((800,800)).save('/tmp/ml/v25b.png')
