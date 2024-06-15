# Generated by Django 5.0.6 on 2024-06-15 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YearlyWeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100)),
                ('parameter', models.CharField(max_length=100)),
                ('year', models.IntegerField(unique=True)),
                ('jan', models.FloatField(blank=True, null=True)),
                ('feb', models.FloatField(blank=True, null=True)),
                ('mar', models.FloatField(blank=True, null=True)),
                ('apr', models.FloatField(blank=True, null=True)),
                ('may', models.FloatField(blank=True, null=True)),
                ('jun', models.FloatField(blank=True, null=True)),
                ('jul', models.FloatField(blank=True, null=True)),
                ('aug', models.FloatField(blank=True, null=True)),
                ('sep', models.FloatField(blank=True, null=True)),
                ('oct', models.FloatField(blank=True, null=True)),
                ('nov', models.FloatField(blank=True, null=True)),
                ('dec', models.FloatField(blank=True, null=True)),
                ('win', models.FloatField(blank=True, null=True)),
                ('spr', models.FloatField(blank=True, null=True)),
                ('sum', models.FloatField(blank=True, null=True)),
                ('aut', models.FloatField(blank=True, null=True)),
                ('ann', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]