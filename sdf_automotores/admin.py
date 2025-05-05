from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class SDFAdminSite(AdminSite):
    # Texto para el encabezado del sitio
    site_header = settings.ADMIN_SITE_HEADER
    # Texto para el título del sitio
    site_title = settings.ADMIN_SITE_TITLE
    # Texto para el título del índice
    index_title = settings.ADMIN_INDEX_TITLE

    def get_app_list(self, request):
        """
        Retorna una lista ordenada de todas las aplicaciones instaladas que el usuario
        tiene permiso para ver.
        """
        app_list = super().get_app_list(request)
        
        # Personalizar el orden de las aplicaciones
        app_list.sort(key=lambda x: x['name'])
        
        return app_list

# Crear una instancia del sitio de administración personalizado
admin_site = SDFAdminSite(name='admin')

# Registrar los modelos en el sitio de administración personalizado
from core.models import Vehiculo, ImagenVehiculo

@admin.register(Vehiculo, site=admin_site)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'anio', 'precio', 'estado', 'activo')
    list_filter = ('marca', 'estado', 'activo')
    search_fields = ('marca', 'modelo', 'descripcion')
    list_editable = ('activo',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

@admin.register(ImagenVehiculo, site=admin_site)
class ImagenVehiculoAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'imagen', 'orden')
    list_filter = ('vehiculo',)
    search_fields = ('vehiculo__marca', 'vehiculo__modelo') 