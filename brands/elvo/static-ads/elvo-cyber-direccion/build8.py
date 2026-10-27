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
def wrap(t,font,maxw):
    words=t.split(); lines=[]; cur=""
    for w in words:
        c=(cur+" "+w).strip()
        if d.textlength(c,font=font)<=maxw: cur=c
        else: lines.append(cur); cur=w
    lines.append(cur); return lines
WHITE=(255,255,255); BLUE=(51,85,255); INK=(5,6,7)
logo=Image.open("../../brand-identity/product-images/elvo-logo-trim.png").convert("RGBA")
wl=Image.new("RGBA",logo.size,(255,255,255,255)); wl.putalpha(logo.getchannel("A"))
lw=230; lh=int(wl.size[1]*lw/wl.size[0]); lg=wl.resize((lw,lh),Image.LANCZOS); im.paste(lg,(70,272),lg)
d=ImageDraw.Draw(im)
d.text((60,350),"CYBER",font=f("Inter-Bold.otf",250),fill=WHITE)
d.text((70,628),"Solo hasta este domingo.",font=f("Inter-SemiBold.otf",40),fill=(235,241,255))
d.text((70,700),"Purificador Nativo Antimetales",font=f("Inter-Bold.otf",56),fill=WHITE)
# producto
cut=Image.open("cut_flip.png").convert("RGBA")
ph=745; pw=int(cut.size[0]*ph/cut.size[1]); cut=cut.resize((pw,ph),Image.LANCZOS)
px=58; py=825
halo=Image.new("L",(W,H),0); ImageDraw.Draw(halo).ellipse([px-60,py+40,px+pw+60,py+ph+60],fill=110)
halo=halo.filter(ImageFilter.GaussianBlur(50))
im=Image.composite(Image.new("RGB",(W,H),(255,255,255)),im,halo)
shd=Image.new("L",(W,H),0); ImageDraw.Draw(shd).ellipse([px+10,py+ph-22,px+pw-10,py+ph+22],fill=120)
shd=shd.filter(ImageFilter.GaussianBlur(14))
im=Image.composite(Image.new("RGB",(W,H),(110,135,225)),im,shd)
im.paste(cut,(px,py),cut)
d=ImageDraw.Draw(im)
def tracked(x,y,t,font,fill,sp):
    for ch in t:
        d.text((x,y),ch,font=font,fill=fill); x+=d.textlength(ch,font=font)+sp
# columna derecha
RX=565; RW=445
d.rounded_rectangle([RX,810,RX+RW,975],radius=52,fill=WHITE)
fp=f("Inter-Bold.otf",88); t="S/ 349"; w=d.textlength(t,font=fp); d.text((RX+(RW-w)/2,812),t,font=fp,fill=BLUE)
fr=f("Inter-Medium.otf",30); t="Precio regular: S/ 598"; w=d.textlength(t,font=fr); d.text((RX+(RW-w)/2,926),t,font=fr,fill=(91,100,112))
d.rounded_rectangle([RX,1005,RX+RW,1120],radius=26,fill=WHITE,outline=BLUE,width=3)
tracked(RX+28,1020,"DE REGALO",f("Inter-Bold.otf",25),BLUE,6)
d.text((RX+28,1058),"Filtro de repuesto",font=f("Inter-Bold.otf",40),fill=INK)
# iconos (blanco sobre círculo azul), caja 64x64
def circle(x,yc):
    d.ellipse([x,yc-32,x+64,yc+32],fill=BLUE); return x+32,yc
def icon_shield(x,yc):
    cx0,cy0=circle(x,yc)
    pts=[(cx0,cy0-20),(cx0+16,cy0-14),(cx0+16,cy0+2),(cx0,cy0+20),(cx0-16,cy0+2),(cx0-16,cy0-14)]
    d.polygon(pts,fill=WHITE)
    d.line([(cx0-7,cy0),(cx0-2,cy0+6),(cx0+8,cy0-6)],fill=BLUE,width=5)
def icon_layers(x,yc):
    cx0,cy0=circle(x,yc)
    for i,wd in enumerate([22,17,12]):
        yy=cy0-14+i*13
        d.rounded_rectangle([cx0-wd,yy,cx0+wd,yy+8],radius=4,fill=WHITE)
def icon_clock(x,yc):
    cx0,cy0=circle(x,yc)
    d.ellipse([cx0-19,cy0-19,cx0+19,cy0+19],outline=WHITE,width=5)
    d.line([(cx0,cy0),(cx0,cy0-11)],fill=WHITE,width=5); d.line([(cx0,cy0),(cx0+9,cy0+5)],fill=WHITE,width=5)
def icon_cal(x,yc):
    cx0,cy0=circle(x,yc)
    d.rounded_rectangle([cx0-19,cy0-17,cx0+19,cy0+19],radius=6,outline=WHITE,width=4)
    d.rectangle([cx0-19,cy0-17,cx0+19,cy0-6],fill=WHITE)
    d.line([(cx0-9,cy0-23),(cx0-9,cy0-12)],fill=WHITE,width=4); d.line([(cx0+9,cy0-23),(cx0+9,cy0-12)],fill=WHITE,width=4)
    for dx in (-9,0,9):
        for dy2 in (2,11): d.ellipse([cx0+dx-2,cy0+dy2-2,cx0+dx+2,cy0+dy2+2],fill=WHITE)
items=[(icon_shield,"Retiene metales pesados"),
       (icon_layers,"Multietapas: 6 etapas para un mejor sabor"),
       (icon_cal,"Núcleo de alta duración: 18 meses")]
ft=f("Inter-Bold.otf",36); y=1170
for ic,t in items:
    ls=wrap(t,ft,RW-84)
    hh=max(64,len(ls)*44)
    ic(RX,y+hh//2)
    for i,l in enumerate(ls): d.text((RX+84,y+(hh-len(ls)*44)//2+i*44),l,font=ft,fill=INK)
    y+=hh+30
print("bullets end",y)
im.save("elvo-cyber-direccion_v8.png"); print("ok")
