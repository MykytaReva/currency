# Generated by Django 4.0.6 on 2022-09-25 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_useravatar_u_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useravatar',
            name='u_id',
            field=models.ForeignKey(blank=True,
                                    null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]
