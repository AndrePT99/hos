# Generated by Django 4.1 on 2024-09-05 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modulos', '0008_alter_usuario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol_idrol',
            field=models.ForeignKey(db_column='rol_idRol', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='modulos.rol'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user',
            field=models.ForeignKey(db_column='user_id', default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
