# Generated by Django 3.0.8 on 2020-07-17 02:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20200717_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='braceletsdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 2, 14, 49, 923607, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='earingsdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 2, 14, 49, 924735, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='featuredproducts',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 2, 14, 49, 921931, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='jewellarydatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 2, 14, 49, 924170, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='necklessdatabase',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reviewdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 2, 14, 49, 925863, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ringsdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 2, 14, 49, 922550, tzinfo=utc)),
        ),
    ]