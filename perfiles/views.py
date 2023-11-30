from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from perfiles.models import Perfil
from perfiles.forms import UsuarioForm

class UsuarioListView(ListView):
    template_name = 'usuarios/usuarios_list.html'
    model = Perfil
    context_object_name = 'usuarios'
    paginate_by = 5

class UsuarioCreateView(CreateView):
    form_class = UsuarioForm
    template_name = 'usuarios/usuario_new.html'
    success_url = reverse_lazy('usuarios_list')

class UsuarioUpdateView(UpdateView):
    template_name = 'usuarios/usuario_update.html'
    model = User
    fields = ['username', 'email','is_active']
    success_url = reverse_lazy('usuarios_list')

class UsuarioDeleteView(DeleteView):
    template_name = 'usuarios/usuario_delete.html'
    model = User
    context_object_name = 'user'
    success_url = reverse_lazy('usuarios_list')
