import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from phonenumber_field.modelfields import PhoneNumberField
from .managers import AccountManager
from django_countries.fields import CountryField


class Account(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_customer = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['first_name', 'last_name', ]

    objects = AccountManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Customer(models.Model):
    MALE = 'MALE'
    FEMALE = 'FEMALE'

    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    user = models.OneToOneField(Account, blank=True, null=True, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, blank=True)
    phone_numbers = ArrayField(PhoneNumberField(), blank=True, null=True)
    device = models.UUIDField(max_length=125, default=uuid.uuid4, unique=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}" if self.user else f"{self.device}"


class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')
    country = CountryField()
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.IntegerField()
    apartment_number = models.IntegerField(blank=True, null=True)
    postal_code = models.CharField(max_length=50)
