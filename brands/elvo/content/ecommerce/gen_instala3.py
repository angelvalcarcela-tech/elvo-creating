import base64,time,requests,sys,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'; R=B+'content/ecommerce/refs-reales/'
def uri(p):
    mt='image/jpeg' if p.endswith('.jpg') else 'image/png'
    return f'data:{mt};base64,'+base64.b64encode(open(p,'rb').read()).decode()
PROD=B+'brand-identity/product-images/nativo-front.png'
REFS=[R+'derivador-limpio.jpg',R+'derivador-y-adaptador.jpg',R+'derivador-instalado-2.jpg',F+'real-instala.png',PROD]
DER=(" CRITICAL DETAIL OF THE DIVERTER (copy the first two reference photos exactly): a chrome cylinder; a BLACK matte lever shaped like a long TEARDROP / leaf (narrow at the top, rounded wide bottom, NOT a T-shaped handle and NOT a rectangle) mounted on the front of the cylinder; a knurled chrome ring at the top screwed onto the faucet; and on ONE SIDE a hexagonal nickel nut with a thin WHITE flexible hose coming out of it. "
     "In every panel where the diverter appears the white hose must be visibly connected to that side nut.")
STYLE=(" Style of the elvo brand: premium, calm, bright; steel-blue and white with electric blue (#3355FF) numbered circles; clean sans-serif type like Inter; photorealistic. Square 1:1. ALL TEXT EXACTLY AS WRITTEN IN QUOTES, in Spanish, add no other words. No text over products or hands. The elvo Nativo must match the last reference: white cylinder, grey drop icon, 'elvo·' wordmark.")
BASE=("Premium installation infographic on a very light steel-blue background (#dbe7f0). Top-left: small blue uppercase kicker \"Así se instala\" and the large dark-navy title \"Tú, en 5 minutos\". Below, THREE tall arch-shaped photo panels side by side with a soft shadow, each with a numbered blue circle and a caption underneath on the plain background. "
 "Panel 1: close-up of a woman's hands screwing the chrome diverter onto the end of a chrome kitchen faucet, the white hose already attached to its side nut and hanging down; caption \"Conectas el derivador\". "
 "Panel 2: a bright modern kitchen counter with the elvo Nativo purifier and a thin stream of clear water falling from its chrome spout into a glass; caption \"Dejas correr el agua 5 min\". "
 "Panel 3: close-up of a finger pressing the black teardrop lever of the diverter installed on the faucet, the white hose running to the elvo Nativo purifier on the counter behind it; caption \"Mueves la palanca y sirves\". "
 "Bottom-left small \"elvo·\".")
J=[('instala3-a',BASE+DER+STYLE+" Kitchen: warm light stone counter, herringbone tile backsplash, window with green trees."),
   ('instala3-b',BASE+DER+STYLE+" Kitchen: bright white-and-steel-blue modern kitchen, soft daylight, a plant. Make the diverter large and sharp in panels 1 and 3.")]
def run(name,p):
    for t in range(3):
        try:
            r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(x) for x in REFS],'image_size':{'width':1536,'height':1536},'quality':'high','num_images':1}); j=r.json()
            while True:
                time.sleep(10); s=requests.get(j['status_url']).json()
                if s.get('status')=='COMPLETED': break
                if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): raise Exception(str(s)[:200])
            u=requests.get(j['response_url']).json()['images'][0]['url']
            open(F+f'{name}.png','wb').write(requests.get(u).content); print('saved',name,flush=True); return
        except Exception as e: print('retry',name,e,flush=True)
ths=[threading.Thread(target=run,args=j) for j in J]
[t.start() for t in ths]; [t.join() for t in ths]; print('ALLDONE',flush=True)
