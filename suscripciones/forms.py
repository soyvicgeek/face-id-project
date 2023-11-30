from django import forms
from suscripciones.models import Suscripcion

class SuscripcionForm(forms.ModelForm):
    class Meta:
        model = Suscripcion
        exclude = ['imagen']
        fields = [
            'nombre',
            'descripcion',
            'costo',
            'capacidad',
            'estado',
        ]
        labels = {
            'nombre': 'Nombre de la Suscripción',
            'descripcion': 'Descripción',
            'costo': 'Costo',
            'capacidad': 'Capacidad de Usuarios',
            'estado': 'Estado',
        }