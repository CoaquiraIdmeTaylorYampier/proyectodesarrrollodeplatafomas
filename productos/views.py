from django.http import HttpResponse
from django.shortcuts import render

import datetime 

# Create your views here.
def activos(request):
    return render(request, 'activos.html')

def pasivos(request):
    return render(request, 'pasivos.html')

def sensores(request):
    return render(request, 'sensores.html')

def mcu(request):
    return render(request, 'mcu.html')

def accesorios(request):
    return render(request, 'accesorios.html')