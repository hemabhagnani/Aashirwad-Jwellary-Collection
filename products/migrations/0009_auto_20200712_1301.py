# Generated by Django 3.0.8 on 2020-07-12 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200712_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='braceletsdatabase',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='braceletsdatabase',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='braceletsdatabase',
            name='summary',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='earingsdatabase',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='earingsdatabase',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='earingsdatabase',
            name='summary',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='featuredproducts',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='featuredproducts',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='featuredproducts',
            name='summary',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='jewellarydatabase',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jewellarydatabase',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='jewellarydatabase',
            name='summary',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='necklessdatabase',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='necklessdatabase',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='necklessdatabase',
            name='summary',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='newtrends',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newtrends',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='newtrends',
            name='summary',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ringsdatabase',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ringsdatabase',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ringsdatabase',
            name='summary',
            field=models.TextField(null=True),
        ),
    ]
