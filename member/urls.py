from django.urls import path

from . import views

app_name = 'member'
urlpatterns = [
    path('', views.MemberList, name='list'),
    path('pesquisa', views.search, name='pesquisa'),
    path('Cadastro', views.registerMember, name='register'),
    path('Deletar/<int:id>', views.deleteMember, name='remove'),
    path('perfil/<int:id>', views.profile, name='profile'),

]
