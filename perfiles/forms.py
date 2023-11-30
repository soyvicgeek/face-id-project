from django import forms
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'is_active',
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo electrónico',
            'password': 'Contraseña',
            'is_active': 'Esta activo'
        }