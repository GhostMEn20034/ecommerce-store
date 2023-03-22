from django.db import models
from apps.accounts.models import Customer
from services.generate_random_token import generate_random_number
from django.core.validators import MaxValueValidator
from services.abstract_models import OrderItemAndCartItemModel

length = 13


def generate_random_public_id():
    public_id = generate_random_number(length)
    if Cart.objects.filter(public_id=public_id).exists():
        public_id = generate_random_public_id()

    return public_id


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    public_id = models.CharField(default=generate_random_public_id, max_length=13)
    total = models.IntegerField(validators=[MaxValueValidator(99999), ], default=0)
    current = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class CartItem(OrderItemAndCartItemModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
