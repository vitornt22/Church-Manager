from django.shortcuts import render


# Create your views here.
def spents(request):
    return render(request, "Saidas/saidas.html",{'active':4})
