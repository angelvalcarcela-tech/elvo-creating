from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H=1080,1920
F="/usr/share/fonts/opentype/inter/"
def f(n,s): return ImageFont.truetype(F+n,s)
BLUE=(51,85,255); WHITE=(255,255,255); INK=(5,6,7); ICE=(238,243,247); GREY=(91,100,112)
def circle(d,cx0,cy0,r=36): d.ellipse([cx0-r,cy0-r,cx0+r,cy0+r],fill=BLUE)
def ic_shield(d,cx0,cy0):
    circle(d,cx0,cy0); d.polygon([(cx0,cy0-22),(cx0+18,cy0-15),(cx0+18,cy0+3),(cx0,cy0+22),(cx0-18,cy0+3),(cx0-18,cy0-15)],fill=WHITE)
    d.line([(cx0-8,cy0),(cx0-2,cy0+7),(cx0+9,cy0-7)],fill=BLUE,width=5)
def ic_layers(d,cx0,cy0):
    circle(d,cx0,cy0)
    for i,wd in enumerate([24,19,13]): yy=cy0-16+i*14; d.rounded_rectangle([cx0-wd,yy,cx0+wd,yy+9],radius=4,fill=WHITE)
def ic_cal(d,cx0,cy0):
    circle(d,cx0,cy0); d.rounded_rectangle([cx0-21,cy0-19,cx0+21,cy0+21],radius=6,outline=WHITE,width=4)
    d.rectangle([cx0-21,cy0-19,cx0+21,cy0-7],fill=WHITE)
    d.line([(cx0-10,cy0-26),(cx0-10,cy0-13)],fill=WHITE,width=4); d.line([(cx0+10,cy0-26),(cx0+10,cy0-13)],fill=WHITE,width=4)
    for dx in (-10,0,10):
        for dy in (3,12): d.ellipse([cx0+dx-2,cy0+dy-2,cx0+dx+2,cy0+dy+2],fill=WHITE)
def ic_drop(d,cx0,cy0):
    circle(d,cx0,cy0); d.polygon([(cx0,cy0-22),(cx0+15,cy0+2),(cx0-15,cy0+2)],fill=WHITE); d.ellipse([cx0-15,cy0-8,cx0+15,cy0+22],fill=WHITE)
def ic_jug(d,cx0,cy0):
    circle(d,cx0,cy0); d.polygon([(cx0-12,cy0-18),(cx0+12,cy0-18),(cx0+17,cy0+18),(cx0-17,cy0+18)],fill=WHITE)
    d.line([(cx0+14,cy0-12),(cx0+24,cy0-6),(cx0+19,cy0+6)],fill=WHITE,width=4)
    d.line([(cx0-11,cy0-2),(cx0+11,cy0-2)],fill=BLUE,width=4)
def ic_bolt(d,cx0,cy0):
    circle(d,cx0,cy0); d.polygon([(cx0+4,cy0-22),(cx0-12,cy0+3),(cx0-1,cy0+3),(cx0-5,cy0+22),(cx0+13,cy0-5),(cx0+1,cy0-5)],fill=WHITE)
    d.line([(cx0-20,cy0+18),(cx0+20,cy0-18)],fill=BLUE,width=6); d.line([(cx0-20,cy0+18),(cx0+20,cy0-18)],fill=WHITE,width=2)
def ic_thermo(d,cx0,cy0):
    circle(d,cx0,cy0); d.rounded_rectangle([cx0-6,cy0-22,cx0+6,cy0+8],radius=6,fill=WHITE); d.ellipse([cx0-12,cy0+2,cx0+12,cy0+24],fill=WHITE)
    d.rectangle([cx0-2,cy0-8,cx0+2,cy0+14],fill=BLUE)
def build(out,cutfile,name_lines,price,regular,gift,items,maxh=690,maxw=440,pname_size=46):
    im=Image.new("RGB",(W,H),BLUE); d=ImageDraw.Draw(im)
    wm=f("Inter-Bold.otf",300)
    for r,y in enumerate(range(120,H,300)):
        x=-120 if r%2==0 else -330
        while x<W:
            d.text((x,y),"elvo",font=wm,fill=BLUE,stroke_width=3,stroke_fill=(78,108,255)); x+=d.textlength("elvo",font=wm)+60
    def wrap(t,font,maxw2):
        words=t.split(); lines=[]; cur=""
        for w in words:
            c=(cur+" "+w).strip()
            if d.textlength(c,font=font)<=maxw2: cur=c
            else: lines.append(cur); cur=w
        lines.append(cur); return lines
    logo=Image.open("../../brand-identity/product-images/elvo-logo-trim.png").convert("RGBA")
    wl=Image.new("RGBA",logo.size,(255,255,255,255)); wl.putalpha(logo.getchannel("A"))
    lw=210; lh=int(wl.size[1]*lw/wl.size[0]); lg=wl.resize((lw,lh),Image.LANCZOS); im.paste(lg,(70,272),lg)
    d=ImageDraw.Draw(im)
    d.text((62,322),"CYBER",font=f("Inter-Bold.otf",214),fill=WHITE)
    t="Solo hasta este domingo"; fd=f("Inter-SemiBold.otf",36); tw=d.textlength(t,font=fd)
    d.rounded_rectangle([70,572,70+tw+70,642],radius=35,fill=(150,196,255)); d.text((105,572+35-fd.size*0.62),t,font=fd,fill=(15,40,150))
    cut=Image.open(cutfile).convert("RGBA")
    sc=min(maxh/cut.size[1],maxw/cut.size[0]); pw,ph=int(cut.size[0]*sc),int(cut.size[1]*sc); cut=cut.resize((pw,ph),Image.LANCZOS)
    pbottom=1350; px=48+(maxw-pw)//2; py=pbottom-ph
    shd=Image.new("L",(W,H),0); ImageDraw.Draw(shd).ellipse([px+10,py+ph-24,px+pw-10,py+ph+26],fill=130)
    shd=shd.filter(ImageFilter.GaussianBlur(16)); im=Image.composite(Image.new("RGB",(W,H),(20,40,170)),im,shd)
    im.paste(cut,(px,py),cut); d=ImageDraw.Draw(im)
    PX0,PX1,PY0,PY1=500,1020,700,1352
    d.rounded_rectangle([PX0,PY0,PX1,PY1],radius=48,fill=ICE)
    fn=f("Inter-Bold.otf",pname_size); y=PY0+44
    for l in name_lines: d.text((PX0+36,y),l,font=fn,fill=INK); y+=pname_size+10
    py2=y+34
    d.rounded_rectangle([PX0+28,py2,PX1-28,py2+128],radius=64,fill=BLUE)
    ps=92 if len(price)<=7 else 80
    fp=f("Inter-Bold.otf",ps); w=d.textlength(price,font=fp); d.text((PX0+(PX1-PX0-w)/2,py2+64-fp.size*0.62),price,font=fp,fill=WHITE)
    fr=f("Inter-Medium.otf",30); t=f"Precio regular: {regular}"; w=d.textlength(t,font=fr); d.text((PX0+(PX1-PX0-w)/2,py2+146),t,font=fr,fill=GREY)
    gy=py2+214
    d.rounded_rectangle([PX0+28,gy,PX1-28,gy+112],radius=26,fill=WHITE,outline=BLUE,width=3)
    x=PX0+56; lab=gift[0]; flb=f("Inter-Bold.otf",24)
    for ch in lab: d.text((x,gy+14),ch,font=flb,fill=BLUE); x+=d.textlength(ch,font=flb)+6
    d.text((PX0+56,gy+50),gift[1],font=f("Inter-Bold.otf",38),fill=INK)
    assert gy+112<=PY1-10,(out,gy+112)
    BY0,BY1=1378,1580
    d.rounded_rectangle([50,BY0,1030,BY1],radius=40,fill=ICE)
    n=len(items); colw=(1030-50)//n; fb=f("Inter-Bold.otf",27)
    for i,(ic,tx) in enumerate(items):
        cx0=50+colw*i+colw//2; ls=wrap(tx,fb,colw-34); ic(d,cx0,BY0+58)
        for j,l in enumerate(ls):
            w=d.textlength(l,font=fb); d.text((cx0-w/2,BY0+112+j*32),l,font=fb,fill=INK)
        if i<n-1: d.line([(50+colw*(i+1),BY0+26),(50+colw*(i+1),BY1-26)],fill=(190,208,223),width=2)
    im.save(out); print(out)
build("elvo-cyber-alivio16_v1.png","cut_alivio16.png",["Bidón","Alivio","16 Litros"],"S/ 159","S/ 201",("DE REGALO","Medidor de agua"),
 [(ic_drop,"Agua de reserva en casa"),(ic_jug,"Se llena con una jarra"),(ic_bolt,"Sin electricidad ni instalación")])
build("elvo-cyber-alivio22_v1.png","cut_alivio22.png",["Bidón","Alivio","22 Litros"],"S/ 198","S/ 213",("DE REGALO","Medidor de agua"),
 [(ic_drop,"Agua de reserva en casa"),(ic_jug,"Se llena con una jarra"),(ic_bolt,"Sin electricidad ni instalación")])
build("elvo-cyber-cero_v1.png","cut_cero.png",["Purificador","Cero","Ósmosis inversa"],"S/ 1,799","S/ 2,800",("FINANCIA","6 cuotas sin intereses"),
 [(ic_thermo,"Agua fría y caliente al instante"),(ic_layers,"Ósmosis inversa de 5 etapas"),(ic_bolt,"Sin instalación")],maxh=560,maxw=450)
