import base64,time,requests,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'; W=B+'brand-identity/product-references/web/'; R=B+'content/ecommerce/refs-reales/'
def uri(p):
    mt='image/jpeg' if p.endswith('.jpg') else 'image/png'
    return f'data:{mt};base64,'+base64.b64encode(open(p,'rb').read()).decode()
H22=W+'alivio-22l-hero.png'; COMP=R+'alivio-componentes.png'; PH=R+'alivio-medidor-ph-tienda.png'
BASE=(" Photorealistic premium lifestyle photograph for an ecommerce listing, bright natural window light, clean modern Lima apartment kitchen in whites, light wood and soft steel-blue tones, shallow depth of field, square 1:1. "
 "The purifier must match the reference exactly: the BOXY RECTANGULAR 22-liter model, white base with a transparent blue-tinted lower tank, an open transparent upper tank with the small white ceramic dome filter visible inside it, and a small black-and-chrome tap at the front; about 61 cm tall and 35 cm wide. NO text anywhere in the image, NO prices. Leave calm empty space at the top (about 20%) for a title overlay.")
J=[('a22-portada',[H22,PH],"Clean premium ecommerce studio product photograph, square 1:1. The BOXY RECTANGULAR 22-liter purifier from the first reference, shown large and centered (about 70 percent of the image height), front view, on a soft steel-blue (#9EBACE) to very light blue gradient background with a subtle floor reflection. In the lower-left foreground, small and at true scale, the small clear dropper bottle with black bulb and plain blank white label, next to a clear glass of water, exactly like the second reference (no swatches needed). Leave about 15 percent empty space at the top and 12 percent at the bottom for overlays. No text anywhere, no logo on the purifier except the existing embossed elvo mark on its base if the reference has it, no props other than the dropper bottle and glass.")]
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
