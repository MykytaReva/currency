# Generated by Django 4.0.6 on 2022-08-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='base_currency_type',
            field=models.CharField(choices=[('UAH', 'Hrivna'), ('USD', 'Dollar'), ('EUR', 'Euro'), ('BTC', 'Bitcoin')], default='UAH', max_length=3),
        ),
        migrations.AlterField(
            model_name='rate',
            name='currency_type',
            field=models.CharField(choices=[('UAH', 'Hrivna'), ('USD', 'Dollar'), ('EUR', 'Euro'), ('BTC', 'Bitcoin')], default='USD', max_length=3),
        ),
    ]
