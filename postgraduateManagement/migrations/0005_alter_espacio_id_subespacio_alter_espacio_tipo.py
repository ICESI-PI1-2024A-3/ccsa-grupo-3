# Generated by Django 5.0.3 on 2024-03-13 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postgraduateManagement', '0004_espacio_capacidad_espacio_id_subespacio_espacio_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacio',
            name='id_subespacio',
            field=models.CharField(blank=True, default='00', max_length=2),
        ),
        migrations.AlterField(
            model_name='espacio',
            name='tipo',
            field=models.CharField(default='Salon', max_length=24),
        ),
    ]
