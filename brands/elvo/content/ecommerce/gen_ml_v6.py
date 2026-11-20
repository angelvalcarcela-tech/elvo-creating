import base64,time,requests,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'; R=B+'content/ecommerce/refs-reales/'; P=B+'brand-identity/product-references/'
def uri(p):
    mt='image/jpeg' if p.endswith('.jpg') else 'image/png'
    return f'data:{mt};base64,'+base64.b64encode(open(p,'rb').read()).decode()
STYLE=(" Modern premium e-commerce hero photograph, shot like a current Apple/Dyson product page: PURE WHITE (#FFFFFF) seamless background, bright crisp studio lighting with a large soft key light, clean specular highlights, rich but natural contrast, subtle realistic grounded shadow under the product, ultra sharp 4K detail, slightly low three-quarter camera angle, product fills about 85 percent of the frame, centered. No text overlays, no badges, no watermark, no logos added, no background props except those described. Square 1:1. Keep every product and its printed artwork EXACTLY as in the references.")
J=[('v6-alivio22',[F+'ml-alivio22-b.png',F+'a22-portada.png',R+'alivio-caja-real.jpg'],"Hero shot of the 22-liter Alivio purifier (boxy rectangular, blue-tinted transparent tanks, white base and dome filter, black-chrome tap) standing on the right, and its light-blue elvo retail box standing at the left, slightly angled, just behind and beside the purifier so they overlap a little. Glossy, luminous plastic, fresh and clean feeling."+STYLE),
 ('v6-nativo',[F+'ml-nativo-ref.png',F+'ml-nativo-box2.png'],"Hero shot: on the LEFT the white counter-top tap purifier from the first reference (grey drop icon and elvo wordmark, chrome swan-neck spout on its left) with a crystal-clear glass of water at its base being filled by a sparkling stream from the spout; on the RIGHT, slightly overlapping, its tall narrow retail box from the second reference with its wide front facing left toward the purifier. Fresh, luminous, water droplets catching light."+STYLE),
 ('v6-vivo',[F+'ml-vivo-ref.png'],"Hero shot of only the counter-top tap purifier from the reference (white cylinder with grey water-drop icon and grey elvo wordmark, chrome swan-neck spout), no box, no glass, no water, polished glossy white plastic and mirror chrome with crisp reflections."+STYLE),
 ('v6-cero',[F+'ml-cero-ref.jpg',P+'cero-pantalla-real.png'],"Hero shot of the white elvo Cero reverse-osmosis dispenser exactly as in the first reference (display with the colorful temperature tiles lit, glowing blue dispensing nozzle, removable jug at the left, tank at the right), in front of it on the drip tray a tall crystal-clear glass full of ice cubes and water that is being filled right now by a clean stream of water pouring from the nozzle, with a few droplets and cold condensation on the glass. Fresh, cold, premium."+STYLE),
 ('v6-kit',[F+'ml-kit-alivio.png',R+'alivio-componentes.png'],"Hero shot of the three replacement filter parts exactly as in the references, arranged neatly: a white ceramic dome filter with grey base ring on the left, a clear cylinder multilayer filter with black, grey, white and tan layers in the center, and a white mineral disc leaning at the right, all at true relative sizes, crisp transparent plastic with reflections."+STYLE)]
def run(name,refs,p):
    for t in range(3):
        try:
            r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(x) for x in refs],'image_size':{'width':1536,'height':1536},'quality':'high','num_images':1}).json()
            if 'status_url' not in r: print('ERR',name,str(r)[:200],flush=True); return
            while True:
                time.sleep(10); s=requests.get(r['status_url']).json()
                if s.get('status')=='COMPLETED': break
                if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): raise Exception(str(s)[:200])
            u=requests.get(r['response_url']).json()['images'][0]['url']
            open(F+name+'.png','wb').write(requests.get(u).content); print('saved',name,flush=True); return
        except Exception as e: print('retry',name,e,flush=True)
ths=[threading.Thread(target=run,args=j) for j in J]
[t.start() for t in ths]; [t.join() for t in ths]; print('ALLDONE',flush=True)
