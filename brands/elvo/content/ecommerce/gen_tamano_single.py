import base64,time,requests,threading
B='/home/user/elvo-creating/brands/elvo/'
F=B+'content/ecommerce/fotos/'; W=B+'brand-identity/product-references/web/'
def uri(p):
    mt='image/jpeg' if p.endswith('.jpg') else 'image/png'
    return f'data:{mt};base64,'+base64.b64encode(open(p,'rb').read()).decode()
BASE=(" Photorealistic premium lifestyle photograph for a product listing, bright natural window light, clean modern Lima apartment kitchen in whites, light wood and soft steel-blue tones, shallow depth of field, square 1:1. The purifier stands alone, centered on a light-wood kitchen counter, photographed straight-on from the front at eye level, completely visible with its base and top, with about 25 percent of the image height as calm empty space above it and 18 percent below the counter edge. A plant and one glass of water are placed well apart on the counter, not touching the purifier. NO logo or brand text on the product, NO text anywhere, NO prices.")
J=[('tam-16',[F+'ml-alivio16-ref.jpg'],"Only the round-dome 16-liter purifier from the reference (white base, blue-tinted transparent tanks, white ceramic dome filter, black-chrome tap), about 62 cm tall and 35 cm wide, the box is NOT shown."+BASE),
   ('tam-22',[W+'alivio-22l-hero.png',F+'a22-portada.png'],"Only the boxy rectangular 22-liter purifier from the references (white base, blue-tinted transparent tanks, white ceramic dome filter, tap), about 61 cm tall and 35 cm wide, no box."+BASE)]
def run(name,refs,p):
    for t in range(3):
        try:
            r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(x) for x in refs],'image_size':{'width':1536,'height':1536},'quality':'high','num_images':1}).json()
            if 'status_url' not in r: print('ERR',name,str(r)[:200]); return
            while True:
                time.sleep(10); s=requests.get(r['status_url']).json()
                if s.get('status')=='COMPLETED': break
                if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): raise Exception(str(s)[:200])
            u=requests.get(r['response_url']).json()['images'][0]['url']
            open(F+name+'.png','wb').write(requests.get(u).content); print('saved',name); return
        except Exception as e: print('retry',name,e)
ths=[threading.Thread(target=run,args=j) for j in J]; [t.start() for t in ths]; [t.join() for t in ths]
from PIL import Image,ImageDraw
for n in ('tam-16','tam-22'):
    im=Image.open(F+n+'.png').convert('RGB').resize((1500,1500)); d=ImageDraw.Draw(im)
    for x in range(0,1500,100): d.line([(x,0),(x,1500)],fill=(255,0,0),width=1); d.text((x+3,3),str(x),fill=(255,0,0))
    for y in range(0,1500,100): d.line([(0,y),(1500,y)],fill=(255,0,0),width=1); d.text((3,y+3),str(y),fill=(255,0,0))
    im.resize((900,900)).save(f'/tmp/ml/{n}_grid.png')
