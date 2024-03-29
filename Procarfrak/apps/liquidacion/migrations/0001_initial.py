# Generated by Django 4.2.1 on 2023-09-20 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conductor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liquidacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=20)),
                ('date', models.DateField()),
                ('amount', models.FloatField()),
                ('estadoL', models.CharField(blank=True, choices=[('al día', 'Al día'), ('pendiente', 'Pendiente')], max_length=10, null=True)),
                ('conductor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='conductor.conductor')),
            ],
        ),
    ]
