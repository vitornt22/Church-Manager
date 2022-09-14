import datetime

from churchManager.settings import STATICFILES_DIRS
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer

from .models import Member


def table(pdf, cont, cont2, lista1, lista2, size):
    styleSheet = getSampleStyleSheet()
    style = styleSheet['Normal']

    pdf.setFont('Helvetica', 10)
    pdf.setFillColor(colors.black)
    pdf.setStrokeColor(colors.black)
    P = Paragraph("olasssss", style)

    for i in range(size):
        pdf.rect(20, cont, 350, 20, stroke=1, fill=0)

        pdf.drawString(23, cont2, lista1[i])

        pdf.rect(370, cont, 200, 20, stroke=1, fill=0)

        pdf.drawString(378, cont2, lista2[i])

        cont -= 20
        cont2 -= 20
    return cont


def createPdf(pdf, m, c, type):
    if m.is_baptized_water:
        status = "membro"
    else:
        status = "congregado"

        # CREATEHEADER
    img = STATICFILES_DIRS[0] + '/dist/img/adPE.jpeg'

    pdf.drawImage(img, 210, 705, 130, 130)
    pdf.setFont("Helvetica-Bold", 15)
    pdf.drawString(170, 680, "Assembleia de Deus, Recife-PE")
    pdf.line(100, 660, 500, 660)
    pdf.drawCentredString(280, 635, "Carta de " + type)
    pdf.setFont("Helvetica", 11)
    pdf.drawCentredString(
        300, 500, "É com muita satisfação que a Igreja Assembleia de Deus Missão (Recife- Pernambuco),")

    pdf.drawCentredString(
        300, 480, "vem através deste informar-lhe da situação Ativa e Regular, dentro dos principios bíblicos")
    pdf.drawCentredString(
        300, 460, "e doutrinários da nossa Intituição o " + status + " " + m.fullName.upper()+",  podendo, ")

    pdf.drawCentredString(
        300, 440, " assim, atuar na obra de Cristo nesta estimada Igreja.")
    pdf.setFont("Helvetica-Bold", 11)

    pdf.drawCentredString(150, 380, "Desde já agradecemos")

    pdf.line(100, 300, 500, 300)
    pdf.setFont("Helvetica", 10)
    pdf.drawCentredString(300, 280, "Assinatura do Secretário")
    pdf.drawString(70, 120, "De: Igreja Assembleia de Deus Missão")
    pdf.drawString(70, 100, "Recife-Pernambuco")
    pdf.drawString(70, 80, "Rua Amarantes Rodrigues Fonseca, Nº 238")

    # SAVE PDF
    return pdf
