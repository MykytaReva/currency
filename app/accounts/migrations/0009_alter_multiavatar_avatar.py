# Generated by Django 4.0.6 on 2022-09-21 15:23

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_multiavatar_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multiavatar',
            name='avatar',
            field=models.FileField(blank=True, upload_to=accounts.models.user_avatar),
        ),
    ]