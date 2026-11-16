import base64,time,requests,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'; W=B+'brand-identity/product-references/web/'; R=B+'content/ecommerce/refs-reales/'
def uri(p):
    mt='image/jpeg' if p.endswith('.jpg') else 'image/png'
    return f'data:{mt};base64,'+base64.b64encode(open(p,'rb').read()).decode()
H16=W+'alivio-16l-hero.png'; H22=W+'alivio-22l-hero.png'; COMP=R+'alivio-componentes.png'; CAJA='/tmp/ecom/a16/caja.png'
BASE=(" Photorealistic premium lifestyle photograph for an ecommerce listing, bright natural window light, clean modern Lima apartment kitchen in whites, light wood and soft steel-blue tones, shallow depth of field, square 1:1. "
 "The product must match the reference exactly: a white gravity water purifier with a transparent tank, a white ceramic dome filter on top and a small black tap/lever at the front. NO logo or brand text on the product, NO text anywhere in the image, NO prices. Leave calm empty space at the top (about 20%) for a title overlay.")
BOX=R+'alivio-caja-real.jpg'
PH=R+'alivio-medidor-ph-tienda.png'
J=[('aqa11-ph',[PH,H16],"Close-up on a bright kitchen counter: a hand holds the small glass dropper bottle (same bottle as in the first reference: clear glass, black rubber bulb) over a clear glass of water on the counter and a single drop is falling into the water; next to the glass sit a few small round color swatches in yellow, green and blue-green like in the reference. The purifier is softly blurred in the background. Clean, simple, easy-to-understand mood. NO text on swatches."+BASE)]
def run(name,refs,p):
    for t in range(3):
        try:
            r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(x) for x in refs],'image_size':{'width':1536,'height':1536},'quality':'high','num_images':1}); j=r.json()
            if 'status_url' not in j: print('ERR',name,str(j)[:200],flush=True); return
            while True:
                time.sleep(10); s=requests.get(j['status_url']).json()
                if s.get('status')=='COMPLETED': break
                if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): raise Exception(str(s)[:200])
            u=requests.get(j['response_url']).json()['images'][0]['url']
            open(F+f'{name}.png','wb').write(requests.get(u).content); print('saved',name,flush=True); return
        except Exception as e: print('retry',name,e,flush=True)
ths=[threading.Thread(target=run,args=j) for j in J]
[t.start() for t in ths]; [t.join() for t in ths]; print('ALLDONE',flush=True)
