# Generated by Django 4.0.3 on 2022-05-31 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0008_alter_pedido_nr_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtopedido',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
    ]
