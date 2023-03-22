from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Category, Product, Facet


@admin.register(Category)
class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)
    readonly_fields = ["slug", ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Facet)
class FacetAdmin(admin.ModelAdmin):
    pass
