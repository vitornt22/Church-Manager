from http.client import HTTPResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


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
        email= request.POST.ger('email')
        senha= request.POST.get('pass')
    return render(request, 'index.html')

@login_required(login_url='company:login', redirect_field_name='next')
def logout_view(request):

    if not request.POST:
        return redirect(reverse('account:login'))

    logout(request)
    return redirect(reverse('company:login'))

@login_required(login_url='company:login', redirect_field_name='next')
def index(request):
    return render(request, 'Estatisticas/estatisticas.html', {'active':1})


@login_required(login_url='company:login', redirect_field_name='next')
def profile(request):
    return render(request, "Adm/Perfil.html", {'active':6})
