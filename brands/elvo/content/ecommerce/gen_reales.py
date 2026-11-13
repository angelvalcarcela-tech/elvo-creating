import base64,time,requests,sys,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'; R=B+'content/ecommerce/refs-reales/'; W=B+'brand-identity/product-references/web/'; L=B+'content/lote11/'
def uri(p):
    mt='image/jpeg' if p.endswith('.jpg') else 'image/png'
    return f'data:{mt};base64,'+base64.b64encode(open(p,'rb').read()).decode()
PROD=B+'brand-identity/product-images/nativo-front.png'
REAL=(" REAL-PRODUCT FIDELITY (very important): the DIVERTER must look exactly like the real one in the reference photos: a chrome cylindrical diverter body with a knurled chrome ring, a side hose connector with a hexagonal nickel nut where a thin WHITE flexible hose attaches, and a BLACK teardrop-shaped rubber lever. "
      "The UNIVERSAL RUBBER ADAPTER must look exactly like the real one in the reference photos: a short black rubber cone/cylinder with a stainless-steel hose clamp (worm-drive screw) around the upper part and a brass threaded ring at the bottom. ")
STYLE=(" Visual style of the elvo brand: premium, calm and bright; steel-blue (#9EBACE), white and deep navy (#010A21) with electric blue (#3355FF) accents; clean modern sans-serif type like Inter; generous margins; rounded corners; photorealistic product photography combined with crisp graphic design. Square 1:1 ecommerce image. "
 "ALL TEXT EXACTLY AS WRITTEN IN QUOTES, in Spanish, correct accents and spelling; add NO other words, numbers, logos or badges. No text may overlap or cover any product or hand. The elvo Nativo purifier must match its reference: white cylindrical body, grey drop icon, 'elvo·' wordmark, white base ring.")
J=[
('real-grifos',[R+'adaptador.jpg',R+'adaptador-arriba.jpg',F+'nativo-10-grifos.png'],
 "Premium compatibility infographic on a light steel-blue background (#dbe7f0). Title at the top-left in dark navy: \"Se adapta a tu grifo\". Left two thirds: a 2x2 grid of four round photographic frames, each a DIFFERENT kitchen faucet spout end: a curved gooseneck, a flat wide spout, a flat rectangular spout, and a flexible black silicone spout. Right third: one tall rounded panel with a clean photograph of the REAL universal rubber adapter exactly as in the first two references (black rubber with steel clamp and brass thread), on a light neutral surface, with the caption under it \"Adaptador universal de jebe\". Bottom: \"Incluye derivador y adaptador universal de jebe. Compatible con la mayoría de grifos estándar.\" Bottom-left small \"elvo·\"."+REAL+STYLE),
('real-caja',[W+'vivo-que-incluye-la-caja.png',R+'derivador-y-adaptador.jpg',R+'adaptador.jpg',PROD],
 "Premium 'what is in the box' flat-lay on a pale warm-stone surface with a soft steel-blue wall at the top. Title \"En la caja\" in dark navy at the top-left on the empty wall, well above the objects. In a tidy horizontal row, each item separate, fully visible and not overlapping: the elvo Nativo purifier body (standing, WITHOUT its spout attached), the separate curved chrome dispensing spout, the PureCore filter cartridge, the chrome DIVERTER with its black teardrop lever and white hose connector (as in the real reference photo), the coiled white hose, the REAL black rubber universal ADAPTER with steel clamp and brass thread (as in the reference photos), a white plastic wrench, a small white sealing washer with a black silicone ring, and a small white manual booklet. Below, one small line of grey text: \"Purificador · Caño · Núcleo · Derivador · Manguera · Adaptador de jebe · Llave · Manual\". Bottom-left small \"elvo·\"."+REAL+STYLE),
('real-instala',[R+'derivador-instalado-2.jpg',R+'derivador-instalado-1.jpg',F+'final-instala.png',PROD],
 "Premium installation infographic on a very light steel-blue background (#dbe7f0). Top-left: small blue uppercase kicker \"Así se instala\" and the large dark-navy title \"Tú, en 5 minutos\". Below, THREE tall arch-shaped photo panels side by side with soft shadow, each with a numbered blue circle and a caption underneath on the plain background: panel 1 shows hands screwing the REAL chrome diverter (black teardrop lever, white hose attached on the side) onto the end of a chrome kitchen faucet, caption \"Conectas el derivador\"; panel 2 shows the elvo Nativo on the counter with water falling into a glass, caption \"Dejas correr el agua 5 min\"; panel 3 shows a finger flipping the BLACK teardrop lever of the diverter installed on the faucet with the white hose, the Nativo behind, caption \"Mueves la palanca y sirves\". Bottom-left small \"elvo·\". Captions never over the photos."+REAL+STYLE),
]
def run(name,refs,p):
    for t in range(3):
        try:
            r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(x) for x in refs],'image_size':{'width':1536,'height':1536},'quality':'high','num_images':1}); j=r.json()
            while True:
                time.sleep(10); s=requests.get(j['status_url']).json()
                if s.get('status')=='COMPLETED': break
                if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): raise Exception(str(s)[:200])
            u=requests.get(j['response_url']).json()['images'][0]['url']
            open(F+f'{name}.png','wb').write(requests.get(u).content); print('saved',name,flush=True); return
        except Exception as e: print('retry',name,e,flush=True)
ths=[threading.Thread(target=run,args=j) for j in J]
[t.start() for t in ths]; [t.join() for t in ths]; print('ALLDONE',flush=True)
