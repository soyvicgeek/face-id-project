from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.listar_usuario, name='usuario_list'),
    path('usuarios-new/', views.agregar_usuario, name='usuario_new'),
    path('usuarios-update/<id>', views.actualizar_usuario, name='usuario_update'),
    path('usuarios-delete/<id>', views.eliminar_usuario, name='usuario_delete')
]