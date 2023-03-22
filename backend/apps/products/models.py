from django.db import models
from treebeard.mp_tree import MP_Node


class Category(MP_Node):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Facet(models.Model):
    FACET_DATA_TYPE_CHOICES = [
        ("string", "string"),
        ("number", "number"),
        ("boolean", "boolean"),
        ("array", "array"),
        ("object", "object"),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    data_type = models.CharField(max_length=50, choices=FACET_DATA_TYPE_CHOICES)
    is_sortable = models.BooleanField()
    is_filterable = models.BooleanField()


class Product(models.Model):
    name = models.CharField(max_length=125)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    has_options = models.BooleanField(default=False)
    product_facets = models.JSONField()
    product_services = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
