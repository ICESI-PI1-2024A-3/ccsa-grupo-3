# Generated by Django 5.0.3 on 2024-03-13 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postgraduateManagement', '0005_alter_espacio_id_subespacio_alter_espacio_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacio',
            name='id_subespacio',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
