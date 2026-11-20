import base64,time,requests,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'; R=B+'content/ecommerce/refs-reales/'; M='/tmp/ml/ref/'; P=B+'brand-identity/product-references/'
def uri(p):
    mt='image/jpeg' if p.endswith('.jpg') else 'image/png'
    return f'data:{mt};base64,'+base64.b64encode(open(p,'rb').read()).decode()
WHITE=(" Professional ecommerce studio product photograph on a PURE WHITE (#FFFFFF) seamless background, soft realistic contact shadow only, no gradient, no props, no text overlays, no badges, no watermark, no logos added, square 1:1, product sharp and large, centered, filling about 80 percent of the frame. Reproduce the product exactly like the reference.")
J=[('ml-alivio22',[F+'a22-portada.png',R+'alivio-caja-real.jpg'],"The boxy rectangular 22-liter purifier from the first reference standing at right, and at left its retail box exactly as in the second reference (light-blue elvo box with the same artwork, standing upright, slightly angled). Nothing else, no dropper bottle, no glass."+WHITE),
 ('ml-nativo',[M+'nativo_unit.png',M+'panel3_frente.png',M+'panel4.png'],"The white counter-top tap purifier from the first reference standing at right with its swan-neck spout, and at left its retail box: a tall narrow white cardboard box whose FRONT face is exactly the artwork of the second reference (blue elvo logo, PURECORE MINERAL SYSTEM, the product picture, waves) and whose RIGHT side face is the artwork of the third reference. Box angled so the front and the right side are both visible. Do not add any other text."+WHITE),
 ('ml-vivo',[M+'vivo_unit.png'],"Only the white counter-top tap purifier from the reference with its spout, no box, no glass, no water."+WHITE),
 ('ml-cero',[M+'cero_unit.png',P+'cero-pantalla-real.png'],"Only the white elvo Cero reverse-osmosis water dispenser from the first reference, front three-quarter view, with its display screen exactly like the second reference, with its removable jug in place, no glass, no cup, no box, no background objects."+WHITE),
 ('ml-kit-alivio',[M+'kit.png'],"Only the replacement filter kit from the reference: one white ceramic dome filter, one clear cylinder multilayer filter with black, brown, white and tan layers, and one white mineral disc, arranged neatly side by side at true relative sizes (dome and cylinder similar height, disc flat). No box, no text."+WHITE)]
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
