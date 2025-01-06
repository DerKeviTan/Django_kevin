# Generated by Django 4.2.4 on 2024-12-03 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('identificacion', models.CharField(max_length=10)),
                ('apellido', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
                ('nacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
    ]
