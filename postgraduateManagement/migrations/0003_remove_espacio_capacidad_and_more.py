# Generated by Django 5.0.3 on 2024-03-13 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postgraduateManagement', '0002_alter_espacio_id_espacio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='espacio',
            name='capacidad',
        ),
        migrations.RemoveField(
            model_name='espacio',
            name='id_subespacio',
        ),
        migrations.RemoveField(
            model_name='espacio',
            name='tipo',
        ),
    ]
