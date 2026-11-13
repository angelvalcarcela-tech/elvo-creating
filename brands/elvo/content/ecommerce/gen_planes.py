import base64,time,requests,sys,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'
def uri(p):
    mt='image/jpeg' if p.endswith('.jpg') else 'image/png'
    return f'data:{mt};base64,'+base64.b64encode(open(p,'rb').read()).decode()
PROD=B+'brand-identity/product-images/nativo-front.png'
CORE=B+'brand-identity/product-images/nativo-repuesto-nucleo.png'
REFS=[PROD,CORE,F+'caja2-b-fix.png']
STYLE=(" Visual style of the elvo brand: premium, calm, bright; steel-blue (#9EBACE), white and deep navy (#010A21) with electric blue (#3355FF) accents; clean modern sans-serif type like Inter; generous spacing; rounded corners; crisp graphic design with photorealistic product renders. Square 1:1 ecommerce image. "
 "ALL TEXT EXACTLY AS WRITTEN IN QUOTES, in Spanish, correct accents; add NO other words, numbers, prices, logos or badges. No text overlaps a product. The elvo Nativo purifier and its PureCore filter cartridge must match the references (white cylinder, grey drop icon, 'elvo·' wordmark; cartridge with white caps and a blue-white label).")
BASE=("Premium plan-comparison infographic. Title at the top-left in dark navy: \"Elige tu plan\" and a smaller grey line under it: \"El equipo es el mismo. Cambia cuánto tiempo te despreocupas.\" "
 "Three equal rounded cards side by side. Card 1: heading \"18 meses\", a row with exactly ONE filter cartridge icon-render, text \"1 núcleo\". "
 "Card 2 (highlighted only with a thin electric-blue border, NO tag or badge): heading \"3 años\", a row with exactly TWO filter cartridges, text \"2 núcleos\". "
 "Card 3: heading \"6 años\", a row with exactly FOUR filter cartridges, text \"4 núcleos\". "
 "The cartridges are shown in a clear row so the count is obvious. Under the three cards, one line of text centered: \"Cada núcleo dura 18 meses de uso normal. Te avisamos por WhatsApp cuando toque cambiarlo.\" "
 "At the very bottom-left, a small elvo Nativo purifier render next to the small wordmark \"elvo·\"."+STYLE)
J=[('planes-a',BASE+" Background: very light steel-blue (#dbe7f0)."),
   ('planes-b',BASE+" Background: white with a soft arch shape behind the three cards. Make the cartridge rows large and easy to count.")]
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
