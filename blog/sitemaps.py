from django.contrib import sitemaps
from django.urls import reverse
from .models import Post, Category, Tag  # ваши модели


class BlogStaticSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return ['blog_index']

    def location(self, item):
        return reverse(item)


class CategorySitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Category.objects.all().order_by('id')  # или 'name', 'order' и т.д.

    def lastmod(self, obj):
        # Возвращаем дату последнего поста в этой категории
        last_post = obj.posts.order_by('-last_modified').first()
        return last_post.last_modified if last_post else None

    def location(self, obj):
        return reverse('blog_category', kwargs={'category_slug': obj.slug})


class TagSitemap(sitemaps.Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return Tag.objects.all().order_by('id')  # или 'name', 'order' и т.д.

    def lastmod(self, obj):
        last_post = obj.posts.order_by('-last_modified').first()
        return last_post.last_modified if last_post else None

    def location(self, obj):
        return reverse('posts_by_tag', kwargs={'tag_slug': obj.slug})


class BlogDynamicSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Post.objects.all().order_by('-created_on')

    def lastmod(self, obj):
        return obj.last_modified  # используем ваше существующее поле


sitemaps = {
    'blog_static': BlogStaticSitemap,
    'blog_categories': CategorySitemap,
    'blog_tags': TagSitemap,
    'blog_posts': BlogDynamicSitemap,
}
