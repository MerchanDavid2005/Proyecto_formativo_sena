# Generated by Django 4.2.5 on 2023-10-01 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_producto_img_alter_servicio_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(default='Cliente', max_length=50),
        ),
    ]
