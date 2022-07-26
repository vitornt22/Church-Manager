from django.shortcuts import render


def entries(request):
    return render(request,'Entradas-Saidas/Entradas-Saidas.html', {'active':3})
