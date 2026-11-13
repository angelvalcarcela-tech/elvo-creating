import base64,time,requests,sys,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'
def uri(p): return 'data:image/png;base64,'+base64.b64encode(open(p,'rb').read()).decode()
REFS=[F+'ref-estilo-despiece.png',B+'brand-identity/product-images/nativo-repuesto-nucleo.png',B+'brand-identity/product-images/nativo-front.png']
BASE=("Square 1:1 premium technical product infographic in the style of the FIRST reference image: a minimal editorial exploded-view engineering illustration of a cylindrical water-filter core, soft monochrome greys with a few thin blue flow arrows, a very faint light-grey grid background, thin leader lines with small dot ends, clean modern sans-serif type. "
 "Do NOT reproduce any logo or text from the first reference (no OQUVA, no English). The object is the elvo PureCore filter core (see second reference: white end caps, dark carbon mesh, label 'elvo· Núcleo PureCore') shown exploded into SIX distinct stacked/nested layers with numbered small blue circles 1 to 6. A small elvo· wordmark in the top-left corner. "
 "Typography hierarchy for every one of the six callouts: FIRST a large bold dark-navy line stating WHAT IT REMOVES, then BELOW it a much smaller grey uppercase line in square brackets naming the component. ALL TEXT EXACTLY AS WRITTEN, in Spanish, correct accents, nothing else added. "
 "Title at the top: \"Qué elimina el Nativo\". Callouts: "
 "1 big \"Cloro, olores y mal sabor\" / small \"[ CARBÓN ACTIVADO ]\"; "
 "2 big \"Plomo y metales pesados*\" / small \"[ ETAPA ANTIMETALES ]\"; "
 "3 big \"Microorganismos\" / small \"[ PLATA COLOIDAL ]\"; "
 "4 big \"Microplásticos y partículas finas\" / small \"[ NANOTECNOLOGÍA ]\"; "
 "5 big \"Turbidez del agua\" / small \"[ ALUMINOSILICATO ]\"; "
 "6 big \"Agua más pura por más tiempo\" / small \"[ PLATA IÓNICA ]\". "
 "Footnote at the bottom in small grey: \"*Según la ficha técnica del núcleo PureCore. Pensado para agua de red potable.\"")
J=[
('despiece-a',BASE+" Layout: light background (#f4f6f8) with grid; the exploded core centered-left, callouts to the right with leader lines; title top-left in dark navy."),
('despiece-b',BASE+" Layout: slightly bluish-white background (#eaf1f7) with grid; the exploded core on the left third and larger, the six callouts stacked on the right with generous spacing; electric-blue (#3355FF) accents for the numbers and arrows; title top-left in dark navy."),
]
def run(name,p):
    for t in range(3):
        try:
            r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(x) for x in REFS],'image_size':{'width':1536,'height':1536},'quality':'high','num_images':1}); j=r.json()
            while True:
                time.sleep(10); s=requests.get(j['status_url']).json()
                if s.get('status')=='COMPLETED': break
                if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): raise Exception(str(s)[:200])
            u=requests.get(j['response_url']).json()['images'][0]['url']
            open(F+f'{name}.png','wb').write(requests.get(u).content); print('saved',name,flush=True); return
        except Exception as e: print('retry',name,e,flush=True)
ths=[threading.Thread(target=run,args=j) for j in J]
[t.start() for t in ths]; [t.join() for t in ths]; print('ALLDONE',flush=True)
