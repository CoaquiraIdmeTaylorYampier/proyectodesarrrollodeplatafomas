from django import forms
from django.contrib.auth.models import User 
class RegistroUsuarioForm(forms.Form): 
    username = forms.CharField(  
        max_length=150,
        required=True, 
        label="Nombre de Usuario",
        error_messages={'required': 'Por favor, ingresa un nombre de usuario.'}
    )
    email = forms.EmailField(
        required=True, 
        label="Correo Electrónico",
        error_messages={  
            'required': 'El correo electrónico es obligatorio.',
            'invalid': 'Por favor, ingresa un formato de correo electrónico válido.'
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label="Contraseña",
        error_messages={'required': 'La contraseña es obligatoria.'}
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label="Confirmar Contraseña",
        error_messages={'required': 'Por favor, confirma tu contraseña.'}
    )

    def clean(self): 
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            self.add_error('password2', 'Las contraseñas no coinciden. Por favor, verifica.')

        if password and len(password) < 8:
            self.add_error('password', 'La contraseña debe tener al menos 8 caracteres.')

        return cleaned_data

    def clean_username(self): 
        username = self.cleaned_data['username'] #Recupera 
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está registrado. Por favor, elige otro.")
        
        return username 

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email