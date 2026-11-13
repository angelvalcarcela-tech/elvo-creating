import base64,time,requests,sys,threading
B='/home/user/elvo-creating/brands/elvo/'
OUT=B+'content/ecommerce/whatsapp/'
def uri(p): return 'data:image/png;base64,'+base64.b64encode(open(p,'rb').read()).decode()
NAT=B+'brand-identity/product-images/nativo-front.png'
CERO=B+'content/lote10/j2-graduacion-ml_v2.png'
CERO2=B+'content/video-cero/v1-cero-solo.png'
REF=B+'content/ecommerce/fotos/cero-08-caja-d.png'
POLO=("A friendly Peruvian woman in her late 20s with long dark hair, a warm natural smile, looking at the camera, wearing a crisp white polo shirt with a small embroidered 'elvo·' wordmark and tiny drop on the left chest (the wordmark exactly like the 'elvo·' on the product in the reference: lowercase 'elvo' followed by a small drop-shaped dot, in grey-blue). "
      "Bright soft studio light, pale steel-blue and white background, natural skin, professional but warm customer-service look. NO other text, no other logos.")
J=[
('perfil-a',[NAT],"Square 1:1 profile portrait for a WhatsApp Business account, head and shoulders, the face centered with generous space around so a circular crop works. "+POLO,1024,1024),
('perfil-b',[NAT],"Square 1:1 profile portrait for a WhatsApp Business account, head and shoulders, slight head tilt, the face centered with generous space around so a circular crop works. A different woman than a typical stock photo, with shoulder-length wavy brown hair. "+POLO,1024,1024),
('banner-a',[NAT,CERO2],"Wide 2.4:1 cover banner for a WhatsApp Business profile of the brand elvo·. A bright, calm modern kitchen counter scene in steel-blue and white tones with soft window light. LEFT side: large clean dark-navy text on two lines, \"Agua pura.\" and \"Simplificada.\", with a small \"elvo·\" wordmark above it. RIGHT side: the elvo Nativo faucet purifier (white cylinder with chrome spout, as in the first reference) and the elvo Cero countertop purifier (as in the second reference) standing on the counter next to a glass of water, both fully visible. The CENTER-BOTTOM area of the banner must be left empty and calm (a circular profile photo will cover it). Add no other text, logos or badges."+" Photorealistic product photography with crisp graphic typography.",1920,800),
('banner-b',[NAT,CERO2],"Wide 2.4:1 cover banner for a WhatsApp Business profile of the brand elvo·. Soft pale steel-blue (#9EBACE to white) gradient background with a subtle arch shape, calm premium look. LEFT side: large dark-navy text on two lines, \"Agua pura.\" and \"Simplificada.\", with a small \"elvo·\" wordmark above it. RIGHT side: the elvo Nativo purifier (as in the first reference) and the elvo Cero purifier (as in the second reference) side by side with a soft shadow and a glass of clear water, both fully visible and bright. The CENTER-BOTTOM area must be left empty (a circular profile photo will cover it). Add no other text, logos or badges."+" Photorealistic product photography with crisp graphic typography.",1920,800),
]
def run(name,refs,p,w,h):
    for t in range(3):
        try:
            r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(x) for x in refs],'image_size':{'width':w,'height':h},'quality':'high','num_images':1}); j=r.json()
            while True:
                time.sleep(10); s=requests.get(j['status_url']).json()
                if s.get('status')=='COMPLETED': break
                if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): raise Exception(str(s)[:200])
            u=requests.get(j['response_url']).json()['images'][0]['url']
            open(OUT+f'{name}.png','wb').write(requests.get(u).content); print('saved',name,flush=True); return
        except Exception as e: print('retry',name,e,flush=True)
ths=[threading.Thread(target=run,args=j) for j in J]
[t.start() for t in ths]; [t.join() for t in ths]; print('ALLDONE',flush=True)
