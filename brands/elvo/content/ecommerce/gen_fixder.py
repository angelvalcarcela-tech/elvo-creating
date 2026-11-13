import base64,time,requests,sys,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'; R=B+'content/ecommerce/refs-reales/'
def uri(p):
    mt='image/jpeg' if p.endswith('.jpg') else 'image/png'
    return f'data:{mt};base64,'+base64.b64encode(open(p,'rb').read()).decode()
FIX=(" Edit this photo with MINIMAL changes. The kitchen faucet has a chrome diverter that is currently drawn WRONG: it sits halfway along the faucet neck. Correct it: the diverter must be screwed onto the VERY TIP of the faucet spout (the water outlet end) and HANG from it, exactly like in the reference image of the hanging diverter (second reference): knurled chrome ring at the TOP attached to the spout tip, the chrome body below with ONE black matte teardrop lever whose pointed tip points DOWN, a hexagonal nickel side nut with the thin WHITE hose connected to it, and a smooth chrome cap with a flat mesh aerator at the very BOTTOM. "
     "Make the rest of the faucet neck plain smooth chrome (no diverter, no lever or block along the neck). The white hose must run from the diverter's side nut to the elvo Nativo purifier as it already does. No exposed male thread at the bottom. "
     "Keep EVERYTHING else exactly identical: the person, hands, purifier (shape, drop icon, 'elvo·'), glass, water, counter, kitchen, lighting, framing and colors.")
REFS=lambda base:[base,R+'derivador-colgado.jpg',F+'instala6-b.png']
J=[('n3-hero',F+'n2-hero.png'),('n3-servir',F+'n2-servir.png'),
   ('n3-nucleo',F+'n2-nucleo.png')]
EXTRA={'n3-nucleo':" In this photo the faucet is at the LEFT of the image: put the diverter at the tip of that faucet's spout and make the white hose clearly run from the diverter's side nut across the counter to the purifier base (currently it disappears behind the faucet base)."}
def run(name,base):
    p=FIX+EXTRA.get(name,'')
    for t in range(3):
        try:
            r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(x) for x in REFS(base)],'image_size':{'width':1536,'height':1536},'quality':'high','num_images':1}); j=r.json()
            while True:
                time.sleep(10); s=requests.get(j['status_url']).json()
                if s.get('status')=='COMPLETED': break
                if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): raise Exception(str(s)[:200])
            u=requests.get(j['response_url']).json()['images'][0]['url']
            open(F+f'{name}.png','wb').write(requests.get(u).content); print('saved',name,flush=True); return
        except Exception as e: print('retry',name,e,flush=True)
ths=[threading.Thread(target=run,args=j) for j in J]
[t.start() for t in ths]; [t.join() for t in ths]; print('ALLDONE',flush=True)
