# Generated by Django 4.2.5 on 2023-10-02 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_usuario_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
