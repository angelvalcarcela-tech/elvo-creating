import base64,time,requests,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'
def uri(p):
    mt='image/jpeg' if p.endswith('.jpg') else 'image/png'
    return f'data:{mt};base64,'+base64.b64encode(open(p,'rb').read()).decode()
BRAND=(" elvo· brand identity: bright, airy, premium; soft steel-blue (#9EBACE) to very light blue (#dbe7f0) backgrounds with white, deep navy (#010A21) headlines and electric-blue (#3355FF) accents; clean Inter-like sans-serif; generous spacing; rounded corners and soft shadows; a small 'elvo·' wordmark in navy at a corner. Superior to a generic competitor ad: refined hierarchy, big confident headline, realistic product render with crisp reflections and soft contact shadow, 1:1 square ecommerce image. ALL TEXT EXACTLY AS WRITTEN, Spanish with correct accents, nothing else added. The purifier must look exactly like the first reference (white cylinder, grey water-drop icon, grey 'elvo' wordmark with its small drop, chrome swan-neck spout); NO other logos.")
J=[('mlv-vivo-hero',[F+'v9-vivo.png'],"Hero benefits image. Headline top-left in navy, large: \"Agua más rica, directo de tu caño.\" The purifier large on the right half, standing on a soft surface with a sparkling water stream filling a glass. Top-right a premium gold starburst seal reading \"#1\" and below it \"EN PURIFICADORES\" with five small stars. On the left under the headline four benefit rows, each with an electric-blue check circle, bold line then small grey line: \"Aporta magnesio al agua\" / \"Con tu caño de siempre\"; \"Reduce cloro, olores y sabores\" / \"Agua más rica en cada vaso\"; \"Rinde 20.000 litros\" / \"Unos 18 meses de uso normal\"; \"Para todo caño\" / \"Kit de adaptadores incluido\". Small footnote at the bottom: \"Los resultados dependen de la calidad del agua de entrada.\""+BRAND),
   ('mlv-vivo-etapas',[F+'v9-vivo.png',F+'etapas7-fal.png'],"Infographic: the purifier core shown as an elegant 3D cutaway cylinder in the center-right, with FOUR clearly distinct layers from top to bottom: ultrafiltration membrane (white-grey), solid activated carbon block (black), magnesium media (warm amber beads), microfiltration (white fine mesh); a single drop of water at the top and a smooth blue flow line passing down through them ending in clean droplets. Headline top-left navy: \"4 etapas, un solo núcleo.\" Subtitle grey: \"De arriba hacia abajo\". Labels on the left with electric-blue numbered circles, a bold line then a small grey line: 1 \"Ultrafiltración\" / \"Reduce cloro, sedimentos, olores y sabor\"; 2 \"Bloque de carbón activado\" / \"Cloro, sedimentos, mal sabor y olor\"; 3 \"Aporte de magnesio\" / \"Aporta magnesio al agua\"; 4 \"Microfiltración\" / \"Atrapa microplásticos, turbiedad y partículas finas\". Thin dotted leader lines. Footnote: \"Esquema ilustrativo. Los resultados dependen de la calidad del agua de entrada.\" No tap or faucet in the drawing."+BRAND),
   ('mlv-vivo-reduce',[F+'v9-vivo.png'],"Value image: lifestyle-premium scene, a bright modern kitchen counter, the purifier at left with a glass of crystal-clear water, and on the right a large elegant card listing what it does. Headline in navy: \"Qué hace el Vivo por tu agua.\" Card rows with electric-blue check circles: \"Cloro y derivados\" / \"Agua sin sabor a cloro\"; \"Olores y sabores\" / \"Para que dé gusto tomarla\"; \"Sedimentos y turbiedad\" / \"Agua más clara\"; \"Microplásticos y partículas finas\" / \"Microfiltración en el núcleo\"; then a highlighted electric-blue pill: \"Y además aporta magnesio\". Footnote: \"Pensado para agua de red potable. Los resultados dependen de la calidad del agua de entrada.\""+BRAND)]
def run(name,refs,p):
    for t in range(3):
        try:
            r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(x) for x in refs],'image_size':{'width':1536,'height':1536},'quality':'high','num_images':1}).json()
            if 'status_url' not in r: print('ERR',name,str(r)[:200],flush=True); return
            while True:
                time.sleep(10); s=requests.get(r['status_url']).json()
                if s.get('status')=='COMPLETED': break
                if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): raise Exception(str(s)[:200])
            u=requests.get(r['response_url']).json()['images'][0]['url']
            open(F+name+'.png','wb').write(requests.get(u).content); print('saved',name,flush=True); return
        except Exception as e: print('retry',name,e,flush=True)
ths=[threading.Thread(target=run,args=j) for j in J]; [t.start() for t in ths]; [t.join() for t in ths]
from PIL import Image
W=Image.new('RGB',(2250,750))
for i,(n,_,_) in enumerate(J):
    try: W.paste(Image.open(F+n+'.png').convert('RGB').resize((750,750)),(i*750,0))
    except Exception as e: print(n,e)
W.save('/tmp/ml/vivo_fal.png')
