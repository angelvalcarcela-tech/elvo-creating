from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H=1080,1920
F="/usr/share/fonts/opentype/inter/"
def f(n,s): return ImageFont.truetype(F+n,s)
BLUE=(51,85,255); WHITE=(255,255,255); INK=(5,6,7); ICE=(238,243,247); GREY=(91,100,112)
im=Image.new("RGB",(W,H),BLUE); d=ImageDraw.Draw(im)
# marca de agua en contorno
wm=f("Inter-Bold.otf",300)
for r,y in enumerate(range(120,H,300)):
    x=-120 if r%2==0 else -330
    while x<W:
        d.text((x,y),"elvo",font=wm,fill=BLUE,stroke_width=3,stroke_fill=(78,108,255)); x+=d.textlength("elvo",font=wm)+60
def wrap(t,font,maxw):
    words=t.split(); lines=[]; cur=""
    for w in words:
        c=(cur+" "+w).strip()
        if d.textlength(c,font=font)<=maxw: cur=c
        else: lines.append(cur); cur=w
    lines.append(cur); return lines
logo=Image.open("../../brand-identity/product-images/elvo-logo-trim.png").convert("RGBA")
wl=Image.new("RGBA",logo.size,(255,255,255,255)); wl.putalpha(logo.getchannel("A"))
lw=210; lh=int(wl.size[1]*lw/wl.size[0]); lg=wl.resize((lw,lh),Image.LANCZOS); im.paste(lg,(70,272),lg)
d=ImageDraw.Draw(im)
d.text((62,322),"CYBER",font=f("Inter-Bold.otf",214),fill=WHITE)
# pastilla de fecha
t="Solo hasta este domingo"; fd=f("Inter-SemiBold.otf",36); tw=d.textlength(t,font=fd)
d.rounded_rectangle([70,572,70+tw+70,642],radius=35,fill=(150,196,255))
d.text((105,572+35-fd.size*0.62),t,font=fd,fill=(15,40,150))
# producto grande a la izquierda
cut=Image.open("cut_flip.png").convert("RGBA")
ph=680; pw=int(cut.size[0]*ph/cut.size[1]); cut=cut.resize((pw,ph),Image.LANCZOS)
px=48; py=668
shd=Image.new("L",(W,H),0); ImageDraw.Draw(shd).ellipse([px+10,py+ph-24,px+pw-10,py+ph+26],fill=130)
shd=shd.filter(ImageFilter.GaussianBlur(16))
im=Image.composite(Image.new("RGB",(W,H),(20,40,170)),im,shd)
im.paste(cut,(px,py),cut)
d=ImageDraw.Draw(im)
# panel derecho claro
PX0,PX1,PY0,PY1=500,1020,700,1352
d.rounded_rectangle([PX0,PY0,PX1,PY1],radius=48,fill=ICE)
fn=f("Inter-Bold.otf",46)
y=PY0+44
for l in ["Purificador","Nativo","Antimetales"]:
    d.text((PX0+36,y),l,font=fn,fill=INK); y+=56
# precio
py2=y+34
d.rounded_rectangle([PX0+28,py2,PX1-28,py2+128],radius=64,fill=BLUE)
fp=f("Inter-Bold.otf",92); t="S/ 349"; w=d.textlength(t,font=fp); d.text((PX0+(PX1-PX0-w)/2,py2+64-fp.size*0.62),t,font=fp,fill=WHITE)
fr=f("Inter-Medium.otf",30); t="Precio regular: S/ 598"; w=d.textlength(t,font=fr); d.text((PX0+(PX1-PX0-w)/2,py2+146),t,font=fr,fill=GREY)
# regalo
gy=py2+214
d.rounded_rectangle([PX0+28,gy,PX1-28,gy+112],radius=26,fill=WHITE,outline=BLUE,width=3)
x=PX0+56
for ch in "DE REGALO":
    d.text((x,gy+14),ch,font=f("Inter-Bold.otf",24),fill=BLUE); x+=d.textlength(ch,font=f("Inter-Bold.otf",24))+6
d.text((PX0+56,gy+50),"Filtro de repuesto",font=f("Inter-Bold.otf",38),fill=INK)
print("panel content end",gy+112,"panel end",PY1)
# iconos
def circle(cx0,cy0,r=36): d.ellipse([cx0-r,cy0-r,cx0+r,cy0+r],fill=BLUE)
def icon_shield(cx0,cy0):
    circle(cx0,cy0)
    d.polygon([(cx0,cy0-22),(cx0+18,cy0-15),(cx0+18,cy0+3),(cx0,cy0+22),(cx0-18,cy0+3),(cx0-18,cy0-15)],fill=WHITE)
    d.line([(cx0-8,cy0),(cx0-2,cy0+7),(cx0+9,cy0-7)],fill=BLUE,width=5)
def icon_layers(cx0,cy0):
    circle(cx0,cy0)
    for i,wd in enumerate([24,19,13]):
        yy=cy0-16+i*14; d.rounded_rectangle([cx0-wd,yy,cx0+wd,yy+9],radius=4,fill=WHITE)
def icon_cal(cx0,cy0):
    circle(cx0,cy0)
    d.rounded_rectangle([cx0-21,cy0-19,cx0+21,cy0+21],radius=6,outline=WHITE,width=4)
    d.rectangle([cx0-21,cy0-19,cx0+21,cy0-7],fill=WHITE)
    d.line([(cx0-10,cy0-26),(cx0-10,cy0-13)],fill=WHITE,width=4); d.line([(cx0+10,cy0-26),(cx0+10,cy0-13)],fill=WHITE,width=4)
    for dx in (-10,0,10):
        for dy in (3,12): d.ellipse([cx0+dx-2,cy0+dy-2,cx0+dx+2,cy0+dy+2],fill=WHITE)
# barra de beneficios
BY0,BY1=1378,1580
d.rounded_rectangle([50,BY0,1030,BY1],radius=40,fill=ICE)
items=[(icon_shield,"Retiene metales pesados"),(icon_layers,"Multietapas: 6 etapas, mejor sabor"),(icon_cal,"Núcleo de alta duración: 18 meses")]
colw=(1030-50)//3; fb=f("Inter-Bold.otf",27)
for i,(ic,tx) in enumerate(items):
    cx0=50+colw*i+colw//2
    ls=wrap(tx,fb,colw-34)
    ic(cx0,BY0+58)
    for j,l in enumerate(ls):
        w=d.textlength(l,font=fb); d.text((cx0-w/2,BY0+112+j*32),l,font=fb,fill=INK)
    if i<2: d.line([(50+colw*(i+1),BY0+26),(50+colw*(i+1),BY1-26)],fill=(190,208,223),width=2)
im.save("elvo-cyber-direccion_v10.png"); print("ok")
