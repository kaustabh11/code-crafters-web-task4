# Generated by Django 4.0.2 on 2022-08-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='daily_cal',
            field=models.FloatField(default=0),
        ),
    ]
