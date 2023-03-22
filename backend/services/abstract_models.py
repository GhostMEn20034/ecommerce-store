from django.db import models
from apps.products.models import Product


class OrderItemAndCartItemModel(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_option = models.IntegerField(default=0, null=True)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
