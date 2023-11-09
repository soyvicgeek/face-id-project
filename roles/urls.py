from django.urls import path
from . import views

urlpatterns = [
    path('roles/', views.listar_usuario, name='rol_list'),
    path('rol-new/', views.agregar_usuario, name='rol_new'),
    path('rol-update/<id>', views.actualizar_usuario, name='rol_update'),
    path('rol-delete/<id>', views.eliminar_usuario, name='rol_delete')
]