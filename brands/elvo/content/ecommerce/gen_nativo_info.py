import base64,time,requests,sys,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'; R=B+'brand-identity/product-references/web/'
def uri(p): return 'data:image/png;base64,'+base64.b64encode(open(p,'rb').read()).decode()
PROD=[B+'brand-identity/product-images/nativo-front.png']
STYLE=(" Visual style of the elvo brand: premium, calm, bright; steel-blue (#9EBACE), white and deep navy (#010A21) with electric blue (#3355FF) accents; clean modern sans-serif typography (like Inter), generous spacing, rounded corners; photorealistic product photography combined with crisp graphic design. Square 1:1 ecommerce product image. "
 "ALL TEXT MUST BE EXACTLY AS WRITTEN IN QUOTES, in Spanish, with correct accents and spelling; do not add any other words, numbers, logos, badges or claims. The elvo Nativo purifier must match the reference exactly: white cylindrical body, grey drop icon, 'elvo·' wordmark, curved chrome spout, white base ring.")
J=[
('info-retiene-a',PROD+[F+'n2-servir.png'],"Premium infographic. Top 58% of the image: a bright warm modern kitchen photo showing the elvo Nativo purifier on the counter, large, with a thin stream of clear water falling from its chrome spout into a glass. Bottom 42%: a deep navy panel with the white title \"Qué retiene y qué reduce\" and a 2x2 checklist with blue circular check icons, each item in white text: \"Retiene plomo y metales pesados*\", \"Reduce cloro, olores y sabores\", \"Atrapa microplásticos y partículas finas\", \"Conserva los minerales del agua\". At the very bottom, small light text: \"*Según la ficha técnica del núcleo PureCore. Pensado para agua de red potable.\""+STYLE),
('info-retiene-b',PROD+[F+'n2-hero.png'],"Premium infographic with a light steel-blue background. Left half: the elvo Nativo purifier large with a clear glass of water beside it, soft shadow. Right half: the title \"Qué retiene y qué reduce\" in dark navy, then four rows, each with a blue circle check icon and dark text: \"Retiene plomo y metales pesados*\", \"Reduce cloro, olores y sabores\", \"Atrapa microplásticos y partículas finas\", \"Conserva los minerales del agua\". At the bottom, small grey text: \"*Según la ficha técnica del núcleo PureCore. Pensado para agua de red potable.\""+STYLE),
('info-etapas-a',PROD+[F+'n2-nucleo.png'],"Premium infographic with a light steel-blue background. Left: the title \"6 etapas en un solo núcleo\" in dark navy and a numbered list with blue numbered circles, each with a bold name and a short grey description: 1 \"Carbón activado\" - \"cloro, olores y mal sabor\"; 2 \"Etapa antimetales*\" - \"retiene metales pesados\"; 3 \"Plata coloidal\" - \"inhibe el crecimiento de microorganismos\"; 4 \"Nanotecnología\" - \"atrapa microplásticos y partículas finas\"; 5 \"Aluminosilicato\" - \"mejora la claridad del agua\"; 6 \"Plata iónica\" - \"mantiene el agua más pura por más tiempo\". Right: an arch-shaped photo of hands lifting the body of the elvo Nativo off its base to reveal the PureCore filter cartridge labelled \"Núcleo PureCore\", in a bright kitchen. Bottom small text: \"*Según la ficha técnica del núcleo PureCore.\""+STYLE),
('info-etapas-b',PROD+[F+'n2-nucleo.png'],"Premium infographic on a deep navy background. Center-left: a beautiful clean 3D cutaway illustration of a cylindrical water filter cartridge (the elvo PureCore core) cut open lengthwise to show SIX distinct stacked layers of different materials and colors, numbered 1 to 6 with blue circles. Right side: labels aligned to each layer in white text with a short light-blue description: 1 \"Carbón activado\" - \"cloro, olores y mal sabor\"; 2 \"Etapa antimetales*\" - \"retiene metales pesados\"; 3 \"Plata coloidal\" - \"inhibe el crecimiento de microorganismos\"; 4 \"Nanotecnología\" - \"atrapa microplásticos y partículas finas\"; 5 \"Aluminosilicato\" - \"mejora la claridad del agua\"; 6 \"Plata iónica\" - \"mantiene el agua más pura por más tiempo\". Title at the top: \"6 etapas en un solo núcleo\". Bottom small text: \"*Según la ficha técnica del núcleo PureCore. Esquema ilustrativo.\""+STYLE),
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
