# Generated by Django 4.1 on 2024-09-09 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0012_remove_detalleventa_valorunitario'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleventa',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
