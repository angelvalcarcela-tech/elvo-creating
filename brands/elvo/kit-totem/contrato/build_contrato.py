import sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_COLOR_INDEX
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

MARCADO = sys.argv[1] == 'marcado'
OUT = sys.argv[2]

d = Document()
sec = d.sections[0]
sec.left_margin = sec.right_margin = Cm(2.3)
sec.top_margin = Cm(2.2); sec.bottom_margin = Cm(2.2)
st = d.styles['Normal']; st.font.name = 'Calibri'; st.font.size = Pt(11)
st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')
st.paragraph_format.space_after = Pt(6)

def run(p, text, bold=False, kind=None, italic=False):
    """kind: None normal, 'add' resaltado (solo marcado), 'del' tachado (solo marcado)"""
    if kind == 'del' and not MARCADO:
        return
    r = p.add_run(text); r.bold = bold; r.italic = italic
    if MARCADO and kind == 'add':
        r.font.highlight_color = WD_COLOR_INDEX.YELLOW
    if MARCADO and kind == 'del':
        r.font.strike = True; r.font.color.rgb = RGBColor(0xC0, 0x00, 0x00)
    return r

def para(parts, align=None, indent=None, space=None):
    p = d.add_paragraph()
    if align == 'c': p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if align == 'j': p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if indent: p.paragraph_format.left_indent = Cm(indent)
    if space is not None: p.paragraph_format.space_after = Pt(space)
    if isinstance(parts, str): parts = [(parts, {})]
    for t, kw in parts: run(p, t, **kw)
    return p

def bullet(parts):
    p = d.add_paragraph(style='List Bullet')
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if isinstance(parts, str): parts = [(parts, {})]
    for t, kw in parts: run(p, t, **kw)
    return p

def head(t): para([(t, {'bold': True})], space=3)

def table(rows, widths=None):
    t = d.add_table(rows=len(rows), cols=len(rows[0])); t.style = 'Table Grid'
    for i, r in enumerate(rows):
        for j, c in enumerate(r):
            cell = t.cell(i, j); cell.text = ''
            pr = cell.paragraphs[0]; rr = pr.add_run(c); rr.bold = (i == 0 or j == 1 and False)
            rr.font.size = Pt(10.5)
    d.add_paragraph()

ADD = {'kind': 'add'}
DEL = {'kind': 'del'}

if MARCADO:
    p = para([('VERSIÓN CON CAMBIOS PROPUESTOS POR ELVO · ', {'bold': True}),
              ('Texto resaltado en amarillo = agregado. ', {'kind': 'add'}),
              ('Texto tachado en rojo = eliminado.', {'kind': 'del'})], align='c')
    p = para('Las demás cláusulas permanecen sin cambios respecto del contrato enviado por TOTEM.', align='c')
    for r in p.runs: r.italic = True; r.font.size = Pt(9.5)

para([('CONTRATO DE PRESTACIÓN DE SERVICIOS DE MARKETING Y PRODUCCIÓN AUDIOVISUAL', {'bold': True})], align='c')
para('Conste por el presente documento el Contrato de Prestación de Servicios que celebran:')
para([('EL PRESTADOR: ', {'bold': True}), ('TOTEM INGENIERÍA DE MARCA S.A.C., identificada con RUC N.º 20609897334, con domicilio fiscal en Av. del Pinar 110, Oficina 605, Santiago de Surco, Lima, debidamente representada por Sophia Andrea Romero Peñaloza, identificada con DNI N.º 74986167, en calidad de Gerente General, en adelante, TOTEM.', {})], align='j')
para([('EL CLIENTE: ', {'bold': True}), ('INVERSIONES GAD S.A.C., identificada con RUC N.º 20522531287, con domicilio fiscal en Av. Alejandro Velasco Astete 179, Dpto. 102, Urb. Mariscal Ramón Castilla, San Borja, Lima, debidamente representada por Ángel Gerardo Valcarcel Saldaña, en calidad de Gerente General, titular de la marca comercial ELVO, en adelante, EL CLIENTE.', {})], align='j')
para('Ambas partes acuerdan celebrar el presente contrato bajo las siguientes condiciones:')

head('PRIMERA. OBJETO DEL CONTRATO')
para('TOTEM se compromete a prestar servicios de estrategia de contenido y producción audiovisual para la marca ELVO, conforme al alcance del Plan Esencial contratado.', align='j')
para('El servicio tiene como finalidad fortalecer la comunicación de la marca, desarrollar contenidos alineados con sus objetivos comerciales y optimizar progresivamente su estrategia de comunicación digital.', align='j')
para([('Los contenidos tendrán como uso principal la publicidad pagada en Meta y otras plataformas, y su uso en la atención comercial de EL CLIENTE, incluida su implementación en chatbots y en conversaciones con clientes por WhatsApp.', ADD)], align='j')

head('SEGUNDA. ALCANCE DEL SERVICIO')
para('El servicio comprende los siguientes entregables por ciclo mensual:')
for t in ['Discovery y desarrollo de estrategia inicial durante el primer ciclo.',
          'Optimización estratégica mensual.',
          'Grilla de ocho contenidos, incluyendo objetivos, conceptos, canales y fechas tentativas de activación.',
          'Desarrollo de conceptos creativos y guiones.',
          'Una sesión mensual de grabación audiovisual.',
          'Producción y edición de ocho videos.']:
    bullet(t)
bullet([('Entrega, junto con cada video final y mediante Google Drive, del material bruto de la sesión de grabación correspondiente, sin textos, y de los archivos editables del proyecto.', ADD)])
for t in ['Portadas y copies para publicación, según corresponda.',
          'Reporte mensual de desempeño, aprendizajes y recomendaciones.',
          'Dos reuniones mensuales: Performance Review y Content Planning.']:
    bullet(t)
para('Durante el primer ciclo, ambas reuniones podrán integrarse en una sola sesión, conforme al cronograma inicial acordado.', align='j')

head('TERCERA. CONSIDERACIONES DEL PRIMER CICLO')
para('Como cortesía comercial y por única vez, TOTEM realizará una sesión adicional de grabación destinada a la campaña Black Days de ELVO.', align='j')
para('El video producido para dicha campaña forma parte de los ocho videos correspondientes al primer ciclo mensual y no constituye un entregable adicional.', align='j')
para('Las actividades y fechas de implementación se desarrollarán conforme al documento de Bienvenida y Roadmap compartido con EL CLIENTE, sujeto a las coordinaciones y aprobaciones correspondientes.', align='j')

head('CUARTA. SERVICIOS NO INCLUIDOS')
para('El servicio contratado no comprende:')
for t in ['Publicación o programación de contenidos.',
          'Community management y atención de mensajes.',
          'Gestión, configuración u optimización de campañas publicitarias.',
          'Inversión en pauta digital.',
          'Implementación de contenidos en chatbots u otras plataformas.',
          'Sesiones adicionales de grabación, salvo la cortesía inicial acordada.',
          'Contratación de modelos, actores, locaciones, utilería especial o proveedores externos.']:
    bullet(t)
bullet([('Entrega de material audiovisual bruto o archivos editables.', DEL)])
para('Cualquier servicio adicional deberá ser cotizado y aprobado previamente por EL CLIENTE.', align='j')

head('QUINTA. VIGENCIA DEL CONTRATO')
para('El servicio tiene como fecha de inicio el 23 de noviembre de 2026, independientemente de la fecha de suscripción del presente contrato.', align='j')
para('Se establece un periodo mínimo de contratación de tres ciclos mensuales consecutivos:')
table([['Ciclo', 'Periodo'], ['Primero', '23/11/2026 – 22/12/2026'], ['Segundo', '23/12/2026 – 22/01/2027'], ['Tercero', '23/01/2027 – 22/02/2027']])
para('Finalizado el periodo mínimo, el servicio se renovará automáticamente por ciclos mensuales, salvo comunicación escrita de cualquiera de las partes con una anticipación mínima de quince días calendario al inicio del siguiente ciclo.', align='j')

head('SEXTA. CONTRAPRESTACIÓN Y CONDICIONES DE PAGO')
para('EL CLIENTE abonará a TOTEM una contraprestación mensual de:')
table([['Concepto', 'Importe'], ['Valor del servicio', 'S/ 1,800.00'], ['IGV (18 %)', 'S/ 324.00'], ['Total mensual', 'S/ 2,124.00']])
para('El pago se realizará al 100 % por adelantado, el día 23 de cada mes, mediante transferencia bancaria a la cuenta comunicada por TOTEM.', align='j')
para('El primer pago, originalmente previsto para el 23 de noviembre de 2026, deberá realizarse a más tardar el 26 de noviembre de 2026.', align='j')
para('TOTEM emitirá el comprobante de pago electrónico conforme a la normativa tributaria vigente y lo remitirá a:')
bullet('gervalcarcel@hotmail.com'); bullet('administracion@jcocontadores.com')
para('En caso de que el pago no se realice dentro de los cinco (5) días calendario siguientes a la fecha de vencimiento, TOTEM podrá suspender temporalmente la ejecución de actividades y la entrega de contenidos, previa comunicación escrita a EL CLIENTE.', align='j')
para('La suspensión por falta de pago no implicará la ampliación automática del ciclo contratado.', align='j')

head('SÉPTIMA. OBLIGACIONES DE TOTEM')
para('TOTEM se compromete a:')
for t in ['a) Desarrollar los servicios contratados con diligencia, profesionalismo y criterios estratégicos y creativos.',
          'b) Cumplir con los entregables y cronogramas acordados, siempre que EL CLIENTE proporcione oportunamente los recursos y aprobaciones necesarios.',
          'c) Mantener comunicación sobre el avance del servicio.',
          'd) Incorporar los ajustes correspondientes al alcance contratado.',
          'e) Analizar la información de desempeño disponible y formular recomendaciones de mejora.',
          'f) Mantener la confidencialidad de la información proporcionada por EL CLIENTE.']:
    para(t, align='j', indent=0.6, space=3)

head('OCTAVA. OBLIGACIONES DE EL CLIENTE')
para('EL CLIENTE se compromete a:')
for t in ['a) Realizar los pagos dentro de los plazos establecidos.',
          'b) Proporcionar información comercial, técnica y gráfica necesaria para la ejecución del servicio.',
          'c) Garantizar la veracidad de las características, beneficios, certificaciones, promociones y demás afirmaciones comerciales de sus productos.',
          'd) Facilitar los productos, espacios y personas previamente coordinados para las sesiones de grabación.',
          'e) Garantizar que las personas que participen en las grabaciones por parte de EL CLIENTE, sean colaboradores, clientes u otros terceros, hayan autorizado el uso de su imagen y voz para los fines del presente contrato.',
          'f) Revisar y aprobar oportunamente las propuestas, guiones y contenidos.',
          'g) Gestionar la publicación, activación publicitaria e implementación de los contenidos entregados.',
          'h) Compartir las métricas de desempeño y la información comercial necesaria para elaborar los reportes.',
          'i) Designar un responsable autorizado para centralizar las comunicaciones y aprobaciones.']:
    para(t, align='j', indent=0.6, space=3)

head('NOVENA. APROBACIONES, AJUSTES Y CRONOGRAMA')
para([('EL CLIENTE deberá proporcionar sus observaciones y aprobaciones dentro de los dos días hábiles siguientes a la recepción de cada entregable, salvo que las partes acuerden un plazo diferente. ', {}),
      ('Si EL CLIENTE no formula observaciones dentro de dicho plazo, el entregable se considerará aprobado.', DEL),
      ('Vencido ese plazo, TOTEM enviará un recordatorio escrito por correo o WhatsApp. Si EL CLIENTE no responde dentro de un día hábil adicional contado desde el recordatorio, el entregable se considerará aprobado.', ADD)], align='j')
para('El servicio incluye hasta dos rondas de ajustes consolidados por entregable, siempre que estos se mantengan dentro del concepto y alcance originalmente acordados.', align='j')
para('Los errores atribuibles a TOTEM serán corregidos sin costo adicional.', align='j')
para('Los cambios de concepto posteriores a una aprobación, nuevas solicitudes creativas o regrabaciones derivadas de modificaciones solicitadas por EL CLIENTE podrán generar una cotización adicional.', align='j')
para('Los retrasos atribuibles a EL CLIENTE podrán dar lugar a la reprogramación de las entregas, sin modificar las fechas de pago previamente establecidas.', align='j')

head('DÉCIMA. ENTREGA Y ACTIVACIÓN DE CONTENIDOS')
para('TOTEM entregará los contenidos finales mediante Google Drive u otro medio digital acordado.', align='j')
para('La publicación, distribución, inversión publicitaria y activación comercial de los contenidos serán responsabilidad de EL CLIENTE.', align='j')
para('Las fechas de publicación o activación no condicionan el cierre del ciclo de producción ni las obligaciones de pago.', align='j')
para('En caso de que la información de desempeño no sea proporcionada oportunamente, el reporte se elaborará con los datos disponibles, indicando las limitaciones correspondientes.', align='j')

head('DÉCIMA BIS. RECHAZO DE CONTENIDOS EN PLATAFORMAS PUBLICITARIAS' + ('  [cláusula nueva]' if MARCADO else ''))
bis = ('Si una plataforma publicitaria rechaza, limita o da de baja un contenido por causas atribuibles a TOTEM (formato, calidad técnica, textos incrustados, música o elementos de terceros, o producción), TOTEM lo corregirá o reemplazará sin costo dentro de los tres días hábiles siguientes a la comunicación de EL CLIENTE. No se incluyen los rechazos derivados del producto, de sus afirmaciones comerciales o del guion aprobado. En esos casos, TOTEM colaborará de buena fe en la adecuación del contenido a las políticas de la plataforma. La corrección no cuenta como ronda de ajustes ni como regrabación.')
para([(bis, ADD)], align='j')

head('DÉCIMA PRIMERA. RESULTADOS DEL SERVICIO')
para('TOTEM se compromete a desarrollar y optimizar la estrategia de contenido conforme a los objetivos establecidos.', align='j')
para('Sin embargo, el servicio no implica una garantía de resultados específicos en ventas, facturación, alcance, seguidores, leads o conversiones, debido a que estos dependen también de factores comerciales, publicitarios, operativos y externos.', align='j')

head('DÉCIMA SEGUNDA. PROPIEDAD INTELECTUAL')
para('Una vez efectuado el pago íntegro del ciclo correspondiente, EL CLIENTE contará con una licencia de uso comercial de los contenidos finales producidos específicamente para su marca, que permitirá su reproducción, publicación y difusión en canales digitales, incluyendo publicidad pagada, por tiempo indefinido y dentro de los límites de las licencias de terceros aplicables.', align='j')
para([('TOTEM garantiza que la música, tipografías, imágenes, clips y demás elementos de terceros incluidos en los contenidos cuentan con licencia para uso comercial, incluida la publicidad pagada, por tiempo indefinido. En caso contrario, los reemplazará sin costo.', ADD)], align='j')
para('TOTEM conservará la titularidad de sus metodologías, procesos internos, herramientas, plantillas, archivos de trabajo y materiales preexistentes.', align='j')
para([('El material bruto y los archivos editables no forman parte de los entregables contratados, salvo acuerdo escrito adicional.', DEL)], align='j')
para('EL CLIENTE autoriza a TOTEM a utilizar los contenidos publicados por EL CLIENTE como parte de su portafolio profesional, salvo que EL CLIENTE indique lo contrario por escrito.', align='j')

head('DÉCIMA TERCERA. CONFIDENCIALIDAD')
para('Ambas partes se comprometen a mantener la confidencialidad de la información comercial, estratégica, financiera, técnica y operativa a la que tengan acceso durante la prestación del servicio.', align='j')
para('Dicha información no podrá ser divulgada a terceros sin autorización, salvo obligación legal.', align='j')
para('Esta obligación se mantendrá vigente incluso después de la finalización del contrato.', align='j')

head('DÉCIMA CUARTA. TERMINACIÓN ANTICIPADA')
para('Durante el periodo mínimo de tres ciclos mensuales, ninguna de las partes podrá dar por terminado unilateralmente el servicio sin causa justificada, salvo acuerdo escrito entre ambas.', align='j')
para('En caso de que EL CLIENTE solicite una terminación anticipada sin incumplimiento atribuible a TOTEM, las partes deberán liquidar los servicios ejecutados, los compromisos asumidos y los costos razonables derivados de la cancelación del periodo contratado.', align='j')
para('En caso de incumplimiento sustancial de alguna de las obligaciones contractuales, la parte afectada podrá solicitar su subsanación mediante comunicación escrita, otorgando un plazo de diez días calendario. De persistir el incumplimiento, podrá resolver el contrato conforme a la legislación aplicable.', align='j')

head('DÉCIMA QUINTA. NATURALEZA DEL SERVICIO')
para('El presente contrato es de naturaleza civil y comercial y no genera vínculo laboral, subordinación, exclusividad ni relación de dependencia entre las partes o sus respectivos colaboradores.', align='j')
para('TOTEM mantendrá autonomía técnica, creativa y operativa en la ejecución del servicio.', align='j')

head('DÉCIMA SEXTA. COMUNICACIONES')
para('Las comunicaciones operativas se realizarán mediante el grupo de WhatsApp ELVO × TOTEM y los correos electrónicos designados por ambas partes.', align='j')
para('Las modificaciones del alcance, condiciones económicas, vigencia o terminación del contrato deberán constar expresamente por escrito y contar con la conformidad de ambas partes.', align='j')

head('DÉCIMA SÉPTIMA. SOLUCIÓN DE CONTROVERSIAS')
para('Las partes procurarán resolver de manera directa y de buena fe cualquier controversia derivada del presente contrato.', align='j')
para('De no alcanzarse un acuerdo, se someterán a la legislación peruana y a la competencia de los jueces y tribunales de Lima, conforme corresponda.', align='j')

head('DÉCIMA OCTAVA. SUSCRIPCIÓN')
para('Las partes reconocen la validez de la firma digital, electrónica o escaneada del presente contrato, la cual tendrá el mismo efecto que la firma manuscrita.', align='j')
para('En señal de conformidad, ambas partes suscriben el presente documento en Lima, a los ___ días del mes de noviembre de 2026.', align='j')
d.add_paragraph()
t = d.add_table(rows=1, cols=2)
l = t.cell(0, 0); r = t.cell(0, 1)
l.text = ('POR TOTEM\n\n\n______________________\nFirma\nRepresentante: Sophia Andrea Romero Peñaloza\nDNI: 74986167\nCargo: Gerente General\nRazón social: TOTEM Ingeniería de Marca S.A.C.\nRUC: 20609897334')
r.text = ('POR INVERSIONES GAD S.A.C. – ELVO\n\n\n______________________\nFirma\nRepresentante: Ángel Gerardo Valcarcel Saldaña\nCargo: Gerente General\nRazón social: Inversiones GAD S.A.C.\nRUC: 20522531287')
for c in (l, r):
    for pp in c.paragraphs:
        for rr in pp.runs: rr.font.size = Pt(10.5)

# pie de página
fp = sec.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
fr = fp.add_run('Contrato ELVO × TOTEM'); fr.font.size = Pt(9); fr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

d.save(OUT)
print('ok', OUT)
