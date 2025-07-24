from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .forms import RegistroUsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm # Necesario para el formulario de login

def registro_usuario(request):
    if request.method == "POST":
        formulario = RegistroUsuarioForm(request.POST)
        if formulario.is_valid():
            user = formulario.save() # UserCreationForm.save() crea el usuario y hashea la contraseña
            messages.success(request, f'¡Tu cuenta "{user.username}" ha sido creada exitosamente! Ahora puedes iniciar sesión.')
            return redirect('login_usuario')
        else:
            # Los errores del formulario se añadirán a los mensajes de Django
            for field, errors in formulario.errors.items():
                for error in errors:
                    # 'non_field_errors' son errores que no pertenecen a un campo específico (ej. contraseñas no coinciden)
                    if field == '__all__':
                        messages.error(request, f"{error}")
                    else:
                        messages.error(request, f"Error en '{field}': {error}")
    else:
        formulario = RegistroUsuarioForm() # Formulario vacío para una solicitud GET

    return render(request, "usuarios/registro.html", {"form": formulario}) # <--- NOTA: Pasamos como 'form'

def login_usuario(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST) # Django AuthenticationForm
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'¡Bienvenido de nuevo, {user.username}!')
            # Redirigir a la página a la que intentaba acceder (si existe 'next') o a la principal
            return redirect(request.GET.get('next', reverse('principal')))
        else:
            # AuthenticationForm ya tiene errores de campo si las credenciales no son válidas
            messages.error(request, "Usuario o contraseña incorrectos.")
            # Es crucial pasar el formulario con los errores para que se muestren en el template
    else:
        form = AuthenticationForm() # Formulario vacío para una solicitud GET
    
    return render(request, "usuarios/login.html", {"form": form}) # <--- NOTA: Pasamos como 'form'

def logout_usuario(request):
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('principal') # Mejor redirigir a la principal, o donde quieras después del logout