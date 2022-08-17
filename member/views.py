
import copy

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from member.forms import MemberForm
from member.models import Member


@login_required(login_url='account:login', redirect_field_name='next')
def MemberList(request):
    members = Member.objects.filter(church=request.user.church)
    return render(request, 'Members/List.html', {'active': 3, 'members': members})


@login_required(login_url='account:login', redirect_field_name='next')
def search(request):
    ...


@login_required(login_url='account:login', redirect_field_name='next')
def deleteMember(request, id):
    remove = Member.objects.get(id=id)
    remove.delete()
    messages.success(request, 'Fiel Deletado com sucesso!')
    return redirect('member:list')


@login_required(login_url='account:login', redirect_field_name='next')
def profile(request, id):
    instancia = Member.objects.get(id=id)
    if request.POST:
        form = MemberForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados Alterados com sucesso')
    else:
        form = MemberForm(instance=instancia)
    return render(request, 'Members/Profile.html', {'active': 3, 'form': form, 'id': id})


@login_required(login_url='account:login', redirect_field_name='next')
def editMember(request):
    ...


@login_required(login_url='account:login', redirect_field_name='next')
def registerMember(request):
    id = None
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.church = request.user.church
            member.save()
            id = member.id
            messages.success(request, 'Fiel Cadastrado com sucesso!')
    else:
        form = MemberForm()

    return render(request, 'Members/Register.html', {'id': id, 'active': 2, 'form': form})
