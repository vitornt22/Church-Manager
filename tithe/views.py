from django.shortcuts import render


# Create your views here.
def tithes (request):
    return render(request, "Tithe/tithes.html", {'active':3})
