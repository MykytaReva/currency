# Generated by Django 4.0.6 on 2022-11-01 09:06

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_alter_useravatar_u_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useravatar',
            name='u_avatar',
            field=models.FileField(default='icons/anonymous.png', upload_to=accounts.models.user_avatar),
        ),
    ]