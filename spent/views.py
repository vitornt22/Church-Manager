import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import SpentForm
from .models import Spent

# flake8: noqa:  E501


@login_required(login_url='account:login', redirect_field_name='next')
def spents(request):
    spents = Spent.objects.filter(church=request.user.church)
    data = request.GET.get('table_search')
    print("DATTTA: ", data)

    if request.GET.get('table_search'):
        try:
            data = data.split('/')
            print('LIST: ', data)
            fullData = data[2]+'-'+data[1]+'-'+data[0]

            if len(data) > 0:
                spents = Spent.objects.filter(Q(church=request.user.church), Q(
                    (Q(date=fullData) | Q(Q(date__month=data[1]), Q(date__year=data[2])))))
                if entries.count() == 0:
                    entries = None
                    data = None

        except:
            entries = None

    return render(request, 'Saidas/saidas.html', {'mask': '00/00/0000', 'target': 'data', 'tag': 'Entrada', 'active': 4, 'spents': spents})


@login_required(login_url='account:login', redirect_field_name='next')
def register(request):
    form = SpentForm()
    print('ENTROU')
    if request.POST:
        form = SpentForm(request.POST)

        if form.is_valid():
            print('E VALIDO')
            entrie = form.save(commit=False)
            entrie.church = request.user.church
            if entrie.date is None:
                entrie.date = datetime.date.today()
            entrie.save()
            form = SpentForm()
            messages.success(request, 'Entrada cadastrada com sucesso')

    else:
        form = SpentForm()

    return render(request, 'Saidas/register.html', {'active': 4, 'form': form})


@login_required(login_url='account:login', redirect_field_name='next')
def edit(request, id):
    spent = Spent.objects.get(id=id)
    mes = datetime.date.today()
    if (spent.date.month != mes):
        messages.error(
            request, 'Nao e possivel alterar saidas de outros meses')
        return redirect('spent:spents')

    mes = datetime.date.today().month
    form = SpentForm()
    if request.POST:
        form = SpentForm(request.POST,  instance=spent)
        if form.is_valid():
            a = form.save(commit=False)
            a.save()
            messages.success(request, 'Dados Alterados com sucesso')

        return redirect('entrie:entries')

    else:
        form = SpentForm(instance=spent)

    return render(request, 'Saidas/register.html', {'text': '', 'active': 4, 'form': form})


@login_required(login_url='account:login', redirect_field_name='next')
def delete(request, id):
    remove = Spent.objects.get(id=id)
    if (remove.date.month == datetime.date.today().month):
        remove.delete()
        messages.success(request, 'Entrada Deletado com sucesso!')
    else:
        messages.error(request, 'Só é possivel deletar entradas do mês')
    return redirect('spent:spents')
