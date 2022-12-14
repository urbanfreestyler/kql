# Generated by Django 3.2 on 2022-02-24 07:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_alter_socialmedia_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='icon',
            field=models.FileField(default=None, help_text='Эта иконка будет отображаться на сайте. Нажав на эту иконку, пользователь будет отправлен по ссылке.', upload_to='icons/%Y%m%d/', validators=[django.core.validators.FileExtensionValidator(['svg', 'png', 'jpg', 'jpeg'])], verbose_name='Иконка соц. сети'),
        ),
    ]
