# Generated by Django 4.2.3 on 2023-08-14 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado_Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('estado_vehiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehiculo.estado_vehiculo')),
            ],
        ),
    ]
