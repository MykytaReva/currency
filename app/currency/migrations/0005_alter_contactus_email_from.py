# Generated by Django 4.0.6 on 2022-08-21 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0004_responselog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='email_from',
            field=models.EmailField(default='testemail@gmail.com', max_length=60),
        ),
    ]
