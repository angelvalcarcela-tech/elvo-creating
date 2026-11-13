import base64,time,requests,sys
B='/home/user/elvo-creating/brands/elvo/content/ecommerce/fotos/'
def uri(p): return 'data:image/png;base64,'+base64.b64encode(open(p,'rb').read()).decode()
p=("Edit this photo with MINIMAL changes. On the elvo Cero, the silver dispensing button just above the tray currently glows with a bright blue light and halo. Turn that light completely OFF: make the button a plain brushed-silver button with no blue glow, no blue light strip and no halo or reflection of blue light around it. "
   "Keep EVERYTHING else exactly identical: the purifier (shape, screen content, buttons, jug), the water pouring into the glass, the glass of ice water, the steaming cup, the kitchen, lighting and framing. Do not redraw or alter anything else.")
r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(B+'cero-02-fria-caliente-c.png')],'image_size':{'width':1536,'height':1536},'quality':'high','num_images':1}); j=r.json(); print(r.status_code,flush=True)
while True:
    time.sleep(10); s=requests.get(j['status_url']).json()
    if s.get('status')=='COMPLETED': break
    if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): print(s); sys.exit(1)
u=requests.get(j['response_url']).json()['images'][0]['url']
open(B+'cero-02-fria-caliente-d.png','wb').write(requests.get(u).content); print('saved',flush=True)
