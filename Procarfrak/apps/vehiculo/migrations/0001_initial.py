# Generated by Django 4.2.1 on 2023-09-20 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('estadoV', models.CharField(blank=True, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], max_length=10, null=True)),
            ],
        ),
    ]
