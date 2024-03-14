# Generated by Django 5.0.3 on 2024-03-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postgraduateManagement', '0003_remove_espacio_capacidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='espacio',
            name='capacidad',
            field=models.IntegerField(blank=True, default=30),
        ),
        migrations.AddField(
            model_name='espacio',
            name='id_subespacio',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='espacio',
            name='tipo',
            field=models.CharField(default='salon', max_length=24),
        ),
    ]