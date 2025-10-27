from django.contrib import sitemaps
from django.urls import reverse
# from django.contrib.flatpages.sitemaps import FlatPageSitemap
# from nataly.models import YourModel  # импортируйте ваши модели


class StaticSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return [
            'home',  # имя URL из nataly/urls.py
            'catalog',
            # добавьте другие статические страницы
        ]

    def location(self, item):
        return reverse(item)


# class DynamicSitemap(sitemaps.Sitemap):
#     changefreq = 'weekly'
#     priority = 0.8
#
#     def items(self):
#         return YourModel.objects.filter(is_published=True)  # пример
#
#     def lastmod(self, obj):
#         return obj.updated_at  # поле с датой обновления


# Если используете flatpages
sitemaps = {
    'static': StaticSitemap,
    # 'dynamic': DynamicSitemap,
    # 'flatpages': FlatPageSitemap,
}
