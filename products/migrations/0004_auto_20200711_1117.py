# Generated by Django 3.0.8 on 2020-07-11 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200711_1107'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='bracelets',
            new_name='braceletsdatabase',
        ),
        migrations.RenameModel(
            old_name='neckless',
            new_name='necklessdatabase',
        ),
        migrations.RenameModel(
            old_name='rings',
            new_name='ringsdatabase',
        ),
    ]
