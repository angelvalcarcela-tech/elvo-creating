import time,requests,sys
B='/home/user/elvo-creating/brands/elvo/'
p=("Realistic photograph of a typical under-sink reverse osmosis water purification system installed inside an open kitchen sink cabinet: three white and clear filter housings mounted on a bracket, a blue storage tank, thin tubing and fittings, a plumber's wrench resting on the cabinet floor, the underside of a stainless steel sink above, and a small separate chrome faucet on the sink. Generic, unbranded, no text, no logos. Bright clean kitchen, steel-blue and white palette, square 1:1 photograph, the whole system centered with generous margins.")
r=requests.post('https://queue.fal.run/openai/gpt-image-2',json={'prompt':p,'image_size':{'width':1536,'height':1536},'quality':'high','num_images':1}); j=r.json(); print(r.status_code,flush=True)
while True:
    time.sleep(10); s=requests.get(j['status_url']).json()
    if s.get('status')=='COMPLETED': break
    if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): print(s); sys.exit(1)
u=requests.get(j['response_url']).json()['images'][0]['url']
open(B+'content/ecommerce/fotos/osmosis-lavadero.png','wb').write(requests.get(u).content); print('saved',flush=True)
