import base64,time,requests,sys,threading
B='/home/user/elvo-creating/brands/elvo/'
def uri(p): return 'data:image/png;base64,'+base64.b64encode(open(p,'rb').read()).decode()
R=B+'brand-identity/product-references/web/'
NAT=[R+'vivo-instalacion-derivador.png',B+'content/lote4/h1-nativo-cerca_v1.png',B+'brand-identity/product-images/nativo-front.png']
ALI=[B+'content/lote3/g1-alivio-botella_v1.png',B+'content/lote2/f11-alivio_v1.png',R+'alivio-armado.png']
SAFE=" COMPOSITION RULE (important, for a vertical social video with text added later): vertical 9:16 full-frame photograph; ALL important subjects (product, hands, glass) sit inside the central band between 15% and 62% of the image height and at least 10% away from the left and right edges; the top 12% is calm empty wall or ceiling; the bottom 35% is a calm, empty, out-of-focus counter or table surface with NO objects. Photorealistic lifestyle photography, bright natural light, steel-blue and white palette, no text, no logos other than those on the product."
NATP=" The elvo Nativo purifier must match the references exactly: white cylindrical body with the grey drop icon and 'elvo·' wordmark, curved chrome spout at its side, white base ring. Installation: chrome diverter with side lever on the end of the single kitchen faucet and ONE white hose to the purifier. Clear colorless water."
ALIP=" The elvo Alivio gravity purifier must match the references exactly: white dome lid, transparent upper tank with white ceramic filter element, transparent lower tank with multimedia filter column, small tap near the bottom, white base. NO logo on the product, no cables, no plugs, no connection to any tap. Clear colorless water."
J=[
('n1c-hook',NAT+[B+'content/lote1/r2d-vivo-cafe_v1.png'],"A woman drinks a glass of clear water standing right beside the elvo Nativo purifier on a kitchen counter. The Nativo is the clear HERO of the photo: large, bright, evenly lit, fully visible in the foreground next to her (about 30% of the image height), crisp white against a darker steel-blue wall behind it, with its grey drop icon, 'elvo·' wordmark, chrome spout, and the white hose running to the faucet at the right. She holds the glass, relaxed and refreshed."+NATP+SAFE),
('n9b-sin-obras',NAT,"The elvo Nativo purifier stands alone on the kitchen counter, a clean white cylinder with NOTHING protruding from its top; its single chrome spout is only on its lower side. A woman stands beside it with one hand resting on the counter, smiling at it, no tools, no cables. The kitchen faucet is clearly SEPARATE, on the far right behind the sink, connected to the purifier only by the thin white hose lying on the counter. Bare wall with no outlets."+NATP+SAFE),
]
def run(name,refs,p):
    for t in range(2):
        try:
            r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(x) for x in refs],'image_size':{'width':1152,'height':2048},'quality':'high','num_images':1}); j=r.json()
            while True:
                time.sleep(10); s=requests.get(j['status_url']).json()
                if s.get('status')=='COMPLETED': break
                if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): raise Exception(str(s)[:200])
            u=requests.get(j['response_url']).json()['images'][0]['url']
            open(B+f'content/lote11/{name}_v1.png','wb').write(requests.get(u).content); print('saved',name,flush=True); return
        except Exception as e: print('retry',name,e,flush=True)
sem=threading.Semaphore(2)
def w(job):
    with sem: run(*job)
ths=[threading.Thread(target=w,args=(j,)) for j in J]
[t.start() for t in ths]; [t.join() for t in ths]; print('ALLDONE',flush=True)
