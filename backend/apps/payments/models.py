from django.db import models
from apps.orders.models import Order


class Payment(models.Model):
    UNPAID = 'UNPAID'
    HANDLING = 'HANDLING'
    PAID = 'PAID'

    PAYMENT_STATUS_CHOICES = [
        (UNPAID, 'Unpaid'),
        (HANDLING, 'Handling'),
        (PAID, 'Paid'),
    ]

    order = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    provider = models.CharField(max_length=60)
    payment_status = models.CharField(max_length=60, choices=PAYMENT_STATUS_CHOICES, default=UNPAID)
    transaction_id = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
