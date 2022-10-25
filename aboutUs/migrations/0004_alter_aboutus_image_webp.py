# Generated by Django 4.0.2 on 2022-02-23 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutUs', '0003_aboutus_image_webp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='image_webp',
            field=models.ImageField(default=None, help_text='Важно! Загрузите картинку в формате .webp', upload_to='img/about/%Y%m%d/', verbose_name='Картинка'),
        ),
    ]