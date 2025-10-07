from django.contrib import admin
from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Что показывать в списке
    # Запрещаем удаление существующей записи (чтобы не остаться без настроек)

    def has_delete_permission(self, request, obj=None):
        return False

    # Запрещаем добавлять новые записи (нам нужна только одна)

    def has_add_permission(self, request):
        # Если запись уже существует, добавление новой запрещено
        return not SiteSettings.objects.exists()
