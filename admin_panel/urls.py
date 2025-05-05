from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='admin_dashboard'),
    path('vehiculos/nuevo/', views.vehiculo_create, name='vehiculo_create'),
    path('vehiculos/<int:pk>/editar/', views.vehiculo_edit, name='vehiculo_edit'),
    path('vehiculos/<int:pk>/eliminar/', views.vehiculo_delete, name='vehiculo_delete'),
    path('vehiculos/imagen/<int:imagen_id>/delete/', views.delete_imagen, name='delete_imagen'),
] 