import base64,time,requests,sys,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'; R=B+'brand-identity/product-references/web/'; L=B+'content/lote11/'
def uri(p): return 'data:image/png;base64,'+base64.b64encode(open(p,'rb').read()).decode()
PROD=B+'brand-identity/product-images/nativo-front.png'
STYLE=(" Visual style of the elvo brand: premium, calm and bright; steel-blue (#9EBACE), white and deep navy (#010A21) with electric blue (#3355FF) accents; clean modern sans-serif type like Inter; generous spacing and margins; rounded corners; photorealistic product photography combined with crisp graphic design. Square 1:1 ecommerce image. "
 "ALL TEXT EXACTLY AS WRITTEN IN QUOTES, in Spanish, correct accents and spelling; add NO other words, numbers, logos or badges. No text may overlap or cover any product or hand: keep all text in clear empty areas. The elvo Nativo purifier must match its reference exactly: white cylindrical body, grey drop icon, 'elvo·' wordmark, white base ring with latches.")
J=[
('final-instala',[F+'n2-conecta.png',F+'n2-servir.png',L+'n7b-palanca_v1.png',PROD],
 "Premium installation infographic on a very light steel-blue background (#dbe7f0). Top-left: small blue uppercase kicker \"Así se instala\" and below it the large dark-navy title \"Tú, en 5 minutos\". Below, THREE tall arch-shaped photo panels side by side (rounded tops, soft shadow), each using the matching reference photo as its picture, with a numbered blue circle and a short caption underneath: panel 1 (hands screwing a chrome diverter onto the kitchen faucet) caption \"Conectas el derivador\"; panel 2 (the elvo Nativo with water falling into a glass) caption \"Dejas correr el agua 5 min\"; panel 3 (a finger flipping the diverter lever, the Nativo behind) caption \"Mueves la palanca y sirves\". Bottom-left small wordmark \"elvo·\". Captions sit below the panels on the plain background, never over the photos."+STYLE),
('final-caja',[R+'vivo-que-incluye-la-caja.png',PROD,F+'nativo-09-caja.png'],
 "Premium 'what is in the box' flat-lay product photo on a pale warm-stone surface with a soft pale steel-blue wall at the top. The title \"En la caja\" in dark navy at the top-left, in the empty wall area, well above the objects. Arranged in a tidy horizontal flat-lay in the middle, each item separate, fully visible and not overlapping its neighbours: the elvo Nativo purifier body (standing, WITHOUT its spout attached), the separate curved chrome dispensing spout lying next to it, the PureCore filter cartridge, the chrome diverter valve with lever, the coiled white hose, a black rubber universal faucet adapter, a small white sealing washer with a black silicone ring, a white plastic wrench, and a small white user manual booklet. Below the objects, in the empty surface area, one small line of grey text: \"Purificador · Caño · Núcleo · Derivador · Manguera · Adaptador de jebe · Llave · Manual\". Bottom-left small \"elvo·\"."+STYLE),
('final-grifos',[F+'nativo-10-grifos.png',F+'nativo-09-caja.png'],
 "Premium compatibility infographic on a light steel-blue background (#dbe7f0). Title at the top-left in dark navy: \"Se adapta a tu grifo\". Left two thirds: a 2x2 grid of four round photographic frames, each showing a DIFFERENT chrome or black kitchen faucet spout end: a curved gooseneck, a flat wide spout, a flat rectangular spout, and a flexible black silicone spout. Right third: one tall rounded panel with a clean photograph of the black rubber universal faucet adapter (a small black rubber cone-shaped threaded adapter) on a light surface, with the caption under it \"Adaptador universal de jebe\". Bottom, one line of text in the empty area: \"Incluye derivador y adaptador universal de jebe. Compatible con la mayoría de grifos estándar.\" Bottom-left small \"elvo·\"."+STYLE),
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
