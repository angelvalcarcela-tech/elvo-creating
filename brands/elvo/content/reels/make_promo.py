"""Genera un promo vertical 1080x1920 a partir de escenas (foto + titular + subtítulo).
Ritmo pensado para atención: ~4 s por escena, transición de ~0.9 s, texto que entra a los 0.7 s,
zoom muy suave y cierre más largo. Uso: python3 make_promo.py <config.json>"""
import json, subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont
F=lambda w,s:ImageFont.truetype(f'/usr/share/fonts/opentype/inter/Inter-{w}.otf',s)
def wrap(d,text,font,maxw):
    out=[];cur=''
    for w in text.split():
        t=(cur+' '+w).strip()
        if d.textlength(t,font=font)<=maxw: cur=t
        else: out.append(cur);cur=w
    if cur: out.append(cur)
    return out
def overlay_png(title,sub,out,card=False,footer=''):
    im=Image.new('RGBA',(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(im)
    if not card:
        for y in range(1000,1920): d.line([(0,y),(1080,y)],fill=(1,10,33,min(215,int(215*((y-1000)/700)**1.2))))
    tl=[]
    for part in title.split('|'): tl+=wrap(d,part,F('Medium',96),900)
    sl=wrap(d,sub,F('Regular',44),900) if sub else []
    h=len(tl)*112+(24+len(sl)*58 if sl else 0); y=(1560-h) if not card else 760
    for ln in tl: d.text((90,y),ln,font=F('Medium',96),fill=(255,255,255,255)); y+=112
    y+=24
    for ln in sl: d.text((90,y),ln,font=F('Regular',44),fill=(222,232,255,255)); y+=58
    if card and footer: d.text((90,1700),footer,font=F('Regular',40),fill=(222,232,255,255))
    d.text((90,1790),'elvo·',font=F('SemiBold',48),fill=(255,255,255,255))
    im.save(out)
def build(cfg):
    out=cfg['out']; tmp=os.path.join(os.path.dirname(out),'tmp'); os.makedirs(tmp,exist_ok=True)
    fps=30; x=cfg.get('xfade',0.9); scenes=cfg['scenes']; n=len(scenes)
    durs=[s.get('dur',4.0) for s in scenes]
    Image.new('RGB',(1080,1920),tuple(cfg.get('card_color',(51,85,255)))).save(os.path.join(tmp,'cierre.png'))
    srcs=[]
    for i,s in enumerate(scenes):
        card=s.get('card',False)
        overlay_png(s['title'],s.get('sub',''),os.path.join(tmp,f't{i}.png'),card=card,footer=s.get('footer',''))
        srcs.append(os.path.join(tmp,'cierre.png') if card else s['src'])
    cmd=['ffmpeg','-y','-loglevel','error']
    for s in srcs: cmd+=['-i',s]
    for i in range(n): cmd+=['-loop','1','-framerate',str(fps),'-t',str(durs[i]+x),'-i',os.path.join(tmp,f't{i}.png')]
    fc=[]
    for k,s in enumerate(scenes):
        frames=int((durs[k]+x)*fps); zmax=s.get('zoom',0.06)
        z=f"min(1.0+{zmax}*on/{frames},{1+zmax})" if k%2==0 else f"max({1+zmax}-{zmax}*on/{frames},1.0)"
        if s.get('card'): z="1.0"
        pre=f"scale=1080:-2,pad=1080:1920:0:(1920-ih)/2:color={s['pad']}" if s.get('pad') else "scale=-2:1920,crop=1080:1920"
        fc.append(f"[{k}:v]{pre},scale=4320:7680:flags=lanczos,zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s=1080x1920:fps={fps},format=yuv420p[b{k}]")
        fc.append(f"[{n+k}:v]format=rgba,fade=t=in:st=0.7:d=0.7:alpha=1[t{k}]")
        fc.append(f"[b{k}][t{k}]overlay=0:0:format=auto,format=yuv420p,setsar=1[s{k}]")
    last='[s0]'; acc=0
    for k in range(1,n):
        acc+=durs[k-1]
        fc.append(f"{last}[s{k}]xfade=transition=fade:duration={x}:offset={round(acc,2)}[x{k}]"); last=f'[x{k}]'
    cmd+=['-filter_complex',';'.join(fc),'-map',last,'-c:v','libx264','-preset','fast','-crf','23','-pix_fmt','yuv420p','-movflags','+faststart',out]
    r=subprocess.run(cmd,capture_output=True,text=True,timeout=2400); print(r.returncode,r.stderr[:300])
if __name__=='__main__': build(json.load(open(sys.argv[1])))
