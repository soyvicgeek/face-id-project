from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from perfiles.models import Perfil
#from perfil.forms import UsuarioForm

class UsuarioListView(ListView):
    template_name = 'usuarios/usuarios_list.html'
    model = Perfil
    context_object_name = 'usuarios'
    paginate_by = 5
'''
class UsuarioCreateView(CreateView):
    form_class = UsuarioForm
    template_name = 'usuarios/usuario_new.html'
    success_url = reverse_lazy('usuarios:usuario_list')

class UsuarioUpdateView(UpdateView):
    template_name = 'usuarios/usuario_update.html'
    model = Usuario
    #fields = ['nombre_corto', 'descuento']
    success_url = reverse_lazy('usuarios:usuario_list')

class UsuarioDeleteView(DeleteView):
    template_name = 'usuarios/usuario_delete.html'
    model = Usuario
    #fields = ['nombre_corto', 'descuento']
    success_url = reverse_lazy('usuarios:usuario_list')
'''
