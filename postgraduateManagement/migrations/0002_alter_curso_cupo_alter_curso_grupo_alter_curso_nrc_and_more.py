# Generated by Django 4.2.11 on 2024-05-05 16:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postgraduateManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='cupo',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='curso',
            name='grupo',
            field=models.CharField(max_length=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nrc',
            field=models.CharField(max_length=6, primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='materia',
            name='creditos',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)]),
        ),
    ]