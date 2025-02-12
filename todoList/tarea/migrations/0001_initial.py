# Generated by Django 5.0.6 on 2024-06-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_vencimiento', models.DateField(blank=True, null=True)),
                ('completada', models.BooleanField(default=False)),
            ],
        ),
    ]
