# informacion/views.py
from django.shortcuts import render
from django.http import HttpResponse

def info_arduino(request):
    return render(request, 'info_arduino.html')

def info_sensores(request):
    return render(request, 'info_sensores.html')

def info_accesorios(request):
    return render(request, 'info_accesorios.html')