import base64,time,requests,threading,os
def uri(p):
    return 'data:image/%s;base64,'%('png' if p.endswith('png') else 'jpeg')+base64.b64encode(open(p,'rb').read()).decode()
def call(name,refs,p):
    out='mock/%s.png'%name
    if os.path.exists(out): return
    for t in range(3):
        try:
            r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(x) for x in refs],'image_size':{'width':1536,'height':1024},'quality':'high','num_images':1}).json()
            if 'status_url' not in r: print('ERR',name,str(r)[:200],flush=True); return
            while True:
                time.sleep(10); s=requests.get(r['status_url']).json()
                if s.get('status')=='COMPLETED': break
                if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): raise Exception(str(s)[:200])
            u=requests.get(r['response_url']).json()['images'][0]['url']
            open(out,'wb').write(requests.get(u).content); print('saved',name,flush=True); return
        except Exception as e: print('retry',name,e,flush=True)
LB='assets/logo-blue.png'; LW='assets/logo-white-on-navy.png'
BR=" The brand is 'elvo' (water purifiers): clean, calm, premium, palette electric blue #3355FF, steel blue #9EBACE, deep navy #010A21, off-white. The logo is the lowercase rounded-sans wordmark 'elvo' with a small water drop at its upper right, EXACTLY as in the logo reference (copy it faithfully, do not redraw or alter the letters). Photorealistic brand-identity mockup, high-end Behance presentation quality. The only text allowed is the elvo logo and the exact text quoted."
J=[
('cover-wall',[LB,LW],"Wide street-level mockup of a long mural/wall advertising panel next to a sidewalk with tree shadows falling across it, sunny sky. The wall has three panels: left panel a photo of a smiling woman drinking a glass of water next to a white countertop water purifier; center panel off-white with the elvo logo in blue at top and the small text \"Agua pura. Simplificada.\"; right panel solid electric blue with a very large white-light-blue drop shape graphic."+BR),
('cards',[LB,LW],"Top-down mockup on a steel-blue (#9EBACE) surface: five business cards scattered at angles, two deep-navy cards with the white elvo logo and three white cards with the blue elvo logo, with small unreadable fine print lines; one card says \"Camila R.\" and \"Fundadora\". Soft shadows."+BR),
('packaging',[LB,LW],"Dense top-down angled pattern of flat rectangular product boxes stacked and tiled, in electric blue, light steel blue and white; each box has the elvo logo (white on blue boxes, blue on white/light boxes) and a thin small drop icon. Soft diagonal light. No other text."+BR),
('tote',[LB,LW],"Lifestyle mockup: a person's lower body in black trousers and sneakers holding a light steel-blue cotton tote bag printed with the elvo logo in navy and a small drop icon, studio floor in warm brown; plus nothing else."+BR),
('van',[LB,LW],"A modern delivery truck with a rectangular electric-blue (#3355FF) cargo box, large white elvo logo centered on the side with a soft white glow arc, parked in a dark concrete garage with a glossy reflective floor, side view."+BR),
('billboard',[LB,LW],"Urban rooftop billboard mockup on a brick building against a bright blue sky: the billboard shows a joyful close-up of a woman's face catching water droplets, elvo logo in blue at top-left, and the text \"Agua pura. Simplificada.\" at the bottom. Realistic street scene."+BR),
]
ths=[threading.Thread(target=call,args=j) for j in J]
[t.start() for t in ths];[t.join() for t in ths]
