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
J=[('aqa5-entrega-c',[BOX,H16],"A friendly delivery person at the door of a bright apartment handing the customer THE EXACT retail box shown in the first reference image (light-blue elvo box, same artwork, same logo and proportions, about 40 cm cube-like size, carried with both hands). Smiling customer receives it, welcoming trustworthy mood. The purifier itself is not visible outside the box."+BASE.replace("The product must match the reference exactly","Keep the same clean style").replace("NO logo or brand text on the product, NO text anywhere in the image","No other text anywhere except what is printed on the box")),
 ('aqa6-caja-c',[BOX,CAJA,H16],"Premium unboxing on a light wooden table, 3/4 top view: on the left the assembled purifier (about 62 cm tall), on the right THE EXACT retail box from the first reference image (light-blue elvo box, same artwork, same logo; a real box of about 40 cm per side, so slightly shorter than the purifier), standing closed next to it. In front, much SMALLER accessories at true scale: white ceramic dome filter about 10 cm tall, multimedia filter column about 20 cm, white mineral disc about 10 cm wide, a tiny dropper bottle and a postcard-sized manual. Warm, gift-like, desirable."+BASE.replace("NO logo or brand text on the product, NO text anywhere in the image","No other text anywhere except what is printed on the box"))]
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
