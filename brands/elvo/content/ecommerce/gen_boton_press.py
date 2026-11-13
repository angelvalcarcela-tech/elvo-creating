import base64,time,requests,sys
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'; R=B+'brand-identity/product-references/'
def uri(p): return 'data:image/png;base64,'+base64.b64encode(open(p,'rb').read()).decode()
refs=[F+'cero-02-fria-caliente-e.png',R+'web/cero-boton-servir.png',R+'cero-pantalla-real.png']
p=("Photograph in the SAME kitchen, window light and counter as the first reference image, with the SAME elvo Cero purifier (identical shape, screen, buttons, jug on the front-left). "
   "A woman's hand with one finger pressing the small silver dispensing button located just above the drip tray, under the screen (see the second reference for the gesture); a clear glass stands on the tray under the spout and a thin stream of plain water has just started to fall into it. "
   "The silver button must be plain brushed silver with NO blue glow or light. Show only her hand and forearm, no face needed. No ice, no steam, no other cups. Medium shot, the machine and the hand clearly visible, centered, with margins. Photorealistic, bright natural light, steel-blue and white palette, no text.")
r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(x) for x in refs],'image_size':{'width':1536,'height':1536},'quality':'high','num_images':1}); j=r.json(); print(r.status_code,flush=True)
while True:
    time.sleep(10); s=requests.get(j['status_url']).json()
    if s.get('status')=='COMPLETED': break
    if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): print(s); sys.exit(1)
u=requests.get(j['response_url']).json()['images'][0]['url']
open(F+'cero-boton-presionando.png','wb').write(requests.get(u).content); print('saved',flush=True)
