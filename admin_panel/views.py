from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from vehiculos.models import Vehiculo, ImagenVehiculo
from vehiculos.forms import VehiculoForm

# Create your views here.

@login_required
def dashboard(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'admin_panel/dashboard.html', {
        'vehiculos': vehiculos
    })

@login_required
def vehiculo_create(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES)
        if form.is_valid():
            vehiculo = form.save()
            imagenes = request.FILES.getlist('imagenes')
            
            # Procesar imágenes adicionales
            for idx, imagen in enumerate(imagenes[:7]):
                try:
                    ImagenVehiculo.objects.create(
                        vehiculo=vehiculo,
                        imagen=imagen,
                        orden=idx
                    )
                except Exception as e:
                    messages.warning(request, f'Error al procesar una imagen: {str(e)}')
                    continue
            
            messages.success(request, 'Vehículo creado correctamente')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = VehiculoForm()
    return render(request, 'admin_panel/vehiculo_form.html', {'form': form})

@login_required
def vehiculo_edit(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES, instance=vehiculo)
        if form.is_valid():
            vehiculo = form.save()
            imagenes = request.FILES.getlist('imagenes')
            
            if imagenes:
                # Eliminar imágenes anteriores si se suben nuevas
                vehiculo.imagenes.all().delete()
                
                # Procesar nuevas imágenes
                for idx, imagen in enumerate(imagenes[:7]):
                    try:
                        ImagenVehiculo.objects.create(
                            vehiculo=vehiculo,
                            imagen=imagen,
                            orden=idx
                        )
                    except Exception as e:
                        messages.warning(request, f'Error al procesar una imagen: {str(e)}')
                        continue
            
            messages.success(request, 'Vehículo actualizado correctamente')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'admin_panel/vehiculo_form.html', {'form': form, 'vehiculo': vehiculo})

@login_required
def vehiculo_delete(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        try:
            vehiculo.activo = False
            vehiculo.save()
            messages.success(request, 'Vehículo desactivado correctamente')
            return redirect('admin_dashboard')
        except Exception as e:
            messages.error(request, f'Error al desactivar el vehículo: {str(e)}')
    return render(request, 'admin_panel/vehiculo_confirm_delete.html', {
        'vehiculo': vehiculo
    })

@login_required
def delete_imagen(request, imagen_id):
    if request.method == 'POST':
        try:
            imagen = ImagenVehiculo.objects.get(id=imagen_id)
            vehiculo_id = imagen.vehiculo.id
            imagen.delete()
            return JsonResponse({'status': 'success'})
        except ImagenVehiculo.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Imagen no encontrada'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)
