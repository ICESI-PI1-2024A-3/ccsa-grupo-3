# Generated by Django 5.0.4 on 2024-04-29 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postgraduateManagement', '0002_viatico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='telefono',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='docente',
            name='telefono',
            field=models.CharField(max_length=16),
        ),
    ]