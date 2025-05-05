from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .admin import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),  # Usar el sitio de administración personalizado
    path('', include('core.urls')),
    path('admin-panel/', include('admin_panel.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 