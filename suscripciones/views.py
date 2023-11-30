from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from suscripciones.models import Suscripcion
from suscripciones.forms import SuscripcionForm

class SuscripcionListView(ListView):
    template_name = 'subs_list.html'
    model = Suscripcion
    context_object_name = 'subs'
    paginate_by = 5

class SuscripcionCreateView(CreateView):
    form_class = SuscripcionForm
    template_name = 'sub_new.html'
    success_url = reverse_lazy('subs_list')

class SuscripcionUpdateView(UpdateView):
    template_name = 'sub_update.html'
    model = Suscripcion
    fields = ['nombre','descripcion','costo','capacidad','estado']
    success_url = reverse_lazy('subs_list')

class SuscripcionDeleteView(DeleteView):
    template_name = 'sub_delete.html'
    model = Suscripcion
    context_object_name = 'sub'
    success_url = reverse_lazy('subs_list')