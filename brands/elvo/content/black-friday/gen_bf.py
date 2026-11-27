import base64,time,requests,threading,os
def uri(p): return 'data:image/%s;base64,'%('png' if p.endswith('png') else 'jpeg')+base64.b64encode(open(p,'rb').read()).decode()
def call(name,refs,p):
    out=f'fotos/{name}.png'
    if os.path.exists(out): return
    for t in range(3):
        try:
            r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(x) for x in refs],'image_size':{'width':1088,'height':1360},'quality':'high','num_images':1}).json()
            if 'status_url' not in r: print('ERR',name,str(r)[:200],flush=True); return
            while True:
                time.sleep(10); s=requests.get(r['status_url']).json()
                if s.get('status')=='COMPLETED': break
                if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): raise Exception(str(s)[:200])
            u=requests.get(r['response_url']).json()['images'][0]['url']
            open(out,'wb').write(requests.get(u).content); print('saved',name,flush=True); return
        except Exception as e: print('retry',name,e,flush=True)
E='../ecommerce/'
BR=(" 4:5 vertical Instagram carousel slide for the brand elvo. Palette: deep navy #010A21, electric blue #3355FF, steel blue #9EBACE, white. Clean, premium, calm; bold sans-serif (Inter-like) headline with generous space; at most the exact text quoted, in Spanish, spelled exactly, sharp. No exclamation marks, no urgency, no percentages, no shipping text, no competitor logos. The small wordmark 'elvo·' (thin lowercase with a drop) bottom-right on a dark area only. Keep the product EXACTLY as in the reference image (shape, proportions, colour). ")
J=[
('bf1',[E+'ml-portadas/elvo-nativo-portada.jpg',E+'ml-portadas/elvo-alivio16-portada.jpg',E+'ml-portadas/elvo-cero-portada.jpg'],
 "COVER SLIDE. Deep navy background with a soft electric-blue glow. Show the three products from the references standing together on a pale stone countertop, each product alone (no boxes): the Nativo (tall white cylindrical tap purifier with chrome spout), the Alivio bottle purifier and the Cero countertop machine, each with a glass of clear water beside it, arranged with the tall Alivio in the middle. Headline in white, large, top-left: \"Black Days\". Under it in light blue: \"Tres formas de tener agua pura en casa.\" Bottom-left small pill: \"elvo.pe\"."+BR),
('bf2',[E+'refs-reales/derivador-instalado-1.jpg',E+'fotos/ref-vivo-real-instalado.png','../../brand-identity/product-images/nativo-front.png'],
 "PRODUCT SLIDE for elvo Nativo. Photorealistic lifestyle: a bright modern kitchen counter with soft cool window light; the white elvo Nativo purifier (reference 3) standing next to a common chrome kitchen faucet, connected with a chrome diverter on the faucet and a thin white hose to the purifier, as in references 1 and 2. The purifier's chrome spout rises in front of the white body and arcs to the LEFT, pouring a thin continuous stream of clear water into a glass held directly under the spout. A navy gradient band at the bottom with white text: headline \"Nativo\" large, and \"desde S/ 299\" in light blue, and a small line: \"Directo en tu caño. Lo instalas tú en 5 minutos.\""+BR),
('bf3',['fotos/ref-alivio.jpg'],
 "PRODUCT SLIDE for elvo Alivio. Photorealistic lifestyle in a bright kitchen with soft window light: the Alivio bottle purifier from the reference standing on the counter, full and sharp, with NO logo and NO text printed on it (keep the purifier completely blank). A woman's hand pours water from a glass jug into the top tank after removing the dome lid, OR a glass is filled from its tap with a real stream of water falling from the tap into the glass. Navy gradient band at the bottom with white text: headline \"Alivio\" large and \"desde S/ 159\" in light blue, and a small line: \"Agua de reserva en casa. Sin luz ni instalación.\""+BR),
('bf4',['fotos/ref-cero.jpg'],
 "PRODUCT SLIDE for elvo Cero. Photorealistic lifestyle in a bright modern kitchen with soft window light: the white Cero countertop reverse-osmosis machine from the reference, exactly as it is, with a ceramic cup under the outlet on its tray and a finger pressing the silver button; clear water falling into the cup with a little gentle steam. No hoses, no tap connection. Navy gradient band at the bottom with white text: headline \"Cero\" large and \"S/ 1,990\" in light blue, and a small line: \"Agua fría o caliente, al instante. Ósmosis inversa.\""+BR),
]
ths=[threading.Thread(target=call,args=j) for j in J]
[t.start() for t in ths];[t.join() for t in ths]
