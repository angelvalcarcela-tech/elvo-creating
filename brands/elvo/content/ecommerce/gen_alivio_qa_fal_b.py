import base64,time,requests,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'; W=B+'brand-identity/product-references/web/'; R=B+'content/ecommerce/refs-reales/'
def uri(p):
    mt='image/jpeg' if p.endswith('.jpg') else 'image/png'
    return f'data:{mt};base64,'+base64.b64encode(open(p,'rb').read()).decode()
H16=W+'alivio-16l-hero.png'; H22=W+'alivio-22l-hero.png'; COMP=R+'alivio-componentes.png'; CAJA='/tmp/ecom/a16/caja.png'
BASE=(" Photorealistic premium lifestyle photograph for an ecommerce listing, bright natural window light, clean modern Lima apartment kitchen in whites, light wood and soft steel-blue tones, shallow depth of field, square 1:1. "
 "The product must match the reference exactly: a white gravity water purifier with a transparent tank, a white ceramic dome filter on top and a small black tap/lever at the front. NO logo or brand text on the product, NO text anywhere in the image, NO prices. Leave calm empty space at the top (about 20%) for a title overlay.")
J=[('aqa2-uso-b',[H16],"A woman facing the camera stands at a kitchen counter next to the purifier. Her RIGHT hand (the hand on the LEFT side of the image) holds the removed top lid of the purifier lifted up in the air, so the upper tank is open; her LEFT hand (on the RIGHT side of the image) tilts a glass jug and pours water into the open upper tank. A full glass of clear water stands beside it. Warm, effortless mood."+BASE),
 ('aqa6-caja-b',[CAJA,H16],"Premium unboxing on a light wooden table, 3/4 top view, with REALISTIC RELATIVE SIZES: the assembled purifier is about 62 cm tall and 35 cm wide and stands next to a large open white shipping box that is clearly big enough to hold it (box about 45 x 40 x 70 cm). Around them, much SMALLER accessories at true scale: the white ceramic dome filter is only about 10 cm tall (roughly one sixth of the purifier height), the multimedia filter column about 20 cm tall, the white mineral disc about 10 cm wide, a tiny 6 cm dropper bottle and a small folded manual about the size of a postcard. The accessories must look clearly small next to the purifier. Warm, gift-like, desirable."+BASE)]
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
