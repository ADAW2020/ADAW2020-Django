# Generated by Django 3.1.1 on 2020-11-20 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelApp1', '0002_auto_20201120_2203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservas',
            old_name='dias',
            new_name='cant_dias',
        ),
    ]
