from django import forms
from usuarios.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        #fields = ['usuario_clave', 'usuario_nombre']
        fields = '__all__'