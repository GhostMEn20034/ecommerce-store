# Generated by Django 4.1.7 on 2023-03-17 16:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99999)]),
        ),
    ]
