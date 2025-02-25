# Generated by Django 4.2.4 on 2024-12-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Matriculas', '0003_remove_curso_carrera_remove_curso_materia_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('decano', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=254)),
                ('iniciales', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
