from django.contrib import admin
from .models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    readonly_fields = ['public_id', ]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass
