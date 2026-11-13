import base64,time,requests
B='/home/user/elvo-creating/brands/elvo/content/ecommerce/fotos/'
def uri(p): return 'data:image/png;base64,'+base64.b64encode(open(p,'rb').read()).decode()
p=("Edit this photo with MINIMAL changes. Remove ONLY the separate clear water jug standing on the counter to the right of the purifier, replacing that area with the plain counter surface and the existing background. "
   "Also on the cardboard box, remove the small slogan line under the 'elvo· Cero' wordmark so only the wordmark remains. "
   "Keep EVERYTHING else exactly identical: the elvo Cero purifier (shape, screen, buttons, installed jug on its front-left, colors, position), the box, the user manual, the warranty card, the lighting and framing. Do not redraw or alter the purifier.")
r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(B+'cero-08-caja.png')],'image_size':{'width':1536,'height':1536},'quality':'high','num_images':1}); j=r.json(); print(r.status_code,flush=True)
while True:
    time.sleep(10); s=requests.get(j['status_url']).json()
    if s.get('status')=='COMPLETED': break
    if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): print(s); raise SystemExit
u=requests.get(j['response_url']).json()['images'][0]['url']
open(B+'cero-08-caja-d.png','wb').write(requests.get(u).content); print('saved',flush=True)
