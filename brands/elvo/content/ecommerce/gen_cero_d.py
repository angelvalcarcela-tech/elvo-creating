import base64,time,requests,sys,threading
B='/home/user/elvo-creating/brands/elvo/'
def uri(p): return 'data:image/png;base64,'+base64.b64encode(open(p,'rb').read()).decode()
R=B+'brand-identity/product-references/'
CER=[B+'content/video-cero/v1-cero-solo.png',R+'cero-pantalla-real.png',R+'web/cero-jarra-a-la-mesa.png']
CEROP=" The elvo Cero must match the references exactly: white body, black touch screen with 'elvo·' wordmark at lower left; left of the screen the blue 'Filter Reset' and 'Pipe Cleaning' buttons, machine diagram with two circles on top, hand-tap icon; right of the screen the temperature, blue '−' and '+' volume buttons with ml, and a grid of 8 temperature tiles; silver dispensing button with blue light above the tray; removable 2-liter jug with handle on the front-left side; the tank is filled through a lid on the top-rear. No hoses, no plugs visible. Clear colorless water."
SQ=" Square 1:1 photograph, photorealistic lifestyle photography, bright natural light, steel-blue and white palette, calm premium feel, no text, no logos besides the product's. Keep the important subjects well inside the frame with generous margins."
R3=B+'brand-identity/product-references/'
CER=[B+'content/video-cero/v1-cero-solo.png',R+'cero-pantalla-real.png',R3+'cero-pantalla-panel-izq.png']
J=[
('cero-06-aviso-d',"MACRO photograph taken from 25 cm away: the camera is filled almost entirely by the left two thirds of the elvo Cero's black touch screen and nothing else. Visible: the wireframe diagram of the machine large in the center, its two circles on top glowing RED, the small square indicators at the BACK of the diagram glowing blue and the small square indicators at the FRONT near the jug glowing blue, plus the blue 'Filter Reset' and 'Pipe Cleaning' buttons and the hand-tap icon at the left edge. The screen occupies at least 85% of the image; only a thin strip of the white body frame and a blurred bright kitchen at the very edges. NO glass, NO cup, NO hands, NO filters, NO tray, NO spout in the frame."+CEROP+SQ),
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
