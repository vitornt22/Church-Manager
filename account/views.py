from http.client import HTTPResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse


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
    return render(request, 'Estatisticas/estatisticas.html', {'active': 1})


@login_required(login_url='account:login', redirect_field_name='next')
def profile(request):
    return render(request, "Adm/Perfil.html", {'active': 6})
