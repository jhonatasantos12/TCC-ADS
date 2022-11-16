# Generated by Django 4.0.5 on 2022-11-02 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('worker', '0003_worker_usuario'),
        ('pedidos', '0014_rename_nr_pedido_pedido_tp_pedido_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoEntrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('Atendente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='worker.worker')),
                ('Status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pedidos.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='ProdutoEntrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=0)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pedidos.pedidoentrada')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
            ],
        ),
    ]
