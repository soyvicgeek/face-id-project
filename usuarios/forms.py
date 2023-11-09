from django import forms
from usuarios.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'usuario_clave',
            'usuario_nombre',
            'usuario_apellido',
            'usuario_correo',
            'usuario_contrasena',
            'usuario_role',
        ]
        #fields = '__all__'