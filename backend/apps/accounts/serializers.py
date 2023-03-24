from rest_framework import serializers
from .models import Customer, CustomerAddress
from django.contrib.auth import get_user_model

Account = get_user_model()


class AccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', )


class AddressesSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='country.name')

    class Meta:
        model = CustomerAddress
        exclude = ('id', 'customer')


class CustomerSerializer(serializers.ModelSerializer):
    user = AccountSerializer()
    sex = serializers.CharField(source='get_sex_display')
    addresses = AddressesSerializer(many=True, read_only=True)
    device = serializers.UUIDField(read_only=True)
    phone_numbers = serializers.ListField(child=serializers.CharField(), read_only=True)

    class Meta:
        model = Customer
        fields = ('user', 'phone_numbers', 'sex', 'date_of_birth',
                  'addresses', 'device', )

    def update(self, instance, validated_data):
        user_data = validated_data.get('user')
        if user_data:
            user_serializer = AccountSerializer(instance.user, data=user_data, partial=self.partial)
            if user_serializer.is_valid():
                user_serializer.save()
        instance.sex = validated_data.get("get_sex_display", instance.sex)
        instance.date_of_birth = validated_data.get("date_of_birth", instance.date_of_birth)
        return instance
