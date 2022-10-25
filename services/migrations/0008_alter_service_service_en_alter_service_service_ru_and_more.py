# Generated by Django 4.0.2 on 2022-02-23 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_rename_desciption_en_service_description_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_en',
            field=models.CharField(default=None, max_length=120, verbose_name='Название услуги (EN)'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_ru',
            field=models.CharField(default=None, max_length=120, verbose_name='Название услуги (RU)'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_uz',
            field=models.CharField(default=None, max_length=120, verbose_name='Название услуги (UZ)'),
        ),
    ]