from django.db import models
from apps.accounts.models import Customer, CustomerAddress
from django.core.validators import MaxValueValidator
from services.generate_random_token import generate_random_number
from services.abstract_models import OrderItemAndCartItemModel

length = 9


def generate_order_number():
    order_number = generate_random_number(length)

    if Order.objects.filter(order_number=order_number).exists():
        order_number = generate_order_number()

    return order_number


class Order(models.Model):
    NEW_ORDER = 'NEW ORDER'
    HANDLING = 'HANDLING'
    TRANSFERRED_TO_THE_DS = 'TRANSFERRED TO THE DS'  # DS -- Delivery Service
    BEING_DELIVERED = 'BEING DELIVERED'
    WAITING_AT_THE_PP = 'WAITING FOR THE CLIENT AT THE PP'  # PP -- Pick-up Point
    COMPLETED = 'COMPLETED'

    DELIVERY_STATUS_CHOICES = [
        (NEW_ORDER, 'New order'),
        (HANDLING, 'Handling'),
        (TRANSFERRED_TO_THE_DS, 'Transferred to the delivery service'),
        (BEING_DELIVERED, 'Being delivered'),
        (WAITING_AT_THE_PP, 'Waiting for the client at the pick-up point'),
        (COMPLETED, 'Completed')
    ]

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    customer_address = models.ForeignKey(CustomerAddress, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=75)
    order_number = models.CharField(default=generate_order_number, max_length=9)
    total = models.IntegerField(validators=[MaxValueValidator(99999), ])
    delivery_status = models.CharField(choices=DELIVERY_STATUS_CHOICES, default=NEW_ORDER, max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class OrderItem(OrderItemAndCartItemModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
