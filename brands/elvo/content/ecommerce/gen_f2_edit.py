import base64,time,requests,sys
B='/home/user/elvo-creating/brands/elvo/content/ecommerce/fotos/'
def uri(p): return 'data:image/png;base64,'+base64.b64encode(open(p,'rb').read()).decode()
p=("Edit this photo, keeping the SAME kitchen, window, blue vase, plant, counter, lighting, camera angle and the SAME elvo Cero purifier (identical shape, screen, buttons and jug). Make only these three changes: "
   "1) Under the spout, on the drip tray, place one plain clear glass of ordinary room-temperature water being filled by a thin stream of plain water falling from the spout (no ice, no steam). "
   "2) The tall glass with ice cubes and cold water and the white ceramic cup with steam, which are currently on the tray, must be moved onto the counter surface to the right of the machine in the lower right of the frame, standing next to each other, looking exactly the same as they do now (iced glass, steaming cup). "
   "3) The silver dispensing button above the tray must have its blue light turned completely OFF: plain brushed silver, no blue glow. "
   "Change nothing else.")
r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(B+'cero-02-fria-caliente.png')],'image_size':{'width':1536,'height':1536},'quality':'high','num_images':1}); j=r.json(); print(r.status_code,flush=True)
while True:
    time.sleep(10); s=requests.get(j['status_url']).json()
    if s.get('status')=='COMPLETED': break
    if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): print(s); sys.exit(1)
u=requests.get(j['response_url']).json()['images'][0]['url']
open(B+'cero-02-fria-caliente-e.png','wb').write(requests.get(u).content); print('saved',flush=True)
