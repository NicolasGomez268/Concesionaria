from django.shortcuts import render, get_object_or_404
from vehiculos.models import Vehiculo
from django.db.models import Q

def home(request):
    vehiculos_destacados = Vehiculo.objects.filter(activo=True).order_by('-fecha_creacion')[:4]
    return render(request, 'core/home.html', {
        'vehiculos_destacados': vehiculos_destacados
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
