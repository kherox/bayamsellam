# Generated by Django 2.0 on 2017-12-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrie',
            name='alpha2',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='countrie',
            name='alpha3',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='countrie',
            name='nom_en_gb',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='countrie',
            name='nom_fr_fr',
            field=models.CharField(max_length=250),
        ),
    ]
