# Generated by Django 3.2 on 2022-02-24 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteSettings', '0005_auto_20220224_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thirdblock',
            old_name='eader_en',
            new_name='header_en',
        ),
        migrations.RenameField(
            model_name='thirdblock',
            old_name='eader_uz',
            new_name='header_uz',
        ),
    ]