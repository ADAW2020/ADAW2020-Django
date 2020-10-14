# Generated by Django 3.1.2 on 2020-10-14 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotelApp1', '0002_auto_20201014_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administradores',
            fields=[
                ('nombre', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('dni_admin', models.IntegerField(max_length=250, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('nombre', models.CharField(max_length=250)),
                ('apellido', models.CharField(max_length=250)),
                ('dni', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('telefono', models.IntegerField()),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('numero', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='reservas',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='reservas',
            name='id',
        ),
        migrations.AddField(
            model_name='reservas',
            name='codigo_reserva',
            field=models.IntegerField(default=1, max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='reservas',
            name='estado',
            field=models.CharField(default='activa', max_length=250),
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
        migrations.AddField(
            model_name='reservas',
            name='dni_cliente',
            field=models.ForeignKey(default=12187427, on_delete=django.db.models.deletion.CASCADE, to='hotelApp1.clientes'),
        ),
        migrations.AddField(
            model_name='reservas',
            name='numero_habitacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hotelApp1.habitacion'),
        ),
    ]
