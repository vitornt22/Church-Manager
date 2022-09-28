# flake8: noqa:  E501
import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render
from report.views import generatorReports

from .forms import EntrieForm
from .models import Entrie


@login_required(login_url='account:login', redirect_field_name='next')
def entries(request):
    entries = Entrie.objects.filter(
        church=request.user.church)
    data = request.GET.get('table_search')

    if request.GET.get('table_search'):
        try:
            print("DATTTA: ", data)
            data = data.split('/')
            print('LIST: ', data)
            fullData = data[2]+'-'+data[1]+'-'+data[0]

            if len(data) > 0:
                entries = Entrie.objects.filter(Q(church=request.user.church), Q(
                    (Q(date=fullData) | Q(Q(date__month=data[1]), Q(date__year=data[2])))))
                if entries.count() == 0:
                    entries = None
                    data = None
        except:
            entries = None

    return render(request, 'Entradas/entradas.html', {'target': 'data', 'mask': '00/00/0000', 'tag': 'Entrada', 'active': 4, 'entries': entries})


@ login_required(login_url='account:login', redirect_field_name='next')
def register(request):
    form = EntrieForm()

    if request.POST:
        form = EntrieForm(request.POST)

        if form.is_valid():
            print('E VALIDO')
            entrie = form.save(commit=False)
            entrie.church = request.user.church
            if entrie.date is None:
                entrie.date = datetime.date.today()
            entrie.save()
            generatorReports(request)
            form = EntrieForm()
            messages.success(request, 'Entrada cadastrada com sucesso')

    else:
        form = EntrieForm()

    return render(request, 'Entradas/register.html', {'active': 4, 'form': form})


@ login_required(login_url='account:login', redirect_field_name='next')
def edit(request, id):
    entrie = Entrie.objects.get(id=id)
    mes = datetime.date.today().month

    if (entrie.date.month != mes):
        messages.error(
            request, 'Nao e possivel alterar entrada de outros meses')
        return redirect('entrie:entries')

    form = EntrieForm()
    if request.POST:
        form = EntrieForm(request.POST,  instance=entrie)
        if form.is_valid():
            a = form.save(commit=False)
            a.save()
            messages.success(request, 'Dados Alterados com sucesso')

            return redirect('entrie:entries')
    else:
        form = EntrieForm(instance=entrie)

    return render(request, 'Entradas/register.html', {'active': 4, 'form': form})


@ login_required(login_url='account:login', redirect_field_name='next')
def delete(request, id):

    remove = Entrie.objects.get(id=id)
    if (remove.date.month == datetime.date.today().month):
        remove.delete()
        messages.success(request, 'Entrada Deletado com sucesso!')
    else:
        messages.error(request, 'Só é possivel deletar entradas do mês')
    return redirect('entrie:entries')
