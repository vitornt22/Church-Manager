# flake8: noqa: E501
import datetime
from http.client import HTTPResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from entrie.models import Entrie
from member.models import Member
from spent.models import Spent


# Create your views here.
def login_view(request):

    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('pass')
        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            print("USUARIO", user)
            return redirect(reverse('account:index'))
        else:
            messages.error(
                request, "Senha ou email Invalidos, tente novamente !")
        return redirect('account:login')

    if request.POST:
        email = request.POST.ger('email')
        senha = request.POST.get('pass')

    return render(request, 'index.html')


@login_required(login_url='account:login', redirect_field_name='next')
def logout_view(request):
    logout(request)
    return redirect(reverse('account:login'))


@login_required(login_url='account:login', redirect_field_name='next')
def index(request):
    mes = datetime.date.today().month
    members = Member.objects.filter(
        church=request.user.church, is_baptized_water=True).count()
    congregados = Member.objects.filter(
        church=request.user.church, is_baptized_water=False).count()
    tithes = Member.objects.filter(
        church=request.user.church, is_tither=True).count()

    caixa = caixaEmpresa(request)
    lucroLista, aumento, entradas, saidas = listaFinancas(
        request.user.church)

    return render(request, 'Estatisticas/estatisticas.html', {'caixa': caixa, 'grafico': [entradas, saidas], 'aumento': aumento, 'lucroMes': lucroLista[int(mes)-1], 'lucroLista': lucroLista, 'members': members,
                                                              'tithes': tithes, 'congregados': congregados, 'active': 1, })


@login_required(login_url='account:login', redirect_field_name='next')
def profile(request):
    return render(request, "Adm/Perfil.html", {'active': 6})


def listaFinancas(church):
    print("EMPRESSSA", church)
    entradas = [0]*12
    saidas = [0]*12
    lucro = [0]*12
    anoAtual = datetime.date.today().year
    mes = datetime.date.today().month
    for i in range(12):
        for j in Entrie.objects.filter(church=church, date__year=anoAtual, date__month=i+1):
            entradas[i] += j.value
        for q in Spent.objects.filter(church=church, date__year=anoAtual, date__month=i+1):
            saidas[i] += q.value
        lucro[i] = entradas[i]-saidas[i]
    if lucro[mes-2] == 0:
        aumento = lucro[mes-1]*100
    else:
        aumento = ((lucro[mes-1]-lucro[mes-2]) * 100) / lucro[mes-2]

    return lucro, aumento, entradas[mes-1], saidas[mes-1]


def caixaEmpresa(request):
    entradas = Entrie.objects.filter(church=request.user.church)
    saidas = Spent.objects.filter(church=request.user.church)
    contEntries = 0
    contSpents = 0

    if (entradas):
        for i in entradas:
            contEntries += i.value

    if (saidas):
        for i in saidas:
            contSpents += i.value

    caixa = contEntries-contSpents

    return caixa
