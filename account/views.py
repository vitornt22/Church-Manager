from http.client import HTTPResponse

from django.shortcuts import render


# Create your views here.
def login_view(request):
    return render(request, 'Estatisticas/estatisticas.html', {'active':1})

def index(request):
    return render(request, 'Estatisticas/estatisticas.html', {'active':1})

def profile(request):
    return render(request, "Adm/Perfil.html", {'active':6})
