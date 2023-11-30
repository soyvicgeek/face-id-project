from django.urls import path
from . import views

urlpatterns = [
    path('', views.UsuarioListView.as_view(), name='usuarios_list'),
    path('new/', views.UsuarioCreateView.as_view(), name='usuario_new'),
    path('update/<pk>/', views.UsuarioUpdateView.as_view(), name='usuario_update'),
    path('delete/<pk>/', views.UsuarioDeleteView.as_view(), name='usuario_delete')
]