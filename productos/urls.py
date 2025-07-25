from django.urls import path
from . import views

urlpatterns = [
    path('activos/', views.activos, name='activos'),
    path('pasivos/', views.pasivos, name='pasivos'),
    path('sensores/', views.sensores, name='sensores'),
    path('mcu/', views.mcu, name='mcu'),
    path('accesorios/', views.accesorios, name='accesorios'),
<<<<<<< HEAD
=======

>>>>>>> 3d94c0261033b0def27954e1ddd3a47a93fc5769
    
]