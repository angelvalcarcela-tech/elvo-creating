import base64,time,requests,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'; W=B+'brand-identity/product-references/web/'; R=B+'content/ecommerce/refs-reales/'
def uri(p):
    mt='image/jpeg' if p.endswith('.jpg') else 'image/png'
    return f'data:{mt};base64,'+base64.b64encode(open(p,'rb').read()).decode()
H16=W+'alivio-16l-hero.png'; H22=W+'alivio-22l-hero.png'; COMP=R+'alivio-componentes.png'; CAJA='/tmp/ecom/a16/caja.png'
BASE=(" Photorealistic premium lifestyle photograph for an ecommerce listing, bright natural window light, clean modern Lima apartment kitchen in whites, light wood and soft steel-blue tones, shallow depth of field, square 1:1. "
 "The product must match the reference exactly: a white gravity water purifier with a transparent tank, a white ceramic dome filter on top and a small black tap/lever at the front. NO logo or brand text on the product, NO text anywhere in the image, NO prices. Leave calm empty space at the top (about 20%) for a title overlay.")
BOX=R+'alivio-caja-real.jpg'
DOM=R+'alivio-filtro-ceramico-en-tanque.png'
J=[('aqa9-filtro-e',[DOM,COMP,H16],"Medium close-up of a hand lifting the white ceramic dome filter out of the open upper tank of the purifier on a bright kitchen counter. CRUCIAL SCALE (see first reference photo): the ceramic dome filter is SMALL, only about one third to 40 percent of the width of the upper tank and clearly smaller than the tank; it is about the size of a fist or a small bowl held easily in one hand, about 10 to 12 cm wide. The upper tank is about 30 cm wide, so the tank must look much bigger than the dome. After removal the upper tank is completely empty inside (no other dome), BUT the lower tank must still contain its installed multimedia filter column (black, brown, white and tan layers) hanging in the middle of the lower tank, as in the second reference. On the counter next to the purifier lies ONE spare new small ceramic dome of the same small size as the one in the hand and NOTHING else (no spare column, no other objects on the counter). The installed multimedia column inside the lower tank must look the same height as the dome (about 20 cm). Clean, easy, reassuring mood."+BASE)]
def run(name,refs,p):
    for t in range(3):
        try:
            r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(x) for x in refs],'image_size':{'width':1536,'height':1536},'quality':'high','num_images':1}); j=r.json()
            if 'status_url' not in j: print('ERR',name,str(j)[:200],flush=True); return
            while True:
                time.sleep(10); s=requests.get(j['status_url']).json()
                if s.get('status')=='COMPLETED': break
                if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): raise Exception(str(s)[:200])
            u=requests.get(j['response_url']).json()['images'][0]['url']
            open(F+f'{name}.png','wb').write(requests.get(u).content); print('saved',name,flush=True); return
        except Exception as e: print('retry',name,e,flush=True)
ths=[threading.Thread(target=run,args=j) for j in J]
[t.start() for t in ths]; [t.join() for t in ths]; print('ALLDONE',flush=True)
