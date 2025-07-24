# usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout # Funciones de autenticación de Django
from django.contrib import messages # Para mostrar mensajes al usuario
from django.urls import reverse
from .forms import RegistroUsuarioForm # Importamos nuestro formulario de registro
from django.contrib.auth.models import User # Importamos el modelo de usuario
from django.contrib.auth.forms import AuthenticationForm # Importamos este para el formulario de login de Django

def registro_usuario(request):
    """
    Vista para el registro de nuevos usuarios.
    Maneja la lógica de presentación del formulario y el procesamiento de los datos enviados.
    """
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
    """
    Vista para el inicio de sesión de usuarios.
    Utiliza el AuthenticationForm de Django para manejar la autenticación.
    """
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
    """
    Vista para cerrar la sesión del usuario.
    """
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('principal')