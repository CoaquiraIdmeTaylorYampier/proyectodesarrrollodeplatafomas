from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.urls import reverse
from .forms import RegistroUsuarioForm 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import AuthenticationForm 

def registro_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, email=email, password=password)
            
            user.save()

            messages.success(request, f'¡Tu cuenta "{username}" ha sido creada exitosamente! Ahora puedes iniciar sesión.')

            return redirect('login_usuario')
        else:

            for field, errors in form.errors.items():
                for error in errors:
                    if field == '__all__': 
                        messages.error(request, f"Error: {error}")
                    else:
                        messages.error(request, f"Error en '{form[field].label}': {error}")
    else:
        form = RegistroUsuarioForm()

    return render(request, "usuarios/registro.html", {"form": form})

def login_usuario(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            
            user = form.get_user()
           
            login(request, user)
            
            messages.success(request, f'¡Bienvenido de nuevo, {user.username}!') 
            return redirect(request.GET.get('next', reverse('principal')))
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")
    else:
        form = AuthenticationForm()
    
    return render(request, "usuarios/login.html", {"form": form})

def logout_usuario(request):

    logout(request)
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('principal')

def lista_usuarios(request):
    
    usuarios = User.objects.all().order_by('username') 

    return render(request, "usuarios/lista_usuarios.html", {'usuarios': usuarios})
