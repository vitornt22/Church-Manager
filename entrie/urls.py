from django.urls import path

from . import views

app_name = 'entrie'
urlpatterns = [
    path('', views.entries, name='entries'),
]
