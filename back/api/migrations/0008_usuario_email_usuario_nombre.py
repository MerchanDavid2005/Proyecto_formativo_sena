# Generated by Django 4.2.3 on 2023-10-04 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_pedido_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
