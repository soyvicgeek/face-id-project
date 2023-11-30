from django.db import models

class Suscripcion(models.Model):
    nombre = models.CharField(max_length=30, unique=True, blank=False, null=False)
    descripcion = models.TextField(default='Descripción de la Suscripción', blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=True)
    imagen = models.ImageField(default='default.jpg', upload_to='photos', blank=True, null=True)
    estado = models.BooleanField(default=True, blank=True)
    capacidad = models.PositiveIntegerField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Suscripción'
        verbose_name_plural = 'Suscripciones'
        ordering = ['-id']

    def __str__(self):
        return f"Suscripción {self.nombre}"