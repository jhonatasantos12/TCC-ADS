# Generated by Django 3.1.6 on 2022-11-17 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20221115_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='valor',
        ),
    ]