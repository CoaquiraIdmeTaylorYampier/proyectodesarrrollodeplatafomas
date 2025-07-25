from django.http import HttpResponse
from django.shortcuts import render
import datetime
from . import forms, models

# Create your views here.
def Index(request):
    return HttpResponse("Hola mundo desde clientes")

def saludar(request):
    return HttpResponse("<h1>Hola Miguel</h1>")

def saludarconnombre(request, nombre):
    return HttpResponse(f"<h1>Hola {nombre.capitalize()}</h1>")

def llamarplantilla(request):
    return render(request, "cliente/uno.html")

def saludarConPlantilla(request, nombre):
    fecha = datetime.datetime.now()
    return render(request, "cliente/dos.html", {
        "name":nombre.capitalize(),
        "fecha": fecha
    })

def crear_persona(request):
    
    if(request.method == "POST"):
        formulario = forms.Formulario_Persona(request.POST)
        if(formulario.is_valid()):
            nombres = formulario.cleaned_data['nombre']
            apellidos = formulario.cleaned_data['apellidos']
            persona = models.Persona.objects.create(nombre = nombres, apellidos = apellidos)
            persona.save()
            return HttpResponse("Hola " + nombres + " " + apellidos + ", fuiste registrado correctamente.")
            #return HttpResponse(models.Persona.objects.all())
    formulario = forms.Formulario_Persona()
    return render(request, "cliente/persona.html", {
        "formulario": formulario
    })

def listar_personas(request):
    return render(request, "cliente/lista_personas.html",{"personas":models.Persona.objects.all()})
    