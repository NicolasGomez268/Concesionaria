from django.shortcuts import render
from .models import Vehiculo

# Create your views here.

def ver_todos_vehiculos(request):
    vehiculos = Vehiculo.objects.filter(activo=True).order_by('-fecha_creacion')
    return render(request, 'vehiculos/todos.html', {'vehiculos': vehiculos})
