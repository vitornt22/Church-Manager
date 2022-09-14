

import io

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.shortcuts import redirect, render
from reportlab.pdfgen import canvas

from member.carta import createPdf
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
        form = MemberForm(request.POST, request.FILES,  instance=instancia)
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
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save(commit=False)
            member.church = request.user.church
            member.save()
            id = member.id
            messages.success(request, 'Fiel Cadastrado com sucesso!')
    else:
        form = MemberForm()

    return render(request, 'Members/Register.html', {'id': id, 'active': 2, 'form': form})  # noqa


@login_required(login_url='account:login', redirect_field_name='next')
def emissions(request):
    members = Member.objects.filter(church=request.user.church)
    data = request.GET.get('table_search')
    if request.GET.get('table_search'):

        if len(data) > 0:
            members = Member.objects.filter(church=request.user.church, fullName__icontains=data)  # noqa
            if members.count() == 0:
                members = None
                data = None

    return render(request, 'Members/Emission.html', {'members': members})


@login_required(login_url='company:login', redirect_field_name='next')
def emitirCarta(request, id, type):

    church = request.user.church
    member = Member.objects.get(id=id)
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    createPdf(p, member, church, type)
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='Carta-'+str(member.id)+'-'+str(member.fullName)+'.pdf')  # noqa
