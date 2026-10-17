from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
W,H=A4
ALAB=HexColor('#EAE7E0');CAL=HexColor('#D8D2C7');PIE=HexColor('#9A948A');PIZ=HexColor('#2B2E2D');GRAF=HexColor('#1C1E1C');HUE=HexColor('#F3F1EC');GLA=HexColor('#82C3C4')
import sys,json
DATA=json.load(open(sys.argv[1])) if len(sys.argv)>1 else {}
out=DATA.get('salida','/home/user/elvo-creating/brands/elvo/documentos/garantia-elvo-nativo.pdf')
c=canvas.Canvas(out,pagesize=A4); c.setTitle('Certificado de garantía · elvo· Nativo'); c.setAuthor('Inversiones Gad S.A.C.')
c.setFillColor(ALAB); c.rect(0,0,W,H,fill=1,stroke=0)
M=48
# banda superior
c.setFillColor(PIZ); c.rect(0,H-118,W,118,fill=1,stroke=0)
c.setFillColor(HUE); c.setFont('Times-Roman',34); c.drawString(M,H-62,'elvo')
x=c.stringWidth('elvo','Times-Roman',34)+M
c.setFillColor(GLA); c.circle(x+5,H-62+3,3.2,fill=1,stroke=0)
c.setFillColor(HUE); c.setFont('Times-Roman',22); c.drawString(M,H-96,'Certificado de garantía')
c.setFont('Helvetica',8.5); c.setFillColor(GLA); c.drawRightString(W-M,H-62,'ELVO· NATIVO · PURIFICADOR DE AGUA PARA CAÑO')
c.setStrokeColor(GLA); c.setLineWidth(0.7); c.line(M,H-108,W-M,H-108)
def label(y,t):
    c.setFillColor(PIE); c.setFont('Helvetica-Bold',8); 
    c.drawString(M,y,t.upper())
    c.setStrokeColor(CAL); c.setLineWidth(0.6); c.line(M,y-5,W-M,y-5)
body=ParagraphStyle('b',fontName='Helvetica',fontSize=9.6,leading=13.6,textColor=GRAF)
def para(y,txt,w=W-2*M,style=body):
    p=Paragraph(txt,style); _,h=p.wrap(w,500); p.drawOn(c,M,y-h); return y-h
y=H-150
label(y,'Datos del pedido (a completar al entregar)'); y-=24
fields=DATA.get('campos',[('N.º de pedido',''),('Nombre del cliente',''),('Producto / combo',''),('Fecha de entrega',''),('Boleta o factura N.º',''),('Garantía válida hasta','')])
colw=(W-2*M)/2
rows=(len(fields)+1)//2
for i,(k,v) in enumerate(fields):
    cx=M+(i%2)*colw; cy=y-(i//2)*30
    c.setFillColor(PIE); c.setFont('Helvetica',7.8); c.drawString(cx,cy,k.upper())
    c.setStrokeColor(PIE); c.setLineWidth(0.5); c.line(cx,cy-14,cx+colw-18,cy-14)
    if v:
        c.setFillColor(GRAF); c.setFont('Helvetica',9.2); c.drawString(cx,cy-11,v)
y-=rows*30+14
sections=[
('Qué cubre','Garantía de <b>1 año</b>, desde la fecha de entrega, contra fallas de fábrica del equipo: carcasa, derivador, conexiones y piezas. Si la falla está cubierta, reparamos o reemplazamos la pieza o el equipo sin costo para ti.'),
('Condiciones','El equipo se usa con núcleos originales elvo· y se cambian cuando corresponde: cada núcleo rinde 20.000 litros, unos 18 meses. Te avisamos por WhatsApp cuando toca el cambio. El Nativo está pensado para agua de red potable.'),
('Qué no cubre','El núcleo (es un consumible que se renueva), golpes o caídas, mal uso, conexiones no compatibles y el uso con agua que no sea de red potable sin tratamiento.'),
('30 días de prueba','Pruébalo en tu casa. Si no te convence, coordinamos el recojo, sin costo para ti, y te devolvemos tu dinero por el mismo medio de pago en 3 a 5 días hábiles. El equipo se devuelve completo, con sus piezas y adaptadores.'),
]
for t,txt in sections:
    label(y,t); y-=14; y=para(y,txt)-18
label(y,'Cómo solicitar la garantía'); y-=14
y=para(y,'Antes de escribirnos, revisa tres cosas, que resuelven la mayoría de los casos: <b>1)</b> retira el film (plástico) del núcleo; <b>2)</b> deja correr el agua por el filtro 10 minutos seguidos; <b>3)</b> reajusta el adaptador de jebe y revisa los empaques.')-8
y=para(y,'Si la falla continúa, escríbenos por WhatsApp con tu <b>número de pedido</b> y una <b>foto o video de la falla</b>, tu dirección, teléfono y el horario en que puedes recibirnos. Te respondemos por el mismo chat.')-14
# caja contacto
bh=46
c.setFillColor(PIZ); c.rect(M,y-bh,W-2*M,bh,fill=1,stroke=0)
c.setFillColor(HUE); c.setFont('Helvetica-Bold',10.5); c.drawString(M+16,y-19,'WhatsApp +51 929 190 100')
c.setFont('Helvetica',9); c.setFillColor(CAL); c.drawString(M+16,y-34,'elvo.pe  ·  contacto.elvo@gmail.com')
c.setStrokeColor(GLA); c.setLineWidth(0.7); c.line(M,y-bh,W-M,y-bh)
# pie
c.setFillColor(PIE); c.setFont('Helvetica',7.4)
c.drawString(M,52,'INVERSIONES GAD S.A.C.  ·  RUC 20522531287  ·  Av. Alejandro Velasco Astete 179, Dpto. 102, San Borja, Lima  ·  Marca elvo·')
leg=ParagraphStyle('l',fontName='Helvetica',fontSize=7.4,leading=9.6,textColor=PIE)
p=Paragraph('Esta garantía comercial no limita los derechos que te corresponden como consumidor según la legislación peruana vigente.',leg); p.wrap(W-2*M,40); p.drawOn(c,M,30)
c.showPage(); c.save(); print(out)
