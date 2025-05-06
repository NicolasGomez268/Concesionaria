from django.urls import path
from . import views
from vehiculos.views import ver_todos_vehiculos

urlpatterns = [
    path('', views.home, name='home'),
    path('vehiculo/<int:pk>/', views.vehiculo_detail, name='vehiculo_detail'),
    path('todos/', ver_todos_vehiculos, name='ver_todos_vehiculos'),
] 