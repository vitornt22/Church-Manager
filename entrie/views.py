from django.shortcuts import render


def entries(request):
    return render(request,'Entradas/entradas.html', {'active':4})
