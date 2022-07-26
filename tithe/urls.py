from django.urls import path

from . import views

app_name = 'tithe'
urlpatterns = [
    path('', views.tithes, name='tithes'),
]
