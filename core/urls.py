from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vehiculo/<int:pk>/', views.vehiculo_detail, name='vehiculo_detail'),
    path('sobre-nosotros/', views.about, name='about'),
    path('contacto/', views.contact, name='contact'),
] 