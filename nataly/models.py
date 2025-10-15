from django.db import models


class SiteSettings(models.Model):
    # Название настроек (для удобства в админке)
    objects = None
    name = models.CharField(
        max_length=100,
        default="Настройки сайта",
        verbose_name="Название"
    )

    # Ваши параметры
    working_hours_per_month = models.PositiveIntegerField(
        default=168,
        verbose_name="Количество рабочих часов в месяц"
    )
    average_salary_per_month = models.PositiveIntegerField(
        default=3600,
        verbose_name="Средняя заработная плата в месяц, рублей"
    )
    professional_income_tax = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=10.0,
        verbose_name="Налог на профессиональный доход, %"
    )
    rent_per_month = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=330.0,
        verbose_name="Арендная плата в месяц, рублей"
    )
    utilities_per_month = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=90.0,
        verbose_name="Коммунальные платежи в месяц, рублей"
    )
    equipment_cost = models.PositiveIntegerField(
        default=2000,
        verbose_name="Стоимость оборудования, рублей"
    )
    equipment_lifespan_months = models.PositiveIntegerField(
        default=96,
        verbose_name="Срок службы оборудования, мес."
    )
    materials_per_month = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=20.0,
        verbose_name="Материалы в месяц, рублей"
    )
    advertising_per_month = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=20.0,
        verbose_name="Реклама в месяц, рублей"
    )

    class Meta:
        verbose_name = "настройки сайта"
        verbose_name_plural = "настройки сайта"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Этот метод гарантирует, что будет создана только ОДНА запись.
        if not self.pk and SiteSettings.objects.exists():
            # Если запись уже есть и это попытка создать новую, не даем этого сделать.
            return
        super().save(*args, **kwargs)
