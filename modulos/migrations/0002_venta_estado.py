# Generated by Django 4.1 on 2024-09-04 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='estado',
            field=models.CharField(default='activa', max_length=10),
        ),
    ]
