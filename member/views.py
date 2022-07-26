from django.shortcuts import render


# Create your views here.
def members (request):
    return render (request, 'Membros/Membros.html', {'active':2})
