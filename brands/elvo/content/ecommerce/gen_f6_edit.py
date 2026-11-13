import base64,time,requests,sys
B='/home/user/elvo-creating/brands/elvo/content/ecommerce/fotos/'
def uri(p): return 'data:image/png;base64,'+base64.b64encode(open(p,'rb').read()).decode()
p=("Edit this real photo of the elvo Cero screen with MINIMAL changes. Make only these changes: "
   "1) On the machine diagram at the upper left of the black screen, the two small circles on top of the drawing currently glow blue; make both of them glow RED (a filter-change alert), same size and position. "
   "2) The silver dispensing button under the screen currently glows blue and spills blue light onto the white panel behind it; turn that light completely OFF so it is a plain brushed-silver button with no blue glow and no blue reflection on the surrounding white surface. "
   "Keep EVERYTHING else exactly identical and sharp: all the screen texts and icons, the 'Filter Reset' and 'Pipe Cleaning' buttons, '23' and '500 ml' with the minus and plus buttons, the eight temperature tiles with their exact temperatures, the blue square indicators on the diagram, the 'elvo' wordmark, the jug handle and framing. Do not redraw, rename or rearrange anything.")
r=requests.post('https://queue.fal.run/openai/gpt-image-2/edit',json={'prompt':p,'image_urls':[uri(B+'real-pantalla-cuadrada.png')],'image_size':{'width':1536,'height':1536},'quality':'high','num_images':1}); j=r.json(); print(r.status_code,flush=True)
while True:
    time.sleep(10); s=requests.get(j['status_url']).json()
    if s.get('status')=='COMPLETED': break
    if s.get('status') not in ('IN_QUEUE','IN_PROGRESS'): print(s); sys.exit(1)
u=requests.get(j['response_url']).json()['images'][0]['url']
open(B+'cero-06-aviso-real.png','wb').write(requests.get(u).content); print('saved',flush=True)
