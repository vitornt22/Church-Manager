
from django.urls import path

from . import views

app_name = 'spent'
urlpatterns = [
    path('', views.spents, name='spents'),
    path('registrar', views.register, name='register'),
    path('editar/<int:id>', views.edit, name='edit'),
    path('deletar/<int:id>', views.delete, name="delete"),

]
