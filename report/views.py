import datetime
import io

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import FileResponse
from django.shortcuts import render
from entrie.models import Entrie
from reportlab.pdfgen import canvas
from spent.models import Spent

from report.models import Report

from .gerarRelatorio import createPdf


def generatorReports(request):
    hoje = datetime.date.today()
    # create report inexistent

    if Report.objects.filter(church=request.user.church, mounth=str(hoje.month), year=str(hoje.year)).exists():  # noqa

        if hoje.month <= 9:
            m = "0"+str(hoje.month)
        else:
            m = hoje.month
        report = Report.objects.create(
            mounth=m, year=str(hoje.year), church=request.user.church)
        report.save()


# Create your views here.


@login_required(login_url='account:login ', redirect_field_name='next')
def reports(request):
    reports = Report.objects.filter(church=request.user.church)
    church = request.user.church
    data = request.GET.get('table_search')

    if request.GET.get('table_search'):
        try:
            print("DATTTA: ", data)
            data = data.split('/')
            print('LIST: ', data)
            month = int(data[1])

            year = data[0]
            print("MES ", month)
            print("ANOOO ", year)

            if len(data) > 0:
                reports = Report.objects.filter(mounth=month, year=year)
                print("REPORT: ", reports)
                if reports.count() == 0:
                    reports = None
                    data = None
        except:
            reports = None
    return render(request, 'Report/reports.html', {'active': 4, 'reports': reports, 'mask': '00/0000'})  # noqa


@ login_required(login_url='account:login ', redirect_field_name='next')
def downloadReport(request, id):
    report = Report.objects.get(id=id, church=request.user.church)
    print("REPOOOORT:", report)
    gains = Entrie.objects.filter(church=request.user.church, date__month=report.mounth, date__year=report.year)  # noqa
    spents = Spent.objects.filter(church=request.user.church, date__month=report.mounth, date__year=report.year)  # noqa
    print("GANHOS E GASTOS", gains, spents)
    print("REPOOOOSOSOSSSNSNNS: ", report)
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    createPdf(p, gains, spents, report)
    # p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='location-'+str(report.id)+'.pdf')  # noqa
