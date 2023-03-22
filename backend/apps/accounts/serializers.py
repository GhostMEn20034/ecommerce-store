from rest_framework import serializers
from .models import Customer, CustomerAddress
from django.contrib.auth import get_user_model


Account = get_user_model()


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', )


class AddressesSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='country.name')

    class Meta:
        model = CustomerAddress
        exclude = ('id', 'customer')


class CustomerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', allow_null=True)
    first_name = serializers.CharField(source='user.first_name', allow_null=True)
    last_name = serializers.CharField(source='user.last_name', allow_null=True)
    sex = serializers.CharField(source='get_sex_display')
    addresses = AddressesSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ('email', 'first_name', 'last_name', 'phone_numbers', 'sex', 'date_of_birth',
                  'addresses', 'device', )
