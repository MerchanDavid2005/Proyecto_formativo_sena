# Generated by Django 4.1.7 on 2023-09-24 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='img',
            field=models.ImageField(default=1, upload_to='productos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicio',
            name='img',
            field=models.ImageField(default=1, upload_to='servicios'),
            preserve_default=False,
        ),
    ]
