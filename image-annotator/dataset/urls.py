from django.urls import path
from . import views

app_name = 'datasetcreator'
urlpatterns = [
    path('datasetcreator/', views.datasetcreator, name='datasetcreator'),
    path('viewconfig/', views.viewconfig, name='viewconfig'),
    path('halamanconfig/<id>', views.halamanconfig, name='halamanconfig'),
    path('halamanconfig/', views.halamanconfig, name='halamanconfig'),
    path('metodeconfig/', views.metodeconfig, name='metodeconfig'),
    path('hasilconfig/', views.hasilconfig, name='hasilconfig'),
     path('viewhasil/', views.viewhasil, name='viewhasil'),
]