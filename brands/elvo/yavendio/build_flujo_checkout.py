from PIL import Image, ImageDraw, ImageFont
import math
F='/usr/share/fonts/opentype/inter/Inter-%s.otf'
def f(w,s): return ImageFont.truetype(F%w,s)
W,H=2300,1560
BLUE=(51,85,255); INK=(5,6,7); GRAY=(91,100,112); BG=(238,243,247); ICE=(220,230,238); PET=(10,42,51); GREEN=(32,140,90); AMB=(232,150,20)
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
def wrap(t,font,mw):
    out=[];cur=''
    for w in t.split():
        c=(cur+' '+w).strip()
        if d.textlength(c,font=font)<=mw: cur=c
        else: out.append(cur);cur=w
    out.append(cur);return out
def arrow(x1,y1,x2,y2,col=GRAY,lw=6):
    d.line((x1,y1,x2,y2),fill=col,width=lw)
    a=math.atan2(y2-y1,x2-x1); s=20
    d.polygon([(x2,y2),(x2-s*math.cos(a-0.45),y2-s*math.sin(a-0.45)),(x2-s*math.cos(a+0.45),y2-s*math.sin(a+0.45))],fill=col)
def step(x,y,w,h,n,title,sub,col=BLUE):
    d.rounded_rectangle((x,y,x+w,y+h),radius=24,fill='white',outline=col,width=5)
    d.ellipse((x+16,y+16,x+68,y+68),fill=col); d.text((x+42,y+42),str(n),font=f('Bold',30),fill='white',anchor='mm')
    yy=y+30
    for l in wrap(title,f('Bold',27),w-110): d.text((x+84,yy),l,font=f('Bold',27),fill=INK); yy+=34
    yy=max(yy,y+86)+8
    for l in wrap(sub,f('Regular',23),w-40): d.text((x+22,yy),l,font=f('Regular',23),fill=GRAY); yy+=29
def lane(y,h,title,tag,col):
    d.rounded_rectangle((40,y,W-40,y+h),radius=30,fill=(247,250,252),outline=col,width=4)
    d.rounded_rectangle((40,y,W-40,y+64),radius=30,fill=col); d.rectangle((40,y+34,W-40,y+64),fill=col)
    d.text((80,y+33),title,font=f('Bold',34),fill='white',anchor='lm')
    d.text((W-80,y+33),tag,font=f('Medium',27),fill='white',anchor='rm')

d.text((W/2,66),'Checkout de Sofía',font=f('Bold',64),fill=INK,anchor='mm')
d.text((W/2,128),'Cómo pasa de «sí, lo quiero» a pedido registrado',font=f('Regular',32),fill=GRAY,anchor='mm')

# entrada
d.rounded_rectangle((60,180,640,250),radius=34,fill=PET); d.text((350,215),'Cliente dice «sí» o da su dirección',font=f('Medium',28),fill='white',anchor='mm')
arrow(645,215,760,215)
d.rounded_rectangle((765,170,1480,260),radius=34,fill='white',outline=BLUE,width=5)
d.text((1122,215),'«¡Excelente elección! ¿Para dónde lo deseas?»',font=f('Bold',28),fill=INK,anchor='mm')
d.text((1530,262),'Con la ciudad o el distrito basta',font=f('Regular',25),fill=GRAY,anchor='lm')

# Lima
ly=320; lh=330
lane(ly,lh,'LIMA Y CALLAO','Paga al recibir · camino corto',GREEN)
arrow(900,262,900,ly-2,GREEN)
d.text((930,292),'Lima o Callao',font=f('Medium',24),fill=GREEN,anchor='lm')
bw=480; gap=70; x=70; yy=ly+95; bh=215
L=[('«En Lima pagas al recibir»','Pide los datos en un solo mensaje'),
   ('Datos del cliente','Nombre completo, dirección con distrito, teléfono de entrega y boleta o factura'),
   ('Registro inmediato','Con nombre, dirección y celular registra el pedido en ese mismo turno, sin resumen'),
   ('Mensaje de confirmación','«¡Listo, {nombre}! Tu pedido quedó registrado». El courier coordina el día')]
bw=490; gap=60
for i,(t,s) in enumerate(L):
    xx=70+i*(bw+gap); step(xx,yy,bw,bh,i+1,t,s,GREEN if i<3 else GREEN)
    if i<3: arrow(xx+bw+4,yy+bh/2,xx+bw+gap-4,yy+bh/2,GREEN)

# Provincia
py=700; ph=560
lane(py,ph,'PROVINCIA','Adelanto de S/20 (Shalom) o total (domicilio)',BLUE)
d.line((1482,215,2282,215),fill=BLUE,width=6); d.line((2282,215,2282,py-4),fill=BLUE,width=6)
arrow(2282,py-40,2282,py-2,BLUE)
d.text((2270,250),'Fuera de Lima',font=f('Medium',24),fill=BLUE,anchor='rm')
P=[('Elige cómo recibirlo','«¿A tu casa o lo recoges en tu Shalom más cercano?»'),
   ('Datos de entrega','En un solo mensaje. Shalom: agencia, nombre y DNI de quien recoge, celular. Domicilio: nombre, dirección con ciudad, DNI, celular'),
   ('¿Con cuál paga?','Pregunta sin dar números: Yape/Plin, transferencia o tarjeta (solo domicilio)'),
   ('Datos de ese medio','Envía solo los del medio elegido y pide la captura. Shalom: S/20. Domicilio: el total'),
   ('Resumen','Con la captura, resumen en viñetas y «¿Confirmo tu pedido?»'),
   ('Registro','Con el sí del cliente, registra el pedido una sola vez')]
bw=330; gap=40; yy=py+95; bh=300
for i,(t,s) in enumerate(P):
    xx=70+i*(bw+gap); step(xx,yy,bw,bh,i+1,t,s,BLUE if i<5 else GREEN)
    if i<5: arrow(xx+bw+3,yy+bh/2,xx+bw+gap-3,yy+bh/2,BLUE)
# notas inferiores en provincia
ny=py+415
d.rounded_rectangle((70,ny,1100,ny+125),radius=22,fill='white',outline=AMB,width=4)
d.text((92,ny+32),'Shalom: el saldo',font=f('Bold',27),fill=AMB,anchor='lm')
for j,l in enumerate(wrap('El cliente yapea el saldo (S/329 en el combo de 3 años, S/469 en el de 6) cuando el pedido llega a su agencia y manda la captura; con eso recibe la clave de recojo.',f('Regular',23),980)):
    d.text((92,ny+66+j*29),l,font=f('Regular',23),fill=GRAY,anchor='lm')
d.rounded_rectangle((1150,ny,2230,ny+125),radius=22,fill='white',outline=BLUE,width=4)
d.text((1172,ny+32),'Domicilio: con tarjeta',font=f('Bold',27),fill=BLUE,anchor='lm')
for j,l in enumerate(wrap('El link de pago de Mercado Pago sale al registrar el pedido y el banco divide el total en hasta 6 cuotas sin intereses.',f('Regular',23),1030)):
    d.text((1172,ny+66+j*29),l,font=f('Regular',23),fill=GRAY,anchor='lm')

# pie
fy=1290
d.rounded_rectangle((40,fy,W-40,fy+210),radius=30,fill='white',outline=ICE,width=4)
d.text((80,fy+40),'Pasa a una persona del equipo',font=f('Bold',32),fill=INK,anchor='lm')
items=['Más de 1 purificador (S/99 de descuento por cada adicional)','Un producto con precio distinto al del catálogo','Cliente que quiere recoger en Jr. Quilca 565, Breña','Cualquier falla del registro']
for i,t in enumerate(items):
    cx=80+(i%2)*1100; cy=fy+95+(i//2)*50
    d.ellipse((cx,cy-9,cx+18,cy+9),fill=AMB); d.text((cx+34,cy),t,font=f('Medium',25),fill=GRAY,anchor='lm')
d.text((60,H-22),'Verde: Lima y registro · Azul: provincia · Ámbar: notas',font=f('Medium',22),fill=GRAY,anchor='lm')
im.save('/home/user/elvo-creating/brands/elvo/yavendio/imagenes/flujo-checkout-sofia.png'); print('ok')
