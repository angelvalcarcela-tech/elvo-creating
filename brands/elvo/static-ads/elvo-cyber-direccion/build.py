import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H=1080,1920
F="/usr/share/fonts/opentype/inter/"
def f(n,s): return ImageFont.truetype(F+n,s)
top=np.array([51,85,255],float); bot=np.array([122,150,255],float)
y=np.linspace(0,1,H)[:,None,None]
im=Image.fromarray(((top*(1-y)+bot*y)*np.ones((H,W,3))).astype("uint8"))
glow=Image.new("L",(W,H),0); g=ImageDraw.Draw(glow)
cx,cy,r=540,1560,780
g.ellipse([cx-r-60,cy-r-60,cx+r+60,cy+r+60],fill=120)
glow=glow.filter(ImageFilter.GaussianBlur(60))
im=Image.composite(Image.new("RGB",(W,H),(215,228,255)),im,glow)
dome=Image.new("L",(W,H),0); ImageDraw.Draw(dome).ellipse([cx-r,cy-r,cx+r,cy+r],fill=255)
dy=np.clip((np.arange(H)-(cy-r))/(2*r),0,1)[:,None,None]
inner=(np.array([246,249,255],float)*(1-dy)+np.array([190,208,255],float)*dy)*np.ones((H,W,3))
im=Image.composite(Image.fromarray(inner.astype("uint8")),im,dome)
d=ImageDraw.Draw(im)
def tracked(x,y,t,font,fill,sp):
    for ch in t:
        d.text((x,y),ch,font=font,fill=fill); x+=d.textlength(ch,font=font)+sp
WHITE=(255,255,255); BLUE=(51,85,255)
logo=Image.open("../../brand-identity/product-images/elvo-logo-trim.png").convert("RGBA")
wl=Image.new("RGBA",logo.size,(255,255,255,255)); wl.putalpha(logo.getchannel("A"))
lw=230; lh=int(wl.size[1]*lw/wl.size[0]); lg=wl.resize((lw,lh),Image.LANCZOS); im.paste(lg,(70,272),lg)
d=ImageDraw.Draw(im)
fl=f("Inter-Medium.otf",25); t="// 27 OCT — 1 NOV"
tw=sum(d.textlength(c,font=fl)+5 for c in t); tracked(W-70-tw,292,t,fl,WHITE,5)
d.text((60,350),"CYBER",font=f("Inter-Bold.otf",250),fill=WHITE)
d.text((70,628),"Agua mejor en casa. Solo hasta este domingo.",font=f("Inter-Medium.otf",38),fill=(235,241,255))
p=Image.open("../../brand-identity/product-images/nativo-equipo-web.png").convert("RGB").crop((190,185,835,905))
pw=520; ph=int(pw*p.size[1]/p.size[0]); p=p.resize((pw,ph),Image.LANCZOS)
mask=Image.new("L",p.size,0); ImageDraw.Draw(mask).rounded_rectangle([0,0,pw,ph],radius=44,fill=255)
px=(W-pw)//2; py=860
sh=Image.new("L",(W,H),0); ImageDraw.Draw(sh).rounded_rectangle([px+8,py+30,px+pw-8,py+ph+20],radius=44,fill=90)
sh=sh.filter(ImageFilter.GaussianBlur(28))
im=Image.composite(Image.new("RGB",(W,H),(90,120,230)),im,sh); im.paste(p,(px,py),mask)
d=ImageDraw.Draw(im)
def pill(x,y,t,font,fill=None,outline=WHITE,tc=WHITE,padx=30,h=64):
    w=d.textlength(t,font=font)+padx*2
    d.rounded_rectangle([x,y,x+w,y+h],radius=h//2,fill=fill,outline=outline,width=3 if outline else 0)
    d.text((x+padx,y+h/2-font.size*0.62),t,font=font,fill=tc)
fp=f("Inter-SemiBold.otf",30)
pill(70,706,"Nativo Antimetales",fp)
pill(70,1000,"S/ 349",f("Inter-Bold.otf",44),fill=WHITE,outline=None,tc=BLUE,padx=34,h=84)
pill(70,1100,"Regalo: filtro",fp,outline=BLUE,tc=BLUE)
pill(W-70-250,1150,"6 etapas",fp,outline=BLUE,tc=BLUE)
pill(W-70-310,1250,"30 días de prueba",fp,outline=BLUE,tc=BLUE)
tracked(70,1570,"ELVO· // CYBER 2026",f("Inter-Medium.otf",24),(36,62,190),5)
im.save("elvo-cyber-direccion_v2.png"); print("ok")
