# Configuración de autenticación
LOGIN_URL = 'admin:login'
LOGIN_REDIRECT_URL = 'admin_dashboard'
LOGOUT_REDIRECT_URL = 'home'

# Configuración del panel de administración
ADMIN_SITE_HEADER = "SDF Automóviles - Administración"
ADMIN_SITE_TITLE = "SDF Automóviles"
ADMIN_INDEX_TITLE = "Panel de Control"

INSTALLED_APPS = [
    # ... otras apps ...
    'django.contrib.humanize',
] 