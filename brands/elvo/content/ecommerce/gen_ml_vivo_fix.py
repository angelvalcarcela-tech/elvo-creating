import threading,sys
sys.path.insert(0,'.')
from gen_ml_vivo_v2 import call,P
J=[('v2-2',[P],"BACKGROUND: solid vivid electric blue. A giant white periodic-table style tile at the left reading \"Mg\" with \"12\" small in the corner and \"Magnesio\" under it, elegant and bold. On the right the purifier with a glass of crystal-clear water. Headline in white at the bottom, large: \"Vivo aporta magnesio.\" Small line: \"Magnesio en tu agua, directo de tu caño.\" Footnote small: \"Los resultados dependen de la calidad del agua de entrada.\""),
('v2-9',[P],"BACKGROUND: light, clean. Headline navy, huge, top-left: \"Vivo vs. lo de siempre.\" Below it a single wide, clean comparison card spanning the lower two thirds of the image, with the purifier standing OUTSIDE the card at the far left. The card has THREE columns: a first column of row labels in navy text (\"Aporta magnesio\", \"Agua al instante, sin cargar\", \"Mantenimiento\"), a second column highlighted in electric blue titled \"elvo· Vivo\" with white check marks in the first two rows and the text \"Núcleo cada 36 meses\" in the third, and a third white column titled \"Bidón o hervir\" with dark crosses in the first two rows and \"Recarga cada semana o gas diario\" in the third. Row labels must NOT overlap the product. Footnote small: \"Comparación con alternativas comunes.\"")]
ths=[threading.Thread(target=call,args=j) for j in J]; [t.start() for t in ths]; [t.join() for t in ths]
from PIL import Image
W=Image.new('RGB',(1500,750))
for i,(n,_,_) in enumerate(J): W.paste(Image.open('fotos/'+n+'.png').convert('RGB').resize((750,750)),(i*750,0))
W.save('/tmp/ml/vfix.png')
