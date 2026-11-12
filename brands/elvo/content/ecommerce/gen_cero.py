import base64,time,requests,sys,threading
B='/home/user/elvo-creating/brands/elvo/'
def uri(p): return 'data:image/png;base64,'+base64.b64encode(open(p,'rb').read()).decode()
R=B+'brand-identity/product-references/'
CER=[B+'content/video-cero/v1-cero-solo.png',R+'cero-pantalla-real.png',R+'web/cero-jarra-a-la-mesa.png']
CEROP=" The elvo Cero must match the references exactly: white body, black touch screen with 'elvo·' wordmark at lower left; left of the screen the blue 'Filter Reset' and 'Pipe Cleaning' buttons, machine diagram with two circles on top, hand-tap icon; right of the screen the temperature, blue '−' and '+' volume buttons with ml, and a grid of 8 temperature tiles; silver dispensing button with blue light above the tray; removable 2-liter jug with handle on the front-left side; the tank is filled through a lid on the top-rear. No hoses, no plugs visible. Clear colorless water."
SQ=" Square 1:1 photograph, photorealistic lifestyle photography, bright natural light, steel-blue and white palette, calm premium feel, no text, no logos besides the product's. Keep the important subjects well inside the frame with generous margins."
J=[
('cero-02-fria-caliente',"The elvo Cero on a bright kitchen counter, just finished serving: on its tray a tall glass of cold clear water with ice cubes and beside it a ceramic cup of hot water with a gentle curl of steam; nobody in frame; soft window light."+CEROP+SQ),
('cero-05-jarra-mesa',"A woman carries the removable 2-liter jug full of clear water from the elvo Cero (on the kitchen counter behind her, its left jug bay now empty) toward a dining table set for lunch where a family waits, warm home atmosphere."+CEROP+SQ),
('cero-07-filtros',"Close-up of the elvo Cero screen where the two circles on the machine diagram glow RED as a filter-change reminder; in the foreground, softly out of focus, a hand holds two new water filter cartridges (one labelled PAC and one labelled ROC)."+CEROP+SQ),
('cero-08-caja',"The elvo Cero standing on a pale stone counter; beside it its removable 2-liter jug, a small Spanish user manual booklet and a warranty card lying flat, and a cardboard shipping box softly blurred behind. Tidy, inviting unboxing mood."+CEROP+SQ),
('cero-09-oficina',"A modern office kitchenette: the elvo Cero on a light counter, two colleagues chatting, one holding a cup that was just filled with hot water; bright office with large window, no water bottles or dispenser jugs anywhere."+CEROP+SQ),
]
def run(name,p):
    for size in ((1536,1536),(1152,1152),(1152,1152)):
        try:
            r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(x) for x in CER],'image_size':{'width':size[0],'height':size[1]},'quality':'high','num_images':1}); j=r.json()
            while True:
                time.sleep(10); s=requests.get(j['status_url']).json()
                if s.get('status')=='COMPLETED': break
                if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): raise Exception(str(s)[:200])
            u=requests.get(j['response_url']).json()['images'][0]['url']
            open(B+f'content/ecommerce/fotos/{name}.png','wb').write(requests.get(u).content); print('saved',name,size,flush=True); return
        except Exception as e: print('retry',name,size,e,flush=True)
sem=threading.Semaphore(3)
def w(job):
    with sem: run(*job)
ths=[threading.Thread(target=w,args=(j,)) for j in J]
[t.start() for t in ths]; [t.join() for t in ths]; print('ALLDONE',flush=True)
