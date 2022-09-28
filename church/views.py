from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

from .forms import ChurchForm

# Create your views here.


@login_required(login_url='account:login', redirect_field_name='next')
def profile(request):

    form = ChurchForm(instance=request.user.church)

    if request.POST:
        form = ChurchForm(request.POST, instance=request.user.church)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.save()
            messages.success(request, "Dados da empresa Alterados")

        else:
            print('NAO E VALIDOOOO')
    return render(request, 'Adm/Perfil.html', {'active': 6, 'form': form, 'Church': request.user.church})
