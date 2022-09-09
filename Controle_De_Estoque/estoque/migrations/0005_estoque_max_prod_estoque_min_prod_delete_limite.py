# Generated by Django 4.0.5 on 2022-09-09 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0004_limite_id_estoque_alter_limite_max_prod_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoque',
            name='max_prod',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='estoque',
            name='min_prod',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.DeleteModel(
            name='Limite',
        ),
    ]
