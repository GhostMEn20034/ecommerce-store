# Generated by Django 4.1.7 on 2023-03-21 17:34

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customer_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='phone_numbers',
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_numbers',
            field=django.contrib.postgres.fields.ArrayField(base_field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='customeraddress',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='addresses', to='accounts.customer'),
        ),
    ]
