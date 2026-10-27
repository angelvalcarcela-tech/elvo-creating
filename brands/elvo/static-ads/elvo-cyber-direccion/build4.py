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
def wrap(t,font,maxw):
    words=t.split(); lines=[]; cur=""
    for w in words:
        c=(cur+" "+w).strip()
        if d.textlength(c,font=font)<=maxw: cur=c
        else: lines.append(cur); cur=w
    lines.append(cur); return lines
WHITE=(255,255,255); BLUE=(51,85,255); INK=(5,6,7); DEEP=(36,62,190)
logo=Image.open("../../brand-identity/product-images/elvo-logo-trim.png").convert("RGBA")
wl=Image.new("RGBA",logo.size,(255,255,255,255)); wl.putalpha(logo.getchannel("A"))
lw=230; lh=int(wl.size[1]*lw/wl.size[0]); lg=wl.resize((lw,lh),Image.LANCZOS); im.paste(lg,(70,272),lg)
d=ImageDraw.Draw(im)
fl=f("Inter-Medium.otf",25); t="// 27 OCT — 1 NOV"
tw=sum(d.textlength(c,font=fl)+5 for c in t); tracked(W-70-tw,292,t,fl,WHITE,5)
d.text((60,350),"CYBER",font=f("Inter-Bold.otf",250),fill=WHITE)
d.text((70,628),"Agua mejor en casa. Solo hasta este domingo.",font=f("Inter-Medium.otf",38),fill=(235,241,255))
# producto recortado a la derecha
cut=Image.open("cut_isnet-general-use.png").convert("RGBA"); cut=cut.crop(cut.getbbox())
ph=700; pw=int(cut.size[0]*ph/cut.size[1]); cut=cut.resize((pw,ph),Image.LANCZOS)
px=W-70-pw-10; py=800
# sombra de contacto + halo
halo=Image.new("L",(W,H),0); ImageDraw.Draw(halo).ellipse([px-60,py+40,px+pw+60,py+ph+60],fill=110)
halo=halo.filter(ImageFilter.GaussianBlur(50))
im=Image.composite(Image.new("RGB",(W,H),(255,255,255)),im,halo)
shd=Image.new("L",(W,H),0); ImageDraw.Draw(shd).ellipse([px+10,py+ph-22,px+pw-10,py+ph+22],fill=120)
shd=shd.filter(ImageFilter.GaussianBlur(14))
im=Image.composite(Image.new("RGB",(W,H),(110,135,225)),im,shd)
im.paste(cut,(px,py),cut)
d=ImageDraw.Draw(im)
def pill(x,y,t,font,fill=None,outline=WHITE,tc=WHITE,padx=30,h=64):
    w=d.textlength(t,font=font)+padx*2
    d.rounded_rectangle([x,y,x+w,y+h],radius=h//2,fill=fill,outline=outline,width=3 if outline else 0)
    d.text((x+padx,y+h/2-font.size*0.62),t,font=font,fill=tc)
# columna izquierda: un solo camino de lectura
pill(70,706,"Nativo Antimetales",f("Inter-SemiBold.otf",30))
d.rounded_rectangle([70,790,470,935],radius=48,fill=WHITE)
fp=f("Inter-Bold.otf",74); w=d.textlength("S/ 349",font=fp); d.text((70+(400-w)/2,800),"S/ 349",font=fp,fill=BLUE)
fr=f("Inter-Medium.otf",27); t="Precio regular: S/ 598"; w=d.textlength(t,font=fr); d.text((70+(400-w)/2,892),t,font=fr,fill=(91,100,112))
d.rounded_rectangle([70,975,500,1085],radius=24,fill=WHITE,outline=BLUE,width=3)
tracked(100,990,"DE REGALO",f("Inter-Bold.otf",24),BLUE,6)
d.text((100,1026),"Filtro de repuesto",font=f("Inter-Bold.otf",36),fill=INK)
items=["Retiene plomo y metales pesados*","Lo instalo yo en 5 minutos, sin gasfitero","Cartucho de 18 meses, no cada pocos meses","6 etapas de filtrado con KDF-F y plata"]
ft=f("Inter-SemiBold.otf",30); y=1120
for t in items:
    ls=wrap(t,ft,480-58)
    cy2=y+19
    d.ellipse([70,cy2-17,104,cy2+17],fill=BLUE)
    d.line([(78,cy2),(84,cy2+7),(96,cy2-7)],fill=WHITE,width=5)
    for i,l in enumerate(ls): d.text((70+50,y+i*37),l,font=ft,fill=INK)
    y+=len(ls)*37+20
print("bullets end",y)
fn=f("Inter-Regular.otf",22)
t="*Según la ficha técnica del núcleo PureCore. Los resultados dependen de la calidad del agua de entrada."
for i,l in enumerate(wrap(t,fn,940)): d.text((70,1560+i*29),l,font=fn,fill=DEEP)
tracked(70,1626,"ELVO· // CYBER 2026",f("Inter-Medium.otf",22),DEEP,5)
im.save("elvo-cyber-direccion_v4.png"); print("ok")
