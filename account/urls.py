from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
    path('', views.login_view, name='login'),
    path('', views.index, name='index'),
    path('Igreja', views.profile, name='profile'),

]
