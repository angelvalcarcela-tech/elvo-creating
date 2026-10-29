from PIL import Image, ImageDraw, ImageFont
import urllib.request, io, os
P='/home/user/elvo-creating/brands/elvo/brand-identity/product-images/'
OUT='/home/user/elvo-creating/brands/elvo/yavendio/imagenes/'
F='/usr/share/fonts/opentype/inter/Inter-%s.otf'
def f(w,s): return ImageFont.truetype(F%w,s)
W,H=1080,1350
BLUE=(51,85,255); INK=(5,6,7); GRAY=(91,100,112); BG=(238,243,247); ICE=(220,230,238); PET=(10,42,51); RED=(200,60,60)

def new():
    im=Image.new('RGB',(W,H),BG); return im,ImageDraw.Draw(im)
def save(im,name):
    im.save(OUT+name+'.jpg',quality=92); im.save(OUT+name+'.png'); print(name)
def wrap(d,t,font,mw):
    out=[];cur=''
    for w in t.split():
        c=(cur+' '+w).strip()
        if d.textlength(c,font=font)<=mw: cur=c
        else: out.append(cur);cur=w
    out.append(cur);return out
def check(d,x,y,s,col):
    d.line([(x,y+s*0.55),(x+s*0.35,y+s*0.9),(x+s,y+s*0.1)],fill=col,width=8,joint='curve')
def cross(d,x,y,s,col):
    d.line([(x,y),(x+s,y+s)],fill=col,width=8); d.line([(x+s,y),(x,y+s)],fill=col,width=8)
def rmask(size,r):
    m=Image.new('L',size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,size[0],size[1]),radius=r,fill=255); return m

# 1) 6 etapas (reemplaza 2-seis-etapas-nativo: sin KDF, sin mercurio, sin pH)
old=Image.open('/tmp/claude-0/-home-user-elvo-creating/69d2e9fd-2a2e-57c3-8d73-f0d56567189d/scratchpad/dl/2-seis-etapas-nativo.jpg').convert('RGB')
cart=old.crop((484,182,670,950)).convert('RGB')
_p=cart.load(); _w,_h=cart.size
# espejar la pared izquierda sobre la derecha para borrar los puntos y guías azules
for _y in range(_h):
    for _k in range(34):
        _p[_w-1-_k,_y]=_p[_k,_y]
im,d=new()
d.text((W/2,92),'6 etapas por dentro',font=f('Bold',68),fill=INK,anchor='mm')
d.text((W/2,152),'elvo· Nativo, directo de tu caño',font=f('Regular',32),fill=GRAY,anchor='mm')
ch=1000; s=ch/cart.height; c2=cart.resize((round(cart.width*s),ch),Image.LANCZOS)
d.rounded_rectangle((60,215,60+c2.width+70,215+ch+40),radius=36,fill='white',outline=ICE,width=3)
im.paste(c2,(95,235))
rows=[('Carbón activado','Reduce cloro, olores y mal sabor'),
      ('Retiene metales pesados','Como arsénico y plomo'),
      ('Plata coloidal','Cuida el agua de bacterias y microorganismos'),
      ('Nanotecnología','Atrapa microplásticos y partículas finas'),
      ('Aluminosilicato','Agua más clara'),
      ('Plata iónica','Mantiene el agua más pura por más tiempo')]
x0=60+c2.width+110; y=215; rh=(ch+40)/6
for i,(t,sub) in enumerate(rows):
    cy=y+rh*i+rh/2
    d.ellipse((x0,cy-30,x0+60,cy+30),fill=BLUE); d.text((x0+30,cy),str(i+1),font=f('Bold',34),fill='white',anchor='mm')
    d.text((x0+85,cy-20),t,font=f('Bold',36),fill=INK,anchor='lm')
    ls=wrap(d,sub,f('Regular',27),W-60-(x0+85)-10)
    for j,l in enumerate(ls): d.text((x0+85,cy+14+j*32),l,font=f('Regular',27),fill=GRAY,anchor='lm')
d.text((W/2,H-62),'Y conserva los minerales buenos del agua',font=f('Bold',34),fill=BLUE,anchor='mm')
save(im,'etapas-nativo-6')

# 2) cuotas
im,d=new()
d.text((W/2,100),'Paga en 6 cuotas',font=f('Bold',74),fill=INK,anchor='mm')
d.text((W/2,182),'sin intereses',font=f('Bold',74),fill=BLUE,anchor='mm')
d.text((W/2,250),'Con tarjeta de crédito · nosotros cubrimos los intereses',font=f('Regular',31),fill=GRAY,anchor='mm')
def cuota(y,h,badge,title,line,cuota_,total,hl):
    d.rounded_rectangle((60,y,W-60,y+h),radius=36,fill='white',outline=BLUE if hl else ICE,width=6 if hl else 3)
    bw=d.textlength(badge,font=f('Bold',26))+48
    d.rounded_rectangle((W-90-bw,y-22,W-90,y+26),radius=24,fill=BLUE if hl else PET)
    d.text((W-90-bw/2,y+2),badge,font=f('Bold',26),fill='white',anchor='mm')
    d.text((100,y+75),title,font=f('Bold',52),fill=INK,anchor='ls')
    d.text((100,y+125),line,font=f('Medium',30),fill=GRAY,anchor='ls')
    d.text((100,y+h-138),'6 cuotas de',font=f('Medium',32),fill=GRAY,anchor='ls')
    d.text((100,y+h-34),cuota_,font=f('Bold',92),fill=BLUE,anchor='ls')
    d.text((W-100,y+h-40),'Total '+total,font=f('Medium',32),fill=GRAY,anchor='rs')
cuota(330,400,'Mayor valor · solo Cyber','Combo 6 años','1 purificador + 3 repuestos','S/81.50','S/489',True)
cuota(790,400,'Solo por Cyber','Combo 3 años','1 purificador + 1 kit de repuesto','S/58.17','S/349',False)
d.text((W/2,1250),'Con débito no hay cuotas · Pides el link de pago por aquí',font=f('Medium',28),fill=GRAY,anchor='mm')
d.text((W/2,1295),'Precios solo por Cyber, hasta el 1 de noviembre',font=f('Medium',28),fill=GRAY,anchor='mm')
save(im,'cuotas-sin-intereses')

# 3) elvo· Cero
cero=Image.open('/tmp/claude-0/-home-user-elvo-creating/69d2e9fd-2a2e-57c3-8d73-f0d56567189d/scratchpad/dl/cero.png').convert('RGB')
im,d=new()
d.text((60,92),'elvo· Cero',font=f('Bold',72),fill=INK,anchor='lm')
d.text((60,160),'Ósmosis inversa con agua fría y caliente',font=f('Medium',34),fill=BLUE,anchor='lm')
pw=1080-120; ph=500
bgc=cero.getpixel((10,10))
panel=Image.new('RGB',(pw,ph),bgc)
cc=cero.crop((185,175,835,905)); prod=cc.resize((round(cc.width*ph/cc.height),ph),Image.LANCZOS)
panel.paste(prod,((pw-prod.width)//2,0))
im.paste(panel,(60,200),rmask((pw,ph),32))
items=[('Fría a 6–7 °C','y caliente en 7 temperaturas, lista en 2 segundos'),
       ('Ósmosis inversa de 5 etapas','con esterilización UV y autolimpieza'),
       ('Sin instalación','Enchufas (110 a 240 V) y llenas el tanque'),
       ('Garantía de 1 año','Te avisamos cuándo cambiar los filtros (kit S/329)')]
y=730
for t,sub in items:
    check(d,70,y+4,34,BLUE)
    d.text((125,y+2),t,font=f('Bold',37),fill=INK,anchor='lm'); d.text((125,y+42),sub,font=f('Regular',28),fill=GRAY,anchor='lm'); y+=100
d.rounded_rectangle((60,H-175,W-60,H-45),radius=30,fill=PET)
d.text((100,H-110),'Precio Cyber',font=f('Medium',34),fill='white',anchor='lm')
d.text((W-100,H-110),'S/1,799',font=f('Bold',84),fill='white',anchor='rm')
save(im,'cero-ficha')

# 4) hoy vs elvo
im,d=new()
d.text((W/2,100),'Tu agua de hoy',font=f('Bold',64),fill=INK,anchor='mm')
d.text((W/2,172),'vs agua elvo· directo del caño',font=f('Bold',64),fill=BLUE,anchor='mm')
def col(x,w,title,rows,good):
    d.rounded_rectangle((x,260,x+w,1130),radius=36,fill='white',outline=BLUE if good else ICE,width=6 if good else 3)
    d.text((x+w/2,325),title,font=f('Bold',40),fill=BLUE if good else INK,anchor='mm')
    yy=410
    for t in rows:
        ls=wrap(d,t,f('Medium',33),w-130)
        (check if good else cross)(d,x+34,yy+6,36,BLUE if good else RED)
        for j,l in enumerate(ls): d.text((x+96,yy+j*42),l,font=f('Medium',33),fill=INK)
        yy+=len(ls)*42+58
col(60,455,'Hoy',['Cargar bidones','Comprar agua cada semana','Hervir y esperar a que enfríe','Gastar en gas y en agua'],False)
col(565,455,'Con elvo· Nativo',['Agua de calidad como la embotellada','Directo de tu caño','1 filtro = unos 1.000 bidones de agua','Se conecta al caño en 5 minutos'],True)
d.text((W/2,1210),'Cada filtro dura unos 18 meses y te avisamos cuándo cambiarlo',font=f('Medium',29),fill=GRAY,anchor='mm')
d.text((W/2,1260),'30 días de prueba · 1 año de garantía',font=f('Bold',32),fill=INK,anchor='mm')
save(im,'hoy-vs-elvo')
