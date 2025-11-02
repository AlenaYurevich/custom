from django.contrib import sitemaps
from django.urls import reverse


class NatalyStaticSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return ['home', 'catalog']

    def location(self, item):
        return reverse(item)


sitemaps = {
    'static': NatalyStaticSitemap,
    }
