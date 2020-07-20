# Generated by Django 3.0.8 on 2020-07-17 01:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20200716_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='braceletsdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 1, 53, 36, 394599, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='earingsdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 1, 53, 36, 395900, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='featuredproducts',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 1, 53, 28, 817422, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='jewellarydatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 1, 53, 36, 395203, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='necklessdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 1, 53, 28, 819188, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reviewdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 1, 53, 36, 397065, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ringsdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 1, 53, 28, 818379, tzinfo=utc)),
        ),
    ]