from django.db import models
from perfiles.models import Perfil

class Log(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to='logs')
    is_correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)