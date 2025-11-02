from django.contrib import sitemaps

try:
    from blog.sitemaps import sitemaps as blog_sitemaps
except ImportError:
    blog_sitemaps = {}

try:
    from nataly.sitemaps import sitemaps as nataly_sitemaps
except ImportError:
    nataly_sitemaps = {}

# Объединяем все sitemaps проекта
sitemaps = {}
sitemaps.update(nataly_sitemaps)
sitemaps.update(blog_sitemaps)
