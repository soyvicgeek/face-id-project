from django.db import models

# Create your models here.

#Modelo Usuario
class Usuario(models.Model):
    usuario_clave = models.PositiveIntegerField(unique=True, blank=False, null=False)
    usuario_nombre = models.CharField(max_length=20, unique=True, blank=False, null=False)
    usuario_apellido = models.CharField(max_length=20, blank=False, null=False)
    usuario_correo = models.EmailField(unique=True, null=False)
    usuario_contrasena = models.CharField(max_length=255, null=False)
    usuario_foto_rostro = models.CharField(max_length=55, null=True, blank=True)
    usuario_modo_registro = models.CharField(max_length=25, null=True, blank=True, default='correo')
    usuario_fecha_registro = models.DateTimeField(auto_now_add=True)
    usuario_role = models.IntegerField(null=False, default=1)
    usuario_estado = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.usuario_nombre
