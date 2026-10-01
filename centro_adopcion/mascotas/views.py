from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Mascota

# Catálogo visible para todos
class MascotaList(ListView):
    model = Mascota

class MascotaDetail(DetailView):
    model = Mascota

# Restricción: solo admins
class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class MascotaCreate(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Mascota
    fields = ['nombre', 'especie', 'edad', 'descripcion', 'estado']
    success_url = reverse_lazy('catalogo')

class MascotaUpdate(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Mascota
    fields = ['estado']  # Solo cambiar estado
    success_url = reverse_lazy('catalogo')

class MascotaDelete(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Mascota
    success_url = reverse_lazy('catalogo')

# Create your views here.
