# Generated by Django 5.0.6 on 2024-06-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yearlyweatherdata',
            name='year',
            field=models.IntegerField(),
        ),
    ]
