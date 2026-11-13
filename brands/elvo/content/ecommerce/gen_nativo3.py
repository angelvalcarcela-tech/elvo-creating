import base64,time,requests,sys,threading
B='/home/user/elvo-creating/brands/elvo/'
R=B+'brand-identity/product-references/web/'
def uri(p): return 'data:image/png;base64,'+base64.b64encode(open(p,'rb').read()).decode()
NAT=[B+'brand-identity/product-images/nativo-front.png',R+'vivo-instalacion-derivador.png',R+'vivo-instalacion-1-paso.png']
KIT=" Setting: the same bright, warm modern kitchen in every photo: light warm-stone counter, soft herringbone-tile backsplash, a window with green trees on the left, a plant and a wooden board blurred in the background, soft natural morning light, steel-blue and white palette. Premium, calm, photorealistic lifestyle photography, square 1:1, no text, no logos besides the product's."
NATP=" The elvo Nativo purifier must match the references exactly: white cylindrical body with the grey drop icon and 'elvo·' wordmark, curved chrome spout at its side, white base ring with latches. Installation: a small chrome diverter valve with a side lever screwed onto the end of the single kitchen faucet and ONE thin white flexible hose running from it to the purifier. Only one faucet. Clear colorless water."
J=[
('n2-conecta',NAT,"Close-up of a woman's hands screwing the small chrome diverter valve with a side lever onto the end of the kitchen faucet by hand, no tools; the thin white flexible hose already attached to the diverter and leading across the counter to the elvo Nativo purifier standing on the counter in the background, softly out of focus but recognizable."+NATP+KIT),
]
def run(name,refs,p):
    for t in range(3):
        try:
            r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(x) for x in refs],'image_size':{'width':1536,'height':1536},'quality':'high','num_images':1}); j=r.json()
            while True:
                time.sleep(10); s=requests.get(j['status_url']).json()
                if s.get('status')=='COMPLETED': break
                if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): raise Exception(str(s)[:200])
            u=requests.get(j['response_url']).json()['images'][0]['url']
            open(B+f'content/ecommerce/fotos/{name}.png','wb').write(requests.get(u).content); print('saved',name,flush=True); return
        except Exception as e: print('retry',name,e,flush=True)
sem=threading.Semaphore(3)
def w(job):
    with sem: run(*job)
ths=[threading.Thread(target=w,args=(j,)) for j in J]
[t.start() for t in ths]; [t.join() for t in ths]; print('ALLDONE',flush=True)
