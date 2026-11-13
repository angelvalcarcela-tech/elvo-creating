import base64,time,requests,sys,threading
B='/home/user/elvo-creating/brands/elvo/'
R=B+'brand-identity/product-references/web/'
def uri(p): return 'data:image/png;base64,'+base64.b64encode(open(p,'rb').read()).decode()
NAT=[B+'brand-identity/product-images/nativo-front.png',R+'vivo-instalacion-derivador.png',R+'vivo-instalacion-1-paso.png']
KIT=" Setting: the same bright, warm modern kitchen in every photo: light warm-stone counter, soft herringbone-tile backsplash, a window with green trees on the left, a plant and a wooden board blurred in the background, soft natural morning light, steel-blue and white palette. Premium, calm, photorealistic lifestyle photography, square 1:1, no text, no logos besides the product's."
NATP=" The elvo Nativo purifier must match the references exactly: white cylindrical body with the grey drop icon and 'elvo·' wordmark, curved chrome spout at its side, white base ring with latches. Installation: a small chrome diverter valve with a side lever screwed onto the end of the single kitchen faucet and ONE thin white flexible hose running from it to the purifier. Only one faucet. Clear colorless water."
J=[
('n2-hero',NAT,"A woman stands beside the kitchen counter drinking a glass of clear water with a relaxed smile. The elvo Nativo purifier stands on the counter right next to her, LARGE and bright (about a third of the image height), fully visible, its chrome spout and the white hose to the faucet at the right."+NATP+KIT),
('n2-servir',NAT,"Medium close-up of the elvo Nativo on the kitchen counter, large in the frame, a thin stream of clear water falling from its chrome spout into a clear glass; the faucet with the chrome diverter and the white hose are visible at the right. No people, no hands."+NATP+KIT),
('n2-cuerpo',NAT,"Close-up of the white body of the elvo Nativo purifier filling most of the frame, showing the grey drop icon and the 'elvo·' wordmark crisply, with the chrome spout partly visible at its side; the warm kitchen softly blurred behind. No hands, no extra objects."+NATP+KIT),
('n2-sin-obras',NAT,"A woman sets the elvo Nativo purifier down on the kitchen counter with both hands and smiles, no tools, no power cord anywhere, the bare tile wall behind her with no outlets; the faucet is clearly separate on the right and connected only by the thin white hose lying on the counter."+NATP+KIT),
('n2-nucleo',NAT+[B+'content/lote3/g3-nucleo_v1.png'],"Hands changing the core of the elvo Nativo: the upper body is lifted off with one hand, the PureCore filter cartridge visible on the base, a white plastic wrench lying beside it on the counter, a glass of water behind."+NATP+KIT),
('n2-filtro-llave',[R+'vivo-instalacion-derivador.png'],"A generic, unbranded small cylindrical water filter screwed directly onto the end of a chrome kitchen faucet, hanging from the faucet spout, water running through it into a glass in the sink; plain white and grey, no text, no logos, no brand."+KIT),
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
