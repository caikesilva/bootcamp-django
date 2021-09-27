from os import name
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('perdidos/', views.perdidos, name="perdidos"),
    path('achados/',views.achados, name="achados"),
    path('detalhes_achado/<int:pk>/', views.detalhes_achado, name="detalhes_achado"),
    path('detalhes_perdido/<int:pk>/', views.detalhes_perdido, name="detalhes_perdido"),
    path('relatorio_perdidos/',views.relatorio_perdidos, name='relatorio_perdidos'),
]