# Generated by Django 5.0.4 on 2024-04-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postgraduateManagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='docente',
        ),
        migrations.AddField(
            model_name='materia',
            name='docente',
            field=models.ManyToManyField(to='postgraduateManagement.docente'),
        ),
        migrations.DeleteModel(
            name='DocentesCursos',
        ),
    ]