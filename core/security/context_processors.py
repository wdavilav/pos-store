from datetime import datetime

from core.security.models import Dashboard


def site_settings(request):
    return {
        'date_joined': datetime.now().date(),
        'dashboard': Dashboard.objects.first()
    }
