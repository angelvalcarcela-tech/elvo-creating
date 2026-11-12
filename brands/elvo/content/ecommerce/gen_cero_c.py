import base64,time,requests,sys,threading
B='/home/user/elvo-creating/brands/elvo/'
def uri(p): return 'data:image/png;base64,'+base64.b64encode(open(p,'rb').read()).decode()
R=B+'brand-identity/product-references/'
CER=[B+'content/video-cero/v1-cero-solo.png',R+'cero-pantalla-real.png',R+'web/cero-jarra-a-la-mesa.png']
CEROP=" The elvo Cero must match the references exactly: white body, black touch screen with 'elvo·' wordmark at lower left; left of the screen the blue 'Filter Reset' and 'Pipe Cleaning' buttons, machine diagram with two circles on top, hand-tap icon; right of the screen the temperature, blue '−' and '+' volume buttons with ml, and a grid of 8 temperature tiles; silver dispensing button with blue light above the tray; removable 2-liter jug with handle on the front-left side; the tank is filled through a lid on the top-rear. No hoses, no plugs visible. Clear colorless water."
SQ=" Square 1:1 photograph, photorealistic lifestyle photography, bright natural light, steel-blue and white palette, calm premium feel, no text, no logos besides the product's. Keep the important subjects well inside the frame with generous margins."
J=[
('cero-08-caja-c',"The elvo Cero standing on a pale stone counter with its 2-liter jug INSTALLED in its bay on the front-left side of the machine (the jug is part of the purifier, NOT separate and NOT lying beside it); next to the machine only a small Spanish user manual booklet and a warranty card lying flat, and a plain brown cardboard shipping box softly blurred behind with only a tiny 'elvo·' wordmark and NO other text or slogan. Tidy, inviting unboxing mood."+CEROP+SQ),
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
