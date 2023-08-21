from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=25, verbose_name='наименование')
    description = models.CharField(max_length=255, verbose_name='описание')
    preview = models.ImageField(upload_to='products/', verbose_name='превью', null=True)
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
