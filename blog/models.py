from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(
        max_length=160,
        blank=True,  # Разрешаем пустое значение
        default='',  # Значение по умолчанию
        verbose_name='Описание (до 160 символов)',
        help_text='Краткое описание для SEO и превью в соцсетях'
    )
    content = RichTextField(config_name='awesome_ckeditor')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='static/images/')
    image_min = models.FileField(upload_to='static/images/')
    alt = models.CharField(max_length=30)
    categories = models.ManyToManyField('Category', related_name='posts')
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['order', '-created_on']  # Сначала по order, затем по дате

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
