import base64,time,requests,sys,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'; R=B+'content/ecommerce/refs-reales/'
def uri(p):
    mt='image/jpeg' if p.endswith('.jpg') else 'image/png'
    return f'data:{mt};base64,'+base64.b64encode(open(p,'rb').read()).decode()
PROD=B+'brand-identity/product-images/nativo-front.png'
REFS=[F+'real2-caja.png',PROD,R+'derivador-limpio.jpg']
P=("Edit this flat-lay photo with MINIMAL changes. Currently the elvo Nativo purifier body and its curved chrome dispensing spout are drawn as TWO separate items. Make them ONE single assembled item: the purifier standing with its curved chrome spout ATTACHED to the base ring at its side, exactly as in the second reference (the product photo): white cylinder, grey drop icon, 'elvo·' wordmark, white base ring, spout curving up and over at the side. Remove the separate spout lying alone. "
   "Re-space the remaining items evenly along the same row so there is no big gap: purifier with spout, PureCore filter cartridge, chrome diverter, coiled white hose, black rubber universal adapter, white plastic wrench, white sealing washer with black ring, small white manual. Keep each item separate, not touching others. Keep the diverter, adapter, hose, wrench, manual, cartridge, background, title \"En la caja\" and lighting exactly as they are. "
   "Replace the small grey caption line under the objects with EXACTLY this text, in Spanish with correct accents: \"Purificador con caño · Núcleo · Derivador · Manguera · Adaptador de jebe · Llave · Manual\". Keep the small \"elvo·\" at the bottom-left. Add no other text.")
J=[('caja2-a',P),('caja2-b',P+" Make sure the purifier with its spout is the largest, clearly visible item at the left of the row.")]
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
