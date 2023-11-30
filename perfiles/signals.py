from django.contrib.auth.models import User, Group
from .models import Perfil
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.perfil.save()

@receiver(post_save, sender=Perfil)
def add_user_to_clients_group(sender, instance, created, **kwargs):
    if created:
        try:
            clients = Group.objects.get(name='cliente')
        except Group.DoesNotExist:
            clients = Group.objects.create(name='cliente')
            clients = Group.objects.create(name='suscriptor')
            clients = Group.objects.create(name='administrador')
        instance.usuario.groups.add(clients)