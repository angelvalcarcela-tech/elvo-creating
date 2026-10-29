from PIL import Image, ImageDraw, ImageFont
P='/home/user/elvo-creating/brands/elvo/brand-identity/product-images/'
F='/usr/share/fonts/opentype/inter/Inter-%s.otf'
def f(w,s): return ImageFont.truetype(F%w,s)
W,H=1080,1350
BLUE=(51,85,255); INK=(5,6,7); GRAY=(91,100,112); BG=(238,243,247); ICE=(220,230,238); PET=(10,42,51)
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
eq=Image.open(P+'nativo-equipo-web.png').convert('RGB').crop((250,180,800,950))
nu=Image.open(P+'nativo-repuesto-nucleo.png').convert('RGB').crop((215,30,385,570))
logo=Image.open(P+'elvo-logo-trim.png').convert('RGBA')
d.text((W/2,92),'Combos elvo· Nativo',font=f('Bold',64),fill=INK,anchor='mm')
d.text((W/2,150),'Pagas una sola vez y el purificador es tuyo',font=f('Regular',32),fill=GRAY,anchor='mm')
def keyout(img):
    img=img.convert('RGBA'); px=img.load(); w,h=img.size; bgc=px[3,h//2][:3]
    for yy in range(h):
        for xx in range(w):
            r,g,b,a=px[xx,yy]
            if abs(r-bgc[0])<38 and abs(g-bgc[1])<38 and abs(b-bgc[2])<38 and (r-b)>18: px[xx,yy]=(255,255,255,0)
    return img
nuk=keyout(nu)
def rmask(size,r):
    m=Image.new('L',size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,size[0],size[1]),radius=r,fill=255); return m
def card(y,h,badge,title,line,price,nrep,hl,valor=''):
    d.rounded_rectangle((60,y,W-60,y+h),radius=36,fill='white',outline=BLUE if hl else ICE,width=6 if hl else 3)
    bw=d.textlength(badge,font=f('Bold',26))+48
    d.rounded_rectangle((W-60-bw-30,y-22,W-60-30,y+26),radius=24,fill=BLUE if hl else PET)
    d.text((W-60-30-bw/2,y+2),badge,font=f('Bold',26),fill='white',anchor='mm')
    # texto a la izquierda
    d.text((95,y+70),title,font=f('Bold',50),fill=INK,anchor='ls')
    ft=f('Medium',29); ls=[l for l in line.split('|')]
    for i,l in enumerate(ls): d.text((95,y+118+i*40),l,font=ft,fill=GRAY,anchor='ls')
    d.text((95,y+h-150),'Valor sin promo '+valor,font=f('Medium',28),fill=GRAY,anchor='ls')
    wv=d.textlength('Valor sin promo '+valor,font=f('Medium',28)); d.line((95+d.textlength('Valor sin promo ',font=f('Medium',28)),y+h-160,95+wv,y+h-160),fill=GRAY,width=3)
    d.text((95,y+h-48),price,font=f('Bold',96),fill=BLUE,anchor='ls')
    # visuales a la derecha
    pw,ph=500,h-60; px0=W-60-30-pw; py0=y+30
    panel=Image.new('RGB',(pw,ph),(222,231,239)); 
    e=eq.copy(); s_=ph*0.80/e.height; e=e.resize((round(e.width*s_),round(ph*0.80)),Image.LANCZOS)
    n=nuk.crop((10,0,nuk.width-10,nuk.height)); nh=ph*0.50; s2=nh/n.height; n=n.resize((round(n.width*s2),round(nh)),Image.LANCZOS)
    total=e.width+30+nrep*(n.width+4)
    x=(pw-total)//2
    ex=Image.new('RGB',e.size,(222,231,239)); 
    panel.paste(e,(x,int(ph*0.12))); x+=e.width
    pd=ImageDraw.Draw(panel); pd.text((x+15,ph//2),'+',font=f('Bold',44),fill=BLUE,anchor='mm'); x+=30
    for i in range(nrep):
        panel.paste(n,(x+i*(n.width+4),int((ph-nh)/2)+10),n)
    im.paste(panel,(px0,py0),rmask((pw,ph),28))
card(215,470,'Mayor valor','Combo 6 años','1 purificador|+ 3 repuestos','S/489',3,True,'S/896')
card(745,430,'Precio Cyber','Combo 3 años','1 purificador|+ 1 kit de repuesto','S/349',1,False,'S/498')
d.text((W/2,1230),'Repuesto suelto S/199 · cada núcleo rinde 20.000 litros (unos 18 meses)',font=f('Medium',28),fill=GRAY,anchor='mm')
d.text((W/2,1275),'Pago contraentrega · 30 días de prueba',font=f('Medium',28),fill=GRAY,anchor='mm')
im.save('imagenes/combos-elvo-nativo.jpg',quality=92); im.save('imagenes/combos-elvo-nativo.png')
print('ok')
