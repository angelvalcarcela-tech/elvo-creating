from PIL import Image, ImageDraw, ImageFont
import math
F='/usr/share/fonts/opentype/inter/Inter-%s.otf'
def f(w,s): return ImageFont.truetype(F%w,s)
W,H=2300,1560
BLUE=(51,85,255); INK=(5,6,7); GRAY=(91,100,112); BG=(238,243,247); ICE=(220,230,238); PET=(10,42,51); RED=(214,56,56); GREEN=(32,140,90); AMB=(232,150,20)
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
def wrap(t,font,mw):
    out=[];cur=''
    for w in t.split():
        c=(cur+' '+w).strip()
        if d.textlength(c,font=font)<=mw: cur=c
        else: out.append(cur);cur=w
    out.append(cur);return out
def box(x,y,w,h,title,lines,col=BLUE):
    d.rounded_rectangle((x,y,x+w,y+h),radius=26,fill='white',outline=col,width=5)
    d.rounded_rectangle((x,y,x+w,y+70),radius=26,fill=col); d.rectangle((x,y+44,x+w,y+70),fill=col)
    d.text((x+w/2,y+36),title,font=f('Bold',30 if len(title)<20 else 25),fill='white',anchor='mm')
    yy=y+92
    for l in lines:
        for s_ in wrap(l,f('Regular',24),w-44):
            d.text((x+22,yy),s_,font=f('Regular',24),fill=INK); yy+=31
        yy+=9
def arrow(x1,y1,x2,y2,col=GRAY,lw=6):
    d.line((x1,y1,x2,y2),fill=col,width=lw)
    a=math.atan2(y2-y1,x2-x1); s_=20
    d.polygon([(x2,y2),(x2-s_*math.cos(a-0.45),y2-s_*math.sin(a-0.45)),(x2-s_*math.cos(a+0.45),y2-s_*math.sin(a+0.45))],fill=col)
def pill(cx,cy,text,col=GRAY,w=150):
    ls=wrap(text,f('Medium',20),w-10); h=len(ls)*26+14
    d.rounded_rectangle((cx-w/2,cy-h/2,cx+w/2,cy+h/2),radius=14,fill=BG,outline=ICE,width=2)
    for i,l in enumerate(ls): d.text((cx,cy-h/2+7+13+i*26),l,font=f('Medium',20),fill=col,anchor='mm')
def badge(x,y,n,col=RED):
    d.ellipse((x-24,y-24,x+24,y+24),fill=col); d.text((x,y),str(n),font=f('Bold',30),fill='white',anchor='mm')

d.text((W/2,70),'Flujo de venta de Sofía',font=f('Bold',64),fill=INK,anchor='mm')
d.text((W/2,132),'Qué hace en cada etapa y dónde está fallando hoy',font=f('Regular',32),fill=GRAY,anchor='mm')

bw=300; gap=160; y0=290; bh=400
xs=[60+i*(bw+gap) for i in range(5)]
d.rounded_rectangle((xs[0],175,xs[0]+bw,235),radius=28,fill=PET); d.text((xs[0]+bw/2,205),'Cliente del anuncio',font=f('Medium',26),fill='white',anchor='mm')
arrow(xs[0]+bw/2,235,xs[0]+bw/2,y0-4)
data=[('1 · SALUDO',['Mira cómo llegó el cliente.','Anuncio con combo: va directo a la venta.','Saludo simple: catálogo y 1 pregunta.','No pide el distrito todavía.'],BLUE),
 ('2 · CATÁLOGO',['Recomienda Nativo, Alivio o Cero.','Sugiere primero el combo de 6 años.','Responde en 1 burbuja corta y cierra con pregunta.','Foto o video antes que texto largo.'],BLUE),
 ('3 · CARRITO',['«¿Para dónde lo deseas?»','Lima: datos en 1 mensaje, se registra y paga al recibir.','Provincia: Shalom con S/20 o a domicilio pagando todo.'],BLUE),
 ('4 · CONFIRMACIÓN',['Pedido registrado.','Da el seguimiento y cuándo llega.'],GREEN),
 ('5 · ENTREGA',['Posventa: estado, reprogramar, instalación y garantía.','Sin preguntas de relleno.'],BLUE)]
for i,(t,ls,c) in enumerate(data): box(xs[i],y0,bw,bh,t,ls,c)
conds=['pregunta producto o precio, o quiere comprar','elige y da su dirección','pedido registrado','consulta su entrega']
for i in range(4):
    arrow(xs[i]+bw+6,y0+190,xs[i+1]-6,y0+190)
    pill(xs[i]+bw+gap/2,y0+250,conds[i],w=150)

y1=800
box(xs[0],y1,bw+60,235,'GARANTÍA Y DEVOLUCIÓN',['Su producto falla, gotea o llegó incompleto.','Recoge evidencia y lo pasa a una persona.'],AMB)
arrow(xs[0]+bw/2,y0+bh+6,xs[0]+bw/2,y1-6,AMB)
box(xs[1],y1,bw+60,235,'DESPEDIDA',['Una sola despedida.','Cuando dice «lo pienso» o agradece.'],GRAY)
arrow(xs[1]+bw/2,y0+bh+6,xs[1]+bw/2,y1-6,GRAY)
d.text((xs[2]+30,y1+100),'← también llega a Despedida desde Confirmación y Entrega,',font=f('Regular',24),fill=GRAY,anchor='lm')
d.text((xs[2]+30,y1+135),'y a Garantía desde Entrega',font=f('Regular',24),fill=GRAY,anchor='lm')

badge(xs[1]+bw-6,y0+6,1); badge(xs[1]+bw-6,y0+bh-6,2); badge(xs[0]+bw-6,y0+6,3)

py=1090
d.rounded_rectangle((60,py,W-60,py+400),radius=30,fill='white',outline=RED,width=6)
d.text((100,py+46),'Lo que está fallando',font=f('Bold',40),fill=RED,anchor='lm')
items=[(1,'Link en el primer mensaje y al final del turno','La etapa Catálogo decía «con el link». Ya está corregido en el archivo nuevo: súbelo y publica.'),
       (2,'Imagen de combos vieja (12 oct, «18 meses»)','La nueva no está en YaVendio. Súbela con el mismo nombre y cambia la descripción.'),
       (3,'«Queda anotado, te avisamos cuando esté disponible»','Un cliente respondió a un mensaje de preventa. Regla nueva en el archivo: «¡Ya lo tenemos disponible!».')]
cw=(W-120-80)/3
for i,(n,t,s_) in enumerate(items):
    cx=100+i*(cw+20)
    badge(cx+24,py+130,n)
    for j,l in enumerate(wrap(t,f('Bold',29),cw-80)): d.text((cx+66,py+112+j*36),l,font=f('Bold',29),fill=INK,anchor='lm')
    yy=py+205
    for l in wrap(s_,f('Regular',25),cw-30): d.text((cx,yy),l,font=f('Regular',25),fill=GRAY,anchor='lm'); yy+=32
d.text((100,py+365),'Fuera del flujo, también por arreglar: recordatorios con textos viejos y anuncios que dicen «pago contraentrega».',font=f('Medium',25),fill=INK,anchor='lm')
d.text((60,H-28),'Azul: etapa de venta · Verde: pedido registrado · Ámbar: caso especial · Rojo: falla',font=f('Medium',22),fill=GRAY,anchor='lm')
im.save('/home/user/elvo-creating/brands/elvo/yavendio/imagenes/flujo-venta-sofia.png'); print('ok')
