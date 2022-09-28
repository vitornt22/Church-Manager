import os
from cmath import rect

from churchManager.settings import STATIC_ROOT
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas


def titulo(pdf, msg, cont):

    if msg == "ENTRADAS":
        value = 250
    else:
        value = 260
    # tables
    pdf.setStrokeColor(colors.black)
    pdf.setFillColor('#6F9EF6')
    pdf.setFont("Helvetica-Bold", 15)
    pdf.rect(20, cont, 550, 20, stroke=1, fill=1)
    pdf.setFillColor('#ffffff')
    pdf.drawString(value, cont+5, msg)
    return pdf


def total(pdf, lista, cont):

    lis = ["Entradas: ", "Saidas: ", "Lucro: "]
    aux = 0
    for i in lista:
        pdf.setStrokeColor(colors.black)
        pdf.rect(20, cont, 550, 20, stroke=1, fill=0)
        pdf.setFillColor('#000')
        pdf.setFont("Helvetica", 10)
        pdf.drawString(30, cont+5, lis[aux]+" "+str(i))
        cont -= 20
        aux += 1


def line(pdf, obj, cont, categoria):

    pdf.setStrokeColor(colors.black)
    pdf.rect(20, cont, 550, 20, stroke=1, fill=0)
    pdf.setFillColor('#000')
    pdf.setFont("Helvetica", 8)

    if obj is not None:
        if categoria == "SAIDAS":
            pdf.drawString(30, cont+5, obj.ocassion)
        else:
            pdf.drawString(30, cont+5, obj.ocassion + str(obj.id))

        pdf.drawString(300, cont+5, "DATA: "+str(obj.date))
        pdf.drawString(470, cont+5, "VALOR(R$): "+str(obj.value))

    else:
        pdf.drawString(30, cont+5, " ")
    return pdf


def cabecalho(pdf, report):

    # img = STATIC_ROOT + '/dist/img/ChurchAnimation.png'
    pdf.setStrokeColor(colors.black)
    pdf.rect(20, 775, 550, 60, stroke=1)
    # pdf.drawImage(img, 20, 780, 110, 50)
    pdf.setFont("Helvetica-Bold", 18)

    if int(report.mounth) <= 9:
        data = "0"+str(report.mounth)+"/"+str(report.year)
    else:
        data = str(report.mounth)+"/"+str(report.year)

    pdf.drawString(150, 800, "RELATÓRIO MENSAL REFERENTE À " +
                   data)
    return pdf


def createPdf(pdf, gains, spents, report):

    pdf = cabecalho(pdf, report)
    pdf.setFont("Helvetica-Bold", 15)
    cont = 730

    aux = 0
    msg = ["ENTRADAS", "SAIDAS"]
    contador = 0
    lista = [gains, spents]

    for i in lista:

        pdf = titulo(pdf, msg[contador], cont)
        cont -= 20

        if i.count() > 0:
            for j in i:
                if aux == 33:
                    pdf.showPage()
                    cont = 730
                    aux = 0
                pdf = line(pdf, j, cont, msg[contador])
                cont -= 20
                aux += 1

        else:
            pdf = line(pdf, None, cont, msg[contador])
            cont -= 20

        contador += 1
        cont -= 20
    cont -= 40
    # ADD TOTAL E LUCROS
    entrada = 0
    saida = 0
    lucro = 0
    for i in gains:
        entrada += i.value
    for i in spents:
        saida += i.value

    lucro = entrada-saida
    pdf = titulo(pdf, "TOTAL", cont)
    cont -= 20
    pdf = total(pdf, [entrada, saida, lucro], cont)
