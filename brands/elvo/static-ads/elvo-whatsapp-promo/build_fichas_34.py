from PIL import Image, ImageDraw, ImageFont
F='/usr/share/fonts/opentype/inter/Inter-%s.otf'
def f(w,s): return ImageFont.truetype(F%w,s)
W,H=1080,1440
BLUE=(37,99,235); DARK=(28,34,44); PILL=(0,43,54); BAND=(225,232,238)
def wrap(d,t,font,mw):
    out=[];cur=''
    for w in t.split():
        c=(cur+' '+w).strip()
        if d.textlength(c,font=font)<=mw: cur=c
        else: out.append(cur);cur=w
    out.append(cur);return out
P={
 'nativo18':dict(src='nativo18-ficha-promo_v2.png',photo=(607,178,1080,1218),focus=1.0,pill=('Purificador de Agua','elvo· Nativo 18 meses'),promo='S/ 349',
   inc=['Purificador Nativo','1 núcleo PureCore (18 meses)','Adaptador universal y derivador','30 días de prueba'],
   why=['Envíos a todo el Perú','Pago contraentrega','Te avisamos por WhatsApp cuándo cambiar el núcleo'],title='¿Por qué elegir Nativo?',
   icons=[(88,1048,50),(230,1048,50),(380,1048,50),(520,1048,50)],caps=['Retiene plomo y metales pesados','Lo instalas en 5 minutos','Sin electricidad ni gasfitero','Reduce cloro, olores y sabores']),
 'nativo3a':dict(src='nativo3a-ficha-promo_v2.png',photo=(607,163,1080,1186),focus=1.0,pill=('Purificador de Agua','elvo· Nativo 3 años'),promo='S/ 349',
   inc=['Purificador Nativo con núcleo instalado','1 núcleo PureCore de repuesto','Adaptador universal y derivador','30 días de prueba'],
   why=['Envíos a todo el Perú','Pago contraentrega','Te avisamos por WhatsApp cuándo cambiar el núcleo'],title='¿Por qué elegir Nativo?',
   icons=[(87,1033,50),(227,1033,50),(367,1033,50),(507,1033,50)],caps=['Retiene plomo y metales pesados','Lo instalas en 5 minutos','Sin electricidad ni gasfitero','Reduce cloro, olores y sabores']),
 'nativo6a':dict(src='nativo6a-ficha-promo_v2.png',photo=(538+160,223,1057,1101),focus=1.0,pill=('Purificador de Agua','elvo· Nativo 6 años'),promo='S/ 489',
   inc=['Purificador Nativo con núcleo instalado','3 núcleos PureCore de repuesto','Adaptador universal y derivador','30 días de prueba'],
   why=['Envíos a todo el Perú','Pago contraentrega','Te avisamos por WhatsApp cuándo cambiar el núcleo'],title='¿Por qué elegir Nativo?',
   icons=[(76,950,42),(333,946,42),(74,1027,42),(337,1027,42)],caps=['Retiene plomo y metales pesados','Lo instalas en 5 minutos','Sin electricidad ni gasfitero','Reduce cloro, olores y sabores']),
 'alivio16':dict(src='alivio16-ficha-promo_v2.png',photo=(583,141,1080,1190),focus=1.0,pill=('Purificador de Agua','Alivio 16'),promo='S/ 159',
   inc=['Purificador de 16 litros','Filtro interno incluido','Gotas de pH','Garantía de 6 meses'],
   why=['Envíos a todo el Perú','Pago contraentrega','30 días de prueba'],title='¿Por qué elegir Alivio?',
   icons=[(87,1028,50),(227,1028,50),(367,1028,50),(507,1028,50)],caps=['Sin electricidad','Se llena con una jarra','7 etapas de filtrado','Fácil de armar']),
 'alivio22':dict(src='alivio22-ficha-promo_v2.png',photo=(593,88,1080,1248),focus=1.0,pill=('Purificador de Agua','Alivio 22'),promo='S/ 198',
   inc=['Purificador de 22 litros','Filtro interno incluido','Gotas de pH','Garantía de 6 meses'],
   why=['Envíos a todo el Perú','Pago contraentrega','30 días de prueba'],title='¿Por qué elegir Alivio?',
   icons=[(95,1047,50),(233,1047,50),(374,1047,50),(506,1047,50)],caps=['Sin electricidad','Se llena con una jarra','7 etapas de filtrado','Fácil de armar']),
}
PW=500  # ancho foto
for k,c in P.items():
    src=Image.open(c['src']).convert('RGB'); bg=src.getpixel((300,1000)) if k=='nativo6a' else src.getpixel((8,8))
    im=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(im)
    # foto a sangre
    if k=='nativo6a':
        ph=src.crop((538+160,223,1057,1101)); s=PW/ph.width; ph=ph.resize((PW,round(ph.height*s)),Image.LANCZOS)
        from PIL import ImageFilter, ImageOps
        gap=H-ph.height; top=ImageOps.flip(ph.crop((0,0,PW,gap))).filter(ImageFilter.GaussianBlur(6))
        full=Image.new('RGB',(PW,H)); full.paste(top,(0,0)); full.paste(ph,(0,gap))
        m=Image.linear_gradient('L').resize((PW,60)); seam=Image.composite(full.crop((0,gap,PW,gap+60)),top.crop((0,gap-60,PW,gap)) if gap>=60 else full.crop((0,gap,PW,gap+60)),m)
        full.paste(seam,(0,gap)); im.paste(full,(W-PW,0))
        ph=None
    else:
      ph=src.crop(c['photo']); s=H/ph.height; ph=ph.resize((round(ph.width*s),H),Image.LANCZOS)
      x0=round((ph.width-PW)*{'nativo18':.5,'nativo3a':.45,'nativo6a':0,'alivio16':.5,'alivio22':.5}[k])
      ph=ph.crop((x0,0,x0+PW,H)); im.paste(ph,(W-PW,0))
    L=36; RW=W-PW-L-24
    # pill
    y=78; f1,f2=f('Bold',30),f('Bold',38)
    d.rounded_rectangle((L,y,L+RW,y+132),radius=44,fill=PILL)
    d.text((L+RW/2,y+40),c['pill'][0],font=f1,fill='white',anchor='mm')
    d.text((L+RW/2,y+90),c['pill'][1],font=f2,fill='white',anchor='mm')
    y+=132+24
    d.text((L,y),'Promo: '+c['promo'],font=f('Bold',72),fill=BLUE); y+=112
    d.text((L,y),'Incluye:',font=f('Bold',38),fill=BLUE); y+=58
    ft=f('Regular',30)
    for i,t in enumerate(c['inc']):
        ls=wrap(d,f'{i+1}.  {t}',ft,RW-6)
        for j,l in enumerate(ls):
            d.text((L+(0 if j==0 else 38),y),l,font=ft,fill=DARK); y+=40
        y+=8
    y+=14
    by=y; bh=282
    d.rectangle((0,by,W-PW,by+bh),fill=BAND)
    y=by+24
    d.text((L,y),'¿Por qué elvo·?',font=f('Bold',38),fill=BLUE); y+=62
    for i,t in enumerate(c['why']):
        ls=wrap(d,f'{i+1}.  {t}',ft,RW-6)
        for j,l in enumerate(ls):
            d.text((L+(0 if j==0 else 38),y),l,font=ft,fill=DARK); y+=40
        y+=8
    y=by+bh+30
    d.text((L,y),c['title'],font=f('Bold',36),fill=BLUE); y+=62
    # iconos en 4 filas
    fc=f('Medium',27)
    for i,((cx,cy,r),cap) in enumerate(zip(c['icons'],c['caps'])):
        ic=src.crop((cx-r,cy-r,cx+r,cy+r)).resize((72,72),Image.LANCZOS)
        iy=y+i*84
        im.paste(ic,(L,iy))
        d.text((L+92,iy+36),cap,font=fc,fill=DARK,anchor='lm')
    print(k,'fin',y+4*84)
    im.save(k+'-ficha-promo_v3_34.png')
