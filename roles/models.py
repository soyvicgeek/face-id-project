from django.db import models

# Create your models here.

#Modelo Usuario
class Rol(models.Model):
    rol_clave = models.PositiveIntegerField(unique=True, blank=False, null=False)
    rol_nombre = models.CharField(max_length=20, unique=True, blank=False, null=False)
    rol_fecha_registro = models.DateTimeField(auto_now_add=True)
    rol_activa = models.IntegerField(null=False, default=1)
    rol_estado = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.rol_nombre
