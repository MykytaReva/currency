# Generated by Django 4.0.6 on 2022-11-07 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_alter_rate_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responselog',
            name='ip',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='responselog',
            name='path',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='responselog',
            name='query_params',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='responselog',
            name='request_method',
            field=models.CharField(max_length=600),
        ),
    ]
