# Generated by Django 3.1.2 on 2020-10-23 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelApp1', '0016_auto_20201023_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservas',
            name='numero_habitacion',
        ),
        migrations.AlterField(
            model_name='reservas',
            name='codigo_reserva',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
