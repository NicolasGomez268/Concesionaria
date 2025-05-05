from django.shortcuts import render, get_object_or_404
from vehiculos.models import Vehiculo
from django.db.models import Q

def home(request):
    vehiculos = Vehiculo.objects.filter(activo=True)
    
    # Aplicar filtros
    marca = request.GET.get('marca')
    modelo = request.GET.get('modelo')
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')
    
    if marca:
        vehiculos = vehiculos.filter(marca__icontains=marca)
    if modelo:
        vehiculos = vehiculos.filter(modelo__icontains=modelo)
    if precio_min:
        vehiculos = vehiculos.filter(precio__gte=precio_min)
    if precio_max:
        vehiculos = vehiculos.filter(precio__lte=precio_max)
    
    return render(request, 'core/home.html', {
        'vehiculos': vehiculos,
        'filtros': {
            'marca': marca,
            'modelo': modelo,
            'precio_min': precio_min,
            'precio_max': precio_max,
        }
    })

def vehiculo_detail(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk, activo=True)
    return render(request, 'core/vehiculo_detail.html', {
        'vehiculo': vehiculo
    })

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')
