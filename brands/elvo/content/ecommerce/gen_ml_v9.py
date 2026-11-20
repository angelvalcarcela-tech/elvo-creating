import base64,time,requests,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'; R=B+'content/ecommerce/refs-reales/'; P=B+'brand-identity/product-references/'
def uri(p):
    mt='image/jpeg' if p.endswith('.jpg') else 'image/png'
    return f'data:{mt};base64,'+base64.b64encode(open(p,'rb').read()).decode()
def call(name,refs,p):
    for t in range(3):
        try:
            r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(x) for x in refs],'image_size':{'width':1536,'height':1536},'quality':'high','num_images':1}).json()
            if 'status_url' not in r: print('ERR',name,str(r)[:200],flush=True); return False
            while True:
                time.sleep(10); s=requests.get(r['status_url']).json()
                if s.get('status')=='COMPLETED': break
                if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): raise Exception(str(s)[:200])
            u=requests.get(r['response_url']).json()['images'][0]['url']
            open(F+name+'.png','wb').write(requests.get(u).content); print('saved',name,flush=True); return True
        except Exception as e: print('retry',name,e,flush=True)
    return False
STYLE=(" Modern premium marketplace hero photograph: PURE WHITE (#FFFFFF) seamless background; the product group fills about 94 percent of the frame width (tight crop, very little empty space), centered, with its base sitting on a common ground line near the bottom; a SOFT, DIFFUSE, light-grey elliptical contact shadow directly under the product that anchors it (background stays pure white); crisp high-contrast studio lighting with a darker defined edge shading on the white plastic so the white product separates clearly from the white background even at thumbnail size; bright clean specular highlights; ultra sharp 4K detail; slightly low three-quarter angle. No text overlays, no badges, no watermark, no added logos. Square 1:1. Keep every product and its printed artwork EXACTLY as in the references.")
JOBS={
'v9-alivio16':([F+'ml-alivio16-ref.jpg'],"Hero shot of the 16-liter Alivio purifier (round dome, blue-tinted transparent tanks, white base, white ceramic dome filter, black-chrome tap) with its light-blue elvo retail box beside it exactly as in the reference."),
'v9-alivio22':([F+'ml-alivio22-b.png',F+'a22-portada.png'],"Hero shot of the boxy rectangular 22-liter Alivio purifier on the right and its light-blue elvo retail box at left slightly behind, overlapping a little, exactly as in the first reference."),
'v9-nativo':([F+'ml-nativo-ref.png',F+'v6-vivo-fix.png',F+'ml-nativo-box2.png'],"Hero shot: the white counter-top tap purifier at LEFT large (grey drop icon in upper third, grey 'elvo' wordmark with its small drop on the lower part, chrome swan-neck spout on its left) with a crystal-clear glass of water at its base being filled by a sparkling stream; at RIGHT, slightly overlapping, its tall narrow retail box exactly as in the third reference with its wide front facing left. The small drop next to the 'elvo' wordmark must be a tiny exact miniature of the big drop icon (same shape, same light grey, same white highlight)."),
'v9-cero':([F+'ml-cero-ref.jpg',P+'cero-pantalla-real.png'],"Hero shot of the white elvo Cero dispenser exactly as in the first reference (colorful temperature tiles lit on the display, glowing blue dispensing nozzle, removable jug at left, tank at right) with a tall crystal-clear glass full of ice cubes and water on the drip tray being filled right now by a clean stream of water from the nozzle, cold condensation on the glass."),
'v9-kit':([F+'ml-kit-alivio.png',R+'alivio-componentes.png'],"Hero shot of the three replacement filter parts exactly as in the references: white ceramic dome filter with grey base ring at left, clear multilayer cylinder filter (black, grey, white, tan layers) in the center, white mineral disc leaning at right, true relative sizes."),
}
def worker(k):
    refs,p=JOBS[k]; call(k,refs,p+STYLE)
ths=[threading.Thread(target=worker,args=(k,)) for k in JOBS]; [t.start() for t in ths]; [t.join() for t in ths]
# vivo: misma foto del nativo sin caja
ok=call('v9-vivo',[F+'v9-nativo.png'],"Edit the reference: remove the tall retail box on the right completely together with its shadow, leaving pure white background there; keep the purifier, spout, glass, water stream, lighting, shadows and reflections EXACTLY the same, and re-center the purifier and glass so the composition is balanced and fills about 94 percent of the frame height. The small drop beside the 'elvo' wordmark must stay a tiny exact miniature of the big drop icon. No other changes, no text.")
print('ALLDONE',flush=True)
