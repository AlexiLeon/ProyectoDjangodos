# Generated by Django 5.2.3 on 2025-06-20 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografia'),
        ),
    ]
