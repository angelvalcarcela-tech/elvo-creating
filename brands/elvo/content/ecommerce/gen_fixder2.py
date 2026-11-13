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
SERV=(" IMPORTANT SCENE RULES for this photo: there are TWO separate spouts. (1) The elvo Nativo purifier's OWN short curved chrome spout beside its white body, delivering water into the glass: keep it EXACTLY as in the original, short, with no diverter on it. (2) The tall chrome KITCHEN FAUCET standing at the RIGHT of the image beside the sink: it must remain visible; the diverter hangs from the very TIP of ITS spout (the downward-pointing outlet at the top of its arch), and the white hose runs from the diverter's side nut down and across the counter to the purifier. The purifier spout and the kitchen faucet must stay two different objects, not merged.")
NUC=(" IMPORTANT SCENE RULES for this photo: the tall chrome KITCHEN FAUCET is at the LEFT of the image, with an arch at its top; its water outlet tip is at the end of that arch. Hang the diverter from the very TIP of that arch outlet (screwed onto the end of the spout, below the arch end), NOT on the vertical neck. The long vertical neck of the faucet below the arch must be plain smooth chrome. The white hose runs from the diverter's side nut, down behind the faucet and along the counter to the base of the purifier, clearly visible. The purifier's own short spout stays exactly as in the original, with no diverter. Keep the hands, the opened purifier with the PureCore cartridge, the glass and the white wrench exactly as they are.")
J=[('n4-servir-a',F+'n2-servir.png',SERV),('n4-servir-b',F+'n2-servir.png',SERV),
   ('n4-nucleo-a',F+'n2-nucleo.png',NUC),('n4-nucleo-b',F+'n2-nucleo.png',NUC)]
def run(name,base,extra):
    p=FIX+extra
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
