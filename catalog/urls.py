from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, products

app_name = CatalogConfig.name

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('products/', products)
]