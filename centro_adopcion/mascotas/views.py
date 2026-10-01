from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Mascota

class MascotaList(ListView):
    model = Mascota
    template_name = 'mascotas/catalogo.html'

class MascotaDetail(DetailView):
    model = Mascota
    template_name = 'mascotas/detalle.html'

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class MascotaCreate(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Mascota
    fields = ['nombre', 'especie', 'edad', 'descripcion', 'estado']
    template_name = 'mascotas/crear.html'
    success_url = reverse_lazy('catalogo')

class MascotaUpdate(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Mascota
    fields = ['estado']
    template_name = 'mascotas/editar.html'
    success_url = reverse_lazy('catalogo')

class MascotaDelete(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Mascota
    template_name = 'mascotas/eliminar.html'
    success_url = reverse_lazy('catalogo')
