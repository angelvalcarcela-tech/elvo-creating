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
('cero-02-fria-caliente-c',"The elvo Cero on a bright kitchen counter dispensing ordinary ROOM-TEMPERATURE water from its spout into a clear glass standing on its tray (plain water, no ice, no steam, screen showing 23 degrees). On the counter just to the right of the machine, already served and standing on the counter surface: a tall glass of cold water with ice cubes and, next to it, a ceramic cup of hot water with a gentle curl of steam. No people."+CEROP+SQ),
('cero-06-aviso-c',"Extreme close-up of the LEFT half of the elvo Cero's black touch screen, filling the frame: the wireframe diagram of the machine with the two circles on top glowing RED (filter change reminder), the small square indicators at the BACK of the diagram glowing blue (water tank) and the small square indicators at the FRONT near the jug glowing blue (jug has water), the 'Filter Reset' and 'Pipe Cleaning' buttons and the hand-tap icon visible. Shallow depth of field, a bright kitchen softly blurred behind. NO hands, NO filters, NO cartridges, nothing else in frame."+CEROP+SQ),
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
