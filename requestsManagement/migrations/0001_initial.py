# Generated by Django 5.0.3 on 2024-03-31 23:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('postgraduateManagement', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoSolicitud',
            fields=[
                ('codigo', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoContable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('fecha_solicitud', models.DateField(auto_now_add=True)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('espacio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postgraduateManagement.espacio')),
                ('estado_solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requestsManagement.estadosolicitud')),
                ('programa', models.ManyToManyField(to='postgraduateManagement.programa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postgraduateManagement.usuario')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contable',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('fecha_solicitud', models.DateField(auto_now_add=True)),
                ('presupuesto', models.IntegerField()),
                ('cuenta_cobro', models.CharField(max_length=50)),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postgraduateManagement.docente')),
                ('programa', models.ManyToManyField(to='postgraduateManagement.programa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postgraduateManagement.usuario')),
                ('estado_solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requestsManagement.estadosolicitud')),
                ('tipo_contable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requestsManagement.tipocontable')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
