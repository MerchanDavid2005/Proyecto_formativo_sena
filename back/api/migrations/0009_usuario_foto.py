# Generated by Django 4.2.3 on 2023-10-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_usuario_email_usuario_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(default=1, upload_to='usuarios/'),
            preserve_default=False,
        ),
    ]