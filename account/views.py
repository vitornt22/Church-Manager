from http.client import HTTPResponse

from django.shortcuts import render


# Create your views here.
def login_view(request):

    return render(request, 'Base/BaseAdmin.html', {'active':1})
