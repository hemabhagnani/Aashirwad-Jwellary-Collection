# Generated by Django 3.0.8 on 2020-07-17 01:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20200717_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='braceletsdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 1, 56, 30, 541522, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='earingsdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 1, 56, 30, 544499, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='featuredproducts',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 1, 56, 29, 781183, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='jewellarydatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 1, 56, 30, 542609, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='necklessdatabase',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='reviewdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 1, 56, 30, 546112, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ringsdatabase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 1, 56, 29, 787042, tzinfo=utc)),
        ),
    ]
