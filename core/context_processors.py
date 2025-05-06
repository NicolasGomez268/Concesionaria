from django.conf import settings
 
def whatsapp_number(request):
    return {
        'WHATSAPP_NUMBER': getattr(settings, 'WHATSAPP_NUMBER', ''),
        'WHATSAPP_DISPLAY': getattr(settings, 'WHATSAPP_DISPLAY', ''),
    } 