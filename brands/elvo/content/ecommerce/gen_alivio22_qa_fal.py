import base64,time,requests,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'; W=B+'brand-identity/product-references/web/'; R=B+'content/ecommerce/refs-reales/'
def uri(p):
    mt='image/jpeg' if p.endswith('.jpg') else 'image/png'
    return f'data:{mt};base64,'+base64.b64encode(open(p,'rb').read()).decode()
H22=W+'alivio-22l-hero.png'; COMP=R+'alivio-componentes.png'; PH=R+'alivio-medidor-ph-tienda.png'
BASE=(" Photorealistic premium lifestyle photograph for an ecommerce listing, bright natural window light, clean modern Lima apartment kitchen in whites, light wood and soft steel-blue tones, shallow depth of field, square 1:1. "
 "The purifier must match the reference exactly: the BOXY RECTANGULAR 22-liter model, white base with a transparent blue-tinted lower tank, an open transparent upper tank with the small white ceramic dome filter visible inside it, and a small black-and-chrome tap at the front; about 61 cm tall and 35 cm wide. NO text anywhere in the image, NO prices. Leave calm empty space at the top (about 20%) for a title overlay.")
J=[('a22-2-uso',[H22],"A woman facing the camera stands at a kitchen counter next to the purifier. Her RIGHT hand (the hand on the LEFT side of the image) holds the removed white top lid lifted up in the air, so the upper tank is open; her LEFT hand (on the RIGHT side of the image) tilts a glass jug and pours water into the open upper tank. A full glass of clear water stands beside it. Warm, effortless mood."+BASE),
 ('a22-7-lab',[H22],"A clean, bright, premium scene: a clear glass of pure water held up to the window light by a hand in the foreground-left, and next to it on a white counter the purifier; behind, subtle laboratory glassware (a clear flask and a test tube rack) softly blurred. Trustworthy, scientific yet warm mood."+BASE),
 ('a22-8-reserva',[H22],"Cozy evening in a Lima apartment kitchen, soft warm lamp light and dusk through the window; on the counter the purifier full of water, a glass pitcher full of water and a filled glass beside it; the kitchen sink faucet is clearly dry and unused. Mood: calm, prepared, reassured, like having water in reserve at home."+BASE),
 ('a22-9-filtro',[H22,COMP],"Medium close-up of a hand lifting the small white ceramic dome filter out of the open upper tank of the purifier on a bright kitchen counter. CRUCIAL SCALE: the ceramic dome filter is SMALL, only about one third to 40 percent of the width of the upper tank, about 10 to 12 cm wide, easily held in one hand; the tank must look much bigger than the dome. After removal the upper tank is completely empty inside (no other dome), BUT the lower tank still contains its installed multimedia filter column (black, brown, white and tan layers). On the counter next to the purifier lies ONE spare new small ceramic dome of the same small size and NOTHING else. Clean, easy, reassuring mood."+BASE),
 ('a22-10-ph',[PH,H22],"Close-up on a bright kitchen counter. A hand holds the glass dropper pipette of a pH test kit pointing STRAIGHT DOWN: black rubber bulb on top between the fingers, thin glass tube below it, and ONE single water drop falling from the very TIP of the glass tube into a clear glass of water placed right below. Physically correct: the drop comes out of the pipette tip. On the counter to the left stands the closed small clear dropper bottle with a plain blank white label. In front of the glass, a straight horizontal row of FIVE small round color swatches going from pale yellow through yellow-green and green to teal blue (exactly like the first reference). The purifier stands softly blurred in the background far right. Clean, simple mood."+BASE)]
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
