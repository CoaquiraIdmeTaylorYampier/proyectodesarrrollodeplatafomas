from django.urls import path
from . import views

urlpatterns = [
    path('activos/', views.activos, name='activos'),
    path('pasivos/', views.pasivos, name='pasivos'),
    path('sensores/', views.sensores, name='sensores'),
    path('mcu/', views.mcu, name='mcu'),
    path('accesorios/', views.accesorios, name='accesorios'),

    
]