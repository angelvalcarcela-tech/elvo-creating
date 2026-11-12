import json,sys
from PIL import Image,ImageDraw
sys.argv=sys.argv[:2]
import importlib.util
spec=importlib.util.spec_from_file_location('mp','make_promo.py'); mp=importlib.util.module_from_spec(spec)
src=open('make_promo.py').read().split("if __name__")[0]
exec(compile(src,'mp','exec'),mp.__dict__)
cfg=json.load(open(sys.argv[1])); tiles=[]
for i,s in enumerate(cfg['scenes']):
    if s.get('card'): im=Image.new('RGB',(1080,1920),(51,85,255))
    else:
        import os
        im=Image.open(s['src']).convert('RGB') if os.path.exists(s['src']) else Image.new('RGB',(1152,2048),(120,120,130)); r=max(1080/im.width,1920/im.height); im=im.resize((int(im.width*r),int(im.height*r)))
        x=(im.width-1080)//2; y=(im.height-1920)//2; im=im.crop((x,y,x+1080,y+1920)); up=int(s.get('up',110)); c=Image.new('RGB',(1080,1920),(1,10,33)); c.paste(im.crop((0,up,1080,1920)) if up>=0 else im,(0,0 if up>=0 else -up)); im=c
    mp.overlay_png(s['title'],s.get('sub',''),'/tmp/ov.png',card=s.get('card',False),footer=s.get('footer',''),pos=s.get('pos','bottom'))
    im=im.convert('RGBA'); im.alpha_composite(Image.open('/tmp/ov.png')); d=ImageDraw.Draw(im)
    for yy in (270,1540): d.line([(0,yy),(1080,yy)],fill=(255,0,0,255),width=4)
    for xx in (70,960): d.line([(xx,0),(xx,1920)],fill=(255,0,0,255),width=4)
    tiles.append(im.convert('RGB').resize((270,480)))
cols=min(len(tiles),6); rows=(len(tiles)+cols-1)//cols
sh=Image.new('RGB',(270*cols,480*rows),'white')
for k,t in enumerate(tiles): sh.paste(t,((k%cols)*270,(k//cols)*480))
sh.save(sys.argv[1].replace('.json','-audit.png')); print(sh.size)
