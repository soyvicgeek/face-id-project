from django import forms
from usuarios.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        # fields = ['categoria_clave', 'categoria_nombre','categoria_descripcion', 'categoria_descuento','categoria_estado']
        fields = '__all__'