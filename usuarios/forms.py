from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Formulario para el registro
class RegistroUsuarioForm(UserCreationForm):
    # Por defecto, UserCreationForm ya incluye username, password, password2.
    # Si quieres añadir email, hazlo así:
    email = forms.EmailField(required=True, label="Correo Electrónico")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',) # Añade 'email' a los campos existentes

    # Puedes añadir validaciones personalizadas aquí si lo necesitas,
    # por ejemplo, para asegurar que el email sea único.