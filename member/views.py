from django.shortcuts import render


# Create your views here.
def listar (request):
    return render (request, 'Membros/Listar.html', {'active':3})

def register (request):
    return render (request, 'Membros/Cadastro.html', {'active':2})

def emissions(request):
    return render (request, 'Membros/Emissao.html', {'active':5})

def member_profile(request):
    return render (request, 'Membros/Profile.html', {'active':3})

