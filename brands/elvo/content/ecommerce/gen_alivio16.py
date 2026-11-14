import base64,time,requests,sys,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'; W=B+'brand-identity/product-references/web/'
def uri(p):
    mt='image/jpeg' if p.endswith('.jpg') else 'image/png'
    return f'data:{mt};base64,'+base64.b64encode(open(p,'rb').read()).decode()
REFS=[W+'alivio-16l-hero.png',W+'alivio-armado.png',W+'alivio-paso1-llenar-con-jarra.png',W+'alivio-paso3-servir.png']
ALI=(" The elvo Alivio 16 L gravity water purifier must match the references exactly: a white dome lid on top; a clear upper tank holding a white dome-shaped ceramic filter; a clear lower tank holding a vertical multimedia filter column (black, white and red-brown layers); a small chrome tap with a black handle near the bottom; a white base. "
     "NO logo or text on the equipment. No power cord, no plugs, no hoses, no connection to any water tap. Clear colorless water.")
STYLE=(" Visual style of the elvo brand: premium, calm and bright; steel-blue (#9EBACE), white and deep navy (#010A21) with electric blue (#3355FF) accents; clean modern sans-serif type like Inter; generous margins; rounded corners; photorealistic photography combined with crisp graphic design. Square 1:1 ecommerce image. "
       "ALL TEXT EXACTLY AS WRITTEN IN QUOTES, in Spanish with correct accents; add NO other words, numbers, prices, logos or badges. No text may overlap or cover a product or a hand: keep text in clear empty areas.")
KIT=" Setting: a bright warm modern home kitchen/living area, light warm-stone surface, soft herringbone-tile wall, window with green trees, a plant, soft morning light."
J=[
('a16-01-principal',"A woman in a light-blue shirt stands beside the elvo Alivio on a kitchen counter and drinks a glass of clear water with a relaxed smile; the Alivio is full of water, LARGE, bright and fully visible next to her. No text at all."+ALI+KIT+" Square 1:1 photograph, no text."),
('a16-02-etapas',"Premium infographic on a light steel-blue background. Title at top-left in dark navy: \"Filtra con 8 etapas\". Left: a clean 3D cutaway illustration of the elvo Alivio (as in the references) showing its clear tanks, the white ceramic filter and the multimedia filter column, with thin leader lines. Right: a numbered list with electric-blue numbered circles and dark-navy text, one per line: 1 \"Filtro cerámico\"; 2 \"Carbón activado y de plata\"; 3 \"WMSM-300\"; 4 \"Arena de sílice\"; 5 \"Zeolita\"; 6 \"Arena mineral\"; 7 \"Piedra mineral\"; 8 \"Llave\". Small \"elvo·\" wordmark bottom-left."+ALI+STYLE),
('a16-03-sin-electricidad',"The elvo Alivio standing alone on a wooden console in a hallway corner of a bright home, far from any kitchen or sink, a bare wall behind it with NO outlets, no cables, no pipes; a plant and soft window light. The Alivio is large and centered with plenty of empty wall above it. Text in dark navy in the empty wall area at the top-left: \"Sin electricidad.\" and below it \"Sin presión de caño.\" Small \"elvo·\" wordmark at the bottom-left."+ALI+STYLE),
('a16-04-uso',"Premium usage infographic on a very light steel-blue background (#dbe7f0). Top-left: small blue uppercase kicker \"Así se usa\" and the large dark-navy title \"Tú, en 3 pasos\". Below, THREE tall arch-shaped photo panels side by side with a soft shadow, each with an electric-blue numbered circle and a caption below on the plain background. Panel 1: hands lifting the white dome lid off the Alivio; caption \"Quitas la tapa\". Panel 2: a glass jug pouring clear water into the open upper tank of the Alivio, lid held aside; caption \"Llenas con una jarra\". Panel 3: a hand holding a glass under the Alivio's chrome tap with a thin stream of water; caption \"Sirves por la llave\". Bottom-left small \"elvo·\"."+ALI+STYLE),
('a16-05-gotas-ph',"Premium product photo on a light steel-blue background (#dbe7f0): a small white plastic dropper bottle with a white dropper cap (the pH drops) standing next to a clear glass of water into which one drop is falling and slightly tinting the water, beside the elvo Alivio softly visible and slightly blurred behind them. Title at the top-left in dark navy: \"Gotas de pH incluidas\" and below it in smaller grey text: \"Mide tu agua y revisa el estado de tus filtros.\" The bottle label shows only the two letters \"pH\". Small \"elvo·\" bottom-left."+ALI+STYLE),
('a16-06-kit',"Premium product photo on a pale warm-stone surface with a soft steel-blue wall at the top: three filter parts of a water purifier kit laid out neatly and separate, side by side — a white ceramic dome filter, a vertical multimedia filter column (black, white and red-brown layers) and a flat white mineral disc — in front of the softly blurred elvo Alivio. Title at the top-left in dark navy on the wall: \"10.000 litros o 1 año\" and below in smaller grey text: \"Lo que ocurra primero. El equipo ya trae su filtro; el kit de repuesto se vende aparte.\" Small \"elvo·\" bottom-left."+ALI+STYLE),
('a16-07-capacidad',"A cozy bright living-dining area: the elvo Alivio, full of water, stands large and fully visible on a wooden sideboard; two people (a couple) are seated at a dining table in the background, relaxed, with glasses of water, softly out of focus. Text in dark navy in the empty wall area at the top-left: \"16 litros\" in very large type and below it in smaller type: \"Para 1 o 2 personas\". Small \"elvo·\" bottom-left."+ALI+STYLE),
('a16-08-medidas',"Clean product-dimension image on a very light steel-blue background (#dbe7f0): the elvo Alivio centered, large, front view, with thin dark-navy dimension lines. A vertical dimension line on its right side labeled in a white rounded pill \"62 cm\" (height), and a horizontal dimension line under its base labeled in a white rounded pill \"35 × 31 cm\" (base). Title at the top-left in dark navy: \"Medidas\". Small \"elvo·\" bottom-left."+ALI+STYLE),
('a16-09-caja',"Premium 'what is in the box' flat-lay on a pale warm-stone surface with a soft steel-blue wall at the top. Title \"En la caja\" in dark navy at the top-left on the empty wall, well above the objects. In one tidy horizontal row with even gaps, each item separate and fully visible: the elvo Alivio fully assembled with its filters installed and its white dome lid on top (standing, the largest item); a small white plastic dropper bottle labeled only \"pH\"; a small white user manual booklet. Below, one small line of grey text: \"Alivio 16 L con filtro · Gotas de pH · Manual\". Small \"elvo·\" bottom-left."+ALI+STYLE),
('a16-10-hogar',"A warm family scene in a bright home in the Peruvian highlands style living room: a mother pours water from a glass jug into the open top tank of the elvo Alivio standing on a wooden table, a child watching, soft window light, cozy. The Alivio is large and fully visible. Text in dark navy in a clear empty area at the top-left: \"Agua de resguardo\" and below \"en casa.\" Small \"elvo·\" bottom-left."+ALI+STYLE),
]
def run(name,p):
    for t in range(3):
        try:
            r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(x) for x in REFS],'image_size':{'width':1536,'height':1536},'quality':'high','num_images':1}); j=r.json()
            if 'status_url' not in j: print('ERR',name,str(j)[:200],flush=True); return
            while True:
                time.sleep(10); s=requests.get(j['status_url']).json()
                if s.get('status')=='COMPLETED': break
                if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): raise Exception(str(s)[:200])
            u=requests.get(j['response_url']).json()['images'][0]['url']
            open(F+f'{name}.png','wb').write(requests.get(u).content); print('saved',name,flush=True); return
        except Exception as e: print('retry',name,e,flush=True)
sem=threading.Semaphore(4)
def w(j):
    with sem: run(*j)
ths=[threading.Thread(target=w,args=(j,)) for j in J]
[t.start() for t in ths]; [t.join() for t in ths]; print('ALLDONE',flush=True)
