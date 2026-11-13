import base64,time,requests,sys,threading
B='/home/user/elvo-creating/brands/elvo/'
R=B+'brand-identity/product-references/web/'
def uri(p): return 'data:image/png;base64,'+base64.b64encode(open(p,'rb').read()).decode()
NAT=[R+'vivo-que-incluye-la-caja.png',R+'vivo-instalacion-derivador.png',B+'brand-identity/product-images/nativo-front.png',B+'content/lote3/g3-nucleo_v1.png']
NATP=" The elvo Nativo purifier must match the references exactly: white cylindrical body with the grey drop icon and 'elvo·' wordmark, curved chrome spout at its side, white base ring. Photorealistic product photography, bright natural light, steel-blue and white palette, square 1:1, generous margins, no text, no logos besides the product's."
J=[
('nativo-09-caja',NAT,"The elvo Nativo purifier standing at the back center on a pale stone counter, and arranged neatly in front of it, each item clearly separated: a chrome diverter valve with a side lever, a coiled white flexible hose, a black rubber universal faucet adapter, a white plastic wrench, one PureCore filter cartridge, and a small user manual booklet. Nothing else, no box text."+NATP),
('nativo-10-grifos',[R+'vivo-instalacion-derivador.png'],"A clean grid of six round photographic frames (3 columns by 2 rows) on a soft steel-blue background, each frame showing a DIFFERENT kitchen faucet spout end in chrome: a curved gooseneck, a flat wide spout, a pull-out spray head, a straight tube, a flat rectangular spout, and a flexible black silicone spout. Same style as the six circles in the reference image but larger and sharper. No text, no logos."+" Photorealistic, square 1:1."),
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
ths=[threading.Thread(target=run,args=j) for j in J]
[t.start() for t in ths]; [t.join() for t in ths]; print('ALLDONE',flush=True)
