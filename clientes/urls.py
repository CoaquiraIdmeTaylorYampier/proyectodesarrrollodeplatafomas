from django.contrib import admin
from django.urls import include, path

from . import views
urlpatterns = [
    path('',views.Index, name = "index"),
    path('/saludar',views.saludar, name = "saludar"),
    path('/saludarconnombre/<str:nombre>',views.saludarconnombre, name = "saludarconnombre"),
    path('/html',views.llamarplantilla,name = "html"),
    path('/saludarhtml/<str:nombre>',views.saludarConPlantilla,name = "HolaHtml"),
    path('/crearpersona', views.crear_persona, name = "crear_persona"),
    path('/listarpersona', views.listar_personas, name = "listar_personas")
]