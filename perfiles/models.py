from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default='default.jpg', upload_to='photos', blank=True)
    biografia = models.TextField(default='Mi Biografía', blank=True, null=True)
    suscripcion = models.BooleanField(default=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by_admin = models.BooleanField(default=True, blank=True, null=True, verbose_name='Creado por Admin')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id']

    def __str__(self):
        return f"Perfil de {self.usuario.username}"