# Generated by Django 4.0.6 on 2022-08-30 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name_plural': 'ContactUs'},
        ),
        migrations.AlterModelOptions(
            name='rate',
            options={'verbose_name_plural': 'Rate'},
        ),
        migrations.AlterModelOptions(
            name='responselog',
            options={'verbose_name_plural': 'ResponseLog'},
        ),
        migrations.AlterModelOptions(
            name='source',
            options={'verbose_name_plural': 'Source'},
        ),
        migrations.AddField(
            model_name='source',
            name='code_name',
            field=models.CharField(default='PrivatBank', max_length=20, unique=True),
            preserve_default=False,
        ),
    ]