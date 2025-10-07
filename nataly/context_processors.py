from .models import SiteSettings


def site_settings(request):
    # Пытаемся получить единственный объект настроек.
    # Если его нет, создаем его с значениями по умолчанию.
    settings, created = SiteSettings.objects.get_or_create(pk=1)
    return {'site_settings': settings}
