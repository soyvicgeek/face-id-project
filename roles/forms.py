from django import forms
from roles.models import Rol

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = '__all__'