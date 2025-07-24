# informacion/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('arduino/', views.info_arduino, name='info_arduino'),
    path('sensores/', views.info_sensores, name='info_sensores'),
    path('accesorios/', views.info_accesorios, name='info_accesorios'),
]