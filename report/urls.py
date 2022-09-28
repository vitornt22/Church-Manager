from django.urls import path

from . import views

app_name = 'report'
urlpatterns = [
    path('', views.reports, name='reports'),
    path('donwload/<int:id>', views.downloadReport, name='download'),

]
