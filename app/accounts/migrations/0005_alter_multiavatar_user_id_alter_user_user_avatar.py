# Generated by Django 4.0.6 on 2022-09-21 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_multiavatar_user_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multiavatar',
            name='user_id',
            field=models.ForeignKey(blank=True,
                                    null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_avatar',
            field=models.ForeignKey(blank=True,
                                    null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to='accounts.multiavatar'),
        ),
    ]
