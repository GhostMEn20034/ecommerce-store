# Generated by Django 4.1.7 on 2023-03-17 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='facets',
            name='type',
        ),
        migrations.AddField(
            model_name='facets',
            name='data_type',
            field=models.CharField(choices=[('string', 'string'), ('number', 'number'), ('boolean', 'boolean'), ('array', 'array'), ('object', 'object')], default=2, max_length=50),
            preserve_default=False,
        ),
    ]
