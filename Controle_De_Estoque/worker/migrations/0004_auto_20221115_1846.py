# Generated by Django 3.1.6 on 2022-11-15 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0003_worker_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='data_registro',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
