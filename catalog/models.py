from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=25, verbose_name='наименование')
    description = models.CharField(max_length=255, verbose_name='описание')
    preview = models.ImageField(upload_to='products/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    production_data = models.DateField(verbose_name='дата создания', auto_now_add=True)
    change_data = models.DateField(verbose_name='дата последнешо изменения', auto_now=True)

    def __str__(self):
        return f'{self.product_name} ({self.description}): {self.price} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    category_name = models.CharField(max_length=25, verbose_name='наименование')
    description = models.CharField(max_length=255, verbose_name='описание')

    def __str__(self):
        return f'{self.category_name} ({self.description})'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Blog(models.Model):
    blog_title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug')
    contents = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='media/', verbose_name='Изображение', **NULLABLE)
    date_production = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    is_publication = models.BooleanField(verbose_name='Опубликовано', default=True)
    views_count = models.IntegerField(verbose_name='Просмотры', default=0)

    def __str__(self):
        return self.blog_title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
