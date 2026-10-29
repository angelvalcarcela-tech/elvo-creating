from PIL import Image, ImageDraw, ImageFont
F='/usr/share/fonts/opentype/inter/Inter-%s.otf'
def f(w,s): return ImageFont.truetype(F%w,s)
W,H=1080,1130
BLUE=(51,85,255); INK=(5,6,7); GRAY=(91,100,112); BG=(238,243,247); ICE=(220,230,238); PET=(10,42,51)
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
def wrap(t,font,mw):
    out=[];cur=''
    for w in t.split():
        c=(cur+' '+w).strip()
        if d.textlength(c,font=font)<=mw: cur=c
        else: out.append(cur);cur=w
    out.append(cur);return out
d.text((W/2,96),'Lo que dicen quienes',font=f('Bold',60),fill=INK,anchor='mm')
d.text((W/2,164),'ya tienen su elvo· Nativo',font=f('Bold',60),fill=BLUE,anchor='mm')
R=[('El agua sale cristalina, sin sabor ni olor.','Carmen S.','Trujillo'),
   ('Lo instalé en menos de 5 minutos, funciona perfecto y tiene muy buen caudal.','Lucía P.','Ica'),
   ('El agua sale transparente, sin sabor y sin ningún residuo. La instalación fue muy fácil.','María G.','Lima')]
y=250
for q,a,c in R:
    ft=f('Medium',38); ls=wrap('“'+q+'”',ft,W-2*60-80)
    h=60+len(ls)*54+80
    d.rounded_rectangle((60,y,W-60,y+h),radius=32,fill='white',outline=ICE,width=3)
    d.rounded_rectangle((60,y,72,y+h),radius=6,fill=BLUE)
    yy=y+38
    for l in ls: d.text((110,yy),l,font=ft,fill=INK); yy+=54
    d.text((110,yy+10),f'{a} · {c}',font=f('Bold',30),fill=BLUE)
    vt='Cliente verificado'; vw=d.textlength(vt,font=f('Medium',26))+36
    d.rounded_rectangle((W-90-vw,yy+4,W-90,yy+50),radius=23,fill=PET)
    d.text((W-90-vw/2,yy+27),vt,font=f('Medium',26),fill='white',anchor='mm')
    y+=h+30
d.text((W/2,H-80),'30 días de prueba · Pago contraentrega',font=f('Medium',30),fill=GRAY,anchor='mm')
im.save('imagenes/resenas-clientes-elvo.jpg',quality=92); im.save('imagenes/resenas-clientes-elvo.png'); print(y)
