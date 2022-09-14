from django.urls import path

from . import views

app_name = 'member'
urlpatterns = [
    path('', views.MemberList, name='list'),
    path('Cadastro', views.registerMember, name='register'),
    path('Deletar/<int:id>', views.deleteMember, name='remove'),
    path('perfil/<int:id>', views.profile, name='profile'),
    path('emissioes', views.emissions, name='emissions'),
    path('emitir/<int:id>/<str:type>',
         views.emitirCarta, name='emitirCarta'),



]
