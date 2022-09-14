from django.urls import path

from . import views

app_name = 'entrie'
urlpatterns = [
    path('', views.entries, name='entries'),
    path('registrar', views.register, name='register'),
    path('editar/<int:id>', views.edit, name='edit'),
    path('deletar/<int:id>', views.delete, name="delete"),

]
