# Generated by Django 4.0.2 on 2022-02-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_alter_phone_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Номер телефона'),
        ),
    ]
