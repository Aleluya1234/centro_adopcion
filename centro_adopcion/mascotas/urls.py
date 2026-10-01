from django.urls import path
from .views import MascotaList, MascotaDetail, MascotaCreate, MascotaUpdate, MascotaDelete

urlpatterns = [
    path('', MascotaList.as_view(), name='catalogo'),
    path('<int:pk>/', MascotaDetail.as_view(), name='detalle'),
    path('crear/', MascotaCreate.as_view(), name='crear'),
    path('editar/<int:pk>/', MascotaUpdate.as_view(), name='editar'),
    path('eliminar/<int:pk>/', MascotaDelete.as_view(), name='eliminar'),
]
