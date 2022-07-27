from django.urls import path

from . import views

app_name = 'member'
urlpatterns = [
    path('', views.listar, name='listar'),
    path('Cadastro', views.register, name='register'),
    path('Emissões', views.emissions, name='emissions'),
    path('Perfil', views.member_profile, name="profile"),

]
