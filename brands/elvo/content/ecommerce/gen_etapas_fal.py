import base64,time,requests,sys,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'; W=B+'brand-identity/product-references/web/'; R=B+'content/ecommerce/refs-reales/'
def uri(p):
    mt='image/jpeg' if p.endswith('.jpg') else 'image/png'
    return f'data:{mt};base64,'+base64.b64encode(open(p,'rb').read()).decode()
REFS=[R+'alivio-componentes.png',W+'alivio-16l-hero.png']
TXT=("ALL TEXT EXACTLY AS WRITTEN, in Spanish with correct accents, nothing else added. Title at the top-left in dark navy: \"8 etapas\" and under it in smaller grey: \"De arriba hacia abajo\". "
 "Eight numbered stages, each with an electric-blue (#3355FF) numbered circle, FIRST a large dark-navy line saying what it does, THEN BELOW it a much smaller grey uppercase line with the component: "
 "1 \"Retiene sedimentos y partículas\" / \"FILTRO CERÁMICO\"; "
 "2 \"Reduce cloro, olores y mal sabor\" / \"CARBÓN ACTIVADO Y DE PLATA\"; "
 "3 \"Complementa el filtrado\" / \"WMSM-300\"; "
 "4 \"Retiene partículas finas\" / \"ARENA DE SÍLICE\"; "
 "5 \"Ayuda a retener impurezas disueltas\" / \"ZEOLITA\"; "
 "6 \"Ayuda a equilibrar el pH\" / \"ARENA MINERAL\"; "
 "7 \"Aporta minerales al agua\" / \"PIEDRA MINERAL\"; "
 "8 \"Sirves cuando quieras\" / \"LLAVE\". "
 "Stages 2 to 6 belong to ONE multimedia filter column and are grouped together by a single bracket labeled \"MULTIMEDIA · 5 CAPAS\"; do NOT draw a separate pointer from each of those five stages to a specific layer. "
 "Footnote at the bottom in small grey: \"Esquema ilustrativo. Funciones generales de cada material. Los resultados dependen de la calidad del agua de entrada.\" Small \"elvo·\" wordmark at the bottom-left.")
STYLE=(" Premium, calm, bright elvo brand style: steel-blue (#9EBACE), white and deep navy (#010A21) with electric-blue accents; clean sans-serif type like Inter; generous spacing; rounded corners; square 1:1 ecommerce image. "
 "Use the first reference as the exact filter parts (white ceramic dome filter, a transparent multimedia filter column with black, brown, white, dark and tan layers, and a white mineral disc). NO logo on any product.")
J=[('etapas-fal-a',"Creative premium infographic on a soft steel-blue background. Center-right: the three filter parts shown as a beautiful clean 3D exploded vertical stack, with a single drop of water at the very top and a smooth curved blue flow line that travels down through the parts to a chrome tap with a black handle at the bottom. Stage labels on the left, aligned with their parts, connected by thin dotted leader lines. "+TXT+STYLE),
   ('etapas-fal-b',"Creative premium infographic on a white background with a large soft steel-blue arch shape. In the center, the three filter parts as a clean 3D exploded vertical stack with light-blue water droplets falling between them; stage labels alternate left and right of the stack, each in a rounded white card with a subtle shadow, connected by thin lines; stage 8 is shown at the bottom next to a small chrome tap with black handle pouring a thin stream of water into a glass. "+TXT+STYLE)]
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
ths=[threading.Thread(target=run,args=j) for j in J]
[t.start() for t in ths]; [t.join() for t in ths]; print('ALLDONE',flush=True)
