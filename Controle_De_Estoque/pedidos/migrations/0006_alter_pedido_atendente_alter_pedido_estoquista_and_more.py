# Generated by Django 4.0.3 on 2022-05-31 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
        ('pedidos', '0005_rename_catagoria_pedido_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='Atendente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='worker.worker'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='Estoquista',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='nr_pedido',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
