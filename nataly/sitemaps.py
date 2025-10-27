from django.contrib import sitemaps
from django.urls import reverse
# from .models import YourModel  # ваши модели


class NatalyStaticSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return ['home', 'catalog']

    def location(self, item):
        return reverse(item)

# class NatalyDynamicSitemap(sitemaps.Sitemap):
#     changefreq = 'weekly'
#     priority = 0.7
#
#     def items(self):
#         return YourModel.objects.all()
#
#     def lastmod(self, obj):
#         return obj.updated_date
