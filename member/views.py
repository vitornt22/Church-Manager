

from church.models import Church
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from member.forms import MemberForm
from member.models import Member


@login_required(login_url='account:login', redirect_field_name='next')
def MemberList(request):
    members = Member.objects.filter(church=request.user.church)
    data = None
    number = members.count()
    data = request.GET.get('search')
    if request.GET.get('search'):

        if len(data) > 0:
            members = Member.objects.filter(church=request.user.church, fullName__icontains=data)  # noqa
            if members.count() == 0:
                members = None
                data = None

    return render(request, 'Members/List.html', {'number': number, 'resultados': data, 'pequisa': 'por nome', 'url': 'member:search', 'active': 3, 'members': members})  # noqa


@login_required(login_url='account:login', redirect_field_name='next')
def deleteMember(request, id):
    remove = Member.objects.get(id=id)
    remove.delete()
    messages.success(request, 'Fiel Deletado com sucesso!')
    return redirect('member:list')


@login_required(login_url='account:login ', redirect_field_name='next')
def profile(request, id):
    instancia = Member.objects.get(id=id)
    if request.POST:
        form = MemberForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados Alterados com sucesso')
    else:
        form = MemberForm(instance=instancia)
    return render(request, 'Members/Profile.html', {'info': instancia, 'active': 3, 'form': form, 'id': id})  # noqa


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

    return render(request, 'Members/Register.html', {'id': id, 'active': 2, 'form': form})  # noqa
